# Skill survey: t–z

Standard: `designs/object-system/SCHEMA.md` (2026-10-29), constitution §15–16.
Shard: top-level `skills/` directories whose names start with t, u, v, w, x, y, or z.
Listed: task, thoughtful-commitment, ties, time, trekify, urban-safari, vehicle, visualizer, workflow, world-generation, worm, yaml-jazz.
No top-level skill starts with u, x, or z. `skills/biome/biomes/tailscale/` is nested and is out of this shard.
`skills/planning` is outside the shard. Its GLANCE was read for the task/workflow comparison. `skills/goal` is outside the shard. Its CARD and GLANCE were read because task, goal, and workflow are the three partial schema blocks.

A passing card is flat, copies the methods and advertisements, keeps `methods:` and `advertisements:` as maps, keeps `k_lines:` as a list, uses `inherits:`, and carries a `schema:` block when the skill owns a schema. `condition:` on a CARD advertisement is the alias of `score_if:`. `type:` is one id. `composes_with:` is not a navigation key.

## Counts

| Check | Count |
|---|---|
| Skills in shard | 12 |
| GLANCE + CARD + SKILL.md | 12 |
| README | 11 (vehicle has none) |
| Flat CARD (no `skill:` or `card:` envelope) | 8 |
| `skill:` envelope | 4 (thoughtful-commitment, ties, trekify, urban-safari) |
| `methods:` map on the CARD | 11 (urban-safari has none) |
| Method entries with `description:` | 7 (task, thoughtful-commitment, time, trekify, workflow, world-generation, yaml-jazz) |
| `advertisements:` map of entries | 8 |
| `advertisements:` list | 1 (ties) |
| Advertisement map whose values are strings | 1 (visualizer) |
| CARD with `invoke_when:` | 4 (trekify, vehicle, visualizer, worm) |
| CARD with `provides:` | 1 (urban-safari) |
| CARD `k_lines:` as a list | 0 |
| CARD `k_lines:` as `{activates, related}` | 2 (vehicle, worm) |
| `inherits:` on the skill CARD | 1 (task) |
| `schema:` block on the CARD | 2 (task, workflow), both partial |
| `schema:` block matching SCHEMA.md (`id`, `applies_to`, `keys` with `shape`) | 0 |
| Skill that owns a schema file | 1 (ties, `TIES-SCHEMA.yml`, not under `schema:`) |

## Per skill

### task

Pyramid: GLANCE 53, CARD 199, SKILL 218, README 111. GLANCE method names match the CARD: OPEN, CLAIM, RELEASE, CHECK, CLOSE, CANCEL, SPLIT, FRONTIER, BOARD, HANDOFF, SYNC.
Flat: yes (`id`, `name` at the top).
methods: map. Entries have `description`, `parameters` (a map whose values are prose), `effect`, often `output` and `invoked_by`. Extra keys `note`, `refuses`, `delegates_to` sit beside the standard ones.
advertisements: map (WORK-ON-ME, TRACK-THIS, WHATS-NEXT). `condition:` is the CARD alias of `score_if:`. WORK-ON-ME `score` is a formula, not a number.
k_lines: absent. Activation text lives in GLANCE `when:`.
inherits: list of one map, `ref: skills/goal` plus `why:`. Canonical. The instance field `parent:` ("task this was SPLIT from") is the legacy spelling of `inherits:` and will be read as a parent.
schema: partial catalog on the CARD. See Schemas.
Also: `type:` is a list. `composes_with:` is a prose map. `TASK.yml.tmpl` is flat and uses `done_when`.

### thoughtful-commitment

Pyramid: GLANCE 40, CARD 283, SKILL 900, README 211. GLANCE says the CARD is 284 lines. GLANCE `key_methods` is a subset of the CARD (CARD also has DEEP-COMMIT, LINK, HISTORY, PLAN-MERGE, PLAN-CHERRY-PICK).
Flat: no. The interface sits under `skill:`, with `version:`.
methods: map, with `description` and `returns`. Parameters are `params:` as a list of names, the legacy spelling of `parameters:`.
advertisements: map, keyed by method name. Entries use `trigger` and `conditions:` (a list) and `score` on a 0–1 scale (0.95, 0.9). SCHEMA.md scores are 0–100, and the CARD trigger key is `score_if:`.
k_lines: absent.
inherits: absent.
schema: `user_config.schema` describes a local config file (emojis, detail, style). It has no `id` and is not the skill's object schema.
Also: `allowed_tools:` is the legacy spelling of `tools:`. `composes_with:` at the bottom. `related:` is a list of ids with comments, not `{id, role, when, why}` entries.

