# Directory-as-Object: A COM-Inspired Architecture

> "Don Box made COM understandable. We made it unnecessary."

## The Selfification of COM

Self eliminated classes. We eliminate implementation objects.

In **Self** (Ungar & Smith), there's no class/instance distinction — objects inherit 
directly from other objects. No metaclass hierarchy. Just objects all the way down.

In **COM**, there's always an underlying C++ implementation class with vtable pointers 
at various offsets. QueryInterface adjusts pointers to find the right entry point.
The "object" is a memory blob containing multiple vtables.

**Directory-as-Object Selfifies COM:**

| COM | Self | Directory-as-Object |
|-----|------|---------------------|
| Implementation class | (none — just objects) | (none — just directories) |
| vtable pointers | Slots | Interface files |
| Pointer adjustment | (none) | (none) |
| Identity = memory address | Identity = the object | Identity = the path |
| QueryInterface finds vtable offset | Message lookup | File lookup |

The directory doesn't CONTAIN an implementation object — **it IS the object**.
The files don't POINT TO vtables — **they ARE the interfaces**.

No underlying class. No pointer adjustment. No offset math.
Just paths and files. Self for the filesystem.

*(We put COM in a rock tumbler until the I prefixes wore off.  
`IUnknown` → `unknown`. `IRoom` → `room`. Clean.)*

## The Insight

Directories are objects. Files are interfaces. The filesystem is the object graph.

This architecture draws from Microsoft's Component Object Model (COM) but eliminates 
the complexity of C++ multiple inheritance, vtable pointer adjustments, and reference 
counting by using the filesystem as the identity and lifetime manager.

## Two Forms of Objects

Objects exist in two forms, with different interface capabilities:

### File Objects (Single Interface)

A standalone file IS an object with exactly one interface:

```
characters/
├── bob.yml           # Object: characters/bob.yml, Interface: CHARACTER
├── alice.yml         # Object: characters/alice.yml, Interface: CHARACTER
└── guards.yml        # Object: characters/guards.yml, Interface: CHARACTER
```

**Type Declaration Convention:**

File objects SHOULD declare their type explicitly with `type:` field:

```yaml
# bob.yml
type: character       # Lowercase interface name (not K-line)
name: Bob the Guard
tags: [guard, hostile]
```

This lets the linter/compiler know definitively what interface the file implements
without guessing from filename or parent directory.

**Properties:**
- **Identity (unknown)**: The file path itself
- **Interfaces**: Only ONE — declared by `type:` field (or inferred as fallback)
- **QueryInterface**: Returns self for matching type, E_NOINTERFACE for anything else
- **Children**: NONE — files cannot contain other objects

```javascript
// File object queryInterface — returns PATH, not data
function queryInterfaceFile(filePath, iid) {
    if (iid === null || iid.toLowerCase() === 'unknown') {
        return filePath;  // Identity
    }
    const data = loadYaml(filePath);
    const fileType = data.type || inferType(filePath);  // Explicit > inferred
    return (iid.toLowerCase() === fileType.toLowerCase())
        ? filePath   // Same file IS the interface
        : null;      // E_NOINTERFACE — can't be a ROOM if it's a CHARACTER
}
```

### Directory Objects (Multiple Interfaces)

A directory IS an object that can support multiple interfaces:

```
don-hopkins/
├── CHARACTER.yml     # Interface: CHARACTER
├── ROOM.yml          # Interface: ROOM
├── SLIDESHOW.yml     # Interface: SLIDESHOW
└── treasures/        # Child object (has its own interfaces)
    └── OBJECT.yml
```

**Properties:**
- **Identity (unknown)**: The directory path itself
- **Interfaces**: ANY — determined by which files exist in the directory
- **QueryInterface**: Checks for corresponding file
- **Children**: AUTOMATIC — every directory can contain child directories

