# K-lines and schemas

Date: 2026-10-29. Standard: `designs/object-system/SCHEMA.md`. Counts are files under `skills/`, unless a row says lines.

## Counts

### Skills

156 directories directly under `skills/` contain `GLANCE.yml`. Each of those 156 also has `CARD.yml` and `SKILL.md`. `INDEX.yml` records `skill_count: 156`.

16 of the 156 lack `README.md`: content-rescue, copy-that, emacs, example-curator, knowledge-frames, mail-digest, mind, moocroworld, no-ai-parrot, place, quora-harvest, skill-log, skill-test, soul, stone, vehicle.

19 more directories under `skills/` contain `GLANCE.yml` and are not themselves a top-level skill (biomes, design-sense registries, characters, examples). 175 directories contain `GLANCE.yml` in all.

Of those 175: 9 lack `CARD.yml`, 19 lack `SKILL.md`, 20 lack `README.md`. The 9 without `CARD.yml` are all nested: `cursor-mirror/characters/i-beam`, `cursor-mirror/reference/universal/model`, `experiment/experiments/turing-chess/characters/dents`, `experiment/experiments/turing-chess/characters/slats`, `image-mining/examples`, `image-mining/images`, `image-mining/scripts`, `prototype/examples/lookup/garden`, `soul-city/examples/characters/robin`.

### Spellings

| Key | Files | Lines | Where |
|---|---|---|---|
| `k_lines:` | 108 | 122 | 95 at column 0. 60 of the files are a `CARD.yml` or a `GLANCE.yml` |
| `k-lines:` | 0 | 0 | Not a key. `skills/skill/CARD.yml` has `3-k-lines:`. Two markdown files mention the string |
| `klines:` | 0 | 0 | Not a key. `sparklines` is a different word |
| `activates:` | 54 | 58 | 51 files use it under `k_lines:`. Column 0 on `micropolis/CARD.yml` (the k-line list) and `file-system-object/CARD.yml` (empty `k_lines:` beside it). `speed-of-light/CARD.yml` uses it inside advertisements as a file pointer (`FLOOR.yml`) |

`advertisements:` is a map in 167 files (170 map blocks, 2 empty maps, 2 inline maps). It is a list (a dash on the next line) in 4 files: `change-name/CARD.yml`, `content-rescue/CARD.yml`, `emacs/CARD.yml`, `place/CARD.yml`. It is a prose block in 1 file: `object/GLANCE.yml`. No file mixes a list with a map.

`advertisement:` (singular) is a key in 6 files: `leela-ai/CARD.yml`, `manufacturing-intelligence/CARD.yml`, `society-of-mind/CARD.yml`, `task/CARD.yml`, `task/GLANCE.yml`, `no-ai-overlord/archetypes/hannibal-chew.yml`.

`invoke_when:` is a key in 99 files (53 of them `CARD.yml`).

`condition:` is a key in 30 files (4 `CARD.yml`, 1 `GLANCE.yml`, the rest examples and world files). On a card the advertisement schema reads `condition:` as `score_if:`. On a world object it reads `condition:` as `guard:`.

`methods:` values are plain strings in 81 files, and in those files every method value is a string. 76 are `GLANCE.yml`. The other five are `showboat/CARD.yml`, `content-rescue/CARD.yml`, `design-sense/lenses/CARD.yml`, `design-sense/masters/CARD.yml`, and `room/ROOM.yml`. 87 files contain at least one plain-string method value. 166 files contain a map-valued method. 17 files contain a list. 6 files mix strings with maps.

`skill:` at column 0 wraps 11 `CARD.yml` files: cauldron, design-sense, groceries, leela-ai, manufacturing-intelligence, no-ai-parrot, society-of-mind, thoughtful-commitment, ties, trekify, urban-safari. `card:` at column 0 wraps 0. The card schema retires both envelopes.

`parents:` is a key in 0 files. `inherits_from:` is a key on 3 cards: `animal/CARD.yml` (column 0, value `null`), `no-ai-ideology/CARD.yml` (column 0, a list), `historical/CARD.yml` (under `ethics:`, value `skills/real-being`). `extends:` on a card occurs once, `card/CARD.yml` `schema.extends: []`. The card schema's parent key is `inherits:` (alias `inherits_from`).

