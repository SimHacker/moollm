#!/usr/bin/env python3
"""M10: `representation.protocol:` -> `representation.governed_by:` in DonHopkins (L8).

The profile layer already spells it governed_by; the biography layer says protocol. Only the
key on the line directly inside a `representation:` block changes, at any nesting (the
character: envelope or the top level). Value and comment stay.

Skipped: a representation block that already has governed_by:.

    python3 designs/object-system/tasks/migrations/m10_governed_by.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys

from mlib import Result, Skip, block_end, data_entries, header_lines, indent, is_content, rename_key_on_line, run


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    reps = [r for _, r in data_entries(data, "representation") if isinstance(r, dict) and "protocol" in r]
    if not reps:
        return Result(None)
    if any("governed_by" in r for r in reps):
        raise Skip("representation has both protocol: and governed_by:")
    expected = copy.deepcopy(data)
    for _, r in data_entries(expected, "representation"):
        if isinstance(r, dict) and "protocol" in r:
            r["governed_by"] = r.pop("protocol")
    lines = text.split("\n")
    out = list(lines)
    for h in header_lines(lines, "representation"):
        end = block_end(lines, h)
        body = [i for i in range(h + 1, end) if is_content(lines[i])]
        if not body:
            continue
        child = indent(lines[body[0]])
        for i in body:
            if indent(lines[i]) == child and re.match(r"^\s*protocol\s*:(\s|$)", lines[i]):
                out[i] = rename_key_on_line(lines[i], "protocol", "governed_by")
    return Result("\n".join(out), expected)


if __name__ == "__main__":
    sys.exit(run("m10_governed_by", __doc__, ["DonHopkins"], lambda b, p: True,
                 re.compile(r"^\s*protocol\s*:", re.M), transform))
