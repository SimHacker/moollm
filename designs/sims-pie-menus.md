# The Sims Pie Menus → MOOLLM

> *"I can't imagine The Sims without pie menus."*
> *— Chaim Gingold, "Play Design" PhD Thesis*

## The Essential Interface

Chaim Gingold, in his doctoral thesis on play design, captured why pie menus were indispensable to The Sims:

> "Pie menus play a critical role in The Sims' user interface design, dovetailing perfectly with the object and AI architecture. Objects advertise verbs to character AI, so it is natural for the verbs to be arranged in a radial menu about objects. I can't imagine an alternate design that would have had the same widespread usability, and therefore appeal, without them. It is difficult to imagine The Sims without pie menus."

This isn't accidental. Pie menus were designed from the start to be the natural interface for object-verb interaction.

---

## Document Index

- [The Essential Interface](#the-essential-interface)
- [What Are Pie Menus?](#what-are-pie-menus)
- [Fitts's Law: The Science](#fittss-law-the-science)
- [Mouse-Ahead: Muscle Memory](#mouse-ahead-muscle-memory)
- [Self-Revealing Gestures](#self-revealing-gestures)
- [The Sims Integration](#the-sims-integration)
- [Objects Advertise Verbs](#objects-advertise-verbs)
- [Hierarchical Pie Menus](#hierarchical-pie-menus)
- [Gesture Space](#gesture-space)
- [Pie Menus in MOOLLM](#pie-menus-in-moollm)
- [Memory Palaces (Method of Loci)](#memory-palaces-method-of-loci)
- [Adventure Map Navigation](#adventure-map-navigation)
- [Editors and Building Tools](#editors-and-building-tools)
- [Don Hopkins' Pie Menu History](#don-hopkins-pie-menu-history)
- [Touchscreen Considerations](#touchscreen-considerations)
- [See Also](#see-also)

---

## What Are Pie Menus?

Pie menus are circular, radial menus that appear centered on the cursor or selection point. Options are arranged like slices of a pie, each in a distinct direction from the center.

```
        [North]
           │
    [NW]   │   [NE]
       ╲   │   ╱
        ╲  │  ╱
         ╲ │ ╱
[West] ────●──── [East]
         ╱ │ ╲
        ╱  │  ╲
       ╱   │   ╲
    [SW]   │   [SE]
           │
       [South]
```

**Key advantages:**

1. **Equal distance** — All items the same distance from center
2. **Direction = meaning** — Position carries semantic weight
3. **Large targets** — Wedges extend to screen edge (infinite radius)
4. **Muscle memory** — Learn gestures, not locations

---

## Fitts's Law: The Science

Fitts's Law states that the time to acquire a target depends on **distance** and **target size**:

```
Time = a + b × log₂(Distance / Size + 1)
```

**Linear menus:** Items are small rectangles at varying distances.

**Pie menus:** All items are the same distance, with wedges that extend infinitely.

| Metric | Linear Menu | Pie Menu |
|--------|-------------|----------|
| Distance | Varies (1-20 items deep) | Constant (1 gesture) |
| Target size | Fixed rectangle | Infinite wedge |
| Traversal | Sequential | Direct |

Result: Pie menus are **15-30% faster** in user studies.

---

## Mouse-Ahead: Muscle Memory

The killer feature: **mouse-ahead typing**.

Once you learn that "Delete" is always to the right, you can:

1. Click to invoke menu
2. Flick right without looking
3. Action executes

You don't wait for the menu to render. You don't read options. You gesture.

```
Traditional menu:
  Click → Wait → Read → Move → Click
  
Pie menu with muscle memory:
  Click-drag-release (one fluid motion)
```

This is why expert Sims players could manage complex households at high speed — pie menus became gestural.

---

## Self-Revealing Gestures

Pie menus solve the discoverability problem of pure gesture systems:

| System | Discoverable? | Fast? |
|--------|---------------|-------|
| Text menus | ✓ Yes | ✗ Slow |
| Pure gestures | ✗ Hidden | ✓ Fast |
| Pie menus | ✓ Self-revealing | ✓ Fast |

For novices: the menu shows all options visually.

For experts: it becomes a gestural shortcut.

The same interface serves both learning and mastery.

---

## The Sims Integration

In The Sims, pie menus weren't bolted on — they were architectural:

### Objects Advertise Verbs

Every object in The Sims has a **tree table** — a registry of available interactions:

```yaml
# MOOLLM equivalent: CARD.yml
toilet:
  advertised_methods:
    USE:
      guard: person.bladder < 75
      satisfies: [bladder]
    CLEAN:
      guard: toilet.dirty > 50
      satisfies: []
    REPAIR:
      guard: toilet.broken AND person.has_skill("repair")
      satisfies: []
```

When you click on a toilet, The Sims queries the object: "What verbs do you advertise?"

The answer populates the pie menu.

### Why Radial Is Natural

Objects are **points in space**. Interactions radiate **outward** from objects.

A toilet offers verbs. Those verbs emanate from the toilet's location. A radial menu centered on the toilet is geometrically natural.

Linear menus would be arbitrary — why would "Use" be above "Clean"? With pie menus, spatial position carries meaning:

- **Up**: Positive actions (Use, Play, Eat)
- **Down**: Negative actions (Destroy, Trash)
- **Left/Right**: Neutral alternatives (Options, More...)

---

## Hierarchical Pie Menus

When more than 8 options exist, pie menus can be hierarchical:

```
         [Social]
            │
    [Talk]  │  [Touch]
        ╲   │   ╱
         ╲──●──╱
        ╱   │   ╲
    [Play]  │  [Fight]
            │
         [Romance]

User selects [Social] →

         [Joke]
            │
   [Gossip] │  [Chat]
        ╲   │   ╱
         ╲──●──╱
        ╱   │   ╲
   [Story]  │  [Argue]
            │
        [Complain]
```

Each level maintains the radial layout. Navigation is still gestural — flick up-then-right for Social → Chat.

### MOOLLM Parallel

The [pub/menus/](../examples/adventure-4/pub/menus/) directory structure mirrors this:

```
pub/
├── menus/
│   ├── drinks.yml      # Top-level category
│   ├── food.yml        # Top-level category
│   ├── games.yml       # Top-level category
│   └── buds.yml        # Top-level category
```

Each menu is a "pie slice" at the top level. Each YAML file contains nested options — the hierarchical sub-pies.

---

## Gesture Space

Pie menus occupy **gesture space** — the set of all possible directional movements:

```
8-direction pie menu:
  ↑ ↗ → ↘ ↓ ↙ ← ↖

Each direction is a unique gesture.
Sequences become "gesture sentences":
  ↑→ = "Social" then "Chat"
  ←↓ = "Options" then "Delete"
```

This connects to **Dasher** and other gesture-based text entry systems. The LLM navigates concept space; the user navigates gesture space. Both are directional, compositional.

### Contrast with Shape Recognition

Some systems recognize shapes (draw a circle for "open", draw an X for "delete"). These are:

- Hard to remember
- Easy to confuse
- Slow to execute

Pie menus are superior because directions are natural and distinct.

---

## Pie Menus in MOOLLM

MOOLLM inherits pie menu principles even without graphical menus:

### 1. Objects Advertise Verbs

Every `CARD.yml` lists `advertised_methods`:

```yaml
# skills/bartender/CARD.yml
advertised_methods:
  SERVE-DRINK:
    visibility: public
    satisfies: [thirst, social]
    
  RECOMMEND:
    visibility: public
    satisfies: [curiosity]
    
  CUT-OFF:
    visibility: private
    satisfies: [safety]
```

When you interact with the bartender, these verbs become available. The LLM "displays" them through description:

> "The bartender looks up expectantly. You could **order a drink**, **ask for a recommendation**, or just **chat**."

Prose pie menu. Options radiate from the interaction point.

### 2. Contextual Relevance

Like The Sims' guard conditions, MOOLLM filters options:

```yaml
SERVE-DRINK:
  guard: customer.in_pub AND customer.age >= 21
```

The LLM won't offer drinks to someone outside the pub. Context shapes availability.

### 3. Hierarchical Structure

MOOLLM's skill composition mirrors hierarchical pie menus:

```
User says: "I want a drink"
  → skill: bartender
    → method: SERVE-DRINK
      → submenu: drinks.yml
        → categories: [cocktails, beer, wine, soft]
          → specific item
```

Each level is a navigation step. The user drills down through prose choices.

### 4. Muscle Memory Equivalent

For CLI interactions or agentic systems, **consistent command syntax** creates muscle memory:

```bash
# These patterns become automatic:
GO kitchen
TALK bartender ABOUT weather
USE toilet
TAKE lamp
```

Consistent verb-noun structure. Users learn the "gesture" — the command shape.

---

## Memory Palaces (Method of Loci)

The **Method of Loci** (memory palace) is an ancient technique: associate information with locations in a familiar space.

### How It Works

1. Visualize a familiar building (your house, a temple)
2. Place items to remember at specific locations
3. To recall, mentally "walk through" the space
4. Items appear at their locations

### The Sims as Memory Palace

Playing The Sims naturally creates memory palaces:

- You remember where objects are
- You know which rooms serve which functions
- Character routines become spatial patterns
- The house layout encodes gameplay information

### MOOLLM Memory Palace

MOOLLM's **filesystem-as-world** is explicitly a memory palace:

```
adventure-4/
├── start/           # Where journeys begin
├── kitchen/         # Where sustenance lives
├── pub/             # Where community gathers
│   ├── bar/         # Behind-the-bar area
│   ├── stage/       # Performance space
│   └── cat-cave/    # Hidden sanctuary
├── maze/            # Where challenges lurk
└── end/             # Where conclusions live
```

The directory structure is the palace. Files are the items placed within rooms. Navigating directories is walking through the palace.

### iLoci: The Memory Palace App

Don Hopkins created **iLoci**, an iPad app implementing the Method of Loci:

- Users build virtual memory palaces
- Place items (images, text, audio) at locations
- Navigate through rooms to recall
- Pie menus for item placement and recall

**iLoci → MOOLLM Connection:**

| iLoci | MOOLLM |
|-------|--------|
| Room | Directory |
| Item | YAML file |
| Navigation | `GO` command / exits |
| Recall | `read_file` |
| Placement | `write_file` |

Both use spatial organization for information management.

---

## Adventure Map Navigation

Adventure games pioneered spatial narrative navigation:

### Classic Adventure (1976)

```
You are in a maze of twisty little passages, all alike.

EXITS: North, South, East
```

### MOOLLM Adventure Map

```yaml
# maze/room-3.yml
room:
  name: "Twisting Passage"
  description: "The walls curve unnaturally..."
  exits:
    north: room-4
    south: room-2
    east: dead-end
```

### Map as Navigation

The [maze/](../examples/adventure-4/maze/) directory contains interconnected rooms. The structure IS the map:

```
maze/
├── entrance.yml
├── room-1.yml
├── room-2.yml
├── room-3.yml
├── grue-den.yml
└── exit.yml
```

Character location is a **path**: `maze/room-3.yml`

Movement updates the path: `maze/room-3.yml` → `maze/room-4.yml`

### DreamScape

**ScriptX's DreamScape** (Kaleida Labs, 1994) used adventure map navigation for multimedia:

- Rooms connected by portals
- Objects with behaviors
- Navigation through a spatial narrative

MOOLLM inherits this: directories are rooms, files are objects, links are portals.

---

## Editors and Building Tools

### The Sims Build Mode

The Sims' Build and Buy modes are **editors** — tools for creating the simulation environment:

| Mode | Function | MOOLLM Equivalent |
|------|----------|-------------------|
| Build | Place walls, floors, doors | Create directories, ROOM.yml |
| Buy | Place objects | Create object YAML files |
| Live | Run simulation | LLM interaction |

### Reader = Writer

From HyperCard's core insight: **readers should be writers**.

In The Sims:
- Players build houses
- Players create characters
- Players arrange scenarios

In MOOLLM:
- Users edit YAML files
- Users create new rooms
- Users define new characters

The simulation is not consumed — it's co-created.

### TinyMUD Builder Commands

MOOLLM inherits [TinyMUD](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#tinymud--lambdamoo) builder commands:

```
@CREATE room "Kitchen"
@DESCRIBE room "A warm space with copper pots..."
@LINK room/exit/north TO pub
@CREATE object "stove" IN room
```

Every player is potentially a builder. The world expands through use.

### Edith: Live Editing

The Sims' **Edith** editor allowed live modification:

- Change object behaviors while game runs
- Inspect simulation state
- Modify values and see immediate effects

MOOLLM inherits this: edit a YAML file, and the LLM immediately sees the new state. No compile step. No restart.

See [sims-edith-editor.md](./sims-edith-editor.md) for details.

---

## Don Hopkins' Pie Menu History

Don Hopkins has implemented pie menus across numerous systems:

### Timeline

| Year | System | Notes |
|------|--------|-------|
| 1986 | Sun Window System | First implementation |
| 1988 | NeWS (Network extensible Window System) | PostScript-based |
| 1989 | HyperTIES | Hypermedia pie menus |
| 1991 | X11 SimCity | Open source implementation |
| 1995 | HyperLook | NeWS successor |
| 2000 | **The Sims** | 16+ million copies |
| 2008 | GTK/Gnome-Pie | Linux desktop |
| 2012 | Unity3D plugin | Game engine |
| 2015 | iLoci | Memory palace app |
| 2020 | Web/JavaScript | Browser-based |

### Key Implementations

**NeWS Pie Menus:** PostScript-programmable, extensible, networked. The "Display PostScript" vision of graphical computing.

**HyperTIES Pie Menus:** Hypermedia browser with embedded pie menus for link navigation. Early "browsing as spatial navigation."

**The Sims:** The most successful consumer deployment. Pie menus became synonymous with object interaction.

**Gnome-Pie:** Free software implementation for Linux desktops. Circular app launcher.

---

## Touchscreen Considerations

### The Nulling Problem

On touchscreens, your finger obscures the target. This is the "nulling problem":

- You can't see what you're pointing at
- Selection requires lifting finger to see, then re-targeting

### Full-Screen Pie Menus

Solution: make the pie menu full-screen:

```
┌────────────────────────┐
│                        │
│    [Option A]          │
│                        │
│ [Opt B]    ●    [Opt C]│
│          (touch)       │
│    [Option D]          │
│                        │
└────────────────────────┘
```

The entire screen becomes the menu. No precision pointing needed — just direction.

### Gesture Zones

Divide the screen into directional zones:

- Touch anywhere in upper-right = "Confirm"
- Touch anywhere in lower-left = "Cancel"

Large targets, no obscuration problem.

---

## MOOLLM Design Implications

### 1. Advertised Methods Are Pie Slices

Every `CARD.yml` is a pie menu definition:

```yaml
# The "pie" for this skill
advertised_methods:
  SLICE-1: ...
  SLICE-2: ...
  SLICE-3: ...
```

When the LLM "displays" available actions, it's rendering the pie.

### 2. Spatial Organization Matters

The filesystem layout creates a memory palace. Design directories like rooms in a meaningful building:

- Group related things spatially
- Use consistent naming
- Create logical navigation paths

### 3. Actions Should Be Gestural

Design commands to be **short and directional**:

```bash
# Good: feels like a gesture
GO north
TAKE lamp
TALK palm

# Bad: feels like a form
NAVIGATE_TO_LOCATION destination=north
ACQUIRE_OBJECT target=lamp
INITIATE_CONVERSATION partner=palm
```

### 4. Hierarchical Composition

Complex interactions decompose into levels:

```
Interact with bartender
  → [Social] [Order] [Games]
    → [Order]
      → [Drinks] [Food] [Buds]
        → [Drinks]
          → [Beer] [Cocktails] [Wine]
```

Each level is a navigation step. Keep it shallow (2-3 levels max).

---

## See Also

### MOOLLM Documents
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Full architecture
- [sims-design-index.md](./sims-design-index.md) — All Sims → MOOLLM documents
- [sims-edith-editor.md](./sims-edith-editor.md) — Live editing tools
- [sims-find-best-action.md](./sims-find-best-action.md) — Object advertisements → autonomy

### Skills
- [skills/card/](../skills/card/) — Advertised methods (the pie menu definition)
- [skills/room/](../skills/room/) — Spatial navigation (memory palace)
- [skills/adventure/](../skills/adventure/) — Map-based exploration
- [skills/action-queue/](../skills/action-queue/) — Action execution

### Examples
- [pub/menus/](../examples/adventure-4/pub/menus/) — Hierarchical menu structure
- [maze/](../examples/adventure-4/maze/) — Adventure map navigation

### External
- [Pie Menu FUD and Misconceptions](https://donhopkins.medium.com/pie-menu-fud-and-misconceptions-be8afc49d870) — Don Hopkins Medium article
- [Chaim Gingold's Play Design PhD Thesis](http://levitylab.com/cog/writing/play-design.pdf) — Original pie menu quote source
- [Understanding Comics](https://en.wikipedia.org/wiki/Understanding_Comics) — Scott McCloud's masking concept

---

## Conclusion

Pie menus in The Sims weren't just a UI choice — they were an architectural decision that unified:

- **Object model** (objects advertise verbs)
- **AI system** (characters choose from advertised verbs)
- **User interface** (verbs displayed radially)
- **Interaction design** (gestural, learnable, efficient)

MOOLLM inherits this unity:

- **CARD.yml** (objects advertise methods)
- **LLM** (understands method semantics)
- **Prose interface** (methods presented in context)
- **Skill composition** (hierarchical, navigable)

The Sims proved that pie menus work at massive scale. MOOLLM translates that insight into language: the LLM's "pie menu" is prose that radiates options from the interaction point.

---

*"Objects advertise verbs to character AI, so it is natural for the verbs to be arranged in a radial menu about objects."*

In MOOLLM: **Skills advertise methods to the LLM, so it is natural for the methods to be presented contextually in prose.**
