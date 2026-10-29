# CARD analysis: advertisements, methods, and what a card carries

Round 2 of the object-system vocabulary work. Round 1 ([VOCABULARY-CLUSTERS.md](VOCABULARY-CLUSTERS.md))
clustered top-level keys into [SCHEMA.md](SCHEMA.md). This round reads a CARD the way a model
does, top to bottom, as one file, and measures each part against the two rules in the
constitution: [§15](../../kernel/constitution-core.md#15-the-semantic-image-pyramid-concentrated-not-dry-universal)
(concentrated, not DRY) and [§16](../../kernel/constitution-core.md#16-advertisements-push-into-the-auction-compile-graduate-universal)
(advertisements: push into the auction, compile, graduate). Analysis only: nothing has been
migrated.

Cards keep object-specific YAML Jazz. Where a card's keys overlap a standard pattern, they
align with it.

Reproduce: `python3 skills/prototype/scripts/behavior_survey.py all` (sections `cards`,
`methods`, `adverts`, `activation`, `world`). Counts below are from 2026-10-29: 153 cards
parsed, 3 unparseable.

## 1. What a CARD carries

| Layer | Keys | State |
|---|---|---|
| Identity, Dublin Core | `id`, `name`, `description`, `type`, `tags`, `credits`, `lineage`, `related`, `see_also` | mostly aligned; `type:` is a list in 120 of 132 cards (SCHEMA: one id) |
| Card face | `tier` 126, `emoji` 124, `tools` 103, `rarity` 76, `tagline` 60, `files` 38, `t_shirt` 9 | consistent; card-standard |
| Advertisements | `advertisements` 119 | section 2 |
| Methods | `methods` 121 | section 4 |
| Activation | `k_lines` 43, `invoke_when` 47, GLANCE `when:` 143 | section 5 |
| Conventions of the objects it makes | copied from the interface file (ROOM, CHARACTER, ...) | **thin**, see below |
| Object-specific YAML Jazz | 382 of 446 distinct keys appear in one or two cards | stays |

### Copy-down from interface files

§15 says the card carries the most important fields and methods of its interface files. The
prototype-file migration moved them out instead:

| Skill | Interface file | Its methods | In the CARD | Its keys not named in the CARD |
|---|---|---|---|---|
| room | `ROOM.yml` | LOOK, ENTER, EXIT, CONTENTS, ADVERTISE | none | `builder_commands` |
| character | `CHARACTER.yml` | STATUS, MOVE, TAKE, DROP, WEAR, REMOVE-PERSONA, RELATE, SNIFF, LICK, GREET, CUDDLE | CREATE only | `inventory_capacity` |
| container | `CONTAINER.yml` | none | none | `default_place`, `provides`, `request_list`, `push_to`, `reserve`, `on_child_change`, `on_place` |
| object | `OBJECT.yml` | none | none | `disabled` |
| ties | `TIES.yml` | none | none | `ties_schema`, `glyphs`, `provenance` |

A model reading the room CARD today learns that rooms advertise NAVIGATE and BUILD-WORLD but
not that every room answers LOOK.

### Synonyms to align

| Key | Cards | Aligns to |
|---|---|---|
| `one_liner` | 3 | `tagline` |
| `references`, `documentation` | 12, 11 | `see_also` (files to read) |
| `related_skills` | 5 | `related` |
| `sibling_skills`, `composes_with`, map-form `related` | 7, 4, 5 | `related` entries with a role: `{ id: room, role: sibling, when: "for places" }` |
| `inherits_from` | 2 | `inherits` |
| `inherited_by`, `can-be-inherited-by` | 2, 1 | a concentrated copy of a computed index; keep, lint against the resolver |
| `allowed_tools` | 4 | `tools`, or the foreign spelling `allowed-tools` (SCHEMA: foreign keys keep theirs) |
| `activates`, `protocol`, `aliases` | 2, 10, 2 | `k_lines` |
| `when_to_use`, `use_when` | 2, 1 | advertisements (section 5) |
| `advertisement` (singular), `advertisement_names`, `ambient-advertisement` | 3, 1, 1 | `advertisements` (section 2) |
| `skill:` map | 11 | flat keys; it repeats name/emoji/tagline under an envelope |
| `status`, `version` | 7, 11 | SCHEMA: no stored status; file facts go in git |
| `schema`, `state_schema`, `plugin_schema`, `attribution_schema`, `advertisement_schema`, `ambient_advertisement_schema` | 13 | one `schema:` map, so a linter can find a card's description of its own objects |
| `examples`, `example`, `examples_worked`, `examples_public`, `example-script` | 13 | `examples` |
| `principles`, `principle`, `philosophy`, `core_insight`, `insight`, `the-insight` | 24 | `principles` |
| `anti_patterns`, `anti-patterns` | 5 | `anti_patterns` |

37 top-level keys in 22 cards use hyphens; SCHEMA spells schema keys with underscores.

Three cards don't parse (`economy`, `no-ai-overlord`, `no-ai-soul`), all from a quoted string
followed by more text on one list line: `- "I think..." (overlords don't think, they KNOW)`.

## 2. Advertisements: one concept

Everything that says "choose me, here, for this" is an advertisement. The populations differ
in which fields they use, not in what they are.

| Population | Where | Shape | Score | Fields in use |
|---|---|---|---|---|
| World offers | objects, rooms, characters | 63 map blocks, 121 list blocks (offers and triggers together) | 0..100 | score 557, action 337, description 322, effect 211, score_if 129 |
| Word and concept triggers | props, characters | list entries | 0..1 (259 of 260) | trigger 253, response 297, result 161 |
| Skill relevance | 119 cards | 109 map, 10 list | 0..100 | score 382, condition 375 (prose), effect 43, trigger 23, satisfies 11 |
| Provides and wants | singular `advertisement:` in leela-ai, manufacturing-intelligence, society-of-mind | `{provides, wants, motives_satisfied}` | none | |

How each maps into the one schema:

- **Skill relevance.** `condition:` is a prose `score_if:`: the situation in which the skill
  wants to be chosen. An LLM evaluates it, so it stays prose without a `_js`. 342 of 404 name
  no method; that is fine, the effect is "load this skill and act", and `method:` is optional.
- **Triggers.** `trigger:` is a standard field naming the words, phrases or concepts the
  advertisement responds to; `response:`/`result:` is an effect (say this). The 0..1 score
  rescales to 0..100. A trigger advertisement can carry guard, score_if and parameters like
  any other, which is what keeps it from being a canned reply.
- **Provides and wants.** Each `provides:` item becomes an advertisement; `wants:` become the
  `parameters:` or `requires:` of the advertisements that need them; `motives_satisfied:`
  becomes `satisfies:` on each.

```yaml
# leela-ai, one provides item recast
advertisements:
  CAUSAL-INFERENCE:
    score: 80
    score_if: "a visual event needs a why, not just a what"
    parameters: { video_feeds: "camera streams", domain_context: "what this factory makes" }
    satisfies: [safety, compliance]
    effect: "schema mechanism explains the event as a causal chain"
```

### Shape problems

1. 442 world advertisements in 97 files are list entries. None has `name:`; 243 use
   `action:`. The compiler export names them `ACTION_0`, `ACTION_1`, ... and keeps only
   description, score and effect, dropping `action` 243, `response` 237, `trigger` 199,
   `result` 112, `score_if` 104, `condition` 40.
2. The linter iterates advertisements with `.items()`; on a list it raises, an `except: pass`
   swallows it, and that object's simulate and method checks never run.
3. `condition:` (52 world, 375 card) is read by nothing. In world offers it means `guard:`
   ("player has feather_token"); in cards it means `score_if:`.
4. `skills/advertisement/CARD.yml` documents `action, description, preconditions, score,
   score-if, satisfies`, which matches neither the engine nor any population.

## 3. Compile, then graduate

The compiler's model: every prose key gets a `_js`/`_py` sibling that an LLM writes, and the
engine runs. State of that pipeline:

- The compiled adventure-4 world has 193 `guard_js`, 64 `score_if_js`, 64 `effect_js` slots;
  3 are filled (the gong's flag disjunctions).
- `adventure.js` and `adventure_runtime.py` read `guard`, `guard_fail`, `effect` directly; no
  other advertisement key is run by the engine.
- Committed `_js` exists in 2 world files: `pub/ROOM.yml` (the bar's tag guard,
  `tags.includes('staff') || ...`, and a fee guard, `world.has('coins', fee)`) and `pub/gong.yml`
  (the three flag disjunctions). The object and exit CARDs show the form in examples.

So nothing has graduated yet, and very little has been compiled. The prose already repeats
shapes that could skip compilation and graduate straight to parameterized keys. Counts are
regex families over world advertisement prose (guard, condition, score_if, requires, trigger,
effect, response, result); they are approximate, roughly ±20%.

### Conditions

| Pattern in the prose | Count | Graduated key (proposal) |
|---|---|---|
| `score_if: always` / never / any | 58 | omit `score_if:` (absent means always) |
| tag or role lists: `requires: ['staff', 'bartender']`, the bar's compiled guard | 48 | `requires_tags: [staff, bartender]` |
| "player has X", "have coin", "item in inventory" | 11 | `requires_items: [feather_token]` |
| bare flag or state word (`open`, `lit`), `state == x` | 20 | `when_state: { open: true }` |
| flag disjunctions (`good_news OR victory OR milestone`) | 4, 3 compiled | `when_flags: { any: [good_news, victory, milestone] }` |
| darkness and lighting | 6 | `requires_lighting: { max: 2 }` |
| proximity (in room, near, touching) | 7 | `reach: room` (the scale in [kernel/INTEREST-GATES.yml](../../kernel/INTEREST-GATES.yml): user, world, room, near, touch, self) |
| fees and coins in guards | 1 compiled, 50 pay effects | `cost: { coins: 5 }` |
| single-word triggers | 192 of 253 | `trigger: { words: [latte, espresso] }`, matched by the engine |
| phrase and concept triggers | 61 | `trigger: { phrases: [...], concepts: [...] }`; phrases match mechanically, concepts stay for the LLM |

### Effects

| Pattern | Count | Graduated key (proposal) |
|---|---|---|
| say, narrate, respond | 161 | `say:` (template with parameters) |
| move, go, teleport | 106 | `move_to:` |
| set state, open, lock, light | 63 | `set: { lit: true }` |
| pay, charge, tip | 50 | `cost:` / `pay:` |
| give, take, drop | 49 | `give:`, `take:` |
| motive and buff changes | 47 | `satisfies: { hunger: 30 }`, `buff:` |
| spawn, create, summon | 31 | `spawn:` |

Those key names are the vocabulary of the deterministic DSL in §16: `requires_tags`,
`when_state`, `reach`, `cost` are its adjectives and prepositions; `say`, `move_to`, `set`,
`give`, `take`, `spawn` are its verbs; items, tags, flags and rooms are its nouns. A graduated
key coexists with prose: an advertisement may have `requires_tags:` and a prose `guard:` for
what the tags don't capture, and only the prose needs a `_js`.

Plugged-in objects extend the vocabulary: a coin dispenser that defines `cost:` makes `cost:`
runnable in any room that contains one, without an engine change.

## 4. Methods

One core across cards (759 entries), prototype files and world objects (444 entries):

| Field | Cards | Notes |
|---|---|---|
| `description` | 470 | `does:` (20, and the prototype files) is the same field |
| `output` | 382 | free text; 262 are combinations of chat, state-change, file |
| `parameters` | 379 | map name → prose; `params` 14, `args` 16, `input` 5 are synonyms; 14 are lists |
| `signature` | 294 | 224 start with the method name |
| `invoked_by` | 286 | player 178, any 21, self 16; `customers` (github, trekify) is the same |
| `effect` | 266 | same word and meaning as in advertisements |
| `returns` | 50 | overlaps `output` |
| `satisfies` | 26 | same as in advertisements |

Long tail (`note`, `example`, `variants`, `delegates_to`, `gate`, ...) is YAML Jazz and stays.

Shape problems:

- `_check_methods` compiles only string entries (name → prose body, with sibling
  `methods_js:`/`methods_py:` maps). All 444 world method entries are maps, so none is
  compiled. Compiling `effect:` (or a `body:`) to an entry-level `effect_js:` would match
  advertisements.
- 11 string-form card methods (content-rescue, showboat) and 3 list-form method blocks
  (skill-log, skill-snitch, skill-test).
- Case already carries meaning: UPPERCASE names are commands a player types (741);
  lowercase names are code-callable functions or protocol steps (18: biome, society-of-mind,
  file-system-object). Not written down anywhere.

The same graduation applies to method effects: a method whose effect is "set lit to true and
say 'the lamp glows'" is `set:` plus `say:`, with no body to compile.

## 5. Activation at each resolution

| Level | Key | Skills | Form |
|---|---|---|---|
| GLANCE | `when:` | 143 | `'"Give voice to idea" → PERSONIFY'` (475 of 507 entries) |
| CARD | `advertisements:` | 119 | `PERSONIFY: { score: 85, condition: "Want to give voice to an idea" }` |
| CARD | `invoke_when:` | 47 | `"giving voice to a concept"` |
| CARD | `k_lines:` | 43 | `activates: [ROOM, SPATIAL, NAVIGATION]` |

GLANCE `when:` is the concentrated copy of the card's advertisements, at glance size, which is
what §15 asks for. Its arrows mostly name methods: 310 verb tokens resolve to card methods, 33
to advertisements only (584 unresolved tokens include prose words, so that count is an upper
bound). The agreement check is a lint: every arrow target exists in the CARD as an
advertisement or method.

`invoke_when:` is a second list at the same level as the advertisements, in the same file;
41 of the 47 cards that have it also have advertisements covering the same situations. Each
`invoke_when:` line is a `score_if:` waiting for its advertisement.

`k_lines:` are the skill's trigger words. They are to a skill what `trigger: { words: }` is
to a world advertisement: words that should wake it. One vocabulary for both lets the same
matcher run on both.

## 6. Recasting "interest"

"Interest" for an advertisement comes from NeWS event dispatch. Where it means advertisement,
it becomes advertisement:

| Where | Use | Recast |
|---|---|---|
| `kernel/INTEREST-GATES.yml` | "Interests (objects, skills, characters, actions) have gates" | `ADVERTISEMENT-GATES.yml`; its proximity scale is the `reach:` key in section 3 |
| `skills/skill/CARD.yml` | `directories_as_interests:`, "virtual interests" | `directories_as_advertisements:` (yaml-jazz GLANCE already says this) |
| `skills/adventure/events/INDEX.yml` | "Each handler expresses INTEREST in certain event types" | "advertises which event types it handles" |

Kept, because they mean something else: Sims personality interests (`interests:` in
`skills/mind-mirror/SIMS-STATS.yml`, `subject.interests.physics` in ADVENTURE-COMPILER.md,
character interest lists), "Person of Interest", and ordinary English.

## Decisions

| # | Decision | Leaning | Confidence |
|---|---|---|---|
| 1 | Fix the compiler's list-advertisement data loss and the linter's swallowed exception before migrating | yes | 85% |
| 2 | Fix the three unparseable cards | yes | 95% |
| 3 | One advertisement schema: score 0..100, guard, score_if, parameters, effect, satisfies, trigger, optional method; prose keys compile to `_js`/`_py` | yes | 85% |
| 4 | World list-form advertisements become maps keyed by `action:` | yes | 85% |
| 5 | `condition:` becomes `guard:` in world objects and `score_if:` in cards | yes | 75% |
| 6 | Triggers: `trigger:` field, scores ×100, `response:`/`result:` become effects | yes | 80% |
| 7 | Singular `advertisement:` provides/wants/motives broken into advertisements | yes | 80% |
| 8 | First graduated keys: `requires_tags`, `requires_items`, `when_state`, `when_flags`, `trigger.words`, `say`, `set`, `move_to`, `give`, `take`, `cost` | start with the top four conditions and `say`/`set` | 65% |
| 9 | Copy prototype methods and key slots down into the room, character, container, object and ties CARDs; lint agreement | yes | 85% |
| 10 | Method core as in section 4; `does:` → `description:`; map-form methods compile `effect:` to `effect_js:` | yes | 75% |
| 11 | Document method-name case: UPPER commands, lower functions and protocol steps | yes | 80% |
| 12 | GLANCE `when:` stays, linted against the CARD; `invoke_when:` lines become advertisement `score_if:` | yes | 70% |
| 13 | `k_lines:` and `trigger.words` share one matcher | yes | 60% |
| 14 | Recast the three "interest" uses in section 6 | yes | 90% |
| 15 | Synonym table in section 1, one batch per row, after a "what a CARD carries" section in `skills/card/SKILL.md` | yes | 70% |
| 16 | `type:` one id, extra values to `tags:` | yes | 65% |
