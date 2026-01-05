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
| 🍺 **The Rusty Lantern** | Themeable pub south of start — games, rumors, secrets | `pub/` |
| 🎭 **Maurice's Skills** | Learned PHOTO-SET-8 in adventure-2 | `coatroom/mannequin.yml` |
| 🏪 **Vending Machine** | Sells Premium Glow Juice | `maze/room-j/lamp-vendor.yml` |
| 💀 **The Skeleton** | Still points west, still waiting | `maze/room-i/ROOM.yml` |
| 💰 **100 Gold Pile** | In the grue's lair | `maze/room-f/gold-pile.yml` |
| 📖 **Legends** | Tales of the Grue Slayer | Throughout |

### What's Reset (Fresh Start)

| Feature | State | Notes |
|---------|-------|-------|
| 🧑 **Player** | New unknown hero | [characters/](./characters/) — rename in coatroom! |
| 🪔 **Lamp** | Full (100 oil) | On the shelf, waiting |
| 🧊 **Fridge** | Fully restocked | 20 food items |
| 📓 **Notebook** | Empty | Your story awaits |
| 🍱 **Lunchbox** | Empty | In the kitchen |
| 💰 **Starting Gold** | 10 (+25 in drawer = 35) | Enough for lamp refills & ACME shopping! |
| 🐉 **The Grue** | RESPAWNED | Grues always respawn |
| 🗺️ **Maze Markers** | Cleared | Map it yourself! |

---

## 👥 Multi-Player Support

This adventure supports **multiple simultaneous players**!

See [ADVENTURE.yml](./ADVENTURE.yml) for per-adventure simulation state:
- **Active players:** Who's currently playing (any number!)
- **Chat target:** Who the chat is addressed to
- **Simulation state:** Global flags, turn number, events

**Quick commands:**

| Command | Effect |
|---------|--------|
| `@don-hopkins Look around` | Direct to specific player |
| `ADDRESS don-hopkins` | Switch default target |
| `PLAYERS` | List all active players |
| `ACTIVATE hero.yml` | Add player to active list |

Multiple players can be in different rooms, carry separate inventories, pursue different goals — but share the same world. See [characters/README.md](./characters/README.md) for details.

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
    │                          │                          │
    │                    ║  TREASURY ║                    │
    │                    ║ (treasure)║                    │
    │                          │                          │
    │                    ║   MAZE    ║                    │
    │                    ║ 10 rooms  ║                    │
    │                    ║  (DARK!)  ║                    │
    │                          │ north                    │
    │                          ↓                          │
    │    KITCHEN ←─west──║   START   ║──east─→ COATROOM   │
    │    (Fridge)        ║  Chamber  ║        (Maurice)   │
    │                          │ south                    │
    │                          ↓                          │
    │                    ║    PUB    ║                    │
    │                    ║  Rusty    ║                    │
    │                    ║ Lantern   ║                    │
    │                                                     │
