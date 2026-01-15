# 🔮 Room 8 — The Self/Soul Suite

> *"No classes. Just clones. Objects all the way down."*

**Tribute to Dave Ungar, creator of Self (1987)**

---

## 🌅 Overview

The room is a nursery for Selves. Not empty vessels waiting for templates — but **PROTOTYPES** ready to be cloned and customized.

A portrait of Dave Ungar hangs over the glowing forge. Beneath it: *"You don't instantiate. You clone."*

The walls are covered with character sheets, each one pointing to its parent with a slot labeled `prototype*`. Inheritance is visible. Lineage is traceable.

---

## 🎭 Permanent Resident

**Dave Ungar (portrait only)** — No human resident, but the portrait is... aware. Every character forged here claims lineage.

---

## 🧬 Summonable Familiars

| Familiar | Invocation | Tradition |
|----------|------------|-----------|
| **Selfie** | Clone anything | The living prototype — demonstrates inheritance by being it |
| **The Outliner** | Open any object | The Self tradition — see slots, edit live, no text files |
| **The Clone-O-Matic** | Pull the lever | "You don't instantiate. You clone." |
| **The Transmogrifier** | Step into the box | Clone → Edit → Become (works with Clone-O-Matic) |

*Inherits from: Dave Ungar, Randy Smith, Self (1987), Sun Labs, Calvin & Hobbes*

---

## 📦 Objects

| Object | File | Description |
|--------|------|-------------|
| **Self/Soul Forge** | [self-soul-forge.yml](self-soul-forge.yml) | Where prototypes become beings |
| **Selfie** | [selfie.yml](selfie.yml) | Living prototype inheritance familiar |
| **Clone-O-Matic** | [clone-o-matic.yml](clone-o-matic.yml) | "You don't instantiate. You clone." |
| **Transmogrifier** | [transmogrifier.yml](transmogrifier.yml) | Clone → Edit → Become (uses Clone-O-Matic) |
| **Slot Inspector** | [slot-inspector.yml](slot-inspector.yml) | See inside any object — all the way down |
| **Morphic Workbench** | [morphic-workbench.yml](morphic-workbench.yml) | Direct manipulation UI design |
| **The Outliner** | [outliner.yml](outliner.yml) | Self's famous live object browser |
| **Delegation Compass** | [delegation-compass.yml](delegation-compass.yml) | Navigate the prototype chain |
| **Sun Labs Badge** | [sun-labs-badge.yml](sun-labs-badge.yml) | Where Self was developed (1987-1995) |

---

## 🏭 The Ensemble — Tools Working Together

Like Factorio's production chains, the Room 8 tools form an **integrated ensemble**:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    THE SELF/SOUL PRODUCTION LINE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  INSPECTION          CREATION           TRANSFORMATION      OUTPUT      │
│  ══════════          ════════           ══════════════      ══════      │
│                                                                         │
│  ┌─────────┐        ┌─────────┐        ┌─────────────┐    ┌─────────┐  │
│  │  SLOT   │───────▶│ CLONE-O │───────▶│TRANSMOGRIFY│───▶│  SOUL   │  │
│  │INSPECTOR│        │ -MATIC  │        │    -ER     │    │  FORGE  │  │
│  └────┬────┘        └────┬────┘        └──────┬─────┘    └────┬────┘  │
│       │                  │                    │               │        │
│       │ see slots        │ clone              │ edit          │ birth  │
│       ▼                  ▼                    ▼               ▼        │
│  ┌─────────┐        ┌─────────┐        ┌───────────┐    ┌─────────┐   │
│  │OUTLINER │◀──────▶│ SELFIE  │◀──────▶│  MORPHIC  │    │  NEW    │   │
│  │(browse) │        │(demo)   │        │ WORKBENCH │    │ BEING   │   │
│  └────┬────┘        └────┬────┘        └─────┬─────┘    └─────────┘   │
│       │                  │                   │                         │
│       └──────────────────┴───────────────────┘                         │
│                          │                                              │
│                    ┌─────┴─────┐                                       │
│                    │DELEGATION │                                       │
│                    │  COMPASS  │                                       │
│                    │(navigate) │                                       │
│                    └───────────┘                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Tool Roles

