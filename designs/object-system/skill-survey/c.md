# Skills c*

Directory listing of `skills/` (top level only): `card`, `cat`, `cauldron`, `change-name`, `character`, `code-review`, `coherence-engine`, `constructionism`, `container`, `content-rescue`, `context`, `copy-that`, `cursor-mirror`. Thirteen. Nested `biome/biomes/cloudflare` is not in this shard.

Judged against `designs/object-system/SCHEMA.md` and constitution §15–16 (2026-10-29). Writers emit flat files. `methods:` is a map of `{description, signature, parameters, effect, invoked_by, body}` (aliases `does:`, `params:`, string entries, and lists are legacy). `advertisements:` is a map; cards use `score_if:`. `k_lines:` is a list of strings. `inherits:` is a list. One CARD. Concentrated copies stay, and they agree.

`score_if:` is already the advertisement key on every map in this shard. `condition:` is gone from these CARDs. `invoke_when:` is still present beside those maps on four skills.

## Counts

| | |
|---|---|
| Skills | 13 |
| Pyramid GLANCE + CARD + SKILL.md + README | 11 |
| README missing | `content-rescue`, `copy-that` |
| One CARD | 13. None split into `ADVERTISEMENTS.yml` / `METHODS.yml` / `K-LINES.yml` |
| Aligned | 1 — `card` |
| Partial | 6 — `code-review`, `coherence-engine`, `constructionism`, `container`, `copy-that`, `cursor-mirror` |
| Drifted | 6 — `cat`, `cauldron`, `change-name`, `character`, `content-rescue`, `context` |
| Schema block matches SCHEMA.md | `card` (on `CARD.yml`), `character` (on `CHARACTER.yml`) |
| Schema block still on older keys | `container` (`type` / `description` / `items`) |
| Schema absent, shape lives elsewhere | `coherence-engine`, `cauldron`, `context`, `copy-that`, `code-review` |

## Per skill

### card — aligned

Files: `GLANCE.yml`, `CARD.yml`, `SKILL.md`, `README.md`, plus `ACTIVATION.md`, `ENSEMBLES.md`, `FLUXX.md`, `examples/`. No second card. Flat. `type: skill` (one id). `k_lines:` is a list: `CARD`, `TRADING-CARD`, `PLAYING-CARD`, `CARD-ARCHITECTURE`, `CARD-SCHEMA`, `SIDECAR-PATTERN`. Advertisements are a map with `score` and `score_if`. Methods are a map of `{signature}` only (CREATE, PLAY, COLLECT, TRADE, EXAMINE, ACTIVATE). That matches the method schema: unstated keys take defaults. No `does:`, no `params:`.

`schema:` on this CARD is the canonical card schema (`id: card`, `applies_to: "every CARD.yml"`, `extends: []`, `conventions`, `keys` with `shape` / `default` / `meaning` / `aliases` / `of`, `retired`, `projection`). `advertisements` is `of: advertisement`. `methods` is `of: method`. `k_lines` aliases include `k_lines.activates`, `invoke_when` is an alias of `advertisements`, `condition:` inside an entry is an alias of `score_if:` on a card. This is the shape SCHEMA.md § Schema files describes. It carries `id` because it is the owner, not a copy.

Residual, not a second schema: GLANCE `methods:` are still strings (`CREATE: "CREATE [name] TYPE [type]"`). The method schema reads a string as `{body: ...}`. These strings are signatures, so the glance copy does not mean the same thing as the card. GLANCE `when:` arrows name CREATE, CARD-ARCHITECTURE, CARD-SCHEMA, SIDECAR-PATTERN, which exist on the card.

No overlap inside the shard that should merge. The card schema's `interfaces:` is how a character directory's CARD copies `CHARACTER.yml`. Quote, card GLANCE `what:`:

> Meta-skill for cards. Trading cards, playing cards, Magic cards, Tarot, business cards, key cards. Portable tokens you carry, play, and activate.

Character, below, is the body those tokens can name. Different objects.

### cat — drifted

Files: GLANCE, CARD, SKILL.md, README. Flat. `type: [skill, companion, game]`.

Drifted keys: `k_lines:` is a map `{activates, related}` (`related` entries use `relation:`, not `why:`). `inherits:` is a map `{from, gets, overrides}`, not a list entry `{ref, gets, overrides}`. `invoke_when:` still lists four lines that the advertisements already say with `score_if`. Methods are maps of `{signature, note}` (`note` is an allowed extension). Advertisements are a map with `score_if`. No schema to reify; a cat is an animal character.

