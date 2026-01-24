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

### 3) 🎴 NEW: Amsterdam Fluxx Championship
🏆 **[skills/experiment/experiments/fluxx-chaos/](./skills/experiment/experiments/fluxx-chaos/)** — 4 characters, 5 tournaments, 20+ games, 116+ turns, 464+ character-turns of emergent narrative gameplay. Up to 30 turns × 4 characters per LLM iteration — proving Speed of Light drive works even with complex changing rules and social dynamics! 24 generated cards, 32 AI-generated artworks, research-grade analysis.

### 4) Get moving fast
📖 **[QUICKSTART.md](./QUICKSTART.md)** — "get playing in 2 minutes"

### 5) Browse the skill library
🧠 **[skills/](./skills/)** — ~80 skills, the building blocks  
Start at: **[skills/README.md](./skills/README.md)**

### 6) Meet the giants
🏛️ **[Hall of MOOLLM Heroes](./examples/adventure-4/characters/real-people/README.md#-hall-of-moollm-heroes)** — The people who made this possible

### 7) Meet the animals
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

---

## 🎴 MAJOR ATTRACTION: Amsterdam Fluxx Championship

**[📊 View Full Analysis →](./skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/SCORE.md)**

A 4-hour LLM session that produced:
- **5 tournaments, 20+ games, 116+ turns** of emergent narrative gameplay
- **24 dynamically generated cards** forged from character stories
- **32 pieces of AI-generated card artwork**
- **Emergent mechanics** — FAFO Token Paradox, Silent Victory Protocol, Melodramatic Loophole
- **Research-grade scoring** — rubrics, Harper numbers, card signatures

| Quick Stat | Value |
|------------|-------|
| Cookie mentions | **271** |
| Love card signatures | **10** |
| Most signed quote | *"I had to let you go."* |
| Bumblewick's 0-8 → Champion | **The Long Shot** |

### 🎨 The Card Gallery

**[📖 View Slideshow →](./skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/artwork/SLIDESHOW.md)**

32 cards with stereo-prompt artwork generation. Each card mined with computer vision.

### 🃏 Dynamic Card Generation

**[📖 View Generated Cards →](./skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/generated-cards.yml)**

24 personal cards created during gameplay:
- **Donna's Melodramatic Wail** — Discovered a loophole in the FAFO Token
- **Bumblewick's Long Shot Echo** — His triumph card... that fizzled when he needed it
- **Don's Cookie Insurance** — Never triggered (irony: MAXIMUM)
- **FAFO Token** — Creeper that blocks winning, signed by all four players

### 🎭 Post-Tournament Roundtable

The characters talk amongst themselves about the game. **[Read the conversation →](./skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/SCORE.md#part-10-post-tournament-roundtable)**

---

## 🎞️ Visual Galleries (Narrative Slideshows)

The adventure includes extensive image-based narrative slideshows — generated, mined, and cross-referenced to maintain high-fidelity continuity across parallel timelines.

**[📋 Full Slideshow Index](./examples/adventure-4/SLIDESHOW-INDEX.md)** | **[🌀 Master Synthesis](./examples/adventure-4/MASTER-SYNTHESIS-SLIDESHOW.md)** | **[🎴 Fluxx Cards](./skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/artwork/SLIDESHOW.md)**

### 🎭 The Main Narrative Arc
*   **[The ACME Heist](./examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/acme-heist-footage/SLIDESHOW.md)** (10 Images)
    *   *Surveillance footage from the Leela Cam (ACM1).* A frame-by-frame chronicle of the ill-fated break-in at ACME Surplus. Captures the approach, the failed entry attempts, the cartoon physics backfires, and the chaotic extraction.
*   **[Donna's Surveillance Selfies](./examples/adventure-4/characters/fictional/donna-toadstool/selfies/SLIDESHOW.md)** (11 Images)
    *   *The Heist from the Inside.* Parallel to the ACME Heist, Donna Toadstool documents her "Quality Control" activities from her high-tech control room. Includes her reactions to the intruders, lever-pulling moments, and the "This is Fine" aftermath.
*   **[Post-Heist Fellowship](./examples/adventure-4/pub/photos/post-heist-fellowship/SLIDESHOW.md)** (4 Images)
    *   *Reconciliation at the Grotto.* After the heist disaster, all characters — including Don, Richard, and Donna — gather at the Gezelligheid Grotto to share drinks, lick wounds, and begin the transition from nemesis to partner.
*   **[Don's MINE to OURS](./examples/adventure-4/characters/real-people/don-hopkins/selfies/SLIDESHOW.md)** (7 Images)
    *   *Transformation and Alliance.* The visual arc of Don Hopkins' journey: from claiming his rabbit transformation to the "Treasure Swim" in the Vault of All Value, culminating in the historic "OURS Accord" with Donna Toadstool.

### 🏠 Portable Sanctuaries & Landings
*   **[Study Arrival Footage](./examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/study-arrival-footage/SLIDESHOW.md)** (8 Images)
    *   *First Contact with Mobile Rooms.* LOB1 captures the historic moment Richard Bartle's Study materializes in the Leela lobby. Features the "Sims Cutaway" effect, the arrival of the FMC Motorcoach, and the pioneers beckoning from their respective shells.
*   **[The Great Picnic](./examples/adventure-4/forest/meadow/picnic-footage/SLIDESHOW.md)** (21 Images)
    *   *An Atmospheric Expedition.* A massive 21-frame saga documenting the journey to the Forest Meadow. Highlights include the discovery of "Pie-Menu Flowers," the arrival of the "Lift Queens" (Dolly and Lolly), a voracious feast, an ACME truck ambush, and a tornado-fueled return to origin.

### 👤 Character & Location Galleries
*   **[Richard Bartle: Essex Study](./examples/adventure-4/characters/real-people/richard-bartle/study/selfies/SLIDESHOW.md)** (8 Images) — Portraits with Heuristic the dragon.
*   **[Palm the Monkey: Portrait Session](./examples/adventure-4/pub/stage/palm-nook/study/palm-portrait-session/SLIDESHOW.md)** (1 Image) — Dutch Golden Age tribute.
*   **[Rocky and Friends](./examples/adventure-4/pub/rooms/room-4/rocky-and-friends/SLIDESHOW.md)** (8+ Images) — Emotional support boulders.
*   **[Dusty Attic Art Styles](./examples/adventure-4/pub/attic/dusty-attic-art-styles/SLIDESHOW.md)** (7 Images) — Multi-style experiments.
*   **[Telescope & Constellation Views](./examples/adventure-4/pub/rooftop/telescope-constellation-views/SLIDESHOW.md)** (2 Images) — Mapping the K-Lines.
*   **[ACME Tunnel Temporal Views](./examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/acme-tunnel-temporal-views/SLIDESHOW.md)** (4 Images) — Deceptive perspectives.

**How they work** — An iterative pipeline maintaining narrative coherence:

1. **YAML Jazz skeleton** — Define the scene's narrative context, characters, objects
2. **Prompt synthesis** — Assemble rich visual prompt from environment + history
3. **Image generation** — [skills/visualizer/](./skills/visualizer/) renders the scene (Imagen, DALL-E, etc.)
4. **Image mining** — [skills/image-mining/](./skills/image-mining/) extracts semantic treasure from the result
5. **YES AND** — Accept emergent elements as canon (self-captioning, unexpected details)
6. **Iterate** — Each new image sees the FULL context of all previous images + mining results

The coherence engine: Visual consistency across 40+ images (Don's tie-dye, Donna's pink glasses, tunnel evolution) emerges from carrying forward the mined context. Frame-to-frame links allow ping-pong navigation between parallel timelines.

Each slideshow inherits from [skills/slideshow/](./skills/slideshow/).

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
