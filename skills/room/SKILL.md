---
name: room
description: "Rooms are intertwingled navigable activation context maps. Entering = calling. Exiting = returning."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [card, container, exit, object, memory-palace, adventure, character, data-flow, multi-presence, plain-text]
tags: [moollm, navigation, space, directory, moo, adventure]
---

# Room

> **Rooms are intertwingled navigable activation context maps. Entering = calling. Exiting = returning.**

Directories as cognitive spaces where [cards](../card/) come to life.

## The Metaphor

| Filesystem | Simulation | Programming |
|------------|------------|-------------|
| Directory | Room | Stack frame |
| `cd room/` | Enter | Function call |
| `cd ..` | Exit | Return |
| Files in dir | Active entities | Local variables |
| Links | Exits/doors | Calls to other functions |

## Room Anatomy

```
room-name/
├── ROOM.yml        # Room definition (REQUIRED!)
├── README.md       # Room's voice (optional)
├── CARD.yml        # Card sidecar (optional)
├── character-*.yml # NPCs embedded in room
├── object-*.yml    # Objects in room
├── inbox/          # Objects thrown INTO this room
├── outbox/         # Objects staged to throw OUT
├── region/         # Sub-region of this room
│   └── ROOM.yml    # Region must also declare itself!
└── nested-room/    # Full sub-room (different location)
    └── ROOM.yml
```

---

## Regions vs Sub-Rooms

### What's a Region?

A **region** is a sub-directory that represents a **portion of the same room** — like the stage area of the pub, or the back corner of a library.

```yaml
# pub/ROOM.yml
room:
  name: "The Rusty Lantern Pub"
  
  # Regions are PARTS of this room
  regions:
    stage:
      path: "stage/"
      description: "The performance stage"
      visibility: public
      
    back-room:
      path: "back-room/"
      description: "Private back room"
      visibility: private
      requires: "bartender approval"
      
    bar:
      path: "bar/"
      description: "The bar counter area"
```

### Regions Have Rules

Each region can have its own:

```yaml
# pub/back-room/ROOM.yml
room:
  name: "Back Room"
  type: region                    # Marks as region, not full room
  parent: "../"                   # Part of parent room
  
  # Access control
  access:
    visibility: private           # Not visible to everyone
    requires: "bartender approval OR staff badge"
    who_allowed:
      - "characters/staff/*"
      - "player if has_flag('vip_access')"
    who_denied:
      - "characters/troublemakers/*"
      
  # Ethics & behavior
  rules:
    - "No recording"
    - "Confidential conversations"
    - "Staff only by default"
    
  # Privacy
  privacy:
    eavesdropping: false          # Can't hear from outside
    visible_from_parent: false    # Can't see inside from pub
    
  # What happens in the back room...
  narrative:
    on_enter: "The door closes behind you with a soft click."
    on_exit: "You return to the bustling pub."
```

### Visibility Types

| Type | Description |
|------|-------------|
| `public` | Anyone can see and enter |
| `visible` | Can see but may need permission to enter |
| `private` | Hidden unless you know about it |
| `secret` | Hidden AND requires discovery |

### Region vs Full Sub-Room

| Feature | Region | Sub-Room |
|---------|--------|----------|
| Part of parent? | Yes | No |
| Own identity? | Partial | Full |
| Exit returns to? | Parent | Varies |
| Shares parent context? | Yes | No |
| Type field | `type: region` | `type: room` |

---

## Directory Type Declaration

### The Rule

**Every directory in an adventure MUST declare what it is.**

| Directory Type | Declaration File |
|----------------|------------------|
| Room | `ROOM.yml` |
| Region | `ROOM.yml` (with `type: region`) |
| Character | `CHARACTER.yml` |
| Adventure root | `ADVENTURE.yml` |
| Personas | `ROOM.yml` (with `type: personas`) |
| Storage | `ROOM.yml` (with `type: storage`) |

### Lint Error: Undeclared Directory

```yaml
# LINT ERROR: Directory without type declaration
- type: MISSING_TYPE_DECLARATION
  severity: WARNING
  path: "pub/mysterious-corner/"
  message: "Directory has no ROOM.yml, CHARACTER.yml, or other type declaration"
  suggestion: "Add ROOM.yml with appropriate type field"
```

