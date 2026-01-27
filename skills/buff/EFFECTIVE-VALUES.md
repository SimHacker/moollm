# Effective Values Protocol

> *"The base value is truth. The effective value is reality."*
> — The Gezelligheid Grotto Design Principles

---

## The Pattern

Every modifiable property has TWO values:

| Property | Purpose |
|----------|---------|
| `foo` | **Base value** — Persistent, ground truth |
| `foo_effective` | **Effective value** — Recalculated each tick |

```yaml
object:
  id: sword-of-flames
  state:
    # Base values (persistent)
    damage: 10
    speed: 5
    
    # Effective values (recalculated each tick)
    damage_effective: null  # Set to 10 + buff mods each tick
    speed_effective: null   # Set to 5 + buff mods each tick
```

---

## The Tick Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                     SIMULATION TICK                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. RESET PHASE (Early)                                      │
│     foo_effective = foo  ← Reset to base value              │
│                                                              │
│  2. BUFF PHASE                                               │
│     Each active buff modifies foo_effective                 │
│     foo_effective += buff.modifier                          │
│                                                              │
│  3. SIMULATE PHASE                                           │
│     Objects run their simulate(), using foo_effective       │
│     Can also modify foo_effective                           │
│                                                              │
│  4. ACTION PHASE                                             │
│     Player actions use foo_effective for calculations       │
│                                                              │
│  5. DISPLAY PHASE                                            │
│     UI shows foo_effective (with optional base comparison)  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Why This Matters

### 1. Buffs Are Temporary

```yaml
# Buff: "Strength Potion"
buff:
  id: strength-potion
  effect: "damage_effective += 5"
  duration: 10  # Turns
  
# When buff expires, damage_effective automatically
# resets to base 'damage' on next tick.
# No cleanup code needed!
```

### 2. Buffs Stack Naturally

```yaml
# Turn 1: damage = 10
# Tick starts: damage_effective = 10
# Strength Potion: damage_effective += 5 → 15
# Rage Buff: damage_effective *= 1.5 → 22
# Final: damage_effective = 22

# If Strength Potion expires:
# Tick starts: damage_effective = 10
# Rage Buff: damage_effective *= 1.5 → 15
# Final: damage_effective = 15
```

### 3. No State Corruption

```yaml
# BAD: Modifying base value
damage = damage + buff_bonus  # Buff expires, but damage is now wrong!

# GOOD: Modifying effective value
damage_effective = damage + buff_bonus  # Resets cleanly each tick
```

### 4. Animation & Tweening

```yaml
object:
  state:
    x: 100           # Base position (target)
    y: 200
    x_effective: 95  # Current animated position
    y_effective: 195
    
simulate: |
  # Tween effective toward base
  x_effective = lerp(x_effective, x, 0.1)
  y_effective = lerp(y_effective, y, 0.1)
```

---

## Compiler Support

The compiler knows about this pattern:

```yaml
# In object definition
state:
  damage: 10
  # Compiler automatically generates:
  # damage_effective: null

# In buff definition  
effect: "damage_effective += 5"
# Compiler generates:
effect_js: (world) => {
  world.object.state.damage_effective += 5;
}
```

### The `_effective` Convention

Any property `foo` can have a `foo_effective` counterpart:

```yaml
state:
  # Combat stats
  damage: 10
  armor: 5
  speed: 3
  
  # Resource stats
  health: 100
  mana: 50
  stamina: 75
  
  # All automatically get _effective versions
  # damage_effective, armor_effective, speed_effective, etc.
```

---

## World Functions

The runtime provides helpers:

```javascript
// Reset all effective values to base
world.resetEffective(obj);

// Get effective value (or base if not set)
world.getEffective(obj, 'damage');  // Returns damage_effective or damage

// Modify effective value
world.modifyEffective(obj, 'damage', 5);  // Adds 5
world.multiplyEffective(obj, 'damage', 1.5);  // Multiplies by 1.5
```

### Python Equivalent

```python
world.reset_effective(obj)
world.get_effective(obj, 'damage')
world.modify_effective(obj, 'damage', 5)
world.multiply_effective(obj, 'damage', 1.5)
```

---

## Buff Template Update

```yaml
# BUFF.yml.tmpl (updated)
buff:
  id: "{{buff_id}}"
  name: "{{name}}"
  
  # What this buff modifies
  modifies:
    - property: damage_effective
      operation: add        # add, multiply, set, min, max
      value: 5
      
    - property: speed_effective
      operation: multiply
      value: 1.2
      
  # Or as natural language (compiled)
  effect: "damage_effective += 5, speed_effective *= 1.2"
  effect_js: null  # Compiled
  effect_py: null  # Compiled
```

---

## Object Simulation with Effective Values

```yaml
object:
  id: magic-sword
  
  state:
    damage: 10
    glow: 0
    charge: 100
    
  simulate: |
    # Early tick: damage_effective is already reset to damage
    
    # Environment effects
    if world.room.is_dark:
      glow_effective += 2  # Glows brighter in dark
      
    # Self-modification based on charge
    if charge > 50:
      damage_effective += 3  # Bonus damage when charged
      
    # Consume charge
    if world.object.state.damage_effective > damage:
      charge -= 1  # Only drain if actually buffed
```

---

## Display in UI

The UI can show both values:

```
┌─────────────────────────────────┐
│  ⚔️ Magic Sword                 │
│                                 │
│  Damage: 10 → 18 (+8)          │
│          ↑      ↑    ↑          │
│         base  eff  buff         │
│                                 │
│  Speed: 5 → 6 (+1)             │
│                                 │
│  Active Buffs:                  │
│  • Strength Potion (+5 dmg)     │
│  • Haste Ring (+1 spd)          │
│  • Charged Sword (+3 dmg)       │
└─────────────────────────────────┘
```

---

## Animation Example

```yaml
object:
  id: floating-orb
  
  state:
    # Base (target) position
    x: 200
    y: 150
    
    # Animated position (effective)
    x_effective: 200
    y_effective: 150
    
    # Animation parameters
    float_offset: 0
    float_speed: 0.1
    
  simulate: |
    # Floating animation
    float_offset += float_speed
    y_effective = y + sin(float_offset) * 10
    
    # If target changes, tween toward it
    x_effective = lerp(x_effective, x, 0.15)
    y_effective = lerp(y_effective, y, 0.15) + sin(float_offset) * 10
```

---

## Modifier Order

Buffs apply in order by priority:

```yaml
buff:
  id: base-buff
  priority: 100  # Lower = earlier
  effect: "damage_effective += 5"
  
buff:
  id: multiplier-buff
  priority: 200  # After base additions
  effect: "damage_effective *= 1.5"
```

**Order matters:**
- Add 5 then multiply by 1.5: (10 + 5) × 1.5 = 22.5
- Multiply by 1.5 then add 5: (10 × 1.5) + 5 = 20

---

## Self-Healing Effective Values

```javascript
// In reset phase, heal any missing effective values
world.resetEffective = (obj) => {
  const state = obj.state || {};
  
  for (const key of Object.keys(state)) {
    if (!key.endsWith('_effective')) {
      const effectiveKey = `${key}_effective`;
      // Reset to base value each tick
      state[effectiveKey] = state[key];
    }
  }
};
```

---

## Protocol Symbol

```
EFFECTIVE-VALUES — Base is truth, effective is reality
```
