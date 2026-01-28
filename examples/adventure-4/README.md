# 🎮 Adventure 4: The Gezelligheid Grotto

> *The world evolved. The pub transformed. The cats remember.*

## 🌍 Overview

Adventure 4 builds on the enriched world from adventure-2 and adventure-3, with significant architectural evolution:

- **Directory-based characters** — Each player has their own folder
- **The Cat Cave** — A TARDIS-like nested room with 10 cats
- **The Pie Menu Round Table** — Debate furniture with compass-stable seats
- **The Gong of Gezelligheid** — Attention, mercy, and musical chairs
- **Marieke the Budtender** — Amsterdam coffeeshop vibes

## 📁 Structure

```
adventure-4/
├── ADVENTURE.yml           # Simulation state (turn, flags, party)
├── LOG.md                  # Summary table (quick reference)
├── TRANSCRIPT.md           # Pure narration (rich reading)
├── README.md               # This file (static description)
│
├── characters/             # Player characters (directory per player)
│   ├── player/             # Default hero (customize in coatroom)
│   ├── don-hopkins/        # Consciousness programmer
│   └── bumblewick.../      # Our beloved hero from adventure-2
│
├── personas/               # Wearable identities
│   └── captain-ashford.yml # The Grue Slayer persona
│
├── garden/                 # Back garden (spawn point, GET LAMP here!)
├── kitchen/                # Mother's domain (note, fridge, Tom)
├── coatroom/               # Maurice's identity laboratory
├── pub/                    # The Gezelligheid Grotto → Gezelligheid Grotto
│   ├── cat-cave/           # TARDIS-like cat retreat
│   ├── pie-table.yml       # Round table with addressable seats
│   ├── gong.yml            # Attention and mercy
│   └── menu-strains.yml    # Cannabis menu (Dutch themed)
├── maze/                   # 10 rooms of darkness
├── end/                    # Treasury
└── home/                   # The goal
```

## 🎯 Goals

From Mother's note on the kitchen table:

1. **Find treasure** — Somewhere in the maze
2. **Bring gold home** — Mother wants proof
3. **Return home safely** — Complete the adventure!

*Plus promises you'll make yourself...*

## 🗺️ World Map

```mermaid
flowchart TB
    subgraph VICTORY["🏠 HOME"]
        HOME[Goal!<br/>Return with treasure]
    end
    
    subgraph DEPTHS["🏛️ THE DEPTHS"]
        TREASURY["💎 TREASURY<br/>Treasure awaits"]
        
        subgraph MAZE_AREA["🌑 THE MAZE (DARK!)"]
            direction LR
            A[A] --- B[B] --- C[C]
            D[D] --- E[E] --- F[F]
            G[G] --- H[H] --- I[I]
            J[J] --- GARDEN["🌿 Garden"]
            CRYSTAL["💎 Crystal<br/>Cave"]
        end
    end
    
    subgraph HUB["🚪 THE HUB"]
        direction LR
        KITCHEN["🍳 KITCHEN<br/>Mom's note<br/>Fridge, ACME catalog"]
        START["⭐ START<br/>Chamber of<br/>Commencement<br/>🪔 LAMP"]
        COATROOM["🎭 COATROOM<br/>Maurice's mirror<br/>Personas"]
    end
    
    subgraph GROTTO["🍺 THE GEZELLIGHEID GROTTO"]
        PUB_MAIN["🏮 Main Floor<br/>Pie Table, Gong<br/>Fireplace, Seating"]
        
        subgraph PUB_WINGS["   "]
            direction LR
            BAR["🍸 Bar<br/>Marieke"]
            CATCAVE["🐱 Cat Cave<br/>TARDIS-like<br/>10 cats"]
            STAGE["🎭 Stage<br/>Palm's nook"]
            ARCADE["🕹️ Arcade"]
            GAMES["🎲 Games"]
        end
        
        subgraph PUB_VERTICAL["   "]
            direction TB
            ROOFTOP["☀️ Rooftop"]
            ATTIC["🧹 Attic"]
            BASEMENT["🍷 Basement<br/>Cellar"]
        end
    end
    
    subgraph CHARS["👥 CHARACTERS"]
        direction LR
        CHAR_DIR["📁 characters/<br/>real-people/<br/>animals/<br/>fictional/"]
    end

    HOME -.-> TREASURY
    TREASURY --> MAZE_AREA
    MAZE_AREA --> START
    KITCHEN <--> START
    START <--> COATROOM
    START --> PUB_MAIN
    PUB_MAIN --- BAR
    PUB_MAIN --- CATCAVE
    PUB_MAIN --- STAGE
    PUB_MAIN --- ARCADE
    PUB_MAIN --- GAMES
    PUB_MAIN -.-> ROOFTOP
    PUB_MAIN -.-> ATTIC
    PUB_MAIN -.-> BASEMENT
    
    style HOME fill:#90EE90,stroke:#228B22,stroke-width:3px
    style START fill:#FFD700,stroke:#DAA520,stroke-width:3px
    style TREASURY fill:#FFD700,stroke:#DAA520
    style MAZE_AREA fill:#1a1a2e,color:#fff
    style PUB_MAIN fill:#8B4513,color:#fff
    style CATCAVE fill:#DDA0DD
    style STAGE fill:#FF69B4
    style CRYSTAL fill:#E0FFFF
    style GARDEN fill:#98FB98
```