Overlap with `character`. Cat GLANCE `what:`:

> Feline companion with trust dynamics. Cats are NPCs that judge you. Buffs require successful interaction. Trust starts at 10 (suspicious) — you must EARN it.

Character GLANCE `what:`:

> Foundational entity pattern. Characters have location, inventory, relationships. Players, NPCs, companions, bots — all are characters. Personas are identity layers worn on top.

Keep both. Fix `inherits` to a one-element list whose `ref` is `skills/animal` (GLANCE already says `inherits: skills/animal`). Move `k_lines.related` to `related:`.

### cauldron — drifted

Files: GLANCE, CARD, SKILL.md, README, `META-PLAN.md`, `protocols/` (MELT, STIR, LADLE, SCOOP, ANCHOR, LINK, TASTE, SERVE, SCRY, TREE, MODEL-ROUTING). One CARD. The protocol files are phase bodies, not an aspect-split of the card. The card does not copy several of them.

Drifted keys:

- `skill:` envelope (`name`, `version`, `emoji`, `tagline`, `config_dir`, `description`). SCHEMA.md retired `skill:` and `version`.
- `invoke_when:` (five lines) beside an advertisements map that already uses `score_if`.
- `allowed_tools:` list. Card face is `tools: {required, optional}`.
- `composes_with:` map on GLANCE and CARD. That is `related:` with `role: composes`.
- `protocol: CAULDRON`. The card schema lists `protocol` as an alias of `k_lines`. There is no `k_lines:` list.
- `classification: meta-orchestrator` beside no `type:`.
- Methods (MELT, STIR, LADLE, ANCHOR, LINK, TASTE, SERVE) are maps with `description`, `parameters`, `returns`, `composes`, and sometimes `delegates_to`. `returns` and `delegates_to` are allowed (`delegates_to` is an object-schema extension). `parameters` values are type tags (`string`, `array`, `dict`), not prose. No `signature`, no `effect`, no `body`. `composes` is not a method key.
- GLANCE `when:` also names TREE, FRONTIER, UNLOCK, SCOOP, SCRY. Those methods live in `protocols/TREE.yml` and `protocols/SCRY.yml` / `SCOOP.yml`, not on the card. `protocols/TREE.yml` opens with `protocol:`, `skill: cauldron`, and `invoke_when:`, and its `node_schema` uses `type` / `items` / `required`. Its methods use `steps:` rather than `body:`. `done_when:` there is the canonical key.

Advertisements that are on the card (MELT, STIR, LADLE, ANCHOR, SERVE) are a map with `score_if`.

The card is the lower band pasted into the middle: `orchestration_model` includes the phase diagram and the guard table. CARD target in the card schema is ~150–200 lines; this CARD is the orchestration plus the methods.

Schema to reify: a playbook node, from `protocols/TREE.yml` `node_schema`, as `schema:` `id: playbook` (or on the task skill if that already owns `done_when`). Keys: `requires` (list of `{node, verify}`), `unlocks` (list of `{id, kind, why}`), `done_when` (the shell guard). Empty `requires` means a root. Guards compute the frontier; a status document does not. `research_complete_when` stays an alias of `done_when`.

Overlap with `coherence-engine` is the word orchestrator, not the job. Cauldron GLANCE `what:`:

> Two-phase discipline for cross-cutting technical plans. Phase 1: one monolith, everything goes in, ideas melt together. Phase 2: split into topical docs + playbooks for parallel executors.

Coherence GLANCE `what:`:

> LLM as consistency maintainer and orchestrator. Not a separate system — how the LLM naturally operates. No separate orchestrator needed. The LLM IS the orchestrator.

Cauldron's card says it "does not do the work itself; it conducts." Coherence's card says no separate orchestrator is needed. Both can stand: cauldron conducts a plan, coherence checks world facts. The coherence sentence is the one that does not survive contact with cauldron, simulation, and self-repair.

### change-name — drifted

Files: GLANCE, CARD, SKILL.md, README, `playbooks/pdf-prestoration.md`. Flat. `type: [skill, toolkit, document-surgery, identity]`. No `k_lines`, no `invoke_when`. Methods SCAN, DISCUSS, EDIT, VERIFY, PUBLISH, PLAN are maps with `description`, `parameters`, `output`, `effect`, `invoked_by` (SCAN also `script`). That is the writer form, minus `signature` (the default is the name).