### Valid Non-Room Directories

Some directories aren't rooms and that's OK:

```yaml
# These don't need ROOM.yml:
messages/           # Mail storage (system)
inbox/              # Postal inbox (system)
outbox/             # Postal outbox (system)
sessions/           # Session logs (meta)
images/             # Asset storage (meta)
```

### Marking System Directories

```yaml
# Alternative: mark as system directory
# pub/messages/.meta.yml
meta:
  type: system
  purpose: "Mail storage for pub"
  requires_room_yml: false
```

### Container Directories (Inheritance Scopes)

Some directories are **inheritance containers** — they provide shared properties to child rooms without being navigable themselves. Like OpenLaszlo's `<node>` element.

```yaml
# maze/CONTAINER.yml — Not a room, but defines inherited properties
container:
  name: "The Twisty Maze"
  description: "Groups maze rooms with shared grue rules"
  
  inherits:
    is_dark: true
    is_dangerous: true
    grue_rules:
      can_appear: true
      
  ambient:
    sound: "dripping water"
    light_level: 0
```

All child rooms (`room-a/`, `room-b/`, etc.) automatically inherit these properties!

Alternatively, you can make the container into an actual room:

```yaml
# maze/ROOM.yml — The maze entrance IS a room
room:
  name: "Maze Entrance"
  description: "Dark passages branch off in every direction..."
  
  exits:
    a: room-a/
    b: room-b/
    # ... etc
```

**DESIGN CHOICE:**
- Use `CONTAINER.yml` if you want inheritance without navigation (see [container skill](../container/))
- Use `ROOM.yml` if you want the directory to be a navigable space

### Hierarchy Example

```
adventure-4/
├── ADVENTURE.yml           # Adventure declaration
├── pub/
│   ├── ROOM.yml            # Room declaration
│   ├── stage/
│   │   └── ROOM.yml        # Region (type: region)
│   ├── bar/
│   │   └── ROOM.yml        # Region
│   ├── back-room/
│   │   └── ROOM.yml        # Private region
│   └── messages/
│       └── .meta.yml       # System directory (no ROOM.yml needed)
├── characters/
│   ├── ROOM.yml            # Hall of characters (type: personas)
│   └── don-hopkins/
│       └── CHARACTER.yml   # Character declaration
└── maze/
    ├── ROOM.yml            # Room declaration
    └── room-a/
        └── ROOM.yml        # Sub-room (full room, not region)
```

## ROOM.yml Structure

```yaml
room:
  name: "Debug Session"
  purpose: "Hunt down the authentication bug"
  
  context:
    - "Bug: Login fails with valid credentials"
    - "Suspected: Session cookie handling"
    
  cards_in_play:
    - instance: "goblin-001"
      card: "Git Goblin"
      goal: "Find when bug was introduced"
      
  working_set:
    - "ROOM.yml"
    - "state/progress.yml"
    
  exits:
    parent: "../"
    related: "../feature-work/"
    
  # Optional: position in 2D world-space
  world_position:
    x: 5
    y: 12
    
  # Optional: objects with positions in room-space
  objects:
    - name: "workbench"
      position: {x: 3, y: 7}
```

## Spatial Coordinates

Rooms can exist in **world-space**. Objects can have positions in **room-space**.

```yaml
# World-space: where is this room in the world?
world_position:
  x: 5
  y: 12

# Room-space: where are objects within this room?
objects:
  - name: "workbench"
    position: {x: 3, y: 7}
```

Navigation can use coordinates:
- `NORTH` from (5,12) → find room at (5,13)
- Named exits override coordinates

**Not all rooms need coordinates.** Abstract spaces can exist outside world-space.

## Vehicles: Portable Rooms That Move

A **vehicle** is a room you can embark, drive, and disembark.

```yaml
# vehicle-tent.yml
room:
  name: "Research Tent"
  is_vehicle: true
  world_position: {x: 5, y: 12}  # Changes when you drive
```

| Command | Effect |
|---------|--------|
| `EMBARK tent` | Enter the vehicle room |
| `DISEMBARK` | Exit to current world location |
| `DRIVE NORTH` | Move vehicle (and occupants) to (5,13) |

