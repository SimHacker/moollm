# Selfish COM: Implementation Guide

> **Prerequisites:** Read [DIRECTORY-AS-OBJECT.md](./DIRECTORY-AS-OBJECT.md) first for the core concept.

This document provides detailed examples, code patterns, and transformation specs for implementing Selfish COM. It's intended for:
- Developers building on this architecture
- LLM compilers generating code from YAML
- Anyone who needs the full picture

---

## QueryInterface Protocol

### API Signature

```javascript
/**
 * @param {string} pointer - Repo-relative path (file or directory)
 * @param {string|null} iid - Interface ID: 'room', 'character', etc.
 *                            null or 'unknown' → return identity
 * @returns {string|null} - Path to interface file, or null
 */
function queryInterface(pointer, iid = null)
```

### Resolution Table

| Pointer | IID | Result |
|---------|-----|--------|
| `don-hopkins/` | `null` | `don-hopkins/` |
| `don-hopkins/` | `'room'` | `don-hopkins/ROOM.yml` |
| `don-hopkins/` | `'character'` | `don-hopkins/CHARACTER.yml` |
| `don-hopkins/` | `'slideshow'` | `null` (not found) |
| `don-hopkins/ROOM.yml` | `null` | `don-hopkins/` (walk up) |
| `don-hopkins/ROOM.yml` | `'character'` | `don-hopkins/CHARACTER.yml` |
| `bob.yml` | `null` | `bob.yml` (file identity) |
| `bob.yml` | `'character'` | `bob.yml` (if type matches) |
| `bob.yml` | `'room'` | `null` (wrong type) |

### Implementation

```javascript
function queryInterface(pointer, iid = null) {
    const objectPath = toObjectPath(pointer);
    if (!exists(objectPath)) return null;
    
    if (iid === null || iid.toLowerCase() === 'unknown') {
        return objectPath;
    }
    
    if (isFile(objectPath)) {
        const data = loadYaml(objectPath);
        const fileType = data.type || inferType(objectPath);
        return (iid.toLowerCase() === fileType.toLowerCase()) 
            ? objectPath : null;
    }
    
    if (isDirectory(objectPath)) {
        const interfaceFile = `${objectPath}/${iid.toUpperCase()}.yml`;
        return exists(interfaceFile) ? interfaceFile : null;
    }
    
    return null;
}

function toObjectPath(pointer) {
    if (isDirectory(pointer)) return pointer;
    const filename = basename(pointer);
    // UPPERCASE.yml = interface file, walk up to directory
    if (filename === filename.toUpperCase() && filename.endsWith('.yml')) {
        return dirname(pointer);
    }
    return pointer;  // File object, return as-is
}
```

---

## Object Forms

### Directory Object (Multiple Interfaces)

```
don-hopkins/
├── CHARACTER.yml     # queryInterface('character')
├── ROOM.yml          # queryInterface('room')
├── SLIDESHOW.yml     # queryInterface('slideshow')
├── portrait.png      # resource (shared by all interfaces)
├── bio.md            # resource
└── memories/         # child object
    └── ROOM.yml
```

Interfaces can reference shared resources:
```yaml
# CHARACTER.yml
avatar: ./portrait.png

# ROOM.yml
owner_portrait: ./portrait.png   # Same resource, different purpose
```

### File Object (Single Interface)

```yaml
# characters/bob.yml
type: character       # Explicit type declaration
name: Bob the Guard
tags: [guard, hostile]
```

File objects CANNOT contain children. They implement exactly one interface.

### Type Declaration

| Object Form | How Type is Determined |
|-------------|------------------------|
| `ROOM.yml` in directory | Filename = type |
| `COLLIDER-body.yml` | Must have `type: collider` inside |
| `bob.yml` standalone | Must have `type: character` inside |

---

## Inheritance (Self-Style)

### Source YAML

```yaml
# characters/abstract/notorious-hacker.yml
type: character
abstract: true
tags: [hacker, notorious]
reputation: mythical
greeting: "Greetings, fellow traveler."

# characters/abstract/pie-menu-freak.yml
type: character
abstract: true
tags: [pie-menus, ui-innovator]
favorite_shape: circular

# don-hopkins/CHARACTER.yml
parents:
  - characters/abstract/notorious-hacker
  - characters/abstract/pie-menu-freak
name: Don Hopkins
tags: [hacker, artist]      # Override
home: ./ROOM.yml
```