Drifted key: `advertisements:` is a list of three prose strings, not a map. No schema to reify.

Near `content-rescue`, not the same job. Change-name GLANCE `what:`:

> Change a name (or email, phone, handle, any identifying string) across the artifacts where it lives — starting with ninja-editing PDF files: scan, describe what's found, discuss the changes, perform them with provenance.

Content-rescue GLANCE `what:`:

> Pull YOUR content back OUT of walled / enshittifying platforms (Medium, etc.) and HN (still good) — text, images, embedded video links — into clean, git-committed, universal Markdown + local assets you control and republish.

### character — drifted

Files: GLANCE, CARD, SKILL.md, README, `ETHICS.md`, prototype `CHARACTER.yml`. One CARD. The prototype is the right place for the schema.

**`CHARACTER.yml` `schema:` matches SCHEMA.md.** `id: character`, `applies_to` every `CHARACTER.yml`, `extends: [object]`, conventions for flat files, list-of-one, dotted keys, cross-repo refs, not-dry layers, safe defaults, visibility, consent placement. Keys use `shape`, `default`, `meaning`, `aliases`, `value_aliases`, `values`, `entry_keys`, `required`, `owner`. `inherits`, `derived_from`, and `layers` match SCHEMA.md § Layers. `moollm_home` is an alias of `layers`, not of `inherits`. `real_being` default: "false when status is fictional; true otherwise, in every layer." `status` is a life fact. Representation rule is computed. This is current.

The prototype's own `methods:` still write `does:` (`MOVE: { signature: "...", does: "change location; the file stays home" }`) and `note:` and `dispatch:`. `does:` is the alias of `description`. `dispatch` is an allowed extension. `note` is an allowed extension.

**The CARD does not match that schema.** Drifted keys on the CARD:

- `type: [skill, entity, game]`.
- `k_lines:` map `{activates, related}` with `relation:`.
- `invoke_when:` five lines, duplicated by advertisements that already have `score_if`.
- `methods:` is only CREATE, and CREATE uses `does:`. The comment says STATUS, MOVE, TAKE, DROP, WEAR, RELATE, SNIFF live on the prototype. §15 says the card copies the important methods, with `from:`. There is no `interfaces:` entry for `CHARACTER.yml`. GLANCE `when:` names TAKE, DROP, WEAR, REMOVE-PERSONA, SNIFF, GREET, CUDDLE, which the card does not list.
- `core_keys` / `layer_relations` / `character_layers` are a second statement of the schema, and they disagree with it.

Disagreements, quoted:

CARD `core_keys.real_being`: "default false if status is fictional or layer is adventure, cast or prototype; true otherwise, including no layer."

`CHARACTER.yml` `real_being.default`: "Computed: false when status is fictional; true otherwise, in every layer."

The same CARD `safe_defaults` says "a real person in a fictional layer states real_being: true", which fights the adventure/cast/prototype default on the line above.

CARD `layer_relations.aliases.inherits` includes `moollm_home`. The schema puts `moollm_home` on `layers`. SCHEMA.md: `moollm_home:` is `layers:` (navigation, not inheritance).

CARD `character_layers.visibility.public_layer`: "may name a private layer in derived_from or layers by ref only."

Same CARD, `resolution.validation`: "Public layer doesn't reference private (blocked)."

SCHEMA.md § Layers: "A public layer never names a private layer, in any key or in prose. The private layer names and inherits the public one." The prototype convention `visibility` says the same. The CARD's first sentence contradicts the schema and its own later check.

CARD `character_layers.precedence`: "Negotiate precedence per-field in metadata" with `public_wins`, `private_wins`, `merge`, and "Conservative default: public_wins for shared fields."

SCHEMA.md: lookup is `inherits` (first match), and "For real beings the biography layer wins other disagreements." The character schema has no `precedence:` key. The CARD describes a mechanism the schema replaced.

No new character schema. Repair the CARD copy so it matches `CHARACTER.yml`, and copy MOVE, TAKE, DROP, WEAR, SNIFF onto the card with `from: CHARACTER.yml`.

Overlap with `cat`: quoted under cat. Overlap with `card`: a `character-card` is a card type ("Summonable personas"); the being is this skill. Do not merge.

