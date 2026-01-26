# Selfish COM: Directory-as-Object Architecture

> "Don Box made COM understandable. We made it unnecessary."

## The Selfification of COM (a.k.a. "Selfish COM")

Self eliminated classes. We eliminate implementation objects.

In **Self** (Ungar & Smith), there's no class/instance distinction — objects inherit 
directly from other objects. No metaclass hierarchy. Just objects all the way down.

In **COM**, there's always an underlying C++ implementation class with vtable pointers 
at various offsets. QueryInterface adjusts pointers to find the right entry point.
The "object" is a memory blob containing multiple vtables.

**Selfish COM:**

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

**Why "Selfish COM"?**
- **Self**ish: Inspired by the Self language (no classes, just objects)
- Self**ish**: The directory IS the object — self-contained, self-describing
- Sel**fish**: Slippery, hard to catch, swims through filesystems

### COM on Top, Self Underneath

The architecture is layered: **COM sits on top of Self**.

```
┌─────────────────────────────────────────────────────────────────┐
│  COM LAYER: Directories + QueryInterface                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  don-hopkins/           ← object identity (unknown)      │   │
│  │  ├── CHARACTER.yml      ← queryInterface('character')    │   │
│  │  ├── ROOM.yml           ← queryInterface('room')         │   │
│  │  ├── portrait.png       ← queryInterface('resource')     │   │
│  │  └── README.md          ← getDoc('readme')               │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
            queryInterface returns PATH to interface file
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  SELF LAYER: Interface files with prototypal inheritance        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  CHARACTER.yml:                                          │   │
│  │    parents:                                              │   │
│  │      - ../abstract/notorious-hacker                      │   │
│  │      - ../abstract/pie-menu-freak                        │   │
│  │      - ../abstract/news-programmer                       │   │
│  │      - ../abstract/simcity-contributor                   │   │
│  │    name: Don Hopkins                                     │   │
│  │    tags: [hacker, artist]                                │   │
│  │    # Local state overrides inherited slots               │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**The COM layer** handles:
- Object identity (`unknown` = directory path)
- Interface enumeration (`ls` the directory)
- Interface lookup (`queryInterface` = file lookup)
- Resource access (images, audio, etc.)

**The Self layer** handles:
- Each interface file IS a Self-style object
- Multiple prototypal inheritance via `parents:` array
- Slot lookup walks the prototype chain
- Local state overrides inherited values

### Interfaces Have Their Own Inheritance

This is the key insight: **once you reach an interface file, it can declare 
any number of parents** — abstract concepts, real people, archetypes:

```yaml
# don-hopkins/CHARACTER.yml
parents:
  - characters/abstract/notorious-hacker
  - characters/abstract/pie-menu-freak  
  - characters/abstract/artist-programmer
  - characters/real-people/self-programmer    # inherit from David Ungar patterns!
  - characters/abstract/cat-lover

name: Don Hopkins
home: ./ROOM.yml              # sibling interface in same directory
interests:
  - cellular automata
  - pie menus
  - NeWS
```

```yaml
# characters/abstract/notorious-hacker.yml
type: character
abstract: true
tags: [hacker, notorious, pie-eyed]
reputation: mythical
default_greeting: "Greetings, fellow traveler of the digital realm."
```

The interface file inherits from multiple parents, mixing in traits from 
abstract archetypes AND concrete examples. Pure Self-style delegation.

### COM Inside Out: The Void at the Center

Traditional COM:
```
┌──────────────────────────────────────┐
│  C++ Implementation Class            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │ IRoom   │ │ IChar   │ │ ISlide  │ │  ← vtable pointers
│  │ vtable* │ │ vtable* │ │ vtable* │ │
│  └─────────┘ └─────────┘ └─────────┘ │
│  [shared member data...]             │  ← one implementation
└──────────────────────────────────────┘
```

In COM, there's ONE monolithic implementation class that implements ALL 
interfaces. The interfaces share state through the underlying C++ object.

**Selfish COM turns this inside out:**

```
┌───────────────────────────────────────┐
│  Directory (unknown)                  │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ ROOM    │ │ CHAR    │ │ SLIDE   │  │  ← interface FILES
│  │ .yml    │ │ .yml    │ │ .yml    │  │ 
│  │ (Self   │ │ (Self   │ │ (Self   │  │  ← each with own
│  │ object) │ │ object) │ │ object) │  │     prototype chain
│  └─────────┘ └─────────┘ └─────────┘  │
│          ↘      ↓      ↙              │
│              [VOID]                   │  ← NO shared implementation!
│                                       │
│  Context: siblings visible via ls     │
│  Resources: queryInterface('resource')│
└───────────────────────────────────────┘
```

**There is no underlying implementation class. There's a VOID.**

Each interface file:
- IS its own Self-style object
- Has its OWN prototype inheritance chain
- Can reference siblings via relative paths (`./ROOM.yml`)
- Lives IN THE CONTEXT of the containing directory
- Can enumerate siblings (`ls`) and query for them

**Siblings include interfaces, resources, AND sub-directories:**

```
don-hopkins/
├── CHARACTER.yml     ← interface (sibling)
├── ROOM.yml          ← interface (sibling)
├── portrait.png      ← resource (sibling) — shared!
├── bio.md            ← resource (sibling) — shared!
├── config.yml        ← data file (sibling) — shared!
└── memories/         ← sub-directory (child object)
```

**Multiple interfaces can share resources within the same directory:**

```yaml
# CHARACTER.yml
name: Don Hopkins
avatar: ./portrait.png          # Uses shared resource
backstory: ./bio.md             # Uses shared doc