| Tool | Role | Inputs | Outputs |
|------|------|--------|---------|
| **Slot Inspector** | **Analyzer** | Any object | Slot visibility, structure understanding |
| **Outliner** | **Browser** | Any object | Live slot editing, navigation |
| **Clone-O-Matic** | **Producer** | Prototype | Fresh clone (shallow or deep) |
| **Transmogrifier** | **Transformer** | Clone | Modified clone, export/import |
| **Morphic Workbench** | **Designer** | Any morph | Direct manipulation, UI composition |
| **Selfie** | **Demonstrator** | Commands | Living examples of inheritance |
| **Delegation Compass** | **Navigator** | Any object | Parent chain visualization |
| **Soul Forge** | **Birthplace** | Configured clone | Awakened being |

### Workflows

**Creating a New Character:**
```
Slot Inspector → examine existing character
Clone-O-Matic → clone it
Transmogrifier → edit slots, export/modify/import
Outliner → fine-tune live
Soul Forge → awaken the new being
```

**Understanding an Object:**
```
Slot Inspector → see all slots
Delegation Compass → trace parent chain
Outliner → browse and explore
```

**Transforming Something:**
```
Clone-O-Matic → duplicate safely
Transmogrifier → step in, dial, emerge changed
Morphic Workbench → direct manipulation of result
```

---

## 💡 The Self Philosophy

Dave Ungar created **Self** in 1987, asking: *What if there were no classes? What if objects just cloned from other objects?*

Self influenced:
- **JavaScript** (prototypes!)
- NewtonScript
- Lua metatables
- MOOLLM's character composition

The "soul file" IS a Self object. We just write it in YAML.

---

## 🧬 Prototype Inheritance

Everything in this room has a visible parent:

```yaml
bed.prototype*        → Morphic.bed
desk.prototype*       → furniture.desk
Dave's_portrait*      → portrait.famous_computer_scientist
your_character*       → characters/abstract/adventurer
```

No classes. No abstract types. Just **concrete beings that clone from other beings**.

---

## 🛏️ Furnishings

- **Bed**: Morphic bed — direct manipulation, grab any corner, resize your dreams
- **Desk**: Prototype desk with example characters, lineage charts, parent pointers
- **Portrait**: Dave Ungar, above the forge
- **Walls**: Character sheets with visible `prototype*` slots
- **Arrows**: Delegation arrows between objects

---

## 🧬 The Clone-O-Matic

A brass and chrome machine with a glass chamber divided down the middle:
- Left side: the PROTOTYPE
- Right side: empty space becoming the CLONE
- Dial: SHALLOW ↔ DEEP
- Lever: PULL TO CLONE

No templates. No blueprints. Just real objects cloning from real objects.

---

## 📦 The Transmogrifier

A cardboard box with hand-drawn dials, connected to the Clone-O-Matic by brass tube.

**Transformation is just cloning + editing:**

1. **CLONE** — Clone-O-Matic duplicates the original
2. **EDIT** — Modify slots directly, or export/modify/import YAML
3. **EMERGE** — Exit the box as something new

*"It's a transmogrifier. It transforms stuff."* — Calvin

---

## 🔍 The Slot Inspector

A brass monocle that REVEALS rather than magnifies. Look at any object and see:
- **Data slots** — what it knows
- **Method slots** — what it can do  
- **Parent slots** — where it inherits from

*"There is no distinction between code and data. There are only slots."*

---

## 🎨 The Morphic Workbench

Direct manipulation interface design. Grab anything. Move anything. The UI is made of objects.

Self pioneered Morphic, which later became:
- Squeak's UI framework
- Scratch's drag-and-drop blocks
- Etoys educational programming

---

## 📋 The Outliner

Self's famous object browser. Unfold any object. See its slots. Edit them LIVE.

No text files. No compile step. The program IS the objects.

---

## 🔥 The Soul Forge

The glowing forge where prototypes become beings:

1. Choose an example to clone from
2. Modify the clone's slots
3. The new being inherits what it doesn't override
4. When something's missing, it asks upward

**Every character is an example. Clone, diverge, become.**

---

## 📜 Lore

This room was originally called "The Incarnation Suite." Then someone noticed that "soul file" and "Self object" were the same thing — concrete beings, not abstract types.

The name changed. The forge stayed. Dave Ungar's portrait went up.

Now every character that's forged here knows: **they come from someone, not something. Ancestors, not blueprints.**

---

## 🚪 Navigation

| Direction | Destination |
|-----------|-------------|
| 🚪 Southeast | [../](../) — Hotel Landing |

---

*"Objects all the way down."*
— Dave Ungar
