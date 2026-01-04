# MOOLLM Quickstart

**Get playing in 2 minutes** ⏱️

---

## 🚀 Get Started in Cursor

```bash
git clone git@github.com:SimHacker/moollm.git
cd moollm
cursor .
```

**That's it.** Open a chat. Start talking. The repo IS the game.

---

## 🎮 Three Ways to Play

### 1. Play an Adventure

Open [examples/adventure‑3/](./examples/adventure-3/) — it's ready to go!

```
> GET LAMP
> GO WEST
> LOOK
```

The LLM is your Dungeon Master. The filesystem is the world. Chat commands become actions. Files track state.

### 2. Read a Legendary Playthrough

Open [examples/adventure‑2/README.md](./examples/adventure-2/README.md) — the complete transcript of Captain Ashford's epic journey:
- Slew a grue with blue cheese
- Made 8 promises to Mother, kept them all
- Wrote a PhD-level postmodern deconstruction paper
- 100+ generated photos

See how an adventure unfolds. Learn the mechanics. Steal ideas.

### 3. Build Your Own World

Just tell Cursor:

> "Clone examples/adventure-3 to examples/my-run-1, then start it — I wake up and look around."

Or manually:
```bash
cp -r examples/adventure-3 examples/my-adventure
```

**What happens:** You'll see detailed results in chat (sometimes raw YAML), but Cursor also weaves your narrative into the adventure's `README.md` — complete with YAML Jazz commentary, links to artifacts, rooms, items, skill definitions, and image prompts.

**Push to GitHub:** When you add, commit, and push, your adventure's README becomes a beautifully formatted web page on GitHub! Hypertext links let you browse rooms, examine objects, and trace your journey. Your playthrough becomes a shareable, navigable story.

**Don't know git?** Just ask Cursor! *"Add all my changes, write a descriptive commit message, and push to GitHub."* It handles everything — no shell commands to memorize. But watch what it does and learn! **This is constructionist education at its finest.** You're not just playing — you're learning git, YAML, file structures, and LLM patterns by doing.

You can edit the YAML directly in Cursor's text editor — or just tell Cursor what you want:

> "Add a garden room west of the kitchen with a mysterious talking flower."

The LLM creates the files, connects the exits, writes the descriptions. Looking at the files helps you understand how it works — but you don't *have* to touch them.

**K-Lines:** The [PROTOCOLS.yml](./PROTOCOLS.yml) file defines symbolic names — like Wikipedia's policy shortcuts (`WP:NPOV`, `WP:RS`) but for LLM behavior. These are Marvin Minsky's "K-Lines" from *Society of Mind*: names that activate conceptual clusters. Type `YAML-JAZZ` and the LLM interprets comments semantically. Type `SPEED-OF-LIGHT` and it simulates multiple agents in one call. Type `POSTEL` and it interprets your input charitably. UPPER-CASE-DASHED names, greppable cognitive triggers — name-activated behaviors.

---

## 📂 The Three Adventures

| Adventure | Purpose | Status |
|-----------|---------|--------|
| [adventure‑1/](./examples/adventure-1/) | **World Building** — Watch a world emerge from chat prompts. README documents creation. | ✅ Template |
| [adventure‑2/](./examples/adventure-2/) | **Legendary Playthrough** — Full transcript, playing and evolving a world, emergent mechanics, epic moments. | ✅ Completed |
| [adventure‑3/](./examples/adventure-3/) | **Fresh Start** — Rich advanced mechanics, crafting, npcs, clean slate, ready to play. Clone this one! | 🎮 **PLAY ME** |

**The Progression:**
- **adventure‑1** created the world (documented)
- **adventure‑2** played and extended it (transcript)
- **adventure‑3** reset with improvements (template)

**To preserve adventure‑3 as a template:**

Just tell Cursor:
> "Clone adventure-3 to adventure-4, rename my character to 'Captain Starlight', and start me in the kitchen making breakfast."

Or manually:
```bash
cp -r examples/adventure-3 examples/adventure-4
```

---

## 💡 What Makes This Different

| Black Box Agent | MOOLLM |
|-----------------|--------|
| "Trust me, I remember" | Read the YAML — see everything |
| Crashes on missing data | Self-heals, continues |
| Single user, single agent | Many agents talk in ONE LLM call |
| Hidden state | **Everything is files** |
| Text generator | **Coherence Engine** — referee, simulator, DM |

---

## 🗺️ Essential Skills to Explore

| Skill | What It Does | Start Here |
|-------|--------------|------------|
| 🚪 [room/](./skills/room/) | **The star.** Directories as rooms. Objects. Vehicles. Exits. Inventories. | [README](./skills/room/README.md) |
| 🗺️ [adventure/](./skills/adventure/) | Text adventures as CLI architecture. Goals. Discoveries. Choices. | [README](./skills/adventure/README.md) |
| 🏗️ [constructionism/](./skills/constructionism/) | **The philosophy.** Learn by building. Papert. Kay. Logo. Micropolis. | [README](./skills/constructionism/README.md) |
| 🎮 [play‑learn‑lift/](./skills/play-learn-lift/) | The methodology. Play → Learn → Lift. How skills evolve. | [README](./skills/play-learn-lift/README.md) |
| 🃏 [card/](./skills/card/) | Characters, tools, functions as playable cards. | [README](./skills/card/README.md) |
| 💬 [soul‑chat/](./skills/soul-chat/) | Everything speaks — objects, rooms, concepts. | [README](./skills/soul-chat/README.md) |
| 🎷 [yaml‑jazz/](./skills/yaml-jazz/) | Comments carry meaning. LLMs interpret, not just parse. | [README](./skills/yaml-jazz/README.md) |