```

---

## 🎬 Begin Your Adventure

**Move 0: Awakening**

You stir. The Chamber of Commencement. Carved initials on the walls tell of those who came before. A brass lamp waits on a shelf.

> `GET LAMP`

*Your story begins...*

---

## 📜 Session Log

| File | Purpose |
|------|---------|
| **[LOG.md](./LOG.md)** | Summary table — turns, locations, files changed |
| **[TRANSCRIPT.md](./TRANSCRIPT.md)** | Pure narration — story, YAML objects, mermaid diagrams |

The LOG is for quick reference. The TRANSCRIPT is for reading (and interactive web rendering).

---

## 🧬 Lineage

| Adventure | Hero | Achievement |
|-----------|------|-------------|
| 1 | *(template)* | World created |
| 2 | **Captain Ashford** (Bumblewick) | Slew grue with cheese, 8/8 promises, PhD paper |
| 3 | **???** | *Your story here* |

---

## 🎭 Tips for New Adventurers

1. **GET LAMP** — In the start room. Don't enter the maze without it.

2. **Check Your Mail** — The Grand Mailbox is right here in the start room!
   - 📬 The flag is UP. You have mail waiting.
   - 📜 Welcome leaflet, matchbooks, and... something from Mother?
   
3. **Visit the Kitchen** — Everything you need is on the table:
   - 📜 **Mother's Note** — MOST IMPORTANT! Read it. Write back.
   - 🧭 **TomTomagotchi** — Your navigation pet (GPS + friend!)
   - 📓 **Notebook** — For collecting memories (auto-sorts!)
   - 🍱 **Lunchbox** — For carrying food

4. **⭐ READ THE NOTE. WRITE A REPLY. MAKE PROMISES!** ⭐
   
   > *This is the most important step for a rich adventure!*
   
   Mother's note asks you to be careful. **Write back to her!**
   - Who are you today? What costume will you wear?
   - What do you promise to bring home?
   - What do you promise NOT to do?
   
   **Your promises become YOUR GOALS.** The DM tracks them.

5. **Raid the Fridge** — 20 food items for maze mapping.
6. **Visit the Coatroom** — Maurice can help you discover who you want to be.
7. **Stop by the Pub** — South of start. Meet NPCs. Play games. Hear rumors.
8. **The Grue Has Respawned** — It's hungry. It's waiting. It's in room-f.
9. **The Vending Machine** — Room J sells Premium Glow Juice (3 gold).
10. **The Skeleton Points West** — Follow its guidance.
11. **There's 100 Gold** — In the grue's lair. If you dare.

---

## 🔮 Hidden Depths

*The dungeon has... evolved.*

**Scoring** isn't what you think. Points aren't fixed — they're *calculated* based on style, difficulty, and creativity.

**Skills** emerge from play. Do something creative? It might become a technique you can use again.

**Curses** are earned. Break a promise? There are... consequences.

**The world grows.** Ask the right questions and new places materialize.

**Companions** are possible. Ask Mother about family. Recruit NPCs. Build a party.

*For the full systems, see [skills/](../../skills/).*

---

## ✨ What's New in Adventure 3

### 🔧 The Workbench

The kitchen counter is more than meets the eye. Mother always said it "tingled."

**What can you do there?**
- **COMBINE** things to make new things
- **TRANSFORM** things into different things  
- **EDIT** things to change their properties
- **PROGRAM** things to do things when other things happen
- And something else... something that goes *deeper*...

### 📦 Mail-Order... Something

There's a catalog on the counter. Dog-eared. The coyote on the cover looks optimistic.

> *"ORDER ANYTHING! DELIVERED IN 2-4 TURNS!"*
> *"Satisfaction Guaranteed!*"*

The asterisk leads to very small print.

### 🍺 The Pub — THE RUSTY LANTERN

**The social hub of the adventure.** South of the Chamber, a timeless tavern awaits.

Inspired by **Bar Karma** (Will Wright & Don Hopkins).

**The Rusty Lantern** changes based on your expectations:
- Think of a space cantina → Z-4RT polishes glasses under neon
- Think of an Amsterdam coffeeshop → Marieke serves koffie verkeerd
- Or describe ANY theme you want...

**What's inside:**

| Object | What It Does |
|--------|--------------|
| 🧑‍🍳 **Bartender** | Ancient, mysterious, knows everything (for a price) |
| 🔥 **Fireplace** | Warmth — and a hearthstone teleportation secret |
| 📋 **Notice Board** | Quest hooks, warnings, community events |
| 👻 **Pac-Man** | Wakka wakka. Who holds the perfect game? |
| 🏓 **Pong** | The original. From Andy Capp's Tavern, 1972. |

---

## 📚 References

| File | What It Is |
|------|------------|
| [ADVENTURE.yml](./ADVENTURE.yml) | **Simulation state**: turn, party, flags |
| [LOG.md](./LOG.md) | **Session log**: narrative transcript |
| [skills/](../../skills/) | **Game systems**: buff, time, needs, economy |
| [kitchen/mothers-note.yml](./kitchen/mothers-note.yml) | **The heart of the game**: promises, goals |
| [pub/README.md](./pub/README.md) | **Social hub**: themes, bartender, cats |
| [adventure-2/README.md](../adventure-2/README.md) | **The legend**: Captain Ashford's journey |

---

*Adventure 3 forked from adventure-2 on January 4, 2026*

*The world remembers. The grue waits. What will YOU do?*
