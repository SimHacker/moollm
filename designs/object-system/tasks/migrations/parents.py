#!/usr/bin/env python3
"""Parent spellings -> inherits:, by text edit so comments survive.

Run from the repo root: python3 designs/object-system/tasks/migrations/parents.py [--check]

Forms, and what each becomes:
  parent: ../            in ROOM.yml / GLANCE.yml   containment, which the directory states: removed
  prototype: <ref>       on an instance file         inherits: [<ref>]
  prototype: ./x.yml     on a dispenser              clones: ./x.yml (what it dispenses, not its parent)
  prototype: {source,id,...} + inherits: {values}    inherits: ["<source>#*.<id>"]; the other keys
                                                     of both blocks become the object's own slots
  inherits: {archetype, source, description}         lineage: (a literary model, not a parent)
  prototypes: [list]  extends: x  parents: [...]     inherits:
  meta.inherits: [moollm/skills/x]                   top-level inherits: [skills/x]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

A4 = "examples/adventure-4/"
CONTAINMENT = [A4 + p for p in (
    "pub/arcade/ROOM.yml", "pub/bar/ROOM.yml", "pub/bar/cat-cave/ROOM.yml",
    "pub/bar/cat-cave/biscuits-spot/ROOM.yml", "pub/games/ROOM.yml",
    "street/lane-neverending/florist/back-room/ROOM.yml", "street/lane-neverending/florist/basement/ROOM.yml",
    "street/lane-neverending/church-of-the-eval-genius/basement-5-no-ai-embassy/mashup-gallery/GLANCE.yml",
    "street/lane-neverending/church-of-the-eval-genius/basement-5-no-ai-embassy/signal-chapel/GLANCE.yml",
    "street/lane-neverending/church-of-the-eval-genius/basement-5-no-ai-embassy/treaty-hall/GLANCE.yml")]
INSTANCES = [A4 + p for p in (
    "characters/fictional/wumpus-snorax/instances/maze-room-e.yml", "coatroom/mannequin.yml",
    "maze/room-b/bats.yml", "maze/room-c/pit.yml", "maze/room-e/wumpus.yml", "maze/room-g/pit.yml",
    "pub/bar/bartender.yml", "pub/bar/budtender-marieke.yml", "street/lane-neverending/e1/sleeping-figure.yml",
    "street/lane-neverending/florist/back-room/ada-ii.yml", "pub/attic/postmodern-paper.yml")]
DISPENSERS = [A4 + p for p in (
    "street/lane-neverending/w1/acme-catalog-dispenser.yml",
    "street/lane-neverending/leela-manufacturing/lobby/leela-catalog-dispenser.yml")]
CATALOG_INSTANCES = [A4 + p for p in (
    "pub/attic/dusty-mirror.yml", "pub/attic/holiday-box.yml", "pub/attic/old-trunk.yml",
    "pub/basement/ale-barrel.yml", "pub/basement/pickle-shelf.yml", "pub/basement/relic-shelf.yml",
    "pub/basement/treasure-chest.yml", "pub/basement/wine-rack.yml")]
LINEAGE = [A4 + "street/lane-neverending/leela-manufacturing/storage/dolly-forklift.yml"]
RENAME = {
    A4 + "characters/animals/worm-confetti-crawler/CARD.yml": ("prototypes", "inherits"),
    "skills/soul-city/examples/characters/robin/soul/minds/archivist/MIND.yml": ("parents", "inherits"),
    "skills/soul-city/examples/characters/robin/soul/minds/navigator/MIND.yml": ("parents", "inherits"),
}
EXTENDS = ["skills/historical/GLANCE.yml"]
META_INHERITS = [f"skills/{s}/CHARACTER.yml" for s in (
    "github", "postel", "procedural-rhetoric", "prototype", "simulation", "society-of-mind", "yaml-jazz")
] + ["skills/cursor-mirror/characters/i-beam/CHARACTER.yml"]


def indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def block_end(lines: list[str], i: int) -> int:
    """Index after the block whose header is lines[i]; trailing blank lines stay outside."""
    j, last = i + 1, i + 1
    while j < len(lines) and (not lines[j].strip() or indent(lines[j]) > indent(lines[i])):
        if lines[j].strip():
            last = j + 1
        j += 1
    return last


def find(lines: list[str], pattern: str) -> int:
    hits = [i for i, l in enumerate(lines) if re.match(pattern, l)]
    assert len(hits) == 1, (pattern, hits)
    return hits[0]


def drop_line(lines: list[str], i: int) -> list[str]:
    out = lines[:i] + lines[i + 1:]
    if 0 < i < len(out) and not out[i - 1].strip() and not out[i].strip():
        del out[i]
    return out


def containment(lines: list[str]) -> list[str]:
    return drop_line(lines, find(lines, r"parent:"))


def instance(lines: list[str]) -> list[str]:
    i = find(lines, r"\s*prototype:\s+\S")
    m = re.match(r"(\s*)prototype:\s+(\S+)(.*)$", lines[i])
    lines[i] = f"{m[1]}inherits: [{m[2]}]{m[3]}"
    return lines


def dispenser(lines: list[str]) -> list[str]:
    i = find(lines, r"\s*prototype:\s+\S")
    lines[i] = lines[i].replace("prototype:", "clones:", 1)
    return lines


def catalog_instance(lines: list[str]) -> list[str]:
    p = find(lines, r"  prototype:\s*$")
    end = block_end(lines, p)
    body = lines[p + 1:end]
    src = next(re.match(r'\s+source:\s*"?([^"]+)"?\s*$', l)[1] for l in body if l.strip().startswith("source:"))
    oid = next(l.split(":", 1)[1].strip() for l in body if l.strip().startswith("id:"))
    kept = [l[2:] for l in body if not re.match(r"\s+(source|id):", l)]
    lines[p:end] = ["  inherits:", f'    - "{src}#*.{oid}"', *kept]
    return lines


def catalog_instance_values(lines: list[str]) -> list[str]:
    hits = [i for i, l in enumerate(lines) if re.match(r"  inherits:\s*$", l)]
    assert len(hits) == 2, hits
    v = hits[1]
    end = block_end(lines, v)
    head = v
    if lines[v - 1].strip() == "# Inherit all barrel properties from prototype":
        head = v - 1
    lines[head:end] = [l[2:] for l in lines[v + 1:end]]
    return lines


def lineage(lines: list[str]) -> list[str]:
    i = find(lines, r"  inherits:\s*$")
    lines[i] = "  lineage:"
    return lines


def rename(old: str, new: str):
    def go(lines: list[str]) -> list[str]:
        i = find(lines, rf"\s*{old}:")
        lines[i] = lines[i].replace(f"{old}:", f"{new}:", 1)
        return lines
    return go


def extends(lines: list[str]) -> list[str]:
    """The skill's CARD already says it extends real-being; a GLANCE describes, it does not delegate."""
    return drop_line(lines, find(lines, r"extends:"))


