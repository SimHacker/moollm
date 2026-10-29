#!/usr/bin/env python3
"""behavior_survey.py — what is inside methods:, advertisements: and the card keys.

vocab_survey.py counts top-level keys. This looks one level down, at the fields
of each method and advertisement entry, and at the top-level keys of every
skills/*/CARD.yml, so the analysis in designs/object-system/analysis/ can be
rerun after a migration.

Usage:
    behavior_survey.py [cards|methods|adverts|activation|world|all]

Sources: skills/*/CARD.yml (cards), skills/*/GLANCE.yml (when:), and every
*.yml under examples/ plus skills/*/<UPPERCASE>.yml prototype files (world),
skipping CARD, GLANCE, INDEX and build/ output.
"""

from __future__ import annotations

import collections
import glob
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]


def load(path: str):
    try:
        return yaml.safe_load(open(ROOT / path, encoding="utf-8"))
    except Exception:
        return None


def cards() -> dict[str, dict]:
    out, bad = {}, []
    for p in sorted(glob.glob("skills/*/CARD.yml", root_dir=ROOT)):
        d = load(p)
        if isinstance(d, dict):
            out[p.split("/")[1]] = d
        else:
            bad.append(p)
    cards.unparseable = bad
    return out


def shape(v) -> str:
    if isinstance(v, dict):
        return "map"
    if isinstance(v, list):
        return "list"
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return "number"
    return type(v).__name__


def top(counter: collections.Counter, n: int = 40) -> None:
    for k, v in counter.most_common(n):
        print(f"  {v:5d}  {k}")


def survey_cards() -> None:
    cs = cards()
    keys = collections.Counter()
    shapes: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for d in cs.values():
        for k, v in d.items():
            keys[k] += 1
            shapes[k][shape(v)] += 1
    print(f"cards: {len(cs)} parse, unparseable: {cards.unparseable}")
    for k, v in keys.most_common():
        print(f"  {v:5d}  {k:28s} {dict(shapes[k])}")


def entries(block):
    if isinstance(block, dict):
        return list(block.items())
    if isinstance(block, list):
        return [(None, x) for x in block]
    return []


def survey_methods() -> None:
    fields, container, case = collections.Counter(), collections.Counter(), collections.Counter()
    sig, params, output = collections.Counter(), collections.Counter(), collections.Counter()
    for d in cards().values():
        m = d.get("methods")
        if m is None:
            continue
        container[shape(m)] += 1
        for name, e in entries(m):
            if name is not None:
                case["UPPER" if re.fullmatch(r"[A-Z0-9_-]+", str(name)) else "lower/mixed"] += 1
            if not isinstance(e, dict):
                fields[f"<{shape(e)} entry>"] += 1
                continue
            fields.update(e.keys())
            s = e.get("signature")
            if s is not None:
                sig["starts with name" if str(s).upper().startswith(str(name).upper()) else "other"] += 1
            p = e.get("parameters", e.get("params"))
            if p is not None:
                params[shape(p)] += 1
            o = e.get("output")
            if o is not None:
                output[re.sub(r"\s*\(.*?\)", "", str(o)).replace(" ", "")] += 1
    print("cards methods: container", dict(container), "names", dict(case))
    print("entry fields:")
    top(fields)
    print("signature:", dict(sig), " parameters:", dict(params))
    print("output values (parentheticals stripped), distinct", len(output))
    top(output, 12)


def survey_adverts() -> None:
    fields, container, link = collections.Counter(), collections.Counter(), collections.Counter()
    score, cond = collections.Counter(), collections.Counter()
    for d in cards().values():
        a = d.get("advertisements")
        if a is None:
            continue
        container[shape(a)] += 1
        methods = {str(k).upper() for k in (d.get("methods") or {})} if isinstance(d.get("methods"), dict) else set()
        for name, e in entries(a):
            if not isinstance(e, dict):
                continue
            fields.update(e.keys())
            n = str(name or e.get("id") or "").upper()
            if n in methods:
                link["same name as a method"] += 1
            elif e.get("method") or e.get("action"):
                link["method:/action: field"] += 1
            else:
                link["no method"] += 1
            score[shape(e.get("score"))] += 1
            c = e.get("condition")
            cond["absent" if c is None else ("expression" if re.search(r"&&|\|\||===|world\.", str(c)) else "prose")] += 1
    print("cards advertisements: container", dict(container))
    print("link to methods:", dict(link))
    print("score:", dict(score), " condition:", dict(cond))
    print("entry fields:")
    top(fields)


def survey_activation() -> None:
    combos = collections.Counter()
    for skill, d in cards().items():
        g = load(f"skills/{skill}/GLANCE.yml")
        has = (
            ("GLANCE when" if isinstance(g, dict) and "when" in g else ""),
            ("invoke_when" if "invoke_when" in d else ""),
            ("advertisements" if "advertisements" in d else ""),
            ("k_lines" if "k_lines" in d else ""),
        )
        combos[" + ".join(x for x in has if x) or "none"] += 1
    print("per skill, which 'when to use me' declarations exist:")
    top(combos)


def survey_world() -> None:
    afields, mfields, container = collections.Counter(), collections.Counter(), collections.Counter()
    paths = glob.glob("examples/**/*.yml", root_dir=ROOT, recursive=True)
    paths += glob.glob("skills/*/[A-Z]*.yml", root_dir=ROOT)
    for p in paths:
        if "/build/" in p or p.endswith(("CARD.yml", "GLANCE.yml", "INDEX.yml")):
            continue
        d = load(p)

        def walk(o, depth=0):
            if depth > 4 or not isinstance(o, dict):
                return
            a, m = o.get("advertisements"), o.get("methods")
            if a is not None:
                container[shape(a)] += 1
                for _, e in entries(a):
                    if isinstance(e, dict):
                        afields.update(e.keys())
            if isinstance(m, dict):
                for _, e in m.items():
                    if isinstance(e, dict):
                        mfields.update(e.keys())
                    else:
                        mfields[f"<{shape(e)} entry>"] += 1
            for v in o.values():
                walk(v, depth + 1)

        walk(d)
    print("world advertisements blocks:", dict(container))
    print("world advertisement fields:")
    top(afields, 25)
    print("world method fields:")
    top(mfields, 20)


SECTIONS = {
    "cards": survey_cards,
    "methods": survey_methods,
    "adverts": survey_adverts,
    "activation": survey_activation,
    "world": survey_world,
}


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for name, fn in SECTIONS.items():
        if which in (name, "all"):
            print(f"\n## {name}")
            fn()
    return 0


if __name__ == "__main__":
    sys.exit(main())
