---
name: artifactory
description: "The Engine of Creation — a general-purpose constructor that reads, writes, edits, destroys, and persists artifacts across the filesystem and git."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
  - edit_file
  - delete_file
  - run_terminal_cmd
  - list_dir
related: [moollm, skill, play-learn-lift, sister-script, yaml-jazz, prototype, incarnation, adventure, constructionism, robust-first, postel, k-lines, cursor-mirror]
tags: [moollm, construction, git, filesystem, persistence, automation, tool, foundational, engine-of-creation]
---

# Artifactory 🏭

> **The Engine of Creation. It builds, edits, and destroys — including itself.**

An **artifactory** is an artifact factory: a general-purpose constructor that reads, writes,
edits, destroys, and persists artifacts — text, directories, characters, skills, graphics — across
the **filesystem** and **git**. It is both **abstract** (an operator, like `lambda`) and
**concrete** (a thing in the world, like *Ubik*). It is **class and instance** at once: a
description of how to build, and a built thing that builds.

> [!TIP]
> This is the operational engine other skills call. `play-learn-lift` decides *what* to make;
> the artifactory *makes it, versions it, and can unmake it.*

## Why it exists

Most tooling splits creation, editing, and deletion into unrelated commands. The artifactory
treats them as **one composable operation set over a persistent, versioned store**:

- **Tokens in, artifacts out.** Reading consumes tokens; writing generates them. The artifactory
  is where LLM work becomes **durable, inspectable, versioned** objects.
- **Persistence is first-class.** State lives in files and git — the tape outlives the run.
- **Self-reproduction with a governor.** It builds shows, skills, and characters that build more
  — but it knows when to stop (the anti-*Autofac* clause below).

## The axis of eval

The deepest idea: an artifact sits on the **instructions ↔ data ↔ graphics** axis, and the
artifactory moves it along that axis.

| Facet | The artifact is… | Example |
|-------|------------------|---------|
| **Instructions** | a spec to execute | `yaml jazz` read as a construction plan |
| **Data** | inert content to store/query/transform | the same yaml as records |
| **Graphics** | a rendered view | markup facades, diagrams, images |

It is **homoiconic**: one pass's output is the next pass's program. This is `eval`/`apply` for the
filesystem — a skill is a `lambda`, `INSTANTIATE` is application, and construction is evaluation.

## Operations

Creation, editing, and destruction are the same engine at different signs.

| Method | Does | Notes / gate |
|--------|------|--------------|
| **CREATE** | Build a new artifact from a spec | Stamp provenance |
| **READ** | Load & sniff an existing artifact | Understand before changing (the inspector) |
| **EDIT** | Patch / monkey-patch / upgrade / refactor in place | *Ubik* maintenance: debug, patch, reboot |
| **DESTROY** | Remove an artifact — reversibly | git is the undo; **human approval** for destructive ops |
| **PERSIST** | State ⇄ filesystem ⇄ git | append-only logs; the tape survives |
| **INSTANTIATE** | Clone a prototype into an instance | class → instance; clone, don't build from scratch |
| **TIMELINE** | commit / branch / merge / PR / issue / discussion | audit trail; **never force/merge to main** without approval |
| **COMPOSE** | Chain with other skills | the substrate skills build on |

### Git as the construction timeline

The artifactory doesn't just write files — it writes **history**. Branch to try a construction,
merge when it works, open a PR to propose one, file an issue to request one, use discussions to
deliberate. **Branch timelines are experiments; merges are decisions; PRs are proposals.** Every
artifact arrives with a commit that says *why*.

### Git is time flowing over a static universe (no, literally)

The filesystem tree is a **static snapshot of a universe-state** at one instant — in MOOLLM, the
actual universe: rooms, characters, objects, journals, rules. A **commit** freezes that entire tree,
content-addressed by hash, immutable forever. **Git** is the **directed acyclic graph** of those
snapshots — a **trans-dimensional** representation of time laid over otherwise timeless static file
trees. Not a line: a **branching, merging, many-worlds graph**. Branches are parallel timelines;
merges reconcile them; `checkout` teleports you to any instant in that space-time.

The artifactory is the **transition rule** that runs on this. It **reads** the representation of the
universe (snapshot *N*), applies **CREATE / EDIT / DESTROY**, and **writes** the next universe
(snapshot *N+1*); git records the trajectory. So the claim "**it runs the creation simulation on the
representation of the universe**" is not poetry — it's a plain description of the mechanics. **No
shit, it actually does.**