# ROOM.yml  
name: Don's Home
owner_portrait: ./portrait.png  # SAME resource, different purpose!
history: ./bio.md               # SAME doc, different context!
```

This is Alan Kay's **biological cell** interpretation of OOP:
- The **directory** is the **cell membrane** — a boundary
- **Interfaces** are different **receptors** on the membrane
- **Resources** are **organelles** inside — shared by all receptors
- **Data files** are **DNA/RNA** — shared configuration
- **Sub-directories** are **daughter cells** — contained objects

The interfaces don't have hidden shared state like COM's C++ implementation.
Instead, they have **explicit shared resources** — visible files in the same 
directory that any interface can reference. Sharing is opt-in and transparent.

**The two mechanisms:**

| Mechanism | What | How |
|-----------|------|-----|
| **Sharing** | State, interfaces, resources | Within a directory (siblings) |
| **Aggregation** | Objects | Via directory tree (parent/child) |

```
pub/                          ← AGGREGATES child objects
├── ROOM.yml                  ← SHARES with siblings below
├── menu.yml                  ← shared state (prices, items)
├── ambiance.mp3              ← shared resource (background music)
├── bar/                      ← AGGREGATED child object
│   ├── ROOM.yml              ← bar SHARES with ITS siblings
│   └── drinks.yml            ← bar's shared state
└── kitchen/                  ← AGGREGATED child object
    ├── ROOM.yml
    └── recipes.yml
```

**Directories share STATE and INTERFACES. Directory trees aggregate OBJECTS.**

The directory provides **context**, not **implementation**:
- Identity (the path)
- Enumeration (what interfaces/resources exist)
- Namespace (relative paths work)
- But NO shared vtable, NO unified implementation

### The `unknown` Interface Methods

The `unknown` interface (directory) provides these fundamental operations:

```javascript
// The unknown interface — every directory implements this
const unknown = {
    // Identity
    path:     () => dirPath,                    // Who am I?
    
    // Enumeration — the critical "ls" operation!
    ls:       () => fs.readdirSync(dirPath),    // List ALL children
    children: () => subdirectories(dirPath),    // List child objects (dirs only)
    siblings: () => ls(dirname(dirPath)),       // List siblings in parent
    
    // Navigation
    parent:   () => dirname(dirPath),           // Go up (..)
    child:    (name) => join(dirPath, name),    // Go down
    
    // Queries
    has:      (name) => exists(join(dirPath, name)),  // Does child exist?
    queryInterface: (iid) => /* ... */,         // Get specific interface
};
```

**`ls` is the critical method** — it enumerates everything in the directory.

A rich `ls` returns structured info, not just names:

```javascript
// Rich ls — returns type info for each entry
unknown.ls()  
// → [
//   { name: 'CHARACTER.yml', kind: 'file', type: 'character' },  // inferred from filename
//   { name: 'ROOM.yml',      kind: 'file', type: 'room' },       // inferred from filename
//   { name: 'portrait.png',  kind: 'file', type: 'resource' },   // non-YAML = resource
//   { name: 'bio.md',        kind: 'file', type: 'resource' },   // markdown = resource
//   { name: 'config.yml',    kind: 'file', type: 'data' },       // lowercase = data
//   { name: 'COLLIDER-body.yml', kind: 'file', type: 'collider' }, // explicit type: field!
//   { name: 'memories/',     kind: 'dir',  type: 'unknown' },    // directory = unknown
// ]
```

**Type inference rules:**
| Pattern | Kind | Type |
|---------|------|------|
| `UPPERCASE.yml` | file | inferred from filename (room, character, etc.) |
| `UPPERCASE-suffix.yml` | file | from explicit `type:` field inside |
| `lowercase.yml` | file | data (shared state) or from `type:` field |
| `*.png`, `*.mp3`, etc. | file | resource |
| `*.md` | file | resource (or doc interface) |
| `name/` | dir | unknown (child object) |

```javascript
// Filter to just interfaces (canonical + suffixed with type:)
unknown.ls().filter(e => e.kind === 'file' && e.type !== 'resource' && e.type !== 'data')
// → [CHARACTER.yml, ROOM.yml, COLLIDER-body.yml]

