---
name: reward
description: "Motto: Rewards should feel earned and fitting."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
---

# Reward Skill

Dynamic achievement rewards.

**Motto:** *"Rewards should feel earned and fitting."*

## Key Concepts

- **Thematically appropriate** — rewards match achievement
- **Dynamically generated** — not pre-defined
- **Types** — items, abilities, titles, heirlooms

## Types

| Type | Description |
|------|-------------|
| Items | Physical objects, tools, treasures |
| Abilities | New skills, techniques, magic |
| Titles | Recognition (LIGHT-BEARER, CAT WHISPERER) |
| Heirlooms | Items with generational power |

## Curse Lifting

Curses have lift conditions. Meeting them grants special rewards:

```yaml
buff:
  name: "Curse of Darkness"
  lift_condition: "Light 3 dark places"
  reward_on_lift: "LIGHT-BEARER title"
```

## See Also

- [scoring](../scoring/) — Score determines reward quality
- [buff](../buff/) — Some rewards are permanent buffs
