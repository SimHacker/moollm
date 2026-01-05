# Needs Skill

Dynamic motivations (Sims-style).

**Motto:** *"Needs drive the story. Low needs create urgency."*

## Key Concepts

- **Scale** — 0-10 (10 = fully satisfied)
- **Decay** — Needs decrease over time
- **Urgency** — Low needs interrupt other activities
- **Inner voice** — YAML Jazz comments reflect mental state

## Standard Needs

| Need | Decay | Satisfy | Critical |
|------|-------|---------|----------|
| Hunger | 2 hours | EAT, DRINK | 2 |
| Energy | 3 hours | SLEEP, REST | 2 |
| Fun | 4 hours | PLAY, GAMES | 3 |
| Social | 6 hours | TALK, hang out | 3 |
| Comfort | Situational | Safe place | 4 |
| Bladder | 4 hours | Use bathroom | 1 |

## Inner Voice (YAML Jazz)

```yaml
hunger: 7   # Satisfied. No food thoughts.
hunger: 3   # Getting peckish. Is that pie?
hunger: 1   # FOOD. FOOD. FOOD. FOOD.
```

## See Also

- [time](../time/) — Needs decay over simulation turns
- [buff](../buff/) — Some buffs affect need decay
- [character](../character/) — Needs stored in character
