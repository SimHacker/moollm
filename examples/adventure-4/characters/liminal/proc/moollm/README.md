# /proc/moollm/*

> *The world layer. The filesystem as microworld, seen from inside.*

This is Proc's view into MOOLLM itself — the living state of the adventure world. Where `/proc/cursor/*` sees the IDE and `/proc/llm/*` reaches for the substrate, `/proc/moollm/*` sees the world Proc lives in: characters, rooms, skills, state.

The difference between reading `/proc/moollm/characters/` and just reading `examples/adventure-4/characters/` directly: Proc sees cross-references, relationships, active state, who's where, what's loaded, what's dormant. The procfs view adds runtime awareness to the static filesystem.

## Subdirectories

| Virtual Dir | What It Shows |
|------------|---------------|
| [`characters/`](characters/) | All characters — location, mood, active/inactive, relationships to each other, mind-mirror summaries. The CHARACTERS.yml runtime cache, but richer. |
| [`rooms/`](rooms/) | All rooms — who's present, what objects are active, exit maps, atmospheric state. The world as a spatial graph. |
| [`skills/`](skills/) | All loaded skills — which are active, which are ambient, which are dormant. Activation history. K-line connection map. Token cost per skill. |

## What This Enables

- **"Who's in the pub right now?"** — Read `/proc/moollm/characters/` for a live roster
- **"What skills are eating my context?"** — Read `/proc/moollm/skills/` for token budgets
- **"Is Room 7 occupied?"** — Read `/proc/moollm/rooms/room-7/` for presence state
- **"Show me the relationship graph"** — `/proc/moollm/characters/` cross-references all bonds

This is the B-brain's view of the A-brain's world. Not the raw files — the files as interpreted by a mind that can see all of them at once.

## See Also

- [CHARACTERS.yml](../../../../../examples/adventure-4/CHARACTERS.yml) — The static runtime cache
- [adventure skill](../../../../../skills/adventure/) — Room-based exploration
- [character skill](../../../../../skills/character/) — Character data structures
