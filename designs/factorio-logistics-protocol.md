# Factorio Logistics Protocol for MOOLLM Adventures

> **Design Session**: January 10, 2026  
> **Inspiration**: Factorio's logistic network → MOOLLM item flow  
> **Key Insight**: "throw ball north" is putting an item on a conveyor belt!
> **Urban Insight**: Grid rooms are CITY BLOCKS at street intersections!

---

## The Revelation

**Don Hopkins slaps the table!**

> "Exits are CONVEYOR BELTS! Rooms are LOGISTIC CHESTS!  
> NPCs are LOGISTIC BOTS! Objects are INSERTERS!  
> The whole placement protocol is FACTORIO!"

---

## The Mapping

| Factorio Concept | MOOLLM Equivalent | Description |
|-----------------|-------------------|-------------|
| **Conveyor Belt** | Exit with `flow` | One-way transport of items between rooms |
| **Inserter** | Object with `simulate` | Picks items, places them elsewhere |
| **Logistic Chest** | Container with `chest_mode` | Storage with network behavior |
| **Logistic Bot** | NPC/Character | Autonomous item carrier |
| **Splitter** | Exit with `placement_rules` | Routes items by type |
| **Circuit Network** | Events/Signals | Conditional control flow |
| **Assembler** | Object with recipes | Transforms inputs → outputs |

---

## Chest Modes (Container Behaviors)

Just like Factorio's colored chests:

```yaml
container:
  name: "The Kitchen Counter"
  chest_mode: passive-provider    # Items here are available to the network
  
# CHEST MODES (Factorio Colors!)
#
# PASSIVE-PROVIDER (Yellow)
#   "Take from me if you need it"
#   - Items here are available to requesters
#   - Items won't leave unless requested
#   - Example: Pantry with food
#
# ACTIVE-PROVIDER (Red)  
#   "I'm pushing these OUT"
#   - Items here actively seek destinations
#   - Auto-routes to matching requester or storage
#   - Example: Mailbox outbox, production output
#
# REQUESTER (Blue)
#   "I WANT these items"
#   - Pulls items from providers
#   - Specifies what it wants with request_list
#   - Example: Recipe station needing ingredients
#
# STORAGE (Yellow variant)
#   "General overflow"
#   - Accepts anything the network can't place
#   - Low priority for retrieval
#   - Example: Storage closet, warehouse
#
# BUFFER (Green)
#   "Hold until needed"
#   - Like storage but higher priority for bots
#   - Staging area
#   - Example: Workbench surface, loading dock
#
```

### Passive Provider (Yellow)

```yaml
container:
  name: "The Pantry"
  chest_mode: passive-provider
  
  # "I have these, take if needed"
  provides:
    - tags: ["food", "ingredient"]
  
  # Don't let the last one leave!
  reserve: 1    # Always keep at least 1 of each
```

### Active Provider (Red)

```yaml
container:
  name: "Factory Output"
  chest_mode: active-provider
  
  # "These items want to LEAVE"
  push_to:
    - match: { tags: ["finished"] }
      destination: warehouse/
    - match: { tags: ["mail"] }
      destination: "#mailbox"
    - default: storage/    # Overflow
```

### Requester (Blue)

```yaml
container:
  name: "Workbench"
  chest_mode: requester
  
  # "I NEED these items"
  request_list:
    - item: "iron-ingot"
      count: 5
      min: 2           # Request more when below this
    - item: "copper-wire"
      count: 10
    - tags: ["fuel"]
      count: 1
```

### Buffer (Green)

```yaml
container:
  name: "Loading Dock"
  chest_mode: buffer
  
  # Staging area — items pause here
  buffer_for:
    - destination: ship/cargo-hold/
      when: "ship.docked == true"
```

---

## Conveyor Belts (Exit Flow)

Exits can have automatic item flow, not just player movement:

```yaml
exit:
  direction: NORTH
  destination: ../factory/
  
  # CONVEYOR BELT BEHAVIOR
  
  flow:
    enabled: true                    # Items flow automatically
    direction: outbound              # outbound | inbound | bidirectional
    speed: 1                         # Items per turn
    
    # Filters — only these items flow
    allow:
      - tags: ["raw-material"]
      - tags: ["fuel"]
    deny:
      - tags: ["finished-product"]   # These go the other way!
    
    # Belt can be full
    capacity: 5                      # Max items in transit
    
    # Visual
    appearance: "conveyor-belt"      # For rendering
    color: "yellow"                  # Belt tier (yellow < red < blue)
```

