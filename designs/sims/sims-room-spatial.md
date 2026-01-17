# Sims Rooms & Spatial System → MOOLLM

> *Room Scoring, Routing, Portals, Levels*
> *Space shapes behavior.*

## Space as Game Mechanic

In The Sims, space wasn't just backdrop — it was active game mechanic:
- **Room score** affected mood
- **Routing** determined what was reachable
- **Portals** connected spaces
- **Privacy** varied by location

MOOLLM inherits this through ROOM.yml and directory structure.

---

## Room Scoring

**Sims:** Every room had a "room score" based on:

| Factor | Effect |
|--------|--------|
| Lighting | +10 per lamp |
| Windows | +15 natural light |
| Art | +5 to +50 per piece |
| Plants | +10 per plant |
| Dirty objects | -10 per mess |
| Broken objects | -15 per break |
| Size | Bigger = better |

Room score directly affected the **Room motive**:
- Score < 20: depressing
- Score 20-50: neutral  
- Score 50-80: pleasant
- Score > 80: luxurious

**MOOLLM:** Room atmosphere in ROOM.yml:

```yaml
# pub/ROOM.yml
atmosphere:
  lighting: warm, amber
  decor: eclectic, lived-in
  plants: many
  art: local artists, rotating
  
  overall: welcoming
  
  mood_effects:
    - comfort: +moderate
    - social: +high (when populated)
    - stress: -moderate
```

The LLM understands "this is a nice room" without numeric scoring.

---

## Room Types

**Sims:** Rooms had implicit types based on contents:

| Type | Key Objects | Behavioral Effects |
|------|-------------|-------------------|
| Bedroom | Bed, dresser | Sleep here |
| Bathroom | Toilet, shower | Hygiene here |
| Kitchen | Stove, fridge | Cook here |
| Living room | Sofa, TV | Socialize here |
| Study | Desk, bookshelf | Work here |

**MOOLLM:** Room types in ROOM.yml:

```yaml
# pub/bar/ROOM.yml
type: bar
purpose: drinks, socializing

# pub/stage/palm-nook/study/ROOM.yml
type: study
purpose: writing, contemplation

# pub/stage/palm-nook/rest/ROOM.yml  
type: bedroom
purpose: sleep, recovery
```

---

## Routing

**Sims:** Pathfinding determined accessibility:

```
Route from (0,0) to (10,5):
  - Check for blocked tiles
  - Check for closed doors
  - Calculate shortest path
  - Reserve path tiles
  - Walk the path
```

Routing failures caused frustration:
- "Can't reach" → action cancelled
- Crowded paths → waiting
- Locked doors → social drama

**MOOLLM:** Navigation through exits:

```yaml
# pub/ROOM.yml
exits:
  north:
    to: street
    type: door
    state: open_during_hours
    
  stage:
    to: pub/stage/
    type: step_up
    always: open
    
  bar:
    to: pub/bar/
    type: counter
    access: staff_only_behind
```

The LLM understands "Palm can go to the stage but not behind the bar."

---

## Portals

**Sims:** Portal objects connected spaces:

| Portal Type | Function |
|-------------|----------|
| Door | Standard room connection |
| Archway | Open passage |
| Stairs | Connect levels |
| Ladder | Vertical access |
| Diving board | Pool entry |

**MOOLLM:** Exits as portals:

```yaml
# pub/ROOM.yml
exits:
  cellar:
    to: pub/cellar/
    type: trapdoor
    visibility: hidden
    requires: knowledge_of_existence
    
  maze:
    to: maze/entrance/
    type: archway
    description: "An ominous opening..."
```

---

## Multi-Level Spaces

**Sims:** Houses had levels (floors):

```
Level 2: Upstairs (bedrooms)
    ↕ connected by stairs
Level 1: Ground (living areas)
    ↕ connected by basement stairs
Level 0: Basement (utilities)
```

Objects could span levels (stairs, spiral staircases).

**MOOLLM:** Directory hierarchy as levels:

```yaml
pub/
├── ROOM.yml         # Ground floor (main pub)
├── cellar/          # Below (accessed by trapdoor)
│   └── ROOM.yml
├── stage/           # Raised platform (sub-room)
│   └── palm-nook/   # Private space on stage
│       ├── study/   # Work area
│       ├── rest/    # Sleep area
│       └── gym/     # Exercise area
```

Subdirectories can represent:
- Different levels (up/down)
- Sub-regions (within same level)
- Private spaces (nested zones)

---

## Routing Slots

**Sims:** Objects defined where Sims could stand:

```
Object: Stove
  Slot 0: (0, -1) // in front, for cooking
  Slot 1: (1, 0)  // side, for passing
  Slot 2: (-1, 0) // other side
```

Multiple Sims queued for slots.

**MOOLLM:** Interaction positions:

```yaml
# pub/pie-table.yml
positions:
  facilitator:
    at: head
    role: leads_discussion
    
  seat-1:
    at: right-of-head
    occupant: null
    
  standing:
    at: perimeter
    role: observer
    capacity: many
```

---

## Standard Heights

**Sims:** Objects existed at standard heights:

```
HEIGHT_GROUND = 0    // Rugs, pets
HEIGHT_TABLE = 2     // Table surfaces
HEIGHT_COUNTER = 3   // Counter height
HEIGHT_SITTING = 5   // Chair seat
HEIGHT_STANDING = 6  // Adult eye level
```

