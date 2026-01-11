# 📢 Advertisement

> *"Objects don't wait to be used — they announce what they can do."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [card/](../card/) | Cards advertise abilities |
| [object/](../object/) | Objects advertise actions |
| [room/](../room/) | Where objects live and advertise |
| [action-queue/](../action-queue/) | Queuing selected actions |
| [coherence-engine/](../coherence-engine/) | Evaluates and orchestrates |
| [needs/](../needs/) | What drives selection scores |
| [designs/sims-personality-motives.md](../../designs/sims-personality-motives.md) | SimAntics origin |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | Objects advertising in action |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

The Sims-style object interaction: every object broadcasts available actions, scored by relevance to context. Instead of memorizing commands, objects **advertise** what's possible.

**Origin:** SimAntics — The Sims behavioral engine. Don Hopkins worked on this.

## Quick Example

```yaml
# workbench.yml
advertisements:
  - action: CRAFT
    score_if: "has_materials"
    satisfies: [productivity, creativity]
    
  - action: EXAMINE
    score: 50
    satisfies: [curiosity]
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Score** | Base relevance (0-100) |
| **score_if** | Condition that boosts/reduces |
| **satisfies** | Needs/goals this addresses |
| **preconditions** | What must be true to enable |

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
