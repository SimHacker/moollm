#!/usr/bin/env python3
"""M2: advertisements as a list -> a map keyed by name.

Scope: moollm skills/*/CARD.yml and examples/**. The key is the entry's `name:`, else its
`id:`, else its `action:` uppercased and hyphenated, else `ON-<TRIGGER>` from its trigger
word. The field the
key came from is dropped when it equals the key (and the entry has other fields); every other
field stays. The list item's first line becomes the map key line, so comments stay where they
were.

Skipped for an agent: string entries, flow-style entries, entries with no name, action or
trigger, triggers too long to make a name from, and duplicate names (unless
--suffix-duplicates). Advertisement lists inside logs and reports (events:, world_state:) are
records of past state and are skipped.

    python3 designs/object-system/tasks/migrations/m02_advert_lists.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import re
import sys

import yaml

from mlib import Result, Skip, block_end, data_entries, header_lines, flow_headers, indent, is_content, \
    entries, run, single_line, skill_card, split_comment, under

KEY = "advertisements"
MAX_TRIGGER_WORDS = 4
LOG_PATHS = ("events", "world_state")
WORD = re.compile(r"[^\W_]+")


def slug(s: str) -> str:
    return "-".join(WORD.findall(s)).upper()


def advert_name(e: dict) -> tuple[str, str | None]:
    """(key, field it came from or None)."""
    for f in ("name", "id"):
        n = e.get(f)
        if isinstance(n, str) and n.strip():
            return n.strip(), f
    a = e.get("action")
    if isinstance(a, str) and slug(a):
        if re.search(r"[,/|]| or ", a):
            raise Skip("action: names several verbs (one advertisement or several?)")
        return slug(a), "action"
    t = e.get("trigger")
    if isinstance(t, list) and t and isinstance(t[0], str):
        t = t[0]
    if isinstance(t, str) and slug(t):
        words = WORD.findall(t)
        if len(words) > MAX_TRIGGER_WORDS:
            raise Skip(f"trigger too long to name an advertisement (> {MAX_TRIGGER_WORDS} words)")
        return "ON-" + slug(t), None
    raise Skip("advertisement entry with no name, action or trigger")


def key_text(k: str) -> str:
    try:
        ok = yaml.safe_load(f"{k}: 1") == {k: 1}
    except yaml.YAMLError:
        ok = False
    return k if ok else '"' + k.replace("\\", "\\\\").replace('"', '\\"') + '"'


def plan(entries_data: list, suffix: bool) -> list[tuple[str, str | None]]:
    """Per entry: (key, field to drop or None)."""
    out, seen = [], {}
    for e in entries_data:
        if not isinstance(e, dict):
            raise Skip("non-map advertisement entries (strings)")
        k, src = advert_name(e)
        drop = src if src and e.get(src) == k and len(e) > 1 else None
        if k in seen:
            if not suffix:
                raise Skip("duplicate advertisement names in one list")
            seen[k] += 1
            k = f"{k}-{seen[k]}"
        else:
            seen[k] = 1
        out.append((k, drop))
    return out


def expected_data(data, suffix: bool):
    import copy
    exp = copy.deepcopy(data)

    def fix(v, path):
        if isinstance(v, dict):
            for k, x in list(v.items()):
                if k == KEY and isinstance(x, list) and x and not (path and path[0] in LOG_PATHS):
                    names = plan(x, suffix)
                    v[k] = {n: {f: y for f, y in e.items() if f != d} for (n, d), e in zip(names, x)}
                else:
                    fix(x, path + [str(k)])
        elif isinstance(v, list):
            for x in v:
                fix(x, path + ["[]"])
    fix(exp, [])
    return exp


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    logs = [p for p, v in data_entries(data, KEY) if isinstance(v, list) and p and p[0] in LOG_PATHS]
    lists = [p for p, v in data_entries(data, KEY) if isinstance(v, list) and v and not (p and p[0] in LOG_PATHS)]
    if logs and not lists:
        raise Skip("advertisement lists only inside a log or report (events:, world_state:)")
    if logs:
        raise Skip("advertisement lists both in the object and in a log section")
    if not lists:
        return Result(None)
    if flow_headers(text.split("\n"), KEY):
        raise Skip("flow-style advertisements:")
    expected = expected_data(data, args.suffix_duplicates)
    lines = text.split("\n")
    out = list(lines)
    notes = []
    for h in reversed(header_lines(lines, KEY)):
        end = block_end(lines, h)
        form, es = entries(lines, h, end)
        if form != "list":
            continue
        base = indent(lines[h])
        snippet = "\n".join(ln[base:] if ln.startswith(" " * base) else ln for ln in lines[h:end])
        try:
            parsed = (yaml.safe_load(snippet) or {}).get(KEY)
        except yaml.YAMLError:
            raise Skip("advertisements block does not parse on its own (anchors?)")
        if not isinstance(parsed, list) or len(parsed) != len(es):
            raise Skip("advertisements list: entry count differs from parse")
        names = plan(parsed, args.suffix_duplicates)
        shift = 2 if es[0].key_indent == base else 0
        block = []
        cursor = h + 1
        for e, (name, drop), ed in zip(es, names, parsed):
            block += [(" " * shift + ln) if ln.strip() else ln for ln in lines[cursor:e.start]]
            block += rewrite_entry(lines, e, name, drop, shift)
            cursor = e.end
            if drop is None and name == slug(str(ed.get("action", ""))) and ed.get("action") != name:
                notes.append("action: kept, its spelling differs from the key")
        block += [(" " * shift + ln) if ln.strip() else ln for ln in lines[cursor:end]]
        out[h + 1:end] = block
    return Result("\n".join(out), expected, sorted(set(notes)))


def rewrite_entry(lines: list[str], e, name: str, drop: str | None, shift: int) -> list[str]:
    first = lines[e.start]
    m = re.match(r"^(\s*)-( +)(.*)$", first) or re.match(r"^(\s*)-()()$", first)
    rest = m[3]
    if rest[:1] in "{[\"'" or (rest and not rest.startswith("#") and not re.match(r"[A-Za-z_][\w-]*\s*:(\s|$)", rest)):
        raise Skip("flow-style or scalar advertisement entry")
    key_ind = e.key_indent + shift
    fi = e.field_indent + shift if e.field_indent is not None else key_ind + 2
    body = [(" " * shift + ln) if ln.strip() else ln for ln in lines[e.start + 1:e.end]]
    head_comment = None
    head: list[str] = []
    if not rest or rest.startswith("#"):
        head_comment = rest[1:].strip() if rest else None
    elif drop and re.match(rf"{drop}\s*:", rest):
        if not single_line(lines, e.start, e.field_indent, e.end):
            raise Skip(f"multi-line {drop}: used as the advertisement key")
        head_comment = split_comment(rest.split(":", 1)[1])[1]
        drop = None
    else:
        head = [" " * fi + rest]
    if drop:
        idx = next((i for i in range(e.start + 1, e.end)
                    if re.match(rf"^ {{{e.field_indent}}}{drop}\s*:(\s|$)", lines[i])), None)
        if idx is None:
            raise Skip(f"{drop}: not found at the entry's field indent")
        if not single_line(lines, idx, e.field_indent, e.end):
            raise Skip(f"multi-line {drop}: used as the advertisement key")
        c = split_comment(lines[idx].split(":", 1)[1])[1]
        k = idx - e.start - 1
        body[k:k + 1] = [" " * fi + "# " + c] if c else []
    key_line = " " * key_ind + key_text(name) + ":" + (f"  # {head_comment}" if head_comment else "")
    return [key_line] + head + body


def add_args(ap):
    ap.add_argument("--suffix-duplicates", action="store_true",
                    help="name repeated keys NAME-2, NAME-3 instead of skipping the file")


def pred(base, p):
    return skill_card(base, p) or under(base, p, "examples/")


if __name__ == "__main__":
    sys.exit(run("m02_advert_lists", __doc__, ["moollm"], pred, re.compile(r"^\s*advertisements:", re.M),
                 transform, add_args))