---

## 🏰 What's In an Adventure?

```
examples/adventure-3/
├── README.md           # The story so far (and play log)
├── MECHANICS.yml       # Game systems: scoring, skills, curses
├── player.yml          # Your character state
├── start/              # Chamber of Commencement
│   ├── ROOM.yml        # Room definition
│   ├── lamp.yml        # GET LAMP!
│   └── mailbox.yml     # Zorkian tradition
├── kitchen/            # Mother's kitchen
│   ├── mothers-note.yml    # ⭐ MOST IMPORTANT — read it, reply!
│   ├── fridge.yml          # 20 foods for maze mapping
│   ├── tomtomagotchi.yml   # Navigation pet
│   └── counter.yml         # Crafting system
├── coatroom/           # Costume room — be anyone!
├── maze/               # 10 dark rooms, grue danger
├── pub/                # Social hub — games, rumors, themes
├── home/               # Mother waits here
└── end/                # Treasury — the goal!
```

**Key insight:** Directories are rooms. Files are objects. The hierarchy IS the world.

---

## 🎯 Your First Session

1. **Open adventure‑3 in Cursor**
2. **Chat:** "I wake up. LOOK. GO WEST. READ NOTE."
3. **Compose your reply to Mother** — your promises become your goals, kickstarting world generation!
4. **Explore:** GO NORTH, LOOK, EXAMINE things
5. **Write back to Mother** — your promises become your goals!

The LLM tracks state in the YAML files. Look at `player.yml` to see your inventory, gold, and location update.

---

## 🧠 Core Concepts (60 seconds)

| Concept | What It Means |
|---------|---------------|
| **FILES-AS-STATE** | No hidden memory. Everything in files you can read. |
| **YAML-JAZZ** | Comments carry meaning. `timeout: 30 # API flaky Mondays` |
| **ROOMS** | Directories are places. Enter = navigate. Objects inside. |
| **CARDS** | Characters/tools as templates. Play them in rooms. |
| **SPEED-OF-LIGHT** | Many agents simulate in ONE LLM call. No round trips. |
| **POSTEL** | Be liberal in input. Interpret charitably. Never crash. |
| **PLAY-LEARN-LIFT** | Explore → find patterns → crystallize into skills. |

---

## 📜 Protocol Symbols (K-Lines)

Type these as commands or mention them to activate behaviors:

```
YAML-JAZZ        # Interpret comments semantically
POSTEL           # Interpret charitably, never crash
PLAY-LEARN-LIFT  # Start exploring, find patterns
SOUL-CHAT        # Give an object/room a voice
ENTER-ROOM       # Navigate to a directory context
SPEED-OF-LIGHT   # Simulate many agents at once
```

Full index: [PROTOCOLS.yml](./PROTOCOLS.yml)

---

## 🔧 Extending Adventures

### Add a Room

```bash
mkdir examples/adventure-3/garden
```

Create `ROOM.yml`:
```yaml
room:
  name: The Hidden Garden
  description: |
    Overgrown with strange flowers that seem to whisper.
  exits:
    south:
      destination: ../kitchen/
      description: "Back to the kitchen"
  objects:
    - mysterious-flower.yml
```

### Add an Object

Create `mysterious-flower.yml`:
```yaml
object:
  name: Mysterious Flower
  portable: true
  description: |
    It pulses with an inner light. Smells like... memories?
  actions:
    SMELL:
      effect: "You remember something you forgot long ago..."
    PICK:
      effect: "It comes away easily. The garden sighs."
```

### Connect It

Edit `kitchen/ROOM.yml` to add an exit:
```yaml
exits:
  north:
    destination: ../garden/
    description: "A hidden door behind the fridge"
```

**Done.** The LLM will find it. The world grows.

---

## 🎪 The Bigger Picture

MOOLLM is **constructionist computing for LLMs**:

- **Papert & Kay** — Learning by building inspectable things
- **The Sims** — Objects advertise, agents select autonomously
- **HyperCard** — Non-programmers building interactive systems
- **MUD/LambdaMOO** — Rooms, objects, verbs, spatial programming
- **Zork/Adventure** — Text adventures as the original CLI

> *"If you can build it, you can understand it. If you can inspect it, you can trust it."*

---

## 📚 Next Steps

| Goal | Read This |
|------|-----------|
| Understand the vision | [README.md](./README.md) |
| Deep dive on rooms | [skills/room/](./skills/room/) |
| Learn the methodology | [skills/play‑learn‑lift/](./skills/play-learn-lift/) |
| Understand skills | [skills/skill/](./skills/skill/) |
| See all protocols | [PROTOCOLS.yml](./PROTOCOLS.yml) |
| Explore the kernel | [kernel/README.md](./kernel/README.md) |

---

## 🎮 The Mantra

> *The LLM is the Coherence Engine.*
> *The filesystem is the world.*
> *The chat is the adventure.*

**Now go GET LAMP!** 🪔