### Bidirectional Flow (Two Lanes!)

Like Factorio's two-lane belts:

```yaml
exit:
  direction: EAST
  destination: ../assembly/
  
  flow:
    enabled: true
    direction: bidirectional
    
    # Lane A: Inputs going IN
    lane_a:
      direction: outbound
      allow: [{ tags: ["ingredient"] }]
      
    # Lane B: Products coming OUT  
    lane_b:
      direction: inbound
      allow: [{ tags: ["product"] }]
```

---

## Inserters (Objects That Move Things)

Objects with `simulate` that act like inserters:

```yaml
object:
  id: robot-arm
  name: "Robotic Arm"
  emoji: "🦾"
  
  type: inserter
  
  # What it picks from
  input:
    source: "../belt-a/"
    filter: { tags: ["component"] }
    
  # Where it puts things  
  output:
    destination: "#assembler"
    place_where: "in"
    
  # Behavior
  simulate: |
    Each turn:
      If input has matching item AND output has space:
        Pick 1 item from input
        Place in output
        emit "The arm transfers a component."
```

### Long-Arm Inserter (Cross-Room!)

```yaml
object:
  id: teleport-inserter
  name: "Long-Range Inserter"
  emoji: "🔮"
  
  type: inserter
  range: 2    # Can reach 2 rooms away!
  
  input:
    source: "../../warehouse/raw-materials/"
    filter: { tags: ["ore"] }
    
  output:
    destination: "../smelter/#input-hopper"
```

### Stack Inserter (Batch Transfer)

```yaml
object:
  id: stack-arm
  name: "Stack Inserter"
  
  type: inserter
  stack_size: 12    # Moves 12 at once!
  
  input:
    source: "#storage"
    filter: { id: "iron-plate" }
    
  output:
    destination: "../train-cargo/"
```

---

## Logistic Bots (NPCs as Carriers)

Characters can be logistic robots!

```yaml
character:
  id: delivery-bot
  name: "Courier Kitten"
  emoji: "🐱📦"
  species: kitten
  
  behavior:
    type: logistic-bot
    
    # Home base — where it rests
    roboport: pub/#charging-station
    
    # What it carries
    cargo_slots: 3
    
    # How it operates
    ai: |
      Each turn:
        If cargo is empty:
          Find nearest active-provider with items
          Travel there, pick up items
        If cargo has items:
          Find matching requester
          Travel there, deliver items
        If idle:
          Return to roboport
          
    # Range (rooms it can reach)
    range: 5    # Max rooms from roboport
```

### Personal Logistics (Player as Bot)

The PLAYER can participate in the network:

```yaml
player:
  id: player
  
  # Player IS a logistic bot with special powers
  logistics:
    personal_requests:
      - item: "torch"
        count: 1
        priority: high
      - tags: ["food"]
        count: 3
        priority: low
        
    # Bots will deliver TO player!
    can_receive: true
    delivery_zone: 2    # Bots can deliver within 2 rooms
```

---

## Splitters (Exit Routing)

Exits that split flow based on item properties:

```yaml
exit:
  direction: NORTH
  destination: ../sorting-room/
  
  # SPLITTER behavior
  splitter:
    enabled: true
    
    # Priority output (items go here first if they match)
    priority_output:
      direction: EAST
      filter: { tags: ["rare"] }
      
    # Default output (everything else)
    default_output:
      direction: NORTH
      
    # Can also filter
    input_filter: { tags: ["sortable"] }
```

### Balanced Splitter

```yaml
exit:
  direction: NORTH
  
  splitter:
    mode: balanced    # Alternate between outputs
    outputs:
      - destination: ../line-a/
      - destination: ../line-b/
      - destination: ../line-c/
```

---

## Circuit Network (Events & Signals)

Objects can send signals like Factorio's circuit network:

```yaml
object:
  id: item-counter
  name: "Chest Monitor"
  
  # Reads from a chest
  reads_from: "#storage-chest"
  
  # Outputs signal
  signals:
    - signal: "iron-plates"
      value: "count of iron-plate in storage-chest"
      
  # Conditional output
  circuit_condition:
    if: "iron-plates > 100"
    output_signal: "iron-full"
    
  # Visual
  displays:
    show: "iron-plates"
    as: "numeric"
```