This enabled proper stacking:
- Lamp ON table
- Plate ON counter
- Cat ON chair

**MOOLLM:** Height zones in ROOM.yml:

```yaml
# pub/bar/ROOM.yml
height_zones:
  floor:
    contains: [stools, dropped_items, cats]
    
  counter:
    height: bar_height
    contains: [taps, glasses, tip_jar]
    
  back_bar:
    height: eye_level
    contains: [bottles, mirrors, signs]
```

---

## Surfaces

**Sims:** Surfaces could hold objects:

```
Table (surface = true, height = TABLE)
  └── Lamp
  └── Book
  └── Plate
      └── Food
```

Surface capacity was limited by footprint.

**MOOLLM:** Containment in YAML:

```yaml
# pub/bar/counter/taps.yml
location: on_counter
contains:
  handles: [ipa, lager, stout, cider]
  
# Or via directory structure
pub/bar/counter/
├── taps.yml
├── tip-jar.yml
└── menu-stand.yml
```

---

## Room Privacy

**Sims:** Rooms had privacy levels:

| Privacy | Examples | Effects |
|---------|----------|---------|
| Public | Living room | All actions OK, witnesses common |
| Semi-private | Bedroom | Some actions restricted, family OK |
| Private | Bathroom | Intimate actions, solo preferred |

**MOOLLM:** Privacy in ROOM.yml:

```yaml
# pub/bar/cat-cave/ROOM.yml
privacy:
  level: high
  access: [cats, biscuit_exception]
  
  witnessing:
    - outsiders_cannot_see_in
    - behaviors_here_are_private
```

See [Ethical Framing Inheritance](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#ethical-framing-inheritance).

---

## Terrain

**Sims:** Outdoor terrain affected routing:

| Terrain | Effect |
|---------|--------|
| Grass | Normal speed |
| Path | Faster |
| Water | Impassable (or pool) |
| Hills | Slower |

**MOOLLM:** Terrain as room property:

```yaml
# maze/dark-room/ROOM.yml
terrain:
  surface: stone
  lighting: none
  hazards: [grues]
  
  movement:
    requires: light_source
    speed: slow
```

---

## Room Connections

**Sims:** Rooms connected through doorways:

```
Living Room ←→ Kitchen ←→ Dining Room
     ↕              ↕
  Hallway    ←→  Stairs
     ↕              ↕
  Front Door      Bedroom
```

Each connection could be:
- Open (archway)
- Closable (door)
- Lockable (privacy)

**MOOLLM:** Full connection graph:

```yaml
# maze/entrance/ROOM.yml
exits:
  north: maze/crossroads/
  south: pub/
  
# Implicitly creates bidirectional connection
# Unless one-way is specified
```

---

## Room Scoring Calculation

**Sims:** Formula for room score:

```python
room_score = 0
for obj in room.objects:
    if obj.is_light:
        room_score += 10
    if obj.is_art:
        room_score += obj.art_value
    if obj.is_dirty:
        room_score -= 10
    if obj.is_broken:
        room_score -= 15

room_score += room.size * 0.5
room_score += room.windows * 15

return clamp(room_score, 0, 100)
```

**MOOLLM:** Semantic room assessment:

```yaml
# pub/stage/palm-nook/ROOM.yml
assessment:
  lighting: natural from stage + desk lamp
  personalization: high (typewriters, books, art)
  cleanliness: tidy
  comfort: cozy
  
  overall: "A warm, personal creative space"
```

The LLM evaluates holistically, not arithmetically.

---

## Upstairs/Downstairs

**Sims:** Levels had implications:

| Level | Typically Contains | Privacy |
|-------|-------------------|---------|
| Ground | Public spaces | Low |
| Upstairs | Bedrooms | High |
| Basement | Utilities, secrets | Variable |
| Attic | Storage, mysteries | High |

**MOOLLM:** Level semantics:

```yaml
# pub/cellar/ROOM.yml
location:
  level: basement
  access: staff_only
  
atmosphere:
  lighting: dim
  purpose: storage
  secrets: maybe
```

---

## The Spatial Grammar

**Sims:** Space communicated function:

```
Front Door → Foyer → Living Room → Kitchen
                 ↓
              Stairs → Private Rooms
```

This grammar taught players:
- Public spaces near entrance
- Private spaces require navigation
- Utilities near bedrooms

**MOOLLM:** Directory structure as grammar:

```
pub/
├── ROOM.yml          # Main public space
├── bar/              # Service area
│   └── cat-cave/     # Hidden private
├── stage/            # Performance
│   └── palm-nook/    # Private (earned)
├── maze/             # Adventure (separate)
└── kitchen/          # Back of house
```

The structure teaches: what's public, what's private, what requires journey.

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#ethical-framing-inheritance) — Room inheritance
- [skills/room/](../skills/room/) — Room building
- [skills/adventure/](../skills/adventure/) — Spatial navigation
- [maze/](../examples/adventure-4/maze/) — Complex spatial example
- [pub/](../examples/adventure-4/pub/) — Multi-zone room

---

*"Room Scoring Terrain Water Pools Setting Up Lots Levels (upstairs/downstairs) Stairs Multi Tile Objects spanning levels"*

Space is not backdrop. Space is gameplay.
