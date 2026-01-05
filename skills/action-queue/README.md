# 🎯 Action Queue

> *"Queue up what to do next. The Sims showed us the way."*

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Sims-inspired task scheduling: queue actions, execute in order. While [return-stack](../return-stack/) tracks *where you've been*, action-queue tracks *what you're going to do*.

## Quick Commands

| Command | Effect |
|---------|--------|
| `DO action` | Add to queue |
| `NEXT` | Execute next |
| `QUEUE` | Show queue |
| `URGENT action` | Insert at front |
| `CANCEL n` | Remove item |
| `CLEAR` | Empty queue |

## The Food Chain Pattern

Objects push prerequisites onto the queue automatically:

```
> DO eat
→ Fridge pushes GET-FOOD
→ Food pushes PREPARE
→ Stove pushes COOK
Queue: [COOK, PREPARE, GET-FOOD, EAT]
```

*Dangling a carrot in front of a donkey.* Complex sequences emerge from simple object rules.

## Related Skills

- [return-stack/](../return-stack/) — Past complements future
- [advertisement/](../advertisement/) — Objects suggest actions
- [room/](../room/) — Where actions happen
- [speed-of-light/](../speed-of-light/) — Multiple actions per turn

## Tools Required

- `file_read` — Read queue state
- `file_write` — Update queue state

---

*See [SKILL.md](SKILL.md) for complete specification.*
