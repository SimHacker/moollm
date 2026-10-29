#!/usr/bin/env python3
"""M5: drop `score_if:` values that restate the default (always, any, true).

An omitted score_if means the score stands as given (CARD-ANALYSIS §3), so `score_if: always`
says nothing. Only score_if inside advertisement entries is touched, and only when its value
fits on its line. A comment on the removed line stays, as a comment line at the same indent.

Skipped: an entry that would be left empty, a multi-line value. The report also counts other
values that restate a proposed default, for a later row once the S1 schema fixes them.

    python3 designs/object-system/tasks/migrations/m05_defaults.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys
from collections import Counter

import yaml

from mlib import Result, Skip, collection_blocks, data_entries, entry_dicts, indent, run, single_line, \
    split_comment, under

DEFAULTS = {"always", "any", "true"}
LATER: Counter = Counter()


def restates(v) -> bool:
    return v is True or (isinstance(v, str) and v.strip().strip(".").lower() in DEFAULTS)


def later(e: dict) -> None:
    """Other default-restating values, by the CARD-ANALYSIS §3 proposals."""
    if e.get("score") == 50:
        LATER["score: 50"] += 1
    if isinstance(e.get("guard"), str) and e["guard"].strip().lower() in ("always", "none", "true", "any"):
        LATER["guard: always/none/true/any"] += 1
    if e.get("guard") is True:
        LATER["guard: true"] += 1
    if e.get("reach") == "room":
        LATER["reach: room"] += 1
    ib = e.get("invoked_by")
    if isinstance(ib, list) and sorted(ib) == ["npc", "player"]:
        LATER["invoked_by: [player, npc]"] += 1
    if isinstance(e.get("score_if"), str) and e["score_if"].strip().lower() in ("never", "none"):
        LATER["score_if: never/none (not a default; probably score: 0)"] += 1
    for k in ("condition", "guard", "score_if"):
        if isinstance(e.get(k), str) and e[k].strip().lower() == "always" and k == "condition":
            LATER["condition: always (after M3 becomes guard/score_if: always)"] += 1


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    found = False
    for _, c in data_entries(data, "advertisements"):
        for e in entry_dicts(c):
            later(e)
            if "score_if" in e and restates(e["score_if"]):
                found = True
                if len(e) == 1:
                    raise Skip("entry has nothing but score_if: always")
    if not found:
        return Result(None)
    expected = copy.deepcopy(data)
    for _, c in data_entries(expected, "advertisements"):
        for e in entry_dicts(c):
            if "score_if" in e and restates(e["score_if"]):
                del e["score_if"]
    lines = text.split("\n")
    out = list(lines)
    for h, end, form, es in collection_blocks(lines, "advertisements"):
        for e in es:
            i = e.fields(lines).get("score_if")
            if i is None:
                continue
            value, comment = split_comment(lines[i].split(":", 1)[1])
            try:
                v = yaml.safe_load(value) if value else None
            except yaml.YAMLError:
                continue
            if not restates(v):
                continue
            if not single_line(lines, i, e.field_indent, e.end):
                raise Skip("multi-line score_if")
            if form == "list" and i == e.start:
                raise Skip("score_if: always on the dash line of a list entry")
            out[i] = " " * indent(lines[i]) + "# " + comment if comment else None
    return Result("\n".join(ln for ln in out if ln is not None), expected)


def pred(base, p):
    return under(base, p, "skills/", "examples/")


def after(args):
    print("  later candidates (values that restate a proposed default, left alone):")
    for k, n in LATER.most_common():
        print(f"    {n:5}  {k}")


if __name__ == "__main__":
    sys.exit(run("m05_defaults", __doc__, ["moollm"], pred, re.compile(r"advertisements"), transform, after=after))
