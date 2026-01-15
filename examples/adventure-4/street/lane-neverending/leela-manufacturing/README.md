# Leela Manufacturing Intelligence

> *"We manufacture understanding."*

Welcome to **Leela Manufacturing Intelligence** — the industrial heart of Lane Neverending. Located at **5 Lane Neverending**, right next door to the pub, this facility transforms raw video streams into actionable insights, beautiful visualizations, and genuine understanding.

In SimCity terms, we're an **Industrial Zone** — but instead of manufacturing widgets, we manufacture **knowledge**.

---

## The Leela Pipeline

The core of Leela Manufacturing is a sophisticated data pipeline that transforms video into understanding.

```mermaid
flowchart TB
    subgraph ModelDev["🔬 Model Development (R&D Basement)"]
        OD[("Object Model\nDevelopment")]
        PD[("Pose Model\nDevelopment")]
    end

    subgraph Training["🏋️ Training Pipeline"]
        OT["Object Model\nTraining\n━━━━━━━━━━\n🎯 mAP: 0.947\n⚡ GPU×4"]
        PT["Pose Model\nTraining\n━━━━━━━━━━\n🎯 PCK: 0.923\n⚡ GPU×4"]
    end

    subgraph Deploy["🚀 Model Deployment"]
        ODep["Object Detector\n━━━━━━━━━━━━\nyolo-leela-v2.3.7"]
        PDep["Pose Estimator\n━━━━━━━━━━━━\npose-leela-v1.8.2"]
    end

    OD --> OT --> ODep
    PD --> PT --> PDep

    subgraph Intake["📹 Video Intake"]
        V[("VIDEO\nInput")]
    end

    V --> |"Fork"| Objects
    V --> |"Fork"| Poses

    subgraph Processing["⚙️ Parallel Processing"]
        Objects["🔵 OBJECTS\nBounding boxes\nClassifications\nConfidence scores"]
        Poses["🟠 POSES\nJoint positions\nMovement vectors\nGesture signatures"]
    end

    ODep -.-> |"powers"| Objects
    PDep -.-> |"powers"| Poses

    Objects --> |"merge"| Insights
    Poses --> |"merge"| Insights

    subgraph Understanding["💡 Understanding"]
        Insights["🟡 INSIGHTS\n━━━━━━━━━━\nContext + Motion\n= Understanding"]
    end

    Insights --> Actions

    subgraph ActionLayer["🐍 Python Actions"]
        Actions["🟢 PYTHON ACTIONS\n━━━━━━━━━━━━━━━\nDefine high-level actions\nEmit to SQL tables\nTrigger alerts"]
    end

    Actions --> SQL

    subgraph Storage["💾 Storage"]
        SQL[("🔘 SQL\nStructured\nIndexed\nQueryable")]
    end

    SQL --> PDA

    subgraph Assistant["🤖 Personal Data Assistant"]
        PDA["💬 PDA\n━━━━━━━━━━━━━━━\nChat-driven interface\nGenerates queries\nAnalyzes results\nCreates visualizations"]
    end

    style V fill:#9b59b6,color:#fff
    style Objects fill:#3498db,color:#fff
    style Poses fill:#e67e22,color:#fff
    style Insights fill:#f1c40f,color:#000
    style Actions fill:#27ae60,color:#fff
    style SQL fill:#95a5a6,color:#fff
    style PDA fill:#1abc9c,color:#fff
```

---

## Pipeline Details

### 🔬 Model Development & Training

Two parallel pipelines develop and train the ML models that power perception:

```mermaid
flowchart LR
    subgraph ObjectPipeline["Object Detection Track"]
        direction TB
        OD1["📚 Research\nYOLO variants\nTransformers\nAttention mechanisms"]
        OD2["🏋️ Training\nCOCO, ImageNet\nLeela-Custom-v3"]
        OD3["🚀 Deploy\nyolo-leela-v2.3.7"]
        OD1 --> OD2 --> OD3
    end

    subgraph PosePipeline["Pose Estimation Track"]
        direction TB
        PD1["📚 Research\nKeypoint detectors\nTemporal models\nMotion predictors"]
        PD2["🏋️ Training\nMPII, COCO-Pose\nLeela-Motion-v2"]
        PD3["🚀 Deploy\npose-leela-v1.8.2"]
        PD1 --> PD2 --> PD3
    end

    style ObjectPipeline fill:#e74c3c,color:#fff
    style PosePipeline fill:#e91e63,color:#fff
```

