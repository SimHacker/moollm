#!/usr/bin/env python3
"""M4: trigger advertisements: score 0..1 -> 0..100, `response:`/`result:` -> `say:`.

A trigger entry is an advertisement entry with a `trigger:` field. Its score is rescaled
(×100, rounded to an int) when it is a number in 0..1; a block whose trigger scores already
go above 1 is on the 0..100 scale and is skipped. The value's comment stays on the line.
`response:` or `result:` on a trigger entry becomes `say:` (CARD-ANALYSIS §3, effects).

Scope: moollm skills/ and examples/, and all of WillWrightShowForFood. Trigger-shaped maps
outside `advertisements:` (secrets:, key_squawks:, ...) and response:/result: on entries
without a trigger are counted in the report and left for a judgment row.

Skipped: an entry with both response: and result:, or one of them beside say:.

    python3 designs/object-system/tasks/migrations/m04_triggers.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys
from collections import Counter

import yaml

from mlib import Result, Skip, collection_blocks, data_entries, entry_dicts, indent, run, under, \
    rename_key_on_line, split_comment

SAY = {"response": "say", "result": "say"}
SCORE_LINE = re.compile(r"^(\s*(?:- +)?score\s*:\s*)([-+]?\d+(?:\.\d+)?|\.\d+)(\s*(?:#.*)?)$")
TALLY: Counter = Counter()


def is_trigger(e) -> bool:
    return isinstance(e, dict) and "trigger" in e


def scalable(e) -> bool:
    s = e.get("score")
    return isinstance(s, (int, float)) and not isinstance(s, bool) and 0 <= s <= 1


def scaled(s) -> int:
    return int(round(s * 100))


def check_block(es: list[dict]) -> None:
    trig = [e for e in es if is_trigger(e)]
    nums = [e["score"] for e in trig if isinstance(e.get("score"), (int, float)) and not isinstance(e.get("score"), bool)]
    if any(n > 1 for n in nums) and any(0 < n < 1 for n in nums):
        raise Skip("trigger scores on both scales in one block")
    for e in trig:
        srcs = [k for k in SAY if k in e]
        if len(srcs) > 1 or (srcs and "say" in e):
            raise Skip("trigger entry with two of response:/result:/say:")


def tally(data) -> None:
    def walk(v, parent):
        if isinstance(v, dict):
            if "trigger" in v and parent != "advertisements" and any(k in v for k in ("score", "response", "result")):
                TALLY[f"trigger-shaped map under {parent}: (left alone)"] += 1
            for k, x in v.items():
                walk(x, k)
        elif isinstance(v, list):
            for x in v:
                walk(x, parent)
    walk(data, "<top>")
    for _, c in data_entries(data, "advertisements"):
        for e in entry_dicts(c):
            if not is_trigger(e) and any(k in e for k in SAY):
                TALLY["response:/result: on an advertisement without trigger: (left alone)"] += 1


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    tally(data)
    colls = [c for _, c in data_entries(data, "advertisements")]
    if not any(is_trigger(e) for c in colls for e in entry_dicts(c)):
        return Result(None)
    for c in colls:
        check_block(entry_dicts(c))
    expected = copy.deepcopy(data)
    for _, c in data_entries(expected, "advertisements"):
        es = entry_dicts(c)
        big = any(isinstance(e.get("score"), (int, float)) and e["score"] > 1 for e in es if is_trigger(e))
        items = c.items() if isinstance(c, dict) else enumerate(c) if isinstance(c, list) else []
        for k, e in list(items):
            if not is_trigger(e):
                continue
            new = {SAY.get(f, f): v for f, v in e.items()}
            if not big and scalable(e):
                new["score"] = scaled(e["score"])
            c[k] = new
    lines = text.split("\n")
    out = list(lines)
    for h, end, form, es in collection_blocks(lines, "advertisements"):
        if not es:
            continue
        base = indent(lines[h])
        snippet = "\n".join(ln[base:] if ln.startswith(" " * base) else ln for ln in lines[h:end])
        try:
            parsed = (yaml.safe_load(snippet) or {}).get("advertisements")
        except yaml.YAMLError:
            raise Skip("advertisements block does not parse on its own")
        vals = list(parsed.values()) if isinstance(parsed, dict) else parsed if isinstance(parsed, list) else []
        if len(vals) != len(es):
            raise Skip("advertisements block: entry count differs from parse")
        big = any(isinstance(v.get("score"), (int, float)) and v["score"] > 1 for v in vals if is_trigger(v))
        for e, v in zip(es, vals):
            if not is_trigger(v):
                continue
            fields = e.fields(lines)
            for f, i in fields.items():
                if f in SAY:
                    out[i] = rename_key_on_line(lines[i], f, SAY[f])
            if "score" in fields and not big and scalable(v):
                i = fields["score"]
                m = SCORE_LINE.match(lines[i])
                if not m:
                    raise Skip(f"score line not a plain number at line {i + 1}")
                out[i] = f"{m[1]}{scaled(v['score'])}{m[3]}"
    return Result("\n".join(out), expected)


def pred(base, p):
    return base.name != "moollm" or under(base, p, "skills/", "examples/")


def after(args):
    for k, n in TALLY.most_common():
        print(f"  later ({n}) {k}")


if __name__ == "__main__":
    sys.exit(run("m04_triggers", __doc__, ["moollm", "WillWrightShowForFood"], pred,
                 re.compile(r"trigger"), transform, after=after))