// Filter to just child objects
unknown.ls().filter(e => e.kind === 'dir')
// → [memories/]

// Filter to just resources
unknown.ls().filter(e => e.type === 'resource')
// → [portrait.png, bio.md]
```

This is like COM's `IEnumUnknown` but richer — type info comes for free.

### LLM Simulation vs Engine Implementation

These APIs exist at two levels:

**1. LLM Simulation (in "software" — the LLM's head)**

The LLM can SIMULATE these protocols during conversation without any actual code:

```
User: "What interfaces does don-hopkins have?"

LLM thinks: "Let me simulate ls('don-hopkins/')..."
LLM responds: "don-hopkins/ has CHARACTER.yml (character), ROOM.yml (room), 
              and portrait.png (resource). It also has a memories/ child object."
```

The LLM "runs" queryInterface, ls, and navigation in its reasoning — no 
JavaScript needed. The YAML files ARE the program, the LLM IS the interpreter.

**2. Engine Implementation (actual utilities)**

The JS adventure engine and other simulators have concrete implementations:

```javascript
// engine.js — actual utility functions
function queryInterface(path, iid) { /* real file lookup */ }
function ls(path) { /* real fs.readdirSync + type inference */ }
function resolveParents(data) { /* real prototype chain walking */ }
```

**The protocols are the same. The implementations differ:**

| Protocol | LLM Simulation | Engine Implementation |
|----------|----------------|----------------------|
| `queryInterface` | LLM reasons about file existence | `fs.existsSync()` |
| `ls` | LLM lists known directory contents | `fs.readdirSync()` |
| `resource.read` | LLM recalls file contents | `fs.readFileSync()` |
| `parent lookup` | LLM walks prototype chain | `Object.assign()` merging |
| `_js` execution | LLM interprets intent | `eval()` or `new Function()` |

**Why this matters:**
- Design once, run anywhere (LLM or engine)
- LLM can prototype without code
- Engine can optimize for performance
- Same YAML files work for both
- Protocols are language-agnostic

### The Full Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│  SOURCE: Directory Tree + YAML Files                                │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  adventure-4/                                                │   │
│  │  ├── pub/ROOM.yml                                           │   │
│  │  ├── characters/don-hopkins/CHARACTER.yml                   │   │
│  │  └── ...                                                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  COMPILER: Python + LLM                                             │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  compile.py:                                                 │   │
│  │  - Walks directory tree (os.walk)                           │   │
│  │  - Reads YAML files (yaml.safe_load)                        │   │
│  │  - Emits events to LLM (found_room, found_condition, etc.)  │   │
│  │  - LLM generates _js from NL descriptions                    │   │
│  │  - LLM handles validation and linting                        │   │
│  │  - Writes back enriched YAML (with _js fields)              │   │
│  │  - Exports flattened JSON                                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  INTERMEDIATE: JSON Trees                                           │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  world.json:                                                 │   │
│  │  {                                                           │   │
│  │    "room": { "pub": {...}, "pub/bar": {...} },              │   │
│  │    "character": { "don-hopkins": {...} },                   │   │
│  │    "slideshow": { ... }                                      │   │
│  │  }                                                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  RUNTIME: JavaScript Engine                                         │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  engine.js:                                                  │   │
│  │  - Loads JSON trees into registry                           │   │
│  │  - Compiles _js strings to functions                        │   │
│  │  - Implements queryInterface, ls, navigation                │   │
│  │  - Runs game loop, handles player input                     │   │
│  │  - Optionally calls LLM for dynamic content                 │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

**The division of labor:**

| Component | Language | Role |
|-----------|----------|------|
| Source files | YAML + dirs | Human-editable, version-controlled |
| Compiler | Python | Tree walking, YAML parsing, JSON export |
| LLM | — | NL→JS translation, linting, event handling |
| Intermediate | JSON | Fast loading, type-free for JS |
| Runtime | JavaScript | Simulation, player interaction, UI |

**The runtime operates on JSON, not YAML:**
- JSON loads faster (no YAML parser needed)
- JSON is native to JavaScript
- Prototype chains pre-resolved during compilation
- `_js` strings ready to eval()

The directory tree and YAML files are the **source of truth**.
The JSON is a **compiled artifact** — regenerate it anytime.

### No Filesystem at Runtime

**Critical insight: The JS engine has NO actual Unix directories.**

At runtime, there's a JSON tree that **mirrors** the directory structure exactly:

```javascript
// What the engine actually sees — pure JSON, no fs calls
const world = {
  "pub": {
    "_path": "pub/",                    // Remembers its "directory"
    "_interfaces": ["room"],
    "name": "The Cozy Pub",
    "exits": { "north": "garden/", "down": "pub/basement/" },
    "_children": {
      "bar": { /* ... */ },             // Child "directories" are nested objects
      "basement": { /* ... */ },
      "kitchen": { /* ... */ }
    },
    "_resources": ["ambiance.mp3", "menu.pdf"],  // Resource list (not contents)
  },
  "pub/bar": {
    "_path": "pub/bar/",
    // ... flattened for fast lookup too
  }
};
```

**The JSON tree provides the same operations as the filesystem:**

| Filesystem | JSON Runtime |
|------------|--------------|
| `ls dir/` | `Object.keys(node._children)` |
| `cat dir/FILE.yml` | `node.fieldName` |
| `test -d dir/child` | `node._children.child !== undefined` |
| `dirname path` | `node._path.split('/').slice(0,-1).join('/')` |
| `readFile resource` | Fetch from CDN using `_path + resourceName` |

**Why this matters:**
- **Portable** — runs in browser, no Node.js fs needed
- **Fast** — no I/O, everything in memory
- **Cacheable** — JSON can be CDN-cached
- **Predictable** — no filesystem race conditions
- **Serializable** — save/restore game state trivially

**The directory structure is preserved semantically, not physically:**

```javascript
// queryInterface still works — it's just object property lookup
function queryInterface(path, iid) {
    const node = registry[path];
    if (!node) return null;
    if (iid === 'unknown') return node;
    return node._interfaces.includes(iid) ? node : null;
}

