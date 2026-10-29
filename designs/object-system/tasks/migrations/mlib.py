"""Shared harness for the mechanical M-row migrations (ALIGNMENT-PLAN.md, phase 3).

Every script edits text line by line so YAML Jazz comments survive, and a file is written only
when the edited text parses, has no new duplicate keys, and equals the data-level version of
the same change. Anything else is skipped with a reason, for an agent to do by hand.

Dry run by default: prints scanned / would change / skipped, a +/- line count per file, and
the full unified diff with --diff. --apply writes. --files limits the scope.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable

import yaml

HERE = Path(__file__).resolve().parent
MOOLLM = HERE.parents[3]
GIT = MOOLLM.parent
sys.path.insert(0, str(MOOLLM / "skills" / "prototype" / "scripts"))
try:
    import visibility  # type: ignore  # noqa: E402
except Exception:
    visibility = None
SKIP_DIRS = {".git", "node_modules", "temp", ".moollm", "dist", "build", "__pycache__"}
VIEWS = {"CARD.yml", "GLANCE.yml", "INDEX.yml"}


class Skip(Exception):
    """The file is left alone; the message is the reason, grouped in the report."""


class Dup(yaml.SafeLoader):
    pass


def _no_dups(loader: yaml.SafeLoader, node: yaml.MappingNode) -> dict:
    keys = [loader.construct_object(k, deep=True) for k, _ in node.value]
    hashable = [k for k in keys if isinstance(k, (str, int, float, bool, type(None)))]
    if len(hashable) != len(set(hashable)):
        raise ValueError(f"duplicate key at line {node.start_mark.line + 1}")
    return yaml.SafeLoader.construct_mapping(loader, node, deep=True)


Dup.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dups)


def has_dups(text: str) -> bool:
    try:
        yaml.load(text, Loader=Dup)
    except ValueError:
        return True
    except yaml.YAMLError:
        return False
    return False


def indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def is_content(line: str) -> bool:
    s = line.strip()
    return bool(s) and not s.startswith("#")


def block_end(lines: list[str], i: int) -> int:
    """Index after the block value of the key on line i (block scalars, maps, compact lists).

    Comment and blank lines only extend the block when content follows them, so a comment
    above the next key stays with that key.
    """
    h = indent(lines[i])
    j, last = i + 1, i + 1
    compact = None
    while j < len(lines):
        ln = lines[j]
        if is_content(ln):
            d = indent(ln)
            dash = ln.lstrip().startswith("-") and (ln.strip() == "-" or ln.lstrip()[1:2] == " ")
            if compact is None:
                compact = d == h and dash
            if d > h or (compact and d == h and dash):
                last = j + 1
            else:
                break
        j += 1
    return last


SCALAR_COMMENT = re.compile(r"^((?:\"(?:[^\"\\]|\\.)*\"|'(?:[^']|'')*'|[^#])*?)\s*(?:\s#\s?(.*))?$")


def split_comment(rest: str) -> tuple[str, str | None]:
    """'value  # note' -> ('value', 'note'). Quotes are respected."""
    m = SCALAR_COMMENT.match(rest)
    if not m:
        return rest.strip(), None
    value, comment = m.group(1).strip(), m.group(2)
    if rest.lstrip().startswith("#"):
        return "", rest.lstrip()[1:].strip()
    return value, comment


def single_line(lines: list[str], i: int, field_indent: int, end: int) -> bool:
    """The value of the field on line i fits on that line (no block scalar, no sub-block)."""
    rest = lines[i].split(":", 1)[1]
    value, _ = split_comment(rest)
    if not value or value[0] in "|>" or value[0] in "[{" and not value.endswith(("]", "}")):
        return False
    j = i + 1
    while j < end and not is_content(lines[j]):
        j += 1
    return j >= end or indent(lines[j]) <= field_indent


KEY_LINE = re.compile(r"^(\s*)(- +)?([^\s#\-][^:#]*?|\"[^\"]*\"|'[^']*')\s*:(\s|$)")
FIELD = re.compile(r"^(\s*)(- +)?([A-Za-z_][\w-]*)(\s*):(?=\s|$)")


def header_lines(lines: list[str], key: str) -> list[int]:
    """Lines `key:` with a block value (nothing after the colon but a comment)."""
    pat = re.compile(rf"^\s*{re.escape(key)}:\s*(#.*)?$")
    return [i for i, ln in enumerate(lines) if pat.match(ln)]


def flow_headers(lines: list[str], key: str) -> list[int]:
    pat = re.compile(rf"^\s*(- +)?{re.escape(key)}:\s*[\[{{]")
    return [i for i, ln in enumerate(lines) if pat.match(ln) and not re.match(rf"^\s*(- +)?{re.escape(key)}:\s*(\[\]|\{{\}})\s*(#.*)?$", ln)]


@dataclass
class Entry:
    start: int
    end: int
    form: str            # "map" or "list"
    key_indent: int      # indent of the map key or of the dash
    field_indent: int | None

    def fields(self, lines: list[str]) -> dict[str, int]:
        """Field name -> line index, for keys sitting exactly at this entry's field indent."""
        out: dict[str, int] = {}
        if self.field_indent is None:
            return out
        for i in range(self.start, self.end):
            m = FIELD.match(lines[i])
            if not m:
                continue
            if i == self.start and self.form == "list" and m[2]:
                out.setdefault(m[3], i)
            elif i > self.start and not m[2] and len(m[1]) == self.field_indent:
                out.setdefault(m[3], i)
        return out