```javascript
// Directory object queryInterface — returns PATH, not data
function queryInterfaceDir(dirPath, iid) {
    if (iid === null || iid.toLowerCase() === 'unknown') {
        return dirPath;  // Identity
    }
    const interfaceFile = `${dirPath}/${iid.toUpperCase()}.yml`;
    return exists(interfaceFile) ? interfaceFile : null;  // E_NOINTERFACE
}
```

### Bare Directories (unknown Only)

A directory with no recognized interface files still exists as an object:

```
assets/
├── images/           # Just a container, no interfaces
│   ├── logo.png
│   └── banner.jpg
└── sounds/           # Just a container, no interfaces
    └── beep.wav
```

queryInterface returns null for everything except `unknown`.
These directories exist purely for containment/organization.

### Summary: File vs Directory Objects

| Aspect | File Object | Directory Object |
|--------|-------------|------------------|
| Identity | File path | Directory path |
| Interfaces | Exactly ONE | ZERO to MANY |
| QueryInterface | Self or nothing | Check for file |
| Children | NONE | Automatic (subdirs) |
| Use case | Simple entities | Complex multi-faceted entities |

## Type Declaration

### Directory Objects: Filename IS Type

For directory objects, the **filename** declares the interface:

```
don-hopkins/
├── CHARACTER.yml     # type = character (filename)
├── ROOM.yml          # type = room (filename)
├── SLIDESHOW.yml     # type = slideshow (filename)
└── README.md         # type = readme (instadoc!)
```

Uppercase filename → interface type. No ambiguity.

### README.md and .md Files (Instadoc)

Standard `queryInterface` only looks for `.yml` files. Documentation files 
(`.md`) use a parallel lookup:

```javascript
function getDoc(pointer, docType = 'readme') {
    const objectPath = toObjectPath(pointer);
    if (!isDirectory(objectPath)) return null;  // Files don't have sub-docs
    const docFile = `${objectPath}/${docType.toUpperCase()}.md`;
    return exists(docFile) ? docFile : null;
}

// Usage
getDoc("don-hopkins", "readme")   // → don-hopkins/README.md
getDoc("don-hopkins", "skill")    // → don-hopkins/SKILL.md
```

**Instadoc** — documentation is a parallel interface system for `.md` files:
- `README.md` → object documentation
- `SKILL.md` → behavioral protocol
- Standard `queryInterface` stays clean (`.yml` only)
- Doc lookup follows same pattern but separate namespace

### File Objects: `type:` Field

For standalone file objects, use explicit `type:` field:

```yaml
# bob.yml
type: character       # Lowercase, not K-line
name: Bob the Guard
tags: [guard, hostile]

# magic-sword.yml
type: object
name: Sword of Destiny
portable: true
```

**Why explicit type?**
- Linter/compiler knows definitively without guessing
- No reliance on parent directory naming conventions
- File can live anywhere and still be correctly typed
- Self-documenting

**Resolution order:**
1. `type:` field (explicit, wins)
2. Infer from parent directory name (fallback)
3. Error if ambiguous

## Typed Pointers

A **pointer** is an interface type + a path. The path can be either a file or directory:

```
character/bob.yml                    → File: bob.yml (type: character)
character/real-people/don-hopkins    → Dir: real-people/don-hopkins/CHARACTER.yml
room/real-people/don-hopkins         → Dir: real-people/don-hopkins/ROOM.yml
```

The type prefix tells you which interface to look for. The path tells you the object identity.

## COM Concepts Mapped to Filesystem

| COM Concept | Filesystem Equivalent |
|-------------|----------------------|
| unknown | File path (single interface) or directory path (multi-interface) |
| Interface | YAML file (standalone file OR uppercase file in directory) |
| QueryInterface | Check if file exists in directory |
| vtable | YAML file contents |
| GUID/IID | Filename (ROOM, CHARACTER, README, SKILL, CARD, etc.) |
| E_NOINTERFACE | File not found |
| AddRef/Release | Filesystem handles lifetime |
| CoCreateInstance | mkdir + write interface files |

## Interface Declaration

Interfaces are declared differently for files vs directories:

**File objects** — the file itself IS the interface:
```
characters/bob.yml      # bob.yml declares CHARACTER interface by existing
characters/alice.yml    # alice.yml declares CHARACTER interface by existing
```

**Directory objects** — standard uppercase files declare interfaces:
```
don-hopkins/
├── CHARACTER.yml    # Declares ICharacter
├── ROOM.yml         # Declares IRoom  
├── CARD.yml         # Declares ICard (quick metadata)
├── SKILL.md         # Declares ISkill (behavioral protocol)
├── README.md        # Declares IReadme (instadoc!)
└── fmc-898/         # Child object (containment)
    └── ROOM.yml
```

Each interface file is a **vtable** — the actual interface implementation.

## The query-interface Protocol

The `query-interface` protocol provides COM-style interface discovery for filesystem objects.

### API: `queryInterface(pointer, iid)`

```javascript
/**
 * queryInterface - COM-style interface lookup for filesystem objects
 * 
 * @param {string} pointer - Repo-relative path to object or interface file
 *                           (later: full moollm:// URL)
 * @param {string|null} iid - Interface ID: 'room', 'character', 'slideshow', etc.
 *                            null or 'unknown' → return object identity (directory)
 * @returns {string|null} - Path to interface file, or null (E_NOINTERFACE)
 */
function queryInterface(pointer, iid = null) {
    // Normalize: walk UP from interface file to object directory
    const objectPath = toObjectPath(pointer);
    if (!exists(objectPath)) return null;
    
    // unknown query → return object identity (directory)
    if (iid === null || iid.toLowerCase() === 'unknown') {
        return objectPath;
    }
    
    if (isFile(objectPath)) {
        // File object: single interface only
        const data = loadYaml(objectPath);
        const fileType = data.type || inferType(objectPath);
        return (iid.toLowerCase() === fileType.toLowerCase()) 
            ? objectPath   // Same file IS the interface
            : null;        // E_NOINTERFACE
    }
    
    if (isDirectory(objectPath)) {
        // Directory object: look for INTERFACE.yml
        const interfaceFile = `${objectPath}/${iid.toUpperCase()}.yml`;
        return exists(interfaceFile) ? interfaceFile : null;
    }
    
    return null;
}

/**
 * Walk UP from interface file pointer to object directory
 * don-hopkins/ROOM.yml → don-hopkins/
 * don-hopkins/CHARACTER.yml → don-hopkins/
 * don-hopkins/ → don-hopkins/
 * bob.yml → bob.yml (file object, no parent to walk to)
 */
function toObjectPath(pointer) {
    if (isDirectory(pointer)) return pointer;
    
    // If it's an interface file (UPPERCASE.yml), walk up to directory
    const filename = basename(pointer);
    if (filename === filename.toUpperCase() && filename.endsWith('.yml')) {
        return dirname(pointer);  // Walk up to object directory
    }
    
    // Otherwise it's a file object (bob.yml) — return as-is
    return pointer;
}
```

### Key Behaviors

| Input Pointer | IID | Result |
|---------------|-----|--------|
| `don-hopkins/` | `null` | `don-hopkins/` (identity) |
| `don-hopkins/` | `'unknown'` | `don-hopkins/` (identity) |
| `don-hopkins/` | `'room'` | `don-hopkins/ROOM.yml` |
| `don-hopkins/` | `'character'` | `don-hopkins/CHARACTER.yml` |
| `don-hopkins/` | `'slideshow'` | `null` (E_NOINTERFACE if no file) |
| `don-hopkins/ROOM.yml` | `null` | `don-hopkins/` (walk up to identity) |
| `don-hopkins/ROOM.yml` | `'unknown'` | `don-hopkins/` (walk up) |
| `don-hopkins/ROOM.yml` | `'character'` | `don-hopkins/CHARACTER.yml` |
| `bob.yml` | `null` | `bob.yml` (file object identity) |
| `bob.yml` | `'character'` | `bob.yml` (if type matches) |
| `bob.yml` | `'room'` | `null` (E_NOINTERFACE) |

### COM Parallel