### Circuit-Controlled Inserter

```yaml
object:
  id: smart-inserter
  name: "Circuit-Controlled Arm"
  
  type: inserter
  
  # Only operates when signal is true
  enabled_condition:
    signal: "iron-needed"
    operator: "=="
    value: true
    
  input:
    source: "#belt"
  output:
    destination: "#furnace"
```

### Train Signal (Room Access Control)

```yaml
exit:
  direction: NORTH
  destination: ../dangerous-room/
  
  # SIGNAL control
  signal_control:
    enabled: true
    
    # Only open when safe
    open_when:
      signal: "grue-cleared"
      value: true
      
    # Closed signal
    closed_message: "⛔ DANGER — Grue detected ahead!"
```

---

## Assemblers (Crafting Objects)

Objects that transform inputs to outputs:

```yaml
object:
  id: furnace
  name: "Stone Furnace"
  emoji: "🔥"
  
  type: assembler
  
  # Current recipe
  recipe:
    id: smelt-iron
    inputs:
      - { item: "iron-ore", count: 1 }
      - { item: "coal", count: 0.5 }
    outputs:
      - { item: "iron-plate", count: 1 }
    time: 3    # Turns to complete
    
  # Internal storage
  input_slots: 2
  output_slots: 1
  
  # State
  state:
    progress: 0
    fuel: 5
    
  simulate: |
    Each turn:
      If has all inputs AND has fuel:
        progress += 1
        fuel -= 0.1
        If progress >= recipe.time:
          Consume inputs
          Produce outputs
          progress = 0
          emit "The furnace produces an iron plate!"
```

---

## The Full Factory Example

```yaml
# A complete logistics setup

# RAW MATERIALS (Passive Provider)
container:
  path: warehouse/raw/
  name: "Raw Materials"
  chest_mode: passive-provider
  provides: [{ tags: ["raw"] }]

# SMELTING ROOM  
room:
  path: smelter/
  name: "Smelting Room"
  
  exits:
    WEST:
      destination: ../warehouse/raw/
      flow:
        enabled: true
        direction: inbound
        allow: [{ tags: ["ore"] }]
    EAST:
      destination: ../warehouse/plates/
      flow:
        enabled: true
        direction: outbound
        allow: [{ tags: ["plate"] }]
        
  objects:
    - furnace-1.yml
    - furnace-2.yml
    - belt-to-furnaces.yml
    - belt-from-furnaces.yml

# PLATE STORAGE (Passive Provider)
container:
  path: warehouse/plates/
  name: "Plate Storage"
  chest_mode: passive-provider
  provides: [{ tags: ["plate"] }]

# ASSEMBLY (Requester)
container:
  path: assembly/
  name: "Assembly Line"
  chest_mode: requester
  request_list:
    - { item: "iron-plate", count: 20, min: 5 }
    - { item: "copper-plate", count: 20, min: 5 }
```

---

## "Throw Ball North" — The Simplest Case

```yaml
# Player throws a ball
action:
  verb: throw
  object: ball
  direction: NORTH
  
# Resolution:
# 1. Find exit NORTH
# 2. Check exit.flow or use default
# 3. Apply exit.place_at or destination's placement_rules
# 4. Move ball to destination
# 5. Emit "The ball bounces north into the maze."

# In the exit:
exit:
  direction: NORTH
  destination: ../maze/room-a/
  
  # Ball lands on floor by default
  place_at: floor
  
  # Or with fancy physics:
  thrown_items:
    land_at: "random zone in destination"
    bounce: true
    noise: "thud"
```

---

## The Sims Connection

| Sims System | Factorio System | MOOLLM System |
|-------------|-----------------|---------------|
| Needs decay | Resource consumption | `simulate` with buffs |
| Job carpool | Logistic bots | NPC carriers |
| Fridge → Counter → Table | Provider → Belt → Requester | `flow` + `placement_rules` |
| Bills & mail | Item transport | Postal system |
| Burglar stealing | Active provider (unwanted!) | `push_to` with events |

---

## Implementation Notes

### Phase 1: Basic Flow
- Add `flow` to EXIT.yml.tmpl
- Implement belt simulation in adventure.py
- Items move on turn tick