### code-review — partial

Files: GLANCE, CARD, SKILL.md, README. Flat. Methods START, EXAMINE, COMMENT, APPROVE, REQUEST-CHANGES, SUMMARIZE are maps with `description`, `parameters`, `output`, `effect`, `invoked_by`. Advertisements are a map with `score_if`. No `k_lines` (the default is the id). No `invoke_when`.

Drifted or nonstandard: `type` is a list (same cluster as the skills below). `focus-areas` is a hyphenated key. `state.review-schema` uses `type` / `description` / `values`, the older schema vocabulary, for a review record (target, focus, status, comments, findings). `output` values are joined strings; the method schema accepts that and asks writers for the list `[chat, state-change, file]`.

Schema to reify: the review record, if it is a stored object. `status` here is work state (`in-progress`, `approved`, `changes-requested`, `abandoned`). SCHEMA.md says work state is not a stored `status:`; `done_when` / `fail_when` say when it is finished. Unsure whether a review's approval is a life-fact-style fact or work state. The card treats it as stored state.

No overlap inside the shard. `see_also` names debugging, rubric, evaluator, research-notebook, which are outside it.

### coherence-engine — partial

Files: GLANCE, CARD, SKILL.md, README. Flat. `type` is a list (`skill`, `meta`, `orchestration`). Methods SIMULATE, DETECT, RECONCILE, ORCHESTRATE are maps with `description`, `parameters`, `output`, `effect`, `invoked_by`. Advertisements are a map with `score_if`. No `k_lines`. No `schema:`.

The domain key is `coherence-domains` (hyphen). Values are prose, not maps. GLANCE `methods:` are still strings. GLANCE `coherence_domains` uses short names (`location`, `inventory`, `relationships`, `buffs`, `references`); the CARD uses `location-consistency`, `inventory-consistency`, `relationship-reciprocal-existence`, `buff-expiration`, `reference-validity`. Same five facts, two names.

The relationship rule is the same in both files. CARD:

> If A has a relationship cell for B, does B have one for A? Reconcile by CREATING the missing cell — never by copying values into it. Contents are per-direction and independent: A may adore B while B has not noticed. A pair-hosted buff lives in one cell and must not be mirrored into the other.

GLANCE `what:` is quoted under cauldron. Self-repair GLANCE `what:`:

> Checklist-based self-healing. Missing state triggers repair. The repair demon watches for problems.

Simulation GLANCE `what:`:

> Central hub for all simulation state. Turns, time, party, selection, flags. Adventure skill inherits from this.

Contradictions:

- SIMULATE `effect`: "Update entity state, tick buffs, process needs." Simulation `tick_effects`: increment turn, tick buffs, decay needs, run object simulations. Two skills advance the clock.
- ORCHESTRATE `invoked_by: [simulation, time]` and SIMULATE `invoked_by: [time, player, adventure]`. Simulation calling coherence to advance the simulation is a cycle.
- DETECT `invoked_by: [self-repair]` and self-repair's checklist already says "References resolve" and "State is consistent." `reference-validity` is that checklist line again.
- The card says "No separate orchestrator needed. The LLM is the orchestrator." Self-repair is a repair demon, simulation is a hub, cauldron is a conductor. The LLM can be who notices. It is not the only object with the job.
- Character schema `relationships` means "Ties to other beings, objects and places, keyed by id." It does not require a reverse cell. Coherence requires the cell and forbids copying its contents. That is a world rule the character schema does not state. Unsure which one is intended. The coherence text is the more specific one, and it matches "unrequited is the normal case."

`state:` is a comment that there is no state. Do not give coherence its own world.

Proposed schema (no file has it yet), owned here, entries not inherited as slots:

```yaml
schema:
  id: coherence
  applies_to: "each entry of an invariants: map. Not a slot of the objects it checks."
  extends: []
  keys:
    left:       { shape: string, meaning: "dotted slot, character.location" }
    right:      { shape: string, meaning: "the other dotted slot, room.occupants" }
    agreement:  { shape: enum, values: [member-of, existence-reciprocal, contents-independent, resolves, expired-removed] }
    repair:     { shape: enum, values: [write-both, create-empty, remove, report] }
    must_not:   { shape: list, of: prose, default: [], meaning: "fixes that would make the sides look the same and are still forbidden" }
    owner:      { shape: ref, meaning: "whose method writes. Coherence detects." }
    on:         { shape: list, of: string, default: [], meaning: "method names that dirty the invariant" }
```

