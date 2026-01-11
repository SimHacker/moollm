# 🎭 Persona

> Identity layers for characters — WHO they are vs WHAT they do

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [character/](../character/) | Personas attach to characters |
| [incarnation/](../incarnation/) | Personas can incarnate |
| [mind-mirror/](../mind-mirror/) | Personality traits |
| [soul-chat/](../soul-chat/) | Personas speak |
| [adversarial-committee/](../adversarial-committee/) | Committee members |
| [bartender/](../bartender/) | Bartender role |
| [budtender/](../budtender/) | Budtender role |
| [buff/](../buff/) | Personas can grant buffs |
| [examples/adventure-4/personas/](../../examples/adventure-4/personas/) | Live persona examples |

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

