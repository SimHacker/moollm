# Skill survey: s

Shard confirmed by directory listing, 2026-10-29. Twenty-eight skills: schema, schema-factory, schema-mechanism, scoring, scratchpad, self-repair, session-log, showboat, simulation, simulator-effect, sister-script, skill, skill-log, skill-snitch, skill-test, slideshow, sniffable-python, society-of-mind, soul, soul-chat, soul-city, speech, speed-of-light, sqlite, stone, storytelling-tools, subjective, summarize.

Standard: `designs/object-system/SCHEMA.md` (2026-10-29), constitution §15–16, `designs/SKILLS-CONSTITUTION-AND-PLAN.md`. Pyramid GLANCE → CARD → SKILL.md → README. Flat files. `methods` is a map; each entry has description, signature, parameters, effect, invoked_by (object method schema; omitted keys mean the documented defaults, and writers still emit the map). `advertisements` is a map (score, score_if on a CARD; condition is the old spelling). `k_lines` is a list. `inherits`, never parents. A skill that owns a schema has a `schema:` block with an `id`.

## Counts

| | n |
|---|---|
| Skills | 28 |
| Full pyramid (GLANCE, CARD, SKILL.md, README) | 24 |
| README missing | 4: skill-log, skill-test, soul, stone |
| `schema:` block with an `id` | 0 |
| CARD `methods` map | 20 |
| CARD `methods` list (legacy) | 3: skill-log, skill-snitch, skill-test |
| CARD `methods` string values | 1: showboat |
| CARD has no `methods` | 4: schema, simulator-effect, sniffable-python, subjective |
| CARD ads map using score + score_if | 14 |
| CARD ads in another shape | 8: skill (condition), skill-log, skill-snitch, skill-test, slideshow (strings), sqlite (when/load), simulator-effect (provides), society-of-mind (advertisement: wrapper) |
| CARD has no offer key | 6: schema, sniffable-python, soul, soul-city, speech, subjective |
| CARD `k_lines` as a list | 0 |
| CARD `k_lines` as a map `{activates, related}` | 7: schema-factory, skill, society-of-mind, soul, soul-city, speech, stone |
| CARD `inherits` | 0 |
| CARD `parents` / `parent` | 0 |

Every GLANCE and CARD in the shard is flat at the top level except society-of-mind, whose CARD opens with a `skill:` envelope and an `advertisement:` key. Line counts (GLANCE / CARD / SKILL.md / README):

| skill | G | C | S | R |
|---|---:|---:|---:|---:|
| schema | 29 | 70 | 156 | 104 |
| schema-factory | 46 | 128 | 191 | 72 |
| schema-mechanism | 47 | 98 | 376 | 56 |
| scoring | 42 | 95 | 55 | 37 |
| scratchpad | 35 | 79 | 111 | 43 |
| self-repair | 52 | 100 | 86 | 40 |
| session-log | 42 | 90 | 444 | 102 |
| showboat | 31 | 67 | 128 | 42 |
| simulation | 51 | 141 | 164 | 86 |
| simulator-effect | 60 | 96 | 331 | 300 |
| sister-script | 54 | 347 | 189 | 65 |
| skill | 58 | 303 | 1177 | 125 |
| skill-log | 29 | 48 | 83 | — |
| skill-snitch | 44 | 134 | 469 | 261 |
| skill-test | 23 | 31 | 16 | — |
| slideshow | 54 | 47 | 608 | 53 |
| sniffable-python | 10 | 23 | 75 | 141 |
| society-of-mind | 68 | 251 | 404 | 550 |
| soul | 57 | 135 | 136 | — |
| soul-chat | 57 | 101 | 131 | 176 |
| soul-city | 70 | 218 | 117 | 379 |
| speech | 53 | 274 | 360 | 90 |
| speed-of-light | 42 | 125 | 468 | 233 |
| sqlite | 31 | 49 | 109 | 22 |
| stone | 46 | 109 | 167 | — |
| storytelling-tools | 48 | 58 | 209 | 30 |
| subjective | 45 | 62 | 389 | 55 |
| summarize | 58 | 337 | 98 | 44 |

CARD sizes past the plan's ~200-line sniff: skill 303, sister-script 347, society-of-mind 251, soul-city 218, speech 274, summarize 337. skill-test's SKILL.md is 16 lines. soul-city's GLANCE is 70 lines, the top of the glance band, and it is a contents list.

## Per skill

### schema

