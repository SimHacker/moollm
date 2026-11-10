# M3 leftovers

Survey of what M3 did not finish. No YAML was edited. A dry run of
`designs/object-system/tasks/migrations/m03_condition.py` on 2026-10-29 scans 1604 files,
would change 0, skips 1, and notes 1.

The skip is `skills/skill/CARD.yml`: `result differs from the intended data change`.
The note is `skills/thoughtful-commitment/CARD.yml`: `conditions:` (plural) in an
advertisement entry, not changed.

M3 renames `condition:` inside advertisement entries. A `CARD.yml` gets `score_if:`.
Anything else gets `guard:`. `score_if` is the situation in which the advertisement wants
to be chosen: false bids 0 and the offer stays available. `guard` is what must be true for
the offer to be offered at all: false hides it, or refuses a named invoke. A world guard,
for this note, is a condition that gates entering or using a thing (an exit, a lock, a
held item, a state such as open or lit).

## skills/skill/CARD.yml

Seven `condition:` spellings. Five are live advertisement fields. Two are not. The file
check refuses the whole edit, so the five live keys are still `condition:`.

### Inside `advertisements:`

These sit on the live map. Each is the situation in which that advertisement wants to be
chosen, beside a `score:`. A safe edit renames the key to `score_if:` and leaves the
quoted value.

```yaml
  CREATE-SKILL:
    score: 90
    condition: "Need to make a new reusable capability"

  INSTANTIATE-SKILL:
    score: 85
    condition: "Create instance from skill prototype"

  DEBUG-SKILL:
    score: 80
    condition: "Skill is broken or incomplete"

  LIFT-PATTERN:
    score: 75
    condition: "Have a local pattern worth generalizing"

  COMPOSE-SKILLS:
    score: 70
    condition: "Need to combine multiple skills"
```

Lines 75, 79, 83, 87, and 91.

### Outside `advertisements:`

Both are under `ambient_advertisement_schema`.

The first is inside the block scalar `example: |`. The scalar depicts an advertisement.
It is a string, not an entry of the live map. Line 227:

```yaml
        condition: always       # Or: "when writing YAML", "when discussing power"
```

The line walker treats the `advertisements:` line inside that scalar as a real collection
and renames this `condition:` to `score_if:`. The data walker does not, because the scalar
is a string. Parsed text then disagrees with the intended data, and the file is skipped.
That is the check. The five live keys stay `condition:` because the whole file is refused.

The second is the name of a documented field, `ambient_advertisement_schema.fields.condition`.
It is not an advertisement entry. The mechanical rename does not touch it, and it is not
what makes the check fail. Lines 236–239:

```yaml
    condition:
      type: string
      options: [always, when-condition-met]
      description: "'always' or a condition string the orchestrator evaluates"
```

### Safe edit

Rename the five keys inside the live `advertisements:` map, and only those. Values stay.
After that edit, a re-run of M3 leaves the file alone: the two remaining `condition:`
spellings are not fields of advertisement entries.

Leave the example scalar and `fields.condition`. Updating them would change the ambient
schema this card is specifying. The example's value `always` is the value M5 drops on a
live `score_if:`; here it is inside a string.

## skills/thoughtful-commitment/CARD.yml

Six `conditions:` lists. All six are inside `advertisements:`. M3 reports the plural key
and does not rename it. There is no singular `condition:` in the file.

```yaml
  TIMELINE:
    trigger: "user wants to see session events"
    conditions:
      - "user asks what happened"
      - "user wants session overview"
      - "user wants to understand flow"
    score: 95

  CONTEXT-FOCUS:
    trigger: "user wants to see context window"
    conditions:
      - "user asks what was in context"
      - "user wants to see inputs"
      - "user asks what LLM saw"
    score: 95

  COMMIT:
    trigger: "user wants to commit with context"
    conditions:
      - "staged changes exist"
      - "user asks for thoughtful/narrative commit"
    score: 90

  EXPLAIN:
    trigger: "user asks why a commit was made"
    conditions:
      - "commit hash provided"
      - "user wants reasoning behind change"
    score: 80

  BLAME:
    trigger: "user asks who wrote code and why"
    conditions:
      - "file path provided"
      - "user wants attribution + reasoning"
    score: 85

  ARCHAEOLOGY:
    trigger: "user wants history of file/pattern"
    conditions:
      - "target path or pattern provided"
      - "user exploring evolution"
    score: 80
```

Each list is when that advertisement wants to be invoked. None gates entering a place or
using an object. TIMELINE and CONTEXT-FOCUS are alternative phrasings of a user intent.
COMMIT, EXPLAIN, BLAME, and ARCHAEOLOGY each pair an input fact ("staged changes exist",
"commit hash provided", "file path provided", "target path or pattern provided") with an
intent. Those facts are inputs to the method. `score_if` is one prose string, so turning
these lists into one `score_if:` is a later judgment about shape. It is not a world-guard
rename.

