#!/usr/bin/env python3
"""
anchor_verify.py — cauldron ANCHOR implementation.

Sister-script: the behavior matches skills/cauldron/SKILL.md §2.4 exactly.

Walks the Phase-2 tree. For every path-like citation in the form ``apps/foo/bar.py:NN``
or ``apps/foo/bar.py:NN-MM`` or just ``apps/foo/bar.py``, verifies that:

1. The cited file exists under ``--code-root``.
2. If a line number is cited, the file has at least that many lines.
3. (Optional, via --strict) the cited line matches an expected pattern.

Drift policy:
- Missing file → ERROR (likely stale monolith).
- Cited line > file length → ERROR (likely drift).
- Cited line ≤ file length → OK (line content drift is flagged by the executor's
  per-step verification, not here).

Exit code: 0 if no drifts, 1 if drifts found, 2 on error.

Usage:
    python anchor_verify.py --docs docs/configuration/ --code-root /path/to/central
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Matches citations like `apps/foo/bar.py:123` or `apps/foo/bar.py:123-145`.
CITE_RE = re.compile(r'`?([a-zA-Z0-9_./-]+\.[a-zA-Z]+)(?::(\d+)(?:-(\d+))?)?`?')

# Files we care about checking (extensions that indicate source).
CODE_EXTS = {'.py', '.sh', '.ts', '.js', '.sql', '.md', '.yml', '.yaml', '.toml'}


def scan(docs: Path, code_root: Path) -> tuple[int, list[str]]:
    total = 0
    drifts: list[str] = []

    for md in docs.rglob('*.md'):
        text = md.read_text()
        for m in CITE_RE.finditer(text):
            path_str, line_start, line_end = m.group(1), m.group(2), m.group(3)
            p = Path(path_str)
            if p.suffix not in CODE_EXTS:
                continue
            if path_str.startswith(('./', '../')) or '/' not in path_str:
                continue

            total += 1
            resolved = code_root / path_str
            if not resolved.exists():
                drifts.append(
                    f"MISSING: {md.relative_to(docs)} cites {path_str!r}, "
                    f"but {resolved} does not exist"
                )
                continue

            if line_start:
                n_lines = sum(1 for _ in resolved.open('r', errors='ignore'))
                ls = int(line_start)
                le = int(line_end) if line_end else ls
                if ls > n_lines or le > n_lines:
                    drifts.append(
                        f"DRIFT: {md.relative_to(docs)} cites {path_str}:{line_start}"
                        f"{'-' + line_end if line_end else ''}, "
                        f"but the file has only {n_lines} lines"
                    )

    return total, drifts


def main() -> int:
    ap = argparse.ArgumentParser(description="cauldron ANCHOR — verify code citations")
    ap.add_argument('--docs', type=Path, required=True, help='Phase-2 tree root')
    ap.add_argument('--code-root', type=Path, required=True,
                    help='root of the code tree paths are relative to')
    ap.add_argument('--strict', action='store_true',
                    help='reserved; content-pattern verification not yet implemented')
    args = ap.parse_args()

    if not args.docs.exists() or not args.code_root.exists():
        print("ERROR: --docs and --code-root must exist", file=sys.stderr)
        return 2

    total, drifts = scan(args.docs, args.code_root)
    print(f"Checked {total} path citations.")
    if drifts:
        print(f"DRIFTS: {len(drifts)}")
        for d in drifts:
            print(f"  {d}")
        return 1
    print("All citations resolve against the current code tree.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