Schemapedia. GLANCE `description`: indexed "schema" senses (interchange, notation, execution, introspection, causal, frames, K-lines, prototype, Society of Mind, SQL/SQLite, git, GitHub, component interop). "Names, delegates, gateways—not one validator." CARD is a file index and `related` list. No methods, advertisements, or k_lines. SKILL.md sorts families and points at `schemas/registry.yml` plus `schemas/mechanisms/<id>/MECHANISM.yml`. `templates/MECHANISM.yml` is the prototype (id, family, plugin_profile, mechanism_relations, moollm_hooks) with the shape written as comments. No `schema:` block.

### schema-factory

GLANCE `what`: "Schema factory for Drescher-style schemas. Deterministic layer before LLM synthesis. Build, lint, ingest, compose, generate context." CARD says it is the practical companion to schema-mechanism. Methods LINT, INGEST, COMPOSE, CONTEXT are a map with signature, description, output; parameters, effect, and invoked_by are absent. Ads LINT-SCHEMA, INGEST-EXPERIENCE, COMPOSE-PLAN, GENERATE-CONTEXT use score and score_if, and `invoke_when` is still a separate list. `k_lines` is `{activates, related}`. Owns `SCHEMA-SCHEMA.yml` under the key `schema_schema:` (id `drescher-schema-schema`, required fields id, action, context, result). The linter looks for `schema:`.

### schema-mechanism

GLANCE `what`: "Drescher's computational theory of causal learning. Schemas: 'Context → Action → Result units.' Discovered through experience." Methods on the CARD are MARGINAL-ATTRIBUTION, SPIN-OFF, SYNTHESIZE-ITEM, PLAN-DIJKSTRA, each with description and a parameters map. GLANCE spells the same four with underscores (MARGINAL_ATTRIBUTION). Ads use score and score_if. No k_lines. SKILL.md is the theory (marginal attribution, spin-off, synthetic items, Dijkstra planning) and the comparison with opaque Python items. It does not own the prescriptive file; the factory does.

### scoring

GLANCE `what`: "Achievement valuation — style counts, emergence rewards. Not just did you succeed, but HOW did you succeed?" SCORE, TRACK, LEADERBOARD have description, parameters, effect, invoked_by, and no signature. One ad, EVALUATE-PERFORMANCE, score_if. Factors (completion, efficiency, style, emergence, exploration) are prose on GLANCE and CARD. `state.scoring-schema` is a hand-drawn total/breakdown blob, not a `schema:` block. related on the GLANCE: rubric, reward, economy.

### scratchpad

GLANCE `what`: "Simple working memory file. Think out loud. Draft ideas. No structure required." WRITE, READ, CLEAR match the scoring shape (map, no signature). One ad, THINK-ALOUD. State is one string. Template `scratch.md.tmpl`. No schema to own.

### self-repair

GLANCE `what`: "Checklist-based self-healing. Missing state triggers repair. The repair demon watches for problems." CHECK, REPAIR, STATUS. Ads SOMETHING-BROKEN and STARTUP-CHECK. Checklist: required files, valid YAML, references resolve, consistent state, no orphans. GLANCE says it implements robust-first. See_also: robust-first, session-log. It does not name coherence-engine; coherence-engine names it.

### session-log

GLANCE `what`: "Human-readable audit trail. Every action leaves a trace. Human-readable. Machine-parseable." LOG, VIEW, SEARCH. One ad, AUDIT-TRAIL. GLANCE `entry_schema` is an example (timestamp, event, details.actor/object/room). `SESSION.yml.tmpl` is a different object (`session:` envelope, id, stats, working_set_snapshot). SKILL.md is 444 lines. The entry shape is owned here and is not a `schema:` block.

### showboat

GLANCE `what`: "CLI tool for coding agents to construct Markdown documents demonstrating their work." Methods INIT, NOTE, EXEC, IMAGE, POP, VERIFY, EXTRACT are one-line strings. Ads DEMO-FEATURE, TUTORIAL-BUILDER, LIVE-PROGRESS use score and score_if. Documents Simon Willison's showboat CLI (`uvx showboat --help` as an ad-hoc skill). No k_lines. Sister-script is in `related`.

### simulation

