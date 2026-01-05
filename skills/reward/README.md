# 🎁 Reward

> Rewards should feel earned and fitting

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Dynamic achievement rewards that are thematically appropriate and feel earned. Not pre-defined — generated to match the achievement.

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

## Related Skills

- [scoring](../scoring/) — score determines reward quality
- [buff](../buff/) — some rewards are permanent buffs