// ls still works — it's just Object.keys
function ls(path) {
    const node = registry[path];
    return [
        ...node._interfaces.map(i => ({ name: `${i.toUpperCase()}.yml`, kind: 'file', type: i })),
        ...node._resources.map(r => ({ name: r, kind: 'file', type: 'resource' })),
        ...Object.keys(node._children || {}).map(c => ({ name: c + '/', kind: 'dir', type: 'unknown' }))
    ];
}
```

**The filesystem is compile-time. The JSON tree is runtime.**
Same structure. Same semantics. Different substrate.

### Why This Matters

**In COM:** If `IRoom` and `ICharacter` need to share data, they go through 
the underlying C++ class. The implementation IS the shared state.

**In Selfish COM:** If `ROOM.yml` and `CHARACTER.yml` need to share data:
- They can reference each other: `resident: ./CHARACTER.yml`
- They can inherit from common parents
- They can read sibling files
- But there's NO hidden shared state — it's all explicit in files

```yaml
# ROOM.yml
name: Don's Home
owner: ./CHARACTER.yml#name        # Reference sibling
style:
  $inherit: ./CHARACTER.yml#style  # Inherit from sibling!
```

The "implementation" is distributed across files, each a live Self object,
connected by explicit references rather than hidden shared memory.

**COM gave us interface-based design.  
Self gave us prototypal inheritance.  
Selfish COM puts interfaces on top of prototypes, with a void at the center.**

### Unity GameObject/Component Parallel

Selfish COM is also surprisingly similar to **Unity's GameObject/Component** model:

| Unity | Selfish COM |
|-------|-------------|
| GameObject | Directory (unknown) |
| Component | Interface file (.yml) |
| Multiple Colliders | Multiple interface files |
| Transform component | Directory tree IS the transform |
| GetComponent<T>() | queryInterface(path, type) |
| AddComponent<T>() | Create new .yml file |
| Hierarchy panel | File explorer / `ls -R` |

**Unity's model:**
```
GameObject "Player"
├── Transform          ← required, links hierarchy
├── MeshRenderer       ← visual component
├── Rigidbody          ← physics component
├── BoxCollider        ← collision shape 1
├── SphereCollider     ← collision shape 2 (multiple!)
└── PlayerController   ← script component
```

Each Component:
- Has its own local data (position, velocity, mesh reference)
- Is aggregated BY the GameObject
- Can reference other components on same GameObject
- Lives in a Transform-based hierarchy tree

**Selfish COM's model:**
```
player/                     ← unknown = GameObject
├── CHARACTER.yml           ← character interface (auto-recognized)
├── INVENTORY.yml           ← inventory interface (auto-recognized)
├── COLLIDER-body.yml       ← collision shape 1 (needs type: collider)
├── COLLIDER-sword.yml      ← collision shape 2 (needs type: collider)
├── sprite.png              ← resource
└── equipment/              ← child object (sub-directory)
    ├── sword/
    │   └── OBJECT.yml
    └── shield/
        └── OBJECT.yml
```

### Multiple Interfaces of Same Type (Suffixed Files)

For multiple instances of the same interface (like Unity's multiple Colliders):

```yaml
# player/COLLIDER-body.yml
type: collider              # EXPLICIT type declaration required!
shape: capsule
height: 1.8
radius: 0.3
center: [0, 0.9, 0]