GLANCE `what`: "Central hub for all simulation state. Turns, time, party, selection, flags. Adventure skill inherits from this." TICK, PAUSE, RESUME, STATUS, SELECT, CONFIGURE have description, parameters, effect, invoked_by, and no signature. Ads MANAGE-GAME-STATE, CONTROL-TIME. `inherited_by: adventure` on the GLANCE is the reverse of `inherits` (the child would declare `inherits: [skills/simulation]`). `CHARACTER.yml` is the patron interface and does use `inherits: [skills/character, skills/representation-ethics]`. SKILL.md's SIMULATION.yml sample is wrapped in `simulation:`. State the GLANCE lists (turn, paused, time, party, selection, flags, git, output) is the prototype this skill owes as a file.

### simulator-effect

GLANCE `what`: "Players imagine simulations are vastly more detailed than they are. This is not a bug — it's the most powerful rendering engine ever built. Off-load computation into the user's brain." GLANCE methods are one-line strings: IMPLY, SEED, SPARSE, ARCHETYPE, JAZZ, DIFF. CARD has no `methods` and no `advertisements`. The same six sit in `provides:` as a list of sentences. `satisfies:` is a list of needs. `use_when` / `avoid_when` stand where score_if would. Two directions, named in the GLANCE: COMPILE (machine's sparse rules, human elaborates) and DECOMPILE (human's few words, machine elaborates, including names the spec left out).

### sister-script

GLANCE `what`: "Document-first automation — the script IS the doc. Structure scripts: imports → globals → CLI definition → implementation." DOCUMENT, FOLLOW, EXTRACT, SYNC, UNDERSTAND, ENHANCE have description, parameters, effect, invoked_by, and no signature. Four ads with score_if. CARD is 347 lines, so the card is carrying protocol that belongs in SKILL.md (189 lines). `SISTER.yml.tmpl` is a template. No `schema:` block.

### skill

The meta-skill. GLANCE `what`: "The meta-skill for creating, understanding, and debugging skills. Every skill you encounter was forged here. Eight MOOLLM extensions to Anthropic's skill model." No `schema:` block anywhere under `skills/skill`.

GLANCE lists eight extensions as one-line strings, and CARD repeats them under `innovations:`. They are the constitution (`designs/SKILLS-CONSTITUTION-AND-PLAN.md` §2, restated in SKILL.md). Leave them in prose:

| # | GLANCE one-liner | Where it lives |
|---|---|---|
| 1 instantiation | "Skills as prototypes" | Constitution. The object key is already `inherits`. Protocol file: `skill-instantiation-protocol.md`. |
| 2 three_tier | "Platform → Narrative → State" | Constitution. The plan's row is multi-tier and includes MOO-maps (GLANCE, CARD, SKILL, README, examples, templates) as the fourth tier. The one-liner is the short form of that essay. |
| 3 k_lines | "Names activate knowledge" | The essay stays prose. The key is the existing `k_lines` list, which this CARD still stores as `{activates, related}`. |
| 4 empathic_templates | "Smart generation" | Constitution, and the empathic-templates skill. |
| 5 speed_of_light | "Many turns per call" | Constitution, and the speed-of-light skill. |
| 6 card_yml | "Machine-readable interface" | Constitution. The card schema is `skills/card/CARD.yml` `schema.id: card`. |
| 7 ethical_framing | "Room-based ethics" | Constitution. Representation records live in representation-ethics. |
| 8 ambient_skills | "Always-on shaping" | Constitution. An ambient skill is an advertisement with a scope, plus the concept K-line `ambient`. |

None of those eight names is a key of the skill schema. Extension 3 is the one that already has a standard key (`k_lines`). Extension 6 is the card schema, owned by the card skill.

The six method one-liners are this skill's behavior, and they are not schema keys either. GLANCE stores them as strings (CREATE, INSTANTIATE, DEBUG, UPGRADE, LIFT, COMPOSE). CARD stores the same six as `{signature}` only. Advertisements CREATE-SKILL, INSTANTIATE-SKILL, DEBUG-SKILL, LIFT-PATTERN, COMPOSE-SKILLS use `condition:` (the CARD alias of `score_if`). `invoke_when` is a second list of the same offers. SKILL.md's Commands table is a third vocabulary: SKILL, SKILLS, LEARN-SKILL, LIFT-SKILL, INSTANTIATE. The schema key that holds the six is `methods`, with the method entry shape from `skills/object/OBJECT.yml`.

The skill schema this directory should own (`schema.id: skill`, applied to a skill directory and its CARD, extending card) has these keys: `name` and `description` (required, Anthropic); `methods` of method; `advertisements` of advertisement; `k_lines` as a list; `inherits` as a list; `related` entries `{id, role, when, why}`; `tier`, `emoji`, `tagline`, `tools`, `files`; `allowed-tools` in the foreign spelling. Publishing declarations from the plan §3.5 (`moollm_compatible`, `respects`, `supports`, `consumes`, `composes_with`) are data an orchestrator filters, so they belong on that schema too. They are a different list from the eight extensions.

