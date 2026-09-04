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

---

## What this actually is

The full definition, stated once:

> **A buff is a constraint — an expression that inherits from a parent and then
> overrides, procedurally modifies and combines with other dependencies, and
> caches. With a tick function and an expiration date.**

Six components, each with prior art worth reading, and then two that are ours:

| Component | What it means here | Where it was solved before |
|---|---|---|
| **Constraint** | a declared relation, not an imperative write | Garnet/Amulet constraints; Blender object constraints with an `influence` weight |
| **Expression** | the value is a formula over other slots | Blender drivers; spreadsheet cells; OpenLaszlo constraint expressions |
| **Inherit then override** | the buff delegates to a parent prototype and shadows selected slots | Self delegation; Garnet KR prototype-instance; CSS inheritance |
| **Procedurally modify and combine** | many contributions fold into one value in a defined order | Blender's modifier stack; GAS's aggregator equation; the CSS cascade |
| **Cache** | the folded result is stored so nobody refolds it per read | Blender's depsgraph with evaluated copies; spreadsheet dirty-marking; Self's maps and inline caches |
| **Dependencies** | the cache knows what it was computed from | any dependency graph worth the name |
| **Tick function** | it advances under its own power, without being read | *not* in constraint systems — this is the simulation half |
| **Expiration date** | the binding dies on a timer, event, or predicate | *not* in constraint systems — this is the buff half |

**The tick function and the expiration date** are the whole difference — the two
rows with no prior art in the constraint column. A constraint system is reactive: it
recomputes when something it depends on changes, and otherwise sits still
forever. A buff **acts when nothing has happened** — the timer runs down, the
poison ticks, the mood decays — and then it **stops existing**. Constraint
graphs have no notion of a relation that ages out.

So: buffs are constraints that got a clock and a mortality.

## Reconciling "cache" with "never cached"

[GAME-PIECES.md](../../designs/GAME-PIECES.md) is emphatic in the other
direction: the host's menu is *"derived fresh, never cached,"* castling rights
as a stored flag is a *"cached-flag bug factory,"* and the troll flag failed
because the world was supposed to remember to clear it.

Both rules are correct because they are about different things:

- **Never cache authoritative state.** A flag that says "this capability is
  gone" and depends on some other system remembering to clear it is the bug.
  There is no owner, no invalidation, and no way to notice it went stale.
- **Always cache derived values — with invalidation.** Refolding every modifier
  on every read is not virtue, it is waste. The rule that matters is not
  *don't cache*, it is **don't cache without a dependency graph that knows how
  to dirty you.**

`foo_effective` *is* a cache. This document has been describing a cache from the
first paragraph. Its invalidation policy just happens to be the crudest one
available: throw everything away and refold from base, once per tick.

That is a defensible default — it is trivially correct, and it is why the reset
phase exists — but it is one point on a spectrum:

| Policy | Invalidate when | Cost | Used by |
|---|---|---|---|
| **Recompute-per-tick** | always, unconditionally | O(all buffs) every tick | this document, today |
| **Dirty-marking / depsgraph** | a dependency changed | O(affected subgraph) | Blender depsgraph; build systems |
| **Lazy pull** | on read, if any dependency is dirty | O(what someone actually looked at) | Garnet constraints |
| **Eager push** | immediately on write, propagating forward | O(downstream) at write time | OpenLaszlo |

The pull-versus-push tradeoff is already written up for the prototype system in
[GARNET-AMULET-PROTOTYPE-SYSTEM.md](../../designs/GARNET-AMULET-PROTOTYPE-SYSTEM.md)
("Pull vs push (Garnet vs OpenLaszlo)") and it applies here unchanged.

Which to use is a scale question, and the honest answer for now is that
recompute-per-tick is right until a profile says otherwise: a few dozen buffs on
a few dozen characters is nothing, and the crude policy cannot be wrong. The
moment buffs are attached to materials or regions rather than characters — the
Korz reading in [SELF-KORZ.md](SELF-KORZ.md) — the affected set stops being
"one character's stats" and dirty-marking starts to matter.

A **soft-tier** buff — a prose guard an LLM judges, per SELF-KORZ.md §4 — is
expensive to evaluate and has no mechanical dependency set, so neither
dirty-marking nor lazy pull can tell when it went stale. Two answers, and they
compose:

- **Time-boxed trust in a cached judgement.** "Re-judge this every N ticks, or
  when the scene changes." A third kind of invalidation, and the only one
  available while the guard is still prose.
- **Compile it, which removes the problem rather than managing it.** A guard
  compiled to a `guard_js` snippet has an ordinary mechanical dependency set,
  costs a function call, and can be dirty-marked like anything else. The prose
  stays as the specification and the snippet **deopts back to it** when it meets
  a case it mishandles. See
  [BUFF-IN-TIME-COMPILER.md](BUFF-IN-TIME-COMPILER.md).

So the cost of a soft guard is a *warmup* cost, not a per-tick cost — which is
the same claim a JIT makes, and it is why the caching spectrum above bottoms out
in compilation rather than in a cleverer invalidation policy.

## See also

- [SELF-KORZ.md](SELF-KORZ.md) — Self → Korz → Korz′, and the lifetime ladder
- [BUFF-IN-TIME-COMPILER.md](BUFF-IN-TIME-COMPILER.md) — English → `_js`/`_py` snippets; the bottom of the caching spectrum
- [CONSEQUENCE-LOOP.md](CONSEQUENCE-LOOP.md) — Blender's modifier stack, constraints with influence, drivers, and the operator half
- [GAME-PIECES.md](../../designs/GAME-PIECES.md) — the never-cache discipline and why it means what it means
- [GARNET-AMULET-PROTOTYPE-SYSTEM.md](../../designs/GARNET-AMULET-PROTOTYPE-SYSTEM.md) — constraints across parallel trees, pull vs push
