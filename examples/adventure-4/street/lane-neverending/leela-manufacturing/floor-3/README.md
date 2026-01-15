# Floor 3: Shipping Department

> *"Where insights go out into the world."*

The **Shipping Department** is the final stage of Leela's visual intelligence pipeline. Finished insights arrive from the Factory Floor, get packaged, labeled, and dispatched to customers across... everywhere.

---

## The Flow of Knowledge

```mermaid
flowchart LR
    subgraph Input["From Floor 2"]
        Insights["✨ Refined Insights"]
    end
    
    Insights --> Package["📦 Packaging\nStations"]
    
    Package --> Doc["📋 Documentation\nCenter"]
    
    Doc --> Dispatch["🚀 Dispatch"]
    
    subgraph Methods["Delivery Methods"]
        Tube["🔵 Pneumatic Tube\n(local, fast)"]
        Drone["🛸 Drone\n(medium range)"]
        Truck["🚛 Truck\n(bulk orders)"]
        Rail["🚂 Rail\n(cross-world)"]
        Pigeon["🕊️ Pigeon\n(traditional)"]
        Pickup["🚶 Walk-in\n(customers collect)"]
    end
    
    Dispatch --> Methods

    style Insights fill:#f1c40f,color:#000
    style Package fill:#3498db,color:#fff
```

---

## Departure Board

The iconic split-flap departure board dominates the center of the floor:

```
*clack clack clack*
```

```mermaid
gantt
    title Current Departures
    dateFormat HH:mm
    axisFormat %H:%M
    
    section Departed
    Insight Bundle #4471 → Rusty Lantern    :done, 14:23, 1m
    Knowledge Crate K-99 → Construction     :done, 14:25, 1m
    
    section Boarding
    Wisdom (Premium) → Origin Plaza         :active, 14:30, 5m
    
    section Queued
    Bulk Questions → RETURN TO INTAKE       :14:47, 3m
    [CLASSIFIED] → [CLASSIFIED]             :15:00, 5m
```

| Time | Shipment | Destination | Status |
|------|----------|-------------|--------|
| 14:23 | Insight Bundle #4471 | The Rusty Lantern | 🟢 DEPARTED |
| 14:25 | Knowledge Crate K-99 | Construction Site | 🟢 DEPARTED |
| 14:30 | Wisdom (Premium) | Origin Plaza | 🟡 BOARDING |
| 14:47 | Bulk Questions | RETURN TO INTAKE | ⏳ QUEUED |
| 15:00 | [CLASSIFIED] | [CLASSIFIED] | ⚪ SCHEDULED |

---

## Packaging Stations

Six specialized stations for different shipment types:

```mermaid
flowchart TB
    subgraph Stations["PACKAGING STATIONS"]
        S1["Station 1\n📦 Standard\nCardboard, labels"]
        S2["Station 2\n🥚 Fragile\nFoam, bubble wrap\nHANDLE WITH CARE"]
        S3["Station 3\n👑 Premium\nVelvet-lined boxes\nGold ribbon"]
        S4["Station 4\n📚 Bulk\nShrink-wrapped pallets"]
        S5["Station 5\n☢️ Hazardous\nContainment vessels\nWarning labels"]
        S6["Station 6\n🎨 Custom\nBespoke packaging\nfor special orders"]
    end

    style S3 fill:#f1c40f,color:#000
    style S5 fill:#e74c3c,color:#fff
```

| Station | Type | Specialist | Current Queue |
|---------|------|------------|---------------|
| 1 | Standard | "Box Bob" | 23 |
| 2 | Fragile | "Careful Carol" | 8 |
| 3 | Premium | "Fancy Frank" | 3 |
| 4 | Bulk | "Big Batch Betty" | 45 |
| 5 | Hazardous | "Hazmat Hannah" | 1 |
| 6 | Custom | "Creative Chris" | 2 |

---

## The Pneumatic Hub

A brass-and-glass marvel of Victorian engineering:

```mermaid
flowchart TB
    Hub["🔵 PNEUMATIC HUB"]
    
    Hub --> T1["Tube 1\n→ Floor 1"]
    Hub --> T2["Tube 2\n→ Floor 2"]
    Hub --> T3["Tube 3\n→ Lobby"]
    Hub --> T4["Tube 4\n→ Basement"]
    Hub --> T5["Tube 5\n→ Loading Docks"]
    Hub --> T6["Tube 6\n→ Mail Room"]
    Hub --> T7["Tube 7\n→ THE PUB\n🍺 PRIORITY"]
    Hub --> T8["Tube 8\n→ Rooftop"]

    style T7 fill:#f39c12,color:#fff
    style Hub fill:#3498db,color:#fff
```

**Tube 7** has special priority status — it goes directly to the pub next door. Some insights are best delivered with a pint.

| Tube | Destination | Avg Transit Time | Capsules/Hour |
|------|-------------|------------------|---------------|
| 1 | Floor 1 (Intake) | 3 seconds | 47 |
| 2 | Floor 2 (Factory) | 3 seconds | 23 |
| 3 | Lobby | 4 seconds | 12 |
| 4 | Basement | 5 seconds | 8 |
| 5 | Loading Docks | 6 seconds | 89 |
| 6 | Mail Room | 4 seconds | 34 |
| 7 | **THE PUB** | 2 seconds | **PRIORITY** |
| 8 | Rooftop | 7 seconds | 15 |

---

## The Explainers

A dedicated team that translates "raw insight" into "actionable knowledge":

> *"If you can't explain it, it's not done."*

```mermaid
flowchart LR
    Raw["🟡 Raw Insight\n'Correlation detected\nbetween variables\nX₇ and ∂Y/∂t'"]
    
    Raw --> Explainer["📝 Explainer"]
    
    Explainer --> Clear["✅ Clear Insight\n'When temperature rises,\nproductivity increases.\nRecommendation: Better HVAC.'"]

    style Raw fill:#f1c40f,color:#000
    style Clear fill:#27ae60,color:#fff
```

---

## Returns Desk

For insights that didn't quite work out:

> *"WE DON'T DO REFUNDS. WE DO BETTER QUESTIONS."*

When an insight fails to provide value, we don't take it back — we figure out what the *real* question should have been.

---

## Camera: SHP1

**SHP1** (Shipping Eye) watches the departure board and packaging stations from above.

| Metric | Last Hour |
|--------|-----------|
| Packages wrapped | 89 |
| Departures recorded | 47 |
| Pneumatic launches | 23 |
| Rush orders | 12 |
| Packages too beautiful | 1 (sent to gallery) |

---

## Connections

| Direction | Destination | Notes |
|-----------|-------------|-------|
| ⬇️ Down | [Floor 2 — Factory](../floor-2/) | Insight Furnace |
| ⬆️ Up | [Rooftop Garden](../rooftop/) | Drone pads |
| 🚛 East | [Loading Docks](../loading-docks/) | Truck dispatch |
| 🛗 Elevator | [Lobby](../lobby/) | Main entrance |

---

## Objects on This Floor

- 📋 [Departure Board](departure-board.yml) — *clack clack clack*
- 📦 [Packaging Stations](packaging-stations.yml) — Six specialists
- 🔵 [Pneumatic Hub](pneumatic-hub.yml) — Eight-tube terminal
- 📹 [Camera SHP1](camera-shp1.yml) — The Shipping Eye

---

*Part of [Leela Manufacturing Intelligence](../README.md) • 5 Lane Neverending*
