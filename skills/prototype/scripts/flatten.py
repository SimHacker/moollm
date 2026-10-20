#!/usr/bin/env python3
"""flatten.py — remove envelope keys (`room:` in ROOM.yml, `object:`, ...) from YAML files.

A text edit, not a YAML round trip, so comments and formatting survive. The
envelope line goes away and its block is dedented to the top level. A file is
written only if the result parses to exactly what resolve.flat() reads from
the original; anything else is skipped and reported.

Usage:
    flatten.py [--write] [--name ROOM.yml] PATH ...
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resolve  # noqa: E402

TOP_KEY = re.compile(r"^([^\s#][^:]*):")


def flatten_text(text: str, key: str) -> str | None:
    lines = text.split("\n")
    start = next((i for i, ln in enumerate(lines) if re.match(rf"^{re.escape(key)}:\s*(#.*)?$", ln)), None)
    if start is None:
        return None
    end = start + 1
    while end < len(lines):
        ln = lines[end]
        if TOP_KEY.match(ln) or ln.startswith("---"):
            break
        end += 1
    # Column-0 comments directly before the next top-level key belong to that key;
    # whitespace-only lines stay in the block, since block scalars can own them.
    k = end
    while k - 1 > start and (lines[k - 1].startswith("#") or not lines[k - 1].strip()):
        k -= 1
    tail = lines[k:end]
    if any(ln.startswith("#") for ln in tail):
        first_comment = k + next(i for i, ln in enumerate(tail) if ln.startswith("#"))
        end = first_comment
    block = lines[start + 1:end]
    content = [ln for ln in block if ln.strip() and not ln.lstrip().startswith("#")]
    if not content:
        return None
    indent = min(len(ln) - len(ln.lstrip(" ")) for ln in content)
    if indent == 0:
        return None
    pad = " " * indent
    out = [ln[indent:] if ln.startswith(pad) else ln.lstrip(" ") if not ln.strip() or ln.lstrip().startswith("#") else ln
           for ln in block]
    trailing = re.match(rf"^{re.escape(key)}:\s*(#.*)$", lines[start])
    head = [trailing.group(1)] if trailing else []
    return "\n".join(lines[:start] + head + out + lines[end:])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--name", help="only files with this name, e.g. ROOM.yml")
    ap.add_argument("--write", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args(argv)
    root = resolve.find_root(Path(args.paths[0]).resolve())
    files = [f for f in resolve.iter_yaml([Path(p) for p in args.paths], root) if not args.name or f.name == args.name]
    done = skipped = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        data = resolve.load_yaml(f)
        if not isinstance(data, dict):
            continue
        key = resolve.envelope_key(f, data)
        if not key:
            continue
        inner = data[key]
        clash = sorted(set(inner) & (set(data) - {key}))
        if clash:
            print(f"skip (same key inside and outside: {', '.join(map(str, clash))}): {resolve.rel(f, root)}")
            skipped += 1
            continue
        new = flatten_text(text, key)
        try:
            ok = new is not None and yaml.safe_load(new) == resolve.flat(f, data)
        except yaml.YAMLError:
            ok = False
        if not ok:
            print(f"skip (result would differ): {resolve.rel(f, root)}")
            skipped += 1
            continue
        done += 1
        if args.write:
            f.write_text(new, encoding="utf-8")
    print(f"{'flattened' if args.write else 'would flatten'}: {done}   skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