def entries(lines: list[str], h: int, end: int) -> tuple[str, list[Entry]]:
    """The entries of the collection block whose header is line h."""
    body = [i for i in range(h + 1, end) if is_content(lines[i])]
    if not body:
        return "empty", []
    c = indent(lines[body[0]])
    form = "list" if lines[body[0]].lstrip().startswith("-") else "map"
    if form == "map" and c <= indent(lines[h]):
        raise Skip("collection block is mis-indented")
    starts = [i for i in body if indent(lines[i]) == c]
    for i in starts:
        if form == "list" and not lines[i].lstrip().startswith("-"):
            raise Skip(f"mixed list and map at line {i + 1}")
        if form == "map" and not KEY_LINE.match(lines[i]):
            raise Skip(f"unreadable entry key at line {i + 1}")
    out = []
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else end
        while e - 1 > s and not is_content(lines[e - 1]):
            e -= 1
        if form == "list":
            m = re.match(r"^(\s*)-( +)(\S)", lines[s])
            fi = len(m[1]) + 1 + len(m[2]) if m else None
            if fi is None:
                nxt = next((k for k in range(s + 1, e) if is_content(lines[k])), None)
                fi = indent(lines[nxt]) if nxt is not None else None
        else:
            nxt = next((k for k in range(s + 1, e) if is_content(lines[k]) and indent(lines[k]) > c), None)
            fi = indent(lines[nxt]) if nxt is not None else None
        out.append(Entry(s, e, form, c, fi))
    return form, out


def collection_blocks(lines: list[str], key: str) -> Iterable[tuple[int, int, str, list[Entry]]]:
    """Block-style `key:` collections. Flow-style ones are not edited; if the data change needs
    them, the result differs from the expected data and the file is skipped."""
    for h in header_lines(lines, key):
        end = block_end(lines, h)
        form, es = entries(lines, h, end)
        yield h, end, form, es


def rename_in_flow(line: str, mapping: dict[str, str]) -> tuple[str, list[str]]:
    """Rename keys at depth 1 of the one-line flow map on this line: `NAME: { does: x }`."""
    start = line.find("{")
    if start < 0:
        return line, []
    out, done, depth, quote, i = list(line[:start]), [], 0, None, start
    expect_key = False
    while i < len(line):
        ch = line[i]
        if quote:
            out.append(ch)
            if ch == quote and line[i - 1] != "\\":
                quote = None
            i += 1
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "{[":
            depth += 1
            expect_key = ch == "{" and depth == 1
            out.append(ch)
            i += 1
            continue
        elif ch in "}]":
            depth -= 1
        elif ch == "," and depth == 1:
            expect_key = True
            out.append(ch)
            i += 1
            continue
        elif ch == "#" and depth == 0 and line[i - 1] == " ":
            out.append(line[i:])
            break
        if expect_key and not ch.isspace():
            expect_key = False
            m = re.match(r"([A-Za-z_][\w-]*)(\s*):", line[i:])
            if m and m[1] in mapping:
                out.append(mapping[m[1]] + m[2] + ":")
                done.append(m[1])
                i += m.end()
                continue
        out.append(ch)
        i += 1
    return "".join(out), done


def rename_key_on_line(line: str, old: str, new: str) -> str:
    return re.sub(rf"^(\s*(?:- +)?){re.escape(old)}(\s*):", rf"\g<1>{new}\g<2>:", line, count=1)


