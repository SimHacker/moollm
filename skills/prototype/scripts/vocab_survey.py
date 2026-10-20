#!/usr/bin/env python3
"""vocab_survey.py — count the competing spellings of each object-system concept.

Prints, per cluster in designs/object-system/VOCABULARY-CLUSTERS.md, how many
YAML objects use each top-level key and in what value shapes, with one example
file per shape. Scans *.yml outside temp/, node_modules/, dist/, .git/, plus
the frontmatter of skills/*/SKILL.md (counted separately).

Usage:
    vocab_survey.py [--cluster NAME] [--examples]
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resolve  # noqa: E402

CLUSTERS: dict[str, list[str]] = {
    "delegation": ["inherits", "parents", "parent", "prototype", "prototypes", "extends", "meta.inherits", "<name*>"],
    "cascade": ["container.inherits", "defaults", "ambient", "provides"],
    "placement": ["location", "home", "contents", "contains", "objects", "characters", "residents", "exits"],
    "activation": ["k-lines", "k_lines", "klines", "when", "invoke_when", "use_when", "triggers", "what", "why"],
    "association": ["related", "see_also", "see-also", "references", "benefits_from", "requires", "respects"],
    "behavior": ["methods", "advertisements", "actions", "commands", "interactions", "operations", "protocol"],
    "envelope": ["card", "room", "character", "container", "instance", "object", "meta", "metadata"],
    "classification": ["type", "kind", "tier", "tags", "ontology", "species", "role", "nature", "archetype"],
    "identity": ["name", "id", "title", "emoji", "emoji_identity", "icon", "aliases", "aka", "also_called"],
    "provenance": ["credits", "lineage", "sources", "source", "origin", "inspiration", "version", "created"],
    "state": ["state", "status", "inventory", "memory"],
    "files": ["files", "interface", "interfaces", "implements"],
}

KLINE = re.compile(r"^[A-Z0-9][A-Z0-9_-]+$")


def shape(v: Any) -> str:
    if isinstance(v, str):
        if "://" in v:
            return "url"
        if KLINE.match(v):
            return "KLINE"
        if "/" in v and " " not in v:
            return "path"
        return "id" if re.match(r"^[\w.-]+$", v) else "prose"
    if isinstance(v, list):
        inner = sorted({shape(x) for x in v[:20]})
        return "list[" + ",".join(inner) + "]"
    if isinstance(v, dict):
        keys = sorted(map(str, v))
        return "map{" + ",".join(keys[:4]) + (",…" if len(keys) > 4 else "") + "}" if len(keys) <= 6 else f"map({len(keys)} keys)"
    return type(v).__name__


def lookup(d: dict[str, Any], key: str) -> tuple[bool, Any]:
    if key == "<name*>":
        hits = {k: v for k, v in d.items() if isinstance(k, str) and k.endswith("*") and len(k) > 1}
        return bool(hits), hits
    cur: Any = d
    for part in key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return False, None
        cur = cur[part]
    return True, cur


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--cluster")
    ap.add_argument("--examples", action="store_true", help="show one example file per shape")
    args = ap.parse_args(argv)
    root = resolve.find_root(Path.cwd())
    docs: list[tuple[Path, dict[str, Any]]] = []
    for f in resolve.iter_yaml([root], root):
        d = resolve.load_yaml(f)
        if isinstance(d, dict):
            docs.append((f, d))
    frontmatter: collections.Counter[str] = collections.Counter()
    for f in root.glob("skills/*/SKILL.md"):
        m = re.match(r"^---\n(.*?)\n---", f.read_text(errors="ignore"), re.S)
        try:
            fm = yaml.safe_load(m.group(1)) if m else None
        except yaml.YAMLError:
            continue
        for k in fm or {}:
            frontmatter[str(k)] += 1
    print(f"yaml objects: {len(docs)}")
    for name, keys in CLUSTERS.items():
        if args.cluster and name != args.cluster:
            continue
        print(f"\n## {name}")
        for key in keys:
            shapes: collections.Counter[str] = collections.Counter()
            example: dict[str, str] = {}
            for f, d in docs:
                found, v = lookup(d, key)
                if found:
                    s = shape(v)
                    shapes[s] += 1
                    example.setdefault(s, resolve.rel(f, root))
            total = sum(shapes.values())
            fm = f"  frontmatter={frontmatter[key]}" if frontmatter[key] else ""
            if not total and not fm:
                continue
            print(f"  {key:20} {total:4d}{fm}")
            for s, n in shapes.most_common(4):
                tail = f"  {example[s]}" if args.examples else ""
                print(f"      {n:4d}  {s[:48]:50}{tail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