## Four example cards

M3 sent these to `score_if:` because the filename is `CARD.yml`. The script's note for that
case is `CARD under examples/: condition -> score_if; check it is not a guard`. Each file
now has `score_if:` and no `condition:`, `guard:`, `exits:`, or `preconditions:`.

None of the four meant a world guard. Confidence 0.9. The prose is the situation in which
the advertisement wants to be chosen. No value matches a world-guard shape (an exit, a held
item, a lock, open or lit, a tag requirement, a fee).

### examples/adventure-4/characters/CARD.yml

`type: [room, metaphysical, repository]`. The room is the directory's metaphor, the Hall of
Bodies. The two advertisements are bids for the card. The methods BROWSE, CREATE, INSPECT,
EMBODY, RETIRE, and EULOGY have no condition.

```yaml
  MANAGE-CHARACTERS:
    score: 90
    score_if: "Need to work with character identities"

  CREATE-CHARACTER:
    score: 85
    score_if: "Starting new adventure or adding player"
```

### examples/adventure-4/personas/CARD.yml

Same shape. `type: [room, metaphysical, repository]`, the Wardrobe of Masks. TRY-ON, ADOPT,
SHED, and TRANSFORM have no condition.

```yaml
  CHANGE-IDENTITY:
    score: 90
    score_if: "Want to present differently"

  CREATE-PERSONA:
    score: 85
    score_if: "Need a new role or mask"
```

### examples/adventure-4/personas/linus-on-coffee-and-a-joint/CARD.yml

A persona card. Four advertisements carry `score_if:`. Four others (ARCHITECTURE-REVIEW,
LICENSE-ADVICE, FLAME-MELLOWING, TEACH-C) have a score and no `score_if`. `state.coffee_level`
is passive state. `invocation.triggers` is a keyword list beside the advertisements.

```yaml
  CODE-REVIEW:
    score: 95
    score_if: "Someone needs honest code feedback"

  EXPLAIN-GIT:
    score: 98
    score_if: "Someone wants to understand git"

  CRITICIZE-CPP:
    score: 75
    score_if: "Someone is considering C++ for kernel/low-level work"

  TUX-REACTION:
    score: 60
    score_if: "Need a quick gut check"
```

Each line is when that review or explanation wants to be chosen.

### examples/adventure-4/characters/real-people/zach-mama/CARD.yml

Sidecar card, `for: ./CHARACTER.yml`. Sixteen `score_if:` lines, all on advertisements.
The character directory has no `condition:` or `guard:` of its own. Twelve are topic
keywords for which bit to bid: MONICA, JACK-HARLOW, FRENCH, LGBT-PRIDE, HECKLERS,
DARK-HUMOR, CANCER-FAMILY, CIVIL-RIGHTS, CHAPPELLE-KAMAU, FULL-SETS, ROAD-TRIP, SOCCER.
MONICA also has `score_high_when:`, which only makes sense as extra bid weight. CORNER-WARMUP
says the advertisements are a topic menu. A menu that hid every topic until the keywords
appeared would not be a menu. False `score_if` drops the bid and leaves the offer available,
which is how a menu works.

Four advertisements name an effect. COME-TO-PUB relocates him, ANNIE-HALL-APPEAR
materializes him, CORNER-WARMUP names the corner he is standing on, and ANOTHER-ONE
hands out the next URL. Their `score_if` is still the bid situation.

```yaml
  COME-TO-PUB:
    score: 82
    score_if: "invited to pub or feels like performing"
    effect: "Relocate to pub/stage/; share URLs one_by_one"

  ANOTHER-ONE:
    score: 88
    score_if: "user wants next video after last topic match"
    effect: "Next rank URL from last matched topic in routines.yml"

  ANNIE-HALL-APPEAR:
    score: 92
    score_if: "pub conversation matches routines.yml annie_hall_triggers"
    effect: "Materialize on stage; paste rank-1 URL; never transcript"

  CORNER-WARMUP:
    score: 60
    score_if: "default on e2 fountain corner"
    effect: "Offer topic menu via advertisements; defer to routines.md"
```

COME-TO-PUB is when he wants to offer the move. The method `COME-TO-PUB` exists beside it.
The line does not lock the pub door.

ANNIE-HALL-APPEAR is when he wants to materialize. That is the Annie Hall bid: autonomy
picks it when the conversation matches. The card does not refuse a named invoke when the
conversation does not match. A guard would.

CORNER-WARMUP is the low bid (60) while he is at the fountain. The method already records
`location: street/lane-neverending/e2/corner-fountain-ne/`. "default on" that corner is the
situation for the floor bid. It does not gate entering the corner, and it does not refuse
the warmup anywhere else.

ANOTHER-ONE is the follow-up bid after a topic has already matched.
