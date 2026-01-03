# 🎮 Adventure 3: A New Hero Awakens

> *The paint is dry on adventure-2. The world has been shaped by legend.*  
> *Now it's YOUR turn.*

---

## 🌍 The World State

This adventure inherits the **enriched world** from adventure-2, where Bumblewick Fantastipants became Captain Ashford and slew a grue with blue cheese.

### What's Preserved (World Improvements)

| Feature | Description | Location |
|---------|-------------|----------|
| 🏛️ **Initials on the Wall** | WC+DW '76, SA '78, CA '26, BF — the lineage | `start/ROOM.yml` |
| ⬆️ **Stairway to Home** | Exit UP leads to the surface | `start/` → `home/` |
| 🎭 **Maurice's Skills** | Learned PHOTO-SET-8 in adventure-2 | `coatroom/mannequin.yml` |
| 🏪 **Vending Machine** | Sells Premium Glow Juice | `maze/room-j/lamp-vendor.yml` |
| 💀 **The Skeleton** | Still points west, still waiting | `maze/room-i/ROOM.yml` |
| 💰 **100 Gold Pile** | In the grue's lair | `maze/room-f/gold-pile.yml` |
| 📖 **Legends** | Tales of the Grue Slayer | Throughout |

### What's Reset (Fresh Start)

| Feature | State | Notes |
|---------|-------|-------|
| 🧑 **Player** | New unknown hero | Identity to be discovered |
| 🪔 **Lamp** | Full (100 oil) | On the shelf, waiting |
| 🧊 **Fridge** | Fully restocked | 20 food items |
| 📓 **Notebook** | Empty | Your story awaits |
| 🍱 **Lunchbox** | Empty | In the kitchen |
| 💰 **Starting Gold** | 10 | Enough for lamp refills |
| 🐉 **The Grue** | RESPAWNED | Grues always respawn |
| 🗺️ **Maze Markers** | Cleared | Map it yourself! |

---

## 🎯 Your Goals

From Mother's note on the kitchen table:

1. **Find treasure** (+10 points)
2. **Bring gold home** (Mother's approval)
3. **Return home safely** (Adventure complete!)

*Plus eight promises to keep... but you'll find those yourself.*

---

## 🗺️ The World

```
                              HOME
                               ↑ up
                               │
    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
    │                    ╔═════╧═════╗                    │
    │                    ║   START   ║                    │
    │                    ║  Chamber  ║                    │
    │                    ╚═════╤═════╝                    │
    │                          │                          │
    │    COATROOM ←── east ────┼──── west ──→ KITCHEN    │
    │    (Maurice)             │              (Fridge)    │
    │                          │ north                    │
    │                          ↓                          │
    │                    ╔═══════════╗                    │
    │                    ║   MAZE    ║                    │
    │                    ║ 10 rooms  ║                    │
    │                    ║  (DARK!)  ║                    │
    │                    ╚═════╤═════╝                    │
    │                          │                          │
    │                          ↓                          │
    │                    ╔═══════════╗                    │
    │                    ║  TREASURY ║                    │
    │                    ║ (treasure)║                    │
    │                    ╚═══════════╝                    │
    │                                                     │
    └─────────────────────────────────────────────────────┘
```

---

## 🎬 Begin Your Adventure

**Move 0: Awakening**

You stir. The Chamber of Commencement. Carved initials on the walls tell of those who came before. A brass lamp waits on a shelf.

> `GET LAMP`

*Your story begins...*

---

## 📜 Chat Log

*This space will fill with your adventure as you play.*

---

### Move 1: ???

**User:** `[your first command]`

**DM:** *[what happens...]*

---

## 📊 Current State

```yaml
player:
  name: "Unknown Hero"
  location: start/
  moves: 0
  score: 0
  gold: 10
  
inventory: []
  # GET LAMP!
  
goals:
  - Find treasure: PENDING
  - Bring gold home: PENDING  
  - Return home safely: PENDING
```

---

## 🧬 Lineage

| Adventure | Hero | Achievement |
|-----------|------|-------------|
| 1 | *(template)* | World created |
| 2 | **Captain Ashford** (Bumblewick) | Slew grue with cheese, 8/8 promises, PhD paper |
| 3 | **???** | *Your story here* |

---

## 🎭 Tips for New Adventurers

1. **GET LAMP** — Seriously. Don't enter the maze without it.
2. **Visit the Kitchen** — Mother's note has important instructions.
3. **Visit the Coatroom** — Maurice can help you discover who you want to be.
4. **Raid the Fridge** — 20 food items for maze mapping.
5. **The Grue Has Respawned** — It's hungry. It's waiting. It's in room-f.
6. **The Vending Machine** — Room J sells Premium Glow Juice (3 gold).
7. **The Skeleton Points West** — Follow its guidance.
8. **There's 100 Gold** — In the grue's lair. If you dare.

---

## 🧪 Emergent Mechanics (from adventure-2)

*Patterns discovered through play. Use as inspiration!*

| Mechanic | What Happens | See |
|----------|--------------|-----|
| 👃 **Smell Gradients** | Transformed food emits smells that diffuse through rooms | [maze/README.md](./maze/README.md) |
| 🔮 **Object Transformation** | Eaten food becomes sentient, prophetic, weaponized... | [kitchen/fridge.yml](./kitchen/fridge.yml) |
| 🐉 **Grue Personality** | The grue can speak, bargain, fight, be eaten | [maze/room-f/](./maze/room-f/) |
| 💀 **Skeleton Stories** | The skeleton accepts gifts, memorials, visitors | [maze/room-i/](./maze/room-i/) |
| ⚡ **Speed of Light** | DM simulates multiple moves seamlessly | [maze/README.md](./maze/README.md) |
| 🎭 **Identity Play** | Costumes affect transformations and interactions | [coatroom/](./coatroom/) |

**DM Principle:** These are EXAMPLES that suggest possibilities. Defer creativity until runtime. Improvise. Surprise yourself!

---

## 📚 References

- [adventure-2/README.md](../adventure-2/README.md) — The legend of Captain Ashford
- [coatroom/mannequin.yml](./coatroom/mannequin.yml) — Maurice and PHOTO-SET-8
- [kitchen/fridge.yml](./kitchen/fridge.yml) — The EAT mechanic
- [maze/room-f/](./maze/room-f/) — The grue's lair
- [maze/room-j/lamp-vendor.yml](./maze/room-j/lamp-vendor.yml) — Premium upgrades

---

*Adventure 3 forked from adventure-2 on January 4, 2026*

*The world remembers. The grue waits. What will YOU do?*