### Phase 2: Chest Modes  
- Add `chest_mode` to CONTAINER.yml.tmpl
- Implement request/provide matching
- Network discovery (which chests are connected)

### Phase 3: Inserters & Bots
- Object `simulate` with I/O
- NPC behavior: logistic-bot
- Pathfinding between rooms

### Phase 4: Circuits
- Signal emission and reading
- Conditional gates on exits
- Visual displays

---

## Why This Matters

**WILL WRIGHT:** "The Sims was a FACTORY for happiness. Needs as resources, actions as recipes."

**DON HOPKINS:** "And Factorio is a GAME about watching conveyor belts! Both are about FLOW."

**MARVIN MINSKY:** "Intelligence is moving the right thing to the right place at the right time."

The logistics protocol makes adventures into LIVING SYSTEMS where items flow, needs are met, and the world runs itself.

**"The best adventures play themselves. You're just there to watch."**

---

## Rooms ARE Logistic Containers — The Unification!

**THE BIG INSIGHT:**

> "Rooms aren't just spaces. They're LOGISTIC NODES that advertise what they need!"

### The Sims + Factorio = MOOLLM

| System | What Advertises | What It Wants |
|--------|-----------------|---------------|
| **The Sims** | Objects | Player attention (actions) |
| **Factorio** | Chests | Items (resources) |
| **MOOLLM** | Rooms AND Objects | Both! |

### Logistic Advertisements on Rooms

Rooms can advertise their NEEDS with attractiveness scores:

```yaml
room:
  name: "The Kitchen"
  
  logistic_advertisements:
    
    NEED_INGREDIENTS:
      description: "Kitchen needs ingredients for cooking"
      wants:
        - tags: ["ingredient"]
          count: 10
      score: 70                   # Base attractiveness
      score_if: "chef_is_cooking" # Condition for bonus
      score_bonus: 30             # Total 100 when chef is cooking!
      
    NEED_FUEL:
      wants:
        - item: "coal"
          count: 5
      score: 50
      score_if: "stove.fuel < 2"
      score_bonus: 50             # Urgent when almost out!
```

### The Flow

```
1. ROOMS announce logistic_advertisements with scores
   │
   ▼
2. LOGISTICS ENGINE collects all ads
   │
   ▼
3. PROVIDERS (other rooms, warehouses) offer matching items
   │
   ▼
4. ENGINE routes items to HIGHEST-SCORING requester
   │
   ▼
5. BOTS or BELTS physically move items
   │
   ▼
6. ROOM receives items, fires on_item_added
```

### Quadrant Containers — Logistics at the Grid Level!

**KEY INSIGHT:** The logistics config lives at the **QUADRANT** level, not in each cell!

The diagonal directions (NW/NE/SW/SE) of the pie menu open into GRID QUADRANTS.
Each quadrant has a `LOGISTIC-CONTAINER.yml` that defines logistics behavior.
Individual grid rooms **inherit** from their parent container.

```
wizard-study/                        # Main room (pie menu center)
  ROOM.yml
  nw/                                # Northwest quadrant (diagonal exit)
    LOGISTIC-CONTAINER.yml           # ← Logistics config HERE!
    iron-ore/
      ROOM.yml                       # Inherits logistics from parent!
    copper-ore/
      ROOM.yml                       # Also inherits!
    coal/
      ROOM.yml
  ne/                                # Northeast quadrant
    LOGISTIC-CONTAINER.yml           # Different config for this quadrant
    finished-goods/
      ROOM.yml
  sw/                                # Southwest quadrant  
    LOGISTIC-CONTAINER.yml           # Ingredients storage (requester)
  se/                                # Southeast quadrant
    LOGISTIC-CONTAINER.yml           # Staging area (buffer)
```

### 🏙️ The Urban Planning Metaphor

**Grid rooms are CITY BLOCKS at street intersections!**

```
           N (street going north)
           ↑
    ┌──────┼──────┐
    │  NW  │  NE  │  ← BUILDINGS you ENTER
    │ BLOCK│ BLOCK│    (warehouses, factories, shops)
W ──┼──────●──────┼── E (streets going east/west)
    │ BLOCK│ BLOCK│    
    │  SW  │  SE  │  ← BUILDINGS you ENTER
    └──────┼──────┘
           ↓
           S (street going south)
```