## Files with a top-level `schema:`

Real schema (`id` and `keys`):

- `skills/advertisement/ADVERTISEMENT.yml` — real schema, `id: advertisement`
- `skills/object/OBJECT.yml` — real schema, `id: method`
- `skills/card/CARD.yml` — real schema, `id: card`
- `skills/character/CHARACTER.yml` — real schema, `id: character`, `extends: [object]`
- `skills/representation-ethics/REPRESENTATION.yml` — real schema, `id: representation`

Concentrated copy:

- `skills/advertisement/CARD.yml` — concentrated copy of `ADVERTISEMENT.yml#schema`. The line says so. It has `keys:` and no `id`
- `skills/exit/GLANCE.yml` — concentrated copy of the exit card's field list (`required`, `optional`, `compiled`)
- `skills/goal/GLANCE.yml` — concentrated copy of the goal card's field list
- `skills/object/GLANCE.yml` — concentrated copy of the object card's field list

Prose pointer:

- `skills/representation-ethics/GLANCE.yml` — `schema: REPRESENTATION.yml`, with the key list in the comment

Local shapes, not an `id`/`keys` schema:

- `skills/exit/CARD.yml` — field list, `required` / `optional`
- `skills/goal/CARD.yml` — field list, `required` / `optional` / `computed`
- `skills/object/CARD.yml` — field list, `required` / `optional` / `computed`
- `skills/task/CARD.yml` — field list, `required` and `optional` as maps of prose
- `skills/workflow/CARD.yml` — one `workflow:` example (id, parent, inputs, steps)
- `skills/container/CARD.yml` — scope fields (`name`, `description`, `defaults`, `rules`, `constraints`, `ambient`, `on_enter`, `on_exit`, `placement_rules`, `zones`, `chest_mode`)
- `skills/prototype/CARD.yml` — parent-slot glossary (`inherits`, `named_parent`, `implied_parent`, `view_parents`, `embedded`, `not_parents`, `never_inherited`)
- `skills/rubric/GLANCE.yml` — `name`, `criteria`, `weights`, `threshold`
- `skills/experiment/experiments/fluxx-chaos/engine/DECK-BUILDER.yml` — `deck_config`
- `skills/cursor-mirror/reference/universal/model/memory.yml` — memory record (`id`, `memory`, `title`, `requestId`, `composerId`, `timestamp`)
- `skills/cursor-mirror/reference/universal/model/entities/agent-transcript.yml` — `Tool_call`, `Tool_result`, `Thinking`
- `skills/cursor-mirror/reference/assimilated/TON-AI-CORE-UNLIMITE-CONTEXT.yml` — conversation log (`root`, `Bubble`, `ToolCallData`, `CodeBlockDetails`)
- `skills/no-ai-joking/examples/hacker-koans-drescher-toaster.yml` — joke anatomy (`recognition`, `understanding`, `resolution`, `reaction`)
- `skills/no-ai-joking/examples/hacker-koans-emacs-bolio-ice-cream.yml` — same joke anatomy
- `skills/no-ai-joking/examples/hacker-koans-greenblatt-foo.yml` — same joke anatomy
- `skills/no-ai-joking/examples/hacker-koans-knight-power-cycle.yml` — same joke anatomy
- `skills/no-ai-joking/examples/hacker-koans-moon-garbage-collector.yml` — same joke anatomy
- `skills/no-ai-joking/examples/hacker-koans-sussman-enlightenment.yml` — same joke anatomy
- `skills/no-ai-joking/examples/minsky-circular-exchange.yml` — same joke anatomy
- `skills/no-ai-joking/examples/minsky-cognitive-bugs-theory.yml` — same joke anatomy
- `skills/no-ai-joking/examples/minsky-quine-self-reference.yml` — same joke anatomy
- `skills/no-ai-joking/examples/minsky-spinach-mayonnaise.yml` — same joke anatomy
- `skills/no-ai-joking/examples/prolog-lightbulb-joke.yml` — same joke anatomy

Fenced examples in markdown (the `schema:` line is column 0 inside a fence):