# player/COLLIDER-sword.yml  
type: collider              # Same type, different instance
shape: box
size: [0.1, 0.8, 0.1]
center: [0.5, 1.2, 0]
trigger: true               # Sword hitbox, not physics
```

**Naming convention:**
- Base name: `COLLIDER` (uppercase, conventional)
- Suffix: `-body`, `-sword`, `-001`, `-sphere` (anything descriptive)
- Full name: `COLLIDER-body.yml`

**Why explicit `type:` is required for suffixed files:**

| Filename | Auto-recognized? | `type:` needed? |
|----------|------------------|-----------------|
| `COLLIDER.yml` | Yes | No (inferred from filename) |
| `COLLIDER-body.yml` | No | Yes (`type: collider`) |
| `COLLIDER-001.yml` | No | Yes (`type: collider`) |
| `my-hitbox.yml` | No | Yes (`type: collider`) |

**We don't do filename alchemy.** The system only auto-recognizes canonical 
uppercase names (`ROOM.yml`, `CHARACTER.yml`, `COLLIDER.yml`). Anything with 
a suffix or non-standard name needs explicit `type:` declaration.

This keeps the linter simple — no regex parsing of filenames, no guessing.
If you want multiple colliders, you tell us what they are.

**Querying multiple interfaces:**
```javascript
// Get the canonical one (if it exists)
queryInterface('player/', 'collider')  // → player/COLLIDER.yml or null

// List ALL colliders (including suffixed)
listInterfaces('player/', 'collider')  // → ['COLLIDER.yml', 'COLLIDER-body.yml', ...]

// Or just read all files with type: collider
getAllOfType('player/', 'collider')    // Scans all .yml files for type field
```

**Key insight: The directory tree IS the hierarchy.**

Unity needs an explicit `Transform` component on every GameObject to link 
parent-child relationships. The Transform tree is SEPARATE from the GameObject 
containment — you manually parent/unparent things.

**In Selfish COM, the filesystem IS the transform tree:**
- Parent directory = parent object
- Child directory = child object
- No separate Transform component needed
- Hierarchy is automatic, implicit, always correct

### The Separation of Hierarchy and Transform

**Unity conflates two things in Transform:**
1. **Hierarchy** — parent/child relationships
2. **Spatial state** — position, rotation, scale

You can't have hierarchy without Transform. Every GameObject needs one.

**Selfish COM separates them cleanly:**

| Concern | Unity | Selfish COM |
|---------|-------|-------------|
| Hierarchy | Transform component | Directory tree (`unknown`) |
| Spatial state | Transform component | TRANSFORM.yml (optional!) |

**Hierarchy comes FREE with the `unknown` interface:**

```
player/                  ← queryInterface(null) returns this (identity)
├── CHARACTER.yml
└── equipment/           ← child object, automatic hierarchy
    └── sword/           ← grandchild, no Transform needed!
        └── OBJECT.yml
```

Every directory IS a node in the hierarchy. No interface needed. Just `ls` to 
enumerate children, `..` to get parent. The `unknown` interface gives you:
- Identity (the path)
- Children (subdirectories)
- Parent (`..`)
- Siblings (other items in parent)

**TRANSFORM.yml is ONLY for spatial state — no hierarchy info:**

```yaml
# player/TRANSFORM.yml
type: transform
position: [100, 50, 0]
rotation: [0, 0, 45]        # degrees — LOCAL, not world
scale: [1.5, 1.5, 1]
time_offset: 0              # for animation sequencing
time_scale: 1.0             # local time dilation
# NOTE: No parent/child fields! Hierarchy is the DIRECTORY TREE.
```

**This separation means:**
- A text adventure room doesn't need TRANSFORM.yml — it has no spatial position
- A 2D game entity can have TRANSFORM.yml with just x, y, rotation
- A 3D model can have full 3D transform
- Hierarchy exists regardless — it's the filesystem

```yaml
# room/ROOM.yml — no transform needed, hierarchy still works
name: The Pub
exits:
  north: ../garden/       # hierarchy navigation via paths
  down: ./basement/       # child object
```

The directory tree IS the scene graph. TRANSFORM.yml is just another interface 
for objects that need spatial data. Most objects don't.

**Unity aggregates through explicit component references:**
```csharp
// Unity: Components reference each other through GetComponent
var rb = GetComponent<Rigidbody>();
var col = GetComponent<BoxCollider>();
```

**Selfish COM aggregates through directory containment:**
```yaml
# player/CHARACTER.yml
name: Hero
equipment:
  weapon: ./equipment/sword/OBJECT.yml    # relative path to child
  armor: ./equipment/shield/OBJECT.yml