### Compiled Output (Flattened)

```json
{
  "don-hopkins": {
    "reputation": "mythical",
    "greeting": "Greetings, fellow traveler.",
    "favorite_shape": "circular",
    "name": "Don Hopkins",
    "tags": ["hacker", "artist"],
    "home": "./ROOM.yml",
    "_parents": ["characters/abstract/notorious-hacker", "characters/abstract/pie-menu-freak"],
    "_path": "don-hopkins/"
  }
}
```

**Compiler flattens inheritance. Runtime does simple property lookup.**

---

## Closure Compilation

### Closure Signature

All `_js` fields compile to bodies wrapped with:
```javascript
(world, subject, verb, object) => { /* body here */ }
```

| Parameter | What | Nullable |
|-----------|------|----------|
| `world` | Shared game state | Never null |
| `subject` | Who is acting | May be null |
| `verb` | The action | May be null |
| `object` | Target of action | May be null |

### Transformation Example

**Input (YAML):**
```yaml
unlock_condition: |
  Player has the red admin card AND has not triggered the alarm.
```

**Output (YAML with compiled _js):**
```yaml
unlock_condition: |
  Player has the red admin card AND has not triggered the alarm.
unlock_condition_js: |
  return subject?.hasItem('red-admin-card') && !world.flags.alarm_triggered
```

**Runtime wrapping:**
```javascript
const fn = eval(`(world, subject, verb, object) => {
  return subject?.hasItem('red-admin-card') && !world.flags.alarm_triggered
}`);
```

### Common Compilable Fields

| NL Field | Compiled Field | Returns |
|----------|----------------|---------|
| `unlock_condition` | `unlock_condition_js` | boolean |
| `visible_when` | `visible_when_js` | boolean |
| `guard` | `guard_js` | boolean |
| `on_enter` | `on_enter_js` | void |
| `description` | `description_js` | string |
| `pass_message` | `pass_message_js` | string |

---

## Runtime Resolution

```javascript
resolveText(obj, key, subject, verb, object) {
    // 1. Cached closure (hot path)
    const jsFn = obj[key + '_js_fn'];
    if (jsFn) return jsFn(this, subject, verb, object);
     
    // 2. Compile and cache
    const jsSrc = obj[key + '_js'];
    if (jsSrc) {
        obj[key + '_js_fn'] = this.compileJs(jsSrc);
        return obj[key + '_js_fn'](this, subject, verb, object);
    }
    
    // 3. Static value (or random from array)
    const value = obj[key];
    if (Array.isArray(value)) {
        return value[Math.floor(Math.random() * value.length)];
    }
    return value || null;
}
```

---

## Compilation Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│  SOURCE: Directory Tree + YAML                                  │
│  adventure-4/                                                   │
│  ├── pub/ROOM.yml                                               │
│  ├── characters/don-hopkins/CHARACTER.yml                       │
│  └── ...                                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  COMPILER: Python walker + LLM                                  │
│  - os.walk() emits events (found_room, found_condition, ...)    │
│  - LLM reads handler instructions                               │
│  - LLM generates _js from NL                                    │
│  - Writes enriched YAML back                                    │
│  - Exports flattened JSON                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  OUTPUT: JSON Trees                                             │
│  {                                                              │
│    "room": { "pub": {...}, "pub/bar": {...} },                  │
│    "character": { "don-hopkins": {...} }                        │
│  }                                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  RUNTIME: JavaScript Engine                                     │
│  - Loads JSON into registry                                     │
│  - Compiles _js to closures on first use                        │
│  - Caches for JIT optimization                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tree-Shaking

The compiler omits fields not used by the target runtime:

**Source (verbose):**
```yaml
object: red-key
author_notes: "Design rationale..."      # Editor only
design_iteration: 3                      # Metadata
unity_prefab: "prefabs/key.prefab"       # Different VM
description: "A small red key"           # ✓ Used
weight: 0.1                              # ✓ Used
```

**Compiled (tree-shaken):**
```json
{
  "id": "red-key",
  "description": "A small red key",
  "weight": 0.1
}
```

---

## Multiple Same-Type Interfaces

For multiple colliders, physics shapes, etc.:

