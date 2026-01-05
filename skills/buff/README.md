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