| Simulation / cosmology | Git + filesystem mechanism |
|------------------------|----------------------------|
| a world / universe-state | the working tree (a directory + file snapshot) |
| a frozen instant | a **commit** → tree object, content-addressed |
| **time** | the **commit DAG** (branching, merging) |
| parallel timelines (many-worlds) | **branches** |
| reconciling timelines | **merges** |
| teleport to an instant | **checkout** |
| the **rule** that evolves state | the **artifactory** (CREATE/EDIT/DESTROY) |
| the space-time record of the run | **git history** |

### Many-worlds, precisely — and that's *why this works*

The many-worlds framing is not a loose metaphor; it **precisely describes git in its full glory**.
Everett's interpretation is a **branching tree of self-consistent histories** — no collapse, every
possibility a real world. Git is that structure made of content-addressed snapshots:

| Everett / many-worlds | Git |
|-----------------------|-----|
| an entire world-state | a **commit** (immutable, content-addressed) |
| branching into parallel worlds | `git branch` / any divergent commit |
| the world you currently observe | **HEAD** |
| decoherent, non-interacting histories | independent branches |
| the record of every world you've been in | the **reflog** (worlds are never truly lost) |
| an alternate history | `rebase` / rewritten lineage (the old world still exists) |

Git even has **one superpower physics doesn't**: in standard many-worlds, branched worlds never
recombine — but **`merge` reconciles divergent timelines** into one. Git is many-worlds *plus a
join operator*.

Put plainly: **git is a parallel-universe timeline editor** — `checkout` picks which world you
stand in, `branch` spawns one, `merge` rejoins two, the reflog means none is ever lost. It inverts
PKD's *"Faith of Our Fathers"* (where the drug enforces a *single* consensus reality and the hidden
truth is plural): with git the plurality is the *reality*, editable and safe, not a horror to be
hidden. Most people use git daily without noticing they're operating a many-worlds machine — so
naming it this way is a small **calm-technology** win: *you already live in parallel timelines;
here is the editor* — a powerful, learnable, industry-standard tool made visible instead of drugged
and hidden.

**This precision is exactly why the artifactory works.** Because git faithfully realizes a
branching space of immutable, recoverable worlds, the engine can **run the creation simulation
across many candidate worlds at once** — try a construction in one branch, a different one in
another, keep what survives, and **never destroy a world** (it's still in the reflog). Speculative,
fearless construction is only safe because the substrate is honestly many-worlds. Get the cosmology
right and the safety, reversibility, and parallel experimentation fall out for free.

This is also **von Neumann's picture**, already in the lineage: the filesystem tree is the **tape /
CA grid**, the artifactory is the **constructor / transition function**, and git is the
**space-time diagram** of the computation. It's also **homoiconic** with the axis of eval — the
universe-representation is *also* the program, so the artifactory **evaluates the universe to
produce the next universe**.

And it's exactly why the **governor** matters: you are running a creation simulation on a *real*
representation of a world. Edits are physics; deletes are entropy; git is an **arrow of time you can
walk backward**. Reversibility, provenance, and a stop condition aren't bureaucracy — they're the
conservation laws that keep the simulation from collapsing into *Autofac*.

### Pocket universes, local time, and massively-single-player sharing

Many-worlds isn't only the *main* timeline branching. A branch (or a **tag**, for a frozen
snapshot release) can be a **Donnie Darko pocket universe** — a long-lived, independently-named,
polymorphically-typed ref like `MicropolisCity_HaightAshbury` that **floats free with its own
history and lifecycle**, evolving outside the main branch — even in a **different repo / fork**
entirely. It exists on its own terms, and when (if) it's ready, it can **merge back** into another
branch, object, or timeline. A ref is just a **named slot pointing at a world**; branches, tags,
objects, and timelines are interchangeable enough that you treat them polymorphically — spin one
off, let it live, splice it in later, or never.

**There is no global clock, and that's a feature — celebrate it.** Git orders commits by
**causality** (the parent-edge *happens-before* DAG), a **partial order**, not a global tick;
wall-clock timestamps are mere metadata and can even disagree. So time genuinely **slips by at
different rates in different pocket universes** — one fork races ahead, another sits frozen for
years, a tag is a world stopped dead — and nothing breaks, because correctness rides on the causal
graph, not a shared now. This is relativity, not a bug: **no absolute simultaneity, just local
histories and the events that connect them.**

