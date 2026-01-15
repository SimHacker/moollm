# 🌿 The Back Garden

> *"Every adventure begins somewhere. Yours begins here, among the flowers."*

The **Rusty Lantern Back Garden** — where heroes spawn, rest, and gather courage.

---

## 🏠 This Is The Starting Room

When you begin your adventure, you wake up here at a garden table.
When you die, you respawn here with your inventory intact.

**First moves:**
1. **GET LAMP** — Essential for the maze!
2. **CHECK MAIL** — There's a mailbox here
3. **GO WEST** to kitchen — Read Mother's note, get food
4. **GO NORTH** to pub — Meet the bartender, get supplies

---

## 🗺️ Topology

```
              ┌─────────┐
              │   PUB   │ ← bar, patrons, stage
              └────┬────┘
   ↙ SW (pub)      │ south        SE (pub) ↘
┌─────────┐   ┌────┴────┐   ┌──────────┐
│ KITCHEN │←──│ GARDEN  │──→│ COATROOM │
└─────────┘ W │ (spawn) │ E └──────────┘
              └────┬────┘
                   │ south
              ┌────┴────┐
              │  MAZE   │ ← dark, grues!
              └─────────┘
```

---

## 🚪 Exits

| Direction | Destination | Description |
|-----------|-------------|-------------|
| **North** | [pub/](../pub/) | The Rusty Lantern — warmth and ale |
| **South** | [maze/room-a/](../maze/room-a/) | ⚠️ The maze — dark and dangerous! |
| **East** | [coatroom/](../coatroom/) | Costume Emporium — be anyone! |
| **West** | [kitchen/](../kitchen/) | Fantastipants Kitchen — supplies |
| **Inward** | [characters/](../characters/) | Hall of Bodies (metaphysical) |

---

## 📦 Objects Here

| Object | File | Purpose |
|--------|------|---------|
| **Lamp** | [lamp.yml](lamp.yml) | 🔥 GET THIS FIRST! Essential for maze |
| **Mailbox** | [mailbox.yml](mailbox.yml) | Check mail, send letters |
| **Garden Table** | [garden-table.yml](garden-table.yml) | Rest, read newspaper |
| **Newspaper** | [newspaper.yml](newspaper.yml) | Local news and rumors |
| **Blackboard** | [blackboard.yml](blackboard.yml) | Today's specials |
| **Suspicious Plant** | [suspicious-plant.yml](suspicious-plant.yml) | It's watching you |

---

## 🌤️ Atmosphere

The garden exists in comfortable neglect — tended just enough to be charming, ignored just enough to be wild.

**Flora:**
- Lavender (buzzing with bees)
- Rosemary (smell of memory)
- Climbing roses (red, fragrant)
- Hops vines (the pub grows its own)
- One SUSPICIOUS PLANT

**Furniture:**
- Three round tables (2, 4, 6 seats)
- A wooden bench against the wall
- A barrel being used as a table
- Mismatched chairs with stories

**Features:**
- Strings of fairy lights (for evening)
- A small fountain (currently a birdbath)
- An invisible cat (Schrodinger, probably)

---

## 🎮 Activities

| Command | Effect |
|---------|--------|
| `SIT` | Take a seat, rest, think |
| `SMELL` | Lavender, rosemary, roses, cooking |
| `WATCH` | May notice the cat. May notice other things. |
| `READ` | Check newspaper or blackboard |
| `GARDEN` | Light weeding. One plant SAYS THANK YOU. |

---

## ⚠️ Before Going South

The maze is **DARK**. You will be eaten by a grue.

**Checklist:**
- [ ] GET LAMP (from this garden)
- [ ] LIGHT LAMP
- [ ] GET FOOD from kitchen (for maze-mapping)
- [ ] READ Mother's note
- [ ] (Optional) Get a costume from coatroom

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [adventure-4/](../) |
| 🍺 North | [pub/](../pub/) |
| 🌀 South | [maze/room-a/](../maze/room-a/) |
| 🎭 East | [coatroom/](../coatroom/) |
| 🍳 West | [kitchen/](../kitchen/) |

---

*"It's the kind of garden where adventures begin — or where heroes rest between them."*
