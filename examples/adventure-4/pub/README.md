# 🍺 The Pub — Home of Gezelligheid

> *"The Gezelligheid Grotto has always been here. It was here before the dungeon. It'll be here after."*  
> — The Bartender (all versions)

---

## 📍 Location

**Path:** `adventure-4/pub/`  
**Parent:** [../](../) (adventure-4 root)  
**Exits:**
- NORTH → [../garden/](../garden/) (back garden, spawn point)
- SOUTH → [../street/lane-neverending/center/](../street/lane-neverending/center/) (Lane Neverending)
- SOUTHWEST → [../kitchen/](../kitchen/) (staff corridor)
- SOUTHEAST → [../coatroom/](../coatroom/) (costume entrance)
- UP → rooms/ | DOWN → basement/ | BACK → ???

---

## 🎭 The Theme System

This pub **transforms**. The room, the staff, the menu, the patrons — all shift based on the current theme.

| Theme | Name | Bartender | Currency |
|-------|------|-----------|----------|
| `classic_adventure` | The Gezelligheid Grotto | Grim | gold |
| `amsterdam_coffeeshop` | **Gezelligheid Grotto** | **Marieke** | gold |
| `space_cantina` | The Rusty Hyperdrive | Z-4RT | credits |
| `cyberpunk_bar` | The Rusty Chrome | Nyx | eddies |
| `victorian_parlor` | The Rusty Cog | Reginald | shillings |
| `pirate_tavern` | The Rusty Anchor | Pegleg Pete | doubloons |
| `wild_west_saloon` | The Rusty Spur | Miss Kitty | dollars |

**Current Theme:** `amsterdam_coffeeshop` → **Gezelligheid Grotto**

---

## 👤 The Staff

### The Bartender (Generic Entity)

**File:** [bartender.yml](bartender.yml)

The bartender is a **constant through all themes** — the same entity wearing different personas. What persists:

- They know everyone's secrets
- They've seen everything
- They're neutral... mostly
- They're ALWAYS here
- They remember across theme changes (but won't admit it)

**Interaction Commands:**
| Command | Effect |
|---------|--------|
| `TALK TO BARTENDER` | Start conversation |
| `ORDER [item]` | Buy from menu |
| `ASK BARTENDER ABOUT [topic]` | Get information (free) |
| `BUY INFORMATION` | Get secrets (costs gold) |
| `RENT ROOM` | Book a room (5 gold) |

### Marieke van der Berg (Current Persona)

**File:** [budtender-marieke.yml](budtender-marieke.yml)

*The Gezelligheid Grotto version of the bartender.*

| Trait | Score | Inner Voice |
|-------|-------|-------------|
| Neat | 8/10 | "A tidy bar is a tidy mind, schat." |
| Outgoing | 7/10 | "You look like you need to talk. Or not." |
| Active | 5/10 | "We move at the speed of coffee." |
| Playful | 6/10 | "ACME again? Loyalty discount?" |
| Nice | 9/10 | "Everyone deserves gezelligheid." |

**Special Knowledge:**
- The 2017 Monkey's Paw incident
- Mother's history at the pub
- Willem and the Monkey's Blessing strain
- Fortune's Mercy terpene

---

## 🐱 The Grotto Family

### Family Tree

```
                        MARIEKE (human caretaker)
                              │
              ┌───────────────┴───────────────┐
              │                               │
          TERPIE ════════════════════ STROOPWAFEL
        (patriarch)        mates        (matriarch)
         [ginger]                        [calico]
              │                               │
              └───────────┬───────────────────┘
                          │
    ┌────┬────┬────┬──────┼──────┬────┬────┬────┐
    │    │    │    │      │      │    │    │    │
   MYR  LEM  LILY PINE  CARRIE HOPS TERP  OCI  JR
```

### Parent Cats

| Cat | File | Personality | Signature Trait |
|-----|------|-------------|-----------------|
| **Terpie** | [cat-terpie.yml](cat-terpie.yml) | Maximum chill | Active: 1, Calm: 7, Restless: 0 |
| **Stroopwafel** | [cat-stroopwafel.yml](cat-stroopwafel.yml) | Fierce matriarch | Active: 9, Restless: 7, Dominant: 7 |

**Their Dynamic:**
> *"She hunts. I rest. Balance."* — Terpie  
> *"He's useless at hunting. Perfect at cuddling."* — Stroopwafel

### The Terpene Litter (8 Kittens)

| Kitten | File | Terpene | Core Trait | Special Ability |
|--------|------|---------|------------|-----------------|
| **Myrcene (Myr)** | [kitten-myrcene.yml](kitten-myrcene.yml) | Sedating | Active: 0 | Sedation field, therapeutic purr |
| **Limonene (Lemon)** | [kitten-limonene.yml](kitten-limonene.yml) | Uplifting | Active: 10 | Joy field, productivity boost |
| **Linalool (Lily)** | [kitten-linalool.yml](kitten-linalool.yml) | Calming | Caring: 7 | Empathy sense, appears when needed |
| **Pinene (Pine)** | [kitten-pinene.yml](kitten-pinene.yml) | Focusing | Analytical: 7 | Perfect memory, focus enhancement |
| **Caryophyllene (Carrie)** | [kitten-caryophyllene.yml](kitten-caryophyllene.yml) | Protective | Cautious: 7 | Threat detection, bit the ACME person |
| **Humulene (Hops)** | [kitten-humulene.yml](kitten-humulene.yml) | Refined | Neat: 8 | Quality detection, appetite suppression |
| **Terpinolene (Terpy Jr.)** | [kitten-terpinolene.yml](kitten-terpinolene.yml) | Chaotic | Spontaneous: 7 | Gravity optional, on the ceiling |
| **Ocimene (Ocie)** | [kitten-ocimene.yml](kitten-ocimene.yml) | Refreshing | Nice: 8 | Air purification, sinus clearing |

---

## 💕 Relationship Matrix

### Bond Scores (0-10)

**Marieke's Bonds:**
| Cat | Bond | Note |
|-----|------|------|
| Terpie | 9 | "The laziest. The best." |
| Stroopwafel | 8 | "Fierce mother. Runs the place." |
| Lily | 9 | "Knows when I'm struggling" |
| Lemon | 8 | "Keeps the designer productive" |
| Carrie | 8 | "Bit the ACME person. Fair." |
| Terpy Jr. | 8 | "On the ceiling again. Normal." |
| Myr | 7 | "Lives on the corner pillow now" |
| Pine | 7 | "Useful during inventory" |
| Ocie | 7 | "Her sneezes help" |
| Hops | 6 | "Has standards. Hard to cuddle." |

**Sibling Rivalries & Alliances:**

| Pair | Relationship | Quote |
|------|--------------|-------|
| Carrie ↔ Lemon | Rivalry + Respect | *"She thinks SHE'S best!"* |
| Pine ↔ Carrie | Intel Partnership | *"She tracks. I act."* |
| Myr ↔ Terpy Jr. | Chaos/Stillness | *"She appears on me. I don't move."* |
| Lily ↔ Henk | Philosopher's Companion | *"He thinks too much. I help."* |
| Lemon ↔ Terpy Jr. | Chaos Buddies | *"NEITHER OF US MAKES SENSE!"* |
| Hops ↔ Everyone | Judging | *"Has opinions. They're correct."* |

---

## 📊 Personality Comparison

### Sims Traits (0-10)

| Character | Neat | Outgoing | Active | Playful | Nice |
|-----------|------|----------|--------|---------|------|
| Marieke | 8 | 7 | 5 | 6 | 9 |
| Terpie | 2 | 3 | **1** | 3 | 8 |
| Stroopwafel | 6 | 5 | **9** | 7 | 5 |
| Myr | 3 | 2 | **0** | 2 | 7 |
| Lemon | 3 | **10** | **10** | **10** | 8 |
| Lily | 5 | 4 | 4 | 4 | **10** |
| Pine | 7 | 4 | 6 | 4 | 6 |
| Carrie | 5 | 3 | 7 | 4 | 4 |
| Hops | **8** | 3 | 4 | 3 | 5 |
| Terpy Jr. | 2 | 6 | 8 | 9 | 6 |
| Ocie | 6 | 6 | 6 | 7 | 8 |

### Mind Mirror Extremes

**Most Energetic:** Lemon (7), Stroopwafel (7)  
**Least Energetic:** Myr (0), Terpie (1)  
**Most Calm:** Terpie (7), Myr (7), Lily (7), Marieke (7)  
**Most Restless:** Stroopwafel (7), Lemon (7)  
**Most Caring:** Lily (7), Carrie (7), Stroopwafel (7), Marieke (7)  
**Most Analytical:** Pine (7)  
**Most Spontaneous:** Terpy Jr. (7), Lemon (7)

---

## 🎮 Objects & Activities

### Games & Entertainment

| Object | File | Description |
|--------|------|-------------|
| Pac-Man Cabinet | [pacman-cabinet.yml](pacman-cabinet.yml) | MOM is 3rd place (847,230) |
| Pong Cabinet | [pong-cabinet.yml](pong-cabinet.yml) | THE prototype from 1972 |
| Pinball Machine | [pinball-machine.yml](pinball-machine.yml) | "Space Adventure Amsterdam" |
| Fruit Machine | [fruit-machine.yml](fruit-machine.yml) | Classic slots |
| Dart Board | [dart-board.yml](dart-board.yml) | Challenge patrons |
| Chess Table | [chess-table.yml](chess-table.yml) | Mid-game abandoned |
| Card Deck | [card-deck.yml](card-deck.yml) | Poker, blackjack, kwartet |

### Furniture & Fixtures

| Object | File | Description |
|--------|------|-------------|
| Fireplace | [fireplace.yml](fireplace.yml) | Hearthstone with teleport rune |
| Notice Board | [notice-board.yml](notice-board.yml) | Quests, warnings, missing persons |
| Pie Table | [pie-table.yml](pie-table.yml) | Octagonal debate table, 8 wedge seats, lazy susan |
| Seating | [seating.yml](seating.yml) | Bar stools, tables, booths, fireplace armchairs, games corner, arcade |

---

## 🍽️ The Menu (Gezelligheid Grotto)

### ☕ Koffie
| Item | Price |
|------|-------|
| Koffie verkeerd | 2 gold |
| Espresso | 2 gold |
| Cappuccino | 3 gold |
| Filter (bottomless) | 2 gold |

### 🥪 Broodjes & Snacks
| Item | Price |
|------|-------|
| Tosti ham-kaas | 4 gold |
| Broodje hagelslag | 2 gold |
| Uitsmijter | 5 gold |
| Bitterballen | 4 gold |

### 🍪 Zoet
| Item | Price |
|------|-------|
| Stroopwafel (warm) | 1 gold |
| Appelgebak | 4 gold |
| Poffertjes | 3 gold |
| Drop (salty licorice) | 1 gold |

### 🍀 Special Strains
| Strain | Price | Effect |
|--------|-------|--------|
| **Monkey's Blessing** | 15 gold | Fortune's Mercy (luck protection) |
| Lucky Strike | 10 gold | Mellow, hopeful |
| Four Leaf Clover | 8 gold | Euphoric, giggly |
| Black Cat Crossing | 12 gold | Inverts bad luck |

---

## 🌟 The Bartender's Lineage

The bartender archetype draws from:

| Reference | Source | Connection |
|-----------|--------|------------|
| **James** | Bar Karma (2011) | 20,000-year-old bartender, Will Wright & Don Hopkins |
| Guinan | Star Trek TNG | El-Aurian, centuries old, unnerves Q |
| Quark | Star Trek DS9 | Ferengi bar owner, deals and dabo |
| Moe | The Simpsons | Long-suffering tavern keeper |
| Sam Malone | Cheers | Everybody knows your name |
| Rick Blaine | Casablanca | "Of all the gin joints..." |

---

## 📁 File Index

### Staff
- [bartender.yml](bartender.yml) — Generic bartender (theme-independent behavior)
- [budtender-marieke.yml](budtender-marieke.yml) — Amsterdam coffeeshop persona

### Cats
- [cat-terpie.yml](cat-terpie.yml) — The mellow patriarch
- [cat-stroopwafel.yml](cat-stroopwafel.yml) — The fierce matriarch

### Kittens
- [kitten-myrcene.yml](kitten-myrcene.yml) — The sleepy one
- [kitten-limonene.yml](kitten-limonene.yml) — The zooming one
- [kitten-linalool.yml](kitten-linalool.yml) — The healer
- [kitten-pinene.yml](kitten-pinene.yml) — The watcher
- [kitten-caryophyllene.yml](kitten-caryophyllene.yml) — The protector
- [kitten-humulene.yml](kitten-humulene.yml) — The refined one
- [kitten-terpinolene.yml](kitten-terpinolene.yml) — The chaos muse
- [kitten-ocimene.yml](kitten-ocimene.yml) — The fresh one

### Objects
- [ROOM.yml](ROOM.yml) — Room definition & theme system
- [cat-cave.yml](cat-cave.yml) — **The Cat Cave** — where cats retreat to hide, sleep, or sulk
- [fireplace.yml](fireplace.yml) — Teleport rune, curios
- [notice-board.yml](notice-board.yml) — Quests & warnings
- [pacman-cabinet.yml](pacman-cabinet.yml) — High scores
- [pong-cabinet.yml](pong-cabinet.yml) — The prototype
- [pinball-machine.yml](pinball-machine.yml) — Flipperkast
- [fruit-machine.yml](fruit-machine.yml) — Slots
- [dart-board.yml](dart-board.yml) — Darts
- [chess-table.yml](chess-table.yml) — Chess
- [card-deck.yml](card-deck.yml) — Cards
- [pie-table.yml](pie-table.yml) — The octagonal debate table with 8 wedge seats
- [seating.yml](seating.yml) — All pub seating: bar, tables, booths, fireplace, games corner, arcade

---

## 🏠 Family Routines

### Morning (6:00-7:00)
```
6:00 — Marieke opens. Terpie doesn't move.
6:15 — Feed everyone. Stroopwafel supervises.
6:30 — Carrie checks perimeter.
6:45 — Lily appears for morning comfort.
7:00 — Lemon begins zooming. Day begins.
```

### Evening (22:00-00:00)
```
22:00 — Last call. Henk on final espresso.
22:15 — Herd kittens to spots.
22:30 — Stroopwafel patrols. Terpie snores.
23:00 — Lily does emotional check on everyone.
23:30 — Myr hasn't moved. Good. Normal.
00:00 — Terpy Jr. is on the ceiling. Also normal.
```

---

*"Gezelligheid isn't a place. It's a feeling. I just provide the setting."*  
— Marieke van der Berg

---

**Last Updated:** Turn 18 (Monkey's Blessing purchased)  
**Current Theme:** Amsterdam Coffeeshop  
**Current Bartender:** Marieke  
**Family Members:** 11 (1 human, 2 cats, 8 kittens)
