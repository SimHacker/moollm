# Activation: one "when to use me" at four resolutions

Round 2 of the vocabulary analysis. Round 1 (cluster 4 in
[../VOCABULARY-CLUSTERS.md](../VOCABULARY-CLUSTERS.md)) left open "`when:` (GLANCE) and
`invoke_when:` (CARD): one key or two?". Numbers from `behavior_survey.py activation` and
ad-hoc counts recorded here (2026-10-29).

## The four declarations

| Key | File | Skills | Shape | Example (abstract, room) |
|---|---|---|---|---|
| `when:` | GLANCE | 143 (133 list, 10 string) | "situation" → VERBS | `'"Give voice to idea" → PERSONIFY'` |
| `invoke_when:` | CARD | 47 | list of situations | `"giving voice to a concept"` |
| `advertisements:` | CARD | 119 | map VERB → {score, condition, effect} | `PERSONIFY: {score: 85, condition: "Want to give voice to an idea"}` |
| `k_lines:` | CARD | 42 | map, usually `activates:` list of symbols | room: `[ROOM, SPATIAL, NAVIGATION, ...]` |

Per skill (153 parseable): 70 have GLANCE `when` + advertisements; 23 have all four; 15 have
`when` + `invoke_when` + advertisements; 16 have `when` only; 4 have none.

## What the arrows point at

475 of 507 GLANCE `when:` entries have the form `"situation" → VERB[, VERB]`. Resolving the
verb tokens against the same skill's CARD:

| Resolves to | Tokens |
|---|---|
| a card method | 310 (15 of these are also advertisements) |
| a card advertisement only | 33 |
| neither | 584, an upper bound: it counts prose words on the right of the arrow as well as verbs the card lacks |

GLANCE `when:` mostly points at methods. Card advertisements mostly don't (342 of 404 name no
method, see [ADVERTISEMENTS.md](ADVERTISEMENTS.md)). The GLANCE line is closer to SCHEMA's
"an advertisement names a method plus guard and score" than the card advertisements it
summarises.

## Reading

They are one concept, interest, at different resolutions, which is what the Semantic Image
Pyramid prescribes:

```
GLANCE when:          situation → VERB                    (one line each, scan)
CARD invoke_when:     situation                           (prose list, no target)
CARD advertisements:  VERB → {score, condition, effect}   (scored, sniff)
CARD k_lines:         symbols that wake the skill         (vocabulary, not situations)
```

`k_lines:` is a different thing: words that should activate the skill, not situations it fits.
It overlaps `tags:` and the round-1 `activates:` synonym, not the other three.

`invoke_when:` is the odd one: a situation list with no verb and no score, carried by 47
cards, 41 of which also have advertisements whose `condition:` fields cover the same ground.

## Options

1. **Pyramid, derived.** CARD `advertisements:` is the source: each entry has `score`,
   `score_if` (the situation), optional `method`. GLANCE `when:` is generated from it
   (`score_if → NAME`). `invoke_when:` is retired into `score_if` fields.
2. **Pyramid, hand-kept.** Same three levels, written by hand, linted for agreement (every
   GLANCE verb exists in the CARD as an advertisement or method).
3. **Two keys.** Keep `when:` for GLANCE and `invoke_when:` for CARD as two resolutions of a
   situation list; advertisements stay separate and scored.

A GLANCE line is written for a glance ("Give voice to idea"), a condition for a decision
("Want to give voice to an idea"); generating one from the other loses that register. The lint in Option 2 catches drift
without flattening the prose.

## Leanings

- Option 2, hand-kept pyramid with an agreement lint (65%). Option 1 if the generated GLANCE
  lines prove good enough on a sample of ten skills.
- Retire `invoke_when:` into advertisement `score_if:` fields (70%); 41 of 47 cards already
  have the advertisements to receive them, and the other 6 would gain advertisements.
- `k_lines:` stays separate; `activates:` folds into it (80%, same as round 1).
