#!/usr/bin/env python3
"""Survey character layers across MOOLLM-related repos.

A person or creature can have one CHARACTER.yml per layer: the adventure layer in
moollm/examples, the profile and cast layers in WillWrightShowForFood, an audience seat in a
repo show, a page in MicropolisCore, and layers in private repos (biography, ...). This reports
how each layer spells identity, parents, purpose and relationships, and which ids have several
layers. Private repos and their layer kinds come from visibility.py (PRIVATE-REPOS.yml).

Usage: layers_survey.py [census|parents|ids|purpose|all] [--root DIR]
DIR is the directory holding the sibling repos (default: moollm's parent).
"""
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import visibility  # noqa: E402

LAYERS = [
    # (layer name, repo, path prefix inside the repo)
    ("adventure", "moollm", "examples/adventure-4/characters/"),
    ("moollm-other", "moollm", ""),
    ("show-audience", "WillWrightShowForFood", "repo-shows/"),
    ("wwsff-cast", "WillWrightShowForFood", "characters/menagerie/"),
    ("wwsff-cast", "WillWrightShowForFood", "characters/sims/"),
    ("wwsff-cast", "WillWrightShowForFood", "characters/robots/"),
    ("wwsff-profile", "WillWrightShowForFood", "characters/"),
    ("micropoliscore", "MicropolisCore", ""),
]
PARENT_KEYS = ["inherits", "moollm_source", "character_ref", "wwsff_local", "canonical",
               "source", "extends", "overlay_of", "incarnation_of", "import_mode", "prototype"]
PURPOSE_HINTS = ["real_being", "representation", "consent", "privacy", "memorial", "deceased",
                 "died", "alive", "living", "invitation", "invited", "status", "ethics",
                 "portrayal", "disclosure", "planted", "authorship"]


@lru_cache(None)
def private_layers(root):
    """(layer, checkout dir name, path prefix) for each private checkout PRIVATE-REPOS.yml describes."""
    v = visibility.get(Path(root))
    out = []
    for d in v.private_checkouts():
        cl = v.character_layer(d)
        if cl:
            out.append((cl[1], d.name, cl[0]))
    return tuple(out)


def layer_of(repo, rel, root=None):
    rows = LAYERS + list(private_layers(Path(root)) if root is not None else [])
    for name, r, prefix in rows:
        if r == repo and rel.startswith(prefix):
            return name
    return None


def load_all(root):
    out = []
    root = Path(root)
    for repo in sorted({r for _, r, _ in LAYERS + list(private_layers(root))}):
        base = root / repo
        if not base.is_dir():
            continue
        for p in base.rglob("CHARACTER.yml"):
            rel = str(p.relative_to(base))
            if "/node_modules/" in rel or "/build/" in rel or "_TEMPLATE" in rel:
                continue
            layer = layer_of(repo, rel, root)
            try:
                data = yaml.safe_load(p.read_text())
            except Exception:
                data = "UNPARSEABLE"
            out.append((layer, repo, rel, p, data))
    return out


def flat(d):
    """Top level, with a character: envelope opened (the slots inside it count as top level)."""
    if isinstance(d, dict) and isinstance(d.get("character"), dict):
        merged = {k: v for k, v in d.items() if k != "character"}
        merged.update(d["character"])
        return merged, True
    return (d if isinstance(d, dict) else {}), False


def shape(v):
    return {dict: "map", list: "list", str: "str"}.get(type(v), type(v).__name__)


def ident(rel, d):
    f, _ = flat(d)
    i = f.get("id")
    return str(i) if isinstance(i, str) else Path(rel).parent.name


def census(rows):
    by = defaultdict(list)
    for r in rows:
        by[r[0]].append(r)
    for layer, rs in by.items():
        keys, env, bad = Counter(), 0, 0
        for _, _, _, _, d in rs:
            if d == "UNPARSEABLE":
                bad += 1
                continue
            f, e = flat(d)
            env += e
            keys.update(f.keys())
        print(f"\n## {layer}: {len(rs)} files, character: envelope {env}, unparseable {bad}")
        print("   " + ", ".join(f"{k} {n}" for k, n in keys.most_common(40)))


def parents(rows):
    print("\n## parent spellings (key: shape count per layer)")
    c = defaultdict(Counter)
    for layer, _, _, _, d in rows:
        f, _ = flat(d)
        for k in PARENT_KEYS:
            if k in f:
                c[k][(layer, shape(f[k]))] += 1
    for k, cc in c.items():
        print(f"   {k:14} " + ", ".join(f"{l}/{s} {n}" for (l, s), n in cc.most_common()))


def ids(rows):
    by = defaultdict(set)
    for layer, repo, rel, _, d in rows:
        if d != "UNPARSEABLE":
            by[ident(rel, d)].add(layer)
    multi = {i: ls for i, ls in by.items() if len(ls) > 1}
    print(f"\n## ids in more than one layer: {len(multi)} of {len(by)}")
    for i, ls in sorted(multi.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"   {i:28} {sorted(ls)}")


def purpose(rows):
    print("\n## purpose and representation keys (top level or one map down), per layer")
    c = defaultdict(Counter)
    for layer, _, _, _, d in rows:
        f, _ = flat(d)
        seen = set(f)
        for v in f.values():
            if isinstance(v, dict):
                seen |= set(v)
        for h in PURPOSE_HINTS:
            if h in seen:
                c[layer][h] += 1
    for layer, cc in c.items():
        print(f"   {layer:15} " + ", ".join(f"{k} {n}" for k, n in cc.most_common()))


SECTIONS = {"census": census, "parents": parents, "ids": ids, "purpose": purpose}


def main(argv):
    root = Path(__file__).resolve().parents[4]
    if "--root" in argv:
        root = Path(argv[argv.index("--root") + 1])
    which = [a for a in argv if a in SECTIONS or a == "all"] or ["all"]
    rows = load_all(root)
    print(f"root {root}: {len(rows)} CHARACTER.yml")
    for name, fn in SECTIONS.items():
        if "all" in which or name in which:
            fn(rows)


if __name__ == "__main__":
    main(sys.argv[1:])
