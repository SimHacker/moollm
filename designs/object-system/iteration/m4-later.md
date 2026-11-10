# M4 later

Survey of what M4 did not rename. No files were rewritten. Counted 2026-10-29 under `skills/` and `examples/`.

M4 (`m04_triggers.py`) opens a file only when its text contains `trigger`. Inside `advertisements:` it rescales a trigger entry's score and renames that entry's `response:` or `result:` to `say:`. Re-running that tally still reports 87 advertisement entries that have `response:` or `result:` and no `trigger:`. Those 87 are 55 copies inside one lint log and 32 live entries in 5 object files. The same live shape, with no `trigger` anywhere in the file, is another 118 entries in 26 files. M4 never opened them.

`say:` is the safe rename for the live advertisement entries only. The other buckets are a different job, or they already say `say:`.

## Search

Ripgrep, `skills/` and `examples/`, `*.yml`, `*.yaml`, `*.md`:

```
rg -e '^[[:space:]]*(-[[:space:]]+)?(response|result):'
```

773 lines, 218 files. `response:` 196, `result:` 577. 184 `.yml` files, 34 `.md` files, no `.yaml`.

The 773 is every matching line. An advertisement entry is a dict in an `advertisements:` collection, at any depth. Parsed every `.yml` and `.yaml` under those two trees (skipping `.git`, `node_modules`, `temp`, `.moollm`, `dist`, `build`, `__pycache__`). Parse failures: 0. That parse is what the counts below come from. Ripgrep cannot see whether the entry also has `trigger:`.

## 1. Live advertisement speech — safe to rename to `say:`

150 entries, 31 files. The entry has `response:` or `result:` and no `trigger:`. The value is a string, the line the object speaks or the result text of the offer (`LOOK` on the mirror, `WASH-DISHES` on the sink, `The stove is {state}.`).

112 are `result:`, and every one of those scores is already above 1. 38 are `response:`, and none of those has a score. No entry has both spellings. No entry also has `say:` or `effect:`. A few stove files are still list entries; renaming the field does not depend on making those lists into maps.

| Tree | Files | Entries |
|---|---:|---:|
| `examples/adventure-4` | 8 | 49 |
| `examples/old/adventure-1` | 7 | 23 |
| `examples/old/adventure-2` | 7 | 23 |
| `examples/old/adventure-3` | 9 | 55 |

32 of the plan's 87 are in this bucket, in the 5 files whose text also contains `trigger` because of a `secrets:` list: `examples/adventure-4/maze/room-g/carved-face.yml` (7), and the lamp-vendor or carved-face copies under `examples/old/adventure-1`, `adventure-2`, and `adventure-3`. The other 118 entries are the 26 files with no `trigger` substring.

Examples:

- `examples/adventure-4/coatroom/mirror.yml` — 19 `result:` entries, map keys such as `LOOK`
- `examples/adventure-4/kitchen/sink.yml` — `WASH-DISHES` and `DRINK`, `response:`
- `examples/adventure-4/kitchen/stove.yml` — list entries, `response:`

`export_advertisement` copies the entry's own keys through and does not fill `effect` from `response` or `result`. `adventure_runtime.py` reads `effect` only. Renaming these to `say:` matches the advertisement field M4 already renamed on trigger entries. It does not change what that runtime prints today.

## 2. Lint log — different job

55 entries, 1 file: `examples/adventure-4/LINTER.yml`. These are the other 55 of the 87. The file is a lint event log (`lint_ignore: true`, timestamp `2026-01-10`). The 55 sit on advertisement copies nested under `world_state`. Ripgrep finds 58 lines in the file; the other 3 are embedded fields (`Ears back, backed away…`, `Substantial`), not those copies.

Examples of the objects the log copied:

- `examples/adventure-4/coatroom/mirror.yml`
- `examples/adventure-4/kitchen/sink.yml`
- `examples/adventure-4/maze/room-g/carved-face.yml`

Rewriting the log would change a record of what the linter saw. Leave it.

## 3. `secrets:` lists — different job

15 entries, 6 files. A `secrets:` list of dicts, each with `trigger:` and `result:`, and the dict is not an advertisement entry. Four more secrets entries (two on each carved face) have `trigger:` and `hint:` and no `result:`. `key_squawks:` occurs nowhere under `skills/` or `examples/`.

