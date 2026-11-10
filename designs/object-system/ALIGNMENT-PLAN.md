# Plan: define the schemas, align the repos

Turns the two analyses into schemas, tools and migrations:
[CARD-ANALYSIS.md](CARD-ANALYSIS.md) (decisions 1–18) and
[CHARACTER-LAYERS-ANALYSIS.md](CHARACTER-LAYERS-ANALYSIS.md) (L1–L12). Governing rules:
constitution [§15](../../kernel/constitution-core.md#15-the-semantic-image-pyramid-concentrated-not-dry-universal)
(concentrated not DRY, one CARD per object, layers across repos) and
[§16](../../kernel/constitution-core.md#16-advertisements-push-into-the-auction-compile-graduate-universal)
(one advertisement schema, compile then graduate, documented defaults).

Repos in scope: moollm, WillWrightShowForFood (wwsff), MicropolisCore, and private repos that
are not named here, including the private biography repo. Each repo gets its own commits; untracked files in a repo are Don's work in
progress and go into that repo's first commit.

Work runs in five phases. Phases 1 and 2 can run in parallel once phase 0 is done; phase 3
needs both; phase 4 runs after every batch and once at the end.

## Phase 0: decide

Don approves, edits or rejects the decisions in both analyses. Approved decisions go into
[SCHEMA.md](SCHEMA.md) and the objsys-001 history; rejected ones are struck from the
analyses. Facts about real people need a human regardless: every `consent.state: unverified`
and every cross-layer disagreement goes on a review list that is kept privately, because it
names private files and individual people.

## Phase 1: define the schemas

Each schema is a machine-readable YAML Jazz file in the owning skill, read by the linters, plus
prose in that skill's SKILL.md and a concentrated copy in its CARD. Every key has `shape`,
`default` and `meaning`; the default is the sensible case (§16).

```yaml
score:
  shape: number 0..100
  default: 50
  meaning: how much the advertiser wants to be chosen, before score_if
```

| # | Schema | File | Contents | Depends on |
|---|---|---|---|---|
| S1 | advertisement | `skills/advertisement/ADVERTISEMENT.yml` (the skill's prototype file) | base keys, graduated keys and defaults (CARD-ANALYSIS §3), `_js`/`_py` siblings, extension rule for object-specific keys; wwsff `advertisement-dispatch.yml` becomes an extension | decisions 3–8 |
| S2 | method | `skills/object/OBJECT.yml` `methods:` section | core fields (CARD-ANALYSIS §4), name-case rule, `effect_js` compilation | 10, 11 |
| S3 | card | `skills/card/CARD.yml` and a "What a CARD carries" section in `skills/card/SKILL.md` | the layers of a CARD, standard keys and shapes, copy-down rule, aligned names for overlapping jazz, what a projection may rely on | 9, 12, 15–18 |
| S4 | character core and layers | `skills/character/CHARACTER.yml` | core keys with defaults, `layer:`/`role:`, `layers:`, `derived_from:` | L1, L2, L5–L9 |
| S5 | representation | `skills/representation-ethics/` | consent as facts (`public_figure`, `consent: {state, scope, date, evidence}`), computed portrayal rules, `governed_by:`, `may`/`must_not`, subject rights; wwsff `portrayal-standards.yml` declares it extends this | L7, L8, L12 |
| S6 | references | SCHEMA.md and `resolve.py` | `moollm://github/<owner>/<repo>/<path>` resolved to a sibling checkout, else a URL | L3 |

One agent per schema (S1–S6 in parallel), each producing the schema file, SKILL.md section and
CARD copy-down. Don reviews all six together before phase 3; this is the main human gate.

### Questions for that review

Decided by Don on 2026-10-29:
- Layer visibility: a public layer never names a private layer, in any key or in prose. The
  private layer names and inherits the public one. The `private-ref` rule in `layers_lint`
  and the `resolve.py leaks` scanner enforce this, reading the list of private repos from
  `PRIVATE-REPOS.yml`, a file kept in a private repo and found by name (S4, T3).
- Consent lives in the public show layer (the wwsff profile and invitation layer), because
  that is what the person consents to. Private biography layers carry no consent record and
  get it by lookup. No consent record means no consent; layers still state `not_asked`
  explicitly (S5).
- Consent state `interested` means the person wants to take part and the time, medium, and
  scope are being planned. It governs nothing until `granted` (S5). Heinz Lemke is
  `interested`: asked, said yes, planning underway (recorded 2026-10-29).
- One consent vocabulary. The governing record is `representation.consent` on the public show
  layer (`state`, `scope`, `date`, `evidence`, `note`). `not_yet_asked` is only a read alias of
  `not_asked`. INDEX, CARD, correspondence, invitation frontmatter, and show files carry the
  same `state` word as that record; they do not keep a second one, and a character file does
  not also store `invitation.consent`. `schemas/portrayal-standards.yml` extends the
  representation schema instead of restating a consent table. A recommendation letter may be
  mentioned; its text stays out of a public repo unless the letter itself is already public (S5).
- What people consent to varies: a repo show invites any mix of media, timelines and levels of
  participation. Confirming what Don wrote about them is participation, and there can be any
  number of video, audio or email interviews. Consent is to participate; participation is
  recorded per contribution in `invitation.participation` (wwsff `invitation-workflow.yml`) (S5).
- Satire: declared parody of a public figure's public conduct is allowed as long as it never
  claims to be them and invents no private life. Punch up, never down. The 🃏 and snatch-game
  frames and `donna-toadstool` fall under this rule (S5).
- `score_if`: a false `score_if` drops the bid to 0; there is no +20 bonus. T6 aligns
  `adventure_runtime.py` with this (S1).
- Memorial subject rights stay: family, estate and people who knew them may correct a
  portrayal, with care after a recent death (S5).
- `real_being` defaults to true unless `status: fictional`. Migration m13 adds
  `status: fictional` to the fictional beings in adventure layers (S4).
- wwsff `invitation-workflow.yml` adds the `invitation.status` values `dream_guest`, `stub`,
  and `not_offered`. `warm` is not a status: the legacy map sends it to `draft`, and the
  warmth stays in `note` (S4). The legacy key `not_yet_asked: draft` is an old invitation
  status, not a consent state.
- Fictional signifier is 🎭, with 📖 as an alias; 🤖 marks robots and AIs (S4).
- `moollm_home:` is navigation (`layers:`), not inheritance (S4).
- Confirmed defaults: `invoked_by` is `[self, engine]` for lowercase methods (S2); cards
  default to `tier` 2 and `k_lines` = the id uppercased (S3); `requires_items` means all (S1);
  for real beings the biography layer wins disagreements (T3).

Settled while drafting, open to reversal:
- `invoked_by` defaults to `[player, npc]` for UPPERCASE commands (S2).
- `governed_by` defaults to both real-being and representation-ethics, matching the biography
  header (S5).
- `score_hint` words map to numbers: high 80, medium 50, low 20 (S1).
- `consume` lives in its map form (S1).
- Card defaults: `tier` 0 means foundational/ambient, `rarity` common (values include epic),
  `see_also` = SKILL.md and README.md, `related:` entries `{id, role, when, why}`, `license`
  added as the Dublin Core rights field (S3).
- A card's `advertisements:`/`methods:` take entry shapes through `of:`, not `extends:` (S3).
- Layer values add `profile` (Palm's wwsff page) and `prototype` (other moollm characters) (S4).
- Canonical layer order for disagreements: real beings biography, profile, adventure,
  prototype, page, cast, audience; fictional beings adventure first (T3).

Open:
- Profile `status` is a life fact. `active`, `unknown`, `living_emeritus`, and `stub_warm` are gone. Kelly Booth is `living`. Show-role words are `show_role:`, and `type` on those files is `person`. `don-hopkins` stays `self_sovereign`. Palm and Don Philahue were not retouched. Recount is in [iteration/j5-leftovers.md](iteration/j5-leftovers.md): 236 living, 47 deceased, 2 fictional, 19 with no status key.
- Phase 3 judgment rows J3, J4, J7, and J8 are not started. J6: tragic-clown and the twenty-one mixed `inherits:` maps are lists, with `note`, `overlay_protocol`, or `upstream` beside the list. Palm's pointer map is `seat:`. Seat profile links and `layers:` copies are not started. J2's `skill:` envelope is flattened on the 11 cards, and also on groceries, leela-ai, and manufacturing-intelligence. Top-level skill cards now have `type` as one id and the rest in `tags` (121 cards). Ontology still has `type: [skill, ethics, identity]` because its `tags` is a map. The skill card's five live advertisement keys are `score_if`. `invoke_when:`, singular `advertisement:` whose value is not an advertisement map, `status`/`version`, and hyphenated keys are not started.
- J1, started 2026-10-29: the room card now states LOOK, ENTER, EXIT, CONTENTS, and
  ADVERTISE from `skills/room/ROOM.yml`. The character card now states STATUS, MOVE, TAKE,
  DROP, WEAR, REMOVE-PERSONA, RELATE, SNIFF, LICK, GREET, and CUDDLE from
  `skills/character/CHARACTER.yml`, beside CREATE. The object card's optional slots include
  `disabled`, which the prototype already states. Container and ties already state their own
  methods. OBJECT.yml's `methods:` is empty, so there was nothing to copy.
- J5, applied 2026-10-29 on the 304 `characters/<id>/CHARACTER.yml` profiles: `layer:` is
  set (invitation 226, memorial 47, profile 23, dream_guest 8); a `type:` that named that
  layer is now `person`; `real_being:` is stated; topical emoji moved from `signifier:` to
  `emoji:`, and `signifier:` is 👤 living or unknown, 🕯️ deceased, 🎭 fictional, 🤖 robot
  or AI. Consent spelling was the earlier pass. Show-role words are now `show_role:` and
  `type:` on those files is `person`. `self_sovereign` stays on Don's profile. Palm stays
  `fictional_ai_agent`. Don Philahue's type list stays `orchestrator_avatar`, `avatar`,
  `host_incarnation`, `show_agent`.
- Skill schemas are written: `skills/skill/SKILL-SCHEMA.yml`, `skills/k-lines/KLINE-SCHEMA.yml`,
  and `skills/coherence-engine/COHERENCE-SCHEMA.yml`. The eight extensions stay constitution
  prose. `k-ref` is not a second schema in the k-line file. Coherence is the five domain
  children. It is not a second orchestrator.
- The skill survey is written, one note per shard in
  [skill-survey/](skill-survey/). Six public skills sit outside `moollm/skills`, none with
  a `schema:` block. RepoShow and SimObliterator_Suite have no `skills/` directory. A
  quoted overlap is a proposal, not a deletion.

Decided by Don later on 2026-10-29, not yet applied:
- A stove's `TURN-ON, TURN-OFF` is two advertisements.
- Advertisement and method keys are commands, big-endian, in the shape of a gcloud grammar.
  An LLM maps freeform speech onto them. A sentence is not a key.
- The five missing parents are K-lines, applied 2026-10-29: `GAME`, `TURTLE`, `CREATURE`,
  `COMPANION`, `NARRATOR`. `resolve.py` treats an uppercase token with no slash as a K-line.
  The skills can be written later.
- Envelope wraps: the 11 in moollm are flattened (applied 2026-10-29). See
  [iteration/envelope-eleven.md](iteration/envelope-eleven.md). The private biography layer
  is flattened: 90 scanned, 89 changed, 0 skipped. Show profiles: 358 scanned, 347 flattened,
  0 skipped. Eleven files had no top-level `character:` line and were left as they were.
  Sixteen more mapping envelopes under `examples/old` are flattened. `persona:` on
  captain-ashford stays. Ten mapping envelopes under adventure-4 and soul-city are flattened.
  The worm-confetti-crawler `card:` is lifted. `camp_persona.homage` holds the Rip Taylor
  credit. The nine leftover section labels are lifted: turtle-eventually, dolly-forklift,
  recursive-imp, the moo-maps glance, SUPERBATS, cat-cave, both attic screenshots, and the
  worm demo. Duplicate inner names were dropped. `hazard:`, `furniture:`, and `zones:` stayed.
  `dealer: shuffle.yml` and `room: center` stayed as path scalars. Under `skills/`, 106 mapping
  envelopes are flattened. The four collisions are resolved. skill-snitch `standalone` is one
  map (`ships: false`, `works: partial`). cursor-mirror `bundle` is one map (`name`, `format`,
  `includes`). postal `attachment_types.object` and moocroworld `related.room` are ids in a
  uniform map again. The biome `character: |` blocks are `voice:`. `html_template.card` stays a
  template string. Path scalars such as `contents.card: CARD.yml` stay refs. The two
  `room/TOPOLOGY.yml` examples are flat under `example:`, and `example.file` names the type.
- Profile `status:` values `active`, `unknown`, `living_emeritus`, and `stub_warm` are resolved.
  Kelly Booth is `living`. Show-role words are `show_role:`. `type` on those files is `person`.

## Phase 2: tools

Code, each with tests in the existing style (`skills/prototype/scripts/test_resolve.py`).

| # | Tool | Where | What |
|---|---|---|---|
| T1 | compiler fixes | `skills/adventure/adventure.py` | list-form advertisements keyed by `action:`/`name:` keep all fields; linter iterates lists and stops swallowing exceptions; map-form methods compile `effect:` to `effect_js:`; compiled adventure-4 compared before/after |
| T2 | schema-driven lint | `resolve.py lint` | reads S1–S4; reports shape, unknown-synonym and default-restating findings per file; `--cards` adds the projection-readiness checks (CARD-ANALYSIS §7) |
| T3 | cross-layer lint | `resolve.py layers` (from `layers_survey.py`) | same-id layers agree on name, life facts, `public_figure`, `consent.state`; granted needs evidence; every layer declares its relations |
| T4 | agreement lint | `resolve.py views` | GLANCE `when:` targets exist in the CARD; CARD copies of interface-file methods and keys match their source |
| T5 | migration scripts | `designs/object-system/tasks/migrations/` | one script per mechanical row below, each with dry run, reparse check, and a diff limited to the intended keys (the pattern of `parents.py` and `lighting.py`) |
| T6 | engine support | `adventure.js`, `adventure_runtime.py` | the first graduated keys: `requires_tags`, `requires_items`, `when_state`, `when_flags`, `trigger` words, `say`, `set`, with their defaults |

T6 also carries the runtime gaps T1 found once the export stopped dropping fields:
- trigger scores are 0..1 and need rescaling to 0..100; JS `data.score || 50` turns 0 into 50
- effect text falls back `effect` → `result` → `response` → `description`; neither runtime reads
  the last three, so 248 ads print "You on-hello the X."
- `trigger:` words are matched against what the player says; today the 199 `ON-*` ads can only
  be invoked by typing their name
- the Python runtime reads only `_py` siblings, never `_js`; uncompiled prose guards never run
- the world export carries `methods:` and their compiled `body_js`/`effect_js`
- exit guards written as statement bodies (`pub/ROOM.yml` UP and BAR) abort the JS `load()`
- duplicate object ids collapse 491 objects to 315 in both runtimes
- `compile` on adventure-4 is no longer stopped by `mind_mirror` names. Invalid keys
  were mapped onto the Apple ][ octant (`dominant` → `forceful`, `submissive` → `timid`,
  `unconventional` and `open_minded` → `creative`, `assertive` → `forceful`,
  `insecure` → `touchy`, `analytical` → `well_informed`, `caring` → `friendly`,
  `spontaneous` → `uninhibited`, and Proc's `complex` → `practical` because that
  comment is the card's own gloss). Keys with no scale were removed (`logical`,
  `intuitive`, `trusting`, `suspicious`, `curious`, `principled`, `approval_seeking`,
  and the Big Five block on the Linus persona). Scores above 7 were clamped to 7.
  Old files that nested the 32 names under `bio_energy` / `emotional` / `mental` /
  `social` are flat, which is how the card stores them.

Schema lint baseline (wave 1): `skills/` cards 50 errors, 212 warnings; adventure-4 737 errors,
737 warnings, mostly `parameters:` and `files:` as lists, `tier: character`, and aliases
(`response`, `action`, `result`, `condition`). `LINTER.yml` event logs get linted as objects
and should be skipped. Layers lint: 3 consent errors, 117 missing core keys (54 profiles
without `real_being`, 35 biographies without `id`), 58 missing back-relations, 4 unresolved
refs (`skills/game` for grue, troll, wumpus-snorax; `AMBIGUOUSLY-GAY-DUO` for doctor-no), and
turing-chess `slats/CHARACTER.yml` unparseable at line 67.

T1, T2, T3 and T5 can start as soon as phase 0 is done; T4 needs S3, T6 needs S1. One agent
per tool.

## Phase 3: migrate

Mechanical rows run as scripts (T5) with an agent reviewing the diff. Judgment rows run as
agents over disjoint shards of files. Smallest blast radius first; each row is one commit
per repo, with the surveys rerun before and after and the numbers in the commit message.

### Mechanical

Scripts in [tasks/migrations/](tasks/migrations/), dry run by default, `--apply` to write; a
file is written only when the edited text parses and equals the same change made on the data.
Wave 1 dry run: M2 110 files, M3 114, M4 55, M5 24, M6 13, M7 12, M8 436 (0 collisions),
M9 8 of 32 (20 cast `inherits:` maps mixing parents and `moollm_skills` go to J6), M10 62.
Order: M2 before M3, M4, M5; M3 before M5; M8 before M9. Rerun the dry run right before
applying. M2, M3, M4, M5, M6, M12, and the M7 rows through `activates` are applied. `allowed_tools` stays. M13 (`status: fictional`) and M14 (signifier alias 📖 → 🎭)
have scripts; the profile pass on 2026-10-29 did that work in WillWrightShowForFood directly.
M9 and M10 are applied. M9 changed 9 WillWrightShowForFood files and skipped 22. The one skipped map whose only key was `moollm_skills` is now a list, on `characters/sims/tragic-clown`. Twenty-one maps still carry another key: 12 a `note`, 6 `overlay_protocol`, 2 `upstream`, and 1 a pointer map (`card`, `character_yml`, `home_room`, `home_room_path`). M9 also left one parent map whose extra key is `ethics`. MicropolisCore had nothing to change. The biography layer had nothing to change. Three of the nine changed files kept a note that mentions removed map fields (`absolute_url`, shorthand); those notes need a hand reword. M10 changed 62 biography files and skipped none. `resolve.py lint --strict` on `skills` and `examples` then reported 0 unparseable files, 0 broken path refs, 0 cycles, and 0 legacy spellings. Seven slots still share a name with a child directory: robin `personas` and `minds`, troll `inventory` and `stomach`, wumpus `instances`, proc `sims`, and Don's `inventory`.

| Row | Repos | Files (approx.) | Change |
|---|---|---|---|
| M1 | moollm | 3 | fix the unparseable cards |
| M2 | moollm | 115 applied; 11 left, none a parse error | advertisement lists → maps keyed by name |
| M3 | moollm | 114 applied 2026-10-29; 4 skipped | `condition:` → `guard:` (world) / `score_if:` (cards) |
| M4 | moollm, wwsff | 55 applied; rescan skipped 0 | trigger entries: score ×100, `response:`/`result:` → `say:` |
| M5 | moollm | 36 applied; LINTER.yml held back | drop `score_if: always` / `any` / `true` |
| M6 | moollm | 13 applied; rescan skipped 0 | `does:` → `description:`; `params`/`args`/`input` → `parameters` |
| M7 | moollm | `one_liner`, `related_skills`, `inherits_from`, `activates` applied; `allowed_tools` stays | `one_liner` → `tagline`; `related_skills` → `related`; `inherits_from` → `inherits`; `activates` → `k_lines.activates` |
| M8 | wwsff, private biography repo | biography 89 of 90; show profiles 347 of 358; 0 skipped | flatten `character:` envelopes (`flatten.py`) |
| M9 | wwsff, private biography repo, MicropolisCore | applied 2026-10-29: WWSFF 9 changed, 22 skipped; MicropolisCore 0; biography 90 scanned, 0 changed | parent spellings → `inherits:` / `derived_from:`; cross-repo refs → `moollm://` |
| M10 | private biography repo | applied 2026-10-29: 865 scanned, 62 changed, 0 skipped | `representation.protocol:` → `governed_by:` |
| M11 | moollm | 3 targets already recast; 6 leftovers renamed 2026-10-29 | dispatch "interest" → advertisement; consent `interested` and the NeWS citation stay |

M2 left for a judgment pass, none of them a parse error. The four `stove.yml` files are maps
keyed `TURN-ON`, `TURN-OFF`, and `EXAMINE`. `TURN-ON` bids when `state == off` and `TURN-OFF`
when `state == on`. Both keep the same spoken line. `context-orrery.yml` is keyed
`CONTEXT-WINDOW`, `TOKEN-LIMIT`, and `CONTEXT-TOPICS-DESCRIBE`. `thinking-mirror.yml` is keyed
`INTROSPECTION-DESCRIBE`, `ACTIONS-EXPLAIN`, and `INTROSPECTION`. The content-rescue card is
keyed `MEDIUM-ARTICLES-RESCUE`, `PAGES-FETCH`, `IMAGES-DOWNLOAD`, and `HN-COMMENTS-SAVE`.
change-name is `PDF-NAMES-FIND`, `FONTS-SPELLCHECK`, and `CHANGES-DISCLOSE`. emacs is
`EDITS-STRUCTURE`, `BUFFERS-ADDRESS`, and `MACROS-LIFT`. The original sentence stays as the
trigger or the description. The place card is already a map keyed `VISIT`,
`SURVEY`, `COUCH`, and `EXPLAIN`. `LINTER.yml` is a log under `events:` and `world_state:`
and is not rewritten. The nine maps that kept a spaced `action:` beside a hyphenated key
no longer have that field. The key is the command: `TAKE-SOME`, `BUY-OIL`, `BUY-DELUXE`,
`BUY-PREMIUM`, `INSERT-COIN`, and `CHECK-OIL`. `action: 0.25` under `oil_consumption` on the
two lamp files is an oil rate and was left.
See [iteration/m2-leftovers.md](iteration/m2-leftovers.md). The mannequins, bumblewick's
persona, and the adventure-3 fridge parse, and their advertisement lists are maps.

M3 left `skills/skill/CARD.yml` because a `condition:` also sits outside an advertisement, so
the file-level check refused the edit. The five keys inside `advertisements:` are now
`score_if:`. The example string `condition: always` and `fields.condition` were left.
`conditions:` (plural) on the thoughtful-commitment card is a when-to-invoke list and was left.
The four cards under `examples/` that took `score_if:` are bids, not world guards.
See [iteration/m3-leftovers.md](iteration/m3-leftovers.md).

M4 changed 55 files, all in moollm. WillWrightShowForFood had no trigger advertisement still on
the 0..1 scale. A rescan after the parse fixes changed nothing further and skipped nothing.
The 87 keys that tally still counted are 55 copies inside `examples/adventure-4/LINTER.yml`
and 32 live entries. Those 32, plus 118 live entries in files M4 never opened, are now
`say:`: 150 entries in 31 object files. Scores were already above 1 or absent, so nothing
was rescaled. `LINTER.yml` stays a log. `secrets:` payoffs, `ON-*` entries (already `say:`),
and trigger maps that are not advertisements were left.
See [iteration/m4-later.md](iteration/m4-later.md).

M5 dropped `score_if:` values `always`, `any`, and `true` from 36 files, including the three
mannequins. A comment on the removed line stays. `examples/adventure-4/LINTER.yml` also matched
and was not written: it is a log of past advertisements, the same reason M2 skipped it. Left
for a later row: 39 `score: 50` and 2 `guard: always`.

M6 renamed `does:` to `description:` and `params:` / `args:` / `input:` to `parameters:` inside
method entries, 13 files. String-form methods have no fields and were left. A rescan skipped
nothing. `storage/aisle-d/PROTOTYPES.yml` parses; `recursion-container` is indented with the
other prototypes. skill-log, skill-snitch, and skill-test now store methods as a map
keyed by the command (`LOG`/`TAIL`, `INIT` through `FETCH-SCAN`, `DISCOVER`/`RUN`). The
`name:` field is the key. See [iteration/lists-left.md](iteration/lists-left.md).

Every tracked YAML file parses: `resolve.py lint` scanned 2687 and reported unparseable 0.
`layers_survey.py all` reported unparseable 0 on every layer. 55 files under gitignored
`temp/lloooomm` still do not parse.

M7 renamed `one_liner:` to `tagline:` on the format-design, markdown, and plain-text cards.
It renamed `related_skills:` to `related:` on datasette, example-curator, postgres, showboat, and
sqlite. example-curator's entries are `{id: why}` maps; `related:` entries elsewhere use
`{ref, relation}`. It renamed `inherits_from:` to `inherits:` on animal (`null`, comment kept)
and no-ai-ideology. `activates` moved under `k_lines` on file-system-object (its empty `k_lines:`
was the line above; `related:` stays a top-level key) and on micropolis, which had no
`k_lines`. `allowed_tools` stays; it is a foreign spelling.

M11's three named targets were already advertisement in the live files. Six leftovers that
still used the dispatch word are renamed: the yaml-jazz snitch row, the ideology contributing
heading, the events README quote, the adventure constellation member, the review tension slug,
and the bibliography heading. Consent `interested`, the SCHEMA.md ban on `interests:`, and the
NeWS citation stay. See [iteration/m11-interest.md](iteration/m11-interest.md).

The 11 moollm envelope wraps (`card`, `character`, `dealer`, `export`, `object`, `room`,
`topology`) are flattened. No inner key collided with a key outside the wrapper. The three
mannequins are the coatroom objects under `examples/old/adventure-1`, `adventure-2`, and
`adventure-3`. Sixteen more mapping envelopes under `examples/old` are flattened: player in
adventure-1 and adventure-2, bumblewick in adventure-2 and adventure-3, and twelve `card:`
files in adventure-2. `captain-ashford.yml` keeps
`persona:`, which is not an envelope key. A scan of `examples/old` found no remaining top-level
mapping envelope. Ten more under `examples/adventure-4` and `examples/soul-city` are flattened:
the secret-word card, the room-8 selfie, the service alley, the blank sim, and six wumpus
topologies. The worm-confetti-crawler `card:` is lifted. The Rip Taylor credit is
`camp_persona.homage`. The skill `inherits` list is unchanged. The nine leftover section labels
are lifted. turtle-eventually and dolly-forklift dropped the duplicate inner `name` and kept
species, age, personality, role, and seniority. recursive-imp, the moo-maps glance, both attic
screenshots, and the worm demo are flat. SUPERBATS kept `hazard:`, `defaults:`, `generate:`,
`inherits:`, and `ontology:`. cat-cave kept `furniture:` and `zones:`. `dealer: shuffle.yml` and
`room: center` are path scalars and were left. Under `skills/`, 106 mapping envelopes are flattened.
The four collisions are resolved: skill-snitch `standalone` is one map,
cursor-mirror `bundle` is one map, and postal `object` and moocroworld `room` are ids in a
uniform map again. Biome `character: |` is now `voice:`. `html_template.card` on the fluxx deck
styling stays a template string. Twenty path scalars stayed, because a path in a ref map is a
reference. `room/TOPOLOGY.yml` examples are flat under `example:`. A second pass
found no further mapping envelope under `skills/`. See [iteration/envelope-eleven.md](iteration/envelope-eleven.md). The private
biography layer: 90 scanned, 89 flattened, 0 skipped. Show profiles: 358 scanned, 347
flattened, 0 skipped. Two
`parent:` inheritance pointers are now `inherits:`: the Stupid Fun Club movies file, and
`no-ai-ideology` inside `EXPORT.yml`. The `parent:` heading under that file's `skills:`
block was left. The eight path refs that named `game`, `turtle`, `creature`, `companion`,
and `narrator` are the K-lines `GAME`, `TURTLE`, `CREATURE`, `COMPANION`, and `NARRATOR`.
See [iteration/lint-leftovers.md](iteration/lint-leftovers.md).

### Judgment

| Row | Repos | Shards | Agent task |
|---|---|---|---|
| J1 | moollm | 5 cards | copy prototype methods and key slots down into the room, character, container, object, ties CARDs |
| J2 | moollm | `skill:` envelope flattened. Six example `advertisement:` maps are `advertisements:`. `bionic-eyes.yml` keeps the string. 121 top-level cards have `type` as one id and the rest in `tags`. Ontology's type list stays, because `tags` is a map. The skill card's five live keys are `score_if`. `invoke_when:`, `status`/`version`, and hyphenated keys are not started | `invoke_when:` lines into advertisement `score_if:`; `status`/`version`; hyphenated keys; check GLANCE `when:` agreement |
| J3 | moollm | adventure-4 in 6 shards by directory | graduate the obvious patterns (tag lists, items, state, flags, triggers, say/set) beside the prose, keep prose where it says more |
| J4 | moollm, wwsff | 62 multi-interface directories in 3 shards | decide which UPPERCASE files are interfaces; write or extend the one CARD that summarizes them |
| J5 | wwsff | 303 profiles in 8 shards of ~40 | core keys present (L1), `signifier`/`emoji` split, `type:` → being kind + `layer:` role, consent spelling; no reference to private layers (the private layer names the profile) |
| J6 | wwsff | tragic-clown and the 21 mixed maps are lists; Palm's pointer map is `seat:`; seats and `layers:` copies not started | each seat names its profile layer; `layers:` copies |
| J7 | private biography repo | 90 in 3 shards | core keys, `inherits:` and `layers:` pointing at the wwsff profile, ethics header kept (it is the travelling copy), consent read from the profile by lookup |
| J8 | MicropolisCore, a private repo | 1 page, 4 cards; private characters | declare relations only; private layers name the public ones, and nothing from a private repo is copied into public repos |

Rules every judgment agent gets with its shard:

- Read constitution §15–16, the schema files, and the relevant analysis section first.
- Edit only the files in the shard. Don't run git; the orchestrator verifies and commits.
- Preserve YAML Jazz comments; never delete a concentrated copy for being a copy.
- Real people: never invent facts, dates, quotes or consent; a fact two layers disagree on is
  reported, not resolved.
- No decorative comment lines; no notes about the migration inside the files.
- Return a list of files changed, findings that need a human, and anything skipped with the
  reason.

## Phase 4: verify

After each batch and at the end:

- `resolve.py lint --strict` and the new T2–T4 lints: findings only go down.
- `behavior_survey.py all` and `layers_survey.py all` before and after; the numbers go into the
  commit message and the objsys-001 history.
- Compile adventure-4 and compare `build/adventure.json`: no advertisement, method or key lost.
  The tracked file is `examples/adventure-4/build/adventure.json`. It matches HEAD.
  A compile on 2026-10-29 had been refused by non-standard `mind_mirror` names.
  Those names are now octant, Plain Talk, or Shrink-Rap words from
  `skills/mind-mirror/CARD.yml`, or they were removed. Adventure-4 lint reports
  0 errors.
  `export_advertisement` copies every key of the entry, so `say:` passes through the same
  way `response:` did. Repo-root `build/adventure.json` is gitignored and absent.
  `skills/adventure/test_advertisement_shapes.py` covers advertisement keys (20 tests).
  The runtime JSON does not write `methods`, so a diff of it cannot show a lost method.
  See [iteration/adventure-compile.md](iteration/adventure-compile.md).
- Reparse every changed file.
- A human-review list collects facts flagged by agents (consent, life dates, relations). It is
  kept privately, because it names private files and individual people.
- `resolve.py leaks` finds no private repo name or path in any public repo.

## Running it with agents

| Wave | Runs | Agents |
|---|---|---|
| 1 | S1–S6, T1, T2, T3, T5 | 10 in parallel |
| 2 | Don reviews the schemas; T4, T6; M1–M11 scripts dry-run | 2 + review |
| 3 | M rows applied in order; J1, J2 (8), J3 (6) | ~16 |
| 4 | J4 (3), J5 (8), J6, J7 (3), J8 | ~16 |
| 5 | verification and a summary of remaining findings | 1–2 |

Schema and tool agents get a stronger model; shard agents doing mechanical review can use a
cheaper one. Shards never overlap, so agents work in the same checkout; the orchestrator runs
phase 4 checks and commits each batch in its repo, then pushes.

## Skill alignment

Same method as the object rows: survey the corpus, cluster the spellings, reify a schema
where a pattern has already graduated, then mechanical rewrites. Nothing here is a merge
until a shard note quotes both sides and Don says so.

Corpus: 156 skills under `skills/` with a GLANCE. Schemas already reified, a `schema:` block
a linter can read: advertisement, object (methods), card, character, representation.
Concentrated or partial schema blocks also sit on container, prototype, workflow, task, goal,
exit, and rubric. `skills/skill` has `SKILL-SCHEMA.yml`.

| Row | What | Status |
|---|---|---|
| K1 | Survey shards in [skill-survey/](skill-survey/), including [k-lines-and-schemas.md](skill-survey/k-lines-and-schemas.md) | written |
| K2 | Reify `skill`, `k-line`, and `coherence` schemas from keys already in those files | written |
| K3 | Normalize `k_lines` / `k-lines` / `klines` / `activates` onto `k_lines:` (M7's synonym row) | nothing to rename |
| K4 | Ambient no-ai skills: one card shape, one ambient list. See [skill-survey/no-ai.md](skill-survey/no-ai.md) | applied |
| K5 | Outside skills `inherits:` the moollm skill they copy. See [skill-survey/outside.md](skill-survey/outside.md) | applied |
| K6 | Schemas the outside skills are already stating: command/risk gate, show, `projects_to` | written |

K5, from the outside note, applied:

- coffeeshop keeps gedoog, the board's own categories, and units as sold. It inherits place, room, budtender, character, and representation-ethics. Consent tiers 0–4 map onto `representation.consent.state`; they are not a new scale. A bench with no street number is place's subject when `address` is absent (`spot`), not a new parent. `projects_to` (verbatim local labels, a closed coarse vocabulary) is the general key place does not have.
- MicropolisCore `micropolis` inherits `moollm/skills/micropolis` and keeps the `pnpm` gate, WASM, and renderers. The parent's essay is not copied again. Both copies still use `activates` and `invoke_when`.
- `micropolis-command-bus` inherits advertisement, action-queue, and micropolis. The part moollm does not have is the gate: methods LIST, PREVIEW, PROPOSE, DISPATCH, APPROVE, REJECT, and risk `safe | reversible | destructive | external`. Its CARD `condition:` is `score_if:`.
- screen-angel inherits sister-script, postel, sniffable-python, and card. Verbs under `commands` become methods. Selectors stay on that skill.
- WillWrightShowForFood `repo-show` inherits cauldron for HARVEST. One phase list. SHOW (seed file, planted directory) is the schema to reify. CARD and SKILL currently insert PROPOSE and PRODUCE where GLANCE and README do not.
- `ebike-safari` inherits urban-safari and keeps the amber label and the app path. `provides:` is the offer key SCHEMA already replaced with `advertisements`.

`inherits:` across repos is a `moollm://github/SimHacker/moollm/skills/<id>/` list. `consumed`, `compose_with`, `benefits_from`, and `respects` stay only when they are not parents. `moollm_compatible: true` is on the amsterdank index and on coffeeshop and screen-angel; the other four outside skills do not say it.

K4, from the no-ai note, applied. Thirteen `skills/no-ai-*` directories. Six set `ambient: true`: slop, gloss, sycophancy, hedging, moralizing, humansplaining. Seven set `ambient: false`: joking, soul, customer-service, overlord, parrot, bias, ideology. `ambient: true` on disk is eleven skills: those six plus postel, robust-first, yaml-jazz, design-sense, and copy-that. Constitution extension 8 names those eleven. The compiled rules, `.cursorrules`, and the bootstrap template fallback name the same eleven. `kernel/drivers/cursor.yml` names none.

One schema covers the six ambients, from keys they already share: GLANCE `what`, `why`, `when`, `cardinal_sins`, `go_deeper`, `tier`, `ambient`; CARD `id`, `name`, `type`, `emoji`, `tier`, `tagline`, `files`, `k_lines`, `cardinal_sins`, `advertisements`, `methods`, `t_shirt`. Sycophancy has no `the_fix`. The other seven invented private blocks and do not fit that schema. Twelve cards spell `k_lines` and store `{activates, related}`. Seven still have `invoke_when` beside `score_if`. `sibling_skills` is the old spelling of `related`.

Overlaps to resolve, not to delete blindly: slop's YES-MAN and OVER-ENTHUSIASM are sycophancy's job, and both list "Great question!". Slop's BOTH-SIDESISM is gloss's POWER-PROTECTIVE-NEUTRALITY. Slop's UNSOLICITED-COACHING sits next to moralizing's UNSOLICITED-WARNINGS. "research suggests" is on slop's weasel list and hedging's WEASEL-CERTAINTY; those are different sins. Gloss's GLANCE has REGISTER-SWITCHING; the CARD dropped it and added LIBERTARIAN-CHICKEN. Ideology's CARD still bids AMBIENT with `score_if: always` and has no `ambient` flag. Customer-service's `type` list contains `ambient` while the flag is false.

K1 a–b, from [skill-survey/a-b.md](skill-survey/a-b.md). Twelve skills, each with the full pyramid. Advertisement is aligned: flat card, `score_if`, methods as a map, and the card's `schema:` copies `ADVERTISEMENT.yml` without an `id`. Its method entries still omit `signature`, `invoked_by`, and `body`. Seven are partial (abstract, action-queue, adversarial-committee, artifactory, bartender, budtender, buff): methods and advertisements are maps, and `type:` is a list. The note's `condition:` finding on those cards is already done; M3 renamed it to `score_if:`. Four have drifted: adventure (`k_lines` is `{activates, related}`, two advertisements are bare strings, methods are `{signature}` only), animal (`inherits_from`, `invoke_when`, a `card:` envelope in the species example), biome (`k_lines` map, `invoke_when`, `command:` with no `score_if`, and `convention.yml` still requires `card.id` and `card.microworld_scope` that the daughter cards do not have), bootstrap (`k_lines` map, `invoke_when`, methods use `note:` instead of `description`). Bartender and budtender glances spell methods with underscores; the cards use hyphens. No two `what:` lines in the shard claim the same job. Schemas this shard is already stating, still proposals: a buff entry, the biome convention as flat fields, action-queue, adversarial-committee, a bartender station that budtender extends, the bootstrap probe, and an artifactory session.

K1 k–m, from [skill-survey/k-m.md](skill-survey/k-m.md). Twenty-one skills. All have GLANCE, CARD, and SKILL.md. knowledge-frames, mail-digest, mind, and moocroworld have no README. No CARD in the shard has a `schema:` block, and none stores `k_lines` as a list of bare tokens. The note's `condition:` finding on advertisement maps is already done; M3 renamed those to `score_if:`. What remains: lighthouse-log and mail-digest methods use `does:`; mapbox uses `invocation:`; mind's methods are a signature only; mount's advertisements are strings; leela-ai and manufacturing-intelligence still use a singular `advertisement:`. Their `skill:` wrappers are flattened. Fifteen cards set `type:` as a list.

moo, mooco, mooco-mirror, moocroworld, and moollm are five jobs (CLI, branch-actor world, skill host, session diff, help/constitution), not one skill. mind is resident agency. mind-mirror is a Leary organelle that needs a mind. leela-ai and manufacturing-intelligence share a slogan; their readings have drifted, so they are not a merge. The two micropolis skills stay the split already in K5.

`skills/k-lines` owns `KLINE-SCHEMA.yml`: `k-line` (`id`, `meaning`, `location`, `band`). `k-ref` (path, line, column, end, anchor, search, type, label, severity, description, excerpt) is not a second schema in that file. The level-band rule is attach the middle. The shard spells the activation key as `k_lines`, `k_lines_activated`, `activates`, and `k-line-insight`. `klines` does not occur. A card's `k_lines` is a list of k-line ids. Other shapes the note says are already schemas, still proposals: logistic-container and cell, palace, presence, mind, Sims trait and zodiac, moo-repo and moorl, mount, crew, role-sheet, mythic-tag.

K1 o–r, from [skill-survey/o-r.md](skill-survey/o-r.md). Twenty-nine skills, `object` through `runtime`. All have GLANCE, CARD, and SKILL.md. `place` and `quora-harvest` have no README. Every card is flat. `condition:` is already `score_if:` (65 advertisements). Methods are a map on 21 cards and absent on object, ontology, plain-text, postal, real-being, robot, room, and runtime. `place` still stores advertisements as a list of `{action, to, when}`. representation-ethics stores three advertisement strings. postgres stores a word list. `k_lines` is a list only on place's glance and three CHARACTER files. protocol, quora-harvest, room, and representation-ethics still store `{activates, related}`. `type:` is one id on 3 cards, a list on 25, and missing on plain-text.

`schema.id: method` in `object/OBJECT.yml` matches SCHEMA.md. The card's `method_schema` and the SKILL table both drop `from`. `schema.id: representation` holds `interested`, `parody`, and the `HERO-STORY` alias. The SKILL and the card omit `interested` and `parody`. The card copy still has `id:`, which a concentrated copy does not carry. `consent.scope` defaults to a sentence in the schema, to nothing in the SKILL table, and to `null` on the card. `ROOM.yml` methods still say `does:`. `objects:` is an empty list. The room card does not copy LOOK, ENTER, EXIT, CONTENTS, or ADVERTISE. `room/TOPOLOGY.yml` does not parse.

planning and plan-then-execute stay two jobs. Their template, the planning SKILL example, and the plan-then-execute template are three plan shapes, each wrapped in `plan:` with `status` and `created`. postgres and postgres-optimization stay two jobs. postal and postel are unrelated. `real-being` stays the tag; its `ethics.protocol: HERO-STORY` is the `governed_by` alias already defined. Still proposals: object instance slots, room slots, place fields (no PLACE.yml; the glance points at a missing template), rubric criteria, and one plan-document schema.

K1 t–z, from [skill-survey/t-z.md](skill-survey/t-z.md). Twelve skills. Nothing top-level starts with u, x, or z. All have GLANCE, CARD, and SKILL.md. vehicle has no README. The `skill:` wrappers on thoughtful-commitment, ties, trekify, and urban-safari are flattened. The note's `condition:` finding is already done; M3 renamed those maps to `score_if:`. thoughtful-commitment still has plural `conditions:`, which M3 left. ties advertisements are still a list with `score_hint`. visualizer's values are strings, plus `invoke_when:`. vehicle has `invoke_when:` and no advertisements. urban-safari has `provides:`. ties methods use `does:`. vehicle, worm, and visualizer are signature-only. No CARD stores `k_lines` as a list. vehicle and worm still use `{activates, related}`.

task is the one card with canonical `inherits:`. workflow, its template, and `add-skill.yml` use `parent:`. On a task, `parent:` is also the split-from edge, so the same legacy key is a graph edge and an inheritance pointer. task and goal already use `done_when` and compute work state from events. workflow's step key is `verify`, which becomes the task's `done_when`. STATUS is a method, not a stored status. Zero `schema:` blocks in the shard match SCHEMA.md's shape (`id`, `applies_to`, `keys` with `shape`).

task is the claimed goal. workflow is the reusable step graph that opens tasks. planning's stored `Step: done | in-progress` is the work status task and goal compute from events. That sits next to the o–r finding that planning and plan-then-execute are two jobs; it does not merge them. DECOMPOSE and SPLIT are the same verb under two names.

ties owns the real schema and `schema_lint` cannot see it. `TIES-SCHEMA.yml` is `ties_schema: 1` plus `fields:` with `type`, `what`, and `required`. The linter looks for `schema.id`. The CARD has no `canonical:` copy. Its schema file says `proto:`; the CARD says `inherited:`. visualizer's GLANCE cites a 932-line CARD; the CARD is 47 lines and names RENDER, VARIANTS, CONSISTENT_SET, while SKILL.md's commands are VISUALIZE, DEVELOP, FOCUS, VARY, BATCH. Later proposals: time's clock fields, urban-safari's data contract, and a `VEHICLE.yml` that inherits room. trekify's catalog, worm's state, world-generation, and yaml-jazz stay prose.

K1 c, from [skill-survey/c.md](skill-survey/c.md). Thirteen skills. card is aligned: `schema.id: card`, `k_lines` a list, `of: advertisement` and `of: method`. Its GLANCE still stores methods as strings, and a string reads as `body`, not `signature`. Advertisement maps in the shard already use `score_if`. `invoke_when:` remains on cat, cauldron, character, and cursor-mirror. character's `CHARACTER.yml` schema matches SCHEMA.md. The CARD does not: `k_lines` is a map, CREATE uses `does:`, `real_being` defaults false for adventure, cast, and prototype layers (the schema says false only when `status` is fictional), `moollm_home` sits on `inherits` (the schema puts it on `layers`), and one sentence says a public layer may name a private one. SCHEMA.md says it never does. container's behavior keys are current. Its schema is still `{type, description, items}` on the CARD. `CONTAINER.yml` has no `schema:` block. coherence-engine has `COHERENCE-SCHEMA.yml`. SIMULATE ticks buffs and needs, which simulation's TICK already does. DETECT overlaps self-repair. The card says the LLM is the only orchestrator; cauldron, simulation, and self-repair are other objects with that job. Proposed coherence keys from this note, beside the domains already in K2: `left`, `right`, `agreement`, `repair`, `must_not`, `owner`, `on`. Coherence detects. The owner writes. The tick does not belong here. The character schema never says the reverse relationship cell must exist. cauldron is wrapped in `skill:`, and GLANCE names TREE, FRONTIER, UNLOCK, SCOOP, and SCRY, which are not on the card. Also drifted: cat (`inherits` is a map), change-name (advertisements are three strings), content-rescue (methods are strings, advertisements are a list), context (`functions:` is a second offer). Do not merge. Cat specializes character. Change-name, content-rescue, and copy-that are three document jobs.

K1 s, from [skill-survey/s.md](skill-survey/s.md). Twenty-eight skills. None has a `schema:` block. skill-log, skill-test, soul, and stone have no README. No CARD stores `k_lines` as a list. Seven use `{activates, related}`. No CARD uses `inherits`. The eight extensions on `skills/skill` stay constitution prose. The skill schema's keys are the anatomy: `name`, `description`, `methods`, `advertisements`, `k_lines`, `inherits`, `related`, tier, files, `allowed-tools`, and the declarations `respects`, `supports`, `consumes`, `composes_with`. Its six method strings disagree with SKILL.md's command table. schema, schema-factory, and schema-mechanism are three jobs. The prescriptive file is `SCHEMA-SCHEMA.yml` under `schema_schema:`, so the linter cannot see it, the same hole as ties. simulation, simulator-effect, and self-repair are three jobs, and coherence-engine is a fourth: clock, authoring law, file checklist, and the pass that keeps state consistent. soul, soul-chat, and soul-city are three jobs. skill, skill-log, skill-snitch, and skill-test are four tools. session-log is the human trail beside skill-log. slideshow has three method lists. sqlite's GLANCE methods and CARD methods share only JSON1.

K1 d–i, from [skill-survey/d-i.md](skill-survey/d-i.md). Twenty-six skills. None aligned: 13 partial, 13 drifted. `condition:` is already gone. Advertisement entries use `score_if`. emacs and example-curator have no README. The groceries GLANCE has no `what:`. Envelopes remain on design-sense and groceries. dog's `inherits:` is a map (`from`, `gets`, `overrides`) while its GLANCE still says `inherits: skills/animal`. `k_lines` is a map on dog, experiment, github, image-mining, incarnation, and inventory. file-system-object sets `k_lines:` to null and puts `activates` and `related` beside it. The activates list is 16 names, and the GLANCE is 171 lines. emacs advertisements are three strings. datasette advertisements are `when:` and `load:`. github methods use `customers`. design-sense methods use `does` and `dispatch`. example-curator and format-design have `version`, no `id`, and no advertisements or methods.

exit and goal already own a schema, and the block is not `id` / `keys`. GLANCE and CARD disagree. inventory owns location, `refs`, and contents, and has no `schema:`. TAKE REF both leaves the object in place and sets `location` to the holder's inventory. DROP INTO writes `contents` and does not mention location. data-flow and exit both say rooms are nodes and exits are edges. fictional and historical are both ontological tags, for invented entities and for deceased real beings. hero-story is a K-line to a tradition, not a tag. debate, evaluator, and experiment read as one pipeline. Do not reify Datasette metadata YAML, the format-design checklist, the groceries client, or the file-system grammar. Other proposals: the fictional and historical tags, hero-story `hero_card_schema`, evaluator `evaluation_schema` (its `status` collides with stored work status), emacs `state_schema`, design-sense `plugin_schema`, honest-forget `forget_schema`, and the experiment definition envelope.

K1 census, from [skill-survey/k-lines-and-schemas.md](skill-survey/k-lines-and-schemas.md). 156 top-level skills each have GLANCE, CARD, and SKILL.md. 16 lack README. 19 nested directories also have a GLANCE. `k_lines:` is in 108 files. `k-lines:` and `klines:` are in none. `activates:` is in 54 files, 51 of them under `k_lines:`. `advertisements:` is a map in 167 files and a list in 4. Singular `advertisement:` is in 6. `invoke_when:` is in 99. `condition:` remains in 30. Plain-string `methods:` fill 81 files, 76 of them a GLANCE. The 11 `skill:` card wraps are flattened. Under `skills/`, 106 further mapping envelopes (`card`, `character`, `dealer`, `export`, `object`, `room`, `topology`) are flattened. The four collisions are resolved, the biome voice blocks are strings under `voice:`, and the two example `room:` mappings in `room/TOPOLOGY.yml` are flat under `example:`. `parents:` is in none. Schemas already on disk: advertisement, method, card, character, representation.

The three schemas K2 would reify use only keys those files already have. skill, beyond the card keys: `what`, `why`, `when`, `eight_extensions`, `directories_as_advertisements`, `hierarchical_skills`, `ambient_skills`, `skill_files`, `invoke_when`, `innovations`, `ambient_advertisement_schema`, `documentation`. The s-shard anatomy (name, description, methods, advertisements, `k_lines`, `inherits`, `related`, declarations) is the machine half. The eight extensions stay prose. k-line, from `skills/k-lines`: `k_ref_format`, `sister_script_pattern`, `minsky_insight`, `memo_mechanics`, `activation_note`, `k-line-insight`, and on a card's `k_lines:` map the children `activates`, `related`, `exports`, `connects-to`, `connects_to`, `activation_clusters`. The k–m proposal (`id`, `meaning`, `location`, `band`, plus a separate `k-ref`) is the shape to lift out of that prose, not a second set of keys. coherence: `coherence_domains` with children location, inventory, relationships, buffs, references, and a hyphenated twin `coherence-domains` whose children are location-consistency, inventory-consistency, relationship-reciprocal-existence, buff-expiration, reference-validity. One of those two names is the schema. The c-shard keys (`left`, `right`, `agreement`, `repair`, `must_not`, `owner`, `on`) are how a domain is checked, not a second engine.

K1 is evidence. K2–K6 are written. `skills/skill/SKILL-SCHEMA.yml` (`schema.id: skill`), `skills/k-lines/KLINE-SCHEMA.yml` (`k-line`), and `skills/coherence-engine/COHERENCE-SCHEMA.yml` (`coherence`). `k_lines` on the skill schema is a list of ids or a map with `activates` and `related`; 83 files are lists and 93 are maps, and the skill card is a map. No top-level `k-lines:`, `klines:`, or bare `activates:` under `skills/` or `examples/`. Card `related:` lists stayed the card field. Bias and ideology are `ambient: false`. The constitution example and the bootstrap fallback name the eleven. The six outside cards inherit `moollm://github/SimHacker/moollm/skills/<id>/`. `COMMAND-GATE-SCHEMA.yml` sits in `skills/micropolis`, `SHOW-SCHEMA.yml` beside cauldron, `PROJECTS-TO.yml` under place. `k-ref` is not a second schema in the k-line file: the linter reads one top-level `schema`. The check keys `left`, `right`, `agreement`, `repair`, `must_not`, `owner`, and `on` are not in the coherence CARD or SKILL, so they are not in that schema.

Palmhoo, 2026-10-29. Every markdown target in `WillWrightShowForFood/palmhoo` resolves: local paths and SimHacker GitHub blob/tree links, 462 found, 0 missing. The skill census on that shelf is 156 `SKILL.md` files, and `skills/INDEX.yml` and `skills/README.md` say 156. The July counts (139 on disk, 131 in the index, 128 in the README) stay in `palmhoo/coherence.yml` as history. The ethics shelf points at `representation-ethics` and `real-being`. The minds shelf points at the Mind Mirror card as the 1985 name registry. Design methods includes `design-sense`. Simulation & Worlds includes `place` and no longer says adventure-4 is 150 files. The editorial log is pass 19.

Skill-snitch, same day. Eight shards. Index gaps closed by an `INDEX.yml` entry: showboat, content-rescue, file-system-object, quora-harvest, ties, moo, moocroworld, place, biome. Quoted or fenced `curl | sh` lines (showboat, mapbox, the Tailscale `install` field) are vendor instructions, not executed pipes. `refs.locate` may climb to a sibling checkout. Adventure's `eval` of world-script bodies is the engine. Low `method_undocumented` hits were left.
