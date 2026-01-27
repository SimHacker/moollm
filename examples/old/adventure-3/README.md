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
| 🍺 **The Gezelligheid Grotto** | Themeable pub south of start — games, rumors, secrets | `pub/` |
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
   - What questions do you have?
   - What do you want to tell her?
   
   **Your promises become YOUR GOALS.** The DM tracks them. At the end
   of the adventure, you'll discover which promises you kept — and which
   you broke. Mother will have opinions.
   
   *This is freeform creative writing that creates game mechanics!*

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

There are systems at work here that previous adventurers never discovered. Mechanisms that respond to how you play, not just what you do. Things that grow. Things that curse. Things that follow you home.

**Scoring** isn't what you think. Points aren't fixed — they're *calculated* based on style, difficulty, and creativity. The same goal achieved elegantly is worth more than brute force.

**Skills** emerge from play. Do something creative? It might become a technique you can use again. Teach it to an NPC? Even better.

**Curses** are earned. Break a promise? There are... consequences. But lifting a curse teaches something. The scar becomes a story.

**The world grows.** Ask the right questions and new places materialize. Wonder where the grue came from? There might be an answer — and a way to find it.

**Companions** are possible. Ask Mother about family. Recruit NPCs. Build a party. They have opinions. They have goals. They talk to each other when you're not looking.

*For the full systems, see [MECHANICS.yml](./MECHANICS.yml). But discovering how they work is half the fun.*

---

## ✨ What's New in Adventure 3

*The Fantastipants Kitchen has been... upgraded.*

### 🔧 The Workbench

That old granite counter? It's more than meets the eye. Mother always said it "tingled" — turns out she wasn't exaggerating.

**What can you do there?**
- **COMBINE** things to make new things
- **TRANSFORM** things into different things  
- **EDIT** things to change their properties
- **PROGRAM** things to do things when other things happen
- And something else... something that goes *deeper*...

Every experiment you succeed at? The counter remembers. It *learns*.

### 📦 Mail-Order... Something

There's a catalog on the counter. Dog-eared. The coyote on the cover looks optimistic.

> *"ORDER ANYTHING! DELIVERED IN 2-4 TURNS!"*
> *"Satisfaction Guaranteed!*"*

The asterisk leads to very small print.

Items ordered from this catalog *work*. Technically. Usually. The malfunction rate is only... well, Tom has calculated it. Tom has concerns.

### 🗄️ The Drawers

Three drawers under the counter. Father's motto: *"You never know what you'll need."* Mother's motto: *"Why do we have SEVEN broken compasses?"*

One of those compasses might be interesting. Tom keeps looking at it.

### 🗑️ The Trash Can

Don't ask where it leads. Don't climb in unless you're prepared.

If you do... well. Your hair will be *fabulous* when you return.

### 📋 Family Recipes

Some recipes are for sandwiches. Some are for soup.

One requires you to slay a monster with dairy products.

Another is too stained to read. *Experiment.*

### 🧪 Going Deeper

The counter can break things down. Not just "disassemble" — *decompose*.

- Kitchen-level? Easy. Sandwich → bread + cheese.
- Chemical-level? Sure. Water → hydrogen + oxygen. (Store in jars.)
- Atomic-level? The counter starts humming.
- Subatomic-level? The room vibrates. Reality wobbles.
- Philosophical-level? **Do not decompose meaning. You need it.**

