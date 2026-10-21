---
name: object
description: Interactable things in the world — the atoms of adventure
allowed-tools:
  - read_file
  - write_file
tier: 1
protocol: SIMANTICS
tags: [moollm, object, interaction, game, sims]
related: [room, advertisement, inventory, buff]
adversary: abstraction
---

# Object

> *"Everything is an object. Objects have slots. Slots hold data OR behavior."*
> — Dave Ungar, Self: The Power of Simplicity

---

## What Is It?

An **Object** is anything you can interact with in the adventure world. Keys, lamps, chests, furniture, food, tools — all objects.

Objects are the **atoms** of the adventure. They:
- Have an identity (id, name, description)
- Advertise their actions (The Sims style)
- Contain state (lit, fuel, uses)
- Inherit from prototypes (Self style)

---

## The Sims Architecture

From Will Wright's SimAntics:

> *"The intelligence is in the objects, not the characters."*

Objects **advertise** what they can do:

```yaml
advertisements:
  LIGHT:
    description: "Light the lamp"
    score: 80
    guard: "lamp has fuel"
    effect: "Darkness retreats"
```

The character picks from what's advertised. No hardcoded behavior.

---

## Self-Style Prototypes

An object that is a variant of another says so and states only what differs:

```yaml
# examples/oil-lamp.yml
name: "Oil Lamp"
inherits: [brass-lantern.yml]   # simulate, methods and advertisements come from there
state:
  lit: false
  fuel: 60
```

A lookup reads the object, then each `inherits:` parent depth-first, then the `defaults.object`
of enclosing CONTAINER.yml files, then the prototype object. A map the object states replaces
the inherited map whole, so an object with its own `advertisements:` gets none of its parent's.

### The prototype object

[`OBJECT.yml`](OBJECT.yml) in this skill is the prototype object: `type: object`, empty
`tags`, `state`, `advertisements` and `methods`, and false `takeable`, `container`, `locked`,
`hidden`, `disabled`. It is the implied parent of every `OBJECT.yml` and of every embedded
object in an `objects:` collection. A plain object file (`lamp.yml`) has no implied parent; it
reaches the prototype through `inherits: [skills/object]` or gets kind defaults from a
container's `defaults.object`.

### Where objects live

| Size | Address | When |
|---|---|---|
| file | `pub/lamp.yml` | most objects |
| directory | `pub/cat-cave/OBJECT.yml` | an object with files or objects of its own |
| embedded | `garden/ROOM.yml#objects.bench` | small things that belong to one room |
| catalog entry | `aisle-e/PROTOTYPES.yml#prototypes.wine-rack` | many related prototypes in one file |

All four answer lookups the same way. An embedded object that grows moves into its own
directory without changing any lookup result. Worked objects are in [`examples/`](examples/).

---

## Object Properties

| Property | Purpose |
|----------|---------|
| `id` | Unique identifier |
| `name` | Display name |
| `type` | Category (item, furniture, tool) |
| `description` | What player sees |
| `examine` | Detailed look |
| `takeable` | Can be picked up |
| `container` | Can hold things |
| `contains` | What's inside |
| `hidden` | Invisible to players (prototypes, triggers, agents) |
| `state` | Mutable properties |
| `advertisements` | Available actions |
| `inherits` | Prototype chain |

---

## State

Objects have mutable state:

```yaml
state:
  lit: false
  fuel: 100
  uses_remaining: 3
```

State changes are tracked in YAML. The adventure is the save game.

---

## Simulate — Object Update Loops

**THE SIMS INSIGHT:** Objects manage their own simulation!

Every object can have a `simulate` property — a natural language description of what happens each turn. The compiler generates a closure that receives `world`.

```yaml
simulate: |
  if lit:
    consume_fuel(1)
    if fuel <= 0:
      extinguish()
      emit("The lamp sputters and dies!")
```

This compiles to:

```javascript
simulate_js: (world) => {
  if (world.object.state.lit) {
    world.consume_fuel(1);
    if (world.object.state.fuel <= 0) {
      world.extinguish();
      world.emit("The lamp sputters and dies!");
    }
  }
}
```

---

## Resilience — The SimCity Zone Pattern

**WILL WRIGHT INSIGHT:**

> *"SimCity zones are self-healing. If one tile burns but the center survives, the zone will eventually rebuild."*

Simulation functions should be:

### 1. Robust — Handle Missing Data

```javascript
// BAD: crashes if state is undefined
if (world.object.state.fuel > 0) { ... }

// GOOD: defensive access
if ((world.object.state?.fuel ?? 0) > 0) { ... }
```

