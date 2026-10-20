"""One-off: lighting prose -> 0..10 level + comment; grue_safe/requires_light/ambient_light out.

Dry run by default; --write to apply. Every changed file must reparse, and the only key
differences allowed are lighting values and the removed keys.
"""
import re
import sys
from pathlib import Path

import yaml

LEVEL = {
    "none": 0, "magical": 7, "natural": 8, "dim": 3, "warm_and_cozy": 6, "warm": 6,
    "natural_sunlight": 9, "crystal_glow": 4, "bright": 8, "industrial": 7, "variable": 5,
    "dim_inside_bright_sign": 3, "dim_filtered": 3, "single_bulb": 4, "bright_sunlight": 10,
    "security_light": 5, "laptop_screen_glow": 2, "dim_with_occasional_flashes": 3,
    "dim_industrial": 3, "screen_glow": 3, "dramatic": 5, "golden_kitchen_glow": 6,
    "dramatic_spotlights": 6, "confrontational": 7, "fluorescent_harsh": 8,
    "fluorescent_low_clearance": 7, "inspection_bright": 9, "server_room_blue": 3,
    "self_righteous": 7, "warm_department_store": 7, "clinical": 8, "interrogation": 9,
    "clinical_white": 9, "fluorescent_oppressive": 8,
    "magical (implausible shaft of golden light)": 7,
    "none (vending machine glow not enough)": 1, "none (mushroom glow)": 1,
    "natural (golden afternoon)": 8, "warm and cozy": 6,
}
GRUE_DARK = 2          # the grue hunts at this level or below
HAND = {"maze/room-h", "maze/room-f"}   # dark-and-safe or lair: the cause is another object
DROP = re.compile(r"^\s*(grue_safe|requires_light|ambient_light):")
LIGHT = re.compile(r"^(\s*)lighting:\s*(.*?)\s*$")


def split_comment(rest: str) -> tuple[str, str]:
    m = re.match(r"^(\"[^\"]*\"|'[^']*'|[^#]*?)\s*(?:#\s*(.*))?$", rest)
    return m.group(1).strip().strip("'\""), (m.group(2) or "").strip()


def migrate(path: Path) -> str | None:
    lines = path.read_text().splitlines(keepends=True)
    data = yaml.safe_load("".join(lines)) or {}
    safe = data.get("grue_safe") if isinstance(data, dict) else None
    notes, out = [], []
    for ln in lines:
        if DROP.match(ln):
            key, rest = ln.split(":", 1)
            value, comment = split_comment(rest)
            if (key.strip() == "grue_safe" and comment and "grue" not in comment.lower()
                    and not any(h in str(path) for h in HAND)):
                notes.append(comment.rstrip("."))
            continue
        out.append(ln)
    for i, ln in enumerate(out):
        m = LIGHT.match(ln)
        if not m or not m.group(2) or m.group(2).startswith(("|", ">")):
            continue
        value, comment = split_comment(m.group(2))
        if value not in LEVEL:
            continue
        level = LEVEL[value]
        if not any(h in str(path) for h in HAND):
            if safe is True and level <= GRUE_DARK:
                level = GRUE_DARK + 1
            if safe is False and level > GRUE_DARK:
                level = GRUE_DARK
        words = [] if value == "none" else [value.replace("_", " ")]
        words += [c for c in (comment, *notes) if c]
        tail = f"  # {'; '.join(words)}" if words else ""
        out[i] = f"{m.group(1)}lighting: {level}{tail}\n"
        notes = []
    new = "".join(out)
    return None if new == "".join(lines) else new


def strip(v, gone=frozenset({"grue_safe", "requires_light", "ambient_light", "lighting"})):
    if isinstance(v, dict):
        return {k: strip(x) for k, x in v.items() if k not in gone}
    if isinstance(v, list):
        return [strip(x) for x in v]
    return v


def check(old: dict, new: dict) -> None:
    assert strip(old) == strip(new)


def main() -> None:
    write = "--write" in sys.argv
    files = [p for p in Path(".").rglob("*.yml")
             if p.name in ("ROOM.yml", "GLANCE.yml") and "temp" not in p.parts
             and (p.parent / "ROOM.yml").exists()]
    n = 0
    for p in sorted(files):
        try:
            old = yaml.safe_load(p.read_text())
        except yaml.YAMLError:
            continue
        new_text = migrate(p)
        if new_text is None:
            continue
        new = yaml.safe_load(new_text)
        if isinstance(old, dict):
            check(old, new)
        n += 1
        if write:
            p.write_text(new_text)
        elif "-v" in sys.argv:
            for ln in new_text.splitlines():
                if LIGHT.match(ln):
                    print(f"{p}: {ln.strip()}")
    print(f"{'wrote' if write else 'would change'} {n} files")


main()