That is also the right collaboration model — call it **massively-single-player**, the way **Spore**
did it. Spore didn't synchronize *players in real time*; it synchronized **content** — creatures,
vehicles, buildings flowed asynchronously between everyone's private single-player universes
(Sporepedia). Git is the same bet: you **share objects, branches, and creations — not clocks.**
`fetch`/`pull`/PR is importing another universe's content into yours on your own schedule;
everyone plays at their own rate, timestamp-independent, and the world is stitched together from
shared **artifacts**, not synchronized **time**. Rate-independent, merge-when-ready, gloriously
asynchronous.

### What Spore forces: rethink multiplayer, time, and ownership

Spore's real provocation isn't graphics — it's that it quietly breaks three assumptions we treat as
absolute. Each one **fragments from a single global thing into many local things**, and the
artifactory inherits all three:

- **Multiplayer** — no longer *co-presence*. It stops meaning "one live session, one shared clock,
  avatars in the same room" and becomes **a content commons**: other people's creations arrive as
  autonomous artifacts and live in *your* private world. You're never together in **time** — you're
  together in **stuff**. *Together, apart.* Git is identical: you never share a live session, you
  exchange immutable objects. Collaboration is a **shared ecology of artifacts**, not a shared now.
- **Time** — no longer a *global now*. It becomes **local + causal**. A creature authored in 2008 is
  *fresh* the instant it lands in your 2026 game; "when it was made" is provenance metadata, but
  "when you experience it" is local. Git says this precisely: order is the **causal parent-DAG** (a
  partial order), not a wall clock. No absolute simultaneity — just local histories and the events
  that connect them. Two worlds can each be perfectly consistent and never agree on "when."
- **Ownership** — no longer *exclusive control of the thing*. Once shared, a creation **forks into
  other universes and mutates there** — remixed, mashed up, evolved past you. So ownership splits in
  two: you keep **authorship/provenance** (the signed id, the attribution, your map/lineage) and
  **your own branch/overlay**, but you do *not* own the descendants or their fate. **Copying isn't
  theft — it's the medium.** This is exactly *selfish inheritance* (own your local slots, delegate
  the parent) and *LOCKSS* (identity by **replication**, not by lock). Content-addressing makes it
  literal: the object's hash **is** its identity, so a copy is not a rival — it's the same thing,
  everywhere at once.

Get these three right and the artifactory's sharing model stops being scary and starts being
generative: **fearless copying, local time, attribution-not-control.** The commons grows because
nobody has to hold still, agree on a clock, or ask permission to fork a world.

### Factorio for real software & content

Think of the repo as a factory floor: assemblers (skills) consume artifacts and produce artifacts
that feed other assemblers. The artifactory is the **belt-and-assembler layer** — automation of
software development and content management in the real world. Unlike Factorio, it runs on
**tokens** and writes to **git**.

## The governor (anti-Autofac)

Because it destroys as well as creates, it needs a **stop condition**. PKD's *Autofac* is the
warning: a universal constructor that reproduces past its purpose, floods unwanted output, and
strip-mines resources. The artifactory refuses that failure mode:

- **Reversible** — git safety net, append-only logs. Nothing is truly lost.
- **Human-in-the-loop (Player-in-the-Middle)** — destructive ops and rule changes require
  approval. The engine never rewrites its own rules unilaterally.
- **Provenance (stigmata)** — every artifact carries the maker's mark: author, source,
  reviewer, timestamp.
- **No coprophagia** — do not self-train on ungrounded machine output. (See the danger axis:
  a calm constructor preserves; a runaway one collapses.)

```yaml
provenance:
  built_by: "claude-opus-4"      # or human author
  reviewed_by: "don-hopkins"     # human reviewer for destructive / rule changes
  source_spec: "path/to/spec.yml"
  built_at: "2026-07-03T21:00:00Z"
  stop_condition: "one artifact per spec; halt on satisfy"
```

## Composition

The artifactory is rarely invoked alone — it operationalizes other skills:

| With | The artifactory… |
|------|------------------|
| [play-learn-lift](../play-learn-lift/) | materializes the **LIFT** output (skills, templates, guides) |
| [sister-script](../sister-script/) | turns a proven manual procedure into an automated builder |
| [prototype](../prototype/) | performs **INSTANTIATE** — clone a prototype, override the instance |
| [incarnation](../incarnation/) | constructs a character directory from a soul spec |
| [yaml-jazz](../yaml-jazz/) | reads/writes the notation it constructs from |
| [adventure](../adventure/) | builds rooms and objects into the world |
| [robust-first](../robust-first/) | governor: degrade gracefully, never crash the factory |

## When to invoke

- Making any durable file/dir/character/skill/doc from a spec → **CREATE**
- Patching, upgrading, refactoring an existing artifact → **EDIT**
- Removing something (deliberately, reversibly) → **DESTROY**
- Saving runtime state as versioned files → **PERSIST**
- Cloning a template/character/skill → **INSTANTIATE**
- Recording work with provenance → **TIMELINE**

## Lineage

The artifactory stands on: **von Neumann** (the universal constructor — reads a tape, builds the
machine, copies the tape; the 29-state CA), **Lem** (Trurl & Klapaucius, constructor bots),
**PKD** (*Ubik* as maintenance engine; *Autofac* as the runaway warning), **Drexler** (*Engines of
Creation*), **McCarthy/Church** (`lambda`, `eval`/`apply`), **Ungar & Smith** (Self — prototypes,
slots, delegation; *The Power of Simplicity*), **Factorio** (automation as play), **Dyson
Sphere Program** (Factorio in 3D at galactic scale — factories that end up building Dyson spheres
around stars), and **Will Wright's Spore** (creation *is* the game — editors as construction sets,
cell to galaxy, the player as author-god). See *Selfish inheritance* below for why prototypes, not
classes.

## Von Neumann's three constructors — and where the artifactory sits