| Urban Element | MOOLLM Element | Description |
|---------------|----------------|-------------|
| **Streets** | Cardinal exits (N/S/E/W) | You TRAVEL along them |
| **Intersection** | The room you're in | Where streets cross |
| **Buildings/Blocks** | Diagonal quadrants (NW/NE/SW/SE) | You ENTER them |
| **City Grid** | The logistic container | The whole neighborhood |
| **Building Interior** | Grid cells within quadrant | Sub-rooms/floors |

**You stand at an intersection. Streets lead NSEW. Buildings fill the corners.**

### Pie Menu = Street Intersection

```
           N (to Great Hall — street north)
           │
    NW ←───●───→ NE
   ORE     │    GOODS        ← ENTER BUILDINGS (diagonals)
  STORAGE  │   OUTPUT          Each building has its own purpose!
   🏭      │    📦
           │
    W ←────┼────→ E
 KITCHEN   │   GARDEN        ← TRAVEL STREETS (cardinals)
   🏠      │    🌳
           │
    SW ←───●───→ SE
  INGRED.  │   STAGING       ← ENTER BUILDINGS (diagonals)
   📦      │    🚚
           │
           S (to Cellar — street south)
```

### The Building Interior Pattern

When you ENTER a diagonal building, you're inside a structure:

```
wizard-study/nw/                 # You entered the NW building!
├── iron-ore/                    # Floor 1 or Room 1
├── copper-ore/                  # Floor 2 or Room 2  
├── coal/                        # Floor 3 or Room 3
└── LOGISTIC-CONTAINER.yml       # Building-wide logistics
```

Inside the building:
- **Navigate between rooms** — Cardinal directions
- **Exit to street** — Diagonal back to intersection (SW exits NW building)

### Why This Matters

1. **Intuitive Navigation** — Everyone understands city grids
2. **Scalable** — Buildings can be as complex as needed internally
3. **Mixed Use** — Some buildings are warehouses, some are factories, some are shops
4. **Zoning** — Different quadrants have different purposes (like city zoning!)

### SimCity Meets Factorio

```yaml
# Each quadrant is like a SimCity zone:
nw:
  zone: industrial     # Ore storage and processing
  logistics: passive-provider
  
ne:
  zone: commercial     # Finished goods output
  logistics: active-provider
  
sw:
  zone: residential    # Ingredient requests (consumption)
  logistics: requester
  
se:
  zone: transport      # Staging, loading docks
  logistics: buffer
```

### Quadrant Examples

```yaml
# wizard-study/nw/LOGISTIC-CONTAINER.yml — Ore Storage (Provider)
logistic-container:
  id: ore-storage
  name: "Ore Storage Quadrant"
  mode: passive-provider
  
  provides:
    - tags: ["ore", "raw-material"]
    
  grid:
    enabled: true
    auto_create_cells: true
    stack_limit: 10000

# wizard-study/sw/LOGISTIC-CONTAINER.yml — Ingredients (Requester)
logistic-container:
  id: ingredients
  name: "Ingredient Storage"
  mode: requester
  
  request_list:
    - tags: ["ingredient"]
      count: 100
      
  logistic_advertisements:
    NEED_INGREDIENTS:
      wants: [{ tags: ["ingredient"], count: 100 }]
      score: 70
```

### Grid Rooms Inherit — Minimal Cells!

Grid rooms are MINIMAL. They inherit behavior from parent:

```yaml
# nw/iron-ore/ROOM.yml
room:
  inherits: ["../"]          # ← Inherit from parent container!
  
  stacks:
    iron-ore: 2500           # Just the data
    
  exits:
    SW: ../../               # Back to main room
    N: ../copper-ore/
    E: ../coal/
    
  # NO logistics config needed — inherited from parent!
```

### Walking Through a Warehouse

If `navigable: true`, players can WALK between cells:

```yaml
# In nw/iron-ore/ROOM.yml
room:
  name: "Iron Ore Storage"
  type: grid-cell
  inherits: ["../"]                  # Inherit from quadrant!
  description: "Towering stacks of iron ore crates."
  
  exits:
    NORTH: ../copper-ore/
    SOUTH: ../coal/
    SW: ../../                       # Back to main room (diagonal corner)
    
  stacks:
    iron-ore: 2500
```