### Riding the Turtle

**RIDE the turtle.** Move around the room, draw on the floor, jump through doors:

```
> RIDE turtle
You mount the turtle. The world scrolls beneath you.

> FORWARD 100
The turtle moves forward. A red line appears on floor.svg.

> RIGHT 90
> FORWARD 50
You're near the door-north.

> ENTER door-north
You jump through the door INTO the next room.
The turtle comes with you.
```

```yaml
# turtle.yml — a vehicle within room-space
turtle:
  position: {x: 100, y: 100}
  heading: 90  # degrees, 0 = north
  pen_down: true
  pen_color: "#e94560"
  rider: "the-explorer"
```

| Command | Effect |
|---------|--------|
| `RIDE turtle` | Mount the turtle, move with it |
| `FORWARD 50` | Move forward, draw if pen down |
| `RIGHT 90` | Turn right |
| `ENTER door` | Jump through door to connected room |
| `INTO subroom` | Descend into nested sub-room |
| `ZOOM OUT` | See the room graph navigator |

**Lineage:** Papert's Logo turtle, Rocky's Boots (1982), Robot Odyssey (1984).

### Snap Cursor & Pie Menus

When you approach an object, the cursor **snaps** to it and shows a **pie menu** of scored actions:

```
        EXAMINE (80)
           ╱
 REPAIR ──●── USE (95) ← default
           ╲
        TAKE (20)
```

**This IS The Sims interaction model:**
- Objects **advertise** their available actions
- Actions are **scored** based on context, needs, state
- High-scoring actions appear prominently

**Lineage:** Don Hopkins' [Pie Menus](https://en.wikipedia.org/wiki/Pie_menu) + Will Wright's SimAntics.

## Cursor as Vehicle: Direct Manipulation

The cursor **carries tools** and applies them to the room floor:

```
> SELECT pen-tool
Cursor now carries: 🖊️ pen (red)

> CLICK workbench
*snap* Cursor at workbench. Pen ready.

> DRAG to door-north
Drawing line from workbench to door-north...
Line added to floor.svg
```

| Tool | Icon | Action |
|------|------|--------|
| `pen` | 🖊️ | Draw lines on floor |
| `eraser` | 🧽 | Remove drawings |
| `selector` | 👆 | Pick up and move objects |
| `linker` | 🔗 | Draw connections between objects |
| `stamper` | 📌 | Place copies of cards |

## Throwing Objects: Data Flow Programming

**Throw objects through exits.** They pile up on the other side.

```
> THROW blueprint door-north
Throwing blueprint through door-north...
blueprint landed in assembly/inbox/
```

### Inbox / Outbox

```
room/
  inbox/           # Objects thrown INTO this room land here
    task-001.yml
  outbox/          # Stage objects before throwing OUT
    result-001.yml
```

| Command | Effect |
|---------|--------|
| `THROW obj exit` | Toss object through exit |
| `INBOX` | List waiting items |
| `NEXT` | Process next item (FIFO) |
| `STAGE obj exit` | Add to outbox |
| `FLUSH` | Throw all staged objects |

### Rooms as Pipeline Stages

Each room is a **processing node**. Exits are **edges**. Thrown objects are **messages**.

```yaml
# Document processing pipeline:
uploads/          # Raw files land here
  inbox/
parser/           # Extract text
  script: parse.py
analyzer/         # LLM analyzes  
  prompt: "Summarize and extract entities"
output/           # Final results collect here
```

**This is Kilroy-style data flow:** rooms as nodes, files as messages, the filesystem as the network.

## Inventories

Characters carry **inventories** — portable rooms always with them.

```yaml
# character/inventory/
sword.card
map.yml
notes/
  finding-001.md
```

| Command | Effect |
|---------|--------|
| `GET sword` | Pick up from room → inventory |
| `DROP map` | Put from inventory → room |
| `GIVE torch TO companion` | Transfer to another character |
| `INVENT` | List what you're carrying |

**Your inventory IS a pocket dimension.**

## Nested Containers

Objects can contain other objects, to arbitrary depth:

```
> PUT screwdriver IN toolbox
> PUT toolbox IN backpack
> OPEN backpack
backpack contains:
  - toolbox (3 items)
  - sandwich
```