Map the five domains onto that, and drop SIMULATE's tick from this skill:

| id | agreement | repair | owner | on | must_not |
|---|---|---|---|---|---|
| location | member-of (both ways) | write-both | character MOVE | MOVE | do not change `home` |
| inventory | member-of | write-both | character TAKE, DROP | TAKE, DROP | |
| relationship | existence-reciprocal and contents-independent | create-empty | character RELATE | RELATE | copy feeling, scores, or buffs; mirror a pair-hosted buff |
| buff-expiration | expired-removed | remove | simulation TICK, or buff | TICK | |
| reference | resolves | report | self-repair for files that must exist; coherence only for paths between objects | | |

DETECT reports. RECONCILE applies `repair` unless `must_not`. ORCHESTRATE is "run the dirty domains for this event." SIMULATE leaves.

### constructionism — partial

Files: GLANCE, CARD, SKILL.md, README. Same method and advertisement shape as code-review (BUILD, INSPECT, MODIFY, SHARE; `score_if`). No `k_lines`. `concepts` uses a hyphenated id `public-artifact`. `philosophy` is prose the card schema would call `principles`. No schema to reify.

GLANCE `connection` says "Play-Learn-Lift IS constructionism as methodology." That other skill is outside this shard; its `what:` was not read. Inside the shard, cauldron lists play-learn-lift as another meta-orchestrator. Constructionism GLANCE `what:`:

> Seymour Papert's philosophy: learn by building inspectable things. The filesystem is a microworld. Skills are constructions. Debugging is learning, not failure.

Not the same claim as cauldron's two-phase plan. Keep both.

### container — partial

Files: GLANCE, CARD, SKILL.md, README, prototype `CONTAINER.yml`. Flat. Advertisements SHARE-DEFAULTS and GROUP-WITHOUT-PLACE are a map with `score_if`. Methods CREATE, DEFAULT, TRACE are maps with `description` plus `output` or `effect`. CREATE's `output: yaml` is outside the method enum `[chat, state-change, file]`. No `k_lines`. `type: [skill, system]`. `related:` is a list of bare ids, which the card schema allows.

**The schema does not match SCHEMA.md.** It sits on the CARD as a flat map of slot → `{type, description, items, values}`: `name`, `description`, `defaults`, `rules`, `constraints`, `ambient`, `on_enter`, `on_exit`, `placement_rules`, `zones`, `chest_mode`. No `id`, no `applies_to`, no `keys:`, no `shape`, no `meaning`, no `aliases`. `CONTAINER.yml` has the slots as real defaults (`defaults: {}`, `rules: []`, `constraints: []`, `placement_rules: []`, `zones: {}`, `chest_mode: null`) and no `schema:` key. SCHEMA.md says a prototype's schema lives under `schema:` so lookup does not return it as slots. A concentrated CARD copy would name `canonical:` and carry no `id`.

`lookup_order` and `merge_across_containers` on the CARD match SCHEMA.md § Cascade (own, declared parents, container defaults nearest first, implied skill; maps deep-merge, lists concatenate nearest first, scalars nearest wins). That part agrees. The adventure compiler still does not apply `defaults:`; `resolve.py` does. The CARD says so.

GLANCE `what:`:

> A directory that is a scope, not a place. CONTAINER.yml's defaults: reach every room, character and object inside it. Like OpenLaszlo's <node>.

Context GLANCE `what:`:

> The world object passed to every compiled closure. Why "world" not "ctx"? More evocative. Self-documenting. The closure sees the WORLD.

Adjacent, not duplicates. Container is authored defaults cascading into children. Context is the runtime argument (`world.player`, `world.room`). A closure reads the world; the world got some of those values from container defaults. Do not merge.

Schema to reify: move the slot definitions into `CONTAINER.yml` under `schema:` `id: container`, `shape` / `meaning` / `of`, and keep a copy on the CARD with `canonical: skills/container/CONTAINER.yml`. `defaults` is a map keyed by kind (`room`, `character`, `object`, interface name, singular of an embedded collection). `on_enter` / `on_exit` are prose with `compiles: true`. `chest_mode` is an enum. `provides` and `request_list` appear only inside comments on the prototype; they are not keys.

### content-rescue — drifted

