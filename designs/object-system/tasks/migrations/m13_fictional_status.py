#!/usr/bin/env python3
"""M13: state `status: fictional` where a fictional layer relied on the retired default.

real_being now defaults to true in every layer unless status: fictional or real_being: false is
stated. Adventure, cast and prototype layers used to default to fictional, so a CHARACTER.yml
there that states neither real_being nor status (top level, character: envelope, or
representation.real_being) would now count as real. This states the fact, beside the
character's other identity keys (after name:, else id:):

  real-people/<id>/CHARACTER.yml, or an id another layer states real_being: true for
      -> real_being: true
  anything nested deeper under real-people/ (robots, pets, rooms of a real person)
      -> unchanged, listed as "needs Don": a pet may be a real animal; a robot or room is
         fictional only when Don says so
  every other file -> status: fictional

Scope: CHARACTER.yml that layers_survey places in an adventure, prototype (moollm-other) or
cast layer. Skipped: files without a top-level name: (several characters in one file, the
schema), templates, files that do not parse.

    python3 designs/object-system/tasks/migrations/m13_fictional_status.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys
from functools import lru_cache
from pathlib import Path

from mlib import MOOLLM, Result, Skip, block_end, indent, is_content, run

sys.path.insert(0, str(MOOLLM / "skills" / "prototype" / "scripts"))
import layers_lint  # noqa: E402
import layers_survey  # noqa: E402

FICTIONAL_LAYERS = {"adventure", "moollm-other", "wwsff-cast"}
REPOS = sorted({r for name, r, _ in layers_survey.LAYERS if name in FICTIONAL_LAYERS})


@lru_cache(None)
def real_elsewhere(root: Path) -> dict[str, set[Path]]:
    """id -> files of layers that state real_being: true."""
    by, _ = layers_lint.load_layers(root)
    out: dict[str, set[Path]] = {}
    for i, layers in by.items():
        for lay in layers:
            f = layers_lint.real_being_of(lay)
            if f and f.value is True:
                out.setdefault(i, set()).add(lay.path.resolve())
    return out


def real_people_place(base: Path, p: Path) -> str | None:
    """'direct' for real-people/<id>/CHARACTER.yml, 'nested' deeper, None outside real-people/."""
    parts = p.relative_to(base).parts
    if "real-people" not in parts:
        return None
    k = len(parts) - 1 - parts[::-1].index("real-people")
    return "direct" if len(parts) == k + 3 else "nested"


def container(data: dict) -> tuple[dict, bool]:
    env = data.get("character")
    if isinstance(env, dict) and ("name" in env or "id" in env):
        return env, True
    return data, False


def states_identity(data: dict) -> bool:
    f, _ = layers_survey.flat(data)
    rep = f.get("representation") if isinstance(f.get("representation"), dict) else {}
    return any(k in f for k in ("real_being", "status")) or "real_being" in rep


def anchor_line(lines: list[str], envelope: bool) -> tuple[int, int]:
    """(index after the name:/id: block, its indent) in the container."""
    lo, hi, want = 0, len(lines), 0
    if envelope:
        h = next((i for i, ln in enumerate(lines) if re.match(r"^character:\s*(#.*)?$", ln)), None)
        if h is None:
            raise Skip("character: envelope is not a block")
        hi = block_end(lines, h)
        first = next((i for i in range(h + 1, hi) if is_content(lines[i])), None)
        if first is None:
            raise Skip("empty character: envelope")
        lo, want = h + 1, indent(lines[first])
    for key in ("name", "id"):
        for i in range(lo, hi):
            if re.match(rf"^ {{{want}}}{key}\s*:", lines[i]) and indent(lines[i]) == want:
                return block_end(lines, i), want
    raise Skip("no name: or id: line in the container")


def transform(path: Path, text: str, data, args) -> Result:
    if not isinstance(data, dict):
        raise Skip("not a map")
    if "_TEMPLATE" in str(path) or "schema" in data:
        raise Skip("template or schema file")
    box, envelope = container(data)
    if "name" not in box:
        raise Skip("no top-level name: (several characters in one file, or not a being)")
    if states_identity(data):
        return Result(None)
    root = args.root.resolve()
    base = next(root / r for r in REPOS if path.resolve().is_relative_to((root / r).resolve()))
    place = real_people_place(base.resolve(), path.resolve())
    if place == "nested":
        return Result(None, notes=["needs Don: nested under real-people/, states neither status nor real_being"])
    i = layers_survey.ident(str(path.relative_to(base)), data)
    others = real_elsewhere(root).get(i, set()) - {path.resolve()}
    if place == "direct" or others:
        key, value, note = "real_being", True, ("real-people/<id>/" if place == "direct"
                                                 else "another layer states real_being: true")
    else:
        key, value, note = "status", "fictional", None
    lines = text.split("\n")
    at, pad = anchor_line(lines, envelope)
    lines.insert(at, f"{' ' * pad}{key}: {'true' if value is True else value}")
    expected = copy.deepcopy(data)
    (expected["character"] if envelope else expected)[key] = value
    notes = [f"real_being: true ({note})"] if note else ["status: fictional"]
    return Result("\n".join(lines), expected, notes)


def pred(base: Path, p: Path) -> bool:
    if p.name != "CHARACTER.yml":
        return False
    rel = p.relative_to(base).as_posix()
    return layers_survey.layer_of(base.name, rel) in FICTIONAL_LAYERS


if __name__ == "__main__":
    sys.exit(run("m13_fictional_status", __doc__, REPOS, pred, None, transform))
