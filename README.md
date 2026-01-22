# MOOLLM 🐒🚉✨

> **Skills are programs. The LLM is `eval()`. Empathy is the interface.**  
> — **[The Eval Incarnate Framework](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md)**

**The Sims meets LambdaMOO, running in Cursor (and other tools, with any model).**

A **filesystem-incarnated skill framework** — a microworld OS for LLM agents.

- The **filesystem is a place**  
- **Directories are rooms**  
- **Files are objects and state**  
- **Names are activation vectors (K-lines)**  
- **Skills are runnable programs** — not just docs  
- The LLM pivots text across **Code / Data / Graphics** via the **[Axis of Eval](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-axis-of-eval)**

If you only read one thing, read this:  
📜 **[designs/eval/EVAL-INCARNATE-FRAMEWORK.md](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md)**  
…and then keep following links until your brain starts glowing. 🔮

---

## ⚡ Start Here

### 1) The framework hub (readable, index-y, linky)
📜 **[Eval Incarnate Framework](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md)**  

If you read only 3 sections:  
- **[The Word](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-word)** — The thesis in one paragraph
- **[The Axis of Eval](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-axis-of-eval)** — Code, Data, Graphics unified
- **[CARD.yml: The Skill Interface](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface)** — How skills advertise

### 2) Play the richest microworld
🎮 **[examples/adventure-4/](./examples/adventure-4/)** — pub, rooms, NPCs, incarnated characters, logs, images, proofs

### 3) Get moving fast
📖 **[QUICKSTART.md](./QUICKSTART.md)** — "get playing in 2 minutes"

### 4) Browse the skill library
🧠 **[skills/](./skills/)** — ~80 skills, the building blocks  
Start at: **[skills/README.md](./skills/README.md)**

