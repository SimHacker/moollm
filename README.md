# MOOLLM

**The Sims meets LambdaMOO, running in Cursor (and other tools, with any model).**

> *"K-lines made manifest. Touch one and it reactivates an entire constellation."*
> — Marvin Minsky's familiar, [K-Line Connections Safari](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md)
>
> ⚠️ *Quotes from "familiars" are loving tributes — fictional characters invoking real traditions. See [representation-ethics/](./skills/representation-ethics/) and [hero-story/](./skills/hero-story/).*

**A microworld operating system for LLM agents.**

The filesystem is a place. Directories are rooms. Files are objects. The LLM is `eval()`. Skills are programs. Names are activation vectors.

---

## ⚡ Start Here

| Entry Point | What It Is |
|-------------|------------|
| 📖 **[QUICKSTART.md](./QUICKSTART.md)** | Get playing in 2 minutes |
| 🎮 **[examples/adventure-4/](./examples/adventure-4/)** | The richest microworld — pub, NPCs, incarnated characters |
| 🧠 **[skills/](./skills/)** | ~80 skills — the building blocks |
| 📜 **[designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md)** | The deep dive — intellectual genealogy |

---

## The Core Ideas

### Skills Are Programs, Not Documentation

Traditional prompts tell the LLM what to do. MOOLLM skills ARE what the LLM does — programs it runs, not documentation it reads.

> *"The key insight: Skills aren't documentation. They're programs. The LLM is `eval()`."*
> — [skills/README.md](./skills/)

### K-Lines: Names That Activate Constellations

