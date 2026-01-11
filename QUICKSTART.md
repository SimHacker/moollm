# MOOLLM Quickstart

**Get playing in 2 minutes** ⏱️

---

## 👀 Browse First (Zero Commitment)

Just explore the repo on GitHub — no install needed!

| Browse This | What You'll See |
|-------------|-----------------|
| [examples/adventure-4/](./examples/adventure-4/) | 🔥 **Start here!** The richest microworld — pub, NPCs, incarnation, Palm the monkey |
| [skills/](./skills/) | All the building blocks — rooms, cards, adventures |
| [kernel/](./kernel/) | The operating system layer — constitution, protocols |
| [PROTOCOLS.yml](./PROTOCOLS.yml) | K-Lines — Wikipedia-style behavior triggers |
| [README.md](./README.md) | The full vision and lineage |

Every directory has a `README.md` that GitHub renders beautifully. Click around. Read the YAML files — they're literate, commented, designed to be understood. **This is markup and data as literature.**

---

## 🚀 Ready to Play? Get Started in Cursor

```bash
git clone git@github.com:SimHacker/moollm.git
cd moollm
cursor .
```

Or just open Cursor and ask:

> "Clone https://github.com/SimHacker/moollm.git and open it"

**That's it.** Open a chat. Start talking. The repo IS the game.

---

## 🎮 Three Ways to Play

### 1. Play an Adventure

Open [examples/adventure‑4/](./examples/adventure-4/) — the richest world with the most features!

```
> LOOK
> GET LAMP
> GO WEST
> READ LETTER
```

The LLM is your Dungeon Master. The filesystem is the world. Chat commands become actions. Files track state.

### 2. Read Epic Session Logs

See how adventures unfold in practice:

| Session | What Happens |
|---------|--------------|
| [marathon-session.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) | 🎮 Don's epic run: Palm's incarnation, 33-turn Fluxx, speed-of-light proven |
| [k-line-connections.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md) | 🔗 K-line safari with Minsky, Nelson, Burke, Kay, Wright, and more |

These aren't transcripts — they're **collaborative literature**. Learn the mechanics. Steal ideas.

### 3. Build Your Own World

Just tell Cursor:

> "Clone examples/adventure-4 to examples/my-run-1, then start it — I wake up and look around."

Or manually:
```bash
cp -r examples/adventure-4 examples/my-adventure
```

**What happens:** You'll see detailed results in chat (sometimes raw YAML), but Cursor also weaves your narrative into the adventure's `README.md` — complete with YAML Jazz commentary, links to artifacts, rooms, items, skill definitions, and image prompts.

**Fork & branch first:** Ask Cursor to fork the repo and create your own branch — now you have your own copy to experiment with freely.

**Add, commit, push:** When you save your work to GitHub, your adventure's README.md becomes a beautifully formatted web page! Hypertext links let you browse rooms, examine objects, and trace your journey. Your playthrough becomes a shareable, navigable story.

**Make PRs:** Developed a cool skill, mechanic, or adventure? Ask Cursor to make a pull request to share your improvements with the community!

**Don't know git?** Just ask Cursor! *"Fork this repo, create a branch called my-adventure, add my changes, commit, and push."* It handles everything — no shell commands to memorize. But watch what it does and learn! **This is constructionist education at its finest.** You're not just playing — you're learning git, YAML, file structures, and LLM patterns by doing.

You can create and edit the YAML directly in Cursor's text editor — or just tell Cursor what you want:

> "Add a garden room west of the kitchen with a mysterious talking flower."

The LLM creates the files, connects the exits, writes the descriptions. Looking at the files helps you understand how it works — but you don't *have* to touch them.

**K-Lines:** The [PROTOCOLS.yml](./PROTOCOLS.yml) file defines symbolic names — like Wikipedia's policy shortcuts (`WP:NPOV`, `WP:RS`) but for LLM behavior. These are Marvin Minsky's "K-Lines" from *Society of Mind*: names that activate conceptual clusters. Type `YAML-JAZZ` and the LLM interprets comments semantically. Type `SPEED-OF-LIGHT` and it simulates multiple agents in one call. Type `POSTEL` and it interprets your input charitably. UPPER-CASE-DASHED names, greppable cognitive triggers — name-activated behaviors.

