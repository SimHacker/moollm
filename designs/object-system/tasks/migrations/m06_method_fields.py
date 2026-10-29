#!/usr/bin/env python3
"""M6: inside `methods:` entries, `does:` -> `description:`; `params:`/`args:`/`input:` -> `parameters:`.

CARD-ANALYSIS §4: one method core across cards, prototype files and world objects. Only the
key changes; values (map or list) and comments stay. Entries are map-form or list-form
methods; string-form methods have no fields and are left alone.

Skipped: an entry that already has the target key, or two spellings of it.

    python3 designs/object-system/tasks/migrations/m06_method_fields.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import re
import sys

from mlib import Result, data_entries, entry_dicts, rename_entry_fields, run, under

MAP = {"does": "description", "params": "parameters", "args": "parameters", "input": "parameters"}


def transform(path, text, data, args):
    if not isinstance(data, dict):
        return Result(None)
    if not any(k in e for _, c in data_entries(data, "methods") for e in entry_dicts(c) for k in MAP):
        return Result(None)
    lines, expected, n = rename_entry_fields(text.split("\n"), data, "methods", MAP)
    return Result("\n".join(lines), expected)


def pred(base, p):
    return under(base, p, "skills/", "examples/", "kernel/")


if __name__ == "__main__":
    sys.exit(run("m06_method_fields", __doc__, ["moollm"], pred, re.compile(r"^\s*methods:", re.M), transform))