### Stacking in Rooms

Any room can have stacks of items:

```yaml
room:
  name: "Armory"
  
  stacks:
    # Fungible items (just count)
    arrow: 500
    bolt: 300
    
    # Instance items (individual state)
    magic-sword:
      count: 3
      instances:
        - { id: flame-blade, damage: 50, enchant: fire }
        - { id: frost-edge, damage: 45, enchant: ice }
        - { id: rusty-old, damage: 10, enchant: null }
        
  stack_limit: 1000    # Per item type
```

### Room Advertisements vs Object Advertisements

Both work together!

```yaml
room:
  name: "The Kitchen"
  
  # ROOM advertises what it NEEDS (logistics)
  logistic_advertisements:
    NEED_INGREDIENTS:
      wants: [{ tags: ["ingredient"], count: 5 }]
      score: 70
      
  # ROOM advertises what it OFFERS (actions)
  advertisements:
    COOK:
      description: "Prepare a meal"
      guard: "ingredients available"
      score: 60
      
  objects:
    - stove.yml     # OBJECT also advertises!
    - fridge.yml    # Another provider!
```

### Priority System

When multiple rooms want the same item:

```yaml
# Kitchen urgently needs fuel
logistic_advertisements:
  NEED_FUEL:
    wants: [{ item: "coal" }]
    score: 100    # URGENT!
    
# Storage room kind of wants overflow
logistic_advertisements:
  STORE_ANYTHING:
    wants: [{ tags: ["any"] }]
    score: 20     # Low priority
```

**Result:** Coal goes to kitchen (score 100 beats 20).

### Signals from Rooms

Rooms emit signals for circuit control:

```yaml
room:
  name: "Treasury"
  
  signals:
    enabled: true
    emit:
      - signal: "gold-count"
        value: "stacks.gold-coin"
      - signal: "is-guarded"
        value: "guard.present"
        
# Door that only opens when treasury has guards
exit:
  destination: ../treasury/
  signal_control:
    open_when:
      signal: "is-guarded"
      value: true
```

---

## Postal IS the Transport Layer!

**THE BIG INSIGHT:** You don't need physical bots to move items!

The postal system IS the logistics transport layer:
- **Instantaneous** — no travel time
- **Free** — no cost for internal logistics
- **Invisible** — items just appear
- **Efficient** — never fails, unlimited capacity

### The Unification

| Factorio | MOOLLM |
|----------|--------|
| Logistics bots flying | Postal system (instant) |
| Items in bot cargo | Email attachments |
| Request triggers bot | Request triggers postal transfer |
| Circuit signals | Text messages |
| Bot charging at roboport | N/A (postal is always on) |

### How It Works

```yaml
# Logistics request triggers postal transfer
logistics_delivery:
  trigger: "requester.request_unfulfilled"
  
  # Auto-generated postal transfer
  postal_transfer:
    type: internal-logistics    # Instant, free
    from: "nw/iron-ore/"
    to: "forge/"
    attachments:
      - type: object
        ref: "iron-ore"
        quantity: 20
        action: send
        
    delivery:
      method: logistics         # Instant, free
      total_time: 0
      cost: 0
```

### Transport Methods

| Method | Time | Cost | Use Case |
|--------|------|------|----------|
| `postal` | Instant | Free | Default for all logistics |
| `bot` | Travel time | Optional | Drama, interactivity |
| `belt` | Per-turn | Free | Visible Factorio-style |

### Bots Are Optional Drama!

**Default:** Postal (efficient, invisible)
**Optional:** Physical bots (fun, interactive)

```yaml
logistic-container:
  transport:
    method: postal    # Default: instant via mail
    # OR
    method: bot       # Physical: slower, visible, pettable!
    bot_config:
      character: "characters/courier-kitten/"
```

When you want drama:
- Player sees the kitten carrying items
- Can intercept, pet, redirect
- Adds gameplay
- But slower!

### Phone Integration

Your phone is the logistics dashboard:

```yaml
# Text notifications = Circuit signals
phone_notifications:
  notify_on:
    - event: "low_stock"
      message: "⚠️ Forge running low on coal!"
    - event: "request_fulfilled"
      message: "📦 Iron ore delivered to forge"

# Camera = Image generation
camera:
  action: generate
  prompt: "A photograph of the warehouse contents..."
```

