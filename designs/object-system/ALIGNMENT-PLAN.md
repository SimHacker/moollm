# Plan: define the schemas, align the repos

Turns the two analyses into schemas, tools and migrations:
[CARD-ANALYSIS.md](CARD-ANALYSIS.md) (decisions 1–18) and
[CHARACTER-LAYERS-ANALYSIS.md](CHARACTER-LAYERS-ANALYSIS.md) (L1–L12). Governing rules:
constitution [§15](../../kernel/constitution-core.md#15-the-semantic-image-pyramid-concentrated-not-dry-universal)
(concentrated not DRY, one CARD per object, layers across repos) and
[§16](../../kernel/constitution-core.md#16-advertisements-push-into-the-auction-compile-graduate-universal)
(one advertisement schema, compile then graduate, documented defaults).

Repos in scope: moollm, WillWrightShowForFood (wwsff), DonHopkins, MicropolisCore,
RepoShowPrivate. Each repo gets its own commits; untracked files in a repo are Don's work in
progress and go into that repo's first commit.

Work runs in five phases. Phases 1 and 2 can run in parallel once phase 0 is done; phase 3
needs both; phase 4 runs after every batch and once at the end.

## Phase 0: decide

Don approves, edits or rejects the decisions in both analyses. Approved decisions go into
[SCHEMA.md](SCHEMA.md) and the objsys-001 history; rejected ones are struck from the
analyses. Facts about real people need a human regardless: every `consent.state: unverified`
and every cross-layer disagreement is listed in `tasks/ALIGNMENT-REVIEW.yml`.

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

Settled while drafting, open to reversal:
- `invoked_by` default depends on name case: `[player, npc]` for UPPERCASE commands,
  `[self, engine]` for lowercase functions (S2).
- `governed_by` defaults to both real-being and representation-ethics, matching the biography
  header (S5).
- `score_hint` words map to numbers: high 80, medium 50, low 20 (S1).
- `requires_items` defaults to all, not any; `consume` lives in its map form (S1).
- Card defaults: `k_lines` = the id uppercased, `tier` 2 (0 = foundational/ambient), `rarity`
  common (values include epic), `see_also` = SKILL.md and README.md, `related:` entries
  `{id, role, when, why}`, `license` added as the Dublin Core rights field (S3).
- A card's `advertisements:`/`methods:` take entry shapes through `of:`, not `extends:` (S3).
- Layer values add `profile` (Palm's wwsff page) and `prototype` (other moollm characters) (S4).
- A public layer may name a private one in `derived_from:` or `layers:` by ref, never
  `inherits:` from it (S4; the Alan Kay example names the DonHopkins repo).
- Canonical layer order for disagreements: real beings biography, profile, adventure,
  prototype, page, cast, audience; fictional beings adventure first (T3).

Open:
- `score_if`: S1 defines a false `score_if` as bid 0 (still available), a numeric `score_if_js`
  replaces the score. `adventure_runtime.py` instead adds +20 when it holds. T6 aligns the
  runtime with whichever Don picks.
- The public-figure rule forbids "defame or mock"; the satire frames (🃏, snatch-game) and
  `donna-toadstool` (fictional satire of a public figure; its `ethics.consent_level:
  public_figure_34_felonies_fair_game` is unmigrated until this is settled) need a framing
  exception or narrower wording.
- Memorial subject rights (family, estate and people who knew them may correct; care with a
  recent death) are policy written by S5, not sourced from an existing doc.
- `public_figure` is unknown, so the private rule applies, for real people whose old level was
  1 or 2 (about 115 layers). A pass can propose `public_figure: true` where the layer's own bio
  cites published work, for Don to confirm in bulk.
- 18 DonHopkins layers and a few wwsff ones claimed explicit consent with no evidence on file:
  `consent.state: unverified`, listed in `tasks/ALIGNMENT-REVIEW.yml` for Don to confirm with a
  date and evidence, or correct.
- `real_being` defaults to false in the adventure layer, so adventure-4's don-hopkins and
  richard-bartle must state `true`; or default true everywhere unless `status: fictional` (S4).
- `invitation.status` values in use but missing from wwsff `invitation-workflow.yml`: `warm`,
  `dream_guest` (also a layer), `stub`, `not_offered`; cast `status: active` is unmapped (S4).
- Fictional signifier: 🎭 (representation-ethics table) or 📖 (adventure-4 headers); 🤖 for
  robots and AIs (S4).
- `moollm_home:` is aliased to `inherits:`, but `audience-character.yml` describes it as a
  cross-promotion link, which reads like `layers.adventure` (S4).
- wwsff `portrayal-standards.yml` uses `meta:`, not `schema:`, and its consent table omits
  level 4; it becomes `schema: { extends: [representation] }` in phase 3.

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
- `compile` on adventure-4 stops on 48 non-standard `mind_mirror` properties

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
applying. M12 (consent as facts) is applied.

| Row | Repos | Files (approx.) | Change |
|---|---|---|---|
| M1 | moollm | 3 | fix the unparseable cards |
| M2 | moollm | 10 cards, 97 world files | advertisement lists → maps keyed by name |
| M3 | moollm | 52 world, 375 card entries | `condition:` → `guard:` (world) / `score_if:` (cards) |
| M4 | moollm, wwsff | 260 | trigger entries: `trigger:` field, score ×100, `response:`/`result:` → `say:` |
| M5 | moollm | 58 | drop `score_if: always` and other values that restate a default |
| M6 | moollm | 20 entries, prototypes | `does:` → `description:`; `params`/`args`/`input` → `parameters` |
| M7 | moollm | synonym table rows | `one_liner`, `references`, `related_skills`, `inherits_from`, `activates`, `allowed_tools`, ... one row per commit |
| M8 | wwsff, DonHopkins | 434 | flatten `character:` envelopes (`flatten.py`) |
| M9 | wwsff, DonHopkins, MicropolisCore | ~70 | parent spellings → `inherits:` / `derived_from:` / `layers:`; cross-repo refs → `moollm://` |
| M10 | DonHopkins | ~70 | `representation.protocol:` → `governed_by:` |
| M11 | moollm | 3 | recast "interest": `INTEREST-GATES.yml` → `ADVERTISEMENT-GATES.yml`, `directories_as_interests`, event-handler wording |

### Judgment

| Row | Repos | Shards | Agent task |
|---|---|---|---|
| J1 | moollm | 5 cards | copy prototype methods and key slots down into the room, character, container, object, ties CARDs |
| J2 | moollm | 153 cards in 8 shards of ~20 | `invoke_when:` lines into advertisement `score_if:`; `type:` list → one id + `tags:`; singular `advertisement:` → advertisements; `skill:` envelope; `status`/`version`; hyphenated keys; check GLANCE `when:` agreement |
| J3 | moollm | adventure-4 in 6 shards by directory | graduate the obvious patterns (tag lists, items, state, flags, triggers, say/set) beside the prose, keep prose where it says more |
| J4 | moollm, wwsff | 62 multi-interface directories in 3 shards | decide which UPPERCASE files are interfaces; write or extend the one CARD that summarizes them |
| J5 | wwsff | 303 profiles in 8 shards of ~40 | core keys present (L1), `signifier`/`emoji` split, `type:` → being kind + `layer:` role, consent spelling, declare `derived_from:` the DonHopkins layer where one exists |
| J6 | wwsff | 28 audience seats, 25 cast | each seat names its profile layer; cast `inherits:` maps split; `layers:` copies |
| J7 | DonHopkins | 90 in 3 shards | core keys, `layers:` pointing at the wwsff profile, ethics header kept (it is the travelling copy) |
| J8 | MicropolisCore, RepoShowPrivate | 1 page, 4 cards; private characters | declare relations only; RepoShowPrivate stays private and nothing from it is copied into public repos |

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
- Reparse every changed file.
- A human-review list collects facts flagged by agents (consent, life dates, relations) in
  `designs/object-system/tasks/ALIGNMENT-REVIEW.yml`.

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
