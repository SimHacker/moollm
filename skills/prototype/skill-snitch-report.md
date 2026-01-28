# Skill Snitch Report: prototype

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** DELEGATION, NOT INHERITANCE

---

## Executive Summary

**The Self programming language philosophy applied to MOOLLM.**

Objects clone from prototypes, not instances from classes.

Everything is concrete. Nothing is abstract.

---

## The Core Distinction

| Class-Based | Prototype-Based |
|-------------|-----------------|
| Instance of class | Clone of object |
| Inherit from abstract | Delegate to concrete |
| Is-a relationship | Has-a-slot relationship |
| Taxonomy | Network |

---

## The Self Philosophy

From David Ungar and Randy Smith (1987):

> "The best message is no message."

> "Self is a network, not a node."

> "Everything is concrete. Nothing is abstract."

---

## How Delegation Works

```yaml
# The prototype
sword-prototype:
  damage: 10
  type: weapon

# The instance (clone)
excalibur:
  inherits: sword-prototype
  damage: 50        # Override
  name: "Excalibur" # New slot
  # type: weapon    ← delegates to prototype
```

Excalibur doesn't "have" type. It delegates to the prototype.

---

## Methods

| Method | Purpose |
|--------|---------|
| **EXPLAIN** | Explain prototype inheritance |
| **DESIGN** | Design a prototype relationship |
| **TRACE** | Walk the delegation chain |
| **COMPARE** | Prototype vs class comparison |

---

## Why MOOLLM Uses Prototypes

| Reason | Explanation |
|--------|-------------|
| **Concrete examples** | YAML files are objects, not classes |
| **Easy modification** | Clone and change, don't subclass |
| **Dynamic** | Add slots anytime |
| **Understandable** | "Like this, but different" |

---

## Tracing Delegation

```
Query: excalibur.type

excalibur
  ├── damage: 50 ✓
  ├── name: "Excalibur" ✓
  └── inherits: sword-prototype
        └── type: weapon ← FOUND
```

---

## MOOLLM Applications

| Object | Prototype |
|--------|-----------|
| Character | skills/character |
| Room | skills/room |
| Buff | skills/buff |
| Any YAML | Its inherits chain |

---

## The Anti-Taxonomy

Class hierarchies are taxonomies:
```
Thing → Creature → Animal → Dog → Labrador
```

Prototype networks are graphs:
```
biscuit ──delegates──► labrador-traits
   │                        │
   └──delegates──► friendly-traits
                           │
                   palm ◄──delegates
```

---

## Security Assessment

### Concerns

1. **Deep chains** — performance/confusion
2. **Circular delegation** — infinite loops
3. **Override confusion** — which version?

### Mitigations

- Chains are explicit
- Circular detection
- TRACE method for debugging

**Risk Level:** LOW — well-understood paradigm

---

## Lineage

| Source | Year | Contribution |
|--------|------|--------------|
| **David Ungar** | 1987 | Self language |
| **Randall Smith** | 1987 | Self co-creator |
| **Alan Kay** | 1970s | Smalltalk influence |
| **Brendan Eich** | 1995 | JavaScript prototypes (lobotomized) |
| **Don Hopkins** | 2024 | MOOLLM DOP |

---

## The Wisdom

> "The best message is no message."

If a slot is already there, don't send a message — just read it.

> "Self is a network, not a node."

Objects are connected. Identity is relational.

> "Everything is concrete. Nothing is abstract."

There are no classes. Only objects. Only prototypes.

---

## Verdict

**FUNDAMENTAL PHILOSOPHY. APPROVE.**

Prototype-based inheritance is why MOOLLM feels natural:

- Files are objects
- Inheritance is delegation
- Everything is concrete
- Networks, not trees