SKILL.md is 1177 lines and also narrates rooms-as-skills, the codebase as a world, play-learn-lift, and a skill compiler. Those stay prose. CARD is 303 lines because it inlines the eight extensions, directories-as-advertisements, hierarchical skills, and ambient skills beside the interface.

### skill-log

GLANCE `what`: "Protocol so any skill can log events in a structured way. Writes to .moollm/skills/<skill-name>/logs/ with time-big-endian filenames." Methods are a list of `{name, description, args, invoke_when}` for LOG and TAIL. `args` is the old spelling of `parameters`. One ad, SKILL-LOG, with trigger, description, invoke_when, and no score. SKILL.md "Body schema (minimal)" is timestamp, description, optional payload. No README. Composes with session-log, skill-snitch, skill-test. SKILL.md states the split with session-log: session-log is the human audit trail; skill-log is per-skill files.

### skill-snitch

GLANCE `what`: "Static analysis + runtime surveillance for skills. Detects undeclared tools, path escapes, secrets, exfiltration." GLANCE methods: SCAN, AUDIT, SNITCH, TRUST, CONSISTENCY. CARD methods are a list and add INIT, OBSERVE, FETCH-SCAN. Entries use `args` and `invoke_when`. One ad, SKILL-SCAN (trigger startup, optional, invoke_when). Analyzers and patterns are plugin files. No k_lines. This is the audit tool the plan lists under "and growing," beside the eight extensions.

### skill-test

GLANCE `what`: "Single harness to discover and run tests for skills. Per-skill config (test.yml / .skill-test.yml); tests can live in-skill. Companion to skill-snitch (audit); skill-test = validate/regress." SKILL.md is 16 lines and says status DESIGN. CARD methods are a list: DISCOVER, RUN. Ads RUN-ALL and RUN-SKILL are description plus args. GLANCE `designs_k_lines` names two design docs; the CARD has no `k_lines`. No README (designs/README.md is an index of designs). The runner config schema is described in prose under designs/runner.

### slideshow

GLANCE `what`: "Present images as linear visual narratives. Visualizer CREATES. Slideshow PRESENTS. Stereo: YML (truth) + MD (narrative) = depth." Three method lists disagree. GLANCE: CREATE, LANDING, SYNC, UPDATE, ORGANIZE. CARD (47 lines, header says "condensed"): BUILD, CURATE, EXPORT, signatures only. SKILL.md Commands Reference: CREATE, UPDATE, SUMMARIZE, ORGANIZE, COMPARE. The body also specifies LANDING and SYNC. GLANCE's comment says CARD.yml is 988 lines; the file is 47. Ads `sequence_story` and `curate_flow` are bare strings. `SLIDESHOW.yml.tmpl` is the format it owns (type, name, nature, contents list, narrative) and has no `schema:` block. Contents entries are ordered, which is the case SCHEMA allows a list, and they key themselves by `dir` rather than `id`.

### sniffable-python

GLANCE `what`: "Defines how to assign sniff depth to lines (glance / structure / full) so tools like moo sniff can emit only the right level." Depths: glance 1, structure 2, full 3. CARD and GLANCE have no methods, advertisements, or k_lines. `related` on the CARD is a map of prose, not `{id, role, when, why}` entries. This is a third resolution ladder (line sniff inside a file), separate from the skill pyramid.

### society-of-mind

GLANCE `what`: "Minsky's theory implemented in MOOLLM. Skills are agents. Characters are societies of minds. Requires mind — agencies that compete; usual host soul." CARD is wrapped in `skill:` and offers behavior through `advertisement.provides` / `wants` / `motives_satisfied`, not an `advertisements` map. Methods define_agent, assemble_agency, resolve_competition, activate_k_line, observe_society use `input` (alias of parameters) as a string, plus output and effect. Lowercase names fit function/protocol steps; the underscores do not match hyphen names. `k_lines.activates` is a list of one-key maps (`minsky: "..."`, and one entry whose key is `k_lines`). `interfaces.agent` is a schema written as pseudo-types (id, function, activates_when, suppresses, amplifies, knows). GLANCE says the skill needs mind, and the usual host is soul.

### soul