| COM | query-interface |
|-----|-----------------|
| `pUnk->QueryInterface(IID_IRoom, &pRoom)` | `queryInterface(ptr, 'room')` |
| `pRoom->QueryInterface(IID_IUnknown, &pUnk)` | `queryInterface(roomFile, 'unknown')` |
| Returns adjusted `this*` | Returns path to interface file |
| `E_NOINTERFACE` | `null` |
| `S_OK` + valid pointer | Non-null path string |

### Future: moollm:// URLs

Currently takes repo-relative paths. Future enhancement: full URLs:

```
moollm://repo/path/to/object#interface

moollm://adventure-4/don-hopkins#room       → ROOM.yml
moollm://adventure-4/don-hopkins#character  → CHARACTER.yml
moollm://adventure-4/don-hopkins             → directory (unknown)
moollm://skills/bootstrap#skill             → SKILL.md (doc interface)
```

The fragment (`#interface`) specifies the interface. No fragment = unknown.

### What We Skip (C++ Complexity)

- **No pointer adjustment** — paths don't need offset math
- **No ref counting** — filesystem handles lifetime
- **No thunks** — no `this` pointer adjustment
- **No multiple vtable layouts** — just filename lookup
- **No GUIDs** — human-readable interface names
- **No registry** — filesystem IS the registry

## Pointer Resolution

A typed pointer = interface type + path. Resolution depends on whether it's a file or directory:

```
# File pointers — the file IS the interface
character/npcs/bob.yml  →  load(npcs/bob.yml)

# Directory pointers — look up interface file
character/real-people/don-hopkins  →  load(real-people/don-hopkins/CHARACTER.yml)
room/real-people/don-hopkins       →  load(real-people/don-hopkins/ROOM.yml)
slideshow/real-people/don-hopkins  →  load(real-people/don-hopkins/SLIDESHOW.yml)
```

**Same directory. Different file lookup. No pointer adjustments.**

### Why This Beats C++ COM

In C++ COM with multiple inheritance:

```cpp
// The nightmare: underlying C++ object with multiple vtables
class DonHopkins : public IRoom, public ICharacter {
    // Memory layout:
    // [vptr_IRoom]        <- offset 0
    // [vptr_ICharacter]   <- offset 8
    // [member data...]
    //
    // QueryInterface must return ADJUSTED pointers
    // to the correct vtable entry point!
};

// The horror
IRoom* pRoom = ...;           // Points to offset 0
ICharacter* pChar;
pRoom->QueryInterface(IID_ICharacter, (void**)&pChar);
// pChar != pRoom even though SAME OBJECT
// pChar points to offset 8 (different vtable)
// Compiler generates "thunks" to adjust 'this' pointer
```

**The C++ model:**
- Underlying C++ class object exists in memory
- Multiple vtable pointers at different offsets  
- QueryInterface returns adjusted pointers to different entry points
- `this` pointer adjustment macrology everywhere

**Our model:**
- **No underlying implementation class**
- **The directory IS the object** (the identity, queryable as 'unknown')
- Files ARE the interfaces (not pointers to vtables)
- QueryInterface = file lookup, identity unchanged

```python
# Clean and simple
room_data = query_interface("don-hopkins", "ROOM")
char_data = query_interface("don-hopkins", "CHARACTER")
# Same path (identity), different files (interfaces). 
# No pointer adjustment. No thunks. No offset math.
```

The directory `don-hopkins/` doesn't CONTAIN an object — it IS the object.
`CHARACTER.yml` and `ROOM.yml` aren't vtable pointers — they ARE the interfaces.

## Registry Compilation

The compiler scans the filesystem and registers both file and directory objects:

```python
def compile_world(root: Path) -> dict[str, dict[str, dict]]:
    """Compile all objects, handling both file and directory forms."""
    tables = {iface: {} for iface in INTERFACES}
    
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in ['.yml', '.yaml']:
            # File object: single interface
            if path.name.upper() not in INTERFACE_FILES:
                # Standalone file like bob.yml
                data = load_yaml(path)
                # Explicit type: field wins, then infer from context
                interface = data.get('type') or infer_type(path)
                relative = path.relative_to(root)
                tables[interface][str(relative)] = data
        
        elif path.is_dir():
            # Directory object: check for interface files
            relative = path.relative_to(root)
            for interface in INTERFACES:
                interface_file = path / f"{interface.upper()}.yml"
                if interface_file.exists():
                    data = load_yaml(interface_file)
                    tables[interface.lower()][str(relative)] = data
    
    return tables

# Standard interfaces (.yml only for QueryInterface)
INTERFACES = ['room', 'character', 'slideshow', 'object', 'catalog', 'card']
INTERFACE_FILES = {'ROOM.YML', 'CHARACTER.YML', 'SLIDESHOW.YML', 'OBJECT.YML', 
                   'CATALOG.YML', 'CARD.YML'}

# Documentation interfaces (.md, separate lookup)
DOC_INTERFACES = ['readme', 'skill']
DOC_FILES = {'README.MD', 'SKILL.MD'}
```

**Result examples:**

A directory with both CHARACTER.yml and ROOM.yml produces TWO registry entries:
- `character/real-people/don-hopkins` → CHARACTER.yml data
- `room/real-people/don-hopkins` → ROOM.yml data

Same object identity (directory), different interfaces (files).

A standalone file produces ONE registry entry:
- `character/npcs/bob.yml` → bob.yml data

Single object (file), single interface (inferred from context).

## Late Binding vs Early Binding

### IDispatch (Late Binding) — YAML Fields

```yaml
# Runtime lookup, flexible, variant-like
interests:
  - pattern: "examine {object}"
    method: examine
    args: [object]

description: |
  A warm, inviting space.
```

The engine looks up fields by name at runtime:

```javascript
// Like IDispatch::GetIDsOfNames + Invoke
const desc = obj['description'];
const interests = obj['interests'];
```

### Direct vtable (Early Binding) — Compiled `_js` Closures

```yaml
# Compiled, typed, fast
guard_js: "(ctx) => ctx.hasTag('acme')"
description_message_js: "(ctx) => `Welcome, ${ctx.player.name}`"
```

The compiler generates callable functions:

```javascript
// Like direct vtable call
if (obj.guard_js_fn) {
    return obj.guard_js_fn(ctx);  // Fast path
}
// Fall back to IDispatch-style lookup
return obj.guard_js ? eval(obj.guard_js)(ctx) : true;
```

### The `_js` Suffix Convention

Any field can have a `_js` companion that provides compiled behavior:

| Static Field | Dynamic Field | Purpose |
|--------------|---------------|---------|
| `description` | `description_js` | Room/object description |
| `pass_message` | `pass_message_js` | Exit success message |
| `fail_message` | `fail_message_js` | Exit failure message |
| `guard` | `guard_js` | Access control predicate |
| `traverse_message` | `traverse_message_js` | Movement narration |

The `_js` version always wins if present — it's the "type library" annotation 
saying "this has a fast path available."

## Engine Resolution Pattern

```javascript
resolveText(obj, key) {
    // 1. Try compiled vtable (direct binding)
    const jsFn = obj[key + '_js_fn'];
    if (jsFn) return jsFn(this.ctx);
    
    // 2. Try JS source, compile & cache (JIT)
    const jsSrc = obj[key + '_js'];
    if (jsSrc) {
        obj[key + '_js_fn'] = eval(jsSrc);
        return obj[key + '_js_fn'](this.ctx);
    }
    
    // 3. Fall back to IDispatch (variant)
    const value = obj[key];
    if (Array.isArray(value)) return value[Math.floor(Math.random() * value.length)];
    return value || null;
}
```

## Containment and Aggregation

### Containment (Directory Objects Only)

Directory objects can contain child objects. File objects cannot.

