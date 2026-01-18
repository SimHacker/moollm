# The Maze

> *"You are in a maze of twisty little passages, all alike."*
> — [Colossal Cave Adventure](https://en.wikipedia.org/wiki/Colossal_Cave_Adventure), 1976

> *"I smell a wumpus!"*
> — [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus), Gregory Yob, 1973

A proper adventure needs a proper maze. This one has grues AND a wumpus.

---

## Two Games, One Maze

This maze runs **two classic games simultaneously**:

| Game | Origin | Threat | Warning |
|------|--------|--------|---------|
| **Grue Survival** | Zork (1980) | Darkness kills | "It is pitch black..." |
| **Hunt the Wumpus** | Yob (1973) | Hazards kill | "I smell a wumpus!" |

They don't interfere — different threat models:
- **Grue** = time pressure (keep lamp lit)
- **Wumpus** = spatial pressure (navigate carefully)

---

## Hunt the Wumpus

### The Hazards

| Hazard | Location | Warning | Effect |
|--------|----------|---------|--------|
| **Grumbus the Wumpus** | room-e | "I smell a wumpus!" | Instant death on entry |
| **Old Leatherwing's Bats** | room-b | "Bats nearby!" | Random relocation |
| **The Whispering Maw** | room-c | "I feel a draft!" | Fall forever |
| **The Silent Drop** | room-g | "I feel a draft!" | Fall forever |
| **The Grue** | everywhere dark | "It is getting dark..." | Eaten in darkness |

### Game State as Files

Hazard positions are stored as instance files, not in ROOM.yml:

```
room-e/wumpus.yml   ← Grumbus lives here (state + memories)
room-b/bats.yml     ← Old Leatherwing's colony
room-c/pit.yml      ← The Whispering Maw
room-g/pit.yml      ← The Silent Drop
```

**Game control via file operations:**
```bash
mv room-e/wumpus.yml room-f/wumpus.yml  # Wumpus moves
rm room-e/wumpus.yml                     # Wumpus killed  
rm room-*/wumpus.yml room-*/bats.yml     # Reset game
```

### Crooked Arrows

The only weapon against the wumpus. Fire through 1-5 rooms:

```
SHOOT 3 → room-d → room-e → room-f
```

- Hit wumpus = **WIN**
- Hit yourself = **LOSE**
- Miss = wumpus wakes (75% moves, 25% stays)

**Buy arrows at the vendor** (12 gold each, or bundle of 5 for 50 gold).

### Play Modes

| Command | Effect |
|---------|--------|
| `PLAY WUMPUS` | Start hunt with full rules |
| `PLAY CLASSIC` | Original 1973 rules only |
| `SIMULATE GAME` | LLM plays as current character |
| `OVERDRIVE` | Fast simulation, montage style |

See [wumpus.yml](./wumpus.yml) for complete game rules (807 lines).
See [wumpus-bas.md](./wumpus-bas.md) for original 1973 BASIC source.

---

## Grue Survival

**The maze is DARK.** All rooms have `lighting: none`.

If you enter without a **lit lamp**:

```
It is pitch black. You are likely to be eaten by a grue.
```

The grue gives you **3 turns** in darkness before attacking. Keep your lamp lit.

See [grue.yml](./grue.yml) for the grue's full personality and mechanics.

---

## ACME Dungeon Supply Depot (room-j)

Everything you need to survive. Flat prices, no limits.

| Category | Item | Price |
|----------|------|-------|
| **Lamp** | Oil Refill | 1 |
| | Deluxe Refill | 2 |
| | Premium Glow Juice | 3 |
| **Light** | Torch | 2 |
| **Pit Gear** | Plank | 5 |
| | Rope (50ft) | 8 |
| | Feather Token | 10 |
| **Wumpus** | Crooked Arrow | 12 |
| | Arrow Bundle (5) | 50 |
| **Bats** | Bat Fruit | 3 |
| **Grues** | Grue Repellent | 15 |

**Easter Egg:** Kick the machine → **50 gold jackpot** (once per game)

*"WHAT DO YOU THINK I AM? A ONE-ARMED BANDIT? IS THIS VEGAS??"*

---

## The Rooms

| Room | Feature | Hazards | Warnings Heard |
|------|---------|---------|----------------|
| [room-a/](./room-a/) | Puddle | — | draft (pit in c) |
| [room-b/](./room-b/) | Echo | **BATS** | bats here, draft (pit in c) |
| [room-c/](./room-c/) | Scratch marks | **PIT** | — |
| [room-d/](./room-d/) | Golden glow | — | wumpus (e), draft (c), bats (b) |
| [room-e/](./room-e/) | Cobwebs | **WUMPUS** | — |
| [room-f/](./room-f/) | Cold + **100 GOLD** | **GRUE LAIR** | draft (g), wumpus (e) |
| [room-g/](./room-g/) | Carved face | **PIT** | — |
| [room-h/](./room-h/) | Mushrooms | — | wumpus (e) |
| [room-i/](./room-i/) | Skeleton | — | — |
| [room-j/](./room-j/) | **VENDOR** | — | — |
| [crystal-cave/](./crystal-cave/) | Crystals | — | — |
| [garden/](./garden/) | Sunlight | — | — |

---

## The Hazard Instances

### Grumbus the Wumpus (room-e)
- Massive, matted fur, milky eyes
- Old arrow scar on left flank
- Snores melodically
- 12 adventurers eaten, 2 arrows dodged
- Donna Toadstool's opinion: "Sleepy Wumpus. Low Energy. SAD!"

### Old Leatherwing's Colony (room-b)
- ~200 bats, alpha has 7ft wingspan
- Regal but cranky
- Specialty: drops people near the wumpus

### The Whispering Maw (room-c)
- Bottomless, jagged edges, crumbling
- 7 fallen, including Sir Reginald ("How deep could it poss—")
- Graffiti: "LOOK DOWN", "RIP REGGIE"

### The Silent Drop (room-g)
- Perfectly circular, smooth as glass
- Predates the maze
- Theories: portal not pit, the face IS the pit looking up

---

## Prototype Files

Game mechanics are defined in shared prototypes:

| File | Lines | Purpose |
|------|-------|---------|
| [wumpus.yml](./wumpus.yml) | 807 | Complete game + wumpus creature |
| [superbats.yml](./superbats.yml) | 346 | Bat colony behavior |
| [bottomless-pit.yml](./bottomless-pit.yml) | 213 | Pit hazard mechanics |
| [grue.yml](./grue.yml) | 239 | Darkness creature |
| [CONTAINER.yml](./CONTAINER.yml) | 115 | Shared maze properties |

---

## Legends from Previous Adventures

- Captain Ashford slew a grue with **blue cheese**
- Room-f still smells of cheese and victory
- The skeleton received a **grue head trophy**
- Mushrooms in room-h spawned **The Thing That Watches**
- A **PhD paper** was written about it all

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| Up | [adventure-4/](../) |
| North (from room-a) | [../garden/](../garden/) — Back to spawn |
| South (deep) | [../end/](../end/) — Treasury |