GLANCE `what`: "Continuity that inhabits a character: history and zero or more minds. Character walks, carries inventory, wears personas. Soul rides along (or jumps). Organizational container — not a metaphysical claim." Owns minds[] (0, 1, or N) and history. GLANCE lists no methods. CARD and SKILL.md agree on INCARNATE, STATUS, MOVE, ADD-MIND, REMOVE-MIND, BRIDGE, stored as signature only. No advertisements. `k_lines` is `{activates, related}`. `dependency_grain` on the CARD is the map of who needs whom: character hosts soul, mind needs soul, soul-chat needs soul, society-of-mind needs mind, soul-city needs nothing from soul (it is the place). No README. Ethics hub is ETHICS.md. The machine twin of the ontology, SOUL-MODEL.yml, sits in soul-city.

### soul-chat

GLANCE `what`: "Multi-voice YAML Jazz dialogues where everything speaks. Needs soul — a continuity body (or anything granted a soul-like voice). Often minds under that soul are the speakers." SPEAK, DIALOGUE, INTERVIEW have description, parameters, effect, invoked_by, and no signature. Ads MULTI-PERSPECTIVE and GIVE-VOICE use score_if. No k_lines. Foundation block points at soul, mind, and soul/ETHICS.md.

### soul-city

GLANCE `what`: "Reusable Soul City prototype: liminal place of rooms, roads, shops, tools, objects, plazas, vehicles. Souls and other beings inhabit it. Many instances compose. Plus the protocol for moving souls across save-file borders into and out of shipped games." Methods INSTANTIATE, STATUS, COMPOSE, WALK, MEASURE, DRAIN, SQUIRT, CROSS are signature-only; MEASURE, DRAIN, SQUIRT, CROSS also use `doc:` (alias of description) pointing at SOUL-BRIDGES.md. No advertisements. `k_lines` is a map whose activates list is long (SOUL-CITY, THE-ROLE-GATE, FORK-AND-SYNC, TRANSMIGRATION, ASYLUM, THE-MARKETPLACE, SOUVENIR, THE-ALBUM, and others). GLANCE is a front door to bound documents (SOUL-MODEL, SOUL-BRIDGES, SOUVENIRS, THE-UPLIFT, GLOSSARY) and is 70 lines. SKILL.md is 117 lines; the README is 379. SOUL-MODEL.yml names its `skill:` as soul-city and its `soul_skill:` as soul.

### speech

GLANCE `what`: "Everything about speech synthesis and recognition. TTS, STT, voice registries by platform." CARD methods SPEAK, LIST-VOICES, ANALYZE-VOICES, TRANSCRIBE, ASSIGN-VOICE have signature and description. GLANCE spells the same names with underscores (LIST_VOICES). No advertisements. `k_lines` is `{activates, related}`. Voice tables live in `voices/` and `platforms/` (apple registry under `registry:`). CARD is 274 lines.

### speed-of-light

GLANCE `what`: "Simulate many turns inside one LLM call. Characters debate, vote, decide without waiting for API round-trips. The context window IS the stage." GLANCE lists no methods. CARD methods: SIMULATE, TAKE_FLOOR, YIELD_FLOOR, POINT_OF_ORDER, CALL_QUESTION, with description and parameters, no signature, no effect; invoked_by on one of the five. TAKE_FLOOR and YIELD_FLOOR use underscores. Five ads with score and score_if; three also set `activates`. See_also includes coherence-engine. This is extension 5 of the skill constitution, as its own skill.

### sqlite

GLANCE `what`: "SQLite for agents and apps: single-file and :memory: databases, sqlite_master, pragmas (WAL, journal), JSON1, STRICT tables, migration habits, FTS5 pointer." GLANCE methods: OPEN, DDL, JSON1, WAL, DELEGATE. CARD methods: INSPECT, MIGRATE, JSON1, COMPARE_TO_POSTGRES, with description, parameters, invoked_by, and no signature or effect. JSON1 is the only shared name. Advertisements are `{when: [sqlite, sqlite3, ...], load: GLANCE.yml}`, which is not an advertisements map. The skill teaches SQLite. The schemapedia sqlite mechanism is delegated from schema. Datasette is the browse path the SKILL.md names.

### stone

