# Lazy cave — roll the dungeon as you explore

Selfish maze generation: **no links until you walk.** Contrast with
[`../all-alike-maze/`](../all-alike-maze/) (pre-authored, one description) and
[`../all-different-maze/`](../all-different-maze/) (Latin square, eleven
descriptions).

## Room voice (`room_voice`) — a Korz dimension on perception

| Value | Descriptions | Navigation |
|---|---|---|
| `alike` | One inherited line — all chambers identical | **Drop pebbles** to deduce the map |
| `different` **(easier)** | Unique word-bag permutations per room (Woods/Knuth style) | **Read carefully** — description is the coordinate |

Legacy alias: `identical_rooms: true|false` maps to `alike`/`different`.

## Play loop

1. **Walk** — undefined direction carves a passage on the fly.
2. **Drop** (alike only) — pebble breadcrumbs.
3. **Look** — description, exits, drops, walled directions.
4. **Map** — deduced graph from visited rooms.
5. **Bot** — `python cave_bot.py ./my-cave` (skips pebbles in `different` mode).

## Link attachment (`link_attach`)

Two-way links; **north here is not necessarily south there**:

| Value | Behavior |
|---|---|
| `skew` **(default)** | A.dir → B.random-free-dir |
| `opposite` | A.dir → B.opposite — hallway cheat |
| `oneway` / `mixed` | traps |

## Quick start

```bash
cd examples/lazy-cave
python lazy_cave.py init ./my-cave -n 10 --voice different --seed 42
python lazy_cave.py look ./my-cave
python lazy_cave.py go ./my-cave north
python cave_bot.py ./my-cave -v
```

Hard alike mode:

```bash
python lazy_cave.py init ./hard-cave -n 10 --voice alike
python lazy_cave.py drop ./hard-cave pebble-1
```

## Treasure rule

Last room in the pool to receive its **first** link gets the chest.

## Korz reading

- `room_voice` = reader-dimension guard (how perception dispatches).
- `alike` = sparse shadow tree — player materializes distinguishing slots.
- `different` = anti-shadow — identity in prose permutation.
- Skew links = back is not `invert(dir)`.