### ties

Pyramid: GLANCE 52, CARD 125, SKILL 304, README 221, plus `TIES-SCHEMA.yml` (636), `RUNGS.yml`, `TIES.yml`, `scripts/ties_lint.py`. GLANCE, CARD, and SKILL agree on the job: a TIES.yml screens (presence, cost, staleness); advertisements stay on the CARD. The CARD does not copy the field table. The schema file is the body.
Flat: no. CARD opens with a `skill:` envelope.
methods: map (READ-THE-SCREEN, WRITE-A-SCREEN, LINT-THE-CORPUS, ADD-AN-ORGANELLE, HOIST-A-PROTOTYPE, READ-A-RUNG). The verb is `does:`, the legacy spelling of `description:`. No `parameters`, `effect`, or `signature`.
advertisements: a list of six maps. Each has `trigger`, `action`, `score_hint` (`high`/`medium`, not a number), and sometimes `condition`. SCHEMA.md wants a map keyed by name, `score` as a number, `score_if:` on a CARD. `score_hint` is the alias of `score`.
k_lines: absent on the CARD. `TIES.yml` `synonyms:` includes the phrases READ THE SCREEN, WRITE A SCREEN, LINT THE CORPUS. CARD `related.k_lines` is one sentence about `~name~` resolution.
inherits: absent. Prototype vocabulary inside the skill is `proto:` (a field in `TIES-SCHEMA.yml`) and `inherited:` (the CARD's HOIST-A-PROTOTYPE, and the examples index). `TIES-SCHEMA.yml` `prototypes:` says the pile's own TIES.yml is the prototype and children say `proto:`. It does not define an `inherited:` key. Those two spellings disagree with each other, and both disagree with `inherits:`.
schema: the skill owns one. It is not a `schema:` block. See Schemas.
Also: CARD `related:` is a map of prose. `TIES.yml` is a legal manifest of the skill directory (`ties_schema: 1`, rungs in order, `description: CARD.yml`, `body: SKILL.md`).

### time

Pyramid: GLANCE 57, CARD 130, SKILL 46, README 52. GLANCE says the CARD is 187 lines. Method names match: TICK, WAIT, PAUSE, RESUME, STATUS. SKILL.md is shorter than the CARD, so the protocol is the card.
Flat: yes.
methods: map. Entries have `description`, `parameters`, `output`, `effect`, `invoked_by`. STATUS is a command that displays turn and time of day.
advertisements: map (CONTROL-TIME, MANAGE-TIME, BUFF-DECAY) with numeric `score` and `condition:`.
k_lines: absent.
inherits: absent.
schema: none. `state.time-schema` is an informal shape (`turn`, `time-of-day`, `advancement`) using hyphens. SCHEMA.md keys use underscores (`time_of_day`).
Also: `type:` is a list. `see_also:` is a list of paths.

### trekify

Pyramid: GLANCE 49, CARD 268, SKILL 433, README 589. GLANCE says the CARD is 275 lines. GLANCE method names use underscores (`MASK_FILE`, `LONG_RANGE_SCAN`). CARD names use hyphens (`MASK-FILE`, `LONG-RANGE-SCAN`). The CARD is the larger set (SCAN, CONFIGURE, PROBE-*, SHORT-RANGE-SCAN, EXFILTRATION-WATCH, TOOL-AUDIT).
Flat: no. `skill:` envelope, with `version:`.
methods: map, with `description`, `parameters` as `{name: type}`, and `returns`. No `effect`.
advertisements: map of four entries, numeric `score`, `condition:`. The same CARD also has `invoke_when:` as a list, a second offer channel.
k_lines: absent.
inherits: absent.
schema: none. Substitutions are a catalog (`substitutions_quick`, `examples/substitutions.yml`), not a `schema:` block.
Also: `allowed_tools:`. `related:` is a list.

### urban-safari

Pyramid: GLANCE 21, CARD 64, SKILL 124, README 60, plus `DATA-CONTRACT.md` and `scripts/`. GLANCE lists methods SYNC, BUILD, INSPECT, SYNC_VIDEO, MAP_TRANSCRIPT, MATCH. The CARD has no `methods:`.
Flat: no. `skill:` envelope, with `version:`.
methods: absent on the CARD. The behavior is CLI entry points in `scripts/`.
advertisements: absent. `provides:` is a list of capabilities, which §16 folds into advertisements.
k_lines: absent.
inherits: absent.
schema: none. `DATA-CONTRACT.md` is the output shape (manifest, geojson, series, meta, video track) in prose and a JSON example.
Also: `type:` inside the envelope is one id (`mobility-content-pipeline`). `related:` is a list of paths.

### vehicle

Pyramid: GLANCE 35, CARD 98, SKILL 81. No README. `ETHICS.md` is the fourth file. GLANCE names EMBARK, DRIVE, DISEMBARK, HITCH. CARD adds RIDE, UNHITCH, STOW, STATUS. No `VEHICLE.yml` prototype, so a vehicle instance gets the skill's name and nothing else until someone writes the prototype.
Flat: yes.
methods: map of `{signature: "prose"}` only. No `description`, `parameters`, or `effect`.
advertisements: absent. `invoke_when:` is a list of four sentences.
k_lines: a map `{activates, related}`. SCHEMA.md wants `k_lines:` as a list and `related:` as its own key. `activates` holds VEHICLE, PORTABLE-ROOM, EMBARK, DISEMBARK, DRIVE, HITCH, CARAVAN.
inherits: absent. The prose says a vehicle is a room. The card does not say `inherits: [skills/room]`.
schema: none. `kinds:` (steed, coach, trailer, caravan, tardis, pocket) is the start of one.
Also: `type:` is a list. `files.see_also` includes `skills/container` described as inheritance parents.

### visualizer

Pyramid: GLANCE 51, CARD 47, SKILL 871, README 41, plus cameras, photographers, film, styles, compositions, profiles, `visualize.py`, `PHOTO-SET-8.yml`. GLANCE says the CARD is 932 lines. The CARD is a 47-line stub. Three command vocabularies:

| Where | Commands |
|---|---|
| GLANCE | VISUALIZE, COMPOSE, PHOTO-SET-8, STEREO, BUG-EYED |
| CARD | RENDER, VARIANTS, CONSISTENT_SET |
| SKILL.md | VISUALIZE, DEVELOP, FOCUS, VARY, BATCH |

The protocol, the stereo pair (PHOTO.yml / PHOTO.md), and the plugin catalogs live in SKILL.md and the subdirectories. The CARD does not carry them. §15 asks the CARD to be the file that says what the object does.
Flat: the CARD is flat. `PHOTO-SET-8.yml` is wrapped in `card:` and again in `skill:`, and uses `inherits_from:`.
methods: CARD map of `{signature, output}`. SKILL.md actions are a different set and are not on the card.
advertisements: a map whose values are strings (`render_prompt: "Turn descriptions into images"`), plus `invoke_when:` as a list.
k_lines: absent on the CARD. Two plugin files use a list: `styles/INDEX.yml` and `styles/jennell-jaquays-tribute.yml`.
inherits: absent on the CARD.
schema: none. SKILL.md discusses EXIF/IPTC/XMP as photo metadata and does not declare it as `schema:`.
Also: `type:` is a list.

### workflow

Pyramid: GLANCE 40, CARD 124, SKILL 182, README 65. Method names match: DEFINE, LIFT, INSTANTIATE, STATUS, AMEND, RETRO, FREEZE. `WORKFLOW.yml.tmpl` and `workflows/add-skill.yml` exist.
Flat: the CARD is flat. The template wraps the body in `workflow:`.
methods: map. Entries have `description` and, variously, `parameters`, `effect`, `output`, `refuses`, `delegates_to`, `composes`. STATUS delegates to task FRONTIER. It is a command, not a stored status.
advertisements: map (LIFT-THIS, RUN-PROCEDURE, RETRO-AFTER-RUN), numeric `score`, `condition:`.
k_lines: absent.
inherits: absent on the skill. Step graphs use `parent:` for "another workflow to inherit steps from" in the CARD schema, the GLANCE, the SKILL, the README, the template, and `add-skill.yml`. That is the legacy spelling of `inherits:`.
schema: partial, nested under `schema.workflow`. See Schemas.
Also: `type:` is a list. `composes_with:` includes the line `planning: "a living plan is a workflow instance with no prototype yet"`.

### world-generation

Pyramid: GLANCE 41, CARD 76, SKILL 307, README 109. GLANCE says the CARD is 78 lines. Method names match: CREATE, EXPAND, CONNECT, TOWER, FLOOR.
Flat: yes.
methods: map with `description`, `parameters`, `output`, `invoked_by`. No `effect`.
advertisements: map (EXPAND-WORLD, CREATE-PLACE), numeric `score`, `condition:`. TOWER, FLOOR, and CONNECT have methods and no advertisements.
k_lines: absent.
inherits: absent. The skill creates rooms and does not say `inherits: [skills/room]`.
schema: none.
Also: `type:` is a list. `see_also:` is a list of two paths. `state: {}`.

### worm

Pyramid: GLANCE 45, CARD 148, SKILL 246, README 137. GLANCE says the CARD is 150 lines. GLANCE names the reversible basis and the tree verbs. The CARD adds movement and unit verbs (MOVE-WORM, MOVE-HEAD, MOVE-ASS, NEXT-UNIT, PREV-UNIT, SELECT-RANGE, TREE-HIDE, TREE-SHOW).
Flat: yes.
methods: map of `{signature: "prose"}` plus an occasional `note` or `units`. No `description`, `parameters`, or `effect`.
advertisements: map of seven entries, numeric `score`, `condition:`. The same CARD also has `invoke_when:` as a list.
k_lines: `{activates, related}`. `activates` holds WORM, CURSOR, TWO-POINTER, EAT-POOP, PIPELINE. `related` inside `k_lines` is the legacy form of the `related:` key.
inherits: absent.
schema: none. `state:` is an instance default (head, tail, buffer, emit_dir), not a `schema:` block.
Also: `type:` is a list.

### yaml-jazz

Pyramid: GLANCE 72, CARD 94, SKILL 327, README 60, plus `CHARACTER.yml`. GLANCE says the CARD is 189 lines. GLANCE is over the usual glance size because it repeats the principles, the three audiences, and `directories_as_advertisements`. Method names match: IMPROVISE, INTERPRET. Ambient.
Flat: the CARD is flat. `CHARACTER.yml` has a `meta:` envelope (`type: skill_characters`).
methods: map with `description`, `parameters`, `output`, `invoked_by`. No `effect`.
advertisements: map. AMBIENT adds `scope`, `resolution`, `rationale` and `condition: always`. SEMANTIC-YAML and DESIGN-STRUCTURE use `condition:` and a numeric `score`.
k_lines: absent on the CARD and the GLANCE. `CHARACTER.yml` has a list of 13: yaml-jazz, mcluhan, medium-is-message, comments-as-data, three-audiences, acoustic-space, saxy-jazz, jessica-rabbit, drawn-that-way, improvisation, semantic-structure, self-aware-character, representation-vs-essence. That list is the canonical shape, on the character interface, not copied onto the CARD.
inherits: absent on the CARD. `CHARACTER.yml` has `inherits: [skills/character, skills/representation-ethics]`.
schema: none. The skill is a notation. It points at `skills/schema` and does not own a `schema:` block.
Also: `type:` is a list. `see_also:` is a list of paths.

## Dedup

### task, workflow, planning

One job, two objects.

The job is work broken into steps, with a way to know where it stands. The two objects are already named.

| | task | workflow | planning (GLANCE only) |
|---|---|---|---|
| What it is | A goal someone has claimed | A reusable step graph | "Flexible task decomposition and progress tracking" |
| Finished | `done_when` guard, then a `done` event | `verify` becomes the step task's `done_when` | `PROGRESS` writes `progress: {Step 1: done}` |
| Where it stands | FRONTIER and BOARD, computed | STATUS, which is task FRONTIER over the instance | STATUS over the stored progress map |
| Change the plan | SPLIT, RELEASE with a note | AMEND one instance, RETRO the prototype | REVISE |
| Reuse | one piece of work | DEFINE, LIFT, INSTANTIATE | none |

`skills/planning/GLANCE.yml` methods are PLAN, DECOMPOSE, PROGRESS, STATUS, REVISE. Its `plan_schema` stores `progress: {"Step 1": done, "Step 2": in-progress}`. That stored work status is the thing task and goal compute from events. DECOMPOSE is task SPLIT. PLAN of a repeated procedure is workflow DEFINE. A one-off plan is what workflow's CARD already calls "a workflow instance with no prototype yet."

INDEX.yml lists planning, task, and workflow as three methodology peers. The GLANCE of planning also names `plan-then-execute`, which workflow already models as FREEZE plus a gate.

Goal stays the unclaimed wanted state. Task is that state plus an owner. An action is one queued step. Workflow is the prototype that opens those tasks. Planning does not add a third object.

### Other overlaps inside the shard

thoughtful-commitment's TIMELINE, CONTEXT-FOCUS, THINKING, and TOOLS are cursor-mirror operations with a commit message on the end. The skill's own addition is COMMIT, MESSAGE, EXPLAIN, and the thought-stream prefix. workflow's CARD already lists thoughtful-commitment as a workflow that exists without the word (`read thinking → draft message → commit`).

trekify's PROBE, LONG-RANGE-SCAN, and EXFILTRATION-SCAN are session and workspace scans that cursor-mirror and ripgrep already perform. The skill's own addition is the substitution catalog and the 🖖 flag. MASK and UNMASK are the part that is not a scan.

ties, yaml-jazz, and the pyramid are three different jobs that share a directory. yaml-jazz is the notation (comments survive). The pyramid is which file you open (GLANCE, CARD, SKILL). ties is the manifest that says the cost of opening each one. `directories_as_advertisements` on yaml-jazz is a directory listing used as an index. A TIES.yml is the manifest you read instead of trusting that listing. They stay separate. The inheritance keys should not: ties `proto:` / `inherited:` and the object schema `inherits:` are one mechanism.

vehicle and room are one spatial object with a move. The card states the relation in prose and in `k_lines.related`, and never as `inherits:`. mount is a different skill (overlay), and the card says so.

world-generation's methods create and link rooms. The room skill owns the room. This skill is the "the place was undefined, now write it" advertisement on top of room.

time STATUS, vehicle STATUS, and workflow STATUS are three commands that share a name. time reports the clock. vehicle reports position and occupants. workflow reports the task frontier. planning's STATUS reports a stored progress map. One name, four meanings.

worm and urban-safari both say "pipeline." worm is a two-pointer cursor (EAT at the head, POOP at the tail). urban-safari is a FIT-to-map batch. Nothing to merge.

visualizer's three command lists are an internal split, recorded under that skill. slideshow and image-mining are named as related and were not in this shard.

## K-line notes

No CARD in this shard uses `k_lines:` as a list.

The two CARDs that have the key use the retired map form `k_lines: {activates, related}`:

- vehicle `activates`: VEHICLE, PORTABLE-ROOM, EMBARK, DISEMBARK, DRIVE, HITCH, CARAVAN
- worm `activates`: WORM, CURSOR, TWO-POINTER, EAT-POOP, PIPELINE

`related` inside that map belongs on `related:`.

Lists that already match the schema sit off the card:

- `skills/yaml-jazz/CHARACTER.yml` — 13 names, including comments-as-data, three-audiences, medium-is-message. The CARD, which is what an orchestrator filters, does not copy them.
- `skills/visualizer/styles/INDEX.yml` — STYLE-GUIDES, ARTIST-REFERENCES, VISUALIZER, PROMPT-TEMPLATES
- `skills/visualizer/styles/jennell-jaquays-tribute.yml` — JAQUAYS-TRIBUTE and five style names

Everywhere else the activation phrases are GLANCE `when:` lines, or `invoke_when:` lists (trekify, vehicle, visualizer, worm). Those phrases are either `k_lines:` entries or advertisement `score_if:` text. Method names in the imperative (OPEN, EMBARK, IMPROVISE, MASK) are the commands and are not repeated as k-lines.

ties puts its commands in `TIES.yml` `synonyms:` (READ THE SCREEN, WRITE A SCREEN, LINT THE CORPUS). A synonym is a resolution alias. A k-line is an activator. The same strings are doing both jobs.

yaml-jazz's sentence "filenames are K-lines" is a claim about directory listings. It is not a `k_lines:` slot.

## Schemas to reify

SCHEMA.md's block is `schema: {id, applies_to, extends, keys}` where each key has `shape`, `meaning`, and `default`. A concentrated copy on a CARD names `canonical:` and has no `id`. `done_when:` is the condition key. `complete_when:` is read as `done_when:`. A stored `status:` is not a work status. Work state is events plus a computed `state`.

### task, goal, workflow — the partial blocks

None of the three matches the block shape. All three are field catalogs. On the two named rules:

| | `done_when` | work `status:` | block shape |
|---|---|---|---|
| task | The required key. `complete_when` and `research_complete_when` appear only in `events.postel_input_mapping`, rewritten to `done_when`. | No `status:` slot. Computed key is `state`. `never_stored` lists ready, blocked, stale, urgent, in_progress_for_too_long. Input words `pending`, `in_progress`, `done`, `blocked` map to events. | `schema.required` / `optional` / `computed` are maps of prose. No `id`, no `applies_to`, no `keys.*.shape`. The CARD is the only copy, so it is neither the canonical file nor a `canonical:` copy. |
| goal (outside the shard) | Required. GLANCE and CARD say `complete_when` is read as `done_when`. Compiled siblings are `done_when_js` / `done_when_py`. | `accepts` turns `status: complete` into a done event and `status: failed` into a failed event. `status: pending` or `active` is dropped. `states:` is computed. | `schema.required` / `optional` / `computed` are lists of names, not key specs. Same missing `id` / `applies_to` / `keys`. |
| workflow | The step field is `verify:`, documented as "becomes the step task's `done_when`." No `complete_when`. | No stored `status:` field. STATUS is a method. | Nested under `schema.workflow`. Values are prose. `parent:` is the legacy spelling of `inherits:`. |

Task's instance field `parent:` (the task this was split from) uses that same legacy spelling for a different fact, a graph edge. Goal's optional `parent:` is the nested-goal edge and has the same collision. Workflow's `parent:` really does mean inherits. One key, two meanings, both outside `inherits:`.

`TASK.yml.tmpl` is already the flat instance: `done_when`, `history` with an `opened` event, no `status`. `WORKFLOW.yml.tmpl` still has the `workflow:` wrapper, `parent: null`, a `steps:` list, and `verify`. A list of steps is legal because order matters, once each step has `id:`. The wrapper and `parent:` and `verify` are the part to reify: `inherits:`, and `done_when:` on the step (or `verify` listed as an alias of `done_when`).

Reify as `schema.id: task` extending `goal`, and `schema.id: workflow` whose step entries use the task keys. Goal's block is the parent schema and lives with goal, not in this shard. Until those files have `schema.id`, `schema_lint` does not discover them.

### ties — the gap

ties is the object-system skill in this shard. It defines a file type, a rung ladder, prototypes, organelles, and a linter. `schema_lint` discovers `skills/*/*.yml` whose `schema:` has an `id`. `TIES-SCHEMA.yml` has `ties_schema: 1` and a `fields:` map. Each field uses `type`, `what`, and `required`, not `shape`, `meaning`, and `default`. There is no `schema:` key and no `id`. The linter will not see it.

The CARD does not carry a concentrated copy with `canonical:`.

Keys to align when that block is written:

| ties now | object schema |
|---|---|
| `ties_schema: 1` | `schema.id: ties`, `applies_to` each TIES.yml |
| `fields.<name>.type` / `what` / `required` | `keys.<name>.shape` / `meaning` / `required` |
| `proto:` | `inherits:` (a reference, or an alias of it) |
| `inherited:` on the pile, named by the CARD and the examples index, undefined in `TIES-SCHEMA.yml` `fields:` | the prototype's own slots, which children inherit |
| `unset:` | a tombstone; the object schema has `except:` on an inherits entry, which is a different fact (refused methods) |
| `tags+:` | list merge; SCHEMA.md cascade concatenates lists nearest-first, and ties specifies child-replaces unless `+` |
| `x:` organelles | foreign schemas, an extension, each guest pointing at its own schema |
| CARD advertisements as a list with `action` and `score_hint` | map keyed by name, `score` a number, `score_if:` |

`inside:` as a list is legal: order is the read order, and each entry has `at:`. The rung keys (glyphs, label, name, definition, description, body) are the schema's required story and belong under `keys:`.

### Worth a block, not one yet

time: `turn`, `time_of_day`, `advancement` (`paused`, `slow`, `normal`, `fast`). STATUS stays a method. Hyphenated key names become underscores.

urban-safari: the web data contract (manifest, trip geojson, series, meta, video track) is the schema, currently `DATA-CONTRACT.md`. The CARD's `provides:` list becomes advertisements.

vehicle: `kinds` plus the move methods, as `schema.id: vehicle` extending room, and a `VEHICLE.yml` prototype so instances inherit the methods.

thoughtful-commitment: the config blob under `user_config.schema` can become `schema.id: thoughtful-commitment-config` if anything lints that file. It is not the skill's object schema.

### Leave as prose

trekify substitutions are a catalog with a flagging rule, not an object schema. visualizer's EXIF discussion and `PHOTO-SET-8.yml` are a protocol and a wrapped card. worm `state:` is an instance default. world-generation and yaml-jazz do not own an instance schema. yaml-jazz stays the notation that the other schemas are written in.