transform: ./TRANSFORM.yml                 # sibling interface
```

### What We Get From This

| Feature | Unity | COM | Selfish COM |
|---------|-------|-----|-------------|
| Multiple same-type | Yes (multi-collider) | No (one impl) | Yes (COLLIDER-*.yml) |
| Hierarchy | Transform tree | Manual | Directory tree |
| Component data | Instance fields | vtable slots | YAML fields |
| Hot reload | Limited | No | Yes (edit YAML) |
| Version control | Binary blobs | N/A | Git-friendly text |
| LLM readable | No | No | Yes |

**Unity's insight:** Composition over inheritance for game entities.  
**COM's insight:** Interface-based design for interop.  
**Self's insight:** Prototypes over classes.  
**Selfish COM:** All three, with directories as the universal aggregator.

---

## Two Levels of Operation: LLM as Eval AND Compiler

This architecture operates at (at least) two distinct levels:

### Level 1: LLM as Eval()

The Densmore-Rosenthal patent used **shell** as eval(). Smalltalk used **bytecode**. 
NeWS used **PostScript**. Traditional adventures used **parsers and scripting engines**.

We use the **LLM itself** as eval().

```
Shell script in file     → /bin/sh evaluates it
PostScript in dictionary → PS interpreter evaluates it
Smalltalk method         → VM evaluates it
Natural language in YAML → LLM evaluates it
```

The YAML files contain natural language descriptions that the LLM "executes" by 
understanding intent. No traditional parser needed — the LLM IS the interpreter.

```yaml
# The LLM reads this and KNOWS what to do
description: |
  A cramped control room filled with blinking monitors and tangled cables.
  The air smells of burnt coffee and desperation. A security panel on the
  wall has a card slot that looks important.
  
actions:
  examine_panel: |
    The panel has slots for three different security cards.
    Only the red ADMIN slot is currently active.
```

### Level 2: LLM as Compiler (NL → JS Translation)

But we don't ONLY interpret at runtime. The LLM also **compiles** natural language 
into executable JavaScript during the build phase.

### The Linter-as-Event-Emitter Pattern

Technically, the Python "compiler" is really a **linter** — it doesn't do the heavy 
lifting itself. It walks the directory tree and **emits events** (declarations) about 
what exists.

**All events contain repo-relative paths = object IDs:**

```
EVENT: found_object     id=street/lane-neverending/           # directory = unknown
EVENT: found_interface  id=street/lane-neverending/ROOM.yml   # interface file
EVENT: found_interface  id=characters/bob.yml                  # file object = interface
EVENT: found_exit       from=street/lane-neverending/ to=street/lane-neverending/acme-surplus/ dir=east
EVENT: found_condition  id=street/lane-neverending/ROOM.yml field=unlock_condition
EVENT: found_resource   id=street/lane-neverending/map.png    # non-YAML file
```

The repo-relative path IS the object identity:
- **Directory path** → object (queryInterface for `unknown`)
- **UPPERCASE.yml path** → interface on containing directory object
- **lowercase.yml path** → file object implementing single interface
- **Non-YAML path** → resource file (images, audio, etc.)

### Resource Management in Selfish COM

COM never handled resources well — you needed separate `.rc` files, resource compilers,
and `LoadResource()` APIs. Resources lived outside the object model.

**Selfish COM integrates resources as first-class object contents:**

```
don-hopkins/
├── CHARACTER.yml        # interface: character data
├── ROOM.yml            # interface: room this character owns
├── portrait.png        # resource: character portrait
├── voice-intro.mp3     # resource: audio greeting
├── signature.svg       # resource: autograph
└── README.md           # interface: documentation
```

**The `resource` interface:**

Any file can be queried for the `resource` interface — it returns the file path 
for raw read/write access. Directories return null (can't read a directory as bytes).

```javascript
function queryInterface(pointer, iid) {
    const objectPath = toObjectPath(pointer);
    
    // resource interface — any FILE can be read/written as bytes
    if (iid === 'resource') {
        return isFile(objectPath) ? objectPath : null;  // dirs can't be read as bytes
    }
    
    // unknown interface — works for both files and directories
    if (iid === null || iid === 'unknown') {
        return objectPath;
    }
    
    // ... rest of interface lookup
}

// Usage
queryInterface('don-hopkins/portrait.png', 'resource')
// → 'don-hopkins/portrait.png' (can read bytes)

queryInterface('don-hopkins/CHARACTER.yml', 'resource')
// → 'don-hopkins/CHARACTER.yml' (YAML is also readable as text)