def data_entries(data: Any, key: str, skip_paths: tuple[str, ...] = ()) -> Iterable[tuple[list[str], Any]]:
    """(path, collection value) for every `key:` in the data, at any depth."""
    def walk(v: Any, path: list[str]):
        if isinstance(v, dict):
            for k, x in v.items():
                if k == key and not (path and path[0] in skip_paths):
                    yield path, x
                yield from walk(x, path + [str(k)])
        elif isinstance(v, list):
            for x in v:
                yield from walk(x, path + ["[]"])
    yield from walk(data, [])


def entry_dicts(coll: Any) -> list[dict]:
    if isinstance(coll, dict):
        return [e for e in coll.values() if isinstance(e, dict)]
    if isinstance(coll, list):
        return [e for e in coll if isinstance(e, dict)]
    return []


def rename_entry_fields(lines: list[str], data: Any, collection: str, mapping: dict[str, str],
                        select: Callable[[dict], bool] = lambda e: True) -> tuple[list[str], Any, int]:
    """Rename fields inside the entries of every `collection:` block, in text and in a data copy.

    `select` picks which entries (by their parsed dict) are touched. A target already present
    in an entry, or two sources mapping to one target, is a Skip.
    """
    import copy
    expected = copy.deepcopy(data)
    for _, coll in data_entries(expected, collection):
        items = coll.items() if isinstance(coll, dict) else enumerate(coll) if isinstance(coll, list) else []
        for k, e in list(items):
            if not isinstance(e, dict) or not select(e):
                continue
            srcs = [s for s in mapping if s in e]
            for s in srcs:
                t = mapping[s]
                if t in e or sum(mapping[x] == t for x in srcs) > 1:
                    raise Skip(f"{collection} entry has both {s}: and {t}:" if t in e
                               else f"{collection} entry has two spellings of {t}:")
            if srcs:
                coll[k] = {mapping.get(f, f): v for f, v in e.items()}
    n = 0
    out = list(lines)
    for h, end, form, es in collection_blocks(lines, collection):
        if not es:
            continue
        snippet = "\n".join(ln[indent(lines[h]):] if ln.startswith(" " * indent(lines[h])) else ln
                            for ln in lines[h:end])
        try:
            parsed = yaml.safe_load(snippet)
        except yaml.YAMLError:
            raise Skip(f"{collection}: block at line {h + 1} does not parse alone")
        parsed = parsed.get(collection) if isinstance(parsed, dict) else None
        vals = list(parsed.values()) if isinstance(parsed, dict) else parsed if isinstance(parsed, list) else []
        if len(vals) != len(es):
            raise Skip(f"{collection}: block at line {h + 1}: entry count differs from parse")
        for e, v in zip(es, vals):
            if not isinstance(v, dict) or not select(v):
                continue
            if e.field_indent is None or (e.form == "list" and re.match(r"^\s*-\s+\{", lines[e.start])):
                if e.end - e.start == 1 and lines[e.start].rstrip().split(" #")[0].rstrip().endswith("}"):
                    out[e.start], done = rename_in_flow(lines[e.start], mapping)
                    n += len(done)
                continue
            for f, i in e.fields(lines).items():
                if f in mapping:
                    out[i] = rename_key_on_line(lines[i], f, mapping[f])
                    n += 1
    return out, expected, n


@dataclass
class Result:
    new_text: str | None
    expected: Any = None         # data the new text must parse to; None skips the check
    notes: list[str] | None = None


Transform = Callable[[Path, str, Any, argparse.Namespace], Result]


def repo_files(root: Path, repos: Iterable[str], pred: Callable[[Path, Path], bool],
               files: list[str] | None) -> list[tuple[Path, Path]]:
    """(repo root, file) pairs. --files narrows the walk to those paths, still filtered by pred."""
    out = []
    for r in repos:
        base = (root / r).resolve()
        if not base.is_dir():
            continue
        starts = [base]
        if files:
            starts = [Path(f).resolve() for f in files if Path(f).resolve().is_relative_to(base)]
        for s in starts:
            cands = [s] if s.is_file() else s.rglob("*.yml")
            for p in cands:
                rel = p.relative_to(base)
                if SKIP_DIRS.intersection(rel.parts):
                    continue
                if pred(base, p):
                    out.append((base, p))
    return sorted(set(out))


