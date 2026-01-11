# ✨ Buff

> *"All effects are buffs. Some are just shitty."*

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Temporary effects system. Buffs modify stats, abilities, or behavior. **Curses are just negative buffs** — no separate system needed.

## Quick Example

```yaml
buff:
  name: "Caffeinated"
  source: "Espresso"
  effect: { energy: +2, focus: +1 }
  duration: 5  # simulation turns
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Numeric** | `{ energy: +2 }` |
| **Semantic** | "feeling lucky" (LLM interprets) |
| **Mixed** | Both stat mods and vibes |
| **Duration** | Turns, natural language, or conditional |
| **Stacking** | Same source refreshes, different sources add |
| **Synergies** | Some buffs combine into stronger effects |

## Sources

| Source | Example |
|--------|---------|
| Interactions | Petting cat → joy |
| Consumables | Coffee → energy |
| Locations | Pub → comfort |
| Items | Lamp → grue immunity |
| Personas | Theme-specific buffs |

## Buff Library

Pre-made buffs ready to use! See `buffs/INDEX.yml`:

```yaml
# Reference from any character
character:
  buffs:
    - ref: skills/buff/buffs/INDEX.yml#fire-resistance
    - ref: skills/buff/buffs/INDEX.yml#haste
    - ref: skills/buff/buffs/INDEX.yml#grue-repellent
```

**Categories in library:**
- Elemental resistances (fire, cold, lightning)
- Movement (haste, water-walking, slow-fall)
- Perception (darkvision, true-sight, detect-magic)
- Stealth (invisibility, silence)
- Combat (berserker-rage, stoneskin)
- Adventure-4 specific (grue-repellent!)

## Related Skills

- [time/](../time/) — Duration measured in simulation turns
- [needs/](../needs/) — Buffs affect need decay
- [character/](../character/) — Buffs stored in character state
- [persona/](../persona/) — Personas grant buffs

## Tools Required

- `file_read` — Read buff definitions
- `file_write` — Update buff state

---

*See [SKILL.md](SKILL.md) for complete specification.*
*See [buffs/INDEX.yml](buffs/INDEX.yml) for the buff library.*
## Buff Library

See `buffs/INDEX.yml` for 20+ pre-made buffs (fire-resistance, haste, grue-repellent, etc.)
