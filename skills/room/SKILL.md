---
name: room
description: "Rooms are intertwingled navigable activation context maps. Entering = calling. Exiting = returning."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [card, adventure, memory-palace, character, world-generation, data-flow, naming]
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
├── ROOM.yml        # Room definition
├── README.md       # Room's voice (optional)
├── CARD.yml        # Card sidecar (optional)
├── character-*.yml # NPCs embedded in room
├── object-*.yml    # Objects in room
├── inbox/          # Objects thrown INTO this room
├── outbox/         # Objects staged to throw OUT
└── nested-room/    # Sub-room
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