- `skills/leela-ai/SKILL.md` — one Drescher example (`context`, `action`, `result`, `learning`)
- `skills/leela-ai/README.md` — one Drescher example
- `skills/schema-factory/SKILL.md` — one example (`id`, `action`, `context`, `result`)
- `skills/schema-mechanism/SKILL.md` — five Drescher examples (`action`, `context`, `result`, and on some `reliability`, `extended_context`, `extended_results`)

`skills/schema/schemas/mechanisms/k-lines/MECHANISM.yml` has no `schema:` key. Its top-level key is `k_lines:`, a mechanism profile (`id`, `family`, `plugin_profile`, `purpose`, `cross_cutting`, `delegate`, `relationship_to_other_schemas`) plus `moollm_hooks:`.

### Keys already reified

Advertisement (`ADVERTISEMENT.yml`): id, description, score, score_if, guard, guard_fail, parameters, effect, method, satisfies, invoked_by, reach, requires_tags, requires_items, when_state, when_flags, requires_lighting, cost, trigger, say, set, move_to, give, take, pay, buff, spawn.

Method (`OBJECT.yml`): description, signature, parameters, effect, output, returns, invoked_by, satisfies, body, from.

Card (`card/CARD.yml`): id, name, description, type, tags, credits, license, emoji, tier, rarity, tagline, t_shirt, tools, files, advertisements, methods, k_lines, state, interfaces, inherits, inherited_by, related, see_also, lineage, schema, examples, principles, anti_patterns.

## Three schemas not yet reified

`what`, `why`, and `when` are the glance triple. They appear on all three specimens. They are not card keys.

### skill

Keys on `skills/skill/GLANCE.yml`: what, why, when, methods, eight_extensions, directories_as_advertisements, hierarchical_skills, ambient_skills, skill_files, lineage, tier.

Keys on `skills/skill/CARD.yml`: id, name, type, emoji, tier, rarity, tagline, description, files, k_lines, invoke_when, advertisements, methods, innovations, directories_as_advertisements, hierarchical_skills, ambient_skills, ambient_advertisement_schema, state, tools, documentation, lineage.

Already card keys: id, name, type, emoji, tier, rarity, tagline, description, files, k_lines, advertisements, methods, state, tools, lineage.

On these two files and not on the card schema: what, why, when, eight_extensions, directories_as_advertisements, hierarchical_skills, ambient_skills, skill_files, invoke_when, innovations, ambient_advertisement_schema, documentation.

Eleven cards still wrap those keys in `skill:`. Keys that appear there and not in the two files above: version, config_dir, k_line, ambient, generates_prose, brand, constitution, what_it_never_does, why_that_constraint, entry, registries, parts. Keys that appear in both the envelope and the specimen: id, name, type, emoji, tagline, description, tier, what.

### k-line

Keys on `skills/k-lines/GLANCE.yml`: what, why, when, methods, k_ref_format, sister_script_pattern, examples, minsky_insight, memo_mechanics, wikipedia_urls_are_k_lines, culture_ship_names_are_k_lines, activation_note, lineage, tier.

Keys on `skills/k-lines/CARD.yml`: id, name, type, emoji, rarity, description, tools, tier, methods, state, k-line-insight, advertisements, see_also, credits. The card's `id` is `protocol`. There is no `k_lines:` key on this card.

Already card keys: id, name, type, emoji, rarity, description, tools, tier, methods, state, examples, advertisements, see_also, credits, lineage.

On these two files and not on the card schema: what, why, when, k_ref_format, sister_script_pattern, minsky_insight, memo_mechanics, wikipedia_urls_are_k_lines, culture_ship_names_are_k_lines, activation_note, k-line-insight.

Keys of a `k_lines:` map on a card's own block (not a nested `related:` or `composes_with:` entry): activates, related, exports (`no-ai-ideology`), connects-to (`leela-ai`, `manufacturing-intelligence`), connects_to (`society-of-mind`), activation_clusters (`experiment`). `related` inside `k_lines` is the map form the card schema already sends to top-level `related:`. `connects-to` and `connects_to` are one slot in two spellings.

`activates:` is also the whole field, in place of `k_lines:`, on `micropolis/CARD.yml`.

### coherence

Keys on `skills/coherence-engine/GLANCE.yml`: what, why, when, methods, coherence_domains, the_insight, no_separate_system, related, tier.

