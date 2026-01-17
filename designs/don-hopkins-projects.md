# Don Hopkins Projects → MOOLLM

> *The tools and ideas that led to MOOLLM*
> *PostScript, NeWS, HyperTIES, SimCity, The Sims → MOOLLM*

## The Thread

MOOLLM didn't appear from nowhere. It's the culmination of decades of work in interactive graphics, spatial computing, user interface design, and language-based systems. This document traces the projects and papers that directly influenced MOOLLM's design.

---

## Document Index

- [The Thread](#the-thread)
- [NeWS and PostScript Programming](#news-and-postscript-programming)
- [PSIBER Space Deck](#psiber-space-deck)
- [The Pseudo Scientific Visualizer](#the-pseudo-scientific-visualizer)
- [HyperTIES](#hyperties)
- [HyperLook and HyperNews](#hyperlook-and-hypernews)
- [PizzaTool](#pizzatool)
- [X11 SimCity](#x11-simcity)
- [SimCity Open Source (Micropolis)](#simcity-open-source-micropolis)
- [The Sims Contributions](#the-sims-contributions)
- [iLoci Memory Palace](#iloci-memory-palace)
- [The Unifying Themes](#the-unifying-themes)
- [See Also](#see-also)

---

## NeWS and PostScript Programming

**NeWS (Network extensible Window System)** was Sun Microsystems' window system based on PostScript (1986-1993).

### The Vision

While X11 treated the display as a dumb bitmap server, NeWS was **programmable**:

- Display PostScript on the server
- Clients send programs, not pixels
- Server executes code, returns results
- Objects live on the server, respond to events

### MOOLLM Connection

| NeWS Concept | MOOLLM Parallel |
|--------------|-----------------|
| Send program, not data | Send skill, not steps |
| Server has intelligence | LLM understands context |
| Objects respond to events | Characters respond to events |
| Extensible at runtime | Skills compose at runtime |

The core insight: **you send a program to the interpreter, not a data structure to a renderer.**

MOOLLM sends skill descriptions to the LLM. The LLM interprets them. This is the NeWS model applied to language.

### Medium Articles
- [The Shape of Psiber Space](https://donhopkins.medium.com/the-shape-of-psiber-space-the-pseudo-scientific-visualizer-1990-549e008d6fbc)
- [NeWS Programming](https://donhopkins.medium.com/hypertalk-and-hyperlook-open-software-for-open-minds-baf23c858fcf)

---

## PSIBER Space Deck

**PSIBER (Pseudo Scientific Interactive Bug Eradication Routines)** was a visual PostScript debugger and data structure editor for NeWS.

### The Tool

- Visualize PostScript data structures as graphical trees
- Edit running programs interactively
- Navigate data like navigating space
- Debug by direct manipulation

### MOOLLM Connection

| PSIBER | MOOLLM |
|--------|--------|
| Visualize data structures | Read YAML files |
| Edit running programs | Edit YAML during session |
| Navigate structure as space | Navigate filesystem as world |
| Debug by looking | Inspect state by reading |

PSIBER proved that **data can be spatial** — you navigate it, you edit it in place, you see relationships visually.

MOOLLM's filesystem-as-world is the same insight: directories are navigable space, files are editable objects, the LLM "sees" state by reading.

---

## The Pseudo Scientific Visualizer

An object browser for macroscopic data examination:

- Browse complex object hierarchies
- See relationships between objects
- Navigate through references and slots
- Examine data at any level of detail

### MOOLLM Connection

The [skills/visualizer/](../skills/visualizer/) skill inherits this. When the LLM describes a complex object:

```markdown
## Palm's Character Overview

Palm is a capuchin monkey philosopher:
├── Location: pub/stage/palm-nook/
├── Relationships:
│   ├── Don Hopkins (Godfather)
│   ├── Maurice (Friend, big cat)
│   └── Bumblewick (Adventure partner)
├── Possessions:
│   └── Study:
│       ├── infinite-typewriters.yml
│       ├── desk.yml
│       └── cushion.yml
└── Skills:
    ├── Philosophy
    ├── Writing
    └── Typing (infinite monkeys)
```

This is the Pseudo Scientific Visualizer — prose-based, LLM-rendered, but structurally the same as the NeWS graphical browser.

---

## HyperTIES

**HyperTIES** (The Interactive Encyclopedia System) was an early hypermedia browser developed at the University of Maryland (1983-1990).

### Innovations

1. **Embedded links** — Links appear in the text, not in separate menus
2. **Definition preview** — Hover over a term, see definition before navigating
3. **Pie menu navigation** — Radial menus for link selection
4. **Authoring in Emacs** — Hypertext creation was text-based

### MOOLLM Connection

| HyperTIES | MOOLLM |
|-----------|--------|
| Embedded links | [Empathic paths](../skills/empathic-templates/) |
| Definition preview | Metadata sidecar files |
| Pie menus | CARD.yml advertised methods |
| Emacs authoring | YAML/Markdown editing |

HyperTIES showed that **hypertext is natural** — links embedded in prose feel intuitive. MOOLLM's skill references, file links, and path navigation all inherit this.

### The "Humane Links" Connection

MOOLLM's [empathic-templates](../skills/empathic-templates/) skill implements "humane links":

- Links are robust (handle renames, moves)
- Links are contextual (semantic resolution)
- Links work both ways (can trace references)

This descends directly from HyperTIES' embedded link philosophy.

---

## HyperLook and HyperNews

**HyperLook** was a NeWS-based hypertext system combining HyperCard-like functionality with NeWS graphics.

**HyperNews** extended this to networked, collaborative hypertext.

### The "Axis of Eval"

Don Hopkins developed the **Axis of Evaluation** concept in HyperLook:

```
     Code
      │
      ├── Evaluates to behavior
      │
Graphics ────────── Data
      │
      ├── Renders visually
      │
      ▼
    Output
```

Programs, graphics, and data are all **equally interpretable**. PostScript demonstrated this: text describes graphics describes behavior.

### MOOLLM's Axis

```
     Skills (Code)
          │
          ├── LLM interprets
          │
Prose (Graphics) ────────── YAML (Data)
          │
          ├── LLM renders as narrative
          │
          ▼
    Response (Output)
```

The LLM evaluates skills like code, renders prose like graphics, processes YAML like data. Same axis, language as the universal medium.

### Medium Article
- [HyperTalk and HyperLook: Open Software for Open Minds](https://donhopkins.medium.com/hypertalk-and-hyperlook-open-software-for-open-minds-baf23c858fcf)

---

## PizzaTool

**PizzaTool** was a NeWS application for ordering pizza, demonstrating PostScript's graphics and networking capabilities.

### Why It Matters

PizzaTool showed that:

1. **Applications can be fun** — Not everything must be serious
2. **Network + graphics work together** — Send order over network, render pizza visually
3. **Objects have behaviors** — Toppings interact, prices calculate
4. **Users are in control** — Customizable, explorable

### MOOLLM Connection

The spirit of PizzaTool lives in MOOLLM's adventure system:

- The [pub/menus/](../examples/adventure-4/pub/menus/) directory is PizzaTool for cannabis and drinks
- Users customize orders (strain, amount, preparation)
- Objects have behaviors (terpene effects, pairing suggestions)
- The LLM renders the "pizza" as narrative

```yaml
# pub/menus/buds.yml - PizzaTool for weed
strains:
  sour-diesel:
    type: sativa
    effects: [energetic, creative]
    pairs_with: [coffee, conversation]
    
  purple-kush:
    type: indica
    effects: [relaxed, sleepy]
    pairs_with: [sunset, cushion]
```

Same pattern: customizable objects, rendered interaction, fun application.

---

## X11 SimCity

Don Hopkins ported SimCity to X11 Unix systems (1992), making it the first open-source SimCity predecessor.

### Innovations

- Pie menus for tool selection
- Network play support
- Customizable city parameters
- Educational version for OLPC

### The Simulator Effect

Will Wright's insight that SimCity demonstrated:

> "People don't just play SimCity — they start *thinking* like urban planners. The game becomes a mental model."

This is the **Simulator Effect**: simulations shape how people understand systems.

### MOOLLM Connection

MOOLLM leverages the Simulator Effect:

- Users don't just interact with characters — they start thinking like simulation designers
- The LLM's behavior becomes a mental model for how agents work
- Playing with YAML shapes how people think about AI systems

---

## SimCity Open Source (Micropolis)

In 2008, Don Hopkins open-sourced SimCity as **Micropolis** for the One Laptop Per Child (OLPC) project.

### The Story

Chaim Gingold helped broker the open-sourcing. The process required:

1. Stripping EA branding
2. Renaming to Micropolis
3. Releasing under GPL
4. Making it educational

### MOOLLM Connection

Micropolis proved that:

1. **Commercial software can become open** — With care and negotiation
2. **Games can be educational** — SimCity taught urban planning
3. **Open source enables adaptation** — Micropolis runs on OLPC, Raspberry Pi, web

MOOLLM is open source from the start. The [examples/adventure-4/](../examples/adventure-4/) world is freely modifiable. Anyone can create new adventures.

---

## The Sims Contributions

Don Hopkins worked on The Sims at Maxis, implementing:

### Pie Menus

The iconic Sims pie menus that made the game accessible. See [sims-pie-menus.md](./sims/sims-pie-menus.md).

### Object Architecture Extensions

Work on the object system, extending how objects advertise behaviors and interact.

### Character Animation

Contributions to the character system and animation pipeline.

### The Key Insights

From The Sims work:

1. **Objects should advertise capabilities** → CARD.yml
2. **Pie menus unify UI and AI** → Advertised methods
3. **Simulation should be inspectable** → YAML files
4. **Play and creation should be seamless** → Filesystem editing

See [sims-design-index.md](./sims/sims-design-index.md) for complete coverage.

---

## iLoci Memory Palace

**iLoci** is an iPad app implementing the Method of Loci (memory palace technique).

### The App

- Build virtual memory palaces
- Place items (text, images, audio) at locations
- Navigate through rooms to recall
- Pie menus for item manipulation

### MOOLLM Connection

| iLoci Feature | MOOLLM Equivalent |
|---------------|-------------------|
| Virtual rooms | Directories |
| Placed items | YAML files |
| Room navigation | `GO` command / exits |
| Item recall | `read_file` |
| Item placement | `write_file` |
| Pie menu selection | CARD.yml methods |

MOOLLM's filesystem-as-world IS a memory palace:

```
adventure-4/
├── start/        # Entrance hall
├── kitchen/      # Sustenance room  
├── pub/          # Gathering place
├── maze/         # Challenge area
└── end/          # Completion space
```

Navigate directories to "remember" where things are. Place files to "store" items. The spatial organization aids recall.

### Connection to Dasher

iLoci connects to **Dasher**, the gesture-based text entry system:

- Navigate in concept space
- Direction = meaning
- Continuous movement = composition

MOOLLM's command navigation works similarly — users move through concept space with prose.

---

## The Unifying Themes

### 1. Language as Universal Medium

From PostScript through The Sims to LLMs:

- **PostScript**: Text describes graphics
- **NeWS**: Programs are transmitted as text
- **Skills**: Prose describes behaviors
- **LLMs**: Language is computation

### 2. Spatial is Natural

From PSIBER through iLoci to MOOLLM:

- **Data as space**: Navigate structures like rooms
- **Memory is spatial**: Location aids recall
- **Navigation is interaction**: Moving IS selecting

### 3. Objects Advertise Capabilities

From The Sims through MOOLLM:

- Objects declare what they can do
- Users/AI choose from advertisements
- Pie menus display advertisements
- CARD.yml formalizes advertisements

### 4. Programs, Not Data

From NeWS through MOOLLM:

- Send program to interpreter, not data to renderer
- The server/LLM has intelligence
- Client describes intent, server executes
- This is the key shift

### 5. Reader = Writer

From HyperCard through The Sims through MOOLLM:

- Users create, not just consume
- Editing is natural, not special
- The world expands through use
- Play → Learn → Lift

---

## The Lineage

```
1985: PostScript         — Text is graphics
      │
1987: NeWS               — Send programs, not pixels
      │
1988: PSIBER             — Data is spatial
      │
1989: HyperTIES          — Embedded hypertext
      │
1990: HyperLook          — Axis of Evaluation
      │
1992: X11 SimCity        — Pie menus + simulation
      │
1994: ScriptX            — DreamScape navigation
      │
2000: The Sims           — Objects advertise verbs
      │
2008: Micropolis         — Open source simulation
      │
2015: iLoci              — Filesystem as memory palace
      │
2025: MOOLLM             — Skills as programs, LLM as VM
```

Each step builds on the last. MOOLLM is the synthesis.

---

## See Also

### MOOLLM Documents
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Complete philosophy
- [sims-design-index.md](./sims/sims-design-index.md) — All Sims influences
- [simcity-multiplayer-micropolis.md](./sims/simcity-multiplayer-micropolis.md) — Multiplayer SimCity, OLPC, constructionist education
- [sims-pie-menus.md](./sims/sims-pie-menus.md) — Pie menu deep dive
- [sims-edith-editor.md](./sims/sims-edith-editor.md) — Live debugging (PSIBER lineage)
- [stanza-notes.md](./stanza-notes.md) — Linguistic motherboard

### Skills
- [skills/visualizer/](../skills/visualizer/) — PSIBER's heir
- [skills/memory-palace/](../skills/memory-palace/) — iLoci's heir
- [skills/card/](../skills/card/) — Object advertisements
- [skills/empathic-templates/](../skills/empathic-templates/) — HyperTIES links

### External
- [Pie Menu FUD and Misconceptions](https://donhopkins.medium.com/pie-menu-fud-and-misconceptions-be8afc49d870)
- [The Shape of Psiber Space](https://donhopkins.medium.com/the-shape-of-psiber-space-the-pseudo-scientific-visualizer-1990-549e008d6fbc)
- [HyperTalk and HyperLook](https://donhopkins.medium.com/hypertalk-and-hyperlook-open-software-for-open-minds-baf23c858fcf)

---

## Conclusion

MOOLLM isn't just inspired by The Sims — it's the culmination of 40 years of work in language-based computing, spatial interfaces, and user empowerment.

The thread runs from PostScript ("text is graphics") through NeWS ("send programs") through PSIBER ("navigate data") through The Sims ("objects advertise") to MOOLLM ("skills are programs, LLM is VM").

Each step made computing more accessible, more spatial, more language-based, more empowering. MOOLLM is the current end of that thread — where language models finally make the "linguistic motherboard" vision real.

---

*"The best way to predict the future is to invent it."*
*— Alan Kay*

*"I've been inventing it for forty years. MOOLLM is what it looks like."*
*— The trajectory*