### Object Paths

Address nested objects with paths:

```
> EXAMINE backpack/toolbox/wrench
> USE inventory/potions/healing
> TAKE ../chest/gold FROM here
```

Path syntax:
- `container/sub/item` — absolute within scope
- `./toolbox/wrench` — relative to current
- `../sibling/item` — parent's sibling
- `/repo-name/path` — multi-repo addressing

### Tags for Search

```
> TAG wrench @favorite
> SEARCH backpack @tool
Found in backpack:
  toolbox/screwdriver [@tool]
  toolbox/wrench [@tool @favorite]
```

## Room Graph Navigator

**ZOOM OUT** to see the whole world:

```
> ZOOM OUT
│  ROOM GRAPH: moollm-palace              │
│       [room] [card] [chat]              │
│         │                               │
│      [★ YOU ARE HERE]                   │

> LINK room TO card
Connection created. You can now JUMP directly.
```

| Command | Effect |
|---------|--------|
| `ZOOM OUT` | See room graph overview |
| `ZOOM IN room` | Enter selected room |
| `LINK a TO b` | Create connection between rooms |

**Like Rocky's Boots:** Navigate the structure. Edit while exploring.

## Speed of Light vs Carrier Pigeons

> **Traditional multi-agent**: Each agent in isolation. One LLM call per agent. Communication by carrier pigeon. **Slow. Expensive. Sad.**

> **MOOLLM**: Simulate as many agents together as possible in ONE LLM call. Communication at the speed of light. Multiple simulation steps per iteration.

```yaml
# In one LLM iteration:
simulation:
  - step: 1
    papert-001: "Microworlds need low floors"
    kay-001: "Yes! Like Smalltalk for children"
    
  - step: 2
    papert-001: 
      responds_to: kay-001
      says: "Exactly! Accessible entry, unlimited ceiling"
      
  - step: 3
    synthesis:
      emerged: "Low floor + high ceiling + prototypes = MOOLLM"
```

Three characters, three steps, instant cross-talk — **ONE LLM call**.

### This IS The Sims

```
The Sims: One frame, all Sims simulated, instant interaction
MOOLLM:   One call, all cards simulated, instant messaging
```

Instead of isolated agent prisons, we have a **shared microworld**.

## Room Navigation

| Action | What Happens |
|--------|--------------|
| **Enter** | Push room's working_set to context |
| **Exit** | Pop context, return to parent |
| **Look** | Read ROOM.yml and README.md |
| **Activate card** | Clone card template into room |
| **Complete card** | Card writes return_value, can be removed |

## Nested Rooms (Virtual Zones)

Rooms can contain rooms (subdirectories) or **virtual zones** (no physical directory):

```yaml
# cat-cave.yml — TARDIS-like nested room
id: cat-cave
type: [room, furniture]  # Both!

zones:  # Virtual sub-rooms
  nap-zone:
    description: "Sunny spot, cushions everywhere"
    path: "pub/cat-cave/nap-zone"  # Virtual path
  box-jungle:
    description: "Cardboard paradise"
    path: "pub/cat-cave/box-jungle"
```

Characters reference virtual zones:

```yaml
# cat-terpie.yml
home: pub/cat-cave/
location: pub/cat-cave/nap-zone  # Virtual zone
```

## Room Relationships

Rooms can remember visitors:

```yaml
relationships:
  don-hopkins:
    visits: 3
    reputation: "regular"
    memory: "Always nice to the cats"
```

## Home vs Location Protocol

Entities have **home** (where file lives) and **location** (where they are):

```yaml
character:
  home: pub/cat-cave/terpie.yml     # File never moves
  location: pub/                     # Currently in pub
```

Movement updates `location`, not file. See [character/](../character/).

## Pie Menu Room Topology

The eight-direction compass maps to **two types of connections**:

```
           N (navigate)
           ↑
    NW ←───●───→ NE
   (grid)  ↑   (grid)
           │
    W ←────┼────→ E
(navigate) │  (navigate)
           │
    SW ←───●───→ SE
   (grid)  ↓   (grid)
           S (navigate)
```

### Cardinal Directions: Spiderweb Navigation

**N/S/E/W** = Major room links, branching "out" or "away"