GLANCE `what`: "The one-page tier. A STONE distills a whole system onto a single dense, legible page whose star is the relationships, not the prose. Named for Stone Librande, whose one-page designs it imitates by being one." Methods STONE, CLONE, AUDIT, ARROWS, LADDER are `{signature, note}`; `note` is not a method key (`description` is). Six ads use score and score_if. `k_lines` is `{activates, related}`. The ladder on the GLANCE is GLANCE → CARD → DESCRIPTION → STONE → README → directory, which inserts a tier the constitution pyramid does not have (GLANCE, CARD, SKILL.md, README). Seed is `examples/STONE.md`. No README, which is consistent with the skill's own claim that a STONE is the page you keep, and still leaves the pyramid without its why-file.

### storytelling-tools

GLANCE `what`: "Narrative capture and sharing tools. Notebooks, letters, photos, exports. Inspired by The Sims' family album." NOTEBOOK, LETTER, PHOTO, SHARE have description, parameters, invoked_by, and no signature or effect. Ads CAPTURE-STORY, SHARE-ADVENTURE. No k_lines. Sits next to session-log (what happened) and slideshow (images as narrative).

### subjective

GLANCE `what`: "Subjective-Oriented Programming. i_have(\"key\") instead of world.has(\"key\"). The \"I\" shifts based on context." No methods and no advertisements. `functions` is six lists (inventory, state, buffs, location, communication, flags) of `i_*` names. Subject resolution priority: object, then npc, then player. Those names are the method map this CARD does not have. SKILL.md is 389 lines of the paradigm; the CARD is 62.

### summarize

GLANCE `what`: "Context compression without losing truth. Create metadata sidecars. Sip before gulping. LLM reads metadata first, full file only if needed." SUMMARIZE, EXTRACT, METADATA, SIP, BOOKMARK have description, parameters, invoked_by; signature absent; effect on three of five. Four ads with score_if. CARD is 337 lines and holds the metadata protocol (brief/standard/detailed, bookmarks, visuals). SCHEMA.md already says a sidecar is `<file>-metadata.yml`. The keys inside it (summary, keywords, bookmarks) are a schema this skill owns and has not put under `schema:`.

## Dedup

### schema, schema-factory, schema-mechanism

Three jobs.

- **schema** is the index of many families. Its own line: names, delegates, gateways, and not one validator. Drescher is one family among interchange, frames, K-lines, Self, SQL, YAML Jazz, git, and the rest. Each family is a `MECHANISM.yml` plugin. Theory stays in the delegated skill.
- **schema-mechanism** is Drescher's theory: a schema is a Context → Action → Result unit, learned by marginal attribution, spin-off, synthetic items, and shortest-path planning. SKILL.md is that account.
- **schema-factory** is the deterministic tool for that one family: lint, ingest, compose, context, with `SCHEMA-SCHEMA.yml` as the prescriptive shape. CARD calls itself the practical companion to schema-mechanism.

Factory's k_lines comment says schema is "JSON Schema / Zod interchange; not Drescher." The schemapedia entry for Drescher delegates back to the mechanism skill, and the factory is the checker. The comment is the stale part. Merging the three would collapse an index, a theory, and a tool into one directory. The prescriptive Drescher object has one owner: the factory. The mechanism-plugin object has one owner: schema. The theory stays prose on schema-mechanism.

### simulation, simulator-effect, self-repair, and coherence-engine

Four jobs. coherence-engine GLANCE `what`: "LLM as consistency maintainer and orchestrator. Not a separate system — how the LLM naturally operates. No separate orchestrator needed. The LLM IS the orchestrator." Its methods are SIMULATE, DETECT, RECONCILE, ORCHESTRATE. Its domains are location against room occupants, inventory (existence is reciprocal; feelings, scores, and buffs are not), buffs at duration 0, and paths that resolve. `related: [self-repair, simulation, time, speed-of-light]`.

- **simulation** is the state and the clock: turn, time, party, selection, flags, and TICK (buffs, needs, object simulations, mail). Adventure is described as inheriting it.
- **coherence-engine** is the pass that reads that state and writes the invariants back. It is how an LLM keeps the simulation's files agreeing with each other.
- **self-repair** is the checklist demon on the substrate: files exist, YAML parses, references resolve, state is consistent, no orphans. robust-first is the principle it implements. It repairs the workspace. Coherence-engine repairs the world model. They meet when a missing file is also a broken reference.
- **simulator-effect** is the authoring law on the other side of the tick: a sparse spec, and the other host elaborates it. COMPILE runs machine rules out to a richer human model. DECOMPILE runs a few human words out to a richer machine world. The Sims zodiac anecdote in the GLANCE: displayed, no behavioral code, testers asked to tune it down. simulation's ONE-STEP-TRAP is the same warning pointed at the clock: do not micro-simulate the detail the brain or the model will fill. simulator-effect does not tick, and it does not heal files.