### 2. Self-Initializing — Create Default State

```yaml
simulate: |
  first ensure state.lit exists (default false)
  ensure state.fuel exists (default 100)
  then proceed with normal simulation
```

The compiled code initializes missing state:

```javascript
simulate_js: (world) => {
  const state = world.object.state ??= {};
  state.lit ??= false;
  state.fuel ??= 100;
  // Now safe to proceed...
}
```

### 3. Self-Healing — Recover from Corruption

```yaml
simulate: |
  if fuel is somehow negative, reset to 0
  if lit but fuel is 0, extinguish (inconsistent state!)
  if broken flag is set but durability is full, clear broken
```

The compiled code heals invalid states:

```javascript
simulate_js: (world) => {
  const state = world.object.state;
  // Heal negative values
  state.fuel = Math.max(0, state.fuel);
  // Heal inconsistency
  if (state.lit && state.fuel <= 0) {
    state.lit = false;  // Self-heal
    world.emit("The lamp was somehow lit without fuel — fixed.");
  }
}
```

### Initial State

Initial values go in `state:`, on the object or on the prototype it inherits. `defaults:` is the
container's key for values that reach every object inside it; an object doesn't use it.

```yaml
name: "Brass Lantern"
state:
  lit: false
  fuel: 100
  durability: 100
simulate: |
  ensure state has lit, fuel and durability (the values above if missing)
  ...
```

---

## Methods — Named Behaviors

Objects can define **named methods** that `simulate` or advertisements can call. Natural language → compiled closures. **1:1 mapping!**

```yaml
methods:
  consume_fuel: "reduce fuel by amount, minimum 0"
  extinguish: "set lit to false, emit darkness event"
  ignite: "set lit to true if fuel > 0"
```

Compiles to:

```javascript
methods_js: {
  consume_fuel: (world, amount) => { 
    world.object.state.fuel = Math.max(0, world.object.state.fuel - amount); 
  },
  extinguish: (world) => { 
    world.object.state.lit = false; 
    world.emit('DARKNESS'); 
  },
  ignite: (world) => { 
    if (world.object.state.fuel > 0) world.object.state.lit = true; 
  }
}
```

### The Power of 1:1 Methods

- Method name in natural language = method name in JS/PY
- `consume_fuel(1)` in YAML → `world.consume_fuel(1)` in JS
- Methods compose — `extinguish()` can call other methods
- Advertisements can call methods in their `effect`

---

## The Complete Pattern

```
Object
├── state         (mutable data)
├── simulate      (per-turn update)
├── methods       (named behaviors)
└── advertisements (player actions)
```

Advertisements call methods. Simulate calls methods. Methods update state.

**Everything flows through compiled closures over `world`.**

---

## Advertisements (Actions)

Each advertisement can have:

```yaml
LIGHT:
  description: "Light the lamp"           # What it does
  score: 80                               # Base attractiveness
  score_if: "player is in dark room"      # When to boost
  guard: "lamp has fuel"                  # Can you do it?
  effect: "Lamp is now lit"               # What happens
```

Natural language fields (`score_if`, `guard`, `effect`) are compiled to JS/PY.

---

## Containers

Containers hold other objects:

```yaml
container: true
contains:
  - brass-key
  - old-map
capacity: 10
locked: true
```

---

## Examples

### Simple Item

```yaml
# examples/brass-key.yml
id: brass-key
name: "Brass Key"
emoji: "🔑"
description: "A heavy brass key."
takeable: true
```

### Lamp with State

```yaml
id: oil-lamp
name: "Oil Lamp"
emoji: "🪔"
state:
  lit: false
  fuel: 100
advertisements:
  LIGHT:
    guard: "fuel > 0 AND not lit"
    effect: "The lamp flickers to life."
```

### Locked Chest

```yaml
id: treasure-chest
name: "Treasure Chest"
container: true
locked: true
contains:
  - gold-coins
  - magic-ring
advertisements:
  UNLOCK:
    guard: "player has chest-key"
    effect: "The lock clicks open."
```

More in [`examples/`](examples/): a wooden chest, the brass lantern with `simulate` and
`methods`, and foods that define their own digestion (strong coffee, a spicy burrito, mystery
meat, grandma's cookies).

---

## Related Skills

- [advertisement](../advertisement/) — How objects announce actions
- [room](../room/) — Where objects live
- [buff](../buff/) — Effects objects can grant
- [prototype](../prototype/) — Inheritance system

---

## Protocol Symbol

```
SIMANTICS — The Sims behavioral architecture
```

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/object/](https://github.com/SimHacker/moollm/tree/main/skills/object)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
