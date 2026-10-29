#!/usr/bin/env python3
"""M8: flatten the `character:` envelope in CHARACTER.yml, in WillWrightShowForFood and the
private biography repos (PRIVATE-REPOS.yml character_layers).

Reuses skills/prototype/scripts/flatten.py: the envelope line goes, its block is dedented to the
top level, a comment on the envelope line stays. The result must parse to exactly what
resolve.flat() reads from the original. A key both inside and outside the envelope is a
collision: flat() would silently keep the outer one, so those files are skipped and listed.

    python3 designs/object-system/tasks/migrations/m08_flatten_envelopes.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import re
import sys

from mlib import MOOLLM, Result, Skip, private_character_repos, run

sys.path.insert(0, str(MOOLLM / "skills" / "prototype" / "scripts"))
import flatten  # noqa: E402
import resolve  # noqa: E402

KEY = "character"


def transform(path, text, data, args):
    if not isinstance(data, dict) or resolve.envelope_key(path, data) != KEY:
        return Result(None)
    inner = data[KEY]
    clash = sorted(map(str, set(inner) & (set(data) - {KEY})))
    if clash:
        raise Skip(f"collision, same key inside and outside the envelope: {', '.join(clash)}")
    if sum(1 for ln in text.split("\n") if re.match(rf"^{KEY}:", ln)) > 1:
        raise Skip("two top-level character: lines")
    new = flatten.flatten_text(text, KEY)
    if new is None:
        raise Skip("envelope block not found as text (flow style or empty)")
    return Result(new, resolve.flat(path, data))


def pred(base, p):
    return p.name == "CHARACTER.yml"


if __name__ == "__main__":
    sys.exit(run("m08_flatten_envelopes", __doc__, ["WillWrightShowForFood", *private_character_repos(layer="biography")], pred,
                 re.compile(r"^character:", re.M), transform))