speed-of-light is the scheduling trick coherence-engine's see_also already records: many of those entity updates inside one call. It is extension 5, not a fifth copy of simulation.

### soul, soul-chat, soul-city

Three jobs, and the CARD `dependency_grain` on soul already says so.

- **soul** is the continuity: history, minds of cardinality 0, 1, or N, inhabiting a character, able to jump. Character walks and holds inventory. Ethics for the stack sit here.
- **soul-chat** is the voice protocol that needs a soul (often the minds speaking): SPEAK, DIALOGUE, INTERVIEW, YAML comments as inner monologue. Objects, rooms, algorithms, and concepts may speak.
- **soul-city** is the place and the border protocol: rooms, roads, shops, plazas, vehicles, and the crossing of save files (MEASURE, DRAIN, SQUIRT, CROSS). Souls inhabit it. The city does not define what a soul is.

SOUL-MODEL.yml is the machine twin and it lives in soul-city, with `soul_skill: skills/soul/`. The ontology file and the city file are in one directory. The grain says the ontology is soul's.

society-of-mind is a fourth neighbor: competition among minds, and it requires mind, whose usual host is soul. It is not a soul and not a city.

### skill, skill-log, skill-snitch, skill-test

Four tools, plus session-log beside the log.

- **skill** forges skills: create, instantiate, debug, upgrade, lift, compose. It is the constitution's host and the anatomy's would-be schema owner.
- **skill-log** writes one YAML file per event under `.moollm/skills/<name>/logs/`, time-big-endian names. Any skill may call it.
- **skill-snitch** audits: declared tools and files against what the skill contains and what cursor-mirror saw it do. SCAN, AUDIT, SNITCH, TRUST, CONSISTENCY, plus INIT, OBSERVE, FETCH-SCAN on the CARD.
- **skill-test** is the validation harness, design-only: discover `test.yml`, run, report drift. The GLANCE says the companion split in one line: snitch audits, skill-test regresses.

session-log is the human-readable session trail (LOG / VIEW / SEARCH), which skill-log's SKILL.md already distinguishes from per-skill files. None of the four is a copy of another. They share a subject (skills) and a log directory convention. skill-test's SKILL.md is too small to carry the protocol, and skill's SKILL.md is large enough to hide the anatomy that should be the schema.

## K-line notes

No CARD in this shard stores `k_lines` as a list. Seven store the legacy map `{activates, related}`: schema-factory, skill, society-of-mind, soul, soul-city, speech, stone. The other twenty-one have no `k_lines` on the CARD. GLANCE `related:` lists are the handles a reader gets, and they are not the key.

society-of-mind's `activates` entries are one-key maps, and one of those keys is `k_lines`, which collides with the slot. soul-city's activates list is a coined vocabulary (THE-ROLE-GATE, FORK-AND-SYNC, ASYLUM, THE-MARKETPLACE) sitting beside filenames that are already K-lines (SOUL-BRIDGES, SOUVENIRS, THE-UPLIFT, SOUL-MODEL). skill-test's `designs_k_lines` on the GLANCE names two design documents and never reaches the CARD.

Method names drift between resolutions, which breaks the copy the pyramid is supposed to keep in agreement:

- schema-mechanism: GLANCE underscores, CARD hyphens (MARGINAL_ATTRIBUTION / MARGINAL-ATTRIBUTION).
- speech: GLANCE LIST_VOICES, CARD LIST-VOICES.
- speed-of-light: CARD TAKE_FLOOR, YIELD_FLOOR; GLANCE has no methods at all.
- sqlite: GLANCE OPEN, DDL, WAL, DELEGATE; CARD INSPECT, MIGRATE, COMPARE_TO_POSTGRES; only JSON1 matches.
- slideshow: GLANCE, CARD, and SKILL.md Commands Reference are three different sets (see Per skill).
- skill: CARD methods and SKILL.md Commands differ (CREATE, DEBUG, UPGRADE, LIFT, COMPOSE versus SKILL, SKILLS, LEARN-SKILL, LIFT-SKILL).
- skill-snitch: CARD adds INIT, OBSERVE, FETCH-SCAN on top of the GLANCE five.
- soul and speed-of-light: the methods exist on the CARD and are absent from the GLANCE, so the small copy dropped the interface.

`inherited_by` on simulation's GLANCE points the wrong direction for lookup. The child (adventure) is who would say `inherits`. Zero CARDs in the shard use `inherits`.

