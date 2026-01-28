# Skill Snitch Report: object

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE INTERACTABLE THING

---

## Executive Summary

**An interactable thing in the adventure world.**

Keys, lamps, chests, furniture — all objects.

Objects have TAGS for easy filtering and ADVERTISEMENTS for autonomous behavior.

---

## The Core Pattern

```yaml
object:
  id: lamp
  name: "Brass Lamp"
  tags: [light-source, takeable]
  state:
    lit: false
  methods:
    LIGHT: "Turn on the lamp"
    EXTINGUISH: "Turn off the lamp"
  advertisements:
    PROVIDE-LIGHT:
      score: 90
      guard: "darkness present"
      effect: "light the lamp"
```

---

## Schema

| Field | Required | Purpose |
|-------|----------|---------|
| id | ✓ | Unique identifier |
| name | ✓ | Display name |
| description | ✓ | What you see |
| tags | | Categories for filtering |
| state | | Dynamic state fields |
| methods | | Named behaviors |
| simulate | | Per-turn update |
| advertisements | | Autonomous behaviors |

---

## Common Tags

| Tag | Meaning |
|-----|---------|
| weapon | Combat item |
| food | Edible |
| drink | Potable |
| container | Can hold things |
| light-source | Illumination |
| tool | Utility |
| treasure | Valuable |
| readable | Books, scrolls |
| wearable | Clothing, armor |
| consumable | Used up |
| magical | Special properties |
| fragile | Can break |
| heavy | Hard to carry |
| key | Opens something |

---

## Compiled Fields

Natural language compiles to closures:

| Source | Target |
|--------|--------|
| `simulate:` | `simulate_js`, `simulate_py` |
| `methods.*:` | `methods_js.*`, `methods_py.*` |
| `advertisements.*.guard:` | `guard_js`, `guard_py` |
| `advertisements.*.score_if:` | `score_if_js`, `score_if_py` |
| `advertisements.*.effect:` | `effect_js`, `effect_py` |

---

## Advertisements

Objects advertise actions they can perform:

```yaml
advertisements:
  PROVIDE-LIGHT:
    description: "Light up the darkness"
    score: 90
    guard: "room.dark and not self.state.lit"
    effect: "self.state.lit = true"
```

Autonomous agents scan advertisements and pick the best one.

---

## Simulation Loop

Objects can update each turn:

```yaml
simulate: |
  If lit for more than 10 turns, run out of oil.
  Reduce oil by 1 per turn when lit.
```

Compiles to closure, runs each tick.

---

## Hidden Objects

`hidden: true` hides objects from LOOK:

- Prototypes (not in world, just templates)
- Agents (invisible actors)
- Tasks (meta-objects)

---

## Container Objects

Objects can contain other objects:

```yaml
container: true
capacity: 10
contains:
  - gold-coin
  - silver-key
locked: true
```

---

## Security Assessment

### Concerns

1. **Method execution** — natural language compiles to code
2. **Effect execution** — advertisements change state
3. **Simulation loop** — runs every turn

### Mitigations

- Expressions compile to sandboxed closures
- Effects bounded by object scope
- Simulation auditable

**Risk Level:** MEDIUM — compiled code execution

---

## Relationship to Other Primitives

```
Room
 └── contains
      └── Object
           ├── state
           ├── methods
           ├── advertisements
           └── may contain: Object
```

---

## Verdict

**THE FUNDAMENTAL INTERACTABLE. APPROVE.**

Objects are what you interact with. Everything that isn't a room or a character is an object.

Tags filter them. Methods define actions. Advertisements enable autonomy.