Files: GLANCE, CARD, SKILL.md, `scripts/`. No README. Flat. `type` is a list. `status: implementing` stores work state.

Drifted keys: `methods:` are four strings (EXTRACT-MANIFEST, FETCH-ASSETS, WIRE-MARKDOWN, SCRAPE-HN). A string reads as `{body}`, and these strings are signatures. `advertisements:` is a list of `{trigger, method}`. `trigger` is an advertisement key; the list form and the missing `score` are the drift. `ties:` and `related_planned_skills:` stand where `see_also` / `related` would. No `k_lines`. No schema.

Overlap quotes are under change-name, and with copy-that:

> Content meant for copying out of chat ships in a fenced block, formatted for its destination venue. One block per artifact. Nothing in the block you wouldn't publish. Out-of-band notes stay outside the fence.

Rescue brings bytes in. Copy-that fences bytes going out. Keep both.

### context — drifted

Files: GLANCE, CARD, SKILL.md, README. The CARD has identity and then `naming`, `standard_keys`, `extended_keys`, `skill_namespace`, `functions`, `runtime`, `related`. No `methods`, no `advertisements`, no `k_lines`. `functions:` is a second behavior offer (emit, narrate, give, take, go, add_buff, …) grouped by area. Constitution §16: advertisements are the one behavior offer.

The CARD is thin because the behavior was never given the standard keys, not because SKILL.md hides a method map. SKILL.md § Utility Functions restates the same lists. § Methods Are Bound shows an example `consume_fuel: "reduce fuel by amount"`, the legacy string method.

Schema to reify: `id: context` for the world object. Keys: `turn`, `timestamp`, `adventure`, `player`, `room`, `party` as the always-present set; `object`, `target`, `npc` as optional; `skills` as a map whose key spelling is the skill id with hyphens turned to underscores. The utility functions are methods on that object, not a `functions:` tree.

Overlap with container: quoted under container.

### copy-that — partial

Files: GLANCE, CARD, SKILL.md, `formats/`, `house-styles/`, `examples/`. No README. Methods FENCE, FORMAT-FOR, PREFLIGHT, DEFINE-VENUE match the code-review map shape. Advertisements are a map with `score_if`. AMBIENT also has `scope`, `resolution`, `rationale`, which are not advertisement-schema keys (jazz, unless a later lint reserves them). No `k_lines`. GLANCE `ambient: true` is not on the CARD.

`plugin_schema` (`venue`, `markup_supported`, `markup_unsupported`, `characters`, `structure`, `quirks`, `test_cases`) is the venue shape in prose, not a `schema:` block. Reify as `schema:` `id: venue` in this skill; format files are instances. `formats/<venue>.yml` was not fully read; unsure whether those files already use other keys.

Overlap with content-rescue: quoted there.

### cursor-mirror — partial

Files: GLANCE, CARD, SKILL.md, README, plus designs, docs, reference, templates. One CARD. Methods STATUS, TREE, TOOLS, THINKING, CONTEXT_SOURCES, TIMELINE, TRANSCRIPT, EXPORT_MARKDOWN are `{signature}` maps. Advertisements are a map of 14 with `score_if`. No envelope.

Drifted keys: `invoke_when:` (four lines) beside those advertisements. Method names use underscores (`CONTEXT_SOURCES`, `EXPORT_MARKDOWN`); the signatures use the CLI hyphen form (`context-sources`). Constitution kebab-case for commands; the card schema says UPPER-DASHES for command names. `staging_methods:` is a second methods map (PREFS-INCLUDE, STAGE-ADD, STAGE-LIST, STAGE-COMMIT, STAGE-PR) with `signature`, `description`, `behavior`. That is `methods:` plus `body:`. `references:` is `see_also`. No `k_lines`; GLANCE `key_commands` is the middle band sitting in the glance instead.

No schema to reify for the skill itself. Command names are the k-lines. No `what:` overlap inside the shard that should merge. Cauldron's ANCHOR composes this skill; it does not restate it. Cursor-mirror GLANCE `what:`:

> Deep introspection into Cursor IDE internals. 73 commands. 7 output formats. Thin CLI over a ~10k-line library. Reads chat history, tool calls, context assembly, MCP traces.

## Dedup

Do not merge any pair in this shard.