def run(name: str, doc: str, repos: Iterable[str], pred: Callable[[Path, Path], bool],
        needle: re.Pattern[str] | None, transform: Transform,
        add_args: Callable[[argparse.ArgumentParser], None] | None = None,
        after: Callable[[argparse.Namespace], None] | None = None) -> int:
    ap = argparse.ArgumentParser(prog=name, description=doc.strip().split("\n\n")[0])
    ap.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    ap.add_argument("--files", nargs="+", metavar="PATH", help="limit the scope to these files or directories")
    ap.add_argument("--diff", action="store_true", help="print the full unified diff")
    ap.add_argument("--root", type=Path, default=GIT, help="directory holding the sibling repos")
    if add_args:
        add_args(ap)
    args = ap.parse_args()
    root = args.root.resolve()
    files = repo_files(root, repos, pred, args.files)
    changed: list[tuple[Path, int, int]] = []
    skipped: dict[str, list[str]] = defaultdict(list)
    notes: dict[str, list[str]] = defaultdict(list)
    for base, f in files:
        rel = str(f.relative_to(root))
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as e:
            skipped[f"unreadable: {type(e).__name__}"].append(rel)
            continue
        if needle and not needle.search(text):
            continue
        try:
            data = yaml.safe_load(text)
        except yaml.composer.ComposerError:
            skipped["multi-document YAML"].append(rel)
            continue
        except yaml.YAMLError:
            skipped["does not parse"].append(rel)
            continue
        try:
            res = transform(f, text, data, args)
        except Skip as e:
            skipped[str(e)].append(rel)
            continue
        for n in res.notes or []:
            notes[n].append(rel)
        if res.new_text is None or res.new_text == text:
            if res.new_text is not None and res.expected is not None and res.expected != data:
                skipped["the data needs the change but no line matched (flow style, or inside a block scalar)"].append(rel)
            continue
        try:
            new_data = yaml.safe_load(res.new_text)
        except yaml.YAMLError as e:
            skipped["result does not parse"].append(f"{rel}: {str(e).splitlines()[0]}")
            continue
        if has_dups(res.new_text) and not has_dups(text):
            skipped["result has duplicate keys"].append(rel)
            continue
        if res.expected is not None and new_data != res.expected:
            skipped["result differs from the intended data change"].append(rel)
            continue
        diff = list(difflib.unified_diff(text.splitlines(), res.new_text.splitlines(),
                                         f"a/{rel}", f"b/{rel}", lineterm="", n=1))
        plus = sum(1 for d in diff if d.startswith("+") and not d.startswith("+++"))
        minus = sum(1 for d in diff if d.startswith("-") and not d.startswith("---"))
        changed.append((f, plus, minus))
        if args.diff:
            print("\n".join(diff))
        if args.apply:
            f.write_text(res.new_text, encoding="utf-8")
    mode = "applied" if args.apply else "dry run"
    print(f"\n{name} ({mode})")
    for f, plus, minus in changed:
        print(f"  {f.relative_to(root)}  +{plus} -{minus}")
    nskip = sum(len(v) for v in skipped.values())
    print(f"scanned: {len(files)}   {'changed' if args.apply else 'would change'}: {len(changed)}   skipped: {nskip}")
    for reason, fs in sorted(skipped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"  skip ({len(fs)}) {reason}")
        for x in fs:
            print(f"      {x}")
    for note, fs in sorted(notes.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"  note ({len(fs)}) {note}")
        for x in fs[:8]:
            print(f"      {x}")
        if len(fs) > 8:
            print(f"      ... {len(fs) - 8} more")
    if after:
        after(args)
    return 0


def private_character_repos(root: Path = GIT, layer: str | None = None) -> list[str]:
    """Dir names of the private checkouts PRIVATE-REPOS.yml gives a character layer (of this
    kind); none when no such file is checked out."""
    if visibility is None:
        return []
    try:
        v = visibility.get(root)
        return [d.name for d in v.private_checkouts()
                if (cl := v.character_layer(d)) and (layer is None or cl[1] == layer)]
    except Exception:
        return []


def under(base: Path, p: Path, *prefixes: str) -> bool:
    rel = p.relative_to(base).as_posix()
    return any(rel.startswith(x) for x in prefixes)


def skill_card(base: Path, p: Path) -> bool:
    parts = p.relative_to(base).parts
    return len(parts) == 3 and parts[0] == "skills" and parts[2] == "CARD.yml"


def skill_interface(base: Path, p: Path) -> bool:
    """skills/<name>/<UPPERCASE>.yml that is not a view: the skill's prototype and interface files."""
    parts = p.relative_to(base).parts
    stem = p.stem
    return (len(parts) == 3 and parts[0] == "skills" and p.name not in VIEWS
            and stem.upper() == stem and any(ch.isalpha() for ch in stem))