The `result:` text belongs to the hidden trigger. On the adventure-4 lamp vendor the offers already use `effect:`, and the secrets sit beside them as a separate list. `say:` is the advertisement's spoken effect. Renaming the secret's `result:` does not put the secret in `advertisements:`.

Examples:

- `examples/adventure-4/maze/room-g/carved-face.yml` — one `result:`, two hint-only secrets
- `examples/adventure-4/maze/room-j/lamp-vendor.yml` — four `result:` secrets; the advertisements use `effect:`
- `examples/old/adventure-1/maze/room-j/lamp-vendor.yml`

The other three files are the lamp-vendor or carved-face copies in `examples/old/adventure-2` and `adventure-3`. Several other `secrets:` values in the tree are dicts (rooms, the attic mirror), not this list shape.

## 4. `ON-*` names — already `say:`

247 advertisement entries, 52 files, are named `ON-*` and already have `trigger:` and `say:`. They live inside `advertisements:`. A walk that labels a dict by its own key reports them as "under `ON-STRUCTURE`" and so on, because the parent key is the entry name. A walk that tests membership in an `advertisements:` collection finds no `ON-*` map outside one.

Ripgrep for `response:` and `result:` does not find these entries. M4 already renamed them.

Examples:

- `examples/adventure-4/pub/rooms/room-6/jazz-typewriter.yml` — `ON-GENERATE-YAML`, `ON-COMMENTS`, `ON-STRUCTURE`
- `examples/adventure-4/pub/attic/recursion-lantern.yml`
- `examples/adventure-4/pub/rooms/room-4/yaml-jazz-trees.yml`

The same walk also hits three schema maps, because one of their keys is the field name `trigger` and a sibling key is `score` or `say`. Those are the field list, and `say:` is already on it: `skills/advertisement/CARD.yml`, `skills/advertisement/ADVERTISEMENT.yml`, `skills/advertisement/GLANCE.yml`.

## 5. Other trigger maps — different job

16 entries, 7 files. The dict has `trigger:` plus `response:` or `result:`, and it is not an advertisement entry and not a `secrets:` item. A blanket rename to `say:` would treat an outcome as a spoken line.

Spoken reply, local to that file:

- `skills/no-ai-customer-service/CARD.yml` — 4 `patterns:` entries, `response:` is the parody line
- `skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/TREATMENT-KARMA.yml` — 4 apology entries, `response:` is the piece's reply; other events in the same file use `message:`

Outcome, not a line:

- `examples/adventure-4/characters/fictional/wumpus-snorax/hazards/BOTTOMLESS-PIT.yml` — `in_room.result: death`, and `message:` is the line
- `examples/adventure-4/characters/real-people/richard-bartle/pets/heuristic/CHARACTER.yml` — 4 abilities, `result:` describes what the ability returns
- `skills/experiment/experiments/fluxx-chaos/engine/MODULES.yml` — `result: "Game ends, no winner"`
- `skills/experiment/experiments/fluxx-chaos/engine/SOLO-MODE.yml` — `result: "You LOSE — score is 0"`
- `skills/experiment/experiments/emo-poker-face/runs/four-player/RUN-005.yml` — `the_cheese_ceremony.result` is what the table did

## 6. The rest of the ripgrep hits — a different word

186 of the 218 files are outside the 32 files in sections 1 and 2. Eight of those 186 are the adventure-4 lamp vendor (section 3) and the seven files in section 5. The other 178 use `result:` and `response:` as a schema outcome, a run record, an example's expected state, or a sentence in markdown.

Examples:

- `skills/schema-factory/examples/schema-example.yml` — `result: [postgres-running]`
- `skills/no-ai-hedging/examples/2026-01-24-passive-evasion-mistakes-were-made.yml` — `result: [actors_named, responsibility_clear]`
- `examples/adventure-4/build/lint-report.yml` — generated event log, 261 matching lines, timestamp `2026-01-27`. The structural pass found no advertisement entry there with `response:` or `result:`. A typical line is a character note: "Ears back, backed away, refused interaction."
