#!/usr/bin/env python3
"""
Lazy cave — roll the dungeon as you explore.

Rooms start unlinked and (by default) all alike. Drop pebbles to tell them
apart. First step in a direction hooks a passage on the fly — two-way but
not necessarily opposite (north here may meet east there). One-way mode
available for extra cruelty.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

OPPOSITE = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
    "northeast": "southwest",
    "northwest": "southeast",
    "southeast": "northwest",
    "southwest": "northeast",
    "ne": "sw",
    "nw": "se",
    "se": "nw",
    "sw": "ne",
    "up": "down",
    "down": "up",
    "in": "out",
    "out": "in",
}

ALIASES = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "ne": "northeast",
    "nw": "northwest",
    "se": "southeast",
    "sw": "southwest",
    "u": "up",
    "d": "down",
}

DIRECTIONS = [
    "north",
    "south",
    "east",
    "west",
    "up",
    "down",
    "ne",
    "nw",
    "se",
    "sw",
]

ALIKE_DESCRIPTION = (
    "You are in a maze of twisty little passages, all alike."
)

# Woods/Knuth word-bag permutations — each room its own coordinate (all-different).
CANON_DIFFERENT = [
    "You are in a maze of twisty little passages, all different.",
    "You are in a maze of twisting little passages, all different.",
    "You are in a little maze of twisty passages, all different.",
    "You are in a twisting maze of little passages, all different.",
    "You are in a twisting little maze of passages, all different.",
    "You are in a twisty little maze of passages, all different.",
    "You are in a twisty maze of little passages, all different.",
    "You are in a little twisty maze of passages, all different.",
    "You are in a maze of little twisting passages, all different.",
    "You are in a maze of little twisty passages, all different.",
    "You are in a little maze of twisting passages, all different.",
]


def build_different_descriptions(max_count: int, rng: random.Random) -> list[str]:
    pool = list(CANON_DIFFERENT)
    seen = set(pool)
    for adj1, adj2 in itertools.permutations(
        ["twisty", "twisting", "little", "narrow", "windy"], 2
    ):
        for noun in ("maze", "passage", "passages"):
            line = f"You are in a {adj1} {noun} of {adj2} passages, all different."
            if line not in seen:
                seen.add(line)
                pool.append(line)
            if len(pool) >= max_count:
                return pool[:max_count]
    rng.shuffle(pool[len(CANON_DIFFERENT) :])
    return pool[:max_count]


def normalize_direction(raw: str) -> str:
    d = raw.strip().lower()
    return ALIASES.get(d, d)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def room_dir(cave_root: Path, room_id: str) -> Path:
    return cave_root / "rooms" / room_id


def room_yml(cave_root: Path, room_id: str) -> Path:
    return room_dir(cave_root, room_id) / "ROOM.yml"


@dataclass
class CaveConfig:
    name: str = "lazy-cave"
    start: str = "start"
    initial_rooms: int = 10
    max_rooms: int = 24
    link_mode: str = "scored"
    link_attach: str = "skew"
    oneway_chance: float = 0.0
    pick_top_n: int = 3
    room_voice: str = "alike"
    starting_pebbles: int = 8
    treasure_object: str = "treasure.yml"
    seed: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CaveConfig:
        cave = data.get("cave") or data
        gen = cave.get("generator") or {}
        room_voice = gen.get("room_voice")
        if room_voice is None:
            identical = gen.get("identical_rooms", True)
            room_voice = "alike" if identical else "different"
        return cls(
            name=cave.get("name", "lazy-cave"),
            start=cave.get("start", "start"),
            initial_rooms=int(gen.get("initial_rooms", 10)),
            max_rooms=int(gen.get("max_rooms", 24)),
            link_mode=str(gen.get("link_mode", "scored")),
            link_attach=str(gen.get("link_attach", "skew")),
            oneway_chance=float(gen.get("oneway_chance", 0.0)),
            pick_top_n=int(gen.get("pick_top_n", 3)),
            room_voice=str(room_voice),
            starting_pebbles=int(gen.get("starting_pebbles", 8)),
            treasure_object=str(gen.get("treasure_object", "treasure.yml")),
            seed=gen.get("seed"),
        )

    @property
    def alike(self) -> bool:
        return self.room_voice == "alike"

    @property
    def needs_pebbles(self) -> bool:
        return self.alike


@dataclass
class CaveState:
    player: str
    links_made: int = 0
    rooms_spawned: int = 0
    treasure_room: str | None = None
    dead_ends: dict[str, list[str]] = field(default_factory=dict)
    inventory: list[str] = field(default_factory=list)
    visited: list[str] = field(default_factory=list)
    oneway_edges: list[dict[str, str]] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path, default_player: str, pebbles: int) -> CaveState:
        raw = load_yaml(path).get("state") or {}
        inv = raw.get("inventory")
        if inv is None:
            inv = [f"pebble-{i}" for i in range(1, pebbles + 1)]
        visited = raw.get("visited") or [default_player]
        return cls(
            player=raw.get("player", default_player),
            links_made=int(raw.get("links_made", 0)),
            rooms_spawned=int(raw.get("rooms_spawned", 0)),
            treasure_room=raw.get("treasure_room"),
            dead_ends=raw.get("dead_ends") or {},
            inventory=list(inv),
            visited=list(visited),
            oneway_edges=raw.get("oneway_edges") or [],
        )

    def save(self, path: Path) -> None:
        save_yaml(
            path,
            {
                "state": {
                    "player": self.player,
                    "links_made": self.links_made,
                    "rooms_spawned": self.rooms_spawned,
                    "treasure_room": self.treasure_room,
                    "dead_ends": self.dead_ends,
                    "inventory": self.inventory,
                    "visited": self.visited,
                    "oneway_edges": self.oneway_edges,
                }
            },
        )

    def note_visit(self, room_id: str) -> None:
        if room_id not in self.visited:
            self.visited.append(room_id)


class LazyCave:
    def __init__(self, cave_root: Path) -> None:
        self.root = cave_root.resolve()
        self.config = CaveConfig.from_dict(load_yaml(self.root / "CAVE.yml"))
        self.state_path = self.root / "CAVE-STATE.yml"
        self.state = CaveState.load(
            self.state_path,
            self.config.start,
            self.config.starting_pebbles,
        )
        self.rng = random.Random(self.config.seed)
        self._desc_pool = build_different_descriptions(
            self.config.max_rooms, self.rng
        )

    def assign_room_voice(self, block: dict[str, Any], slot: int, *, entrance: bool = False) -> None:
        block["voice"] = self.config.room_voice
        if self.config.alike:
            block["description"] = ALIKE_DESCRIPTION
            return
        block["description_slug"] = f"diff-{slot:02d}"
        if entrance and slot == 0:
            block["description"] = (
                "You are at the cave mouth. Passages are not carved yet — "
                "walk and the walls will decide. (Twisty little passages "
                "ahead, all different.)"
            )
        else:
            block["description"] = self._desc_pool[slot % len(self._desc_pool)]

    def list_rooms(self) -> list[str]:
        rooms_dir = self.root / "rooms"
        if not rooms_dir.is_dir():
            return []
        return sorted(
            p.name
            for p in rooms_dir.iterdir()
            if p.is_dir() and (p / "ROOM.yml").exists()
        )

    def read_room(self, room_id: str) -> dict[str, Any]:
        return load_yaml(room_yml(self.root, room_id))

    def write_room(self, room_id: str, data: dict[str, Any]) -> None:
        save_yaml(room_yml(self.root, room_id), data)

    def room_block(self, room_id: str) -> dict[str, Any]:
        room = self.read_room(room_id)
        return room.setdefault("room", room)

    def exits(self, room_id: str) -> dict[str, Any]:
        return self.room_block(room_id).get("exits") or {}

    def drops(self, room_id: str) -> list[str]:
        return list(self.room_block(room_id).get("drops") or [])

    def link_count(self, room_id: str) -> int:
        return sum(
            1 for d in self.exits(room_id) if self.destination(room_id, d)
        )

    def is_linked(self, room_id: str) -> bool:
        return self.link_count(room_id) > 0

    def unlinked_rooms(self) -> list[str]:
        return [r for r in self.list_rooms() if not self.is_linked(r)]

    def destination(self, room_id: str, direction: str) -> str | None:
        direction = normalize_direction(direction)
        spec = self.exits(room_id).get(direction)
        if spec is None:
            return None
        if isinstance(spec, str):
            text = spec.strip()
            return text.split("/")[0].strip() if text else None
        if isinstance(spec, dict):
            dest = spec.get("destination") or spec.get("to")
            if dest:
                return str(dest).strip("/").split("/")[-1]
        return None

    def is_oneway(self, room_id: str, direction: str) -> bool:
        direction = normalize_direction(direction)
        spec = self.exits(room_id).get(direction)
        return isinstance(spec, dict) and bool(spec.get("oneway"))

    def is_dead_end(self, room_id: str, direction: str) -> bool:
        direction = normalize_direction(direction)
        return direction in (self.state.dead_ends.get(room_id) or [])

    def mark_dead_end(self, room_id: str, direction: str) -> None:
        direction = normalize_direction(direction)
        ends = self.state.dead_ends.setdefault(room_id, [])
        if direction not in ends:
            ends.append(direction)

    def bfs_distance(self, start: str, goal: str) -> int:
        if start == goal:
            return 0
        seen = {start}
        frontier = [(start, 0)]
        while frontier:
            node, dist = frontier.pop(0)
            for direction in self.exits(node):
                nxt = self.destination(node, direction)
                if not nxt or nxt in seen:
                    continue
                if nxt == goal:
                    return dist + 1
                seen.add(nxt)
                frontier.append((nxt, dist + 1))
        return 999

    def room_theme(self, room_id: str) -> str:
        block = self.room_block(room_id)
        return str(block.get("theme") or block.get("name") or room_id)

    def drop_count(self, room_id: str) -> int:
        return len(self.drops(room_id))

    def free_directions(self, room_id: str) -> list[str]:
        exits = self.exits(room_id)
        free = [
            d
            for d in exits
            if not self.destination(room_id, d)
        ]
        if not exits:
            return list(DIRECTIONS)
        used = set(exits)
        free.extend(d for d in DIRECTIONS if d not in used)
        return free or list(DIRECTIONS)

    def pick_attach_direction(self, target: str, avoid: str | None = None) -> str:
        attach = self.config.link_attach
        if attach == "opposite" and avoid and OPPOSITE.get(avoid):
            opp = OPPOSITE[avoid]
            free = self.free_directions(target)
            if opp in free:
                return opp
        free = self.free_directions(target)
        if avoid and len(free) > 1:
            filtered = [d for d in free if d != avoid]
            if filtered:
                free = filtered
        return self.rng.choice(free)

    def use_oneway(self) -> bool:
        attach = self.config.link_attach
        if attach == "oneway":
            return True
        if attach == "mixed":
            return self.rng.random() < self.config.oneway_chance
        return False

    def eligible_targets(self, from_room: str, direction: str) -> list[str]:
        direction = normalize_direction(direction)
        opposite = OPPOSITE.get(direction)
        candidates: list[str] = []

        for rid in self.list_rooms():
            if rid == from_room:
                continue
            if self.config.link_mode == "opposite" and opposite:
                free = self.free_directions(rid)
                if opposite in free or not self.exits(rid):
                    candidates.append(rid)
            else:
                if self.free_directions(rid) or not self.is_linked(rid):
                    candidates.append(rid)

        return candidates

    def score_candidate(self, from_room: str, direction: str, target: str) -> float:
        score = self.rng.random() * 0.01
        if self.config.link_mode in ("scored", "skew"):
            score += max(0, 10 - self.bfs_distance(from_room, target))
            if self.room_theme(from_room) == self.room_theme(target):
                score += 1
            score += self.drop_count(target) * 3.0
            if not self.is_linked(target):
                score += 1
            if self.drop_count(from_room):
                score -= 0.5
        return score

    def pick_target(self, from_room: str, direction: str) -> str | None:
        candidates = self.eligible_targets(from_room, direction)
        if not candidates:
            return None
        if self.config.link_mode in ("scored", "skew"):
            ranked = sorted(
                candidates,
                key=lambda t: self.score_candidate(from_room, direction, t),
                reverse=True,
            )
            top = ranked[: max(1, self.config.pick_top_n)]
            return self.rng.choice(top)
        return self.rng.choice(candidates)

    def next_room_id(self) -> str:
        existing = self.list_rooms()
        for i in range(1, self.config.max_rooms + 1):
            rid = f"room-{i:02d}"
            if rid not in existing:
                return rid
        return f"room-{len(existing) + 1:02d}"

    def spawn_room(self, room_id: str | None = None) -> str:
        if self.state.rooms_spawned >= self.config.max_rooms:
            raise RuntimeError("max_rooms reached")
        prototype = self.root / "ROOM.prototype.yml"
        if not prototype.exists():
            raise FileNotFoundError(f"missing prototype: {prototype}")
        rid = room_id or self.next_room_id()
        dest = room_dir(self.root, rid)
        if dest.exists():
            raise FileExistsError(dest)
        dest.mkdir(parents=True)
        shutil.copy2(prototype, dest / "ROOM.yml")
        data = self.read_room(rid)
        block = data.setdefault("room", data)
        slot = len(self.list_rooms())
        block["internal_id"] = rid
        self.assign_room_voice(block, slot)
        block["theme"] = block.get("theme", f"spawn-{self.state.rooms_spawned + 1}")
        self.write_room(rid, data)
        self.state.rooms_spawned += 1
        return rid

    def set_exit(
        self,
        room_id: str,
        direction: str,
        other: str,
        *,
        oneway: bool = False,
    ) -> None:
        direction = normalize_direction(direction)
        data = self.read_room(room_id)
        block = data.setdefault("room", data)
        exits = block.setdefault("exits", {})
        prev = exits.get(direction)
        desc = ""
        if isinstance(prev, dict):
            desc = prev.get("description") or ""
        spec: dict[str, Any] = {
            "destination": f"../{other}/",
            "description": desc or f"A passage leading {direction}.",
        }
        if oneway:
            spec["oneway"] = True
        exits[direction] = spec
        self.write_room(room_id, data)

    def connect(self, a: str, dir_a: str, b: str, dir_b: str | None, oneway: bool) -> None:
        dir_a = normalize_direction(dir_a)
        if dir_b is None:
            dir_b = self.pick_attach_direction(b, avoid=OPPOSITE.get(dir_a))
        dir_b = normalize_direction(dir_b)

        self.set_exit(a, dir_a, b, oneway=oneway)
        if not oneway:
            self.set_exit(b, dir_b, a, oneway=False)
        else:
            self.state.oneway_edges.append(
                {"from": a, "direction": dir_a, "to": b}
            )
        self.state.links_made += 1

    def maybe_place_treasure(self, room_id: str) -> bool:
        if self.state.treasure_room:
            return False
        unlinked = self.unlinked_rooms()
        if len(unlinked) == 1 and unlinked[0] == room_id:
            self._install_treasure(room_id)
            return True
        if len(unlinked) == 0 and self.link_count(room_id) == 1:
            self._install_treasure(room_id)
            return True
        return False

    def _install_treasure(self, room_id: str) -> None:
        src = self.root / "objects" / self.config.treasure_object
        if src.exists():
            dest_dir = room_dir(self.root, room_id)
            shutil.copy2(src, dest_dir / self.config.treasure_object)
        data = self.read_room(room_id)
        block = data.setdefault("room", data)
        name = self.config.treasure_object
        objs = block.setdefault("objects", [])
        if name not in objs:
            objs.append(name)
        notes = block.setdefault("annotations", [])
        notes.append("Treasure materialized — last room to join the graph.")
        self.write_room(room_id, data)
        self.state.treasure_room = room_id

    def move(self, direction: str) -> dict[str, Any]:
        direction = normalize_direction(direction)
        here = self.state.player

        if self.is_dead_end(here, direction):
            return {
                "ok": False,
                "reason": "dead_end",
                "room": here,
                "direction": direction,
                "message": f"No passage {direction} — you already found a wall there.",
            }

        dest = self.destination(here, direction)
        if dest and dest in self.list_rooms():
            self.state.player = dest
            self.state.note_visit(dest)
            self.state.save(self.state_path)
            back = OPPOSITE.get(direction, "?")
            hint = ""
            if self.is_oneway(here, direction):
                hint = " (one-way — no return through this passage)"
            return {
                "ok": True,
                "action": "walk",
                "from": here,
                "to": dest,
                "direction": direction,
                "message": f"You go {direction}." + hint,
            }

        target = self.pick_target(here, direction)
        spawn = False
        if target is None and self.state.rooms_spawned < self.config.max_rooms:
            try:
                target = self.spawn_room()
                spawn = True
            except (RuntimeError, FileExistsError):
                target = None

        if target is None:
            self.mark_dead_end(here, direction)
            self.state.save(self.state_path)
            return {
                "ok": False,
                "reason": "dead_end",
                "room": here,
                "direction": direction,
                "message": f"You feel a solid wall {direction}. Dead end.",
            }

        oneway = self.use_oneway()
        attach = None if self.config.link_attach == "opposite" else None
        if self.config.link_attach == "opposite":
            attach = OPPOSITE.get(direction, "south")
        else:
            attach = self.pick_attach_direction(target, avoid=OPPOSITE.get(direction))

        was_unlinked = not self.is_linked(target)
        self.connect(here, direction, target, attach, oneway=oneway)
        placed = was_unlinked and self.maybe_place_treasure(target)
        self.state.player = target
        self.state.note_visit(target)
        self.state.save(self.state_path)

        link_desc = f"{here}.{direction} -> {target}.{attach}"
        if oneway:
            link_desc += " (ONE-WAY)"
        return {
            "ok": True,
            "action": "link_and_walk",
            "from": here,
            "to": target,
            "direction": direction,
            "attach": attach,
            "oneway": oneway,
            "spawned": spawn,
            "treasure_placed": placed,
            "treasure_room": self.state.treasure_room,
            "links_made": self.state.links_made,
            "link": link_desc,
            "message": (
                f"You grope {direction}; the cave gives way into another chamber"
                f"{', all alike' if self.config.alike else ''}."
                f"{(' Something glints.' if placed else '')}"
                + (" The passage will not take you back." if oneway else "")
            ),
        }

    def drop(self, item: str) -> dict[str, Any]:
        here = self.state.player
        if item not in self.state.inventory:
            return {
                "ok": False,
                "message": f"You aren't carrying {item}.",
            }
        self.state.inventory.remove(item)
        block = self.room_block(here)
        drops = block.setdefault("drops", [])
        drops.append(item)
        self.write_room(here, self.read_room(here))
        self.state.save(self.state_path)
        return {
            "ok": True,
            "message": (
                f"You drop {item}. It joins the floor — your breadcrumb in a "
                f"sea of identical passages."
            ),
        }

    def look(self) -> dict[str, Any]:
        here = self.state.player
        block = self.room_block(here)
        desc = block.get("description") or ALIKE_DESCRIPTION
        drops = self.drops(here)
        exits = {
            d: self.destination(here, d)
            for d in self.exits(here)
            if self.destination(here, d)
        }
        dead = self.state.dead_ends.get(here, [])
        lines = [desc, ""]
        if self.config.alike:
            lines.append(
                f"[internal id: {block.get('internal_id', here)} — for your map notes]"
            )
        elif block.get("description_slug"):
            lines.append(f"[{block['description_slug']}]")
        if drops:
            lines.append("")
            lines.append("On the floor: " + ", ".join(drops))
        if exits:
            lines.append("")
            lines.append("Passages:")
            for d, dest in sorted(exits.items()):
                arrow = " (one-way)" if self.is_oneway(here, d) else ""
                lines.append(f"  {d} -> {dest}{arrow}")
        if dead:
            lines.append("")
            lines.append("Walled directions: " + ", ".join(dead))
        objs = block.get("objects") or []
        if objs:
            lines.append("")
            lines.append("Objects here: " + ", ".join(str(o) for o in objs))
        return {"ok": True, "message": "\n".join(lines), "room": here}

    def map_notes(self) -> dict[str, Any]:
        graph: dict[str, dict[str, str]] = {}
        for rid in self.state.visited:
            graph[rid] = {}
            for d in self.exits(rid):
                dest = self.destination(rid, d)
                if dest:
                    tag = d
                    if self.is_oneway(rid, d):
                        tag = f"{d} (1w)"
                    graph[rid][tag] = dest
            drops = self.drops(rid)
            if drops:
                graph[rid]["__drops__"] = ", ".join(drops)
            dead = self.state.dead_ends.get(rid, [])
            if dead:
                graph[rid]["__walls__"] = ", ".join(dead)

        lines = [
            "Your deduced map (visited rooms only):",
            (
                "Drop pebbles to tell chambers apart — descriptions lie."
                if self.config.alike
                else "Read descriptions carefully — each chamber is its own coordinate."
            ),
            "",
        ]
        for rid in self.state.visited:
            block = self.room_block(rid)
            title = block.get("description_slug") or rid
            if not self.config.alike and block.get("description"):
                title = block["description_slug"] or title
            lines.append(f"=== {title} ===")
            info = graph.get(rid, {})
            if "__drops__" in info:
                lines.append(f"  drops: {info.pop('__drops__')}")
            if "__walls__" in info:
                lines.append(f"  walls: {info.pop('__walls__')}")
            for d, dest in sorted(info.items()):
                lines.append(f"  {d} -> {dest}")
            if not info and "__drops__" not in graph.get(rid, {}):
                lines.append("  (no exits recorded yet)")
            lines.append("")

        if self.state.oneway_edges:
            lines.append("Known one-way links:")
            for e in self.state.oneway_edges:
                lines.append(
                    f"  {e['from']} --{e['direction']}--> {e['to']}"
                )

        return {"ok": True, "message": "\n".join(lines).rstrip(), "graph": graph}

    def status(self) -> dict[str, Any]:
        here = self.state.player
        block = self.room_block(here)
        return {
            "room": here,
            "internal_id": block.get("internal_id", here),
            "inventory": list(self.state.inventory),
            "drops_here": self.drops(here),
            "exits": {
                d: self.destination(here, d)
                for d in self.exits(here)
                if self.destination(here, d)
            },
            "dead_ends": self.state.dead_ends.get(here, []),
            "visited": list(self.state.visited),
            "links_made": self.state.links_made,
            "treasure_room": self.state.treasure_room,
            "unlinked_remaining": len(self.unlinked_rooms()),
            "link_attach": self.config.link_attach,
            "room_voice": self.config.room_voice,
            "description_slug": block.get("description_slug"),
        }

    def observe(self) -> dict[str, Any]:
        """Structured senses for bots — no internal room id in alike mode."""
        here = self.state.player
        block = self.room_block(here)
        objs = [str(o) for o in (block.get("objects") or [])]
        return {
            "drops": list(self.drops(here)),
            "description": block.get("description", ""),
            "description_slug": block.get("description_slug"),
            "room_voice": self.config.room_voice,
            "needs_pebbles": self.config.needs_pebbles,
            "exits": {
                d: self.destination(here, d)
                for d in self.exits(here)
                if self.destination(here, d)
            },
            "dead_ends": list(self.state.dead_ends.get(here, [])),
            "objects": objs,
            "inventory": list(self.state.inventory),
            "treasure_visible": any(
                "treasure" in o.lower() for o in objs
            ),
        }

    def room_label(self) -> str:
        """Bot/human coordinate: pebble, description slug, or anonymous."""
        block = self.room_block(self.state.player)
        if not self.config.alike:
            slug = block.get("description_slug")
            if slug:
                return str(slug)
        drops = self.drops(self.state.player)
        if drops:
            return drops[-1]
        return "@anon"


def init_cave(
    cave_root: Path,
    count: int,
    start: str = "start",
    seed: int | None = None,
) -> None:
    cave_root.mkdir(parents=True, exist_ok=True)
    (cave_root / "rooms").mkdir(exist_ok=True)
    (cave_root / "objects").mkdir(exist_ok=True)

    template_root = Path(__file__).resolve().parent
    for name in ("ROOM.prototype.yml", "CAVE.yml"):
        src = template_root / name
        dst = cave_root / name
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)

    treasure = cave_root / "objects" / "treasure.yml"
    if not treasure.exists():
        src = template_root / "objects" / "treasure.yml"
        if src.exists():
            shutil.copy2(src, treasure)

    rooms_dir = cave_root / "rooms"
    ids = [start] + [f"room-{i:02d}" for i in range(1, count)]
    proto = cave_root / "ROOM.prototype.yml"

    cfg_path = cave_root / "CAVE.yml"
    cfg = CaveConfig.from_dict(load_yaml(cfg_path))
    rng = random.Random(seed if seed is not None else cfg.seed)
    desc_pool = build_different_descriptions(cfg.max_rooms, rng)

    for slot, rid in enumerate(ids):
        rdir = rooms_dir / rid
        if rdir.exists():
            continue
        rdir.mkdir()
        shutil.copy2(proto, rdir / "ROOM.yml")
        data = load_yaml(rdir / "ROOM.yml")
        block = data.setdefault("room", data)
        block["internal_id"] = rid
        block["voice"] = cfg.room_voice
        if cfg.alike:
            block["description"] = ALIKE_DESCRIPTION
        else:
            block["description_slug"] = f"diff-{slot:02d}"
            if rid == start:
                block["description"] = (
                    "You are at the cave mouth. Passages are not carved yet — "
                    "walk and the walls will decide. (Twisty little passages "
                    "ahead, all different.)"
                )
                block["start"] = True
            else:
                block["description"] = desc_pool[slot % len(desc_pool)]
        if rid == start:
            block.setdefault("start", True)
        save_yaml(rdir / "ROOM.yml", data)

    state_path = cave_root / "CAVE-STATE.yml"
    pebbles = cfg.starting_pebbles if cfg.needs_pebbles else 0
    CaveState(
        start,
        rooms_spawned=len(ids),
        inventory=[f"pebble-{i}" for i in range(1, pebbles + 1)] if pebbles else [],
        visited=[start],
    ).save(state_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Lazy cave — roll links as you walk")
    sub = parser.add_subparsers(dest="cmd", required=True)

    init_p = sub.add_parser("init", help="Create cave with N unlinked rooms")
    init_p.add_argument("path", type=Path)
    init_p.add_argument("-n", "--rooms", type=int, default=10)
    init_p.add_argument("--start", default="start")
    init_p.add_argument("--seed", type=int, default=None)
    init_p.add_argument(
        "--voice",
        choices=("alike", "different"),
        default=None,
        help="room_voice dimension (default from CAVE.yml)",
    )

    go_p = sub.add_parser("go", help="Move in a direction")
    go_p.add_argument("path", type=Path)
    go_p.add_argument("direction")

    drop_p = sub.add_parser("drop", help="Drop a breadcrumb item")
    drop_p.add_argument("path", type=Path)
    drop_p.add_argument("item")

    for name in ("look", "map", "status"):
        sub.add_parser(name, help=f"{name} command").add_argument("path", type=Path)

    args = parser.parse_args()
    if args.cmd == "init":
        args.path.mkdir(parents=True, exist_ok=True)
        if args.voice:
            cave_yml = args.path / "CAVE.yml"
            if not cave_yml.exists():
                template = Path(__file__).resolve().parent / "CAVE.yml"
                if template.exists():
                    shutil.copy2(template, cave_yml)
            data = load_yaml(cave_yml)
            data.setdefault("cave", {}).setdefault("generator", {})[
                "room_voice"
            ] = args.voice
            save_yaml(cave_yml, data)
        init_cave(args.path, args.rooms, start=args.start, seed=args.seed)
        cfg = CaveConfig.from_dict(load_yaml(args.path / "CAVE.yml"))
        print(
            f"Initialized {args.path} with {args.rooms} rooms "
            f"(start={args.start}, room_voice={cfg.room_voice})"
        )
        return

    cave = LazyCave(args.path)
    if args.cmd == "go":
        result = cave.move(args.direction)
        print(result["message"])
        if result.get("link"):
            print(f"[linked {result['link']}]")
        if result.get("treasure_placed"):
            print(f"Treasure placed in {result['treasure_room']}")
        return

    if args.cmd == "drop":
        print(cave.drop(args.item)["message"])
        return

    if args.cmd == "look":
        print(cave.look()["message"])
        return

    if args.cmd == "map":
        print(cave.map_notes()["message"])
        return

    if args.cmd == "status":
        print(json.dumps(cave.status(), indent=2))


if __name__ == "__main__":
    main()
