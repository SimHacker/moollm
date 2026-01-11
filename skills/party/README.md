# 🎭 Party

> You're never alone. Unless you want to be.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [character/](../character/) | Companions are characters |
| [cat/](../cat/) | Cats as party members |
| [dog/](../dog/) | Dogs as loyal companions |
| [needs/](../needs/) | Companions have needs |
| [simulation/](../simulation/) | Party state lives in SIMULATION.yml |
| [room/](../room/) | Rooms can be party members too |
| [adventure/](../adventure/) | Parties explore adventures |

**Quick Links:**
- [Full Specification](SKILL.md) — complete party system

## Overview

Party management for companions, groups, and ensemble play. Companions have relationships with you AND each other. Asking about family/pets CREATES them!

## Simulation State

In `SIMULATION.yml`:

```yaml
party:
  members:
    - characters/don-hopkins/
    - pub/cat-cave/terpie.yml
  leader: characters/don-hopkins/
  formation: line

selection:
  targets: [pub/cat-cave/terpie.yml]  # Always a list
```

**Selection targets:** Characters, rooms (rooms are characters too!), objects, concepts.

## Commands

- `SELECT [target]` / `DESELECT`
- `PARTY` / `RECRUIT` / `DISMISS`
- `PARTY FORMATION [line/circle/defensive]`
- `HOLD / FOLLOW / SCATTER / REGROUP`

## Emergent Creation

Asking about family or companions **creates them**!

> "Do I have a sister?" → Now you do.

