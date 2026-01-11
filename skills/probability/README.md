# 🎲 Probability

> No dice. Just odds and narrative.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [character/](../character/) | Stats used in calculations |
| [buff/](../buff/) | Buffs modify probabilities |
| [scoring/](../scoring/) | Scores based on outcomes |
| [coherence-engine/](../coherence-engine/) | LLM calculates probabilities |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

LLM-calculated success chances. No physical dice — the LLM calculates probability from stats + modifiers and narrates outcomes consistently.

## Calculation

```
base_chance = (stat_1 + stat_2) / max_possible
modified_chance = base_chance + relationship + buffs
```

## Modifiers

| Relationship | Modifier |
|--------------|----------|
| Stranger | +0 |
| Friend | +0.2 |
| Soulmate | +0.4 |

## Malfunction Stacking

Multiple risky items compound:

```
P(something fails) = 1 - (P(item1 works) × P(item2 works) × ...)
```