Keys on `skills/coherence-engine/CARD.yml`: id, name, type, emoji, rarity, description, tools, tier, methods, state, coherence-domains, insight, advertisements, see_also, credits.

Already card keys: id, name, type, emoji, rarity, description, tools, tier, methods, state, advertisements, see_also, credits, related.

On these two files and not on the card schema: what, why, when, coherence_domains, coherence-domains, the_insight, insight, no_separate_system.

`coherence_domains:` (GLANCE) children: location, inventory, relationships, buffs, references.

`coherence-domains:` (CARD) children: location-consistency, inventory-consistency, relationship-reciprocal-existence, buff-expiration, reference-validity.

Same five facts, two spellings of the parent and of each child. `the_insight` and `insight` are the same prose slot.

## K-line collisions

A claim is an `INDEX.yml` id or alias, or a token in that card's own `k_lines.activates` (a bare string, or the key of a one-entry map). `related:`, `connects-to`, and `activation_clusters` values are references and are not counted as claims. Comparison folds case and treats `_` as `-`.

22 tokens are claimed by two or more skills. 37 further tokens differ only by case, and both spellings belong to one skill (the directory id, and the same id in UPPER-DASHES). Those 37 are the ordinary pair and are not listed.

| Token | Skills | Spellings |
|---|---|---|
| no-ai | 9 | `NO-AI` on no-ai-bias, no-ai-customer-service, no-ai-hedging, no-ai-humansplaining, no-ai-joking, no-ai-moralizing, no-ai-slop, no-ai-soul, no-ai-sycophancy |
| think-deeply | 4 | `THINK-DEEPLY` on no-ai-gloss, no-ai-hedging, no-ai-moralizing, no-ai-sycophancy |
| drescher | 3 | `drescher` on leela-ai and manufacturing-intelligence; `DRESCHER` on schema-factory |
| minsky | 3 | `minsky` on leela-ai, manufacturing-intelligence, society-of-mind |
| papert | 3 | `papert` on leela-ai, manufacturing-intelligence, society-of-mind |
| actions | 2 | `ACTIONS` on github and biome/biomes/github |
| chomsky | 2 | `chomsky` on leela-ai and manufacturing-intelligence |
| constructionism | 2 | id `constructionism`; `CONSTRUCTIONISM` on micropolis |
| drax-point | 2 | `DRAX-POINT` on no-ai-bias and no-ai-joking |
| git | 2 | `GIT` on github and biome/biomes/github |
| github | 2 | id `github`; `GITHUB` on github and biome/biomes/github |
| inventory | 2 | id `inventory` and `INVENTORY` on inventory; `INVENTORY` also on character |
| k-line | 2 | `k-line` on manufacturing-intelligence; `K-LINE` on protocol |
| k-lines | 2 | id `k-lines`; `k_lines` on society-of-mind |
| pi | 2 | `PI` on no-ai-gloss and no-ai-slop |
| pretend-intelligence | 2 | `PRETEND-INTELLIGENCE` on no-ai-gloss and no-ai-slop |
| protocol | 2 | INDEX alias `protocol` on k-lines; id `protocol` and `PROTOCOL` on protocol |
| prototype | 2 | id `prototype`; `PROTOTYPE` on skill |
| schema-mechanism | 2 | id `schema-mechanism`; `SCHEMA-MECHANISM` on schema-factory |
| simulator-effect | 2 | id `simulator-effect`; `simulator-effect` on manufacturing-intelligence |
| sister-script | 2 | id `sister-script`; `SISTER-SCRIPT` on protocol |
| yaml-jazz | 2 | id `yaml-jazz`; `YAML-JAZZ` on image-mining |

`INDEX.yml` has one alias: k-lines → `protocol`. That alias is the protocol row.

## Dedup

Each group is a different job. No merge.

### planning, plan-then-execute, workflow

planning: "Flexible task decomposition and progress tracking. Less rigid than plan-then-execute. Plans can evolve as you learn."

plan-then-execute: "Frozen plans with human approval gates. Two-phase execution: 'plan → freeze → approve → execute.' Security through separation."

workflow: "A workflow is a reusable procedure: a prototype of steps with edges, actors, guards and gates. INSTANTIATE clones it into a directory and spawns tasks. The tasks carry the state; the workflow carries the shape."

