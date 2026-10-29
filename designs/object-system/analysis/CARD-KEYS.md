# Card top-level keys

Round 2 of the vocabulary analysis: every top-level key in `skills/*/CARD.yml`, sorted by
whether it is schema-standard, card-standard, object-specific jazz, or a synonym that should
align. Numbers from `python3 skills/prototype/scripts/behavior_survey.py cards` (2026-10-29),
153 cards parsed. Canonical keys: [../SCHEMA.md](../SCHEMA.md) "The other keys".

## Cards that don't parse

`economy`, `no-ai-overlord`, `no-ai-soul`. Same cause in all three: a quoted string followed by
more text on one list line, which YAML rejects.

```yaml
- "I think..." (overlords don't think, they KNOW)      # no-ai-overlord line 57
```

Nothing reads these cards: not the linter, the survey, or a model using a YAML tool.

## Schema-standard

| Key | Cards | Shape | Matches SCHEMA? |
|---|---|---|---|
| `name` | 141 | str | yes |
| `id` | 129 | str | yes; 12 cards rely on the directory name |
| `description` | 133 | str | yes |
| `type` | 132 | 120 list, 12 str | **no**: SCHEMA says one id |
| `methods` | 121 | 118 map, 3 list | 3 lists, see [METHODS.md](METHODS.md) |
| `advertisements` | 119 | 109 map, 10 list | 10 lists, and the content differs, see [ADVERTISEMENTS.md](ADVERTISEMENTS.md) |
| `state` | 69 | map | yes |
| `see_also` | 66 | 65 list, 1 map | yes |
| `k_lines` | 43 | map | yes |
| `related` | 39 | 34 list, 5 map | maps carry a role per link |
| `lineage` | 30 | list/map/str | yes |
| `inherits` | 15 | 13 list, 2 map | 2 maps |
| `tags` | 13 | list | yes |

`type:` as a list: values like `[skill, protocol, methodology]` are classifications, which
SCHEMA puts in `tags:`. Only 13 cards have `tags:`.

## Card-standard (the trading-card face)

Not in SCHEMA, used consistently, read by models and by INDEX generation. They are the card's
own schema and stay.

| Key | Cards | Notes |
|---|---|---|
| `tier` | 126 | number (1 string) |
| `emoji` | 124 | |
| `tools` | 103 | `{required, optional}` map |
| `rarity` | 76 | |
| `tagline` | 60 | `one_liner` (3) is the same thing |
| `credits` | 56 | 51 map, 5 list |
| `files` | 38 | 34 map, 4 list |
| `t_shirt` | 9 | |

## Synonyms to align

| Key | Cards | Same as | Note |
|---|---|---|---|
| `one_liner` | 3 | `tagline` | |
| `references` | 12 | `see_also` | maps of {details, protocols}: files to read |
| `documentation` | 11 | `see_also` / `files` | |
| `related_skills` | 5 | `related` | |
| `sibling_skills` | 7 | `related` with a role | maps family → members |
| `composes_with` | 4 | `related` with a role | maps id → {role, when} |
| `inherits_from` | 2 | `inherits` | |
| `inherited_by`, `can-be-inherited-by` | 2, 1 | computed | a reverse index, belongs in INDEX |
| `allowed_tools` | 4 | `tools`, or foreign `allowed-tools` | SCHEMA: foreign keys keep their spelling; this one was respelled |
| `activates` | 2 | `k_lines` | round 1 decision |
| `when_to_use`, `use_when` | 2, 1 | `invoke_when` / advertisements | see [ACTIVATION.md](ACTIVATION.md) |
| `advertisement` (singular) | 3 | `provides:` / `wants:` / `satisfies:` | see ADVERTISEMENTS.md, concept D |
| `advertisement_names`, `ambient-advertisement` | 1, 1 | `advertisements:` | the advertisement skill's own card |
| `skill` | 11 | envelope | repeats name/emoji/tagline; SCHEMA says flat files |
| `status` | 7 | none | SCHEMA forbids stored status; use git or `done_when:` |
| `version` | 11 | git | SCHEMA: "about the file" goes in git or a sidecar |
| `protocol` | 10 | `k_lines` | 9 are a single K-LINE string |
| `aliases` | 2 | `k_lines` | names that should activate the skill |

`related:` with roles: `sibling_skills`, `composes_with` and the 5 map-form `related:` all want
"link plus why". One shape covers them:

```yaml
related:
  - container                                    # bare id, no role
  - { id: room, role: sibling, when: "for places" }
```

## Hyphenated keys

37 top-level keys in 22 cards use hyphens (`object-hooks`, `default-roster`, `pie-menu`,
`focus-areas`, `languages-supported`, ...). SCHEMA: keys use underscores, names of things use
hyphens. These are object-specific jazz keys, so the rule bites only if a script reads them,
but a model writing the next card copies whatever spelling it sees.

## Object-specific jazz

Of 446 distinct top-level keys, 382 appear in one or two cards: `cardinal_sins`, `ethics`, `ontology`,
`incarnation`, `combinations`, `terpene_data`, `vs_dog`, `blast_radius`, `persona_trees`, ...
They are what each card is about, and the request was to keep them. Alignment applies only
where one of them overlaps a standard pattern:

- `schema`, `state_schema`, `plugin_schema`, `attribution_schema`, `advertisement_schema`,
  `ambient_advertisement_schema` (13): a card describing the shape of its own objects. One
  key, `schema:` with sub-keys, would let a linter find them.
- `examples`, `example`, `examples_worked`, `examples_public`, `example-script` (13). The
  `example_cats`/`example_dogs`/`example_biomes`/`example_session` keys are content, not
  example collections, and stay.
- `principles`, `principle`, `philosophy`, `core_insight`, `insight`, `the-insight` (24).
- `anti_patterns`, `anti-patterns` (5).
- `workflow`, `workflows`, `playbooks`, `phases` (6).

## Options

1. **Lint, don't migrate.** Add these as `lint --strict` warnings on cards; fix as cards are
   touched.
2. **One migration batch per row** of the synonym table, each a mechanical commit with the
   survey rerun before and after.
3. **Card schema file.** Write `skills/skill/CARD-SCHEMA.yml` (or extend SCHEMA.md with a
   "cards" section) listing schema keys, card-standard keys, and the aligned names for the
   overlapping jazz, so new cards copy the right spelling.

## Leanings

- Fix the three unparseable cards first (95%); it is three lines.
- Option 3, then Option 2 for the synonym table, Option 1 for the jazz overlaps (70%).
- `type:` as a list: move the extra values to `tags:` and keep `type:` one id (65%). The
  alternative is to let SCHEMA allow a list; 120 of 132 cards already do that.
- `skill:` envelope, `status`, `version`: delete after checking that their values appear
  elsewhere in the card (80%).