---

## 📂 Adventure-4: The Recommended Starting Point

| Adventure | What It Is |
|-----------|------------|
| 🔥 **[adventure‑4/](./examples/adventure-4/)** | **START HERE.** The richest world: pub with NPCs, incarnation protocol, character directories, session logs, Palm the monkey. All features demonstrated. |

### The Prototypes That Led Here

Adventure-4 evolved through three earlier iterations:

| Prototype | What It Contributed |
|-----------|---------------------|
| [adventure‑1/](./examples/adventure-1/) | 🌱 **The Seed** — Minimal starting structure. 10 maze rooms. The foundation. |
| [adventure‑2/](./examples/adventure-2/) | 🏆 **Captain Ashford's Run** — First full playthrough. Proved the mechanics work. Slew a grue with blue cheese. |
| [adventure‑3/](./examples/adventure-3/) | 🎮 **Rich Template** — Added pub, NPCs, crafting. Reset for fresh exploration. |

**Adventure-4 inherits everything from 1-2-3** and adds: incarnation protocol, character directories, Speed of Light simulation, session logs, Palm's essays, K-line navigation. It's the current "gold standard."

**To start fresh:**

```bash
cp -r examples/adventure-4 examples/my-adventure
```

Or ask Cursor: *"Clone adventure-4 to my-adventure-1, rename my character to 'Captain Starlight', and start me in the pub."*

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
examples/adventure-4/
├── README.md           # The story so far (and play log)
├── characters/         # Player & NPC character directories
│   ├── real-people/    # Real people (ethical framing)
│   ├── fictional/      # Fictional characters
│   └── animals/        # Animal characters (Palm, Biscuit, Terpie)
├── sessions/           # Session logs (collaborative literature!)
├── start/              # Chamber of Commencement
│   ├── ROOM.yml        # Room definition
│   ├── lamp.yml        # GET LAMP!
│   └── mailbox.yml     # Zorkian tradition
├── kitchen/            # Mother's kitchen
│   ├── mothers-note.yml    # ⭐ Read it, reply — your promises become goals!
│   ├── fridge.yml          # 20 foods for maze mapping
│   └── counter.yml         # Crafting system
├── coatroom/           # Costume room — be anyone!
├── maze/               # 10 dark rooms, grue danger
├── pub/                # 🔥 Social hub — games, stage, NPCs, themes
│   ├── stage/          # Performance space, Palm's nook
│   └── bar/            # Bartender Marieke, budtender George
├── home/               # Mother waits here
└── end/                # Treasury — the goal!
```

**Key insight:** Directories are rooms. Files are objects. The hierarchy IS the world.

---

## 🎯 Your First Session

1. **Open adventure‑4 in Cursor**
2. **Chat:** "I wake up. LOOK. GO WEST. READ NOTE."
3. **Compose your reply to Mother** — your promises become your goals!
4. **Explore:** GO NORTH, LOOK, EXAMINE, TAKE things
5. **Visit the pub** — meet Marieke the bartender, George the budtender, play Fluxx!

The LLM tracks state in the YAML files. Look at character files to see inventory, gold, and location update.

---

## 🧠 Core Concepts (60 seconds)

| Concept | What It Means |
|---------|---------------|
| [**FILES-AS-STATE**](./PROTOCOLS.yml) | No hidden memory. Everything in files you can read. |
| [**YAML-JAZZ**](./skills/yaml-jazz/) | Comments carry meaning. `timeout: 30 # API flaky Mondays` |
| [**ROOMS**](./skills/room/) | Directories are places. Enter = navigate. Objects inside. |
| [**CARDS**](./skills/card/) | Characters/tools as templates. Play them in rooms. |
| [**SPEED-OF-LIGHT**](./skills/speed-of-light/) | Many agents simulate in ONE LLM call. No round trips. |
| [**POSTEL**](./skills/postel/) | Be liberal in input. Interpret charitably. Never crash. |
| [**PLAY-LEARN-LIFT**](./skills/play-learn-lift/) | Explore → find patterns → crystallize into skills. |

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
mkdir examples/adventure-4/garden
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
