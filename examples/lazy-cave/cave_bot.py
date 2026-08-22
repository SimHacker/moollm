#!/usr/bin/env python3
"""
Cave bot — drops pebbles, deduces the map, finds treasure.

Classic all-alike maze strategy: mark chambers with inventory items,
explore unknown passages, backtrack over the graph you learned.
Works with skew links (return direction != opposite) and one-way traps.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from lazy_cave import DIRECTIONS, LazyCave, normalize_direction


@dataclass
class BotReport:
    steps: int = 0
    pebbles_used: int = 0
    rooms_marked: int = 0
    treasure_found: bool = False
    treasure_label: str | None = None
    log: list[str] = field(default_factory=list)

    def note(self, msg: str, verbose: bool) -> None:
        self.log.append(msg)
        if verbose:
            print(msg)


class CaveBot:
    """DFS explorer with pebble breadcrumbs and BFS backtracking."""

    def __init__(self, cave: LazyCave, *, verbose: bool = False) -> None:
        self.cave = cave
        self.verbose = verbose
        self.report = BotReport()
        self.graph: dict[str, dict[str, str]] = {}
        self.dead: dict[str, set[str]] = {}
        self.oneway_from: set[tuple[str, str]] = set()
        self.visited: set[str] = set()
        self.true_id: dict[str, str] = {}

    def _label(self) -> str:
        return self.cave.room_label()

    def _sync_true_id(self, label: str) -> None:
        true = self.cave.state.player
        self.true_id[label] = true

    def _observe(self) -> dict[str, Any]:
        return self.cave.observe()

    def _mark_if_needed(self, label: str) -> None:
        if not self.cave.config.needs_pebbles:
            return
        obs = self._observe()
        if obs["drops"]:
            return
        inv = obs["inventory"]
        if not inv:
            self.report.note(f"{label}: no pebbles left to mark", self.verbose)
            return
        item = inv[0]
        self.cave.drop(item)
        self.report.pebbles_used += 1
        self.report.rooms_marked += 1
        self.report.steps += 1
        new_label = self.cave.room_label()
        self.true_id[new_label] = self.cave.state.player
        self.report.note(f"marked {new_label} (dropped {item})", self.verbose)

    def _record_edge(self, src: str, direction: str, dst: str, oneway: bool) -> None:
        direction = normalize_direction(direction)
        self.graph.setdefault(src, {})[direction] = dst
        if oneway:
            self.oneway_from.add((src, direction))
        elif direction not in self.graph.get(dst, {}):
            rev = self._find_return(dst, src)
            if rev:
                self.graph.setdefault(dst, {})[rev] = src

    def _find_return(self, at: str, target: str) -> str | None:
        for d, dest in self.graph.get(at, {}).items():
            if dest == target:
                return d
        return None

    def _learn_from_observation(self, label: str) -> None:
        obs = self._observe()
        for d, dest_true in obs["exits"].items():
            dest_label = self._label_for_true(dest_true)
            if dest_label:
                self.graph.setdefault(label, {})[normalize_direction(d)] = dest_label
        for d in obs["dead_ends"]:
            self.dead.setdefault(label, set()).add(normalize_direction(d))

    def _label_for_true(self, true_id: str) -> str | None:
        for label, tid in self.true_id.items():
            if tid == true_id:
                return label
        block = self.cave.read_room(true_id)
        room = block.get("room") or block
        if slug := room.get("description_slug"):
            return str(slug)
        drops = room.get("drops") or []
        if drops:
            return drops[-1]
        return None

    def _move(self, direction: str) -> dict[str, Any]:
        self.report.steps += 1
        src = self._label()
        result = self.cave.move(direction)
        dst = self._label()
        self._sync_true_id(dst)

        if result.get("ok"):
            oneway = bool(result.get("oneway"))
            self._record_edge(src, direction, dst, oneway)
            self.visited.add(dst)
            action = result.get("action", "walk")
            self.report.note(
                f"{src} --{direction}--> {dst} ({action})",
                self.verbose,
            )
            if result.get("treasure_placed"):
                self.report.note(
                    f"treasure placed (engine says {result.get('treasure_room')})",
                    self.verbose,
                )
        else:
            self.dead.setdefault(src, set()).add(normalize_direction(direction))
            self.report.note(
                f"{src} :: {direction} walled ({result.get('reason')})",
                self.verbose,
            )
        return result

    def _path_to(self, start: str, goal: str) -> list[str] | None:
        if start == goal:
            return []
        queue: deque[tuple[str, list[str]]] = deque([(start, [])])
        seen = {start}
        while queue:
            node, path = queue.popleft()
            for direction, nxt in self.graph.get(node, {}).items():
                if (node, direction) in self.oneway_from and path:
                    continue
                if nxt in seen:
                    continue
                new_path = path + [direction]
                if nxt == goal:
                    return new_path
                seen.add(nxt)
                queue.append((nxt, new_path))
        return None

    def _walk_path(self, directions: list[str]) -> None:
        for d in directions:
            self._move(d)

    def _unexplored_directions(self, label: str) -> list[str]:
        known = set(self.graph.get(label, {}))
        known |= self.dead.get(label, set())
        return [d for d in DIRECTIONS if d not in known]

    def _known_unvisited_neighbors(self, label: str) -> list[tuple[str, str]]:
        out = []
        for d, nxt in self.graph.get(label, {}).items():
            if nxt not in self.visited:
                out.append((d, nxt))
        return out

    def explore(self, max_steps: int = 500) -> BotReport:
        start = self._label()
        self._sync_true_id(start)
        self.visited.add(start)
        self._mark_if_needed(start)
        stack: list[str] = [start]

        while stack and self.report.steps < max_steps:
            label = stack[-1]
            self._learn_from_observation(label)

            obs = self._observe()
            if obs["treasure_visible"]:
                self.report.treasure_found = True
                self.report.treasure_label = label
                self.report.note(f"TREASURE at {label}", self.verbose)
                return self.report

            for direction in self._unexplored_directions(label):
                if self.report.steps >= max_steps:
                    break
                before = self.cave.state.player
                result = self._move(direction)
                after_label = self._label()
                if result.get("ok"):
                    self._mark_if_needed(after_label)
                    obs2 = self._observe()
                    if obs2["treasure_visible"]:
                        self.report.treasure_found = True
                        self.report.treasure_label = after_label
                        self.report.note(f"TREASURE at {after_label}", self.verbose)
                        return self.report
                    stack.append(after_label)
                    break
                self.cave.state.player = before
            else:
                stack.pop()
                if not stack:
                    break
                target = stack[-1]
                path = self._path_to(label, target)
                if path is None:
                    self.report.note(
                        f"stuck at {label}, cannot return to {target}",
                        self.verbose,
                    )
                    break
                self._walk_path(path)

        if not self.report.treasure_found and self.cave.state.treasure_room:
            self.report.note(
                f"out of steps; treasure is in {self.cave.state.treasure_room} "
                f"(bot may not have reached it)",
                self.verbose,
            )
        return self.report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pebbled maze solver for lazy caves"
    )
    parser.add_argument("path", type=Path, help="Cave instance directory")
    parser.add_argument("--max-steps", type=int, default=500)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--log-json", type=Path, default=None)
    args = parser.parse_args()

    cave = LazyCave(args.path)
    bot = CaveBot(cave, verbose=args.verbose)
    report = bot.explore(max_steps=args.max_steps)

    summary = {
        "steps": report.steps,
        "pebbles_used": report.pebbles_used,
        "rooms_marked": report.rooms_marked,
        "treasure_found": report.treasure_found,
        "treasure_label": report.treasure_label,
        "engine_treasure_room": cave.state.treasure_room,
        "graph": bot.graph,
    }
    print(json.dumps(summary, indent=2))
    if args.log_json:
        args.log_json.write_text(json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
