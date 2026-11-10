# Envelope eleven

Flattened 2026-10-29. Each file still had one column-0 envelope mapping. No key appeared both inside that mapping and beside it, so nothing was skipped. `skills/prototype/scripts/flatten.py` `flatten_text` removed the envelope line and dedented its block to that column. None of these envelope lines had a trailing comment. `yaml.safe_load` of each result equals `resolve.flat` of the original: the same document with the wrapper key removed. Keys outside the envelope were left as they stood.

`flatten_text` takes the key as an argument. `resolve.envelope_key` returns `topology` for `TOPOLOGY.yml` and `export` for `EXPORT.yml` from the filename stem, so those two used the same function as the rest.

The three old mannequin `object:` envelopes are the coatroom files under `examples/old/adventure-1`, `adventure-2`, and `adventure-3`. No other `*mannequin*` file in this repo has a column-0 `object:`.

## Flattened

- `archive/sim-obliterator/skill/CARD.yml` — `card:`. Outside, untouched: `sister_repo`, `methods`, `advertisements`, `lineage`, `related`, `tools`.
- `skills/experiment/experiments/turing-chess/characters/slats/CHARACTER.yml` — `character:`. The mapping was the whole document.
- `skills/experiment/experiments/fluxx-chaos/engine/DEALER.yml` — `dealer:`. Outside, untouched: `deck_exhaustion`, `deck_state`, `dramatic_timing`, `extension_points`, `forever_game`, `game_termination`, `handle_shuffle`, `modes`, `runtime`, `selection_algorithms`.
- `skills/no-ai-ideology/EXPORT.yml` — `export:`. Outside, untouched: `skills`, `dependencies`, `dependency_graph`, `installation`, `statistics`.
- `examples/old/adventure-3/kitchen/fridge.yml` — `object:`. Outside, untouched: `eat_mechanic`.
- `examples/old/adventure-3/kitchen/tomtomagotchi.yml` — `object:`. The mapping was the whole document.
- `examples/old/adventure-3/coatroom/mannequin.yml` — `object:`. The mapping was the whole document.
- `examples/old/adventure-2/coatroom/mannequin.yml` — `object:`. The mapping was the whole document.
- `examples/old/adventure-1/coatroom/mannequin.yml` — `object:`. The mapping was the whole document.
- `examples/old/adventure-3/pub/ROOM.yml` — `room:`. The mapping was the whole document.
- `skills/room/TOPOLOGY.yml` — `topology:`. Outside, untouched: `compass`, `cardinal`, `diagonal`, `grid`, `connectivity`, `generation`, `memory_palace`, `rules`, `urban_planning`.

## Skipped

None.