```yaml
exits:
  n: ../great-hall/      # Major room north
  s: ../cellar/          # Major room south
  e: ../garden/          # Major room east
  w: ../kitchen/         # Major room west
```

These form the **spiderweb** — sparse, long-distance connections between major locations.

### Diagonal Directions: Grid Quadrants

**NW/NE/SW/SE** = Corner links to expandable sub-room grids

```yaml
exits:
  ne: ne/ne-1-1/         # Corner of northeast grid
  nw: nw/nw-1-1/         # Corner of northwest grid
  se: se/se-1-1/         # Corner of southeast grid
  sw: sw/sw-1-1/         # Corner of southwest grid
```

Each diagonal opens into an **infinite storage quadrant**:

```
        NE QUADRANT GRID
        
    ne-1-4 ─── ne-2-4 ─── ne-3-4
       │          │          │
    ne-1-3 ─── ne-2-3 ─── ne-3-3
       │          │          │
    ne-1-2 ─── ne-2-2 ─── ne-3-2
       │          │          │
    ne-1-1 ─── ne-2-1 ─── ne-3-1
       │
       └────── connects to main room (sw exit)
```

### Grid Room Naming

```
{quadrant}-{x}-{y}

ne-1-1 = closest northeast room (grid corner)
ne-3-4 = 3 east, 4 north in NE quadrant
sw-2-2 = 2 west, 2 south in SW quadrant
```

### Directory Structure

```
wizard-study/
├── ROOM.yml              # Main room (pie menu center)
├── nw/                   # Northwest quadrant
│   ├── nw-1-1/ROOM.yml   # Grid corner (connects to main)
│   ├── nw-2-1/ROOM.yml   # One east
│   └── nw-1-2/ROOM.yml   # One north
├── ne/                   # Northeast quadrant
├── sw/                   # Southwest quadrant
└── se/                   # Southeast quadrant
```

### Grid Room Auto-Linking

Grid rooms have 8-direction exits to adjacent cells:

```yaml
# ne/ne-2-3/ROOM.yml
room:
  name: "Storage NE-2-3"
  grid_position: { quadrant: ne, x: 2, y: 3 }
  
  exits:
    n: ../ne-2-4/    # y+1
    s: ../ne-2-2/    # y-1
    e: ../ne-3-3/    # x+1
    w: ../ne-1-3/    # x-1
    ne: ../ne-3-4/   # x+1, y+1
    nw: ../ne-1-4/   # x-1, y+1
    se: ../ne-3-2/   # x+1, y-1
    sw: ../ne-1-2/   # x-1, y-1
```

Corner rooms (x=1, y=1) have a special exit back to main:

```yaml
# ne/ne-1-1/ROOM.yml (corner room)
room:
  is_grid_corner: true
  exits:
    sw: ../../       # Back to main room!
    n: ../ne-1-2/
    e: ../ne-2-1/
    ne: ../ne-2-2/
```

### The Metaphor: Outside and Inside

| Direction | Type | Metaphor | Function |
|-----------|------|----------|----------|
| N/S/E/W | Cardinal | "Outside" / Highways | Navigate to other major rooms |
| NW/NE/SW/SE | Diagonal | "Inside" / Frontage roads | Expand into storage grids |

**4 ways OUT** (navigation) + **4 quadrants IN** (infinite storage) = **Unlimited worlds**

### Grid Connectivity Modes

Grids in quadrants can be **continuous** or **private**:

```yaml
# CONTINUOUS: One big grid shared between quadrants
grid_mode: continuous
# nw-4-1 connects to ne-1-1 (wrap around)
# All four quadrants form one unified grid

# PRIVATE: Each quadrant has isolated grid  
grid_mode: private
# nw grid has no connection to ne grid
# Four separate storage areas
```

**Sparse grids are valid!** You don't need every cell:

```yaml
# Sparse grid — only rooms that exist
wizard-study/ne/
├── ne-1-1/     # Corner room (required)
├── ne-2-1/     # Exists
├── ne-5-3/     # Exists (gap is fine!)
└── ne-10-1/    # Far out on X axis
# Missing rooms = impassable
# Like real buildings along a road
```

### Grid Numbering Conventions

