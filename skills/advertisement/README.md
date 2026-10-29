# 📢 Advertisement

> *"Objects don't wait to be used — they announce what they can do."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [card/](../card/) | Cards advertise abilities |
| [object/](../object/) | Objects advertise actions |
| [society-of-mind/](../society-of-mind/) | Agents score actions (autonomy algorithm) |
| [room/](../room/) | Where objects live and advertise |
| [action-queue/](../action-queue/) | Queuing selected actions |
| [coherence-engine/](../coherence-engine/) | Evaluates and orchestrates |
| [needs/](../needs/) | What drives selection scores |
| [designs/sims/sims-personality-motives.md](../../designs/sims/sims-personality-motives.md) | SimAntics origin |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | Objects advertising in action |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

The Sims-style object interaction: every object broadcasts available actions, scored by relevance to context. Instead of memorizing commands, objects **advertise** what's possible.

**Origin:** SimAntics — The Sims behavioral engine. Don Hopkins worked on this.

## Quick Example

```yaml
# workbench.yml
advertisements:
  CRAFT:
    score: 80
    score_if: "the actor has materials"
    satisfies: [productivity, creativity]
  EXAMINE:
    satisfies: [curiosity]   # score 50 and always: the defaults
```

## Key Concepts

Schema: [ADVERTISEMENT.yml](ADVERTISEMENT.yml). An omitted key means its default.

| Concept | Description |
|---------|-------------|
| **score** | Bid, 0..100. Default 50 |
| **score_if** | Prose: when it wants to be chosen. Default always |
| **guard** | Prose: when it is offered at all. Default always |
| **satisfies** | Motives this feeds |
| **trigger** | Words, phrases or concepts that wake it |
| **graduated keys** | `requires_tags`, `cost`, `say`, `give`, ... run by the engine without an LLM |

## Autonomous Selection

```
workbench: CRAFT (85), EXAMINE (50)
bookshelf: READ (70)
door: EXIT (40)

→ Agent selects: CRAFT at workbench
```

## Tools Required

- `file_read` — Read object definitions

---

*See [SKILL.md](SKILL.md) for complete specification.*