def meta_inherits(lines: list[str]) -> list[str]:
    m = find(lines, r"meta:\s*$")
    i = next(k for k in range(m + 1, block_end(lines, m)) if re.match(r"  inherits:\s*$", lines[k]))
    end = block_end(lines, i)
    items = [l[2:].replace("moollm/", "", 1) for l in lines[i + 1:end]]
    del lines[i:end]
    lines[m:m] = ["inherits:", *items, ""]
    return lines


PLAN = ([(f, [containment]) for f in CONTAINMENT] + [(f, [instance]) for f in INSTANCES]
        + [(f, [dispenser]) for f in DISPENSERS]
        + [(f, [catalog_instance, catalog_instance_values]) for f in CATALOG_INSTANCES]
        + [(f, [lineage]) for f in LINEAGE] + [(f, [rename(*r)]) for f, r in RENAME.items()]
        + [(f, [extends]) for f in EXTENDS] + [(f, [meta_inherits]) for f in META_INHERITS])


def main() -> int:
    check = "--check" in sys.argv
    changed = 0
    for path, steps in PLAN:
        f = Path(path)
        text = f.read_text()
        lines = text.split("\n")
        try:
            for step in steps:
                lines = step(lines)
        except (AssertionError, StopIteration) as e:
            print(f"skip {path}: {e!r}")
            continue
        new = "\n".join(lines)
        yaml.safe_load(new)
        if new != text:
            changed += 1
            if not check:
                f.write_text(new)
    print(f"{'would change' if check else 'changed'} {changed} of {len(PLAN)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
