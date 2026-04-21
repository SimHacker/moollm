#!/usr/bin/env python3
"""
split_monolith.py — cauldron LADLE implementation.

Sister-script: the behavior matches skills/cauldron/SKILL.md §2.3 exactly.
If script and doc disagree, the doc is canonical.

Walks a Phase-1 monolith's ``## N.`` boundaries and writes each slice to a target
file under ``out_dir/``. No manual copy-paste.

Usage:
    python split_monolith.py --monolith docs/topic-plan.md \
        --out-dir docs/topic/ \
        --map mapping.yml

Where ``mapping.yml`` is:

    file_map:
      '1': '01-overview.md'
      '2': '01-overview.md'
      '3': '02-affected-surfaces.md'
      '4': '03-shared-packages.md'
      # ...
      'Appendix A': 'design-wisdom.md'
      'Appendix B': '10-open-questions.md'
    header_templates:
      '01-overview.md':
        title: 'Overview: what is wrong, and the target model'
        desc: 'Maps to §1–§2 of the original plan.'
      # ...

Every output file gets a preamble:

    > <desc>
    >
    > Cross-references like `§X.Y` refer to numbered sections in the original plan,
    > mapped to files per README.md.

The monolith is NOT deleted or moved. It stays as the Phase-1 artifact of record.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(2)


HEADER_RE = re.compile(r'^## (\d+|Appendix [A-Z])\.\s+(.*)$')


def parse_boundaries(text: str) -> list[tuple[str, int, int, str]]:
    """Return list of (section_key, start_line, end_line, title)."""
    lines = text.split('\n')
    boundaries: list[tuple[str, int, str]] = []
    for i, line in enumerate(lines):
        m = HEADER_RE.match(line)
        if m:
            boundaries.append((m.group(1), i, m.group(2).strip()))
    slices: list[tuple[str, int, int, str]] = []
    for idx, (key, start, title) in enumerate(boundaries):
        end = boundaries[idx + 1][1] if idx + 1 < len(boundaries) else len(lines)
        slices.append((key, start, end, title))
    return slices


def split(monolith_path: Path, out_dir: Path, mapping: dict) -> list[Path]:
    text = monolith_path.read_text()
    lines = text.split('\n')
    slices = parse_boundaries(text)

    file_map = mapping['file_map']
    header_templates = mapping.get('header_templates', {})

    buckets: dict[str, list[str]] = {}
    for key, start, end, title in slices:
        if key not in file_map:
            print(f"WARNING: no mapping for §{key} ({title!r}), skipping", file=sys.stderr)
            continue
        fname = file_map[key]
        body = '\n'.join(lines[start:end])
        buckets.setdefault(fname, []).append(body.strip())

    out_dir.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    for fname, parts in buckets.items():
        tmpl = header_templates.get(fname, {})
        title = tmpl.get('title', fname.replace('.md', '').replace('-', ' ').title())
        desc = tmpl.get('desc', '(auto-split)')
        preamble = f"""# {title}

> {desc}
>
> Cross-references like `§X.Y` refer to numbered sections in the original plan.
> See [../README.md](README.md) for the § → file mapping.

---

"""
        body = '\n\n'.join(parts)
        out_path = out_dir / fname
        out_path.write_text(preamble + body + '\n')
        created.append(out_path)
        print(f"wrote {out_path}")

    return created


def main() -> int:
    ap = argparse.ArgumentParser(description="cauldron LADLE")
    ap.add_argument('--monolith', type=Path, required=True)
    ap.add_argument('--out-dir', type=Path, required=True)
    ap.add_argument('--map', type=Path, required=True,
                    help='YAML file with file_map and header_templates')
    args = ap.parse_args()

    if not args.monolith.exists():
        print(f"ERROR: monolith not found: {args.monolith}", file=sys.stderr)
        return 2
    mapping = yaml.safe_load(args.map.read_text())
    created = split(args.monolith, args.out_dir, mapping)
    print(f"\nLADLE complete: {len(created)} files written to {args.out_dir}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
