# Sims Portable Objects → MOOLLM Containment

> *Carrying Objects, Inventory, and Object Containment*
> *Objects within objects, characters carrying things, recursive containment*

## The Carrying System

The Sims had elaborate systems for characters interacting with portable objects:

| Sims Feature | Description |
|--------------|-------------|
| **Portable Objects** | Objects that can be picked up and moved |
| **Carrying Accessories** | Visual representation of held items |
| **Carrying Objects** | The object itself being transported |
| **Carrying Animations** | Movement sequences with objects |
| **Slot Positions** | kHeightHand — where objects are held |

When a Sim picked up a plate of food, the object:
1. Left its current position (table surface)
2. Attached to the Sim's hand slot
3. Moved with the Sim during navigation
4. Could be placed on new surfaces

---

## MOOLLM Containment Model

MOOLLM implements containment through filesystem structure and YAML references:

### Physical Containment (Directory)

```
pub/
├── bar/
│   ├── cocktail-shaker.yml    # Object IN bar
│   └── glasses/
│       ├── martini.yml        # Objects IN glasses container
│       └── rocks.yml
└── kitchen/
    └── plate.yml
```

Objects are **physically contained** in their directory location.

### Portable Object Pattern

```yaml
# characters/palm/inventory/basket.yml
name: WOVEN-BASKET
type: container
portable: true
contents:
  - banana.yml      # Object inside basket
  - scroll.yml      # Another contained object
  
# When Palm moves, his inventory moves with him
```

### Location vs. Home