*See also:*
- *[How to Deconstruct Almost Anything](http://www.fudco.com/chip/deconstr.html) — Chip Morningstar's legendary essay on the collision of engineering and postmodern literary criticism.*
- *[Captain Ashford's Deconstruction Paper](../../designs/postmodern-deconstruction.md) — Our own PhD-level analysis of adventure-2, applying Morningstar's methods to grues, lamps, and the filesystem-as-world.*

*If you're going to decompose reality, you might as well understand the theory.*

Components can be recombined. Hydrogen + oxygen = water (and a small boom). What else might you synthesize?

### 📬 The Grand Mailbox

Grandmother negotiated eternal free postage in 1923. The mailbox in the start room connects to everywhere — the dungeon, the surface, other dimensions.

**Send anything.** Letters. Photos. Recipes. Skills. Gold. Items.
**Receive anything.** Replies from Mother. ACME deliveries. Chain letters. Plot.

There are matchbooks in the kitchen drawer. Mail them away for stamps featuring famous adventurers. One lousy point each.

### 🍺 The Pub — THE GEZELLIGHEID GROTTO

**The social hub of the adventure.** South of the Chamber, a timeless tavern awaits.

Inspired by **Bar Karma** (Will Wright & Don Hopkins) — the first crowdsourced TV series about a bar at the edge of the universe where lost souls face karmic crossroads. The bartender there was 20,000 years old. Ours is... similar.

**The Gezelligheid Grotto** changes based on your expectations:
- Think of a space cantina → Z-4RT polishes glasses under neon
- Think of a western saloon → Miss Kitty has opinions about your hat
- Think of a pirate tavern → Pegleg Pete asks about your sea legs
- Or describe ANY theme you want...

**What's inside:**

| Object | What It Does |
|--------|--------------|
| 🧑‍🍳 [**Bartender**](./pub/bartender.yml) | Ancient, mysterious, knows everything (for a price) |
| 🪑 [**Seating**](./pub/seating.yml) | Bar (public), Tables (social), Booths (private) |
| 🎯 [**Dart Board**](./pub/dart-board.yml) | Challenge patrons, settle disputes, show off |
| ♟️ [**Chess Table**](./pub/chess-table.yml) | The eternal game — legend says Death left it mid-play |
| 🃏 [**Card Deck**](./pub/card-deck.yml) | Poker, Adventurer's Ruin, Fluxx, the mystery of the 7♣ |
| 🔥 [**Fireplace**](./pub/fireplace.yml) | Warmth — and a hearthstone teleportation secret |
| 📋 [**Notice Board**](./pub/notice-board.yml) | Quest hooks, warnings, community events |
| 👻 [**Pac-Man**](./pub/pacman-cabinet.yml) | Wakka wakka. Who holds the perfect game? |
| 🏓 [**Pong**](./pub/pong-cabinet.yml) | The original. From Andy Capp's Tavern, 1972. |
| 🍒 [**Fruit Machine**](./pub/fruit-machine.yml) | One-armed bandit. It predates the bar itself. |
| 🎱 [**Pinball**](./pub/pinball-machine.yml) | "BAR KARMA" — face your fate in Wizard Mode |

**Social mechanics:** Where you sit matters! Bar stools for regulars and quick service. Tables for games and mixing. Booths for secrets and deals. The bartender serves the bar. A waitress serves tables. Booths? Flag someone down.

**Narrative device:** The pub is where:
- You hear **rumors** (true, mostly-true, and false-but-fun)
- You meet **NPCs** who become companions
- You get **quest hooks** from the notice board
- You discover **plot** through eavesdropping
- You find Mother's **old booth** from her adventuring days

There's a back room. The bartender doesn't talk about it. *Yet.*

*The pub grows with the story. New patrons. New secrets. New themes.*

---

## 🧪 Emergent Mechanics (from adventure-2)

*Patterns discovered through play. Use as inspiration!*

| Mechanic | What Happens | See |
|----------|--------------|-----|
| 🧭 **TomTomagotchi** | Navigation pet that grows with your adventure | [kitchen/tomtomagotchi.yml](./kitchen/tomtomagotchi.yml) |
| 👃 **Smell Gradients** | Transformed food emits smells that diffuse through rooms | [maze/README.md](./maze/README.md) |
| 🔮 **Object Transformation** | Eaten food becomes sentient, prophetic, weaponized... | [kitchen/fridge.yml](./kitchen/fridge.yml) |
| 🐉 **Grue Personality** | The grue can speak, bargain, fight, be eaten | [maze/room-f/](./maze/room-f/) |
| 💀 **Skeleton Stories** | The skeleton accepts gifts, memorials, visitors | [maze/room-i/](./maze/room-i/) |
| ⚡ **Speed of Light** | DM simulates multiple moves seamlessly | [maze/README.md](./maze/README.md) |
| 🎭 **Identity Play** | Costumes affect transformations and interactions | [coatroom/](./coatroom/) |

**DM Principle:** These are EXAMPLES that suggest possibilities. Defer creativity until runtime. Improvise. Surprise yourself!

---

## 📚 References

| File | What It Is |
|------|------------|
| [MECHANICS.yml](./MECHANICS.yml) | **Game systems**: scoring, skills, curses, party, world generation |
| [kitchen/mothers-note.yml](./kitchen/mothers-note.yml) | **The heart of the game**: promises, goals, shaping Mother |
| [kitchen/tomtomagotchi.yml](./kitchen/tomtomagotchi.yml) | **Navigation companion**: GPS, missions, growth |
| [start/mailbox.yml](./start/mailbox.yml) | **Postal system**: mail, stamps, chain letters |
| [pub/ROOM.yml](./pub/ROOM.yml) | **Social hub**: themes, bartender, back room |
| [kitchen/counter.yml](./kitchen/counter.yml) | **Crafting**: combine, transform, decompose |
| [kitchen/acme-catalog.yml](./kitchen/acme-catalog.yml) | **Mail order**: cartoon physics, malfunctions |
| [adventure-2/README.md](../adventure-2/README.md) | **The legend**: Captain Ashford's complete journey |

---

*Adventure 3 forked from adventure-2 on January 4, 2026*

*The world remembers. The grue waits. What will YOU do?*
