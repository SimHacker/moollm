#!/usr/bin/env python3
"""Schema keys use underscores: k-lines, klines, see-also, invoked-by -> k_lines, see_also, invoked_by.

Run from the repo root: python3 designs/object-system/tasks/migrations/schema_keys.py [--check]

Only keys are renamed (a line whose first token is the key, optionally as a list item), in
.yml, .tmpl and .md files. Values stay: `- k-lines` in a list names the k-lines skill.
A YAML file is written only if it still parses, has no duplicate keys, and equals the old
data with those keys renamed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

RENAMES = {"k-lines": "k_lines", "klines": "k_lines", "see-also": "see_also", "invoked-by": "invoked_by"}
KEY = re.compile(r"^(\s*(?:- )?)(k-lines|klines|see-also|invoked-by)(\s*:)", re.M)
SKIP = {".git", "node_modules", "temp", ".moollm", "dist"}


class Dup(yaml.SafeLoader):
    pass


def no_dups(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    keys = [loader.construct_object(k, deep=deep) for k, _ in node.value]
    hashable = [k for k in keys if isinstance(k, (str, int, float, bool, type(None)))]
    if len(hashable) != len(set(hashable)):
        raise ValueError(f"duplicate key at line {node.start_mark.line + 1}")
    return yaml.SafeLoader.construct_mapping(loader, node, deep)


Dup.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, lambda l, n: no_dups(l, n, True))


def renamed(v):
    if isinstance(v, dict):
        return {RENAMES.get(k, k) if isinstance(k, str) else k: renamed(x) for k, x in v.items()}
    if isinstance(v, list):
        return [renamed(x) for x in v]
    return v


def main() -> int:
    check = "--check" in sys.argv
    changed, skipped = [], []
    for f in sorted(Path(".").rglob("*")):
        if SKIP.intersection(f.parts) or not f.is_file() or f.suffix not in {".yml", ".md", ".tmpl"}:
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = KEY.sub(lambda m: m[1] + RENAMES[m[2]] + m[3], text)
        if new == text:
            continue
        if f.suffix == ".yml":
            try:
                old_data = yaml.safe_load(text)
            except yaml.YAMLError:
                old_data = None
            if old_data is not None:
                try:
                    new_data = yaml.load(new, Loader=Dup)
                except (yaml.YAMLError, ValueError) as e:
                    try:
                        yaml.load(text, Loader=Dup)
                        skipped.append(f"{f}: {e}")
                        continue
                    except (yaml.YAMLError, ValueError) as before:
                        if str(before) != str(e):
                            skipped.append(f"{f}: {e}")
                            continue
                        new_data = yaml.safe_load(new)
                if new_data != renamed(old_data):
                    skipped.append(f"{f}: data differs beyond the rename")
                    continue
        changed.append(f)
        if not check:
            f.write_text(new, encoding="utf-8")
    print(f"{'would change' if check else 'changed'} {len(changed)} files")
    for s in skipped:
        print("skip", s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