### 🔀 Video Processing Fork

Video enters and immediately forks to parallel processors:

```mermaid
flowchart TB
    V["📹 VIDEO INPUT"]
    V --> |"Frame by frame"| Fork{"Junction Alpha\n(Fork)"}
    Fork --> |"Blue containers"| O["🔵 Object Detector\n━━━━━━━━━━━━━━\n• Bounding boxes\n• Classifications\n• Confidence: 97%\n\n'A cat. 97% sure.'"]
    Fork --> |"Orange containers"| P["🟠 Pose Estimator\n━━━━━━━━━━━━━━\n• Joint positions\n• Movement vectors\n• Gestures\n\n'Waving. Definitely.'"]
    
    O --> Merge{"Junction Beta\n(Merge)"}
    P --> Merge
    
    Merge --> I["🟡 INSIGHTS\n━━━━━━━━━━━━━━\n'A cat (97%) is\nwaving (definitely).'"]

    style V fill:#9b59b6,color:#fff
    style O fill:#3498db,color:#fff
    style P fill:#e67e22,color:#fff
    style I fill:#f1c40f,color:#000
```

### 🐍 Python Actions Layer

Insights flow into Python actions that define high-level events:

```mermaid
flowchart LR
    I["🟡 Insights"] --> A["🟢 Python Actions"]
    
    A --> E1["📊 events.greetings"]
    A --> E2["📈 metrics.engagement"]
    A --> E3["🚨 alerts.unusual"]
    A --> E4["📋 state.machines"]
    
    subgraph Example["Example Transformation"]
        direction TB
        In["Cat detected waving"]
        Out1["action: GREETING_DETECTED"]
        Out2["emit: timestamp, entity, gesture"]
        Out3["emit: engagement_score: 0.87"]
        In --> Out1 --> Out2 --> Out3
    end

    style I fill:#f1c40f,color:#000
    style A fill:#27ae60,color:#fff
```

### 💬 PDA: Personal Data Assistant

The chat-driven interface for exploring your data:

```mermaid
flowchart TB
    User["👤 User"] --> |"Natural language"| Chat["💬 Chat Interface"]
    
    Chat --> Gen["🔧 Generate Query"]
    Gen --> Read["📖 Read SQL Data"]
    Read --> Analyze["🔍 Analyze Results"]
    Analyze --> Viz["📊 Visualize"]
    
    Viz --> User
    
    subgraph Examples["Example Conversations"]
        Q1["'What did the cat do yesterday?'"]
        Q2["'Show me all greetings this week'"]
        Q3["'Why is engagement down?'"]
        Q4["'Compare this week to last'"]
    end

    style Chat fill:#1abc9c,color:#fff
    style User fill:#3498db,color:#fff
```

---

## Factory Floor Map

```mermaid
flowchart TB
    subgraph Building["🏭 LEELA MANUFACTURING INTELLIGENCE"]
        direction TB
        
        subgraph Roof["🌿 Rooftop Garden"]
            Tree["🌳 Origin Tree"]
            Turtle["🐢 Eventually"]
            Scope["🔭 Telescope"]
            Drones["🛸 Drone Pads"]
        end
        
        subgraph F3["Floor 3: Shipping"]
            Depart["📋 Departure Board"]
            Pack["📦 Packaging"]
            Pneumatic["🔵 Pneumatic Hub"]
        end
        
        subgraph F2["Floor 2: Processing"]
            Furnace["🔥 Insight Furnace"]
            Cells["🧪 Processing Cells"]
            Board["📺 Big Board"]
        end
        
        subgraph F1["Floor 1: Intake"]
            Conv["🔄 Conveyor System"]
            Sort["📬 Sorting Stations"]
            Intake["📊 Intake Board"]
        end
        
        subgraph Lobby["Ground Floor: Lobby"]
            Dir["📋 Directory"]
            Elev["🛗 Elevator"]
        end
        
        subgraph Base["Basement: R&D"]
            Lab["🔬 Laboratory"]
            Shelf["🚫 Forbidden Shelf"]
            Zone7["⚠️ Zone 7"]
        end
        
        subgraph External["External Facilities"]
            Load["🚛 Loading Docks"]
            Store["📦 Storage Complex"]
            W23["🏛️ Warehouse 23"]
            Mail["📮 Mail Room"]
            Yard["🏗️ Logistics Yard"]
        end
    end
    
    Roof --> F3 --> F2 --> F1 --> Lobby --> Base
    Lobby --> External

    style Roof fill:#27ae60,color:#fff
    style F3 fill:#3498db,color:#fff
    style F2 fill:#e74c3c,color:#fff
    style F1 fill:#f39c12,color:#fff
    style Lobby fill:#9b59b6,color:#fff
    style Base fill:#34495e,color:#fff
    style External fill:#7f8c8d,color:#fff
```