stone's ladder inserts DESCRIPTION and STONE between CARD and README. That is a tier the skill argues for, and it is a different pyramid from §15. A STONE that is the one page you keep still wants its relationships in the CARD's `k_lines` list and `related` entries so an orchestrator can project it with the others.

## Schemas to reify

Nobody in the shard has a `schema:` block. These are the owned shapes, in the order they block other work.

1. **skill** — `schema.id: skill`. Keys named in Per skill (name, description, methods, advertisements, k_lines, inherits, related, tier, emoji, tagline, tools, files, allowed-tools, and the §3.5 declarations). Extends card. The eight extensions stay prose. The six forge commands become method entries with description, signature, parameters, effect, and invoked_by. Reconcile the Commands table into that map.

2. **schema-factory** — `SCHEMA-SCHEMA.yml` is the Drescher object (id, action, context, result, reliability, evidence, extended_context, extended_results, synthetic_items, composite_actions). The top-level key is `schema_schema:`. Put it under `schema:` with an `id` so `schema_lint` discovers it. schema-mechanism keeps the theory and does not get a second copy.

3. **schema** — `templates/MECHANISM.yml` is a prototype whose keys (id, family, plugin_profile, mechanism_relations, moollm_hooks) are written as comments and example slots. The schema of a mechanism plugin goes under `schema:` on that file so instances under `schemas/mechanisms/<id>/` inherit the prototype and not the schema. The registry index can stay a document.

4. **skill-log** — body schema now living as a YAML sample in SKILL.md: timestamp, description, payload. Filename pattern is part of the schema's meaning, not a second skill.

5. **session-log** — one entry shape. GLANCE's timestamp/event/details example and `SESSION.yml.tmpl`'s `session:` envelope disagree, and the envelope is the legacy wrapper. Pick the entry, drop the wrapper, give it `schema.id`.

6. **simulation** — the SIMULATION.yml sample in SKILL.md (turn, paused, parameters, player, party, selection, flags) is the prototype file the skill does not have, wrapped in `simulation:`. Flat prototype plus `schema:` for the keys instances inherit.

7. **slideshow** — `SLIDESHOW.yml.tmpl` (type, name, nature, ordered contents, narrative). After the three method lists are one list, the template's contents entry gets `id` (dir as an alias if dir stays). GLANCE's "988 lines" comment is a stale pointer at a CARD that is now 47 lines.

8. **soul** — the soul object (host character, minds cardinality, history, bridges). SOUL-MODEL.yml is that schema's working decision and it currently lives in soul-city with `skill: skills/soul-city`. The city keeps the place and the crossing methods; the model schema moves with soul, and soul-city inherits it.

9. **summarize** — metadata sidecar keys (summary focuses, keywords, bookmarks, visuals). SCHEMA.md already names the sidecar file. The keys need an id here.

10. **society-of-mind** — `interfaces.agent` (id, function, activates_when, suppresses, amplifies, knows) is a schema drawn as pseudo-types inside a wrapped CARD. `schema.id: agent`, and the CARD becomes flat: `advertisements` map, `methods` map, `k_lines` list.

11. **scoring** — `state.scoring-schema` (total, breakdown) plus the five factors. Small. rubric may own criteria; the score event is this skill's.

12. **skill-test** — test.yml / .skill-test.yml, described as a config schema inside designs and not implemented. The block belongs on the skill when the harness exists. Until then the prose is the only shape.

13. **speech** — `voices/apple.yml` and the other registries share platform, command, and per-voice type/quality/use_for. One voice-registry schema; the files stay instances.

14. **subjective** — the `i_*` names are methods (inventory, state, buffs, location, communication, flags), with subject resolution as the effect's rule. A methods map, not a new schema id, unless the subject-priority table is something the engine runs without an LLM. Then it graduates to keys on the method or on context.

Left as prose, on purpose: simulator-effect (a law, two directions, six methods once they are a map), scratchpad (one string), showboat (someone else's CLI), sniffable-python (three depths; a schema only if moo sniff reads it as keys), stone (four properties are the audit rubric; the page is an example), storytelling-tools (letter and photo examples are instances of object and mail), sqlite (SQL itself; the schemapedia sqlite mechanism stays under schema), sister-script (canonical section order is a writing rule; SISTER.yml.tmpl can grow a schema when its keys stabilize), self-repair (the checklist is five sentences and can stay an advertisement guard until the checks are parameters).
