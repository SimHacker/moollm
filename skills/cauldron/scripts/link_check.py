#!/usr/bin/env python3
"""
link_check.py — cauldron LINK implementation.

Sister-script: the behavior matches skills/cauldron/SKILL.md §2.5 exactly.

Walks every markdown file under a directory. For every ``[label](target)`` link,
verifies the target exists.

- ``http://`` / ``https://`` / ``#anchor-only`` links are skipped.
- ``path#anchor`` is split; only the path component is checked.
- Backticked content is stripped before scanning (so literal ``[x](y)`` in code examples
  isn't mistaken for a real link).

Exit code: 0 if all links resolve, 1 if any are broken.

Usage:
    python link_check.py --dir docs/configuration/
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
FENCE_RE = re.compile(r'```.*?```', re.DOTALL)
INLINE_CODE_RE = re.compile(r'`[^`]*`')


def strip_code(text: str) -> str:
    """Remove fenced and inline code so literal link syntax in examples doesn't false-positive."""
    text = FENCE_RE.sub('', text)
    text = INLINE_CODE_RE.sub('', text)
    return text


def check_dir(root: Path) -> tuple[int, list[tuple[str, str, str]]]:
    broken: list[tuple[str, str, str]] = []
    total = 0
    for md in root.rglob('*.md'):
        text = md.read_text()
        stripped = strip_code(text)
        for m in LINK_RE.finditer(stripped):
            label, target = m.group(1), m.group(2)
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            total += 1
            file_part = target.split('#', 1)[0]
            if not file_part:
                continue
            resolved = (md.parent / file_part).resolve()
            if not resolved.exists():
                broken.append((str(md.relative_to(root)), target, label))
    return total, broken


def main() -> int:
    ap = argparse.ArgumentParser(description="cauldron LINK — verify markdown links")
    ap.add_argument('--dir', type=Path, required=True)
    args = ap.parse_args()

    if not args.dir.exists():
        print(f"ERROR: directory not found: {args.dir}", file=sys.stderr)
        return 2

    total, broken = check_dir(args.dir)
    print(f"Checked {total} internal links.")
    if broken:
        print(f"BROKEN: {len(broken)}")
        for src, tgt, lbl in broken:
            print(f"  {src}: [{lbl}]({tgt})")
        return 1
    print("All resolve.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