queryInterface('don-hopkins/', 'resource')
// → null (directory — can't read as bytes)
```

**The `resource` interface virtualizes file operations:**

```javascript
// Resource interface methods (virtualized file I/O)
const resource = {
    read:   (path) => fs.readFileSync(path),           // GET contents
    write:  (path, data) => fs.writeFileSync(path, data), // PUT contents (replace)
    edit:   (path, patch) => applyPatch(path, patch),  // PATCH contents (modify)
    delete: (path) => fs.unlinkSync(path),             // DELETE file
    exists: (path) => fs.existsSync(path),             // HEAD check
    stat:   (path) => fs.statSync(path),               // metadata
};
```

This means EVERY file implements at least TWO interfaces:
- `unknown` — identity (the path itself)
- `resource` — virtualized read/write/edit/delete

YAML files implement THREE:
- `unknown` — identity
- `resource` — raw text I/O (read/write/edit/delete)
- `{type}` — structured interface (room, character, etc.)

**Resources are:**
- Co-located with the object that owns them
- Version-controlled alongside interfaces
- Discoverable by directory listing
- No separate resource compiler or manifest needed

The filesystem IS the resource manager. `ls` IS `EnumResources()`.

```
COM: LoadResource(hModule, MAKEINTRESOURCE(IDB_PORTRAIT))
Us:  fs.readFile(`${objectPath}/portrait.png`)
```

Self eliminated classes. We eliminated resource compilers.

The LLM reads these events and looks up **event handlers** in a separate directory.
The handlers are natural language instructions telling the LLM what to do:

```yaml
# handlers/compile/found_condition.yml
instruction: |
  When you see a natural language condition, generate a JavaScript arrow function
  that implements the same logic. Use ctx.player for player state, ctx.world for
  world flags, ctx.room for current room. Return boolean.
  
  Write the result to {field}_js adjacent to the original field.
```

### Visitor Pattern via Handler Directories

This IS the Visitor pattern — you can point the linter at **different directories 
of event handlers** to get completely different behaviors:

```
handlers/
├── compile/           # NL → JS translation handlers
│   ├── found_condition.yml
│   ├── found_action.yml
│   └── found_magic.yml
├── validate/          # Consistency checking handlers
│   ├── found_exit.yml     # "verify target room exists"
│   ├── found_item.yml     # "verify item is defined somewhere"
│   └── found_character.yml
├── export/            # JSON generation handlers
│   ├── found_room.yml
│   └── found_character.yml
├── document/          # README generation handlers
│   └── found_room.yml     # "generate room documentation"
└── visualize/         # Graph generation handlers
    └── found_exit.yml     # "add edge to room graph"
```

**Same linter, different handlers, different behaviors:**

```bash
# Compile: translate NL to JS
python lint.py --handlers=handlers/compile adventure-4/

# Validate: check consistency
python lint.py --handlers=handlers/validate adventure-4/

# Export: generate JSON
python lint.py --handlers=handlers/export adventure-4/

# Document: generate READMEs
python lint.py --handlers=handlers/document adventure-4/
```

The linter just **declares what exists**. The handlers (NL instructions to the LLM) 
decide **what to do about it**. Separation of traversal from behavior.

### The Compilation Pipeline (Refined)

```
┌─────────────────────────────────────────────────────────────────────┐
│  LINTING (Python walks tree, emits events)                          │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ lint.py: "I found ROOM.yml at path X with exits Y, Z..."    │   │
│  │          "I found condition field with NL value..."          │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │ events
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  HANDLER LOOKUP (LLM reads NL instructions)                         │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ handlers/compile/found_condition.yml:                        │   │
│  │ "Generate JS arrow function from this NL description..."     │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │ LLM executes handler
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  OUTPUT (LLM writes results)                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ YAML updated with _js fields, or JSON exported, or           │   │
│  │ validation errors reported, or docs generated...             │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

**The key insight: You can SEE the translation.**

```yaml
# BEFORE: Human writes natural language
unlock_condition: |
  Player has the red admin card AND has not triggered the alarm.

# AFTER: LLM compiles, BOTH are visible in the YAML
unlock_condition: |
  Player has the red admin card AND has not triggered the alarm.
unlock_condition_js: |
  (ctx) => ctx.player.hasItem('red-admin-card') && !ctx.world.flags.alarm_triggered
```

This creates **parallel bilingual code** — the natural language intent sits right 
next to the compiled JavaScript. Debuggable. Auditable. Human-readable.