---

## Floor Directory

| Floor | Name | Purpose |
|-------|------|---------|
| 🌿 | **Rooftop** | Garden, drone pads, wisdom tortoise |
| 3 | **Shipping** | Packaging, departure board, pneumatic tubes |
| 2 | **Processing** | Insight Furnace, processing cells, Big Board |
| 1 | **Intake** | Conveyor system, sorting, intake monitoring |
| G | **Lobby** | Directory, elevator, street access |
| B | **Basement** | R&D Laboratory, Zone 7, Forbidden Shelf |

### External Facilities

| Facility | Purpose |
|----------|---------|
| 🚛 **Loading Docks** | 8 bays (4 in, 4 out), forklifts, drones, carriages |
| 📦 **Storage Complex** | Container prototypes, cloning station, Dolly |
| 🏛️ **Warehouse 23** | Long-term artifact storage (cursed items) |
| 📮 **Mail Room** | Postal integration, pneumatic tubes, pigeons |
| 🏗️ **Logistics Yard** | Trucks, sorting, mass transport |

---

## Storage Aisles

The Storage Complex contains prototypical containers for cloning:

```mermaid
flowchart LR
    subgraph Storage["📦 STORAGE COMPLEX"]
        A["Aisle A\n🪵 Wooden\nCrates, barrels\nchests, boxes"]
        B["Aisle B\n🔩 Metal\nBins, drums\nlockers, safes"]
        C["Aisle C\n👜 Soft\nSacks, bags\npouches, packs"]
        D["Aisle D\n✨ Special\nParadox boxes\nQuantum containers"]
        E["Aisle E\n🖼️ Display\nShelves, cases\nracks, mannequins"]
        L["Aisle L\n🏭 Leela\nLogistics chests\n/dev/null box"]
    end
    
    Dolly["🏗️👑 Dolly\nLift Queen\nFork Queen"]
    Clone["🔬 Cloning\nStation"]
    
    Dolly --> Storage
    Clone --> Storage

    style A fill:#8B4513,color:#fff
    style B fill:#708090,color:#fff
    style C fill:#DEB887,color:#000
    style D fill:#9400D3,color:#fff
    style E fill:#20B2AA,color:#fff
    style L fill:#FF6B6B,color:#fff
```

---

## Key Personnel

| Name | Role | Location |
|------|------|----------|
| 👑 **Dolly Doorin** | Lift Queen / Fork Queen | Storage Complex |
| 🐢 **Eventually** | Wisdom Tortoise | Rooftop Garden |
| 👤 **The Archivist** | Curator | Warehouse 23 |
| 👤 **Dr. Unknown** | Zone 7 Lead | Basement (probably) |
| 👴 **Old Jareth** | Stable Master | Carriage House |

---

## Live Statistics

```mermaid
pie title Pipeline Throughput Today
    "Frames Processed" : 1247000
    "Objects Detected" : 389124
    "Poses Tracked" : 89124
    "Insights Created" : 47891
```

```mermaid
pie title GPU Allocation
    "Object Training" : 1847
    "Pose Training" : 1000
    "Inference" : 500
```

---

## Quick Reference

### Pipeline Flow

```
VIDEO → [fork] → OBJECTS ──┐
                           ├──→ INSIGHTS → PYTHON ACTIONS → SQL → PDA
        [fork] → POSES ────┘
```

### Model Pipeline

```
DEVELOPMENT → TRAINING → DEPLOYMENT → PROCESSOR
     ↑                                    │
     └────────── feedback ────────────────┘
```

### Data Access

```
USER → 💬 CHAT → PDA → SQL
                  ↓
              ANALYSIS
                  ↓
           VISUALIZATION
```

---

## Address

**Leela Manufacturing Intelligence**  
5 Lane Neverending  
(Next to the pub)

*"The insight will come. Eventually."* — Eventually the Tortoise

---

*Part of the [MOOLLM Hotel](../../../) adventure world.*
