#!/usr/bin/env python3
"""M9: parent spellings in CHARACTER.yml -> `inherits:` / `derived_from:`, cross-repo refs -> moollm://.

Scope: CHARACTER.yml in WillWrightShowForFood, DonHopkins, MicropolisCore. Keys at the top level
or directly inside a `character:` envelope:

  character_ref, canonical_soul, prototype_ref, canonical_home, moollm_home, wwsff_local,
  moollm_source, and an `inherits:` map           -> inherits: [ref, ...]
  upstream                                        -> derived_from: [ref]

A reference becomes:
  - a GitHub URL, or a map {repo, path, absolute_url, canonical_dir, character_url,
    character_dir, character: CHARACTER.yml, import_mode: overlay, note}
        -> moollm://github/<owner>/<repo>/<path>, with the absolute URL (and the note) kept as a
           YAML Jazz comment on the item's line. The owner is checked against
           `git -C <sibling> remote get-url origin`.
  - a relative path into a sibling repo -> moollm://..., the original path as the comment.
  - a path inside the same repo -> unchanged.
Two references to the same target (canonical_soul and prototype_ref) become one item.
If skills/prototype/scripts/refs.py exists, its to_uri() builds the URI.

Skipped for an agent: maps with other keys (home_room, lineage, invitation, moollm_skills, ...;
the cast `inherits:` maps that mix parents and skills are row J6), map fields that disagree,
relative paths that resolve nowhere, spellings at two levels in one file, an existing
`inherits:` that is not a block list.

    python3 designs/object-system/tasks/migrations/m09_parent_spellings.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

from mlib import MOOLLM, Result, Skip, block_end, indent, is_content, run, split_comment

sys.path.insert(0, str(MOOLLM / "skills" / "prototype" / "scripts"))
try:
    import refs  # type: ignore  # noqa: E402
except ImportError:
    refs = None

INHERITS = ("character_ref", "canonical_soul", "prototype_ref", "canonical_home", "moollm_home",
            "wwsff_local", "moollm_source")
DERIVED = ("upstream",)
REF_KEYS = {"repo", "path", "absolute_url", "canonical_dir", "character_url", "character_dir",
            "character", "import_mode", "note"}
GITHUB = re.compile(r"^https?://github\.com/([^/\s]+)/([^/\s#]+?)(?:\.git)?(?:/(?:tree|blob)/[^/\s]+(?:/(.*))?)?/?$")
ROOT: Path = MOOLLM.parent


def to_uri(owner: str, repo: str, path: str) -> str:
    path = path.strip("/")
    if refs is not None and callable(getattr(refs, "to_uri", None)):
        for call in (lambda: refs.to_uri(owner, repo, path), lambda: refs.to_uri(f"{owner}/{repo}/{path}")):
            try:
                u = call()
            except Exception:
                continue
            if isinstance(u, str) and u.startswith("moollm://"):
                return u
    return f"moollm://github/{owner}/{repo}/{path}".rstrip("/")


@lru_cache(None)
def owner_of(repo: str) -> str | None:
    """Owner from the sibling checkout's origin URL (read-only git)."""
    d = ROOT / repo
    if not d.is_dir():
        return None
    try:
        url = subprocess.run(["git", "-C", str(d), "remote", "get-url", "origin"], capture_output=True,
                             text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return None
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", url)
    return m[1] if m and m[2] == repo else None


def check_owner(owner: str, repo: str) -> None:
    o = owner_of(repo)
    if o is None:
        raise Skip(f"no sibling checkout of {repo} to confirm its owner")
    if o != owner:
        raise Skip(f"{repo} owner is {o} in its origin, {owner} in the file")


def norm_path(p: str, repo: str) -> str:
    p = p.strip().strip("/")
    if p.startswith(repo + "/"):
        p = p[len(repo) + 1:]
    return re.sub(r"/?CHARACTER\.yml$", "", p)


def from_url(url: str) -> tuple[str, str, str] | None:
    m = GITHUB.match(url.strip())
    return (m[1], m[2], norm_path(m[3] or "", m[2])) if m else None


def ref_from_map(m: dict, f: Path, base: Path) -> tuple[str, str, str | None, str | None]:
    """(value, target key for dedupe, comment on the item line, note for a line above it)."""
    if "moollm_skills" in m:
        raise Skip("inherits: map lists skills beside the parent (L4 split, row J6)")
    extra = set(m) - REF_KEYS
    if extra:
        raise Skip(f"parent map has keys beyond a reference: {', '.join(sorted(extra))}")
    if m.get("character", "CHARACTER.yml") != "CHARACTER.yml":
        raise Skip("parent map names a file other than CHARACTER.yml")
    if m.get("import_mode", "overlay") != "overlay":
        raise Skip(f"import_mode: {m['import_mode']}")
    found: set[tuple[str, str, str]] = set()
    url_shown = None
    for k in ("absolute_url", "character_url", "character_dir"):
        if isinstance(m.get(k), str):
            r = from_url(m[k])
            if not r:
                raise Skip(f"{k} is not a GitHub URL")
            found.add(r)
            url_shown = url_shown or m[k].strip()
    repo = m.get("repo")
    if isinstance(repo, str):
        r = from_url(repo) or (tuple(repo.strip("/").split("/", 1)) + ("",) if repo.count("/") == 1 else None)
        if not r:
            raise Skip(f"unreadable repo: {repo}")
        owner, name = r[0], r[1]
        for k in ("path", "canonical_dir"):
            if isinstance(m.get(k), str):
                found.add((owner, name, norm_path(m[k], name)))
        if not any(isinstance(m.get(k), str) for k in ("path", "canonical_dir", "absolute_url", "character_url", "character_dir")):
            found.add((owner, name, ""))
    note = m.get("note") if isinstance(m.get("note"), str) else None
    if isinstance(m.get("path"), str) and not found and not isinstance(repo, str):
        if set(m) - {"path", "note"}:
            raise Skip("parent map with a local path and other keys")
        value, target, comment = ref_from_str(m["path"], f, base)
        return value, target, comment, note
    if len(found) != 1:
        raise Skip("parent map fields disagree about the target" if found else "parent map names no target")
    owner, name, path = found.pop()
    check_owner(owner, name)
    return to_uri(owner, name, path), str((ROOT / name / path).resolve()), url_shown, note


def ref_from_str(v: str, f: Path, base: Path) -> tuple[str, str, str | None]:
    v = v.strip()
    r = from_url(v)
    if r:
        check_owner(r[0], r[1])
        return to_uri(*r), str((ROOT / r[1] / r[2]).resolve()), v
    if "://" in v:
        raise Skip(f"reference with an unknown scheme: {v}")
    cands = [(f.parent / v).resolve()] + ([] if v.startswith(".") else [(base / v).resolve()])
    hit = next((c for c in cands if c.exists()), None)
    if hit is None:
        raise Skip("relative reference resolves to nothing")
    target = hit.parent if hit.name == "CHARACTER.yml" else hit
    if hit.is_relative_to(base):
        return v, str(target), None
    if not hit.is_relative_to(ROOT):
        raise Skip("reference leaves the repos directory")
    name, *rest = hit.relative_to(ROOT).parts
    owner = owner_of(name)
    if owner is None:
        raise Skip(f"no origin for sibling repo {name}")
    return to_uri(owner, name, norm_path("/".join(rest), name)), str(target), v


def level_dict(data: dict, env: bool) -> dict:
    return data["character"] if env else data


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    base = next(p for p in [path.parent, *path.parents] if (p / ".git").exists())
    env = data.get("character") if isinstance(data.get("character"), dict) else None
    levels = {}
    for env_flag, d in ((False, data), (True, env)):
        if d is None:
            continue
        keys = [k for k in d if k in INHERITS + DERIVED or (k == "inherits" and isinstance(d[k], dict))]
        if keys:
            levels[env_flag] = keys
    if not levels:
        return Result(None)
    if len(levels) > 1:
        raise Skip("parent spellings at two levels (top and inside character:)")
    in_env, keys = next(iter(levels.items()))
    d = level_dict(data, in_env)
    lines = text.split("\n")
    if in_env:
        e = [i for i, ln in enumerate(lines) if re.match(r"^character:\s*(#.*)?$", ln)]
        if len(e) != 1:
            raise Skip("character: envelope not found as one block")
        lo, hi = e[0] + 1, block_end(lines, e[0])
        child = next(indent(ln) for ln in lines[lo:hi] if is_content(ln))
    else:
        lo, hi, child = 0, len(lines), 0

    def find(k: str) -> int:
        hits = [i for i in range(lo, hi) if re.match(rf"^ {{{child}}}{re.escape(k)}\s*:(\s|$)", lines[i])]
        if len(hits) != 1:
            raise Skip(f"{k}: not found once at its level")
        return hits[0]

    new: dict[str, list[tuple[str, str, str | None, str | None]]] = {"inherits": [], "derived_from": []}
    spans = []
    notes = []
    for k in sorted(keys, key=find):
        v = d[k]
        dest = "derived_from" if k in DERIVED else "inherits"
        if isinstance(v, dict):
            item = ref_from_map(v, path, base)
            if item[3] and re.search(r"absolute_url|shorthand|\brepo\b|\bpath\b", item[3]):
                notes.append("kept note mentions the removed map fields (absolute_url, shorthand); reword by hand")
        elif isinstance(v, str):
            item = ref_from_str(v, path, base) + (None,)
        else:
            raise Skip(f"{k}: is a {type(v).__name__}")
        new[dest].append(item)
        i = find(k)
        spans.append((i, block_end(lines, i) if isinstance(v, dict) else i + 1, dest))
    existing = {k: d.get(k) for k in new if k in d and not (k == "inherits" and isinstance(d[k], dict))}
    for k, v in existing.items():
        if not isinstance(v, list):
            raise Skip(f"existing {k}: is a {type(v).__name__}, not a list")

    expected = copy.deepcopy(data)
    ed = level_dict(expected, in_env)
    for k in keys:
        del ed[k]
    items_by_dest = {}
    for dest, items in new.items():
        if not items:
            continue
        seen, kept = set(), []
        for value, target, comment, note in items:
            if target in seen or value in (existing.get(dest) or []):
                if note:
                    raise Skip("a duplicate reference carries a note")
                continue
            seen.add(target)
            kept.append((value, comment, note))
        items_by_dest[dest] = kept
        ed[dest] = list(existing.get(dest) or []) + [v for v, _, _ in kept]

    out = list(lines)
    pad = " " * child
    inserts: dict[int, list[str]] = {}
    for dest, kept in items_by_dest.items():
        item_lines = []
        for v, c, note in kept:
            if note:
                item_lines.append(f"{pad}  # {' '.join(note.split())}")
            item_lines.append(f"{pad}  - {v}" + (f"  # {c}" if c else ""))
        if dest in existing:
            j = find(dest)
            if re.match(rf"^ {{{child}}}{dest}\s*:\s*\[", lines[j]):
                raise Skip(f"existing {dest}: is a flow list")
            end = block_end(lines, j)
            ind = next(indent(ln) for ln in lines[j + 1:end] if is_content(ln))
            inserts.setdefault(end, []).extend(" " * ind + x.lstrip() for x in item_lines)
        else:
            first = min(s for s, _, dd in spans if dd == dest)
            inserts.setdefault(first, []).extend([f"{pad}{dest}:"] + item_lines)
    drop = set()
    for s, e, _ in spans:
        block = lines[s:e]
        inner = [split_comment(ln.split(":", 1)[1])[1] if ":" in ln and is_content(ln) else ln.strip()[1:].strip()
                 for ln in block[1:] if ln.strip() and (not is_content(ln) or " #" in ln)]
        if any(inner):
            raise Skip("comments inside a parent map (move them by hand)")
        drop.update(range(s, e))
    result = []
    for i, ln in enumerate(out + [""]):
        if i in inserts:
            result.extend(inserts[i])
        if i < len(out) and i not in drop:
            result.append(ln)
    return Result("\n".join(result), expected, sorted(set(notes)))


def pred(base, p):
    return p.name == "CHARACTER.yml"


if __name__ == "__main__":
    sys.exit(run("m09_parent_spellings", __doc__, ["WillWrightShowForFood", "DonHopkins", "MicropolisCore"], pred,
                 re.compile(r"^\s*(" + "|".join(INHERITS + DERIVED) + r"|inherits)\s*:", re.M), transform))
