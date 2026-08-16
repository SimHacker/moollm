# 👃🦏 Snorax the Patient — The Wumpus Who IS The Game

> *"Patience is not low energy. Patience is POWER."*

Snorax is not just a wumpus. Snorax IS the game **Hunt the Wumpus**.

The game rules, the dodecahedron topology, the original 1973 BASIC source code — all of it lives here in Snorax's character directory. When you hunt the wumpus, you are hunting Snorax. When Snorax hunts you, the game is hunting you.

---

## 🎲 The Character IS The Game

| File | What It Contains |
|------|------------------|
| [CHARACTER.yml](./CHARACTER.yml) | Snorax's soul + game integration |
| [GAME.yml](./GAME.yml) | Complete Hunt the Wumpus rules |
| [DODECAHEDRON.yml](./DODECAHEDRON.yml) | The canonical 20-cave topology |
| [wumpus-basic-source.md](./wumpus-basic-source.md) | Original 1973 BASIC source code |
| [hazards/SUPERBATS.yml](./hazards/SUPERBATS.yml) | Super-bat hazard mechanics |
| [hazards/BOTTOMLESS-PIT.yml](./hazards/BOTTOMLESS-PIT.yml) | Pit hazard mechanics |
| `instances/` | Active game sessions |

---

## 🎮 How To Play

**Start a game:**
```
PLAY WUMPUS
HUNT WUMPUS
SUMMON SNORAX
```

**In game:**
```
MOVE [direction]     — Travel to adjacent room
SHOOT [direction]    — Fire crooked arrow
```

**Win condition:** Arrow hits wumpus
**Lose conditions:** Enter wumpus room, run out of arrows, shot by own arrow

---

## 🗺️ The Dodecahedron

Snorax's native territory is a 20-room dodecahedron. Each room connects to exactly 3 others:

```
         1
       / | \
      2  5  8
     /|  |  |\
   10 3  4  7 9
   |  |\ /|  | |
  11 12-+-14 17 18
   |  | X |  |  |
  19-13-+-15-16-+
    \  20   /
     \___|_/
```

Or play in any room network — the adventure-4 maze, a custom dungeon, even the pub.

---

## 🤝 Parallel Play With The Grue, The Troll, And Others

Snorax, the Grue, and [Two-Toll the Cross-Platform Troll](../troll/) run **parallel games** in the same space:

| Game | Host | Threat Type | How You Die |
|------|------|-------------|-------------|
| **Hunt the Wumpus** | Snorax (beast — haunts a room) | Spatial | Enter wrong room |
| **Don't Go In The Dark** | Grue (field — is everywhere dark) | Time | Stay in darkness 3 turns |
| **Pay The Troll** | Two-Toll (border — prices an edge) | Economic | Cross the guarded edge without paying (steel or treasure, per fronting mind) |

They don't compete. They complement. Each binds to a different element of the
world graph — node, ambient condition, edge — so any room network can host all
three at once. Worst case: lamp dying adjacent to the wumpus room, on the wrong
side of an unpaid bridge.

More portable NPCs (superbats, bottomless pit, the ACME vending machine) and the
travel contract they share: [soul-city/PORTABLE-NPCS.md](../../../../../skills/soul-city/PORTABLE-NPCS.md).

---

## 📜 History

- **1973:** Gregory Yob creates Hunt the Wumpus
- **1975:** Published in *Creative Computing*
- **2012:** Listed in Time's All-Time 100 Greatest Video Games
- **2026:** Incarnated as Snorax at the NPC Incarnation Ceremony

---

*"I smell a wumpus!"* — What others say. Snorax finds this flattering.
