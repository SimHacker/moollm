# Selfish COM: Directory-as-Object

**The insight:** Directories are objects. Files are interfaces. The filesystem IS the object graph.

## Why Care?

- **Human-readable** — YAML files, not binary blobs
- **LLM-friendly** — AI can read and write your "code"
- **Git-friendly** — merge conflicts are manageable text
- **Hot-reloadable** — edit files, see changes
- **Zero ceremony** — no build step to add an interface

## The Pattern

**Real example:** [don-hopkins/](../examples/adventure-4/characters/real-people/don-hopkins/)

```
don-hopkins/              ← Object (identity = path)
├── CHARACTER.yml         ← queryInterface('character')
├── ROOM.yml              ← queryInterface('room')
├── portrait.png          ← resource
└── memories/             ← child object
```

That's it. The directory IS the object. Each `.yml` file IS an interface.

**See it at scale:** [96 ROOM.yml files](../examples/adventure-4/) across nested directories, all following this pattern.

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

**Implementation:** [`compileJs()` at engine.js:181](../skills/adventure/engine.js#L181), [`resolveText()` at engine.js:3083](../skills/adventure/engine.js#L3083)

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

**Live code:**
- Source: [adventure-4/](../examples/adventure-4/) — 96 rooms, 50+ characters
- Compiler: [compile.py](../skills/adventure/compile.py)
- Runtime: [engine.js](../skills/adventure/engine.js) (4200 lines)

## Prior Art: The Densmore-Rosenthal Patent

**This isn't a new idea.** Owen Densmore and David Rosenthal proved it works in 1991.

**[US Patent 5187786A](https://patents.google.com/patent/US5187786A/en)** — *"Method and apparatus for implementing a class hierarchy of objects in a hierarchical file system"* (Sun Microsystems, filed 1991-04-05)

The patent describes **exactly this architecture**:
- Directories represent classes and instances
- Files within directories contain methods (shell scripts)
- PATH files encode inheritance chains
- Message sending via shell: `SEND aF001 methodA args`

**Owen Densmore** also created `object.ps` for NeWS — OOP in PostScript using dictionaries as objects. The same pattern: data structures ARE the objects, the interpreter IS the runtime.

**Tom Stambaugh** (C2 Wiki) on the origin:
> *"Owen and I discussed his 'crazy' idea at a poolside table at the now-demolished Hyatt Palo Alto, on El Camino. I told him that it made sense to me, we scribbled furiously on napkins..."*

**John Warnock's vision** (as recalled by Densmore):
> *"PostScript is a linguistic 'mother board', which has 'slots' for several 'cards'. The first card we built was a graphics card. We're considering other cards."*

This "pluggable slots" concept maps directly to our interface files.

### The Lineage

| Year | Innovation | Contribution |
|------|------------|--------------|
| 1986 | **[Self](https://selflanguage.org/)** (Ungar & Smith) | Eliminated classes — just objects |
| 1986 | **NeWS object.ps** (Densmore) | OOP in PostScript dictionaries |
| 1991 | **[Densmore-Rosenthal Patent](https://patents.google.com/patent/US5187786A/en)** | OOP in Unix filesystem — **proof it works** |
| 1993 | **[COM](https://learn.microsoft.com/en-us/windows/win32/com/component-object-model--com--portal)** (Microsoft) | Interface-based design |
| 1993 | **OLE / IDispatch** (Microsoft) | Late binding, automation |
| 2026 | **Selfish COM** | All of the above + LLM-friendly YAML |

**We're not inventing — we're combining.** The patent proves the filesystem approach works. We add YAML (human/LLM readable), prototypal inheritance (Self-style), and compiled closures (LLM as compiler).

---

*COM gave us interfaces. Self eliminated classes. Densmore showed us the filesystem IS the object graph. Selfish COM combines all three — filesystem-native, human-readable, LLM-friendly.*

---

**Deep dive:** [SELFISH-COM-IMPLEMENTATION.md](./SELFISH-COM-IMPLEMENTATION.md) — Full examples, code patterns, transformation specs.
