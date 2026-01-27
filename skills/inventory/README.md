# Inventory

> **"Carry pointers or values. Set them down, they become real."**

The universal protocol for carrying, storing, and transferring objects.

## Quick Start

```yaml
# In any container (character, bag, chest, room...)
inventory:
  refs:
    - pub/bar/brass-lantern.yml           # Lightweight pointer
    - seating.yml#bar.stool-1             # Point into a file
    - characters/README.md#doctor-no      # Even markdown headings
  objects:
    - { id: cookie, name: "Cookie", weight: 0.1 }  # Deep copy
  fungibles:
    - { proto: economy/gold.yml, count: 500 }      # Integer stack
    - { proto: economy/moolah.yml, count: 3.99 }   # Fractional! Why not?
```

## The Core Insight

**Carry two kinds of things: POINTERS and VALUES.**

- **Pointers** — lightweight paths to things elsewhere (weight: 0)
- **Values** — text, numbers, arrays, objects, entire subtrees

When you DROP either, it gets **boxed** into a YAML file with its own existence and local storage, inheriting from the object pointed to.

| What You Carry | Weight | What Happens on Drop |
|----------------|--------|----------------------|
| **Pointer** | 0 | Gets BOXED into a new file |
| **Value** | varies | Inserted or becomes file |
| **Object** | weight | File moves or copies |
| **Fungible** | per-item | Count transfers |

## Commands

| Command | What It Does |
|---------|--------------|
| `TAKE brass-lantern` | Smart pickup (usually ref) |
| `TAKE REF TO statue` | Explicitly take pointer |
| `TAKE VALUE OF cookie` | Take deep copy |
| `DROP item` | Smart drop |
| `DROP item AS INSTANCE` | Create new inheriting file |
| `DROP item AS COPY` | Copy actual file |
| `DROP item AS MOVE` | Move actual file |
| `BEAM piano TO concert-hall` | Teleport heavy object |
| `INVENTORY` | List what you have |

## Structural Editing

The same pointer syntax enables **syntax-independent YAML/JSON editing**:

| Command | What It Does |
|---------|--------------|
| `PEEK file#key.subkey` | Read value |
| `POKE file#key = value` | Write value |
| `SNIP file#subtree` | Extract (leaves hole) |
| `PULL file#subtree TO new.yml` | Extract to file |
| `SPLICE value INTO file#list` | Insert into list |
| `SET file#key = value` | Create/overwrite |
| `DELETE file#key` | Remove key |
| `MOVE file#src TO file2#dst` | Relocate subtree |

**Works on YAML and JSON identically.** Pointers address structure, not syntax.

## Boxing: When Pointers Become Instances

**Boxing** (almost but not quite entirely unlike Java boxing) — instantiating a pointer into a real file with identity.

```
Don has: ref → street/acme-catalog.yml

> DROP catalog AS INSTANCE IN kitchen

Creates: kitchen/acme-catalog-001.yml
  inherits: street/acme-catalog.yml
  instantiated_by: don
  instantiated_at: 2026-01-23T14:00:00Z
```

The catalog is now **instantiated** — a real file that inherits from the prototype. It can have local state, annotations, condition — anything that diverges from its parent.

**Once boxed, always boxed.** Pick up a boxed item and all its properties travel with it. But with some sleight of hnd you can pick up a reference to its prototype, or its prototype's prototype! Just say what you want.

## Reference Pointer Syntax

References can point ANYWHERE:

| Syntax | Example |
|--------|---------|
| File | `pub/cookie-jar.yml` |
| Section | `pub/cookie-jar.yml#cookie` |
| Nested | `seating.yml#bar.stool-1` |
| Markdown | `README.md#doctor-no` |
| JSON | `config.json#/settings/defaults` |
| Line | `engine.cpp:142` |
| Range | `engine.cpp:10-30` |

**Unified addressing:** This syntax is shared across inventory, location, postal, and structural editing. Mail a letter to a function. Stand on a JSON key. Same address space, everywhere.

## Universal Application

Inventory works for ANY container:

- **Characters** — Palm's backpack
- **Bags** — Bag of holding
- **Chests** — Treasure chest
- **Rooms** — Objects in the pub
- **Vehicles** — Cargo hold
- **Artifacts** — Ring with stored spell

## Code as Space (Bidirectional Pointers)

**The pointer syntax goes both ways.** Not just "what you carry" but "where you ARE."

An object's `location:` field uses the same pointer syntax. Characters can exist *inside* source code:

```yaml
# Alice standing on a TypeScript function
name: Alice
location: src/lib/utils.ts#fetchData
note: "Reviewing with the hacking party"

# Bug marker at a specific line range
name: Bug Marker
location: src/auth/login.ts:45-67
```

**The codebase becomes a dungeon.** Files are rooms. Functions are objects. Line ranges are spots. A hacking party can stand around a function and discuss it.

| Use Case | Location Pointer |
|----------|------------------|
| **Code review** | Stand on functions, debate |
| **Bug hunting** | Place markers at suspicious lines |
| **Architecture tour** | Walk through modules as rooms |
| **Pair programming** | Multiple characters at same location |

## Files

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Full protocol documentation |
| [CARD.yml](CARD.yml) | Machine-readable interface |
| [INVENTORY.yml.tmpl](INVENTORY.yml.tmpl) | Template for standalone inventory |

## Related Skills

| Skill | Relationship |
|-------|--------------|
| [character](../character/) | Characters have inventories |
| [object](../object/) | Objects can be items or containers |
| [room](../room/) | Rooms implicitly contain objects |
| [prototype](../prototype/) | References point to prototypes |
| [postal](../postal/) | Mail uses inventory transfer |
| [economy](../economy/) | Currency as fungible stacks |

## Lineage

- **The Sims** — Routing slots, object advertisements
- **Factorio** — Logistic inventory, fungible stacks  
- **Text adventures** — TAKE, DROP, INVENTORY
- **Self language** — Prototype references
- **Unix** — Pointers vs copies

---

*"Pointers and values — carry them light, drop them real."*