### Why Postal Beats Bots

| Physical Bots | Postal Transport |
|---------------|------------------|
| Slow | Instant |
| Can get stuck | Never fails |
| Limited cargo | Unlimited |
| Visible (breaks immersion?) | Invisible (just works) |
| Fun to watch | Efficient |

**Use bots when you want fun. Use postal when you want efficiency.**

### The Complete Integration

```
                    LOGISTICS
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
    REQUESTER       PROVIDER         BELT/EXIT
    (wants items)   (has items)      (physical flow)
        │               │               │
        │               │               │
        ▼               ▼               ▼
    │           POSTAL SYSTEM              │
    │   (Instant, Free, Invisible)         │
    │                                      │
    │  ┌─────────┐      ┌─────────┐       │
    │  │  Text   │      │ Letter  │       │
    │  │ Signals │      │ Items   │       │
    │  └─────────┘      └─────────┘       │
    │                                      │
    │  ┌─────────┐      ┌─────────┐       │
    │  │ Camera  │      │  Phone  │       │
    │  │ Images  │      │ Notifs  │       │
    │  └─────────┘      └─────────┘       │
```

---

## Image Mining: Camera as Resource Extractor

**The revelation continues:**

> "Your camera is a PICKAXE for visual reality!
> Every image is a compressed lode of resources.
> Point, shoot, MINE!"

### The Core Mechanic

Just like the Kitchen Counter's DECOMPOSE:
- `sandwich` → `bread + cheese + lettuce`
- `lamp` → `brass + glass + wick + oil`

Images can be MINED:
- `ore_vein.png` → `iron-ore × 12` + `stone × 8`
- `forest.png` → `wood × 5` + `leaves × 20`
- `treasure.png` → `gold × 100` + `gems × 15`

### Resource Acquisition Chain

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CAMERA    │ ──► │   IMAGE     │ ──► │   MINE      │
│ (capture)   │     │ (analysis)  │     │ (extract)   │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
                                              ▼
                    ┌─────────────────────────────────────┐
                    │         LOGISTICS SYSTEM            │
                    │  (Resources flow to containers)     │
                    └─────────────────────────────────────┘
```

### Integration with Logistics

```yaml
# Objects can be mineable
object:
  name: Ancient Ore Painting
  
  mineable:
    enabled: true
    yields:
      - item: iron-ore
        quantity: [5, 15]
      - item: artistic-essence
        quantity: 1
        rare: 0.3
    exhaustion:
      max_mines: 3
      diminishing: 0.5

# Mined resources auto-route
mining_config:
  routing:
    - match: { tags: ["ore"] }
      destination: "nw/ore-storage/"
    - match: { tags: ["organic"] }
      destination: "ne/organic-materials/"
```

### Camera Phone as Mining Interface

```yaml
phone_mining:
  # AR overlay shows mineable resources
  ar_overlay:
    shows:
      - resource_types: "icons"
      - richness: "glow intensity"
      - exhaustion: "fade level"
      
  # Tap to preview, long-press to mine
  gestures:
    tap: analyze
    long_press: mine
```

### Mining Depth Levels

| Depth | What You Extract |
|-------|------------------|
| Surface | Physical materials (ore, wood, stone) |
| Deep | Hidden resources, emotions, concepts |
| Quantum | Probabilities, observations |
| Philosophical | Meaning, narrative, existence |
| Sensations | Colors, smells, flavors, attitudes, emotions |

**Deep mining example:**
```yaml
mine:
  target: "sunset.png"
  depth: philosophical
  
  yields:
    - item: "passage-of-time"
      type: abstract
    - item: "beauty-that-fades"
      type: poetic
```

### The Complete Resource Flow

```
📷 Camera shot
    │
    ▼
🖼️ Image analyzed
    │
    ▼
⛏️ MINE action
    │
    ▼
💎 Resources extracted
    │
    ▼
📬 Postal delivers (instant!)
    │
    ▼
📦 Logistics containers receive
    │
    ▼
🏭 Assemblers process
    │
    ▼
🎁 Products created!
```

**The factory grows. The camera mines. Reality yields its resources.**

---

*Design complete. The factory grows. Items flow. The mail never stops.*

*Last updated: January 10, 2026*
