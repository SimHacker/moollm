# W1: Leela's Neighborhood

> *"Where intelligence meets industry. And also a nice pub."*

**W1** is the segment of Lane Neverending just west of the center. This is prime real estate — home to [Leela Manufacturing Intelligence](../leela-manufacturing/) at 5 Lane Neverending, and right next to the beloved neighborhood pub.

---

## The Neighborhood

```mermaid
flowchart LR
    W2["← w2"] --> W1["W1\nYou Are Here"]
    W1 --> Center["center →"]
    
    subgraph Buildings["This Block"]
        Leela["🏭 LEELA\n5 Lane Neverending\n(south side)"]
        Pub["🍺 THE PUB\n7 Lane Neverending\n(just east)"]
    end
```

---

## Leela Manufacturing Intelligence

```mermaid
flowchart TB
    subgraph Leela["🏭 LEELA MANUFACTURING"]
        direction TB
        Roof["🌿 Rooftop Garden"]
        F3["Floor 3: Shipping"]
        F2["Floor 2: Factory"]
        F1["Floor 1: Intake"]
        Lobby["Ground: Lobby"]
        Basement["Basement: R&D"]
    end
    
    Street["W1 (here)"] --> Lobby

    style Leela fill:#3498db,color:#fff
```

The visual intelligence factory. Video comes in, understanding comes out. Full documentation: [Leela Manufacturing →](../leela-manufacturing/)

---

## The Pub

Just east of Leela, almost at the corner with center. A priority pneumatic tube connects the two buildings directly.

| Feature | Notes |
|---------|-------|
| Priority tube from Leela | 2 second delivery |
| Garden in back | Origin Tree cutting grows there |
| Rooftop telescope | Waves at Leela's telescope |

---

## Street Furniture

| Fixture | Location | Notes |
|---------|----------|-------|
| 🏮 Lamp Post | North side | Standard flyweight instance |
| 🪑 Bench | South side, near Leela entrance | Good for thinking |

---

## Connections

| Direction | Destination | Notes |
|-----------|-------------|-------|
| ⬅️ West | [w2](../w2/) | More landmarks |
| ➡️ East | [center](../center/) | Origin Plaza |
| 🏭 South | [Leela Manufacturing](../leela-manufacturing/) | The factory |
| 🍺 East | The Pub | Next door |

---

*Part of [Lane Neverending](../README.md)*
