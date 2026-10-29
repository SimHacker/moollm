#!/usr/bin/env python3
"""M14: `signifier: "📖"` -> 🎭, or 🤖 when the being's type names a robot, AI or bot.

📖 is a value alias of 🎭 (skills/character/CHARACTER.yml schema.keys.signifier). The rewrite
applies to fictional beings only: real_being: false or status: fictional in the file, or no
layer of the id is real by layers_lint's rule. On a real being 📖 is a topical emoji, which
belongs in emoji:; those files are skipped for Don (lint reports them as signifier info).
Comments are not touched; the value keeps its quotes and trailing comment.

Scope: CHARACTER.yml and CARD.yml in moollm, WillWrightShowForFood, MicropolisCore, RepoShow
and the private character repos (PRIVATE-REPOS.yml character_layers).

    python3 designs/object-system/tasks/migrations/m14_signifier_alias.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys
from functools import lru_cache
from pathlib import Path

from mlib import MOOLLM, Result, Skip, private_character_repos, run

sys.path.insert(0, str(MOOLLM / "skills" / "prototype" / "scripts"))
import layers_lint  # noqa: E402
import layers_survey  # noqa: E402

ALIAS = "📖"
LINE = re.compile(r"^(\s*(?:- +)?signifier\s*:\s*)([\"']?)📖\ufe0f?\2(\s*(?:#.*)?)$")


@lru_cache(None)
def real_ids(root: Path) -> frozenset[str]:
    by, _ = layers_lint.load_layers(root)
    return frozenset(i for i, ls in by.items() if layers_lint.is_real(ls))


def walk(v, fn):
    if isinstance(v, dict):
        for k in list(v):
            if k == "signifier" and isinstance(v[k], str) and v[k].replace("\ufe0f", "") == ALIAS:
                v[k] = fn(v)
            else:
                walk(v[k], fn)
    elif isinstance(v, list):
        for x in v:
            walk(x, fn)


def transform(path: Path, text: str, data, args) -> Result:
    if not isinstance(data, dict):
        raise Skip("not a map")
    f, _ = layers_survey.flat(data)
    i = f["id"] if isinstance(f.get("id"), str) else path.parent.name
    rep = f.get("representation") if isinstance(f.get("representation"), dict) else {}
    stated_fictional = (f.get("real_being") is False or rep.get("real_being") is False
                        or layers_lint.norm_status(f.get("status")) == "fictional")
    if not stated_fictional and (f.get("real_being") is True or i in real_ids(args.root.resolve())):
        raise Skip("real being: 📖 is a topical emoji here; Don picks the signifier (👤) and moves 📖 to emoji:")

    def pick(container: dict) -> str:
        t = " ".join(str(container.get(k) or f.get(k) or "") for k in ("type", "species"))
        return "🤖" if layers_lint.ROBOT_TYPE.search(t) else "🎭"

    expected = copy.deepcopy(data)
    walk(expected, pick)
    want = pick(f)
    out = [LINE.sub(lambda m: f"{m[1]}{m[2]}{want}{m[2]}{m[3]}", ln) for ln in text.split("\n")]
    return Result("\n".join(out), expected, [f"signifier 📖 -> {want}"])


def pred(base: Path, p: Path) -> bool:
    return p.name in ("CHARACTER.yml", "CARD.yml")


if __name__ == "__main__":
    sys.exit(run("m14_signifier_alias", __doc__,
                 ["moollm", "WillWrightShowForFood", "MicropolisCore", "RepoShow", *private_character_repos()],
                 pred, re.compile(r"^\s*(?:- +)?signifier\s*:\s*[\"']?📖", re.M), transform))
