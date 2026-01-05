# 🔋 Needs

> Needs drive the story. Low needs create urgency.

**Quick Links:**
- [Full Specification](SKILL.md) — complete needs system

## Overview

Dynamic motivations (Sims-style). Needs fluctuate over time and drive behavior. Low needs create urgency. Satisfied needs enable other activities.

## Scale (0-10)

| Value | Meaning |
|-------|---------|
| 10 | Fully satisfied |
| 7-9 | Comfortable |
| 4-6 | Manageable |
| 2-3 | Urgent |
| 0-1 | Critical |

## Standard Needs

| Need | Decay Rate | Satisfy With |
|------|------------|--------------|
| Hunger | 2 hours | EAT, DRINK |
| Energy | 3 hours | SLEEP, REST |
| Fun | 4 hours | PLAY, GAMES |
| Social | 6 hours | TALK, hang out |
| Comfort | Situational | Safe place |
| Bladder | 4 hours | Use bathroom |

## YAML Jazz Inner Voice

```yaml
hunger: 7   # Satisfied. No food thoughts.
hunger: 3   # Getting peckish. Is that pie?
hunger: 1   # FOOD. FOOD. FOOD. FOOD.
```

Comments update dynamically to reflect mental state!

## Related Skills

- [time](../time/) — Needs decay over simulation turns
- [buff](../buff/) — Some buffs affect need decay
- [character](../character/) — Needs stored in character state
