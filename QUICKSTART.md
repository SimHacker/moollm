# MOOLLM Quickstart

**Get playing in 2 minutes** ⏱️

---

## 👀 Browse First

Explore on GitHub — no install needed:

| Start Here | What You'll Find |
|------------|------------------|
| 🔥 [examples/adventure-4/](./examples/adventure-4/) | The richest microworld — pub, NPCs, Palm the monkey |
| 🧠 [skills/](./skills/) | ~80 skills — all the building blocks |
| 📜 [designs/eval/EVAL-INCARNATE-FRAMEWORK.md](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md) | The deep dive |

Every directory has a README. Every YAML is literate and commented.

---

## 🚀 Install & Run

```bash
git clone git@github.com:SimHacker/moollm.git
cd moollm
cursor .
```

Or ask Cursor: *"Clone https://github.com/SimHacker/moollm.git and open it"*

**That's it.** Open a chat. The repo IS the game.

---

## 🎮 Play

```
> LOOK
> GO WEST
> READ NOTE
> GET LAMP
```

The LLM is your Dungeon Master. Directories are rooms. Files are objects.

---

## 🏗️ Build

Tell Cursor what you want:

> "Clone adventure-4 to my-adventure-1, start me in the pub."

> "Add a garden west of the kitchen with a talking flower."

Or copy manually and edit the YAML directly.

---

## 📚 Learn from Sessions

| Session | Highlights |
|---------|------------|
| [marathon-session.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) | Palm's incarnation, 33-turn Fluxx |
| [k-line-connections.md](./examples/adventure-4/characters/real-people/don-hopkins/sessions/k-line-connections.md) | K-line safari with conceptual pioneers |

These are collaborative literature — see mechanics in action.

---

## 🗂️ What's In adventure-4?

```
examples/adventure-4/
├── characters/         # Players, NPCs, animals
├── sessions/           # Play logs (shareable literature)
├── start/              # Beginning room with lamp
├── kitchen/            # Mother's note → your goals!
├── pub/                # Social hub — games, NPCs, stage
├── maze/               # 10 dark rooms, grues
└── end/                # Treasury — the goal!
```

> 📚 Full structure: [examples/adventure-4/README.md](./examples/adventure-4/)

---

## 🧠 Core Concepts

| Concept | Meaning |
|---------|---------|
| **FILES-AS-STATE** | No hidden memory — everything in files |
| **YAML-JAZZ** | Comments carry semantic meaning |
| **ROOMS** | Directories are places |
| **K-LINES** | Names that activate conceptual clusters |
| **SPEED-OF-LIGHT** | Many agents in one LLM call |
| **POSTEL** | Interpret charitably, never crash |

> 📚 Full protocol list: [PROTOCOLS.yml](./PROTOCOLS.yml)

---

## 🔧 Quick Recipes

### Add a Room

```yaml
# examples/adventure-4/garden/ROOM.yml
room:
  name: The Hidden Garden
  exits:
    south:
      destination: ../kitchen/
```

### Add an Object

```yaml
# examples/adventure-4/garden/flower.yml
object:
  name: Mysterious Flower
  portable: true
  actions:
    SMELL: "You remember something you forgot..."
```

> 📚 Full guide: [skills/room/](./skills/room/)

---

## 📚 Next Steps

| Goal | Read This |
|------|-----------|
| Understand the vision | [README.md](./README.md) |
| Deep architecture dive | [EVAL-INCARNATE-FRAMEWORK.md](./designs/eval/EVAL-INCARNATE-FRAMEWORK.md) |
| All skills | [skills/](./skills/) |
| All protocols | [PROTOCOLS.yml](./PROTOCOLS.yml) |

---

> *The LLM is the Coherence Engine. The filesystem is the world. The chat is the adventure.*

**Now go GET LAMP!** 🪔
