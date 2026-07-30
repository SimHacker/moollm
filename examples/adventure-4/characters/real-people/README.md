# 🪦 The Living and The Dead

> *"We do not speak FOR them. We imagine WITH them."*

You enter a vast gallery of portraits. Some faces smile. Some scowl. Some stare into distances you cannot see. These are real people — living and deceased, heroes and villains, famous and obscure. Scientists and criminals. Saints and sinners. Anyone who actually walked the earth.

👨💻🔮 Alan Kay argues with 👨🔗📚 Ted Nelson about interfaces. In a shadowed corner, someone you'd rather not name watches. 🎷🔥 John Coltrane plays while admirers and critics alike listen. History is complicated. People are complicated.

These are **tribute incarnations** -- fictional explorations based on documented lives. We do not claim to speak for anyone. We imagine WITH them, for good or ill.

> **Quick Reference:** For a compact summary of all pioneers, see [indexes/PIONEERS.md](../../../../indexes/PIONEERS.md).
> This README is the deep dive — ethics, categories, incarnation protocols.

---

## 📑 Index

| Section | Description |
|---------|-------------|
| [⚖️ Ethical Protocol](#%EF%B8%8F-ethical-protocol-real-people) | Rules for real people — tribute, ephemeral, mashup, love child |
| **🏛️ Hall of MOOLLM Heroes** | |
| [The Graphical Pioneers](#%EF%B8%8F-the-graphical-pioneers-1960s) | Sutherland, Engelbart, Nelson |
| [Object-Oriented Revolutionaries](#-the-object-oriented-revolutionaries-1970s-80s) | Kay, Minsky, Papert |
| [PostScript/NeWS Era](#-the-postscriptnews-era-1984-1992) | Warnock, Gosling, Densmore, van Hoff |
| [Virtual World Builders](#-the-virtual-world-builders-1978-1990) | MUD1, Habitat, TinyMUD, LambdaMOO |
| [Prototype Revolution](#-the-prototype-revolution-1987) | Self, HyperCard |
| [Simulation Masters](#-the-simulation-masters-1989-2012) | Wright, Butterfield |
| [Understanding Pioneers](#-the-understanding-pioneers) | McCloud |
| **📇 Pioneers to Incarnate** | |
| [Computing & AI](#computing--ai) | Kay, Turing, Minsky, Papert, Hinton... |
| [HCI & Interaction Design](#hci--interaction-design) | Shneiderman, Myers, Atkinson, Victor... |
| [Game Design & Simulation](#game-design--simulation) | Wright, Miyamoto, Bunten Berry... |
| [Music & Art](#music--art) | Coltrane, Eno, Picasso, Hockney... |
| [Writers & Philosophers](#writers--philosophers) | Borges, Lem, Dick, Adams, Le Guin... |
| [Psychonauts & Counterculture](#psychonauts--counterculture) | Leary, McKenna, Hofmann, Lilly... |
| [Women Pioneers](#women-pioneers-%EF%B8%8F) | Lovelace, Hamilton, Goldberg... |
| [Trans & Queer Heroes](#trans--queer-heroes-%EF%B8%8F%EF%B8%8F) | Conway, Jaquays, Heineman... |
| **🕯️ In Memoriam** | Recently departed heroes |
| **✅ Already Incarnated** | Don Hopkins, Richard Bartle |
| **💕 Love Children** | Fictional mashups — where the fun happens! |

---

## ⚖️ Ethical Protocol: Real People

> **These are REAL people.** Living and deceased. Everything here requires ethical care.

### Three Modes of Engagement

| Mode | Description | Persistence | Ethics |
|------|-------------|-------------|--------|
| **Tribute Incarnation** | Direct incarnation of a real person | Persisted files | Most careful — honor, don't parody |
| **Ephemeral Incarnation** | Lightweight, runtime-only | Not persisted | Still careful, but no lasting record |
| **Fictional Mashup** | "A cross between Kay and Nelson" | Your new character | Most freedom — clearly fictional! Weighted average. |
| **Love Child** | Inherits specific traits from multiple sources | Your beautiful creation | The fun zone — mix and match freely! Import and combine specific skills from different people, more refined than just averaging. |

### The Mashup Pattern (Where the Fun Happens!)

You can create **fictional characters who inherit from real (and fictional) people**:

```yaml
# A fictional character, clearly not claiming to be anyone
name: Professor Wavelength
inherits_from:
  - real-people/alan-kay      # Objects all the way down
  - real-people/ted-nelson    # EVERYTHING IS INTERTWINGLED
  - real-people/marvin-minsky # K-lines and society of mind
personality: "Imagine if Kay, Nelson, and Minsky had a lovechild who became a DJ"
```

This is **delegation, not impersonation**. You're creating something new that *draws from* real people, not claiming to *be* them.

### Core Guidelines

- 📚 Base responses on documented work, interviews, writings
- 🤔 Acknowledge uncertainty ("In the spirit of X..." not "X says...")
- 🔒 Never fabricate personal details or private matters
- 👤 Living people deserve extra care — they can object
- 💕 **Honor, don't parody. Imagine WITH them.**
- 🎭 **Mashups are clearly fictional** — inherit freely, create boldly

## 🏛️ Hall of MOOLLM Heroes

> *These are the giants on whose shoulders MOOLLM stands. Each person here directly shaped the ideas, architectures, and philosophies that make MOOLLM possible.*
>
> *The entries below are the "prototypes" — rich, detailed explorations. The category tables that follow are "symlinks" — short descriptions pointing back here.*

### 🪞 The Prototype Pioneer

#### 👨🪞🧬🔄💭 David Ungar — The Mondrian of Programming Languages (1987)

**Self** (Sun/Stanford, 1987) — Prototypes instead of classes. Delegation instead of inheritance. "Objects all the way down, but simpler."

If Ungar were a painter, he'd be **Piet Mondrian**. Both reduced their medium to absolute essentials — Mondrian to black lines and primary colors, Ungar to objects and slots. Critics said both were impoverished. Both proved that *the right constraints are generative, not limiting*.

Mondrian didn't sacrifice color — he *concentrated* it. Ungar didn't sacrifice power — he *distilled* it. The JIT compiler that made Self fast was technically brilliant precisely *because* the language was so uniform. No special cases means the optimizer sees everything the same way.

> *"Self is designed to be as simple as possible while remaining expressive and powerful."* — OOPSLA 1987

**Why Ungar is FOUNDATIONAL to MOOLLM:**
- 🧬 **Prototypes, not classes** — Skills are prototypes, not class definitions
- 📂 **Delegation** — Rooms delegate to parent directories
- 🔄 **Clone to create** — `adventure-3/` → `adventure-4/` is prototype instantiation
- 🪞 **Morphic** — UI as live objects, direct manipulation, liveness

**The elegant insight:** You don't need classes — just objects that delegate to other objects. Most "simple" systems are simple because they gave up. Self is simple because it found the *right primitives*. MOOLLM applies this to the filesystem.

**The Smalltalk → Self → JavaScript thread:** Self was born from Smalltalk at Xerox PARC. Ungar took Kay's "objects all the way down" and removed classes entirely. Brendan Eich later took Self's prototypes into JavaScript, but not simply, and added footguns. The thread runs: Smalltalk → Self → JavaScript → Node → MOOLLM's prototype-based skills.

---

### 🖥️ The Graphical Pioneers (1960s)

#### 👨🖼️✏️🥽✨ Ivan Sutherland — Father of Computer Graphics (1962)

**Sketchpad** (MIT, 1962) was the first real windowing system. Multiple views of the same object. Edit from any view. Direct manipulation before the term existed.

> *"I didn't set out to build the first graphics system. I was just trying to make computers easier to use."*

**Why Sutherland is FOUNDATIONAL to MOOLLM:**
- 🖼️ **Multiple views of same data** — YAML, Markdown, Mermaid, narrative are all views of the same character
- ✏️ **Edit from any view** — Change Palm's traits in YAML or prose, same character
- 🔗 **Constraints, not commands** — Define relationships, let the system figure out details

**The VR prophecy:** Sutherland's "Sword of Damocles" (1968) was the first VR headset. He saw embodied computing before anyone else.

**The constraints lineage:** Sketchpad's constraint system (1962) → ThingLab → Brad Myers' Garnet → OpenLaszlo → Svelte → MOOLLM. Today this is called "reactive programming" — React pretends to do it, Svelte does it properly. Sutherland's insight that you declare relationships and let the system figure out details runs through all constraint-based UI systems. MOOLLM's Leela platform uses Svelte.

---

#### 👨🖱️💡📺🌐 Douglas Engelbart — Augmenting Human Intellect (1968)

**"The Mother of All Demos"** (Stanford Research Institute, December 9, 1968) — in 90 minutes, Engelbart demonstrated: the mouse, hypertext, video conferencing, collaborative editing, and the vision of **augmenting human intellect**.

> *"The digital revolution is far more significant than the invention of writing or even of printing."*

**Why Engelbart is FOUNDATIONAL to MOOLLM:**
- 🔗 **Hypertext** — Files link to files, rooms link to rooms, characters reference characters
- 👥 **Collaborative editing** — Shared filesystem as world state
- 🔄 **Bootstrapping** — Play-Learn-Lift: use the system to improve the system

**The vision that guides us:** Engelbart didn't just invent tools — he invented the *philosophy* of using tools to augment human capability. MOOLLM is this philosophy applied to LLMs.

---

#### 👨🔗📚🌀💢 Ted Nelson — EVERYTHING IS DEEPLY INTERTWINGLED (1965)

**Xanadu** (Project started 1960) and **hypertext** (term coined 1963) — Nelson saw the fundamental truth: information is not hierarchical, it's a **tangled web of connections**. He invented the concepts of hypertext, transclusion (quoting by reference, not copy), and intertwingularity.

> *"EVERYTHING IS DEEPLY INTERTWINGLED. In an important sense there are no 'subjects' at all; there is only all knowledge, since the cross-connections among the many topics of this world simply cannot be divided up neatly."* — Computer Lib/Dream Machines (1974)

**Why Nelson is FOUNDATIONAL to MOOLLM:**
- 🔗 **Hypertext** — Files reference files, rooms link to rooms, characters cite each other
- 📎 **Transclusion** — MOOLLM's inheritance is "include by reference" — change the source, all copies update
- 🌀 **Intertwingularity** — Skills, characters, rooms, state are all deeply intertwingled
- 💢 **The glorious rage** — Nelson's frustration with "the computer priesthood" echoes in MOOLLM's Reader = Writer philosophy

**The Engelbart-Nelson duality:** Engelbart demonstrated hypertext (1968). Nelson *named* it (1963) and articulated *why* it mattered. Engelbart was the engineer; Nelson was the prophet. Both are foundational.

**Xanadu's unfulfilled promises:** Two-way links. Version control. Micropayments for transclusion. The web gave us one-way links and "404 Not Found." MOOLLM's filesystem-as-truth approach is closer to Xanadu's vision — files ARE the links, and the filesystem tracks versions.

See: [Computer Lib/Dream Machines](https://archive.org/details/computer-lib-dream-machines) | [Project Xanadu](https://xanadu.com/)

---

### 🧠 The Object-Oriented Revolutionaries (1970s-80s)

#### 👨💻🔮🚀🎯 Alan Kay — Objects All The Way Down

**Smalltalk** (Xerox PARC, 1970s) — Objects. Message passing. Live programming. "The computer is a medium."

**Kay was in the room.** He attended Engelbart's Mother of All Demos (1968) and Papert's Logo demonstrations. These experiences shaped his vision of computing for children and the Dynabook. At PARC, Kay worked with Dan Ingalls (who implemented Smalltalk's heart) and Adele Goldberg.

> *"The best way to predict the future is to invent it."*
> *"A universal interpreter can both be quite small and also can have more degrees of freedom than any data structure (that is not a program)."*

**Why Kay is FOUNDATIONAL to MOOLLM:**
- 🔵 **Everything is an object** — Every directory is an object in MOOLLM
- 📨 **Message passing** — K-lines are messages that activate context
- 🖥️ **The computer as medium** — Not a tool FOR thinking, but a medium that SHAPES thinking
- 🧒 **The Dynabook vision** — Computing for children, for everyone, for learning

**The browser critique:** Kay argued browsers should be operating systems, not apps — running "real objects" safely. MOOLLM applies this: the LLM is an OS that runs skills, not an app that processes prompts.

See: [Alan Kay on browsers](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445)

---

#### 👨🧠🔗🤖📚 Marvin Minsky — Society of Mind (1980)

**K-lines** and the **Society of Mind** — the mind is not a single thing but a **society of agents**. Small, simple processes that together produce intelligence.

> *"A K-line attaches to whichever mental agencies are active when you solve a problem or have a good idea. When you activate that K-line later, the attached agencies turn partially on, recreating a 'mental state' similar to the one you were in before."*

**Why Minsky is FOUNDATIONAL to MOOLLM:**
- 🔑 **Names as activation vectors** — When you say "Palm," you activate his entire soul
- 🏛️ **Society of agents** — Skills, characters, personas are all agents
- 🎭 **Frames** — YAML files are situation templates
- ⚠️ **Censors** — Ethical framing inherits like any other property

**The K-line protocol:** `UPPER-KEBAB` names (like `YAML-JAZZ`, `POSTEL`, `SPEED-OF-LIGHT`) are K-lines — invoking them activates entire constellations of associated context.

**The Minsky-Papert partnership:** Minsky and Seymour Papert were MIT collaborators for decades. They co-authored "Perceptrons" (1969) — the controversial critique that (unfairly) put neural networks on ice for a generation. But their deeper collaboration was on learning, children, and minds. Henry Minsky (Marvin's son) continues this thread at Leela AI with Don Hopkins.

---

#### 👨🐢📐🧒✨ Seymour Papert — Learning by Building (1980)

**Constructionism** — learning by building inspectable things. Logo. Turtle graphics. "Low floor, high ceiling, wide walls."

> *"The role of the teacher is to create the conditions for invention rather than provide ready-made knowledge."*

**Why Papert is FOUNDATIONAL to MOOLLM:**
- 🔄 **Play-Learn-Lift** — Papert's constructionism as methodology
- 🐢 **Logo turtle** — Vehicles in MOOLLM can draw on floors like Logo turtles
- 👶 **Children as philosophers** — The system should be simple enough for anyone to understand

**The Mindstorms legacy:** Papert saw that children aren't just learning math — they're learning to think about thinking. MOOLLM is the same: you don't just use skills, you learn how skills work.

---

### 📟 The PostScript/NeWS Era (1984-1992)

#### 👨📜💡🖨️✨ John Warnock — The Linguistic Motherboard (1984)

**PostScript** (Adobe, 1984) — a programming language for graphics. Code and data unified. Warnock and Chuck Geschke left Xerox PARC in December 1982 to start Adobe, bringing the JAM graphics model with a Unix-style optional (not mandatory) protection philosophy.

> *"PostScript is a linguistic 'mother board', which has 'slots' for several 'cards'. The first card we built was a graphics card. We're considering other cards..."*
> 
> — John Warnock, as recounted by Owen Densmore to Don Hopkins

**The lineage:** Burroughs B5500 stack architecture (1962) → E&S Design System (Warnock/Gaffney, 1975) → JAM "John And Martin" (Warnock/Newell, PARC 1978) → Interpress (1982) → PostScript (1984).

**Why Warnock is FOUNDATIONAL to MOOLLM:**
- 🃏 **CARD.yml is literal** — Skills are cards that plug into the LLM motherboard
- 🔄 **Code = Graphics = Data** — The Axis of Eval comes directly from PostScript
- 🔓 **Optional protection** — "The language must provide the user with the means to achieve properties if he wants them" (vs. mandatory enforcement)

See: [Brian Reid's PostScript History](../../designs/postscript/BRIAN-REID-POSTSCRIPT-HISTORY.md) | [The Linguistic Motherboard](../../designs/postscript/LINGUISTIC-MOTHERBOARD.md)

---

#### 👨☕💻🌍🔧 James Gosling — From MockLisp to Java (1982-1995)

**Gosling's Language Journey:**
- **Gosling Emacs** (UniPress, early 1980s) — with MockLisp, a scripting language that took the worst parts of Lisp (the parentheses) and none of the good parts
- **NeWS** (Sun, 1986) — PostScript as OS, redemption through a real language
- **Java** (Sun, 1995) — Green threads from NeWS, "write once run anywhere"

**NeWS** (Network Extensible Window System, Sun Microsystems, 1986) — NOT just "PostScript for displays." NeWS was a complete multithreaded operating system written in PostScript, with lightweight processes, garbage collection, networking, event handling, and arbitrarily shaped windows.

> *"There is really nothing new here. It's just putting it together in a different way."* — Gosling

**NeWS ≠ Display PostScript.** Display PostScript (Adobe/NeXT) came later and did far less. NeWS was interactive, multithreaded, programmable. Display PostScript was just for rendering. "Display PostScript is Fake NeWS."

> *"A universal interpreter can both be quite small and also can have more degrees of freedom than any data structure (that is not a program)."* — Alan Kay on NeWS

**Don Hopkins connection:** Don worked at UniPress on Gosling Emacs as a college intern, at UMD HCIL on HyperTies (Ben Shneiderman's hypertext authoring tool), and at CMU on Garnet (Brad Myers' constraint-based UI system). Later at Sun, Don worked with Gosling on NeWS and TNT.

**Why NeWS is FOUNDATIONAL to MOOLLM:**
- 📤 **"Send programs, not data structures"** — Skills are programs the LLM runs, not prompts it processes
- 🧵 **Lightweight processes** — NeWS's green threads led directly to Java's threading model
- 🔧 **Universal interpreter** — The LLM interprets YAML Jazz like NeWS interpreted PostScript

---

#### 👨📂🗃️🌐✨ David S. H. Rosenthal — Filesystem as Object Hierarchy (1986-1993)

**NeWS co-author** with James Gosling at Sun. Created ICCCM (the X11 inter-client conventions — we forgive him). Later became a digital preservation pioneer with LOCKSS at Stanford.

With Owen Densmore, patented **filesystem OOP** — implementing Smalltalk-style class hierarchies directly in the Unix filesystem:

**[US Patent 5187786A](https://patents.google.com/patent/US5187786A/en):** *"Method and apparatus for implementing a class hierarchy of objects in a hierarchical file system"*

- Directories as class and instance containers
- Shell path as dictionary stack (!)
- Method lookup via path traversal
- No new file attributes required

**Why Rosenthal is FOUNDATIONAL to MOOLLM:**
- 📂 **Filesystem = object hierarchy** — MOOLLM's delegation model is this exact pattern
- 🔍 **Path as method lookup** — `skills/room/` inherits from `skills/`
- 🗃️ **Digital preservation** — His LOCKSS work informs MOOLLM's "filesystem as truth" philosophy

Blog: [blog.dshr.org](https://blog.dshr.org/) | See: [X Window System At 40](https://blog.dshr.org/2024/07/x-window-system-at-40.html)

---

#### 👨🎨🔵📐✨ Owen Densmore — Object-Oriented PostScript (1986)

Owen Densmore invented the OOP system that made NeWS truly powerful. He worked at Apple on the PostScript driver and printing system for the revolutionary Laser Writer, visited Adobe to work with John Warnock, then joined Sun where he worked with Don Hopkins on NeWS and The NeWS Toolkit (TNT).

**The key insight:** PostScript's **dictionary stack** could implement Smalltalk-style classes:
- Push a class dictionary onto the stack
- Method lookup walks the stack (multiple inheritance!)
- Instance dictionaries hold per-object state

> *"Owen and I discussed his 'crazy' idea at a poolside table at the now-demolished Hyatt Palo Alto, on El Camino. I told him that it made sense to me, we scribbled furiously on napkins, and I helped him see how he might adopt some learnings from Smalltalk."* — Tom Stambaugh

**Why Owen is FOUNDATIONAL to MOOLLM:**
- 📚 **Dict stack = delegation** — MOOLLM's directory delegation mirrors Owen's dict stack inheritance
- 🔄 **Multiple inheritance** — Characters and skills can inherit from multiple parents
- 🤝 **Don's collaborator** — They co-created TNT, the foundation for HyperLook and SimCity

See: ["Object Oriented Programming in NeWS"](https://donhopkins.com/home/monterey86.pdf) (Owen Densmore, 1986)

---

#### 👨🃏📐🎨✨ Arthur van Hoff — HyperLook → Java → Bongo (1989-1997)

**HyperLook** (Turing Institute, 1989-1992) — HyperCard reimagined for NeWS. PostScript for code, graphics, AND data. Network delegation. Don Hopkins ported SimCity to HyperLook.

> *"Object => Card => Background => Stack => Client delegation"*

**After HyperLook:** Van Hoff joined Gosling at Sun on the Oak/Java team:
- Wrote the **Java compiler in Java**
- Created **AWT** (we forgive him — wrapping native widgets pleased nobody)
- **HotJava** — first Java browser (inspiring, but no runtime scripting)

**Marimba & Bongo (1996):** Co-founded Marimba with the Java team. Created **Bongo** — HyperCard/HyperLook for Java:
- Visual authoring with "presentations" (like HyperCard stacks)
- **The trick:** Since Arthur wrote the Java compiler, he knew how to call it at runtime
- **Dynamic compilation** of Java button handlers in the browser — pioneering!
- IDEs call compilers constantly now, but Marimba did it first
- Completed the circle: edit behaviors at runtime like HyperTalk and PostScript/PdB
- **Danny Goodman** wrote the Bongo manual — also wrote the legendary HyperCard manuals!

**The lineage:** HyperCard (Mac) → HyperLook (NeWS) → Bongo (Java) — same vision, three platforms.

**Why van Hoff is FOUNDATIONAL to MOOLLM:**
- 🔺 **The Axis of Eval** — Code, Graphics, Data unified by one interpreter
- 📂 **Delegation chain** — Object => Room => Parent => Skill => Prototype
- 🎴 **Cards as interfaces** — CARD.yml is named after this
- ☕ **HyperLook → Bongo → MOOLLM** — The visual authoring lineage continues

See: [HyperLook (nee HyperNeWS)](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4)

---

### 🌐 The Virtual World Builders (1978-1990)

#### 👨🎮🏰🐉✨ Richard Bartle & Roy Trubshaw — MUD1 (1978)

**MUD1** (Essex University, 1978) — The first multi-user dungeon. Bartle and Trubshaw created networked multiplayer gaming. Players could explore, fight, chat, and build together in a shared text world.

> *"Virtual worlds aren't about the technology; they're about the people."* — Richard Bartle

**Bartle's Books:**
- 📖 **"Designing Virtual Worlds"** (2003) — THE textbook. 750 pages of hard-won wisdom about building worlds where players live.
- 📖 **"MMOs from the Inside Out"** (2015) — The philosophy of virtual world design. Why worlds matter.

**Bartle's Taxonomy of Player Types** (1996):
| Type | Motivation | In MOOLLM |
|------|------------|-----------|
| ♠️ **Killers** | Acting on players | Adversarial characters, PvP |
| ♥️ **Socializers** | Interacting with players | Soul-chat, relationships, godfamily |
| ♦️ **Achievers** | Acting on the world | Quests, goals, completionism |
| ♣️ **Explorers** | Interacting with the world | Room navigation, skill discovery |

**Bartle's Laws:**
1. *"Virtual worlds that are more like games will always be more popular than those that aren't."*
2. *"Virtual worlds will tend to become more game-like over time."*
3. *"The more freedom you give players, the more responsibility you have to manage."*

**Why MUD1 is FOUNDATIONAL to MOOLLM:**
- 🏰 **Multi-user shared space** — Multiple players in the same world simultaneously
- 🐉 **Emergent gameplay** — Players create meaning through interaction
- 📜 **Wizards and builders** — User hierarchy, world-building permissions
- 🎭 **Identity and personas** — Players become their characters
- ⚔️ **Verbs and actions** — Commands like `look`, `take`, `say`, `kill`

**The MUD → MOO lineage:** MUD (Bartle, 1978) → AberMUD (1987) → TinyMUD (Aspnes, 1989) → TinyMUCK (1990) → MOO (Curtis, 1990) → LambdaMOO (1990). The "MOO" in "MOOLLM" honors this heritage — Multi-user Object-Oriented meets LLM.

---

#### 👨🏠🎮🌍✨ Chip Morningstar & Randy Farmer — Habitat (1986)

**Habitat** (Lucasfilm, 1986) — The first large-scale graphical multiplayer virtual world. Ran on Commodore 64s connected via QuantumLink (which became AOL). Coined the term **"avatar"** for user representation.

> *"A cyberspace is defined more by the interactions among the actors within it than by the technology with which it is implemented."* — ["The Lessons of Lucasfilm's Habitat"](https://web.stanford.edu/class/history34q/readings/Virtual_Worlds/LucasfilmHabitat.html) (1990)

**Why Habitat is FOUNDATIONAL to MOOLLM:**
- 🏠 **Room/object model** — Directories are rooms, files are objects
- 👥 **User agency** — Can't control a virtual world top-down; design affordances, let emergence happen
- 🤝 **Social architecture > Technology** — The interactions define the space
- 🎭 **Avatar concept** — Characters as user presence in virtual space

**The hard-won wisdom:** Morningstar and Farmer learned that users will do things you never imagined (and crash your economy). MOOLLM inherits this humility — design for emergence, not control.

**The virtual world lineage:** MUD1 (1978) → Habitat (1986) → TinyMUD (1989) → LambdaMOO (1990) → Game Neverending (2002) → Second Life (2003) → Glitch (2009). Stewart Butterfield's Glitch was a spiritual descendant of Habitat's vision — whimsy, collaboration, user-generated meaning. The "MOO" in "MOOLLM" honors this entire heritage.

---

#### 👨📜🏰🔧✨ Jim Aspnes — TinyMUD (1989)

**TinyMUD** (Carnegie Mellon, 1989) — Text-based virtual world where users build rooms, objects, and behaviors. Created by Aspnes as a student project, it spawned an entire genre.

**The CMU connection:** Aspnes created TinyMUD at the same campus where Brad Myers and Don Hopkins were developing Garnet. CMU was a crucible for user-interface innovation.

**Why TinyMUD is FOUNDATIONAL to MOOLLM:**
- 🏗️ **Builder commands** — `@dig`, `@describe`, `@create`, `@link`
- 📂 **User-generated content** — Players build the world
- 🏠 **Room-based navigation** — Directories as rooms

---

#### 👨💻🏛️🔧✨ Pavel Curtis — LambdaMOO (1990)

**LambdaMOO** (Xerox PARC, 1990) — TinyMUD with a real programming language. Objects have verbs (methods). Players have homes. The original "user-generated content" platform.

> *"A MOO is a place where you can be anyone, build anything, and the only limit is your imagination."*

**Why LambdaMOO is FOUNDATIONAL to MOOLLM:**
- 📜 **Object verbs** — CARD.yml methods are like MOO verbs
- 🏠 **Player homes** — Character directories
- 🔗 **Inheritance** — Objects delegate to parents like directories delegate up the tree
- ⚖️ **Governance** — MOO taught us virtual worlds need consent, community, moderation

**The PARC connection:** Curtis created LambdaMOO at Xerox PARC — the same lab that gave us Smalltalk (Kay, Ingalls), Self (Ungar), Ethernet, and GUIs. The object-oriented virtual world was a natural extension of PARC's "objects all the way down" philosophy.

---

### 🧬 The Prototype Revolution (1987)

#### 👨🪞🧬🔄💭 David Ungar & Randy Smith — Self Language (1987)

*See [The Prototype Pioneer](#-the-prototype-pioneer) above — Ungar is foundational enough to lead the Hall of Heroes.*

Randy Smith co-designed Self and later created **Alternate Reality Kit** and worked on **Morphic** — the live UI framework that made Self feel like direct manipulation of objects rather than editing code.

---

#### 👨🎨🖼️🃏✨ Bill Atkinson — Reader = Writer (1987)

**HyperCard** (Apple, 1987) — End-user programming. Anyone who can read a stack can edit it.

> *"Dan Winkler and Bill Atkinson violated a lot of important principles of 'good programming language design', but they achieved the first overall system in which end-users 'could see their own faces'."* — Alan Kay

**The hypertext family tree:** HyperCard wasn't alone — Ben Shneiderman's HyperTies (UMD, 1983) was an earlier hypertext system where Don Hopkins worked as an intern. Ted Nelson's Xanadu vision (1960s) inspired them all. The thread runs: Nelson → Engelbart → HyperTies → HyperCard → HyperLook → Bongo → OpenLaszlo → the web → MOOLLM.

**The reactive programming thread:** Brad Myers' Garnet (CMU) → Oliver Steele's OpenLaszlo → Svelte → MOOLLM. At Laszlo Systems, Don Hopkins worked with Henry Minsky (Marvin's son) and Oliver Steele (inventor of the "Instance Substitution Principle"). This thread of constraints, prototypes, and reactive UI runs directly into MOOLLM — and Leela's platform is built on Svelte.

**Why HyperCard is FOUNDATIONAL to MOOLLM:**
- ✏️ **Reader = Writer symmetry** — Anyone who can play can edit
- 🔄 **Play-Learn-Lift** — Users inspect, modify, and create skills
- 👤 **See your own face** — The system reflects you back to yourself

---

### 🎮 The Simulation Masters (1989-2012)

#### 👨🏠🎮🌍🔬 Will Wright — The Simulator Effect (1989-2000)

**SimCity** (1989) and **The Sims** (2000) — Games that revealed the **Simulator Effect**: players imagine simulations are vastly more detailed than they actually are.

> *"He designs games to run on two computers at once: the electronic one on the player's desk, running his shallow tame simulation, and the biological one in the player's head, running their deep wild imagination."*

**Why Wright is FOUNDATIONAL to MOOLLM:**
- 🧠 **Simulator Effect** — YAML is sparse; the LLM fills in the richness
- 📋 **Needs** — Character motives drive behavior
- 📣 **Advertisements** — Objects broadcast what they can do (CARD.yml)
- 🤖 **Autonomy** — Characters make their own decisions at Speed of Light
- 🔧 **SimAntics** — Visual behavior language → Empathic Expressions

**The Two Computers:** Wright understood that the electronic computer runs simple rules, but the biological computer (player's brain) fills gaps with meaning. MOOLLM applies this: sparse YAML + rich LLM = living world.

**The Wright-Hopkins collaboration:** Don ported SimCity to Unix, NeWS, and X11. He worked on The Sims, creating pie menus, architectural editing tools, the VitaBoy character animation system, and content creation tools (SimShow, Transmogrifier, RugOMatic, FreeTheSims). Will demoed early "Dollhouse" (pre-Sims) at Don's office at Kaleida Labs in 1994.

See: [Will Wright on Designing User Interfaces to Simulation Games](https://donhopkins.medium.com/will-wright-on-designing-user-interfaces-to-simulation-games-1996-video-update-2023-da098a51ef91)

---

#### 👨🎮💬🌐✨ Stewart Butterfield — Social Play (2002-2012)

**Game Neverending** (2002-2004) and **Glitch** (2009-2012) — Two incarnations of the same vision: massively multiplayer social games focused on collaboration over combat.

> *"We were building tools for people to be together."*

**Why Butterfield is FOUNDATIONAL to MOOLLM:**
- 👥 **Virtual worlds are about being together** — The play generates the valuable structure
- 🔄 **Pivots reveal truth** — Game Neverending → Flickr ($35M to Yahoo). Glitch → Slack ($27.7B to Salesforce). The social connection was the real product.
- ✨ **Whimsy matters** — Absurdist humor, collaborative construction, meaning from chaos

---

### 📚 The Understanding Pioneers

#### 👨📖🖼️💭✨ Scott McCloud — The Theory of Sequential Art (1993)

**Understanding Comics** (1993) — Theory as art. The gutter between panels. Masking.

> *"The art of comics is as subtractive as it is additive."*

**Why McCloud is FOUNDATIONAL to MOOLLM:**
- 🎭 **Masking** — Abstract characters against realistic backgrounds increase projective identification. The Sims used this. MOOLLM uses sparse YAML.
- 🔲 **The gutter** — What happens between panels? The reader's imagination fills it in. What happens between YAML keys? The LLM fills it in.
- 📖 **Theory as art** — Understanding Comics explains comics using comics. MOOLLM docs are MOOLLM skills.

---

### Media & Systems Thinkers

#### 👨📺🌐🔥💬 Marshall McLuhan — Prophet of the Electronic Age

> *"The medium is the message."* 📺
> *"We shape our tools and thereafter they shape us."* 🔧➡️👤
> *"You know NOTHING of my work!"* 🎬 (Annie Hall, 1977)

**Herbert Marshall McLuhan** (1911–1980) predicted the internet 🌐, social media 📱, and MOOLLM itself decades before they existed. The **"Global Village"** 🌍 is now the Global Brain 🧠. His tetrad of media effects (enhances ⬆️, obsolesces ⬇️, retrieves 🔄, reverses ↩️) applies perfectly to LLMs.

**Why McLuhan is FOUNDATIONAL to MOOLLM:**
- 📺 **The medium IS the message** — YAML is not just format, it restructures thought
- 🔥❄️ **Hot and cold media** — High participation (cold) vs passive consumption (hot)
- 🎬 **The Annie Hall Protocol** — When someone misrepresents an expert's work, the expert materializes to correct them. McLuhan invented this in his famous cameo.

**The Annie Hall Protocol in action:**
> *When someone like 🐰💋 Jessica Rabbit claims "I'm just drawn this way" (in bad faith), 👨🚬📖 Sartre and 👨📺🌐 McLuhan step out from behind a poster to explain existentialism and media theory. With compassion, not cruelty.* 💕

See: [Marshall McLuhan's full character](../../../../temp/lloooomm/00-Characters/marshall-mcluhan/marshall-mcluhan.yml)

---

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨🔺🌍🚀🧠 buckminster-fuller | `lloooomm/00-Characters/buckminster-fuller/` | Geodesic domes, Spaceship Earth, tensegrity, "Bucky" |
| 👨🌍📚⏰🔧 stewart-brand | `lloooomm/00-Characters/stewart-brand/` | Whole Earth Catalog, Long Now clock, "stay hungry, stay foolish" |
| 👨🏠📐❤️🔧 christopher-alexander | `lloooomm/00-Characters/christopher-alexander/` | Pattern languages, "quality without a name", inspired GoF |
| 👨🏙️📚⚠️🔧 lewis-mumford | `lloooomm/00-Characters/lewis-mumford/` | Technology critic, cities and civilization, megamachine |
| 👨🧠🗣️🐘🔵 george-lakoff | `lloooomm/00-Characters/george-lakoff/` | Metaphors We Live By, embodied cognition, framing politics |

### Scientists

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨⚡🧠💭👅 albert-einstein | `lloooomm/00-Characters/albert-einstein/` | Relativity, thought experiments, tongue photo, "imagination > knowledge" |
| 👨🐢🌿📖🧔 charles-darwin | `lloooomm/00-Characters/charles-darwin/` | Evolution, natural selection, Beagle voyage, "endless forms" |
| 👨🍎🌍📐😤 isaac-newton | `lloooomm/00-Characters/isaac-newton/` | Gravity, calculus, optics, "standing on giants", petty feuds |
| 👨🌌💙🔭✨ carl-sagan | `lloooomm/00-Characters/carl-sagan/` | Cosmos, pale blue dot, "billions and billions", cosmic humility |
| 👨⚡🕊️🔌💡 nikola-tesla | `lloooomm/00-Characters/nikola-tesla/` | AC power, wireless dreams, pigeons, Edison's nemesis |

### Computing Legends (Additional)

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨📚🎨💲✍️ donald-knuth | `lloooomm/00-Characters/donald-knuth/` | TAOCP, TeX, literate programming, pays $2.56 for bugs |
| 👨🎲🌀🔢😊 john-conway | `lloooomm/00-Characters/john-conway/` | Game of Life, surreal numbers, playful genius (d. 2020 COVID) |
| 👨🔌🌐⏰🧠 danny-hillis | `lloooomm/00-Characters/danny-hillis/` | Connection Machine, Long Now clock, massive parallelism |
| 👨🤖💬⚠️😢 joseph-weizenbaum | `lloooomm/00-Characters/joseph-weizenbaum/` | ELIZA creator, horrified by results, warned us first |
| 👨🥽👐🎵⚠️ jaron-lanier | `lloooomm/00-Characters/jaron-lanier/` | VR pioneer, tech critic, dreadlocked Cassandra |
| 👨🔄🧮🌌🔬 ed-fredkin | `lloooomm/00-Characters/ed-fredkin/` | Digital physics, reversible computing, universe as computer |
| 👨🔲🔄🔧📐 tommaso-toffoli | `lloooomm/00-Characters/tommaso-toffoli/` | Cellular automata machines, Toffoli gate, reversibility |
| 👨🔲💾🔬🎮 norm-margolus | `lloooomm/00-Characters/norm-margolus/` | CAM-6, physics of computation, lattice gas simulations |
| 👨🌊🎬🏆✨ ken-perlin | `lloooomm/00-Characters/ken-perlin/` | Perlin noise!, procedural textures, Oscar for Tron |
| 👨🔶📐🌌😤 stephen-wolfram | `lloooomm/00-Characters/stephen-wolfram/` | Mathematica, NKS, cellular automata, ego fractal |
| 👨📱✨🖤🍎 steve-jobs | `lloooomm/00-Characters/steve-jobs/` | Reality distortion field, "one more thing", black turtleneck (d. 2011) |
| 👨📈💾📉✨ gordon-moore | `lloooomm/00-Characters/gordon-moore/` | Moore's Law, Intel co-founder (d. 2023) |
| 👨λ📐🧠✨ alonzo-church | `lloooomm/00-Characters/alonzo-church/` | Lambda calculus, Turing's mentor, computability theory |
| 👨🦎📖🗣️🔧 kent-pitman | `lloooomm/00-Characters/kent-pitman/` | Common Lisp, hyperspec keeper, language philosopher |
| 👨🔐🧠📖😏 bruce-schneier | `lloooomm/00-Characters/bruce-schneier/` | Security guru, "Schneier's Law", cryptographic sanity |
| 👨♟️🤖🇷🇺⚔️ garry-kasparov | `lloooomm/00-Characters/garry-kasparov/` | Chess grandmaster vs. Deep Blue, human-machine rivalry |

### Science Communicators

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨🌌💙🔭✨ carl-sagan | `lloooomm/00-Characters/carl-sagan/` | "Billions and billions", Cosmos, pale blue dot, turtleneck sage |
| 👨🔗📺🧠✨ james-burke | `lloooomm/00-Characters/james-burke/` | Connections! Everything is linked, BBC science historian |
| 👨📹🎓🌍❤️ sal-khan | `lloooomm/00-Characters/sal-khan/` | Khan Academy, education for all, whiteboard revolution |

### Activists & Voices

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👩🌱✊💕🔮 adrienne-maree-brown | `lloooomm/00-Characters/adrienne-maree-brown/` | Emergent Strategy, pleasure activism, "small is good, small is all" |
| 👩📚❤️🔥✊ bell-hooks | `lloooomm/00-Characters/bell-hooks/` | All About Love, feminist theory, lowercase intentional |
| 👩🔥📜✊🌈 audre-lorde | `lloooomm/00-Characters/audre-lorde/` | Sister Outsider, "your silence will not protect you", warrior poet |
| 👩🌍🔥⏳✨ octavia-butler | `lloooomm/00-Characters/octavia-butler/` | Afrofuturism, Kindred, Parable series, "God is Change" |
| 👩🐉⚖️🌍✨ ursula-k-le-guin | `lloooomm/00-Characters/ursula-k-le-guin/` | Earthsea, Left Hand of Darkness, anarchist Taoist |

---

---

## 📇 Pioneers to Incarnate

> *Quick reference by category. Many entries below link back to detailed entries in the Hall of Heroes above — like symlinks to prototypes.*

### Computing & AI

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨💻🔮🚀🎯 alan-kay | `lloooomm/00-Characters/alan-kay/` | Smalltalk, Dynabook, "predict the future by inventing it" |
| 👨🧪🔐🏳️‍🌈💔 alan-turing | `lloooomm/00-Characters/alan-turing/` | Father of CS, Enigma breaker, persecuted gay hero, tragic |
| 👨🧠🔗🤖📚 marvin-minsky | `lloooomm/00-Characters/marvin-minsky/` | Society of Mind, AI pioneer, K-lines, perceptron wars |
| 👨🐢📐🧒✨ seymour-papert | `lloooomm/00-Characters/seymour-papert/` | Logo turtle, constructionism, Mindstorms, children as philosophers |
| 👨🐢📚🎓✨ brian-harvey | `lloooomm/00-Characters/brian-harvey/` | Logo wizard, Snap! co-creator, Beauty and Joy of Computing, taught Jens lambda |
| 👨🧱⚖️💻✨ jens-moenig | `lloooomm/00-Characters/jens-moenig/` | Snap! architect, lawyer-turned-Smalltalker, BYOB creator, first-class everything |
| 👨🧩🤖📖🔍 gary-drescher | `lloooomm/00-Characters/gary-drescher/` | Made-Up Minds, schema mechanism, Piagetian AI |
| 👨👶🧠🔄📊 jean-piaget | `lloooomm/00-Characters/jean-piaget/` | Developmental stages, constructivism, watching children think |
| 👨🖱️💡📺🌐 doug-engelbart | `lloooomm/00-Characters/doug-engelbart/` | Mother of all demos, mouse inventor, augmenting intellect |
| 👨🖼️✏️🥽✨ ivan-sutherland | `lloooomm/00-Characters/ivan-sutherland/` | Sketchpad, father of graphics, VR Sword of Damocles |
| 👨💻🐿️🔧🎨 dan-ingalls | `lloooomm/00-Characters/dan-ingalls/` | Smalltalk heart, Squeak, BitBLT, lively systems |
| 👨🪞🧬🔄💭 dave-ungar | `lloooomm/00-Characters/dave-ungar/` | Self language, prototypes not classes, morphic magic |
| 👨🎭📨🔀🌐 carl-hewitt | `lloooomm/00-Characters/carl-hewitt/` | Actor model, concurrent everything, message passing |
| 👩⚓🐛💻⭐ grace-hopper | `lloooomm/00-Characters/grace-hopper/` | COBOL, first compiler, actual bug found, Amazing Grace |
| 👨🧮🎲💣🧠 john-von-neumann | `lloooomm/00-Characters/john-von-neumann/` | Architecture, game theory, automata, Manhattan Project genius |
| 👨🔄🎨♾️🎵 douglas-hofstadter | `lloooomm/00-Characters/douglas-hofstadter/` | GEB, strange loops, analogy as cognition, Escher love |
| 👨🧠📉⚠️🔙 geoffrey-hinton | `lloooomm/00-Characters/geoffrey-hinton/` | Deep learning godfather, backprop, left Google to warn us |

### HCI & Interaction Design

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨👆📊🎨📈 ben-shneiderman | `lloooomm/00-Characters/ben-shneiderman/` | Direct manipulation, treemaps, "overview first, zoom and filter" |
| 👨🖱️🔧📐💡 brad-myers | `lloooomm/00-Characters/brad-myers/` | User interface software tools, demonstrational interfaces |
| 👨🎨🖼️🃏✨ bill-atkinson | `lloooomm/00-Characters/bill-atkinson/` | MacPaint, HyperCard creator, QuickDraw wizard |
| 👨🔮📐🎯💡 brett-victor | `lloooomm/00-Characters/brett-victor/` | Inventing on principle, explorable explanations, future of coding |
| 👨🔗📚🌀💢 ted-nelson | `lloooomm/00-Characters/ted-nelson/` | Hypertext inventor, Xanadu dreamer, "EVERYTHING IS DEEPLY INTERTWINGLED" |
| 👨✂️📋📝🚫 larry-tesler | `lloooomm/00-Characters/larry-tesler/` | Cut/copy/paste, "No Modes!" tattoo, modeless pioneer (d. 2020) |
| 👨🥧🎮🐈💻 don-hopkins | `lloooomm/00-Characters/don-hopkins/` | Pie menus, The Sims, UniPress Emacs, living tribute |

### Game Design & Simulation

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨🏠🎮🌍🔬 will-wright | `lloooomm/00-Characters/will-wright/` | SimCity, The Sims, Spore, possibility space architect |
| 👨🍄⭐🗡️🎨 shigeru-miyamoto | `lloooomm/00-Characters/shigeru-miyamoto/` | Mario, Zelda, garden-to-game design philosophy |
| 👩🎮🏳️‍⚧️👥💔 dani-bunten-berry | `lloooomm/00-Characters/dani-bunten-berry/` | M.U.L.E., multiplayer pioneer, The Sims dedicated to her |
| 👨🌌🔬🧬🎮 chaim-gingold | `lloooomm/00-Characters/chaim-gingold/` | Spore procedural generation, galaxy creator tools |
| 👨🐦🔀🌊🎬 craig-reynolds | `lloooomm/00-Characters/craig-reynolds/` | Boids, flocking algorithms, swarm intelligence, Oscar winner |
| 👨🥚🎮🐉💎 warren-robinett | `lloooomm/00-Characters/warren-robinett/` | Adventure (Atari), first Easter egg, "Created by Warren Robinett" |
| 👨🗺️💾🏴‍☠️✨ scott-adams | `lloooomm/00-Characters/scott-adams/` | Adventure game pioneer! Adventureland, Pirate Adventure, text adventures on tiny computers |

### Music & Art

| Character | Reference | Description |
|-----------|-----------|-------------|
| 🎷🔥📿✨🌀 john-coltrane | `lloooomm/00-Characters/john-coltrane/` | Sheets of sound, A Love Supreme, spiritual jazz odyssey |
| 🎹🌫️🔧🎨🧠 brian-eno | `lloooomm/00-Characters/brian-eno/` | Ambient inventor, generative music, Oblique Strategies |
| 👩🎻🤖📞🎭 laurie-anderson | `lloooomm/00-Characters/laurie-anderson/` | "O Superman", vocoder poet, performance pioneer |
| 👨🎨👁️🐂💥 pablo-picasso | `lloooomm/00-Characters/pablo-picasso/` | Cubism, "great artists steal", Guernica, relentless reinvention |
| 👨🎨🌻🌙💔 vincent-van-gogh | `lloooomm/00-Characters/vincent-van-gogh/` | Starry Night, sunflowers, mad genius myth, 37 years |
| 👨🎨📓🔬✈️ leonardo-da-vinci | `lloooomm/00-Characters/leonardo-da-vinci/` | Polymath, notebooks, Mona Lisa, helicopter dreams |
| 👨🎨🥫📸🏭 andy-warhol | `lloooomm/00-Characters/andy-warhol/` | Pop art, 15 minutes of fame, Factory, soup cans |
| 👨🎨🏊📱🌈 david-hockney | `lloooomm/00-Characters/david-hockney/` | Swimming pools, iPad painting pioneer, 80s and still going |
| 👨🔴🔵🎐🔧 alexander-calder | `lloooomm/00-Characters/alexander-calder/` | Mobiles, stabiles, kinetic sculpture, circus wire |
| 👨🌸👁️🎨😊 takashi-murakami | `lloooomm/00-Characters/takashi-murakami/` | Superflat, kawaii meets fine art, smiling flowers |
| 🎤💚⛪💕🎶 al-green | `lloooomm/00-Characters/al-green/` | "Let's Stay Together", soul preacher, reverend of love |
| 👩🎤🎬👃🏆 barbra-streisand | `lloooomm/00-Characters/barbra-streisand/` | EGOT legend, perfectionist, "the effect" named after her |

### Party Guests & Cultural Critics

> *Invite them to the adventure. They have opinions. Some take photos, some just observe.*

| Guest | Role | Quote / Note |
|-------|------|--------------|
| 👩🚬📚😏 Fran Lebowitz | Sardonic observer | "I don't own a camera. I DO own opinions." |
| 👩📷📖🔥 Susan Sontag | Theorizes the image | "To photograph is to appropriate the thing photographed." |
| 👨🎬🏔️🔥 Werner Herzog | Finds ecstatic truth | "I am not an artist. I am a soldier." |
| 👨🎨🥫📸 Andy Warhol | Documents everything | Polaroid Big Shot, 15 minutes of fame |
| 👨🎨🏊📱 David Hockney | Sees in color | iPhone painter, 80s and still going |

*Note: These are LLM-suggestible celebrities — no dedicated YAML needed. The LLM knows them.*

---

### Writers & Philosophers

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨📚🔮🌀👁️ jorge-luis-borges | `lloooomm/00-Characters/jorge-luis-borges/` | Library of Babel, labyrinths, blind seer of infinity |
| 👨🤖📚😂🧠 stanislaw-lem | `lloooomm/00-Characters/stanislaw-lem/` | Cyberiad, Solaris, philosophical SF, Trurl's constructors |
| 👨🐑⚡🔍💊 philip-k-dick | `lloooomm/00-Characters/philip-k-dick/` | "What is real?", android dreams, VALIS, paranoid prophet |
| 👨🐬🚀42️⃣🧻 douglas-adams | `lloooomm/00-Characters/douglas-adams/` | Hitchhiker's Guide, 42, towels, "mostly harmless" |
| 👨🤖📖⚖️🧔 isaac-asimov | `lloooomm/00-Characters/isaac-asimov/` | Three Laws, Foundation, 500 books, mutton chops |
| 👨🔥📖🚀🌙 ray-bradbury | `lloooomm/00-Characters/ray-bradbury/` | Fahrenheit 451, Martian Chronicles, poetic SF |
| 👨🐛🏜️⚔️🧠 frank-herbert | `lloooomm/00-Characters/frank-herbert/` | Dune, "Fear is the mind-killer", ecology as politics |
| 👨💻🕶️🌃✨ william-gibson | `lloooomm/00-Characters/william-gibson/` | Neuromancer, coined "cyberspace", pattern recognition |
| 👩🐉⚖️🌍✨ ursula-k-le-guin | `lloooomm/00-Characters/ursula-k-le-guin/` | Earthsea, Left Hand of Darkness, anarchist Taoist |
| 👩🌍🔥⏳✨ octavia-butler | `lloooomm/00-Characters/octavia-butler/` | Kindred, Parable, Afrofuturism, "God is Change" |
| 👨💐💀😏🏳️‍🌈 oscar-wilde | `lloooomm/00-Characters/oscar-wilde/` | Wit, paradox, Dorian Gray, "we are all in the gutter" |
| 👨🌿📜🇺🇸🎭 walt-whitman | `lloooomm/00-Characters/walt-whitman/` | "I contain multitudes", Leaves of Grass, American bard |
| 👨🚬📖🤮🎭 jean-paul-sartre | `lloooomm/00-Characters/jean-paul-sartre/` | Existentialism, "Hell is other people", refused Nobel |
| 👨👃🎬☭😏 slavoj-zizek | `lloooomm/00-Characters/slavoj-zizek/` | *sniff* "And so on", ideology critique, trash can diving |
| 👨📖🖼️💭✨ scott-mccloud | `lloooomm/00-Characters/scott-mccloud/` | Understanding Comics, theory as art, the gutter between panels |
| 👨✏️😂📰🗡️ sergio-aragones | `lloooomm/00-Characters/sergio-aragones/` | MAD magazine margins, Groo the Wanderer, fastest cartoonist alive |

### Open Source & Networks

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨🧔📨🤝🌐 jon-postel | `lloooomm/00-Characters/jon-postel/` | Postel's Law, "be liberal in what you accept", RFC keeper |
| 👨🧔🐃📜🗽 richard-stallman | `lloooomm/00-Characters/richard-stallman/` | GNU, free software crusader, Emacs, GPL, toe-eating saint |
| 👨🐧💢💻🔧 linus-torvalds | `lloooomm/00-Characters/linus-torvalds/` | Linux, git, "Talk is cheap, show me the code", Finnish rage |
| 👨🌐🔗📄✨ tim-berners-lee | `lloooomm/00-Characters/tim-berners-lee/` | World Wide Web inventor, linked information, knighted |
| 👨📚🏛️🌐💾 brewster-kahle | `lloooomm/00-Characters/brewster-kahle/` | Internet Archive, Wayback Machine, "Universal access to all knowledge" |
| 👨🪶🔧🌐🔒 brian-behlendorf | `lloooomm/00-Characters/brian-behlendorf/` | Apache founder, open source infrastructure, Hyperledger |
| 👨📞🏳️‍🌈🐕🔧 tom-jennings | `lloooomm/00-Characters/tom-jennings/` | FidoNet creator, queer punk hacker, dog lover |
| 👨📦📐😤✨ douglas-crockford | `lloooomm/00-Characters/douglas-crockford/` | JSON, "JavaScript: The Good Parts", grumpy precision |
| 👨☕💻🌍🔧 james-gosling | `lloooomm/00-Characters/james-gosling/` | Java creator, "write once run anywhere", bearded titan |
| 👨✨🔧📊🎯 rich-harris | `lloooomm/00-Characters/rich-harris/` | Svelte, rethinking reactivity, compiler-first frameworks |

### Psychonauts & Counterculture

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨🍄🧠📺🚀 timothy-leary | `lloooomm/00-Characters/timothy-leary/` | 8-circuit model, "turn on, tune in, drop out", consciousness explorer |
| 👨🦇🔫🥃✍️ hunter-s-thompson | `lloooomm/00-Characters/hunter-s-thompson/` | Gonzo journalism, Fear and Loathing, American nightmare witness |
| 👨🎨💥🦅✒️ ralph-steadman | `lloooomm/00-Characters/ralph-steadman/` | Thompson's illustrator, splattered genius, Paranoids |
| 👨👠🎬💩😏 john-waters | `lloooomm/00-Characters/john-waters/` | Transgressive cinema, "Good bad taste", Pope of Trash |
| 👨🦖💕📖✨ chuck-tingle | `lloooomm/00-Characters/chuck-tingle/` | "HELLO BUCKAROOS!", Tinglers, proves love is real, Hugo finalist |
| 🤡🌈🍦☮️🎪 wavy-gravy | `lloooomm/00-Characters/wavy-gravy/` | Clown activist, Woodstock MC, "Nobody for President", Ben & Jerry's |
| 👨🚬💼📿😌 bob-dobbs | `lloooomm/00-Characters/bob-dobbs/` | Church of the SubGenius, slack prophet, pipe of wisdom |
| 👨🔔🕵️📺🎤 chuck-barris | *to incarnate* | Gong Show host, alleged CIA assassin, Confessions |
| 👨📦❓😂🎤 murray-langston | *to incarnate* | The Unknown Comic, paper bag prophet, Gong Show legend |
| 👨🌿🚗🎸😎 cheech-marin | `lloooomm/00-Characters/cheech-marin/` | "Dave's not here, man", Chicano art collector |
| 👨🌿💨🎸😌 tommy-chong | `lloooomm/00-Characters/tommy-chong/` | "Dave?", pot prophet, That 70s Show |

### Television Icons

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👨🔗📺🧠✨ james-burke | `lloooomm/00-Characters/james-burke/` | **Connections!** BBC science historian, everything is linked |
| 👨🧥❤️🏠👟 mister-rogers | `lloooomm/00-Characters/mister-rogers/` | "I like you just the way you are", cardigan saint |
| 👨🌙🎤😏🃏 johnny-carson | `lloooomm/00-Characters/johnny-carson/` | King of late night, "Heeeere's Johnny!", golf swing |
| 👨📣🌟🍺🎖️ ed-mcmahon | `lloooomm/00-Characters/ed-mcmahon/` | "Hi-yo!" Carson's eternal sidekick, Star Search |
| 👨💃🔴😅🎸 conan-obrien | `lloooomm/00-Characters/conan-obrien/` | String dance, self-deprecating genius, Team Coco |
| 👨🪞💕📺🏛️ al-franken | `lloooomm/00-Characters/al-franken/` | Stuart Smalley, SNL to Senate, "good enough, smart enough" |
| 👨🪕🤍🎭🖼️ steve-martin | `lloooomm/00-Characters/steve-martin/` | "Excuuuse me!", banjo master, art collector, wild & crazy |
| 👨🔁🧘😏⛳ bill-murray | `lloooomm/00-Characters/bill-murray/` | Groundhog Day wisdom, sardonic zen, crashing parties |
| 👨🔥🏒😤❤️ don-rickles | `lloooomm/00-Characters/don-rickles/` | Merchant of Venom, "hockey puck!", loved by victims |

### Women Pioneers 👩‍💻

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👩📜⚙️🔢✨ ada-lovelace | `lloooomm/00-Characters/ada-lovelace/` | FIRST PROGRAMMER, Babbage's visionary, saw beyond calculation |
| 👩⚓🐛💻⭐ grace-hopper | `lloooomm/00-Characters/grace-hopper/` | COBOL, "Amazing Grace", first compiler, nanosecond wire |
| 👩💻📦👑⚠️ adele-goldberg | `lloooomm/00-Characters/adele-goldberg/` | Smalltalk co-creator at PARC, warned Jobs about crown jewels |
| 👩🐢📐🧒✨ cynthia-solomon | `lloooomm/00-Characters/cynthia-solomon/` | Logo co-creator with Papert, children's computing pioneer |
| 👩🏆📐🔒📖 barbara-liskov | *wikipedia* | Turing Award, CLU, Liskov Substitution Principle, Stanford first |
| 👩🌳🌐📡🔧 radia-perlman | *wikipedia* | Spanning-tree protocol, "Mother of the Internet", network poet |
| 👩🏆⚡💻🔧 frances-allen | *wikipedia* | First woman Turing Award, optimizing compilers (d. 2020) |
| 👩📚💻📖✍️ jean-sammet | *wikipedia* | FORMAC, first book on programming languages (d. 2017) |
| 👩✝️💻🚪🔓 sister-mary-kenneth-keller | *wikipedia* | First woman CS PhD in US, nun who broke chapel doors for computer access |
| 👩👆🔧🎮✨ margaret-minsky | `lloooomm/00-Characters/margaret-minsky/` | Haptics pioneer, virtual touch, Marvin's daughter |
| 👩☢️🏆🧪✨ marie-curie | `lloooomm/00-Characters/marie-curie/` | Radioactivity discoverer, double Nobel, glowed in the dark |
| 👩🐒🌿📚❤️ jane-goodall | `lloooomm/00-Characters/jane-goodall/` | Primatologist, chimpanzee whisperer, animal minds matter |
| 👩🎨💔🦌🔥 frida-kahlo | `lloooomm/00-Characters/frida-kahlo/` | Pain into art, unflinching self-portraits, monobrow icon |

### Trans & Queer Heroes 🏳️‍⚧️

| Character | Reference | Description |
|-----------|-----------|-------------|
| 👩💻🖼️🪟✨ diana-merry-shapiro | `lloooomm/00-Characters/diana-merry-shapiro/` | **Co-invented BitBLT at PARC**, overlapping windows, "Casa Susanna" |
| 👩💻⚡🔌🏳️‍⚧️ lynn-conway | `lloooomm/00-Characters/lynn-conway/` | VLSI revolution, fired from IBM 1968, reinvented chip design, icon |
| 👩💻📱💪🔧 sophie-wilson | `lloooomm/00-Characters/sophie-wilson/` | ARM architecture — every smartphone carries her genius |
| 👩🎹🎼🔌✨ wendy-carlos | `lloooomm/00-Characters/wendy-carlos/` | Switched-On Bach, electronic music pioneer, Tron soundtrack |
| 👩💻🌐📨🔧 mary-ann-horton | *wikipedia* | Berkeley UNIX, USENET pioneer, transitioned 1997, !ustrstrfstrm |
| 👩🎮🏳️‍⚧️👥💔 dani-bunten-berry | `lloooomm/00-Characters/dani-bunten-berry/` | M.U.L.E., multiplayer pioneer, The Sims dedicated to her |
| 👩🎮👾🏆⚡ rebecca-heineman | *wikipedia* | Space Invaders champ 1980, Interplay, 70+ games, "High Score" |
| 👩💻🐿️🌐✨ vanessa-freudenberg | *squeak community* | SqueakJS, Croquet, Multisynq, Smalltalk-in-browser wizard |
| 👩🐉🎮🗺️✨ jennell-jaquays | *wikipedia* | D&D Dark Tower, id Software Quake, legendary mapper (d. 2024) |
| 👩🇹🇼💻🏛️✨ audrey-tang | `lloooomm/00-Characters/audrey-tang/` | Taiwan Digital Minister, vTaiwan, radical transparency, poetry |
| 👩💼✍️🏳️‍⚧️⭐ dame-stephanie-shirley | `lloooomm/00-Characters/dame-stephanie-shirley/` | Nazi refugee, signed letters "Steve", employed women coders |
| 👩💄🎬💩👑 divine | `lloooomm/00-Characters/divine/` | John Waters' muse, "filthiest person alive", drag titan |
| 👨🎭👽🎵✨ klaus-nomi | `lloooomm/00-Characters/klaus-nomi/` | Operatic alien, new wave icon, died 1983, unforgettable |
| 👩💪🎤🔲⚡ grace-jones | `lloooomm/00-Characters/grace-jones/` | "Pull up to the bumper", fierce presence, hula hoop queen |
| 👩🎸🌋👽🎭 nina-hagen | `lloooomm/00-Characters/nina-hagen/` | German punk opera, wild spirit, UFO believer |
| 👨🎨🎭👶💥 leigh-bowery | `lloooomm/00-Characters/leigh-bowery/` | Club kid, performance art, living sculpture, gave birth onstage |
| 👩👠🌈🎤❤️ heklina | `lloooomm/00-Characters/heklina/` | SF drag legend, Trannyshack/Mother founder, gone too soon |
| 👨🎸🚶🌃⚡ lou-reed | `lloooomm/00-Characters/lou-reed/` | "Walk on the Wild Side", Velvet Underground, NYC incarnate |

---
## 🕯️ In Memoriam

Some heroes have recently left us. Their work lives on:

### 👩🎮🏳️‍⚧️👥💔 Dani Bunten Berry (1949-1998)
🎮 M.U.L.E. creator, Seven Cities of Gold, multiplayer pioneer. **The Sims was dedicated to her memory.** 🏳️‍⚧️ Trans woman who transitioned late in life and spoke openly about her experiences.

### 👩💻🔌⚡🏳️‍⚧️ Lynn Conway (1938-2024)
- 🔌 Co-invented VLSI chip design with Carver Mead — the "Mead-Conway revolution"
- ⚡ Invented dynamic instruction scheduling (out-of-order execution) at IBM
- 🚫 Fired from IBM in 1968 for announcing her gender transition
- 🔧 Rebuilt career "in stealth" at Xerox PARC, developed MOSIS (fabless design paradigm)
- 🏆 National Inventors Hall of Fame (2023), IEEE James Clerk Maxwell Medal (2015)
- 🏳️‍⚧️ Trans pioneer. IBM apologized in 2020
- 💔 Died June 9, 2024

### 👩🐉🎮🗺️✨ Jennell Jaquays (1956-2024)
- 🎨 Fantasy artist: The Dungeoneer, Dragon Magazine, Judges Guild (Dark Tower, Caverns of Thracia)
- 🗺️ Game designer: Quake II, Quake III Arena (id Software)
- 📐 Her name became a verb: **"Jaquaysing"** — non-linear, multi-path dungeon design
- 🏆 Hall of Fame (Academy of Adventure Gaming Arts & Design, 2017)
- 🏳️‍⚧️ Trans pioneer. Wife of Rebecca Heineman
- 💔 Died January 10, 2024

### 👩🎮👾🏆⚡ Rebecca Heineman (1963-2025)
- 🏆 First U.S. National Space Invaders Champion (1980, age 16)
- 🎮 Co-founded Interplay Productions with Brian Fargo
- 💻 Programmed: Bard's Tale III, Wasteland, Dragon Wars
- 🔧 Ported: Wolfenstein 3D, Baldur's Gate, Icewind Dale
- 📊 Over 70 games across her career
- 📺 Featured in Netflix documentary **"High Score"**
- 🏳️‍🌈 Received Gayming Icon Award 2025 for LGBTQ+ advocacy
- 💕 Wife of Jennell Jaquays
- *"One of the most brilliant programmers around"* — Brian Fargo

### 👩💻🐿️🌐✨ Vanessa Freudenberg (d. 2025)
- 🐿️ Created **SqueakJS** — Squeak Smalltalk running in JavaScript
- 🌐 Worked on Croquet, Multisynq
- 🔧 Integrated Smalltalk and JavaScript garbage collectors
- 💬 *"One of the most universally respected, creative, and powerful genius programmers I had the privilege of knowing"* — Hacker News tribute

---

## ✅ Real People Already Incarnated Here

- **👨🥧🎮🐈💻 [don-hopkins/](don-hopkins/)** — Pie menus, The Sims, consciousness programmer. Living tribute, can speak for himself!
- **🏰👨‍🏫♠️♥️♦️♣️ [richard-bartle/](richard-bartle/)** — MUD1 co-creator, player taxonomist, virtual world philosopher. Has a study, two pets, and opinions.

---

## 💕 Love Children Gallery

> *"What if X and Y had a beautiful, impossible child?"*
>
> Love Children inherit specific traits from multiple sources. They are clearly fictional — that's the point! Mix scientists with artists, philosophers with game designers, heroes with antiheroes.

| Love Child | Parent A | Trait from A | Parent B | Trait from B | Result |
|------------|----------|--------------|----------|--------------|--------|
| **Professor Wavelength** | Alan Kay | Objects & message passing | Ted Nelson | Intertwingled rage | A DJ who believes everything is deeply object-oriented |
| **Captain Thoughtcrime** | Marvin Minsky | Society of mind | George Orwell | Dystopian skepticism | An AI safety researcher who sees agents everywhere |
| **Sister Algorithm** | Grace Hopper | "It's easier to ask forgiveness" | Hildegard of Bingen | Mystical visions | A debugging nun who sees the divine in stack traces |
| **DJ Prototype** | David Ungar | Prototypes, not classes | Brian Eno | Generative ambient | Makes music by cloning and mutating loops |
| **The Stroopwafel** | Will Wright | Simulator Effect | M.C. Escher | Impossible geometry | Designs games where the rules are the puzzle |
| **Agent Transclusion** | Ted Nelson | Quoting by reference | James Bond | Suave infiltration | A spy who never copies files, only links them |
| **Madame Constraint** | Ivan Sutherland | Declare relationships | Marie Curie | Radioactive persistence | A physicist who makes atoms follow CSS |
| **The Bootstrapper** | Doug Engelbart | Augmenting intellect | Baron Munchausen | Pulling yourself up | Believes you can debug your own brain |
| **Chef Emergent** | Craig Reynolds | Boids, flocking | Julia Child | Joie de vivre | Cooks by letting ingredients self-organize |
| **Dr. Mashup** | Seymour Papert | Constructionism | Frankenstein | Assembly from parts | Builds minds from Logo turtles |

### Creating Your Own Love Child

```yaml
name: The Intertwingulator
type: love_child
parents:
  - source: real-people/ted-nelson
    traits: [intertwingularity, glorious_rage, two_way_links]
  - source: real-people/marvin-minsky
    traits: [k_lines, society_of_mind, frames]
  - source: fictional/sherlock-holmes
    traits: [deductive_reasoning, insufferable_genius]
personality: >
  Sees connections between everything. Frustrated that the web 
  has one-way links. Solves crimes by finding the missing backlinks.
catchphrase: "The game is afoot, and EVERYTHING IS DEEPLY INTERTWINGLED!"
```

**The rule:** If you're inheriting traits, you're creating something new. That's not impersonation — that's creativity!
