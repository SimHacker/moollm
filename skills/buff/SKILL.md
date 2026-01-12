---
name: buff
description: Temporary effects system — curses are just shitty buffs
allowed-tools:
  - read_file
  - write_file
tier: 1
protocol: BUFF-AS-MODIFIER
related: [simulation, time, needs, character, cat, dog, persona, yaml-jazz]
tags: [moollm, effects, curses, stats, game, modifiers]
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

## Effective Derived Values: Flags Edition

This is the **effective derived values protocol** for booleans.

| Type | Base | Modifiers | Effective |
|------|------|-----------|-----------|
| **Numeric** | `energy: 5` | buff `+2` | `effective_energy: 7` |
| **Boolean** | `in_darkness: false` | room.lit=false, has_lamp=false | `effective_in_darkness: true` |

Same pattern:
- **Numeric:** base + sum(modifiers) = effective
- **Boolean:** base OR any(conditions) = effective flag

### Push / Pull / Latch

The LLM can handle any combination:

| Mode | Pattern | Example |
|------|---------|---------|
| **Pull** | Compute on demand | `in_darkness` derived from lamp + room state |
| **Push** | Source sets flag | Buff explicitly sets `urgent_situation: true` |
| **Latch** | Stays until cleared | `has_visited_room_a: true` persists |

```yaml
# PULL — derived on demand, not stored
in_darkness: (room.lit == false) AND (has_lamp == false)

# PUSH — buff explicitly sets
buff:
  sets_flags: [urgent_situation]

# LATCH — persists in state until cleared
player:
  visited_rooms: [room-a, room-b]  # grows, never shrinks
```

Traditional reactive systems pick one mode. The LLM does all three simultaneously — it sees the whole context and figures out which pattern applies.

### Tweening and Animation

Values don't have to snap — they can interpolate over time:

| Type | Instant | Tweened |
|------|---------|---------|
| **Numeric** | `energy: 5 → 7` | `energy: 5 → 7 over 3 turns` |
| **Boolean** | `lit: false → true` | `lit: fading in over 2 turns` |
| **Position** | `room-a → room-b` | `walking through hallway` |

```yaml
buff:
  name: "Warming Up"
  effect: { warmth: +3 }
  tween: ease-in    # Gradual increase
  duration: 5

animation:
  entering_room:
    from: hallway
    to: pub
    frames: [approaching, at_door, stepping_in, arrived]
```

The LLM narrates intermediate states. "You feel yourself warming up..." not just "You are warm now."

### Velocity

Any reactive variable can have a rate of change:

```yaml
energy:
  value: 5
  velocity: -1      # Draining 1 per turn
  
trust:
  value: 45
  velocity: +3      # Building rapport
  
mood:
  value: "content"
  velocity: "improving"  # Semantic velocity works too
```

| Variable | Value | Velocity | Meaning |
|----------|-------|----------|---------|
| `energy` | 5 | -1 | Tired and getting worse |
| `trust` | 45 | +3 | Relationship strengthening |
| `position` | room-a | north | Moving northward |
| `mood` | anxious | calming | Settling down |

The LLM reads velocity to predict and narrate: *"You're running low on energy and fading fast..."* vs *"Low energy but recovering."*

### Physics Simulation

Extend to full 2D/3D cartoon physics:

```yaml
thrown_ball:
  position: [5, 3]
  velocity: [2, 4]       # Moving up-right
  acceleration: [0, -1]  # Gravity pulling down
  
bouncing:
  elasticity: 0.8        # Loses 20% on bounce
  
cartoon_physics:
  hang_time: true        # Pause at apex
  squash_stretch: true   # Deform on impact
  delayed_fall: true     # Look down first, then fall
```

The LLM narrates physics with cartoon timing:

> *The ball arcs gracefully upward... hangs for a moment at the peak... 
> then plummets, SQUASHING flat against the floor before bouncing back 
> slightly less enthusiastically.*

Works for:
- Thrown objects (ball, inventory items)
- Character movement (jumping, falling, knockback)
- Environmental effects (swinging doors, rolling boulders)
- Looney Tunes logic (run off cliff, pause, look down, THEN fall)
- Temperature cooling or warming (ice cream melting, water freezing)

## Commands

| Command | Effect |
|---------|--------|
| `BUFFS` or `STATUS` | List active buffs with remaining duration |
| `EXAMINE [buff]` | Full details of buff source, effect, duration |