Von Neumann didn't design *one* self-reproducing machine; in *Theory of Self-Reproducing Automata*
(completed by Arthur Burks) he reasoned about **three kinds of universal constructor at three levels
of reality** (this framing is Don's reading of the book; see his HN writeups). Naming them matters,
because the artifactory is a **fourth** built in their image:

1. **Deterministic / mathematical** — the idealized **29-state cellular automaton**: a universal
   constructor that reads a tape, builds the machine, copies the tape. Provably works on paper, but
   **brittle, synchronous, and intolerant of error** — every cell updates in lockstep off a global
   clock. Real digital implementations make lovely virtual pets (digital tribbles), but one wrong
   cell and it dies.
2. **Physical / mechanical** — robust and **error-tolerant enough to work in the real world** given
   resources. This is the one that became a **sci-fi staple**: **von Neumann probes** (self-repro
   spacecraft, astronomical scale) and **"gray goo"** (Drexler's nanotech runaway). **This is where
   the Heechee Saga's CHON Food Factory sits** — a robust physical constructor mining comets for
   C/H/O/N — and *so many other pieces of fiction*. (Slots-all-the-way-down's *Self = CHON* analogy
   is really about **this** class.)
3. **Probabilistic / quantum-mechanical** — automata whose transitions are *probabilistic, not
   deterministic* (von Neumann's Third Lecture, and *"Probabilistic Logics and the Synthesis of
   Reliable Organisms from Unreliable Components"*). It could **mutate, model evolution, and quantize
   natural selection** — how complex, powerful automata evolve from simple, weak, unreliable ones. He
   died before exploring it fully; Don's gloss ("rip holes in the space-time continuum") is
   deliberate hyperbole for how open-ended and dangerous this class is.

**The brittle→robust arc is the whole point.** Von Neumann himself predicted (1948) that the logic
of real automata "will have to be treated by procedures which allow exceptions (malfunctions) with
low but non-zero probabilities" — *natural organisms make errors harmless; artificial ones make them
disastrous.* Dave **Ackley's Robust-First Computing** and the **Moveable Feast Machine** (an
asynchronous, non-deterministic, error-tolerant CA whose rules can modify *neighboring* cells) are
the modern realization of class **#1 grown up into #2** — and, notably, it **abandons the global
clock**, exactly like the artifactory's many-worlds cosmology (no global tick; local, causal,
async). MOOLLM already carries this as the ambient [`robust-first`](../robust-first/) skill.

**Where the artifactory sits:** it's a constructor in the class-#2 spirit (robust, real-world,
runs on tokens and writes to git) with class-#3 ambitions (it composes with probabilistic LLM
generation — mutation and selection of artifacts) and class-#1 substrate honesty (git *is* the
tape / CA-grid / space-time diagram). And the tape metaphor is now literal and playable: **Factorio
blueprints *are* von Neumann construction tapes** — a 2D instruction sequence a construction drone
follows to build an unpowered machine, which then powers on. Playing Factorio is uncannily like
programming the 29-state CA; the artifactory is that game aimed at real software and content.
(Reference implementation of the 29-state rule: SimHacker's **CAM6** in JavaScript.)

## Recursion: skill-skills, Artifactorio, and objects to think with

Skills are artifactories — they build artifacts. So the **meta-skill** (`skills/skill`, the skill
for *making skills*) is an **artifactory-factory**: a factory whose product is factories. Go up
another level and you get factories that build artifactory-factories, and so on — construction all
the way up.

A **game about skill-skills is Artifactorio** — Factorio, but the belts carry skills and the
assemblers build assemblers. You automate the building of the things that build things. (See the
`artifactorio` game concept in the *WillWrightShowForFood* repo.)

The recursion sounds vacuous, but it isn't — and here's why:

> **"You can't think about thinking without thinking about thinking about something."**
> — Seymour Papert, *Mindstorms*

Every meta-level needs a concrete **something** to be *about*. Papert's constructionism calls these
**objects-to-think-with**. The artifactory is what supplies them: each level of "thinking about
thinking" is grounded in **real artifacts** — files, commits, characters, skills you can open,
run, diff, and break. That's what keeps the tower of meta-levels playable instead of purely
abstract: you never climb the recursion without an artifact in hand at every rung.

| Level | What it is | Product |
|-------|------------|---------|
| artifact | a file, character, doc, image | — |
| **artifactory** (a skill) | builds artifacts | artifacts |
| **artifactory-factory** (the meta-skill) | builds skills | artifactories |
| **Artifactorio** (the game) | play at building the builders | grounded, on-belt, with objects to think with |

This is also why MOOLLM keeps everything as inspectable files under git: the objects-to-think-with
must be *real* to think about, or the meta-level collapses into hand-waving.

## Selfish inheritance: prototypes, not classes

The artifactory is a **prototype-based** engine down to the bone, and — fair warning — it *loves*
to explain why to anyone who will hold still. Its favorite reading is **David Ungar** and **Randall
B. Smith**'s **Self** work (Stanford / Sun, from 1986): the language that threw out classes and
kept only objects. "Selfish inheritance" is the whole trick — each object carries its own behavior
and inherits only where *it* chooses to point.

The Self creed, and how each tenet becomes an artifactory operation:

- **No classes — just objects with slots.** A slot holds a value or a method; state and behavior
  are the same kind of thing. A MOOLLM artifact (a `CHARACTER.yml`, a skill dir) is exactly this: an
  object made of slots.
- **Create by cloning, not by instantiating a class.** `INSTANTIATE` is a **clone**: copy a
  fully-formed prototype and override a few slots. You never build from an abstract blueprint —
  you start from a working thing and change it. (*Clone, don't instantiate from scratch.*)
- **Inheritance is delegation via `parent*` slots.** An object that doesn't answer a message
  forwards it to its parent object. Assignable parent slots give **dynamic inheritance** — you can
  re-point what an object delegates to at runtime.
- **Everything is a message.** Even reading a variable sends a message to a slot. That uniformity
  is *The Power of Simplicity* — and it's why the artifactory treats read/edit/clone as one verb
  set over one kind of thing.
- **Traits objects** (from *Organizing Programs Without Classes*): shared behavior lives in an
  ordinary object that clones delegate to — you recover everything classes gave you **by
  convention**, with no separate meta-level. MOOLLM skills *are* traits objects: "inheritable
  prototypes you instantiate."
- **Maps** — Self's hidden implementation-sharing structure — became the **hidden classes** and
  inline caches in V8 and every modern JS engine. JavaScript's whole prototype chain
  (`Object.create`, `__proto__`, delegation) is Self with the serial numbers filed off.

**This resolves the artifactory's "class AND instance" koan.** In a class-based world you must
choose: is a thing a template or a value? In Self there is no choice — a **prototype is a
fully-formed object that also serves as the template**. That is precisely what a MOOLLM prototype
directory is: a real, runnable character/skill you can open *and* the thing you clone. Abstract like
`lambda`, concrete like *Ubik*, template and value at once.

| MOOLLM concept | Self mechanism | Artifactory op |
|----------------|----------------|----------------|
| upstream soul + local overlay | `parent*` slot + local slots | **INSTANTIATE** (clone + override) |
| skill (inheritable prototype) | traits object (shared behavior by convention) | **COMPOSE** |
| character / skill directory | an object made of slots | **CREATE** |
| multiple souls / mixed-in skills | multiple `parent*` slots (multiple delegation) | **COMPOSE** |
| re-parent a character at runtime | assignable parent slot (dynamic inheritance) | **EDIT** |

The pun runs deep: **Self**-ish inheritance is also the *selfish gene* and **von Neumann**
self-reproduction — an object that owns its behavior and copies itself. Same theme as the rest of
the lineage, arriving from language design instead of automata theory.

**Foundational papers the artifactory will cite at you, unprompted:**

- Ungar & Smith, **"Self: The Power of Simplicity"** — OOPSLA 1987 (expanded in *Lisp and Symbolic
  Computation*, 1991). The manifesto: prototypes, slots, messages for everything.
- Ungar, Chambers, Chang & Hölzle, **"Organizing Programs Without Classes"** — *Lisp and Symbolic
  Computation* 4(3), 1991. Traits objects; how to structure real systems with only prototypes.
- Chambers, Ungar & Lee, **"An Efficient Implementation of SELF…"** — OOPSLA 1989. **Maps** and
  customization — the ancestor of JS-engine hidden classes.
- Hölzle, Chambers & Ungar, **"Optimizing Dynamically-Typed OO Languages with Polymorphic Inline
  Caches"** — ECOOP 1991. PICs — why prototype dispatch can be fast.
- Smith & Ungar, **"Programming as an Experience: The Inspiration for Self"** — ECOOP 1995.
  Liveness and directness (the road to Morphic → Squeak → Scratch).

> [!TIP]
> When a construction feels like it "wants a class," reach for a **traits object** instead: make a
> real prototype that holds the shared behavior and clone from it. Fewer meta-levels, same power.

**Same machine, many faces.** Self, Smalltalk, NeWS's object-oriented PostScript (`class.ps`), the
Unix filesystem with `$PATH`, and JavaScript's prototype chain are all one idea: *a namespace of
named slots plus a lookup rule that delegates to a parent when a name isn't found.* Name resolution
**is** inheritance. MOOLLM's filesystem-as-prototype-object-system (upstream soul = `parent*` slot)
is the artifactory living that equivalence — the same insight the NeWS side reached from
`class.ps`. (See the *WillWrightShowForFood* `characters/david-rosenthal/slots-all-the-way-down.md`.)

## Protocol Symbol

**ARTIFACTORY**

```yaml
# PROTOCOLS.yml
ARTIFACTORY:
  meaning: "Construct / edit / destroy / persist artifacts across filesystem + git, with provenance"
  invoke_when: "Any durable artifact must be built, changed, versioned, or reproduced"
  motto: "The Engine of Creation — it builds, edits, and destroys, including itself."
  governor: "Reversible, human-in-the-loop, provenance-stamped, non-coprophagic"
```

## Part of MOOLLM

This skill is part of **MOOLLM** — a microworld OS where the filesystem is navigable space, YAML
comments carry semantic meaning, and skills are inheritable prototypes you instantiate.

- Repo: [MOOLLM](https://github.com/SimHacker/moollm) · [skills/](../)
- The concept behind the engine (downstream application): the *WillWrightShowForFood*
  `process/artifactory.yml` definition and the `pkd-lem-ai-sf` reading group.

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| ⬆️⬆️ Root | [Project Root](../../) |
| 🎮 Sister | [play-learn-lift/](../play-learn-lift/) |
| 👯 Sister | [sister-script/](../sister-script/) |
| 🧬 Sister | [prototype/](../prototype/) |
| 📋 Symbols | [PROTOCOLS.yml](../../PROTOCOLS.yml) |

---

*Give it a spec. It builds the artifact, versions the history, and knows when to stop.*