Planning revises a plan while the work is happening. Plan-then-execute freezes a plan and then runs it. Workflow is the reusable shape that a run is cloned from. Workflow's glance already names plan-then-execute as the freeze gate it composes with.

### schema, schema-factory, schema-mechanism

schema has no `what:`. Its `description:` opens: "Indexed schema senses: interchange, notation (YAML Jazz), execution (shell-orchestration), introspection (cursor-mirror DB/model), causal (Drescher), frames, K-lines…" and closes "Names, delegates, gateways—not one validator." `related_skills` lists schema-mechanism and schema-factory.

schema-factory: "Schema factory for Drescher-style schemas. Deterministic layer before LLM synthesis. Build, lint, ingest, compose, generate context."

schema-mechanism: "Drescher's computational theory of causal learning. Schemas: 'Context → Action → Result units.' Discovered through experience."

One is an index of many families, one is the checker for the Drescher family, one is the theory. schema-factory's card points `related` at schema-mechanism as the foundation and at schema as interchange.

### soul, soul-chat, soul-city

soul: "Continuity that inhabits a character: history and zero or more minds. Character walks, carries inventory, wears personas. Soul rides along (or jumps bodies). Organizational container — not a metaphysical claim. Multiple minds are first-class. Nesting allowed under Self."

soul-chat: "Multi-voice YAML Jazz dialogues where everything speaks. Needs soul — a continuity body (or anything granted a soul-like voice). Often minds under that soul are the speakers. Characters, objects, rooms, algorithms, concepts — all may have voices. Comments in YAML become inner monologue."

soul-city: "Reusable Soul City prototype: liminal place of rooms, roads, shops, tools, objects, plazas, vehicles. Souls and other beings inhabit it. Many instances compose. Plus the protocol for moving souls across save-file borders into and out of shipped games."

Soul is the continuity. Soul-chat is the dialogue that needs a soul. Soul-city is the place and the border protocol. Soul-city's glance says the ontology lives in `skills/soul`.

### simulation, simulator-effect, self-repair, coherence-engine

simulation: "Central hub for all simulation state. Turns, time, party, selection, flags. Adventure skill inherits from this."

simulator-effect: "Players imagine simulations are vastly more detailed than they are. This is not a bug — it's the most powerful rendering engine ever built. Off-load computation into the user's brain."

self-repair: "Checklist-based self-healing. Missing state triggers repair. The repair demon watches for problems."

coherence-engine: "LLM as consistency maintainer and orchestrator. Not a separate system — how the LLM naturally operates. No separate orchestrator needed. The LLM IS the orchestrator."

Simulation holds the clock and the state. Simulator-effect is the authoring rule that a sparse spec is enough. Self-repair is the checklist on files. Coherence-engine is the pass over cross-object facts. Coherence's glance `related` is self-repair, simulation, time, and speed-of-light.

### postgres, postgres-optimization

postgres: "Production PostgreSQL operations: connection strings and psql, roles and schemas, migrations, essential extensions, introspection queries, backup vocabulary. Deep query tuning stays in postgres-optimization."

postgres-optimization: "Unconventional PostgreSQL performance techniques. Beyond standard DBA: constraint exclusion, function-based indexes, hash exclusion constraints."

Operations and extensions on one side, index and plan tricks on the other. The first glance names the second as the delegate for a slow query.

### moo, mooco, mooco-mirror

moo: "The moo CLI is the moo virtual machine — user-space file tools over GitHub branches (read, write, list, resolve moorls). Each branch is a moo (ClassName_ObjectID). Repos live in moocroworld (REPOS.yml); moo owns its own ephemeral cache in .moollm/skills/moo/cache/."

mooco: "Custom orchestrator designed to host MOOLLM skills. Explicit context control. Safe tool execution. Skills remain portable across orchestrators."

mooco-mirror: "Parallel introspection for MOOCO sessions. Inspects events, compares with Cursor-mirror. Reveals divergence, improves portability."

Moo is the branch CLI. Mooco is an orchestrator. Mooco-mirror compares that orchestrator's traces with Cursor. Moo's glance points `related` at moocroworld, the model the CLI runs, which is a fourth job.