| Pair | Keep | Why |
|---|---|---|
| cat, character | both | Cat is a species. Fix inherits and k_lines. Do not copy the character schema onto the cat card. |
| card, character | both | Card schema is the view. Character schema is the being. A directory can have both files. |
| container, context | both | Cascade defaults versus the runtime `world` argument. |
| coherence-engine, simulation | both | Clock and decay stay on simulation. Coherence names the invariant and who writes. Delete SIMULATE's tick effect from coherence. |
| coherence-engine, self-repair | both | Files exist, YAML parses, orphans: self-repair. Cross-object facts: coherence. Reference checks should be one of them. The cards currently list both. |
| coherence-engine, cauldron | both | World facts versus a plan's phase graph. Stop calling either "the" orchestrator. |
| cauldron, constructionism | both | Brewing a plan is not Papert's microworld. Cauldron's pointer at play-learn-lift is `related`, not a merge with constructionism. |
| change-name, content-rescue, copy-that | all three | PDF name surgery, platform repatriation, fence on the way out of chat. |
| code-review, cursor-mirror | both | Review a diff. Read a Cursor session. |

The repeated card shape (methods with `description` / `parameters` / `output` / `effect` / `invoked_by`, advertisements with `score` / `score_if`, no `k_lines`, `type` as a list) is one template, shared by code-review, coherence-engine, constructionism, and copy-that. Dedup the template by finishing the card schema's aliases, not by merging the skills. `type: [list]` still needs the migration the card schema already describes (first id stays, the rest move to `tags`).

## K-line notes

The name activates. The level-band is the middle (`designs/P-PYRAMID.md`): a K-line reopens an intermediate band, not the whole pyramid. The upper band is the current goal (reloading it makes the problem look solved). The lower band is the current facts and the procedure (reloading it paints false detail). For a skill, the directory name is the activator, the `k_lines` list is the middle (structural words), and SKILL.md / protocol files / examples stay the lower band.

What this shard does:

- `card` is the one list of strings. `CARD` is the name. `TRADING-CARD`, `PLAYING-CARD`, `CARD-SCHEMA` are the middle. The schema section is lower-band material that belongs on this card, because this skill owns the schema.
- `character` and `cat` store the middle and the navigation in one map (`activates` plus `related`). Navigation is `related:`. `INVENTORY` on the character card is another skill's name, not this skill's middle.
- Everyone else omits `k_lines`. The default (the id in UPPER-DASHES) means only the name fires. The middle band is missing, or it is hiding in GLANCE `when:` / `key_commands` (`cursor-mirror`) or in `protocol: CAULDRON` (`cauldron`).
- Cauldron's phase names (MELT, STIR, LADLE, TREE, SCRY) are the middle band and should be the `k_lines` list. The state-machine diagram and `protocols/*.yml` are the lower band. The CARD currently holds the diagram.
- Saying a name should load GLANCE and CARD. It should not load cauldron's orchestration diagram, cursor-mirror's reference tree, or character's per-field precedence essay.

## Schemas to reify

| Skill | Now | Reify |
|---|---|---|
| card | `CARD.yml` `schema:` `id: card` | Already matches. Leave it. GLANCE method strings are a bad copy, not a schema gap. |
| character | `CHARACTER.yml` `schema:` `id: character` | Already matches. The CARD's `core_keys`, `moollm_home` alias, public-names-private sentence, and `precedence:` do not. No second schema. |
| container | CARD map of `{type, description}` | `CONTAINER.yml` `schema:` `id: container` with `shape` / `meaning`. CARD copy gets `canonical:` and no `id`. |
| coherence-engine | `coherence-domains:` prose | `schema:` `id: coherence` as in the table above. `invariants:` map `of: coherence`. SIMULATE does not own the tick. |
| cauldron | `protocols/TREE.yml` `node_schema` with `type` / `items` | `schema:` for a playbook node: `requires`, `unlocks`, `done_when`. Flatten the CARD's `skill:` envelope first. |
| context | `standard_keys:` list, `functions:` tree | `schema:` `id: context` for the world object. Functions become methods. |
| copy-that | `plugin_schema:` prose | `schema:` `id: venue` for `formats/<venue>.yml`. |
| code-review | `state.review-schema` with `type` / `description` | Only if a review record is a real object. Do not store work `status` if `done_when` can say it. Unsure. |
| cat, change-name, constructionism, content-rescue, cursor-mirror | none | Nothing new. Fix keys in place. |
