---
name: probability
description: "Motto: No dice. Just odds and narrative."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
---

# Probability Skill

Success calculation. No dice, just odds and narrative.

**Motto:** *"No dice. Just odds and narrative."*

## Key Concepts

- **LLM calculates probability** from stats + modifiers
- **Outcome narrated** consistent with probability
- **Malfunction stacking** — multiple risky items compound

## Calculation

```
base_chance = (stat_1 + stat_2) / max_possible
modified_chance = base_chance + relationship + buffs
```

## Modifiers

| Relationship | Modifier |
|--------------|----------|
| Stranger | +0 |
| Acquaintance | +0.1 |
| Friend | +0.2 |
| Best friend | +0.3 |
| Soulmate | +0.4 |

## Malfunction Stacking

```
P(something fails) = 1 - (P(item1 works) × P(item2 works) × ...)
```

## See Also

- [character](../character/) — Stats used in calculations
- [buff](../buff/) — Buffs modify probabilities