```
player/
├── COLLIDER.yml           # Canonical (auto-recognized)
├── COLLIDER-body.yml      # Suffixed (needs type: collider)
├── COLLIDER-sword.yml     # Suffixed (needs type: collider)
```

```yaml
# COLLIDER-body.yml
type: collider             # Required for suffixed files
shape: capsule
height: 1.8

# COLLIDER-sword.yml
type: collider
shape: box
trigger: true
```

Query patterns:
```javascript
queryInterface('player/', 'collider')     // → COLLIDER.yml (canonical)
listInterfaces('player/', 'collider')     // → [COLLIDER.yml, COLLIDER-body.yml, ...]
```

---

## Registry Compilation

```python
def compile_world(root: Path) -> dict[str, dict]:
    tables = {iface: {} for iface in INTERFACES}
    
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in ['.yml', '.yaml']:
            if path.name.upper() not in INTERFACE_FILES:
                # Standalone file object
                data = load_yaml(path)
                interface = data.get('type') or infer_type(path)
                tables[interface][str(path.relative_to(root))] = data
        
        elif path.is_dir():
            # Directory object - check for interface files
            for interface in INTERFACES:
                interface_file = path / f"{interface.upper()}.yml"
                if interface_file.exists():
                    data = load_yaml(interface_file)
                    tables[interface][str(path.relative_to(root))] = data
    
    return tables

INTERFACES = ['room', 'character', 'object', 'slideshow', 'service']
INTERFACE_FILES = {f'{i.upper()}.YML' for i in INTERFACES}
```

---

## COM Mapping Reference

| COM Concept | Selfish COM |
|-------------|-------------|
| `IUnknown` | Directory path |
| `QueryInterface` | File existence check |
| vtable pointer | YAML file contents |
| GUID/IID | Filename (ROOM, CHARACTER) |
| `E_NOINTERFACE` | File not found |
| `AddRef`/`Release` | Filesystem handles lifetime |
| Type library | `_js` compiled closures |
| `IDispatch` | Runtime YAML field lookup |

---

## Example: Full Object Lifecycle

### 1. Author writes YAML

```yaml
# pub/ROOM.yml
name: The Cozy Pub
description: A warm tavern with crackling fire.

exits:
  north:
    to: garden/
    unlock_condition: The door is unlocked after 6pm.
  down:
    to: basement/
    guard: Player has a lantern or other light source.

on_enter: The bartender looks up and nods.
```

### 2. Compiler processes

Events emitted:
```
found_room      id=pub/
found_exit      from=pub/ to=garden/ dir=north
found_condition id=pub/ROOM.yml field=exits.north.unlock_condition
found_exit      from=pub/ to=basement/ dir=down  
found_condition id=pub/ROOM.yml field=exits.down.guard
```

### 3. LLM compiles conditions

```yaml
# pub/ROOM.yml (enriched)
name: The Cozy Pub
description: A warm tavern with crackling fire.

exits:
  north:
    to: garden/
    unlock_condition: The door is unlocked after 6pm.
    unlock_condition_js: return world.time.hour >= 18
  down:
    to: basement/
    guard: Player has a lantern or other light source.
    guard_js: return subject?.hasInventoryTag('lighting')

on_enter: The bartender looks up and nods.
```

### 4. Export to JSON

```json
{
  "room": {
    "pub/": {
      "name": "The Cozy Pub",
      "description": "A warm tavern with crackling fire.",
      "exits": {
        "north": {
          "to": "garden/",
          "unlock_condition_js": "return world.time.hour >= 18"
        },
        "down": {
          "to": "basement/",
          "guard_js": "return subject?.hasInventoryTag('lighting')"
        }
      },
      "on_enter": "The bartender looks up and nods."
    }
  }
}
```

### 5. Runtime executes

```javascript
// Player tries to go down
const exit = room.exits.down;
const canPass = world.resolveCondition(exit, 'guard', player, 'go', 'down');
// Evaluates: player.hasInventoryTag('lighting')
```

---

## See Also

- [DIRECTORY-AS-OBJECT.md](./DIRECTORY-AS-OBJECT.md) — Core concept overview
- [../skills/adventure/engine.js](../skills/adventure/engine.js) — Runtime implementation
- [../skills/adventure/compile.py](../skills/adventure/compile.py) — Compiler implementation
