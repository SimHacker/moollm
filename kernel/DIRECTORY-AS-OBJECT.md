# Selfish COM: Directory-as-Object

**The insight:** Directories are objects. Files are interfaces. The filesystem IS the object graph.

## Why Care?

- **Human-readable** — YAML files, not binary blobs
- **LLM-friendly** — AI can read and write your "code"
- **Git-friendly** — merge conflicts are manageable text
- **Hot-reloadable** — edit files, see changes
- **Zero ceremony** — no build step to add an interface

## The Pattern

```
don-hopkins/              ← Object (identity = path)
├── CHARACTER.yml         ← queryInterface('character')
├── ROOM.yml              ← queryInterface('room')
├── portrait.png          ← resource
└── memories/             ← child object
```

That's it. The directory IS the object. Each `.yml` file IS an interface.

**COM parallel:**
- `pUnk->QueryInterface(IID_IRoom, &pRoom)` → check if `ROOM.yml` exists
- `IUnknown` → the directory path itself
- `E_NOINTERFACE` → file not found

**Self parallel:**
- No classes, just objects (directories)
- Prototypal inheritance via `parents:` arrays in YAML
- Slots = file contents

## Two Object Forms

**Directory objects** — multiple interfaces:
```
pub/
├── ROOM.yml        ← room interface
├── MENU.yml        ← menu interface  
└── bar/            ← child object
```

**File objects** — single interface:
```
characters/
├── bob.yml         ← one object, one interface
└── alice.yml       ← one object, one interface
```

## QueryInterface

```javascript
queryInterface('don-hopkins/', 'room')      // → don-hopkins/ROOM.yml
queryInterface('don-hopkins/', 'character') // → don-hopkins/CHARACTER.yml
queryInterface('don-hopkins/', null)        // → don-hopkins/ (identity)
queryInterface('bob.yml', 'character')      // → bob.yml (file IS interface)
```

No pointer adjustment. No vtables. Just file lookup.

## Inheritance (Self-Style)

```yaml
# don-hopkins/CHARACTER.yml
parents:
  - characters/abstract/notorious-hacker
  - characters/abstract/pie-menu-freak
name: Don Hopkins
tags: [hacker, artist]
```

The compiler flattens this at build time. Runtime gets simple property lookup.

## Compiled Closures

Natural language compiles to JavaScript:

```yaml
# BEFORE (human writes)
unlock_condition: Player has the red key and hasn't triggered the alarm.

# AFTER (LLM compiles, both visible)
unlock_condition: Player has the red key and hasn't triggered the alarm.
unlock_condition_js: return subject?.hasItem('red-key') && !world.flags.alarm_triggered
```

Body-only closures. Engine wraps with `(world, subject, verb, object) => { ... }`.

## What We Skip

All the C++ COM complexity:
- No pointer adjustment or thunks
- No reference counting (filesystem handles lifetime)
- No GUIDs (human-readable interface names)
- No registry (filesystem IS the registry)
- No binary formats (YAML text files)

## The Stack

```
YAML source files  →  Python compiler + LLM  →  JSON trees  →  JS runtime
   (human edits)        (flattens, compiles)    (fast load)    (executes)
```

The directory tree is source of truth. JSON is compiled artifact.

## Prior Art

This builds on:
- **Self** (Ungar & Smith) — eliminated classes, just objects
- **COM** (Microsoft) — interface-based design  
- **Densmore-Rosenthal Patent** (1991) — OOP in Unix filesystem

The patent describes directories as objects, files as methods, 35 years before us.

---

*COM gave us interfaces. Self eliminated classes. Densmore showed us the filesystem IS the object graph. Selfish COM combines all three — filesystem-native, human-readable, LLM-friendly.*