**Legend:** Solid lines = normal exits | Dotted lines = up/down

## ✨ What's New in Adventure 4

### 🥧 The Pie Menu Round Table

An octagonal table with compass-stable seats (N, NE, E, SE, S, SW, W, NW).

- **Addressable seats:** `pub/pie-table.yml#SW`
- **Built-in Robert's Rules** for structured debate
- **SUMMON_PANEL** — Instant diverse voices for any topic
- **MUSICAL_CHAIRS** — The slices stay, the chairs go

### 🔔 The Gong of Gezelligheid

| Strikes | Effect |
|---------|--------|
| 1 | All conversation pauses |
| 2 | Emergency interrupt |
| 3 | **Mercy ending** (The Gong Show) |

### 🐱 The Cat Cave

A modest wooden cabinet that's bigger on the inside.

- **Exterior:** 60cm × 40cm × 50cm
- **Interior:** At least 50 meters. Possibly infinite.
- **Residents:** Terpie, Stroopwafel, and 8 terpene kittens
- **Zones:** Vestibule, Nap Zone, Great Hall, The Depths

### 🌿 Amsterdam Coffeeshop Theme

Marieke van der Berg runs the budtending station.

- **Menu:** Lucky strains with MOOLLM-themed names
- **Effect:** Buffs grant temporary psychological effects
- **Wisdom:** "Gezelligheid cannot be translated, only experienced."

## 📜 Session Logs

| File | Purpose |
|------|---------|
| **[LOG.md](./LOG.md)** | Summary table — turns, locations, files changed |
| **[TRANSCRIPT.md](./TRANSCRIPT.md)** | Pure narration — story, YAML objects, mermaid diagrams |

The LOG is for quick reference. The TRANSCRIPT is for reading.

**This README is static.** All play state goes to LOG.md and TRANSCRIPT.md.

## 🧬 Lineage

| Adventure | Hero | Achievement |
|-----------|------|-------------|
| 1 | *(template)* | World created |
| 2 | **Captain Ashford** | Slew grue with cheese, 8/8 promises |
| 3 | **Don Hopkins** | Built the architecture, met the cats |
| 4 | **???** | *Your story here* |

## 🎬 Quick Start

```
> GET LAMP              # In garden/ — don't enter maze without it
> GO WEST               # Kitchen — read Mother's note!
> READ NOTE             # Make promises. Write back.
> GO SOUTH              # Pub — meet Marieke. Visit the Cat Cave.
> GO NORTH              # Into the maze... lamp ready?
```

## 🎞️ Visual Galleries

The adventure includes 14 narrative slideshows with 100+ images — generated, mined, and cross-referenced.

**[📋 Full Slideshow Index](../../indexes/SLIDESHOWS.md)** — Complete catalog with descriptions.
**[🌀 Master Synthesis](./MASTER-SYNTHESIS-SLIDESHOW.md)** — All timelines woven chronologically.

**Quick Links:**
- [The ACME Heist](./street/lane-neverending/leela-manufacturing/lobby/acme-heist-footage/SLIDESHOW.md) (10) — Surveillance footage
- [Donna's Selfies](./characters/fictional/donna-toadstool/selfies/SLIDESHOW.md) (11) — Heist from inside
- [Don's MINE to OURS](./characters/real-people/don-hopkins/selfies/SLIDESHOW.md) (7) — Transformation arc
- [The Great Picnic](./forest/meadow/picnic-footage/SLIDESHOW.md) (21) — Epic meadow journey


---

## 📚 References

| Resource | Purpose |
|----------|---------|
| [ADVENTURE.yml](./ADVENTURE.yml) | Simulation state |
| [skills/](../../skills/) | Game mechanics |
| [kitchen/mothers-note.yml](./kitchen/mothers-note.yml) | The heart of the game |
| [pub/README.md](./pub/README.md) | Cat family, strain menu |

---

*Forked from adventure-3 on January 5, 2026.*

*The cats remember. The gong waits. What will YOU do?*
