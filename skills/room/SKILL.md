---
name: room
description: "Directories as navigable cognitive spaces with activation context. Maps filesystem structure to rooms with exits, regions, objects, inventories, and spatial coordinates. Use when navigating worlds, creating rooms, managing spatial layouts, or building data-flow pipelines between directory nodes."
license: MIT
allowed-tools: "read_file, write_file"
metadata:
  tier: 1
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
  name: "The Gezelligheid Grotto Pub"
  
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

## Vehicles: Portable Rooms

A **vehicle** is a room with `is_vehicle: true` — embark, drive, disembark. Includes Logo-style turtle navigation (RIDE, FORWARD, RIGHT) and Sims-style pie menu interactions where objects advertise scored actions.

| Command | Effect |
|---------|--------|
| `EMBARK vehicle` | Enter the vehicle room |
| `DRIVE direction` | Move vehicle and occupants |
| `DISEMBARK` | Exit to current world location |

**Lineage:** Papert's Logo turtle, Don Hopkins' Pie Menus, Will Wright's SimAntics.

## Data Flow: Throwing Objects Through Exits

Rooms are **processing nodes**. Throw objects through exits — they land in `inbox/`. Stage outgoing items in `outbox/`.

| Command | Effect |
|---------|--------|
| `THROW obj exit` | Toss object through exit |
| `INBOX` / `NEXT` | List or process waiting items |
| `STAGE obj exit` / `FLUSH` | Stage and send outgoing items |

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

Objects contain other objects to arbitrary depth. Address with paths: `backpack/toolbox/wrench`, `./relative`, `../sibling`. Tag items with `@tag` for search across containers.

## Room Graph Navigator

`ZOOM OUT` to see the whole world graph. `ZOOM IN room` to enter. `LINK a TO b` to create connections. Navigate the structure while editing — like Rocky's Boots.

## Speed of Light: Multi-Agent in One Call

Simulate multiple agents together in ONE LLM call — instant cross-talk instead of isolated agent prisons. Like The Sims: one frame simulates all characters with instant interaction. See [speed-of-light/](../speed-of-light/) for full protocol.

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

> **Full specification:** [TOPOLOGY.yml](./TOPOLOGY.yml)

The eight-direction compass maps to **two types of connections**:

| Direction | Type | Function |
|-----------|------|----------|
| N/S/E/W | Cardinal | Navigate to major rooms (spiderweb) |
| NW/NE/SW/SE | Diagonal | Expand into storage grids (quadrants) |

**4 ways OUT** (navigation) + **4 quadrants IN** (infinite storage) = **Unlimited worlds**

Grid naming: `{quadrant}-{x}-{y}` (e.g., `ne-2-3` = 2 east, 3 north in NE)

See: [exit skill](../exit/) for PIE-MENU-TOPOLOGY protocol, [memory-palace/](../memory-palace/) for Method of Loci

## Codebase as Navigable World

Directories are rooms. Files are objects. Functions are chambers you can enter.

```yaml
# Location paths with line numbers
location: "@central/apps/insights/pyleela/brain/Schema.py:142"

# Path syntax
- @repo/path/to/file.py       # file in repo
- @repo/path/to/file.py:42    # specific line
- @repo/path/dir/             # directory (room)
```

See [character/](../character/) for party-based code review, README.md for detailed examples.

## NPC Embedding Patterns

| Pattern | When | Example |
|---------|------|---------|
| `cat-name.yml` | Embedded NPC | `pub/cat-terpie.yml` |
| `name/CHARACTER.yml` | Complex character | `characters/don-hopkins/` |
| `staff-name.yml` | Role-based grouping | `pub/staff-marieke.yml` |

See [naming/](../naming/) for conventions.

## Rooms as Logistic Containers

Rooms participate in a **logistics network** (Sims + Factorio unification). Rooms advertise needs with attractiveness scores, items route to highest-scoring requester, and bots or belts move items physically. Supports stacking (fungible counts or individual instances) and grid cells for warehouse patterns.

See [logistic-container/](../logistic-container/) and [factorio-logistics-protocol.md](../../designs/factorio-logistics-protocol.md) for full specification.

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