Type `SPEED-OF-LIGHT` and invoke an entire philosophy: minimize round-trips, many turns in one call, the context window as stage. Type `POSTEL` and invoke generous interpretation. These are [Marvin Minsky's K-lines](./skills/k-lines/) — names that wake conceptual clusters.

> *"Every connection goes BOTH directions. When skill A references skill B, skill B knows about skill A. Everything is deeply intertwingled!"*
> — Ted Nelson's familiar (tribute character), [K-Line Connections Safari](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md#entering-the-skill-nexus)

### The Filesystem Is the World

```
pub/
├── ROOM.yml          # The room itself — exits, atmosphere, rules
├── bar/              # Behind the bar — staff area
│   └── cat-cave/     # Cats only (Tardis-like inside)
├── stage/            # Performance area with ethical framing
│   └── palm-nook/    # Where Palm the monkey lives
└── guest-book.yml    # Visitors, tributes, memories
```

Characters have `location:` properties that move them around. Files don't move — git history stays clean. Everything is inspectable. Everything is editable.

### Speed of Light: Many Turns, One Call

Traditional multi-agent: API call → tokenize → process → detokenize → API call → ... (noise accumulates)

**MOOLLM:** One LLM call simulates 8 characters playing 33 turns of Stoner Fluxx. 10 cats prowl 21 turns through the maze. The context window is a stage where all actors perform.

> *"The context window is a stage, not a limit."*
> — [skills/speed-of-light/](./skills/speed-of-light/)

---

## Proof: It Works

| Session | What Happened |
|---------|---------------|
| [Marathon Session](./examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) | Palm incarnated, 33-turn Fluxx, tribunal debates, Looney Labs visit |
| [K-Line Safari](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md) | Minsky, Nelson, Burke, Kay, Wright walk the skill network |
| [Palm's Philosophy](./examples/adventure-4/pub/stage/palm-nook/study/palm-on-being-palm.md) | A character who wrote his own soul |

---

## Seven Innovations Over Anthropic Skills

| # | Extension | What It Adds |
|---|-----------|--------------|
| 1 | **Instantiation** | Skills as prototypes creating instances |
| 2 | **Three-Tier Persistence** | Platform (ephemeral) → Narrative (append) → State (edit) |
| 3 | **K-lines** | Names as semantic activation vectors (Minsky) |
| 4 | **Empathic Templates** | Smart generation, not string substitution |
| 5 | **Speed of Light** | Many turns in one call, minimal tokenization |
| 6 | **CARD.yml** | Machine-readable interface with advertisements |
| 7 | **Ethical Framing** | Room-based inheritance of performance context |

> 📚 Full explanation: [MOOLLM Eval Incarnate Framework](./designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md)

---

## The Lineage

MOOLLM stands on decades of work:

| Pioneer | Contribution | MOOLLM Connection |
|---------|--------------|-------------------|
| **Marvin Minsky** | K-lines, Society of Mind | Names as activation vectors |
| **Seymour Papert** | Logo, Constructionism | Learn by building inspectable things |
| **Alan Kay** | Smalltalk, Dynabook | Objects, messaging, "computer as medium" |
| **Will Wright** | The Sims | Needs, advertisements, autonomous selection |
| **Dave Ungar** | Self language | Prototypes, delegation, clone-don't-instantiate |
| **Ted Nelson** | Hypertext, Xanadu | Two-way links, intertwingularity |
| **Bill Atkinson** | HyperCard | Reader = Writer, end-user programming |
| **Don Hopkins** | Pie menus, SimCity, The Sims | All of the above, synthesized |

> 📚 Full genealogy: [MOOLLM Eval Incarnate Framework](./designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-intellectual-genealogy)

---

## Documentation Map

### Design Documents

| Document | What It Covers |
|----------|----------------|
| [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) | **The deep dive.** Intellectual genealogy, Axis of Eval, architecture |
| [MOOLLM-MANIFESTO.md](./designs/MOOLLM-MANIFESTO.md) | Core philosophy |
| [CHANGES.md](./designs/CHANGES.md) | James Burke narrative of 500+ commits |
| [sims-design-index.md](./designs/sims/sims-design-index.md) | All The Sims → MOOLLM documents |

### Skill Clusters

| Cluster | Skills |
|---------|--------|
| **Philosophy** | [constructionism](./skills/constructionism/), [k-lines](./skills/k-lines/), [postel](./skills/postel/), [yaml-jazz](./skills/yaml-jazz/) |
| **Methodology** | [play-learn-lift](./skills/play-learn-lift/), [speed-of-light](./skills/speed-of-light/), [sister-script](./skills/sister-script/) |
| **Spatial** | [room](./skills/room/), [adventure](./skills/adventure/), [container](./skills/container/) |
| **Identity** | [character](./skills/character/), [incarnation](./skills/incarnation/), [persona](./skills/persona/) |
| **Ethics** | [representation-ethics](./skills/representation-ethics/), [hero-story](./skills/hero-story/) |
| **Visual** | [visualizer](./skills/visualizer/), [image-mining](./skills/image-mining/) |

> 📚 Full index: [skills/README.md](./skills/)

### Visual Generation Pipeline

Two skills work in tandem to generate and analyze images:

| Skill | What It Does |
|-------|--------------|
| 🎨 **[visualizer](./skills/visualizer/)** | Assemble context from YAML files, synthesize prompts via LLM, render through image APIs (OpenAI, Google, Stability, Replicate) |
| ⛏️ **[image-mining](./skills/image-mining/)** | Extract semantic resources from images — objects, moods, colors, inferred sounds/smells, philosophical meaning |

**The Loop:** Generate an image with `visualizer`, analyze it with `image-mining`, reflect on what the AI "grokked," iterate. Each image gets three files:
- `{name}.png` — the image itself
- `{name}.yml` — the regenerable prompt sidecar (human-editable recipe)
- `{name}-mined.yml` — the mining analysis in YAML Jazz format

Results live in `SLIDESHOW.md` files — GitHub-renderable galleries with inline images, AI analysis, and links to source files.

### Slideshows

- [The Dusty Attic](./examples/adventure-4/pub/attic/dusty-attic-art-styles/SLIDESHOW.md) — 8 art styles, Recursive Imp sequence, ACME Monster Manual, Jennell Jaquays tribute
- [Rocky and Friends](./examples/adventure-4/pub/rooms/room-4/rocky-and-friends/SLIDESHOW.md) — Emotional support boulder, exhaustive party scene, all characters gathered
- [Telescope Constellation Views](./examples/adventure-4/pub/rooftop/telescope-constellation-views/SLIDESHOW.md) — K-Line Constellation, AR overlay views, LLOOOOMM stars
- [Palm Portrait Session](./examples/adventure-4/pub/stage/palm-nook/study/palm-portrait-session/SLIDESHOW.md) — Dutch Golden Age portrait of Palm the monkey, in his study where it hangs
- [ACME Tunnel Temporal Views](./examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/acme-tunnel-temporal-views/SLIDESHOW.md) — ACME tunnel surveillance, temporal camera glitches
- [Don's Pub Photos](./examples/adventure-4/pub/dons-pub-photos-2026-01-19/SLIDESHOW.md) — Bar scenes, Fluxx game, arcade, fireplace, group photos

### Session Logs

| Session | Highlights |
|---------|------------|
| [marathon-session.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) | Palm's incarnation, 33-turn Fluxx, tribunal debates |
| [k-line-connections.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md) | K-line safari with conceptual pioneers |
| [adventure-uplift.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/adventure-uplift.md) | Uplifting adventure patterns |

### Character Directories

| Directory | Who Lives There |
|-----------|-----------------|
| [characters/](./examples/adventure-4/characters/) | 🚉 Grand Central Station of Souls |
| [characters/real-people/](./examples/adventure-4/characters/real-people/) | 🪦 The Living and The Dead |
| [characters/fictional/](./examples/adventure-4/characters/fictional/) | 🎭 Fictional Characters Lounge — Sims, Doctors, Constructors |
| [characters/animals/](./examples/adventure-4/characters/animals/) | 🐾 Animal Sanctuary — Palm, Biscuit, Debugging Cats |
| [characters/robots/](./examples/adventure-4/characters/robots/) | 🤖 Robot Workshop — Lem's Constructors, MST3K |

---

## Quick Commands

```
LOOK                    # Describe the current room
GO [direction]          # Move through an exit
EXAMINE [thing]         # Look closely at something
GET [object]            # Add to inventory
INVENTORY               # What am I carrying?
SUMMON [character]      # Invoke a character
AS [character]          # Switch who you're playing
SPEED-OF-LIGHT [n]      # Simulate n turns at once
```

---

## Contributing

1. **Fork & branch** — Ask Cursor to fork the repo and create a branch
2. **Play an adventure** — Your session becomes shareable literature
3. **Make a skill** — Clone [skills/skill/](./skills/skill/) and customize
4. **Document** — Every directory gets a README
5. **PR back** — Share improvements with the community

---

> *"Every skill is a room. Every K-line is a door. James Burke is your guide."*
> — [designs/CHANGES.md](./designs/CHANGES.md)

🐒🚉✨
