# Advertisements: four concepts under one key

Round 2 of the vocabulary analysis, looking inside each `advertisements:` entry rather than at
the key. Numbers from `python3 skills/prototype/scripts/behavior_survey.py adverts` and `world`
(2026-10-29). Round 1 is [../VOCABULARY-CLUSTERS.md](../VOCABULARY-CLUSTERS.md) cluster 6;
the canonical form is [../SCHEMA.md](../SCHEMA.md).

## What SCHEMA.md says

> `advertisements:` map, each naming a method plus guard and score.

Almost nothing in the repo is written that way. 18 of 404 card advertisements name a method,
none has a `guard:`, and the 442 list-form entries in world files are not maps.

## The four concepts

| # | Concept | Where | Shape | Score | Read by |
|---|---|---|---|---|---|
| A | **Offer**: an action an object offers a character in the world (Sims) | world objects, characters, rooms | map NAME → {description, score, score_if, guard, guard_fail, effect} | 0..100 (697 entries) | `adventure.py`, `adventure_runtime.py`, `adventure.js` |
| B | **Interest**: when a model should pick this skill, and how much it wants to be picked | 119 cards | map NAME → {score, condition (prose), effect} | 0..100 | models only; no script |
| C | **Reaction**: a phrase in chat gets a canned line | world objects (box-of-edge-cases, many props) | list of {trigger, score, response} | 0..1 (259 of 260) | nothing; the export drops it |
| D | **Profile**: what an entity provides, wants, satisfies | `advertisement:` (singular) in 3 cards (leela-ai, manufacturing-intelligence, society-of-mind) | map {provides, wants, motives_satisfied} | none | models only |

A and B share a shape and a scale, and differ in who chooses: a character in a simulated world
choosing among objects, or a model in a session choosing among skills. C is a different scale,
a different trigger (text, not world state) and a different output (a line, not an effect).
D is a description, not an offer.

### A: offers (the engine's meaning)

The engine's `Advertisement` dataclass (`skills/adventure/adventure.py`) and the runtime read:
`description, score, score_if, guard, guard_fail, effect`, each prose field with optional
`_js`/`_py` compiled forms. World map-form entries mostly use these.

Two other spellings carry the same meaning:

- `condition:` (40 world entries, e.g. the grue's `LURK: condition: "any dark room exists"`)
  is a guard by meaning; the engine never reads it, so those offers are always available.
- `requires:` (50, LINTER.yml) and `cost:`/`cooldown:`/`risk:` are guard-like and unread.

### B: interest (the card meaning)

```yaml
# skills/abstract/CARD.yml
advertisements:
  PERSONIFY: { score: 85, condition: "Want to give voice to an idea", effect: "Concept becomes character" }
```

- 342 of 404 entries link to no method. `abstract` has four advertisements and no methods: its
  advertisements name uses of the skill, not callable operations.
- `condition:` is always prose (375) and means "the situation in which this is relevant". In
  the engine's vocabulary that's `score_if`, not `guard`: an unmatched interest is not
  forbidden, just not attractive.
- 22 entries have no score; 1 has a formula (`task: WORK-ON-ME = priority × fit × freshness`).
- Card-specific fields with real content: `trigger` 23, `satisfies` 11, `scope/resolution/rationale`
  11 each (copy-that), `score_hint` 10 (design-sense). Object-specific YAML Jazz; allowed.

### C: reactions

```yaml
# examples/adventure-4/pub/attic/box-of-edge-cases.yml
advertisements:
  - { trigger: "edge", score: 0.95, response: "*box rattles* You rang?" }
```

199 list entries have `trigger:` and no name; 237 have `response:`. The 0..1 score is a match
confidence, not an attractiveness.

### D: profiles

```yaml
advertisement:
  provides: [{ neural_symbolic_vision: "See what + understand why" }, ...]
  wants: [...]
  motives_satisfied: [...]          # manufacturing-intelligence spells it motives-satisfied
```

## Defects found

1. **List-form advertisements lose their names and most fields in the compiled world.** 97
   world files hold 442 list entries. None has `name:`; 243 use `action:`. The export
   (`adventure.py`, "Handle list-style advertisements") names them `ACTION_0`, `ACTION_1`, ...
   and keeps only `description`, `score`, `effect`. Dropped: `action` 243, `response` 237,
   `trigger` 199, `result` 112, `score_if` 104, `condition` 40.
2. **The linter skips objects with list-form advertisements.** `_check_advertisement` is called
   through `(obj.advertisements or {}).items()`; a list raises, the surrounding `except` passes,
   and `_check_simulate` / `_check_methods` never run for that object.
3. **`condition:` is unread everywhere.** In world offers it was meant as a guard, in cards as
   a relevance cue.
4. **The advertisement skill documents a fifth schema.** `skills/advertisement/CARD.yml` gives
   `action, description, preconditions, score, score-if, satisfies` and a separate
   `advertisement_names:` list; neither the engine nor any population uses that set.
5. Round 1's batch "advertisements as list -> map, 13 files" undercounts: 10 cards and 97
   world files (121 list blocks counting nested ones).

## Options

**Key per concept.** Offers keep `advertisements:` (the Sims meaning, and the engine's). The
others get their own keys:

| Concept | Option 1 | Option 2 |
|---|---|---|
| A offer | `advertisements:` map, engine fields | same |
| B interest | `advertisements:` map with the same fields, `score_if:` replacing `condition:`; a card's subject is the skill and its world is the session | `interests:` map {score, when, effect} |
| C reaction | `reactions:` map keyed by trigger phrase {response, confidence} | `advertisements:` entries with `trigger:` + `response:`, score rescaled ×100 |
| D profile | `provides:` / `wants:` / `satisfies:` top-level | fold into `satisfies:` on each advertisement |

Option 1 for B argues that a skill is an object and the session is its world, so one schema
covers both and a model reading a card already knows how to read a room's offers. Option 2
argues the two are scored by different choosers and should not share a scale by accident.

**Shared field names, whatever the key.** `score` 0..100; `score_if` (prose, when it is more
attractive); `guard` (prose, when it is not available at all) with `guard_fail`; `effect`;
`method` (names the method the offer runs, when there is one). Each of these keeps its
`_js`/`_py` siblings.

**Method link.** "Each names a method" is false for B and rare for A. Options: make `method:`
optional (an offer without one is performed by the model from `effect:`), or require offers
to be named after a method. Optional fits the data.

**Lists to maps.** Map keyed by the offer name (`action:` value, uppercased) for A; keyed by
trigger phrase for C. Mechanical for the 243 `action:` entries; the 199 trigger entries move
with whatever C decides.

## Leanings

- Offers: `advertisements:` map with the engine's field names, `method:` optional, `condition:`
  read as `guard:` (75%).
- Interest: Option 1, the same schema with `score_if:` in place of `condition:` (60%). The
  alternative is close; the deciding question is whether a skill and a room should be scored
  by the same chooser.
- Reactions: their own key, `reactions:` (70%).
- Profiles: top-level `provides:` / `wants:` / `satisfies:` (55%; 3 files, low stakes).
- Fix defects 1 and 2 before migrating anything, so the migration can be checked against a
  compile that doesn't drop data (85%).
