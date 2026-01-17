# Sims Object Model → MOOLLM

> *Objects, Properties, Categories, Interactions*
> *Every YAML file is a Sims object.*

## The Object Philosophy

In The Sims, *everything* was an object: toilets, beds, phones, food, even abstract concepts like jobs and relationships. Objects had:
- **Properties** — state values
- **Interactions** — things you could do with them
- **Categories** — groupings for organization
- **Placement rules** — where they could exist

MOOLLM inherits this completely. Every `.yml` file is an object. Every directory is a container. Every skill advertises interactions.

---

## Object Properties

**Sims:** Objects had typed properties:

| Property | Type | Example |
|----------|------|---------|
| `dirty` | int (0-100) | Toilet cleanliness |
| `broken` | bool | Stove malfunction |
| `value` | int | Purchase price |
| `comfort` | int | How comfy a chair is |
| `fun` | int | Entertainment value |

**MOOLLM:** YAML properties are semantic:

```yaml
# pub/bar/bartender.yml
properties:
  mood: cheerful
  expertise: cocktails
  shift: evening
  tips_earned: 47.50
  
# pub/furniture/cozy-chair.yml
properties:
  comfort: high
  capacity: 1
  style: worn-leather
  occupied_by: null
```

No strict types — the LLM understands "high" comfort vs numeric scales.

---

## GUIDs

**Sims:** Every object class had a GUID (Globally Unique Identifier):

```
GUID: 0x00001234  // Standard toilet
GUID: 0x00001235  // Fancy toilet
```

**MOOLLM:** File paths ARE identifiers:

```
pub/bar/bartender.yml     # Unique identity
pub/arcade/pinball.yml    # Different object
skills/bartender/         # Skill prototype
```

No need for numeric GUIDs — the filesystem provides unique addressing.

---

## Object Categories

**Sims:** Objects belonged to categories for catalog organization:

| Category | Examples |
|----------|----------|
| Seating | Chairs, sofas, benches |
| Surfaces | Tables, counters, desks |
| Appliances | Stove, fridge, dishwasher |
| Electronics | TV, computer, stereo |
| Plumbing | Toilet, sink, shower |
| Decorations | Paintings, plants, rugs |

**MOOLLM:** Directory structure IS categorization:

```
pub/
├── bar/              # Bar-related objects
│   ├── taps.yml
│   └── stools.yml
├── arcade/           # Entertainment objects
│   ├── pinball.yml
│   └── jukebox.yml
├── kitchen/          # Food preparation
│   └── stove.yml
└── furniture/        # Seating, surfaces
    ├── cozy-chair.yml
    └── pie-table.yml
```

Categories emerge from organization, not metadata.

---

## Function Tables

**Sims:** Objects had "function tables" — which standard functions they supported:

| Function | Purpose |
|----------|---------|
| Init | Object creation |
| Main | Idle behavior |
| Clean | When cleaned |
| Repair | When fixed |
| Prepare Food | Cooking surfaces |
| Wash Hands | Sinks |

**MOOLLM:** `CARD.yml` advertised methods:

```yaml
# pub/kitchen/stove.yml
id: pub-stove
inherits_from: skills/appliance

advertised_methods:
  COOK:
    description: "Prepare food"
    satisfies: [hunger]
    requires: ingredients
    
  CLEAN:
    description: "Scrub the surfaces"
    satisfies: [environment]
    
  REPAIR:
    description: "Fix broken burners"
    requires: repair_skill >= 3
```

Same concept: objects declare what they can do.

---

## Multi-Tile Objects

**Sims:** Large objects spanned multiple tiles:

```
┌─────────────────┐
│  GRAND PIANO    │
│  (3x2 tiles)    │
│  ○ ←sit here    │
└─────────────────┘
```

Properties included:
- **Footprint** — which tiles occupied
- **Interaction slots** — where Sims stand/sit
- **Blocking** — what tiles are impassable

**MOOLLM:** Objects with spatial extent:

```yaml
# pub/pie-table.yml
spatial:
  footprint: large  # LLM understands scale
  seats: 8
  positions:
    - id: head
      role: facilitator
    - id: seat-1
      occupant: null
    - id: seat-2
      occupant: palm
    # ...
```

Or with URL-addressable positions:

```yaml
# Addressable as pub/pie-table.yml#seat-3
positions:
  seat-3:
    occupant: maurice
    facing: center
```

---

## Portable Objects

**Sims:** Some objects could be picked up and carried:

| Object | Carryable | Two-Handed |
|--------|-----------|------------|
| Book | Yes | No |
| Baby | Yes | Yes |
| Pizza box | Yes | Yes |
| Refrigerator | No | — |

**MOOLLM:** Inventory and portability:

```yaml
# Object definition
portable: true
size: small  # fits in pocket
carry_mode: one_hand

# Or for larger items
portable: true
size: large
carry_mode: two_hands
requires: strength >= 3
```

The [inventory](../skills/inventory/) skill manages what characters carry.

---

## Object Placement Constraints

**Sims:** Objects had placement rules:

| Rule | Example |
|------|---------|
| Surface required | Lamp needs table |
| Floor only | Toilet can't go on table |
| Wall-mounted | Painting needs wall |
| Outdoors only | Pool can't be inside |
| Level constraint | Stairs span two floors |

**MOOLLM:** ROOM.yml placement:

```yaml
# pub/bar/ROOM.yml
placement_zones:
  counter:
    allows: [glasses, taps, bottles]
    height: counter
    
  floor:
    allows: [stools, standing_characters]
    height: ground
    
  wall:
    allows: [mirror, signs, decorations]
```

And objects declare their needs:

```yaml
# decorations/neon-sign.yml
placement:
  requires: wall
  zone: wall
  height: eye_level
```

---

## Object Initialization

**Sims:** Objects ran "Init" trees when placed:

```
Init Tree:
  Set dirty = 0
  Set broken = FALSE
  Register with room
  Play placement sound
```

**MOOLLM:** Object templates with defaults:

```yaml
# skills/appliance/CARD.yml (template)
default_state:
  condition: new
  cleanliness: 100
  last_used: null
  
on_create:
  - register_with_room
  - announce: "A new {type} appears!"
```

When you create `pub/kitchen/new-blender.yml`, it inherits these defaults.

---

## Object Slots

**Sims:** Objects defined "slots" — positions for interaction:

```
Slot 0: "sit" position (chair seat)
Slot 1: "use" position (in front of chair)
Slot 2: "talk_to" position (beside chair)
```

**MOOLLM:** Interaction positions in YAML:

```yaml
# pub/furniture/cozy-chair.yml
slots:
  sit:
    capacity: 1
    grants: [comfort_buff, rest_action]
    
  approach:
    for: interaction
    distance: adjacent
    
  converse:
    for: social
    facing: seat_occupant
```

---

## Standard Heights

**Sims:** Objects existed at standard heights:

| Height | Value | Examples |
|--------|-------|----------|
| Ground | 0 | Rugs, pets |
| Low table | 1 | Coffee tables |
| Table | 2 | Dining tables |
| Counter | 3 | Kitchen counters |
| Hand | 4 | Carried objects |
| Sitting | 5 | People in chairs |
| Standing | 6 | People standing |

**MOOLLM:** Heights as semantic levels:

```yaml
# Room height zones
heights:
  floor: [rugs, pets, dropped_items]
  low: [coffee_table, ottoman]
  table: [dining_surface, desk]
  counter: [bar_counter, kitchen_counter]
  eye_level: [mirror, artwork]
  ceiling: [chandelier, fan]
```

The LLM understands "put it on the table" vs "put it on the floor."

---

## Surfaces & Containment

**Sims:** Surfaces could hold objects:

```
Counter → holds → Plate → holds → Food
Table → holds → Lamp
```

**MOOLLM:** Directories ARE containment:

```
pub/bar/counter/
├── taps.yml           # On the counter
├── tip-jar.yml        # On the counter
└── menu-stand.yml     # On the counter

pub/bar/counter/tip-jar.yml:
  contains:
    - coins: 3.50
    - note: "Thanks Marieke!"
```

Files in directories are "on" that surface. YAML contains property is "inside."

---

## The Object Lifecycle

**Sims:**
```
Create → Init → Idle → Interact → Degrade → Repair/Replace → Delete
```

**MOOLLM:**
```yaml
lifecycle:
  created: 2026-01-09
  state: active
  degradation:
    cleanliness: -1/day
    condition: -0.1/use
  
  events:
    - 2026-01-08: cleaned by Marieke
    - 2026-01-07: used by Palm
```

State tracked in YAML, history in comments.

---

## Missing Objects Protocol

**Sims:** The game handled missing objects gracefully:

> "Loading and Saving — Missing Objects"

If a saved game referenced a deleted object, the game:
1. Logged the missing reference
2. Substituted a placeholder
3. Continued loading

**MOOLLM:** [Postel's Law](../skills/postel/) for missing files:

```yaml
# If referenced file doesn't exist
response: graceful_degradation
  - log: "Referenced object not found: {path}"
  - substitute: generic_placeholder
  - continue: true
```

The LLM can work around missing objects by inferring from context.

---

## Draw Groups

**Sims:** Objects had draw groups for rendering order:

```
Draw Group 1: Floor tiles
Draw Group 2: Rugs
Draw Group 3: Furniture
Draw Group 4: Objects on furniture
Draw Group 5: Sims
Draw Group 6: Effects
```

**MOOLLM:** Description ordering in prose:

The LLM naturally describes scenes in logical order — setting, then furnishings, then characters, then actions. No explicit draw groups needed.

---

## Object vs. Skill

**Sims:** Objects contained behavior (SimAntics trees).
**MOOLLM:** Objects *reference* skills (CARD.yml inheritance).

```yaml
# pub/bar/bartender.yml
inherits_from: skills/bartender
personality: marieke  # Overrides from character

# The skill defines behaviors
# The object instantiates them
# The character provides personality
```

Separation of:
- **What** it can do → skill
- **Where** it is → directory
- **Who** it is → character properties

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface) — CARD.yml as object interface
- [skills/room/](../skills/room/) — Room and containment
- [sims-portable-objects.md](./sims-portable-objects.md) — Carrying, inventory, containment
- [sims-simantics-vm.md](./sims-simantics-vm.md) — Object behaviors
- [sims-find-best-action.md](./sims-find-best-action.md) — Object advertisements

---

*"Objects Object Properties Relationship Matrix Strings... Single Tile Objects Multi Tile Objects Object Categories Object Placement Constraints Object Function Tables"*

The object model is the world model. MOOLLM inherits it all.