```
acme-surplus/                    # Directory object
├── ROOM.yml                     # Interface: ROOM
├── warehouse/                   # Child directory object
│   └── ROOM.yml
├── basement/                    # Child directory object
│   ├── ROOM.yml
│   └── control-room/            # Grandchild directory object
│       └── ROOM.yml
└── characters/                  # Child container (bare directory)
    ├── shopkeeper.yml           # File object (single interface)
    └── guard.yml                # File object (single interface)
```

**Containment paths:**
- `room/acme-surplus` (directory object, multi-interface capable)
- `room/acme-surplus/warehouse` (child directory object)
- `room/acme-surplus/basement/control-room` (grandchild)
- `character/acme-surplus/characters/shopkeeper.yml` (file object, single interface)

File objects (`shopkeeper.yml`) ARE contained BY directories but CANNOT contain children themselves.

### Aggregation (Sibling Interfaces)

A ROOM.yml can reference a CHARACTER.yml from the same directory:

```yaml
# ROOM.yml
name: Don's Home
resident: ./CHARACTER.yml  # Reference sibling interface of same object
```

Or embed data from it:

```yaml
# ROOM.yml  
name: Don's Home
owner:
  $ref: ./CHARACTER.yml#character/name
```

This is like COM aggregation — the directory object delegates to its interface files.

## Navigation Patterns

| Pattern | Meaning |
|---------|---------|
| `./` | Same directory (sibling interface) |
| `../` | Parent directory (container object) |
| `child/` | Child directory (contained object) |
| `../../sibling/` | Navigate up then down |

These are relative paths resolved against the current object's identity (directory).

## Comparison Summary

| Aspect | C++ COM | Filesystem Objects |
|--------|---------|---------------------|
| Identity | Memory address | File or directory path |
| Interface | vtable pointer | YAML file (standalone or in dir) |
| QueryInterface | Pointer adjustment | File lookup or self |
| Single interface | Simple class | Standalone file |
| Multiple interfaces | Complex layout | Directory with multiple files |
| Ref counting | Manual AddRef/Release | Filesystem |
| Type info | .tlb files | File naming convention |
| Late binding | IDispatch | YAML field lookup |
| Early binding | Direct vtable | `_js` compiled closures |
| Containment | Tricky delegation | Child directories (dirs only) |
| Registration | Registry hell | Compile to JSON |

## Benefits

1. **No pointer adjustments** — Same path, different file lookup
2. **No ref counting** — Filesystem handles lifetime
3. **Human readable** — YAML files, not binary vtables
4. **Git-friendly** — Merge conflicts are manageable
5. **Inspectable** — Just read the files
6. **Flexible** — Add interfaces by adding files
7. **LLM-friendly** — Can read and write the "vtables"

## Implementation in Adventure Engine

### Compiler (`compile.py`)

```python
# Scan for all interface files in each directory
for dir in adventure.rglob('*'):
    if (dir / 'ROOM.yml').exists():
        room_table[path_to_id(dir)] = compile_room(dir)
    if (dir / 'CHARACTER.yml').exists():
        char_table[path_to_id(dir)] = compile_character(dir)
    if (dir / 'SLIDESHOW.yml').exists():
        slideshow_table[path_to_id(dir)] = compile_slideshow(dir)
```

### Runtime (`engine.js`)

```javascript
get(ref) {
    // ref = "room/pub" or "character/don-hopkins"
    // Registry keys are type-prefixed
    return this.registry[ref];
}

// QueryInterface equivalent
queryInterface(path, type) {
    return this.get(`${type}/${path}`);
}
```

### Export (`world.json`)

```json
{
  "room": {
    "pub": { "name": "The Pub", "exits": {...} },
    "don-hopkins": { "name": "Don's Home", "exits": {...} }
  },
  "character": {
    "don-hopkins": { "name": "Don Hopkins", "tags": [...] }
  }
}
```

Note: `don-hopkins` appears in both `room` and `character` tables — same object, 
different interfaces.

---

*Inspired by Don Box's "Essential COM" and David Ungar's Self.  
COM gave us interface-based design. Self showed us we don't need classes.  
This architecture Selfifies COM — making it filesystem-native, human-readable, and LLM-friendly.*
