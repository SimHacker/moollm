# Lane Neverending

> *"A street that loops forever. Just like good ideas."*

**Lane Neverending** is the main thoroughfare running through this neighborhood. Named in tribute to [Habitat](https://en.wikipedia.org/wiki/Habitat_(video_game)), [Game Neverending](https://en.wikipedia.org/wiki/Game_Neverending), and [Glitch](https://en.wikipedia.org/wiki/Glitch_(video_game)) — pioneering virtual worlds that showed us what online communities could be.

The street runs east and west... and then loops back on itself. Walk far enough in either direction and you'll end up where you started. That's not a bug. That's the point.

---

## Street Map

```mermaid
flowchart TB
    subgraph NorthSide["NORTH SIDE OF STREET"]
        N_W3["     "]
        N_W2["     "]
        N_W1["🏚️ ACME<br/>(closed)"]
        N_C["     "]
        N_E1["     "]
        N_E2["     "]
        N_E3["     "]
    end
    
    subgraph Street["═══════════ LANE NEVERENDING (east ↔ west) ═══════════"]
        W3["w3"] --> W2["w2"] --> W1["w1"] --> C["center"] --> E1["e1"] --> E2["e2"] --> E3["e3"]
        E3 --> |"loops!"| W3
    end
    
    subgraph SouthSide["SOUTH SIDE OF STREET"]
        S_W3["     "]
        S_W2["     "]
        S_W1["🏭 LEELA"]
        S_C["🍺 PUB"]
        S_E1["     "]
        S_E2["     "]
        S_E3["     "]
    end

    style N_W1 fill:#7f8c8d,color:#fff
    style S_W1 fill:#3498db,color:#fff
    style S_C fill:#f39c12,color:#fff
    style C fill:#27ae60,color:#fff
```

**Key locations:**
- **ACME Surplus** (4 Lane Neverending) — North side of W1, closed, painted tunnel
- **Leela Manufacturing** (5 Lane Neverending) — South side of W1, thriving factory
- **The Pub** — South side of center, neighbor to Leela

---

## Street Segments

| Segment | North Side | South Side |
|---------|------------|------------|
| [w3](w3/) | Curiosity shops | — |
| [w2](w2/) | Landmarks | — |
| [w1](w1/) | **ACME Surplus** (closed, painted tunnel) | **Leela Manufacturing** (thriving) |
| [center](center/) | — | **The Pub**, Origin Plaza |
| [e1](e1/) | — | Sleeping Figure, Glitch Memorial |
| [e2](e2/) | Market Square | Fountain of Infinite Loops |
| [e3](e3/) | Loop point | → connects to w3 |

---

## The Loop

```mermaid
flowchart TB
    Start["Start anywhere"]
    
    Start --> Walk["Walk east..."]
    Walk --> More["Keep walking..."]
    More --> Still["Still walking..."]
    Still --> Back["You're back where<br/>you started"]
    
    Back --> |"or"| West["Walk west..."]
    West --> MoreW["Keep walking..."]
    MoreW --> StillW["Still walking..."]
    StillW --> BackW["You're back where<br/>you started"]
```

The street loops. East connects to west. West connects to east. You can walk forever and never leave. You can also walk forever and see everything.

---

## Leela Manufacturing

The crown jewel of Lane Neverending: [Leela Manufacturing Intelligence](leela-manufacturing/) at **5 Lane Neverending**.

```mermaid
flowchart TB
    subgraph Leela["🏭 LEELA MANUFACTURING"]
        Roof["🌿 Rooftop"]
        F3["Floor 3: Shipping"]
        F2["Floor 2: Factory"]
        F1["Floor 1: Intake"]
        Lobby["Lobby"]
        Basement["Basement: R&D"]
    end
    
    Street["Lane Neverending W1"] --> Lobby

    style Leela fill:#3498db,color:#fff
```

The visual intelligence factory. Where video becomes understanding.

---

## Street Furniture

Every segment of Lane Neverending shares common elements, implemented via the [Flyweight Pattern](STREET-FURNITURE.yml):

```mermaid
flowchart LR
    subgraph Prototypes["📋 Shared Prototypes"]
        Lamp["🏮 Lamp Post<br/>Magical flame<br/>Grue-safe"]
        Bench["🪑 Street Bench<br/>Wrought iron<br/>Comfortable"]
        Cobbles["🟫 Cobblestones<br/>Well-worn<br/>Historic"]
        Gutter["💧 Gutter<br/>Functional<br/>Occasional frog"]
    end
    
    subgraph Instances["Each Street Gets"]
        L1["Lamp Post<br/>(north side)"]
        L2["Lamp Post<br/>(south side)"]
        B1["Bench<br/>(unique carvings)"]
    end
    
    Prototypes --> |"flyweight"| Instances
```

| Fixture | Description | Per Street |
|---------|-------------|------------|
| 🏮 Lamp Post | Magical flame, grue-safe | 1-2 |
| 🪑 Bench | Wrought iron, carved names | 1 |
| 🟫 Cobblestones | Historic, well-worn | Throughout |
| 💧 Gutter | Drainage, occasional frog | Along edges |

---

## Landmarks

### Origin Plaza (Center)

```mermaid
flowchart TB
    Plaza["🌳 ORIGIN PLAZA"]
    
    Plaza --> Tree["The Origin Tree<br/>(ancient, knowing)"]
    Plaza --> Lamp["The Flickering Lamp<br/>(famous, mysterious)"]
    Plaza --> Fountain["The Fountain<br/>(wishes optional)"]
```

The heart of Lane Neverending. The tree here is the source of cuttings throughout the neighborhood — including the one on [Leela's rooftop](leela-manufacturing/rooftop/).

### The Flickering Lamp (e1)

One lamp post that flickers. Nobody knows why. It's been that way since before anyone can remember. Some say it's trying to tell us something.

### Glitch Memorial (e1)

A small plaque honoring the citizens of [Glitch](https://en.wikipedia.org/wiki/Glitch_(video_game)) (2011-2012):

> *"Here once stood a world of giants and imagination.*
> *The giants are gone. The imagination remains.*
> *Thanks for all the cubimal boxes."*

### ACME Surplus (w1, North Side)

An abandoned storefront directly across from Leela Manufacturing. Mail-order killed the brick-and-mortar business. There's a boarded-up section with a painted tunnel that you **cannot** walk through, no matter how fast you run.

(Rumor has it ACME agents *can* use it for deliveries...)

The contrast is striking: on one side of the street, a failed retail gimmick shop. On the other, a thriving knowledge factory. The future won.

---

## The Pub

The neighborhood pub sits just east of [Leela Manufacturing](leela-manufacturing/):

```mermaid
flowchart LR
    Leela["🏭 Leela<br/>5 Lane Neverending"]
    Pub["🍺 The Pub<br/>(next door)"]
    
    Leela --> |"pneumatic tube"| Pub
    Leela --> |"walk"| Pub
    Pub --> |"wave via telescope"| Leela
```

There's a priority pneumatic tube directly from Leela to the pub. Some insights are best delivered with a pint.

---

## History

**Lane Neverending** is named in tribute to:

| Project | Years | Legacy |
|---------|-------|--------|
| **Habitat** | 1986-1988 | First graphical MMO. Proved virtual worlds work. |
| **Game Neverending** | 2002-2004 | Became Flickr. Pioneered social gaming. |
| **Glitch** | 2011-2012 | Beautiful, weird, wonderful. Gone too soon. |

The name "Neverending" reflects:
- The infinite loop of the street
- The persistence of virtual worlds
- The idea that good communities never truly end

---

## Address Format

Buildings on Lane Neverending use this format:

```
[Number] Lane Neverending

Examples:
5 Lane Neverending (Leela Manufacturing)
7 Lane Neverending (The Pub)
```

---

## Navigation

The street loops, so you can always get anywhere:

| From | Going East | Going West |
|------|------------|------------|
| Center | → e1 → e2 → e3 → w3 → w2 → w1 → center | → w1 → w2 → w3 → e3 → e2 → e1 → center |

It doesn't matter which way you go. You'll get there.

---

*Part of the [MOOLLM Hotel](../../) adventure world*
