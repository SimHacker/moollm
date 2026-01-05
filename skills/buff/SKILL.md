---
name: buff
description: Temporary effects system — curses are just shitty buffs
allowed-tools:
  - file_read
  - file_write
tier: 1
protocol: BUFF-AS-MODIFIER
tags: [effects, curses, stats, game]
related: [character, time, needs, persona, cat]
---

# Buff

> *"All effects are buffs. Some are just shitty."*

Buffs modify stats, abilities, or behavior. They have durations, can stack, and come from various sources. **Curses are just negative buffs** — no separate system.

## Structure

```yaml
buff:
  name: "Caffeinated"
  source: "Espresso"
  effect: { energy: +2, focus: +1 }
  duration: 5  # simulation turns
  stacks: false
```

| Field | Purpose |
|-------|---------|
| `name` | Display name |
| `source` | What granted this buff |
| `effect` | Stat mods OR semantic prompt |
| `duration` | How long it lasts |
| `stacks` | Can multiple instances exist? |
| `max_stacks` | If stacking, limit |
| `decay` | How it ends (time, action, condition) |

## Buff Types

### Numeric
Traditional stat modifiers:
```yaml
buff:
  name: "Caffeinated"
  effect: { energy: +2, focus: +1 }
  duration: 5
```

### Semantic
Arbitrary effect prompts interpreted by the LLM — not predefined stats, just vibes:

- "feeling lucky"
- "cats seem to like you today"
- "slightly cursed"
- "radiating calm energy"
- "shadows feel watchful"

**How it works:**
```
Buff: "cats seem to like you today"
Action: PAT TERPIE
LLM: Gives bonus, narrates extra warmth
```

### Mixed
Combine numeric and semantic:
```yaml
buff:
  name: "Terpie's Blessing"
  effect:
    calm: +2
    vibe: "cats trust you more"
  duration: "a while"
```

## Sources

| Source | Example |
|--------|---------|
| Interactions | Petting a cat grants joy |
| Consumables | Coffee grants energy |
| Locations | Being in pub grants comfort |
| Items | Lit lamp grants grue immunity |
| Relationships | High friendship grants trust |
| Personas | Wearing persona grants themed buffs |

## Stacking

- **Same source:** Doesn't stack — refresh duration instead
- **Different sources:** Stack additively up to category limit

### Category Limits
```yaml
terpene_effects: 3
charm_effects: 5
consumable_effects: 4
negative_effects: 3  # 3+ same negative = LEGENDARY
```

### Synergies
Some buffs COMBINE into stronger effects:
- Myr + Lily = "Sedation Stack"
- Lemon + Pine = "Focus Boost"
- All 8 kittens = "ENTOURAGE EFFECT" (legendary)

## Negative Buffs (Curses)

Curses are just shitty buffs. Same structure, negative effects.

```yaml
buff:
  name: "Scratched"
  source: "Failed BELLY RUB"
  effect: { hp: -1, visible_marks: true }
  duration: "Until healed"
```

### Persistent Curses
Long-term negative buffs with lift conditions:
```yaml
buff:
  name: "Curse of Darkness"
  effect: { lamp_efficiency: -25% }
  duration: conditional
  lift_condition: "Light 3 dark places"
  reward_on_lift: "LIGHT-BEARER title"
```

## Duration Types

| Type | Example |
|------|---------|
| Turns | `duration: 4` |
| Conditional | `duration: until you eat` |
| While present | `duration: while in pub` |
| Permanent | `duration: forever` |
| Natural language | `duration: a few minutes` |
| Probabilistic | `duration: 25% fade chance per turn` |

### Natural Language Durations

We're not tracking real time — the LLM interprets and makes its best guess:

- "forever"
- "5 minutes"
- "a day"
- "until sunset"
- "randomly 50%"
- "a while"
- "briefly"
- "until you forget"

See [time/](../time/) for full natural duration examples.

### Decay

When LLM judges turn(s) have passed:
1. Decrement duration on timed buffs
2. Remove buffs that hit 0
3. Apply new buffs from current turn

## Commands

| Command | Effect |
|---------|--------|
| `BUFFS` or `STATUS` | List active buffs with remaining duration |
| `EXAMINE [buff]` | Full details of buff source, effect, duration |
