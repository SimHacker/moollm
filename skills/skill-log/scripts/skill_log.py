#!/usr/bin/env python3
"""
skill-log writer: write one log entry to .moollm/skills/<skill_name>/logs/YYYYMMDD-HHMMSS-<slug>.yml
Time big-endian; body is YAML with timestamp, description, optional payload.
Usage:
  python skill_log.py <skill_name> <description_slug> [key=value ...]
  MOOLLM_ROOT=/path python skill_log.py cursor-mirror export-done format=json
"""
from __future__ import annotations

import os
import re
import sys
from datetime import datetime
from pathlib import Path


def find_moollm_root(start: Path | None = None) -> Path:
    """Resolve .moollm dir: MOOLLM_ROOT env (workspace root) -> .moollm under it; else walk up for .moollm."""
    root = os.environ.get("MOOLLM_ROOT")
    if root:
        return Path(root).resolve() / ".moollm"
    current = (start or Path.cwd()).resolve()
    for parent in [current, *current.parents]:
        if (parent / ".moollm").is_dir():
            return parent / ".moollm"
    return current / ".moollm"


def slugify(description: str, max_len: int = 64) -> str:
    """Filesystem-safe slug: lowercase, replace non-alnum with hyphens, collapse, strip."""
    s = re.sub(r"[^a-z0-9]+", "-", description.lower()).strip("-")
    return s[:max_len] if len(s) > max_len else s


def log_dir(moollm_root: Path, skill_name: str) -> Path:
    """Path to .moollm/skills/<skill_name>/logs/"""
    out = moollm_root / "skills" / skill_name / "logs"
    out.mkdir(parents=True, exist_ok=True)
    return out


def log_entry(
    skill_name: str,
    description_slug: str,
    payload: dict | None = None,
    moollm_root: Path | None = None,
) -> Path:
    """
    Write one log entry. Returns path to written file.
    """
    root = moollm_root or find_moollm_root()
    base = log_dir(root, skill_name)
    now = datetime.now()
    ts_file = now.strftime("%Y%m%d-%H%M%S")
    slug = slugify(description_slug)
    filename = f"{ts_file}-{slug}.yml"
    path = base / filename

    ts_iso = now.isoformat()

    with open(path, "w", encoding="utf-8") as f:
        f.write("# skill-log entry\n")
        f.write(f"timestamp: {ts_iso!r}\n")
        f.write(f"description: {description_slug!r}\n")
        if payload:
            f.write("payload:\n")
            for pk, pv in payload.items():
                f.write(f"  {pk}: {pv!r}\n")

    return path


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: skill_log.py <skill_name> <description_slug> [key=value ...]", file=sys.stderr)
        return 1
    skill_name = sys.argv[1]
    description_slug = sys.argv[2]
    payload = {}
    for arg in sys.argv[3:]:
        if "=" in arg:
            k, v = arg.split("=", 1)
            payload[k.strip()] = v.strip()
    path = log_entry(skill_name, description_slug, payload if payload else None)
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