```yaml
grid_rules:
  no_negatives: true        # Always positive coordinates
  zero_reserved: true       # 0 = the highway (N/S/E/W web)
  one_one_adjacent: true    # 1-1 is always next to center
  rotationally_symmetric: true
  
  addressing: |
    Grid coords are POSITIVE and RELATIVE to quadrant.
    This means you can rename 'nw/' to 'sw/' and the
    internal links still work — just rotated!
    
  metaphor: |
    N/S/E/W = STREETS (travel between intersections)
    Intersection = Current room (where streets cross)
    Diagonal quadrants = BUILDINGS you ENTER
    Grid interior = Building floors/rooms
    
    The whole grid is a CITY:
    - Cardinals = Travel along streets
    - Diagonals = Enter buildings at corners
    - City blocks fill the four quadrants
```

### 🏙️ The Urban Planning Metaphor

**Grid rooms are CITY BLOCKS at street intersections!**

```
           N (street north)
           ↑
    ┌──────┼──────┐
    │  NW  │  NE  │  ← BUILDINGS you ENTER
    │ 🏭   │  📦  │    (warehouses, factories)
W ──┼──────●──────┼── E (streets east/west)
    │  📦  │  🚚  │    
    │  SW  │  SE  │  ← BUILDINGS you ENTER
    └──────┼──────┘
           ↓
           S (street south)
```

| Urban Element | MOOLLM Element | Action |
|---------------|----------------|--------|
| **Streets** | Cardinal exits (N/S/E/W) | TRAVEL along them |
| **Intersection** | Current room | WHERE YOU ARE |
| **Buildings** | Diagonal quadrants | ENTER them |
| **Building Floors** | Grid cells | Navigate INSIDE |

Example: **Fooblitzky-style city** (streets with buildings):

```
     N (street north)
     │
  ┌──┴──────────────────┐
  │ 🏢 nw-1-3  nw-2-3   │  NW Building
  │    │       │        │  (floors inside)
  │ 🏢 nw-1-2  nw-2-2   │
  │    │       │        │
  │ 🏢 nw-1-1──nw-2-1───┼── to NE building
  └─────────────────────┘
     │
     ●  (YOU ARE HERE — intersection)
     │
  W ─┴─ E (streets)
```

### Relative Addressing for Portability

```yaml
# All grid exits use relative paths:
exits:
  n: ../ne-2-4/    # Up one Y
  e: ../ne-3-3/    # Right one X
  sw: ../../       # Back to main (corner room only)

# This means:
# 1. Copy nw/ dir, rename to se/
# 2. Search-replace "nw-" with "se-"  
# 3. Grid still works! Just rotated 180°
```

### Memory Palace Application

- **Cardinal rooms** = Major memory palace locations (palaces)
- **Grid quadrants** = Detail storage (shelves, drawers, niches)
- **Sparse grids** = Only memorable items get rooms
- **Navigate with N/S/E/W**, store details in NW/NE/SW/SE