### 5) Meet the giants
🏛️ **[Hall of MOOLLM Heroes](./examples/adventure-4/characters/real-people/README.md#-hall-of-moollm-heroes)** — The people who made this possible

### 6) Meet the animals
🐾 **[Animal Sanctuary](./examples/adventure-4/characters/animals/)** — Palm the monkey, Biscuit the dog, 8 terpene-named kittens, 8 puppies, Confetti Crawler the worm

---

## 🧠 90-Second Mental Model

MOOLLM is "eval() made real" — in the filesystem.

**Incarnate skills** aren't just prompts — they have:
- an interface (**[CARD.yml](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface)**)
- instantiation (**[Seven Extensions](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#seven-extensions-over-anthropic-skills)**)
- persistence (**[Three-Tier Persistence](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#three-tier-persistence)**)
- delegation/inheritance (**[Glossary](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#glossary)**)
- semantic activation (**[K-lines](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980)**)
- ethics framing (**[Ethical Framing Inheritance](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#ethical-framing-inheritance)**)

**Same text, different stance:**
- treat it as **Data** (schema, diff, validate)
- as **Code** (imperative behavior in comments)
- or as **Graphics** (render Markdown/Mermaid or generate images)

That's the **[Axis of Eval](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-axis-of-eval)**.

---

## 🧭 Guided Tours (Choose Your Adventure)

### 🛠️ Building Skills
1. **[The Word](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-word)** — The thesis
2. **[Axis of Eval](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-axis-of-eval)** — Code/Data/Graphics pivot
3. **[CARD.yml](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface)** — Machine-readable interface
4. **[Seven Extensions](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#seven-extensions-over-anthropic-skills)** — Beyond Anthropic Skills
5. **[Three-Tier Persistence](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#three-tier-persistence)** — Ephemeral / Narrative / State

### 🗺️ Building Worlds (Rooms + Movement + Social Boundaries)
- **[Vehicles: Portable Rooms](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#vehicles-portable-rooms)**
- **[Home vs Location](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#home-vs-location)**
- **[Boundary Types](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#boundary-types)**
- **[The Tardis Pattern](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-tardis-pattern)**
- **[The Guest Book Pattern](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-guest-book-pattern)**

### 🧑‍⚖️ Ethics Focus (Real People, Tribute, Framing)
- **[The Tribute Protocol](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-tribute-protocol)**
- **[Representation Spectrum](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-representation-spectrum)**
- **[Ethical Framing Inheritance](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#ethical-framing-inheritance)**
- **[Ethical Protocol for Real People](./examples/adventure-4/characters/real-people/README.md#-ethical-protocol-real-people)** — Tribute, ephemeral, mashup, love child
- **[Love Children Gallery](./examples/adventure-4/characters/real-people/README.md#-love-children-gallery)** — Fictional mashups (where the fun happens!)
- Skills: **[representation-ethics/](./skills/representation-ethics/)** | **[hero-story/](./skills/hero-story/)**

---

## ✅ Proof That It Works (Read the Receipts)

### Palm — The Canonical Example
- **Framework section:** **[Palm: The Canonical Example](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#palm-the-canonical-example)**
- **The epic log:** **[marathon-session.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md)**
- **Palm's own writing:** **[palm-on-being-palm.md](./examples/adventure-4/pub/stage/palm-nook/study/palm-on-being-palm.md)**

### K-line Safari (Skill Network as a Place)
- **[k-line-connections.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md)**

### Speed of Light (Many Turns — One Call)
- Framework: **[Speed of Light](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#speed-of-light)** | **[Speed of Light Proofs](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#speed-of-light-proofs)**
- Skill: **[skills/speed-of-light/](./skills/speed-of-light/)**

### The Simulator Effect
- **[The Simulator Effect](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect)** — Will Wright's insight: players imagine simulations are richer than they are

---

## 🧩 Core Parts (Links, Not Lectures)

### Interfaces: CARD.yml
- **[CARD.yml: The Skill Interface](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface)**
- **[Cards as Ethical Smart Pointers](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cards-as-ethical-smart-pointers)**
- **[Cards as Activation Records](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cards-as-activation-records)**

### Persistence Model
- **[Three-Tier Persistence](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#three-tier-persistence)** — Ephemeral / Narrative / State

### Delegation and K-lines
- **[Glossary](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#glossary)** — Instantiate, Persist, Incarnate, Delegate
- **[K-lines](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980)** — Names that wake constellations

### The Empathic Suite
- **[The Empathic Suite](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-empathic-suite)**
- Skills: **[empathic-expressions/](./skills/empathic-expressions/)** | **[empathic-templates/](./skills/empathic-templates/)** | **[postel/](./skills/postel/)** | **[yaml-jazz/](./skills/yaml-jazz/)**

---

## 🧬 The Lineage (This Is Not New — It's an Unbroken Thread)

Full genealogy: **[Appendix A: Intellectual Lineage](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#1-sketchpad-ivan-sutherland-1962)**

| Pioneer | Contribution | MOOLLM Connection |
|---------|--------------|-------------------|
| **[Ivan Sutherland](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#1-sketchpad-ivan-sutherland-1962)** | Sketchpad | Constraints, multiple views |
| **[Douglas Engelbart](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#2-nlsaugment-douglas-engelbart-sri-1968)** | Mother of All Demos | Augmenting intellect |
| **[Alan Kay](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#3-smalltalk-alan-kay-xerox-parc-1970s)** | Smalltalk | Objects, messaging |
| **[Marvin Minsky](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980)** | K-lines, Society of Mind | Names as activation vectors |
| **[Seymour Papert](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#5-constructionism-seymour-papert-1980)** | Logo, Constructionism | Play-Learn-Lift |
| **[John Warnock](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#6-postscript--the-linguistic-motherboard-john-warnock-owen-densmore-1984)** | PostScript | "Linguistic motherboard" |
| **[James Gosling](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#7-news-james-gosling-sun-1986)** | NeWS | Network window system |
| **[Morningstar & Farmer](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#8-habitat-chip-morningstar--randy-farmer-lucasfilm-1986)** | Habitat | First virtual world |
| **[David Ungar](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#9-self-david-ungar--randy-smith-sunstanford-1987)** | Self | Prototypes, delegation |
| **[Bill Atkinson](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#10-hypercard-bill-atkinson-apple-1987)** | HyperCard | Reader = Writer |
| **[Pavel Curtis](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#11-tinymud--lambdamoo-jim-aspnes-pavel-curtis-1989-1990)** | LambdaMOO | User-built rooms |
| **[Arthur van Hoff](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#12-hyperlook-arthur-van-hoff-turing-institute-1989-1992)** | HyperLook | PostScript + HyperCard |
| **[Will Wright](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#13-simcity--the-sims-will-wright-maxis-1989-2000)** | The Sims | Needs, advertisements |
| **[Stewart Butterfield](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#14-game-neverending--glitch-stewart-butterfield-2002-2012)** | Glitch | Social play |

🏛️ **[Hall of MOOLLM Heroes](./examples/adventure-4/characters/real-people/README.md#-hall-of-moollm-heroes)** — Full entries for each pioneer  
💕 **[Love Children Gallery](./examples/adventure-4/characters/real-people/README.md#-love-children-gallery)** — Fictional mashups inheriting from multiple sources

---

## 🗂️ Repo Map (High-Signal Directories)

| Directory | What's There |
|-----------|--------------|
| **[designs/eval/](./designs/eval/)** | EVAL-INCARNATE-FRAMEWORK.md and related docs |
| **[skills/](./skills/)** | ~80 skills — the building blocks |
| **[examples/adventure-4/](./examples/adventure-4/)** | The living world — pub, rooms, characters |
| **[examples/adventure-4/pub/](./examples/adventure-4/pub/)** | The pub (room root) |
| **[examples/adventure-4/characters/](./examples/adventure-4/characters/)** | 🚉 Grand Central Station of Souls |
| **[examples/adventure-4/characters/real-people/](./examples/adventure-4/characters/real-people/)** | 🏛️ Hall of Heroes + 💕 Love Children |
| **[examples/adventure-4/characters/animals/](./examples/adventure-4/characters/animals/)** | 🐾 Animal Sanctuary — Palm, Biscuit, 8 terpene kittens, 8 puppies, Confetti Crawler |

---

## 🎮 Quick Commands

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

(Then go read: **[Speed of Light](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#speed-of-light)**)

---

## 🎞️ Visual Galleries (Slideshows)

The adventure includes **image-based narrative slideshows** — generated, mined, and cross-referenced:

**[📋 Full Slideshow Index](./examples/adventure-4/SLIDESHOW-INDEX.md)** | **[🌀 Master Synthesis](./examples/adventure-4/MASTER-SYNTHESIS-SLIDESHOW.md)**

### Main Narratives (4 Parallel Timelines)

| Timeline | Slideshow | Images | Description |
|----------|-----------|--------|-------------|
| **A** | [The ACME Heist](./examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/acme-heist-footage/SLIDESHOW.md) | 10 | Surveillance footage of the break-in |
| **B** | [Donna's Selfies](./examples/adventure-4/characters/fictional/donna-toadstool/selfies/SLIDESHOW.md) | 11 | The heist from the control room |
| **C** | [Post-Heist Fellowship](./examples/adventure-4/pub/photos/post-heist-fellowship/SLIDESHOW.md) | 4 | Everyone gathers at the pub |
| **D** | [Don's MINE to OURS](./examples/adventure-4/characters/real-people/don-hopkins/selfies/SLIDESHOW.md) | 7 | Transformation → Alliance |

### Character Portraits

| Character | Slideshow | Description |
|-----------|-----------|-------------|
| [Richard Bartle](./examples/adventure-4/characters/real-people/richard-bartle/study/selfies/SLIDESHOW.md) | Selfies from Essex | Study portraits with Heuristic |
| [Palm the Monkey](./examples/adventure-4/pub/stage/palm-nook/study/palm-portrait-session/SLIDESHOW.md) | Portrait Session | Dutch Golden Age tribute |

### Pub Galleries

| Gallery | Description |
|---------|-------------|
| [Don's Pub Photos](./examples/adventure-4/pub/photos/dons-pub-photos-2026-01-19/SLIDESHOW.md) | Facebook-style photo tour |
| [Rocky and Friends](./examples/adventure-4/pub/rooms/room-4/rocky-and-friends/SLIDESHOW.md) | Emotional support boulder |
| [Dusty Attic Art](./examples/adventure-4/pub/attic/dusty-attic-art-styles/SLIDESHOW.md) | Same room in 7 art styles |
| [Telescope Views](./examples/adventure-4/pub/rooftop/telescope-constellation-views/SLIDESHOW.md) | K-Line constellation |

**How they work**: Each slideshow inherits from [skills/slideshow/](./skills/slideshow/). Images are generated via [skills/visualizer/](./skills/visualizer/) and mined via [skills/image-mining/](./skills/image-mining/).

---

## 🤝 Contributing

1. **Play an adventure** — Your session becomes shareable literature  
   → start at **[examples/adventure-4/](./examples/adventure-4/)**

2. **Make a skill** — Clone the meta-skill  
   → **[skills/skill/](./skills/skill/)**

3. **Give it a CARD** — Machine-readable interface and advertisements  
   → **[CARD.yml section](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface)**

4. **Document it** — Every directory deserves a landing page that links outward

5. **PR back** — Improvements welcome, especially link-rich maps and examples

---

## One Mantra (For Your Clipboard)

> **Skills are programs. The LLM is `eval()`. Empathy is the interface.**  
> 📜 **[EVAL-INCARNATE-FRAMEWORK.md](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md)**

🐒🚉✨