As described in the [Incarnate Framework](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#home-vs-location-the-virtualization-of-presence):

```yaml
# An object has a "home" (filesystem location)
# and a "location" (where it currently is)

# pub/bar/cocktail-shaker.yml
name: COCKTAIL-SHAKER
home: pub/bar/cocktail-shaker.yml  # Permanent address
location: characters/marieke/hands  # Currently being held
```

---

## Standard Heights → Slot Types

The Sims defined standard heights for object placement:

| Height | Description | MOOLLM Equivalent |
|--------|-------------|-------------------|
| `kHeightGround` | Floor level | Room-level objects |
| `kHeightLowTable` | Coffee table | surface-objects list |
| `kHeightTable` | Dining table | table contents |
| `kHeightCounter` | Kitchen counter | counter-objects |
| `kHeightHand` | Character's hand | inventory/hands |
| `kHeightSitting` | Lap/seated position | seated-with |
| `kHeightEndTable` | Side table | side-contents |

**MOOLLM:**

```yaml
# pub/bar/ROOM.yml
surfaces:
  bar_top:
    height: counter
    contents:
      - napkin-holder.yml
      - bell.yml
      
  tables:
    height: table
    contents:
      - menu.yml
      
# characters/palm/CHARACTER.yml
inventory:
  hands:
    - banana.yml
  pockets:
    - key.yml
```

---

## Recursive Containment

The Sims allowed objects inside objects:

```
Refrigerator
├── Milk carton
├── Leftover pizza
└── Mystery container
    └── ??? (green and fuzzy)
```

**MOOLLM:**

```yaml
# pub/kitchen/refrigerator.yml
name: GROTTO-FRIDGE
type: container
temperature: cold
contents:
  - item: oat-milk.yml
    quantity: 1
    freshness: 85%
    
  - item: mystery-container.yml
    last_checked: never
    contents:
      - something-fuzzy.yml  # Nested containment!
      
actions:
  - OPEN
  - CLOSE
  - GET-ITEM
  - PUT-ITEM
  - INSPECT-MYSTERY
```

---

## Animation to Narrative

The Sims had specific animations for carrying:

| Animation Type | Description |
|----------------|-------------|
| `a2o-carry-plate` | Two-handed plate carry |
| `a2o-carry-glass` | One-handed drink carry |
| `a2o-carry-baby` | Careful baby carry |
| `a2o-put-down` | Setting object on surface |

**MOOLLM:** Animation becomes prose:

```yaml
# Instead of animation files:

carry_narrative:
  one_handed: |
    Palm grabs the banana with practiced ease, 
    continuing to gesture with his free hand.
    
  two_handed: |
    Palm carefully lifts the banana cake, 
    balancing it with both paws as he navigates.
    
  precious: |
    Palm cradles the ancient scroll against his chest,
    tail curling protectively.
```

---

## Object Transfer Protocol

When objects move between containers/holders:

**The Sims:**
1. Object leaves source slot
2. Character performs pickup animation
3. Object attaches to hand slot
4. Character navigates
5. Character performs put-down animation
6. Object enters destination slot

**MOOLLM:**

```yaml
# Action: Give banana to Maurice

transfer:
  object: inventory/banana.yml
  from: palm/inventory/hands
  to: maurice/inventory/received
  
narrative: |
  Palm reaches into his basket and withdraws a particularly
  fine banana. "For you, my friend," he says, offering it
  to Maurice with a slight bow. The cat sniffs it cautiously,
  then accepts it with feline grace.
  
state_changes:
  - palm.inventory.banana: removed
  - maurice.inventory.banana: added
  - relationship.palm_maurice: +5 (gift given)
```

---

## Surfaces and Placement

The Sims tracked which surfaces could hold objects:

```
Surface: Coffee Table
├── Can hold: small objects
├── Height: kHeightLowTable
├── Slots: 4 positions
└── Current: [Magazine] [Cup] [empty] [empty]
```

**MOOLLM:**

```yaml
# pub/seating/coffee-table.yml
name: WEATHERED-COFFEE-TABLE
type: surface
capacity: 4 slots

occupancy:
  - slot: 1
    object: magazine-cannabis-culture.yml
  - slot: 2
    object: maurice-water-bowl.yml
  - slot: 3
    empty: true
  - slot: 4
    empty: true

behaviors:
  on_full: |
    "There's no room on the table. 
    Something would need to be moved."
```

---

## Censorship and Visibility

The Sims famously blurred certain content:

```
Censorship system:
├── Toilet use → pixelated
├── Shower/bath → pixelated
├── WooHoo → covered
└── Clothing change → pixelated
```

The blur was technically a "carried accessory" — an invisible object attached to the character's position.

**MOOLLM:** Tasteful narration instead of blur:

```yaml
# Narrative approach to privacy

privacy_handling:
  bathroom:
    narration: "Palm excuses himself to the facilities."
    # No explicit description
    
  intimacy:
    narration: "The curtain falls on this private moment..."
    # Fade to black
    
  changing:
    narration: "Palm emerges wearing fresh clothes."
    # Skip the between-state
```

This connects to [representation-ethics](../skills/representation-ethics/) — tasteful handling of sensitive content.

---

## Inventory Management

**The Sims:**
- Limited personal inventory
- Objects on lot always accessible
- "Go get item" as autonomous action

**MOOLLM:**

```yaml
# characters/palm/inventory.yml
capacity:
  hands: 2 items
  pockets: 4 small items
  basket: 10 items (Palm's signature item)
  
constraints:
  hands:
    - max_size: medium
    - note: "Prehensile tail can hold one extra small item"
    
current:
  hands:
    - banana-gift.yml
  pockets:
    - room-key.yml
    - notebook-stub.yml
  basket:
    - infinite-typewriters.yml  # His prized possession
    - various-fruits.yml
```

---

## Multi-Tile Objects

The Sims had objects spanning multiple tiles:

```
Grand Piano:
├── Tile 1: keyboard
├── Tile 2: body
├── Tile 3: lid
└── Routing: approach from tile 1
```

**MOOLLM:**

```yaml
# pub/stage/grand-piano.yml
name: GROTTO-GRAND
type: instrument
tiles:
  - position: keyboard
    interactions: [PLAY, PRACTICE, SHOW-OFF]
  - position: body
    interactions: [LEAN, ADMIRE]
  - position: lid
    interactions: [OPEN, CLOSE, HIDE-INSIDE]
    
routing:
  approach: keyboard
  audience_view: body
  
note: |
  Palm once tried to perform from inside the piano.
  Maurice was not amused.
```

---

## The Containment Principle

Both systems share a principle:

> **Objects have positions, and positions can be inside other objects.**

The Sims: Object → Slot → Parent Object → Room → Lot
MOOLLM: File → Directory → Parent Directory → Adventure

```yaml
# Nested containment example

location_path:
  world: moollm/examples/adventure-4/
  lot: pub/
  room: bar/
  surface: counter/
  container: tip-jar.yml
  object: lucky-coin.yml
  
# The lucky coin is IN the tip jar
# which is ON the counter
# which is IN the bar
# which is IN the pub
# which is IN the adventure
```

---

## MOOLLM Enhancements

MOOLLM adds capabilities The Sims didn't have:

### 1. Semantic Containment

Objects can be "in" abstract containers:

```yaml
# Abstract containment
palm_memory:
  - type: concept
    contains:
      - memory-of-first-banana.yml
      - wisdom-from-elders.yml
      
# Not physical — mental containment
```

### 2. Dynamic Container Creation

```yaml
# Create container on the fly
action: "Palm fashions a basket from palm fronds"

result:
  - new_object: improvised-basket.yml
    type: container
    capacity: 3 small items
    durability: temporary
```

### 3. Virtual Containment

```yaml
# Object references another's contents
coat_pockets:
  reference: characters/visitor/inventory.yml#pockets
  access: view_only  # Can see, not take
  
# "I noticed something glinting in their pocket..."
```

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#home-vs-location-the-virtualization-of-presence) — Home vs. Location
- [sims-object-model.md](./sims-object-model.md) — Object properties
- [sims-room-spatial.md](./sims-room-spatial.md) — Room containment
- [skills/room/](../skills/room/) — Room definitions
- [representation-ethics](../skills/representation-ethics/) — Privacy handling

---

*"A Sim's inventory is their immediate world. Their pockets, their hands, what they carry — this is agency made tangible."*