See: [Pie Menus](https://en.wikipedia.org/wiki/Pie_menu), [Method of Loci](../memory-palace/), [Fooblitzky](https://en.wikipedia.org/wiki/Fooblitzky)

## Codebase as Navigable World

Modern IDEs like Cursor can mount multiple repositories. Each repository becomes a navigable world:

**Directories are Rooms:**
```
@central/apps/insights/pyleela/brain/
├── Schema.py           # The Schema Chamber
├── Action.py           # The Action Hall  
├── World.py            # The World Atrium
├── Item.py             # The Item Vault
└── DijkstraPlanner.py  # The Planning Room
```

**Files are Objects with Chambers:**

A file is an object you can examine. Functions within are **chambers** you can enter:

```
> examine Schema.py
Schema.py contains:
  - class Schema (line 18)
    - __init__ (line 22)
    - createSyntheticItemIfNeeded (line 163)

> enter createSyntheticItemIfNeeded
You are now in the createSyntheticItemIfNeeded chamber.
This function implements Drescher's synthetic item creation...
```

**Location Paths with Line Numbers:**

Characters can be "at" a specific line in a file:

```yaml
location: "@central/apps/insights/pyleela/brain/Schema.py:142"
# Character is examining line 142 of Schema.py
```

Path syntax for code:
- `@repo/path/to/file.py` — file in mounted repo
- `@repo/path/to/file.py:42` — specific line
- `@repo/path/to/file.py:42-67` — line range
- `@repo/path/dir/` — directory (room)

**Links in Cards:**

Connect skills to code artifacts:

```yaml
as_room:
  artifacts:
    - schema-mechanism: "@central/apps/insights/pyleela/brain/"
    - task-queue: "@central/tools/edgebox/scripts/ingest.py"
```

See [character/](../character/) for party-based code review.

## NPC Embedding Patterns

| Pattern | When | Example |
|---------|------|---------|
| `cat-name.yml` | Embedded NPC | `pub/cat-terpie.yml` |
| `name/CHARACTER.yml` | Complex character | `characters/don-hopkins/` |
| `staff-name.yml` | Role-based grouping | `pub/staff-marieke.yml` |

See [naming/](../naming/) for conventions.

## Rooms ARE Logistic Containers!

### The Unification: Sims + Factorio

Rooms can participate in a **logistics network**:

| Feature | Source | MOOLLM |
|---------|--------|--------|
| Action advertisements | The Sims | Objects advertise what they DO |
| Item requests | Factorio | Containers advertise what they NEED |
| Attractiveness scores | Both | Higher score = higher priority |

### Room Logistics Mode

```yaml
room:
  name: "The Kitchen"
  
  logistics:
    mode: requester              # passive-provider, requester, buffer...
    request_list:
      - tags: ["ingredient"]
        count: 10
        priority: high
```

### Logistic Advertisements

Rooms advertise their NEEDS with attractiveness scores:

```yaml
logistic_advertisements:
  
  NEED_INGREDIENTS:
    description: "Kitchen needs ingredients"
    wants:
      - tags: ["ingredient"]
        count: 10
    score: 70                    # Base priority
    score_if: "chef_is_cooking"  # When to boost
    score_bonus: 30              # Total 100 when cooking!
    
  DESPERATELY_NEED_LIGHT:
    wants:
      - tags: ["light-source"]
        count: 1
    score: 100                   # Very high!
```

### Stacking in Rooms

Rooms can have stacks of items:

```yaml
room:
  name: "Armory"
  
  stacks:
    # Fungible (just count)
    arrow: 500
    bolt: 300
    
    # Instance (individual state)
    magic-sword:
      count: 3
      instances:
        - { id: flame-blade, damage: 50 }
        - { id: frost-edge, damage: 45 }
        
  stack_limit: 1000
```

### Grid Room Cells

Warehouse rooms can be grid cells:

```yaml
room:
  name: "Iron Ore Storage"
  type: grid-cell
  
  grid_cell:
    enabled: true
    parent: "../"
    coordinates: { x: 2, y: 3 }
    item_type: iron-ore
    
  stacks:
    iron-ore: 2500
```

### The Flow

```
1. ROOMS advertise logistic needs with scores
2. LOGISTICS ENGINE collects all advertisements
3. Items route to HIGHEST-SCORING requester
4. BOTS or BELTS move items physically
5. ROOM receives items, fires on_item_added
```

See [logistic-container/](../logistic-container/) and [factorio-logistics-protocol.md](../../designs/factorio-logistics-protocol.md).

---

## The Philosophy

> **Spatial navigation IS cognitive navigation.**

When you "enter" the debug-session room:
- Your context shifts to debugging
- Relevant cards are already in play
- The room's knowledge is loaded
- You know where the exits lead

## Live Examples

- [examples/adventure-3/pub/](../../examples/adventure-3/pub/) — A room with NPCs
- [examples/adventure-3/pub/cat-cave/](../../examples/adventure-3/pub/cat-cave/) — Nested room with zones

## Dovetails With

### Sister Skills
- [card/](../card/) — Cards **live** in rooms
- [memory-palace/](../memory-palace/) — Memory Palace IS Room + mnemonic intent
- [adventure/](../adventure/) — Adventure IS Room + narrative framing
- [data-flow/](../data-flow/) — Rooms as processing nodes
- [speed-of-light/](../speed-of-light/) — Multi-agent instant communication

### Kernel
- [kernel/context-assembly-protocol.md](../../kernel/context-assembly-protocol.md) — Working set loading
