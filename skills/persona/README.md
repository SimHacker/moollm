# 🎭 Persona

> Identity layers for characters — WHO they are vs WHAT they do

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Personas define **who** a character is, separate from **what** they do (their role). These are combinable — same persona can wear different roles, same role can be worn by different personas.

## Persona vs Role

| Concept | Definition | Example |
|---------|------------|---------|
| **Persona** | WHO they are | Marieke: warm, patient, Dutch |
| **Role** | WHAT they do | Bartender: serve drinks, know regulars |

## Combinability

```yaml
# Same role, different personas
coffeeshop: { role: bartender, persona: marieke }
tavern:     { role: bartender, persona: grim }

# Same persona, different roles
working:  { persona: marieke, role: bartender }
studying: { persona: marieke, role: botanist }
```

## File Patterns

- Lightweight: `persona-name.yml` in room directory
- Heavyweight: `persona-name/PERSONA.yml` with accessories

## Related Skills

- [character](../character/) — personas attach to characters
- [mind-mirror](../mind-mirror/) — personality traits
- [buff](../buff/) — personas can grant buffs
