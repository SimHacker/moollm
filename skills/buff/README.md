# ✨ Buff

> *"All effects are buffs. Some are just shitty."*

## Target: Characters Only

**Buffs only apply to characters, never rooms directly.**

If a room needs buffs (e.g., "haunted", "poisoned air"), create a "room spirit" character:
- `room/dark-cave` → `character/dark-cave-spirit`
- Buff the spirit, not the room
- Keeps buff system simple: one target type, one closure signature

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [simulation/](../simulation/) | Buffs live in simulation state |
| [time/](../time/) | Duration measured in simulation turns |
| [needs/](../needs/) | Buffs affect need decay |
| [character/](../character/) | Buffs stored in character state |
| [cat/](../cat/) | Cats can grant charm buffs |
| [dog/](../dog/) | Dogs grant loyalty buffs |
| [persona/](../persona/) | Personas grant buffs |
| [yaml-jazz/](../yaml-jazz/) | Semantic buffs (LLM interprets) |
| [examples/adventure-4/](../../examples/adventure-4/) | Grue-repellent in action |

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

## Lifecycle Hooks

Buffs have three lifecycle hooks, written as natural language prompts and compiled to JS:

| Hook | Compiles To | When It Runs |
|------|-------------|--------------|
| `start` | `start_js` | Buff activates on character |
| `simulate` | `simulate_js` | Each simulation tick |
| `is_finished` | `is_finished_js` | Returns `true` → buff ends |

```yaml
buff:
  name: "Poison"
  start: "Character turns green, loses 1 HP immediately"
  simulate: "Lose 1 HP per tick, emit groaning sound"
  is_finished: "Character HP below 10 OR 5 ticks have passed"
  tags: [curse, damage-over-time]
```

**Closure signature:** `(world, subject, verb, object) => { ... }`
- `subject` = the character with the buff
- Body-only in YAML, engine wraps with signature

## Standard Character Properties

Buffs modify these standard character stats:

### Sims-Style Needs
| Property | Range | Decay | Description |
|----------|-------|-------|-------------|
| `hunger` | 0-100 | -1/hr | Need to eat |
| `energy` | 0-100 | -2/hr | Tiredness, need for sleep |
| `social` | 0-100 | -1/hr | Need for interaction |
| `hygiene` | 0-100 | -0.5/hr | Cleanliness |
| `bladder` | 0-100 | varies | Bathroom urgency |
| `fun` | 0-100 | -1/hr | Entertainment need |
| `comfort` | 0-100 | context | Physical comfort |

### Mind-Mirror Stats (Cognitive/Emotional)
| Property | Range | Description |
|----------|-------|-------------|
| `focus` | 0-100 | Concentration, attention span |
| `mood` | -100 to +100 | Emotional state (negative=sad, positive=happy) |
| `stress` | 0-100 | Anxiety level |
| `creativity` | 0-100 | Creative thinking capacity |
| `confidence` | 0-100 | Self-assurance |
| `patience` | 0-100 | Tolerance for delays/frustration |
| `curiosity` | 0-100 | Drive to explore/learn |

### Combat/Adventure Stats
| Property | Range | Description |
|----------|-------|-------------|
| `hp` | 0-max | Health points |
| `damage` | numeric | Attack power |
| `armor` | numeric | Damage reduction |
| `speed` | numeric | Movement/action rate |
| `luck` | -100 to +100 | Chance modifier |

### Room Spirit Properties

When a room has a "spirit" character, buff its stats to affect the room:

| Spirit Property | Affects | Example |
|-----------------|---------|---------|
| `production_speed` | Work rate in room | Factory spirit +20% = faster crafting |
| `error_rate` | Mistake probability | Haunted spirit +30% = more accidents |
| `comfort_bonus` | Comfort granted to visitors | Cozy spirit +15 comfort |
| `mood_influence` | Mood effect on occupants | Creepy spirit -10 mood |
| `discovery_chance` | Finding hidden things | Mysterious spirit +25% secrets |
| `danger_level` | Hazard intensity | Cursed spirit = traps more deadly |

```yaml
# Example: Haunted Library Spirit
character:
  id: library-spirit
  name: "Spirit of the Old Library"
  location: room/old-library
  
  # Base stats (affected by buffs)
  production_speed: 100    # Books found per search
  error_rate: 5            # % chance of disturbing something
  mood_influence: -5       # Slightly creepy
  discovery_chance: 20     # Good for finding secrets
  
  buffs:
    - id: poltergeist-activity
      effect: { error_rate: +15, mood_influence: -20 }
      simulate: "Occasionally knock books off shelves"
```

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


## Tools Required

- `file_read` — Read buff definitions
- `file_write` — Update buff state

## Relationship to Mount

| Layer | Purpose |
|-------|---------|
| **Buff** | Game mechanics — stats, durations, stacking, chains |
| **Mount** | Skill overlays — personality modification, room zones |

Buffs are for **numeric/semantic effects** (energy +2, "feeling lucky").
Mounts are for **skill attachment** (NO-AI-JOKING™ on Pee-wee).

They can work together: a mounted skill might grant buffs, or a buff might reference a skill.

See: [mount/](../mount/) for skill mounting, [NO-AI Brand](../../designs/eval/NO-AI-BRAND.md) for mounting philosophy.

---

*See [SKILL.md](SKILL.md) for complete specification.*
*See [buffs/INDEX.yml](buffs/INDEX.yml) for the buff library.*