### The Full Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│  AUTHORING (Human + LLM in Cursor)                                  │
│  ┌─────────────┐                                                    │
│  │ YAML + NL   │  ← Human writes natural language descriptions     │
│  └─────────────┘                                                    │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  COMPILATION (Python + LLM)                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐             │
│  │ compile.py  │ → │ LLM transl. │ →  │ YAML + _js  │             │
│  │ walks dirs  │    │ NL → JS     │    │ (both vis.) │             │
│  └─────────────┘    └─────────────┘    └─────────────┘             │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  EXPORT (Python)                                                    │
│  ┌─────────────┐                                                    │
│  │ JSON world  │  ← Flattened for JS engine consumption            │
│  │ JSON chars  │                                                    │
│  └─────────────┘                                                    │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  RUNTIME (JS Engine)                                                │
│  ┌─────────────┐    ┌─────────────┐                                │
│  │ engine.js   │ ← │ eval(_js)   │  ← Executes compiled closures  │
│  │ simulation  │    │ closures    │                                │
│  └─────────────┘    └─────────────┘                                │
└─────────────────────────────────────────────────────────────────────┘
```

### What Gets Compiled to `_js`?

The LLM translates these natural language fields into executable JavaScript:

| NL Field | Compiled Field | Purpose |
|----------|----------------|---------|
| `unlock_condition` | `unlock_condition_js` | Exit gates, door locks |
| `score_condition` | `score_condition_js` | Point triggers |
| `visible_when` | `visible_when_js` | Conditional visibility |
| `available_when` | `available_when_js` | Action availability |
| `on_enter` | `on_enter_js` | Room entry effects |
| `on_examine` | `on_examine_js` | Object examination |
| `magic` | `magic_js` | Arbitrary game logic |

### Why Both Levels?

**Level 1 (LLM as Eval)** handles:
- Understanding player intent ("look at the weird blinking thing")
- Generating dynamic descriptions
- NPC dialogue and personality
- Emergent situations not pre-scripted

**Level 2 (LLM as Compiler)** handles:
- Deterministic game logic (scoring, gates, flags)
- Performance-critical paths (don't call LLM every frame)
- Auditable behavior (see exactly what code runs)
- Offline operation (compiled JS needs no LLM)

The **NL stays in the YAML** so:
- Humans can read and modify intent
- LLM can re-compile if logic needs updating
- Debugging shows BOTH intent and implementation
- Version control tracks changes to both

---

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

## Prior Art and Inspiration

### The Densmore-Rosenthal Patent (1991)

**US Patent 5187786A** — *"Method for apparatus for implementing a class hierarchy 
of objects in a hierarchical file system"*

Owen M. Densmore and David S. H. Rosenthal, Sun Microsystems, filed 1991-04-05.

This patent describes implementing Smalltalk-style OOP using Unix filesystem and shell:
- Directories represent classes and class instances
- Files within directories contain methods (shell scripts)
- PATH files encode inheritance chains
- Message sending via shell: `SEND aF001 methodA args`
- Supports `Self` and `Super` pseudo-classes

**Key parallel to Directory-as-Object:**
- Directory = object identity
- Files = interface implementations (methods/data)
- Path lookup = inheritance/method resolution

The patent predates our work by 35 years and establishes the core insight.

### The Hyatt Palo Alto Napkin Session

Tom Stambaugh (C2 Wiki) describes the moment of inspiration:

> *"Owen and I discussed his 'crazy' idea at a poolside table at the now-demolished 
> Hyatt Palo Alto, on El Camino. I told him that it made sense to me, we scribbled 
> furiously on napkins, and I helped him see how he might adopt some learnings from 
> Smalltalk. It was one of those afternoons that could only have happened at that 
> time in that place in that culture."*  
> — Tom Stambaugh, wiki.c2.com

### Warnock's Linguistic Motherboard

Owen Densmore recalled John Warnock's vision for PostScript:

> *"PostScript is a linguistic 'mother board', which has 'slots' for several 'cards'. 
> The first card we (Adobe) built was a graphics card. We're considering other cards. 
> In particular, we've thought about other network services, such as a file server card."*  
> — John Warnock to Owen Densmore, Adobe (circa 1985)

This "pluggable slots" concept directly influenced NeWS and maps to our 
interface-file architecture: the directory is the motherboard, interface files 
are the cards.

### NeWS object.ps

Densmore's `object.ps` implemented OOP in PostScript for NeWS using:
- PostScript dictionaries as objects/classes
- Dictionary stack for dynamic scoping (like our path-based lookup)
- Multiple inheritance and prototype-based specialization

All NeWS UI toolkits were built on this system. The same patterns appear in 
Directory-as-Object but using YAML files instead of PostScript dictionaries.

### The Lineage

```
Smalltalk (Xerox PARC, 1970s)
    ↓
Self (Ungar & Smith, 1986) — eliminated classes
    ↓
NeWS object.ps (Densmore, 1986) — OOP in PostScript
    ↓
Densmore-Rosenthal Patent (1991) — OOP in Unix filesystem
    ↓
COM/OLE (Microsoft, 1990s) — interface-based design
    ↓
Selfish COM (2026) — Self + COM for LLMs
```

### References

- Patent: https://patents.google.com/patent/US5187786A/en
- Tom Stambaugh quote: http://wiki.c2.com/?ForthPostscriptRelationship
- Owen Densmore paper: "Object Oriented Programming in NeWS" (Monterey '86)
- Don Hopkins archive: https://donhopkins.com/home/archive/NeWS/

---

*Inspired by Don Box's "Essential COM", David Ungar's Self, and Densmore & Rosenthal's 
1991 patent. COM gave us interface-based design. Self showed us we don't need classes.
Densmore showed us the filesystem IS the object graph.  
Selfish COM — filesystem-native, human-readable, and LLM-friendly.*
