#!/usr/bin/env python3
"""M3: `condition:` inside advertisement entries -> `guard:` (world objects) or `score_if:` (CARDs).

In a world object (examples/**, skills/<name>/<UPPERCASE>.yml prototype and interface files)
a condition says when the offer is available, which is a guard. In a CARD.yml it says when the
skill wants to be chosen, which is a score_if (CARD-ANALYSIS §2). Only the key changes; the
prose value and its comments stay. CARDs under examples/ follow the CARD rule and are listed
in the report so a reviewer can check them.

Skipped: an entry that already has the target key, flow-style advertisement blocks. Plural
`conditions:` is reported, not changed.

    python3 designs/object-system/tasks/migrations/m03_condition.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import re
import sys

from mlib import Result, data_entries, entry_dicts, rename_entry_fields, run, skill_card, skill_interface, under


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    target = "score_if" if path.name == "CARD.yml" else "guard"
    notes = []
    plural = any("conditions" in e for _, c in data_entries(data, "advertisements") for e in entry_dicts(c))
    if plural:
        notes.append("conditions: (plural) in an advertisement entry, not changed")
    has = any("condition" in e for _, c in data_entries(data, "advertisements") for e in entry_dicts(c))
    if not has:
        return Result(None, notes=notes)
    lines, expected, n = rename_entry_fields(text.split("\n"), data, "advertisements", {"condition": target})
    if path.name == "CARD.yml" and "/examples/" in path.as_posix():
        notes.append("CARD under examples/: condition -> score_if; check it is not a guard")
    return Result("\n".join(lines), expected, notes)


def pred(base, p):
    return skill_card(base, p) or skill_interface(base, p) or under(base, p, "examples/")


if __name__ == "__main__":
    sys.exit(run("m03_condition", __doc__, ["moollm"], pred, re.compile(r"conditions?:"), transform))
