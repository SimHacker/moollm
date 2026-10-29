# Object-system analysis, round 2

Round 1 ([../VOCABULARY-CLUSTERS.md](../VOCABULARY-CLUSTERS.md)) clustered top-level keys and
settled `inherits:`, `defaults:`, views and flat files into [../SCHEMA.md](../SCHEMA.md). This
round looks inside the behavior keys (what a method entry and an advertisement entry contain)
and at the full set of card top-level keys. Analysis only: nothing here has been migrated.

Cards may keep object-specific YAML Jazz schemas. Where a card's keys overlap a standard
pattern, they should align with it. These files mark which is which.

Reproduce the numbers: `python3 skills/prototype/scripts/behavior_survey.py all` (or one of
`cards`, `methods`, `adverts`, `activation`, `world`).

| File | Subject |
|---|---|
| [ADVERTISEMENTS.md](ADVERTISEMENTS.md) | four concepts under one key; engine fields; compiler data loss |
| [METHODS.md](METHODS.md) | card, prototype and engine dialects; a common core |
| [ACTIVATION.md](ACTIVATION.md) | GLANCE `when:`, `invoke_when:`, advertisements, `k_lines:` as one ladder |
| [CARD-KEYS.md](CARD-KEYS.md) | every card top-level key: standard, card face, synonym, jazz |

## Findings

1. `advertisements:` means four things: world **offers** (engine, 0..100), skill **interest**
   (cards, 0..100, model-only), chat **reactions** (trigger → response, 0..1), and **profiles**
   (singular `advertisement:`, provides/wants). The score scales separate reactions from the
   rest: 259 of 260 trigger entries score 0..1, 697 of 705 others score above 10.
2. The adventure compiler drops list-form advertisements' names and most fields: 442 entries in
   97 world files become `ACTION_0...` with only description, score, effect. The linter skips
   the rest of each such object's checks because a `.items()` call on a list is swallowed.
3. The compiler only compiles string-form methods. All 444 world method entries are maps, so
   none is compiled.
4. Methods share a core of `description, signature, parameters, effect, output, returns,
   invoked_by` across cards, prototypes and world; prototypes say `does:` for `description:`.
5. GLANCE `when:` entries mostly name methods (310 tokens), card advertisements mostly don't
   (342 of 404). SCHEMA's "advertisement names a method" describes GLANCE better than CARD.
6. `invoke_when:` (47 cards) duplicates advertisement conditions in 41 of them.
7. `type:` is a list in 120 of 132 cards; SCHEMA says one id.
8. Three cards don't parse.

## Decisions to make

| # | Decision | Leaning | Confidence | File |
|---|---|---|---|---|
| 1 | Fix the compiler's list-advert loss and the linter's swallowed exception before any migration | yes | 85% | ADVERTISEMENTS |
| 2 | Fix the three unparseable cards | yes | 95% | CARD-KEYS |
| 3 | Offers: `advertisements:` map with engine fields; `condition:` → `guard:`; `method:` optional | yes | 75% | ADVERTISEMENTS |
| 4 | Interest: same schema as offers, `condition:` → `score_if:` (vs a separate `interests:` key) | same schema | 60% | ADVERTISEMENTS |
| 5 | Reactions get their own key, `reactions:` | yes | 70% | ADVERTISEMENTS |
| 6 | Profiles become top-level `provides:` / `wants:` / `satisfies:` | yes | 55% | ADVERTISEMENTS |
| 7 | Method core as listed; `does:` → `description:` | yes | 75% / 90% | METHODS |
| 8 | Engine compiles map-form methods via `body:` → `body_js`/`body_py` inside the entry | yes | 70% | METHODS |
| 9 | Method name case: UPPER = command, lower = function or protocol step | document it | 80% | METHODS |
| 10 | `output:` becomes a list over {chat, state-change, file} | yes | 60% | METHODS |
| 11 | Activation: hand-kept pyramid with an agreement lint; retire `invoke_when:` into `score_if:` | yes | 65% / 70% | ACTIVATION |
| 12 | `type:` one id, extras to `tags:` (vs SCHEMA allowing a list) | one id | 65% | CARD-KEYS |
| 13 | Synonym table in CARD-KEYS migrated one row per batch, after a card schema section exists | yes | 70% | CARD-KEYS |
| 14 | Delete the `skill:` envelope, `status`, `version` after checking their values exist elsewhere | yes | 80% | CARD-KEYS |

Decisions 3–6 interact: if 4 goes the other way, `interests:` joins the list of keys and
decision 11's lint targets it instead of `advertisements:`.
