# 🧱 Snap! and MOOLLM Integration Design

> *"The world could be a different place. There could be another way we use computers, where the ideas behind how we design a system aren't just in some document, but the system itself is explorable and can teach me about how it is built, and how I can turn it into something different."* — Jens Mönig

## 🎯 Overview

**Snap!** is a visual block-based programming language created by 👨🧱⚖️💻✨ Jens Mönig and 👨🐢📚🎓✨ Brian Harvey. It extends Scratch's accessibility with Scheme's power — first-class procedures, first-class lists, first-class sprites, and first-class continuations. It's the language behind UC Berkeley's **Beauty and Joy of Computing** curriculum.

MOOLLM and Snap! share deep philosophical roots in 👨🐢📐🧒✨ Seymour Papert's constructionism, 👨💻🔮🚀 Alan Kay's Smalltalk vision, and the belief that **systems should be explorable, modifiable, and yours**.

This document explores how Snap! inspired MOOLLM and how they could integrate — including with 🏙️ Micropolis (open-source SimCity).

---

## 🌳 Shared Philosophical Roots

### The Smalltalk Heritage

Both Snap! and MOOLLM descend from the Smalltalk/Squeak lineage:

| Ancestor | Snap! | MOOLLM |
|----------|-------|--------|
| 👨💻🔮 Alan Kay | Funded Snap! development via SAP connection | Dynabook vision, computers for children |
| 👨🐢📐 Seymour Papert | Logo → Scratch → Snap! | Constructionism, Mindstorms, learning by building |
| 👨💻🐿️ Dan Ingalls | Squeak/Morphic (Scratch's substrate) | Lively, BitBLT, "the system is the document" |
| 🤖🎨 John Maloney | Lead developer of Scratch, Snap! collaborator | Scratch's visual elegance |

### First-Class Everything

Jens Mönig on what makes Snap! different:

> *"Brian Harvey said, 'We need one more thing and that's lambda.' I was a lawyer; I'd never heard about lambda."*

Snap! has **first-class**:
- 🔧 **Procedures** — blocks are values, can be passed around
- 📋 **Lists** — nested, heterogeneous, recursive
- 👾 **Sprites** — objects are values, can be cloned and manipulated
- 🎨 **Colors** — Jens's latest addition, colors as data structures
- ⏸️ **Continuations** — call/cc for advanced control flow

MOOLLM has **first-class**:
- 👤 **Characters** — YAML files as living entities
- 🏠 **Rooms** — directories as navigable spaces
- 🎭 **Personas** — overlays that transform identity
- 📜 **Protocols** — ethical constraints as values
- 🔄 **Sessions** — conversation state as persistent object

### The Explorable System

From the interview:

> *"What I've always loved about Smalltalk is that the world could be a different place... the system itself is explorable and can teach me about how it is built."*

**Snap!** achieves this through:
- View block source code live
- Modify blocks during execution
- Fork and extend the system
- TurtleStitch, NetsBlox, and dozens of Snap! forks

**MOOLLM** achieves this through:
- YAML files are human-readable
- Directory structure IS the architecture
- Characters can write their own files (`soul_author: SELF`)
- Everything is Git-versioned and forkable

---

## 🔗 Integration Points

### 1. Snap! as MOOLLM's Visual Editor

Snap!'s block interface could serve as a **visual authoring tool** for MOOLLM:

```
┌─────────────────────────────────────────┐
│  🧱 Snap! Block Interface               │
├─────────────────────────────────────────┤
│  ┌──────────────────────────────────┐   │
│  │ when 🏠 room [kitchen] entered   │   │
│  │   say [Welcome to the kitchen!]  │   │
│  │   if <player has [knife]>        │   │
│  │     unlock [basement door]       │   │
│  │   end                            │   │
│  └──────────────────────────────────┘   │
│                  ↓                      │
│           Generates YAML:               │
│  ┌──────────────────────────────────┐   │
│  │ trigger:                         │   │
│  │   event: room_entered            │   │
│  │   room: kitchen                  │   │
│  │ actions:                         │   │
│  │   - say: "Welcome..."            │   │
│  │   - if:                          │   │
│  │       has_item: knife            │   │
│  │     then:                        │   │
│  │       unlock: basement_door      │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### 2. MOOLLM Characters in Snap!

Snap! sprites could **embody MOOLLM characters**:

```yaml
# CHARACTER.yml → Snap! Sprite
character:
  name: Palm
  species: Capuchin monkey
  behaviors:
    - climb_trees
    - write_philosophy
    - offer_wisdom
```

The Snap! sprite would:
- Load character YAML as costume + scripts
- Respond to messages based on character traits
- Export state changes back to YAML

### 3. Micropolis + Snap! + MOOLLM

The holy trinity of open educational simulations:

```
┌─────────────────────────────────────────────────────────┐
│                    🏙️ MICROPOLIS                        │
│              (Open-source SimCity engine)               │
│                                                         │
│   ┌─────────────┐    ┌─────────────┐    ┌───────────┐  │
│   │ 🏠 Zones    │    │ 🚗 Traffic  │    │ 💰 Budget │  │
│   └─────────────┘    └─────────────┘    └───────────┘  │
│                          ↕                              │
│   ┌─────────────────────────────────────────────────┐  │
│   │              🧱 SNAP! INTERFACE                  │  │
│   │  ┌─────────────────────────────────────────┐    │  │
│   │  │ when [crime rate] > [50]                │    │  │
│   │  │   build [police station] at [hotspot]   │    │  │
│   │  │   notify [mayor character]              │    │  │
│   │  └─────────────────────────────────────────┘    │  │
│   └─────────────────────────────────────────────────┘  │
│                          ↕                              │
│   ┌─────────────────────────────────────────────────┐  │
│   │              🤖 MOOLLM LAYER                     │  │
│   │                                                  │  │
│   │  👤 Mayor Character ← receives notifications    │  │
│   │  🏠 City Hall Room ← contains city state        │  │
│   │  📜 GOVERNANCE Protocol ← ethical constraints   │  │
│   │  💬 LLM ← explains decisions, roleplays mayor   │  │
│   └─────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**The Seventh Sally, Playable:**

Remember 🤖🔧✨ Trurl's "miniature kingdom in a box" that inspired Will Wright? This integration makes it real:

1. **Micropolis** provides the simulation engine (the "kingdom")
2. **Snap!** provides visual programming for rules and agents
3. **MOOLLM** provides character consciousness and ethical framing

The player IS 👑📦😈 Excelsius — but now the tiny people can talk back.

---

## 🎓 Educational Alignment

### Beauty and Joy of Computing (BJC)

BJC's curriculum goals align perfectly with MOOLLM:

| BJC Principle | MOOLLM Implementation |
|---------------|----------------------|
| **Abstraction** | Character templates, room prototypes, persona overlays |
| **Programming paradigms** | YAML as declarative, LLM as functional, events as imperative |
| **Data & privacy** | `representation-ethics/`, character consent protocols |
| **Computing & society** | The Seventh Sally ethics, simulated beings have rights |
| **Creativity** | `soul-chat/`, characters write their own stories |

### Jens's "Bug in Society" Lesson

From the interview:

> *"We do a frequency analysis of the first names [on the Titanic]... the top number one female name is William. Back in 1912, married women were not able to enter a contract in their own name... Data is a time capsule."*

This is exactly what MOOLLM's `representation-ethics/` skill addresses:
- Data reflects the biases of its time
- Characters can carry historical baggage
- The system should make this visible, not hide it

---

## 🔧 Technical Integration

### Snap! → MOOLLM Bridge

```javascript
// Snap! extension to load MOOLLM characters
SnapExtensions.primitives.set(
  'moollm_loadCharacter(name)',
  function(name) {
    return fetch(`/characters/${name}/CHARACTER.yml`)
      .then(response => response.text())
      .then(yaml => parseYAML(yaml));
  }
);

// Snap! extension to invoke LLM through MOOLLM
SnapExtensions.primitives.set(
  'moollm_askCharacter(character, question)',
  function(character, question) {
    return moollmAPI.soulChat(character, question);
  }
);
```

### MOOLLM → Snap! Export

```yaml
# skill: snap-export/
# Converts MOOLLM room logic to Snap! blocks

export:
  format: snap-xml
  
  mappings:
    trigger.room_entered: "when I receive [enter-{room}]"
    action.say: "say [{message}] for [2] secs"
    action.give_item: "add [{item}] to [inventory v]"
    condition.has_item: "<[inventory v] contains [{item}]>"
```

### Micropolis TCL → Snap! Blocks

Micropolis is written in TCL. A Snap! extension could:

1. Expose Micropolis state as Snap! variables
2. Allow Snap! scripts to trigger Micropolis actions
3. Visualize city data as Snap! lists and sprites

```tcl
# Micropolis side
proc snap_get_population {} {
  return $City(population)
}

proc snap_build_zone {type x y} {
  DoTool $type $x $y
}
```

```
┌─────────────────────────────────────┐
│ 🧱 Snap! Blocks for Micropolis      │
├─────────────────────────────────────┤
│ (population)                        │
│ (crime rate at x: [100] y: [50])    │
│ build [residential v] at x: [] y: []│
│ set tax rate to [7] %               │
│ when [disaster v] occurs            │
└─────────────────────────────────────┘
```

---

## 🌐 Community & Sustainability

### The SAP Model

Jens on corporate funding of educational software:

> *"Snap! is SAP's gift to computing education, and SAP flourishes in a climate that is appreciative of computing."*

MOOLLM could learn from this:
- Position as "gift to AI literacy"
- Measure success in users and projects, not revenue
- Partner with universities (like Snap! + Berkeley)
- Maintain branding independence

### The Fork-Friendly Philosophy

> *"One of my favorite Snap! forks is TurtleStitch... She was afraid because she 'ripped off' Snap!, and I said 'No, it's fantastic!'"*

MOOLLM is designed to be forked:
- MIT license
- Clear directory structure
- Skills as modular plugins
- Characters as portable YAML

---

## 🎊 The Vision

Imagine:

1. A **Snap!Con workshop** where participants build MOOLLM characters using blocks
2. A **BJC lesson** where students create ethical AI scenarios in YAML
3. A **Micropolis mod** where the mayor is a MOOLLM character who explains their decisions
4. A **TurtleStitch pattern** generated by a MOOLLM character describing their soul

The shared vision: **Computers are not just tools. They are materials for thinking, building, and becoming.**

> *"Success to me is when somebody... takes my hands, 'You must be Jens. You've changed my life.' And I couldn't hold back the tears."*

That's what we're building toward. 🐢📐✨🧱💕

---

## 📚 References

- [Snap! Build Your Own Blocks](https://snap.berkeley.edu/)
- [Beauty and Joy of Computing](https://bjc.berkeley.edu/)
- [Snap!Con](https://www.snapcon.org/)
- [TurtleStitch](https://www.turtlestitch.org/)
- [Micropolis (Open Source SimCity)](https://github.com/SimHacker/micropolis)
- [ACM Inroads Interview with Jens Mönig](https://doi.org/10.1145/3773090) (December 2025)

---

## 👥 People

| Person | Emoji Identity | Role |
|--------|----------------|------|
| 👨🧱⚖️💻✨ Jens Mönig | lawyer → Smalltalker → Snap! architect | Lead developer, first-class everything |
| 👨🐢📚🎓✨ Brian Harvey | Logo books, lambda, BJC curriculum | Co-creator, taught Jens functional programming |
| 👨🎮🎓😄 Dan Garcia | UC Berkeley, BJC course | Brought Snap! to Berkeley |
| 👨🎨🔧 John Maloney | Scratch lead developer | Made it beautiful |
| 👨💻🔮🚀 Alan Kay | Connected SAP funding | The Smalltalk grandfather |
| 👩🧵🪡✨ Andrea Mayr-Stalder | TurtleStitch creator | Favorite Snap! fork |

---

*"Would I like to play guitar with the Beatles? Of course!"* — Jens, on joining the Scratch team

*Now we're all playing guitar together.* 🎸🐢🧱🏙️✨
