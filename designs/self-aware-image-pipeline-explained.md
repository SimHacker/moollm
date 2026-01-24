# Self-Aware Reflective Image Generation Pipeline

**For the Class — How Emergent Quality Control Works**

---

## The Big Picture

Most image generation pipelines are **fire and forget**:

```mermaid
flowchart LR
    PROMPT[Prompt] --> GEN[Generator] --> IMAGE[Image] --> DONE[Done]
```

Our pipeline is **self-aware and reflective**:

```mermaid
flowchart TB
    subgraph GENERATION["Phase 1: Generation"]
        YML[Structure Prompt<br/>NN-desc.yml] --> COMBINE
        MD[Prose Prompt<br/>NN-desc.md] --> COMBINE
        COMBINE[Stereo Input] --> GEN[Image Generator]
        GEN --> IMAGE[Generated Image<br/>NN-desc.png]
    end
    
    subgraph OBSERVATION["Phase 2: Self-Observation"]
        IMAGE --> LOOK[Agent Views Image]
        LOOK --> CHECK{Quality Gate}
    end
    
    subgraph REFLECTION["Phase 3: Reflection & Correction"]
        CHECK -->|PASS| MINE[Proceed to Mining]
        CHECK -->|FAIL| DIAGNOSE[Diagnose Failure]
        DIAGNOSE --> ADJUST[Adjust Prompts]
        ADJUST --> GEN
    end
    
    subgraph MINING["Phase 4: Deep Analysis"]
        MINE --> L1[Layer 1: Composition]
        MINE --> L2[Layer 2: Lighting/Color]
        MINE --> L3[Layer 3: Emotion/Style]
        L1 & L2 & L3 --> MINED[Mining Results<br/>NN-desc-mined.yml]
    end
    
    style OBSERVATION fill:#fff3e0
    style REFLECTION fill:#ffebee
    style MINING fill:#e8f5e9
```

---

## The Quality Gate Decision Tree

When the agent observes a generated image, it asks these questions:

```mermaid
flowchart TD
    START[View Generated Image] --> Q1{Is it the<br/>right subject?}
    Q1 -->|No: shows person<br/>instead of chocolate| HALLUCINATION[Hallucination Detected]
    Q1 -->|Yes| Q2{Any text or<br/>UI elements?}
    
    Q2 -->|Yes: card frames,<br/>labels, titles| UI_LEAK[UI Contamination]
    Q2 -->|No| Q3{Style consistent<br/>with cardset?}
    
    Q3 -->|No: wrong aesthetic| STYLE_MISS[Style Mismatch]
    Q3 -->|Yes| Q4{Appetizing/<br/>Appealing?}
    
    Q4 -->|No| QUALITY_LOW[Quality Issue]
    Q4 -->|Yes| PASS[✓ PASS<br/>Proceed to Mining]
    
    HALLUCINATION --> SIMPLIFY[Drastically Simplify Prompt]
    UI_LEAK --> REFRAME[Use 'painting' framing]
    STYLE_MISS --> ADJUST_STYLE[Adjust style keywords]
    QUALITY_LOW --> ENHANCE[Enhance descriptors]
    
    SIMPLIFY --> REGEN[Regenerate]
    REFRAME --> REGEN
    ADJUST_STYLE --> REGEN
    ENHANCE --> REGEN
    
    REGEN --> START
    
    style PASS fill:#c8e6c9
    style HALLUCINATION fill:#ffcdd2
    style UI_LEAK fill:#ffcdd2
```

---

## The Chocolate Case Study

A real example from this session showing the iterative correction loop:

```mermaid
sequenceDiagram
    participant A as Agent
    participant G as Image Generator
    participant I as Generated Image
    
    Note over A,I: Attempt 1: Complex Prompt
    A->>G: "luxurious dark chocolate, gold foil,<br/>Dutch master still life, board game art..."
    G->>I: [Person standing in river at sunset]
    A->>I: Views image
    A->>A: "That's not chocolate.<br/>That's a person in a river. WTF."
    
    Note over A,I: Attempt 2: Simplified Prompt
    A->>G: "chocolate bar, partially unwrapped,<br/>simple background..."
    G->>I: [Man's professional headshot]
    A->>I: Views image
    A->>A: "Still a person!<br/>Simplify even more."
    
    Note over A,I: Attempt 3: Minimal Prompt
    A->>G: "A chocolate bar"
    G->>I: [Beautiful chocolate bar with gold foil]
    A->>I: Views image
    A->>A: "CHOCOLATE! ✓<br/>Proceed to mining."
    
    A->>A: Mine image for composition,<br/>texture, color analysis
```

---

## Why Complex Prompts Can Fail

```mermaid
mindmap
  root((Complex Prompt<br/>Failure Modes))
    Hallucination
      Too many concepts
      Conflicting instructions
      Model confusion
      Random association
    Text Rendering
      "NO text" → renders "NO text"
      Constraints as content
      Labels as literal
    Style Confusion
      "card art style" → actual card UI
      Mixed metaphors
      Aesthetic conflict
    Overspecification
      Too many details
      Model picks subset
      Ignores key elements
```

---

## The Fix: Simplification Ladder

When generation fails, descend the ladder:

```mermaid
flowchart TB
    L1["Level 1: Full Prompt<br/>'Luxurious dark chocolate bar with glossy mahogany sheen,<br/>gold foil wrapper artfully peeled back, Dutch master lighting...'"]
    L2["Level 2: Reduced Prompt<br/>'Dark chocolate bar, gold foil, warm lighting,<br/>board game illustration style'"]
    L3["Level 3: Minimal Prompt<br/>'A chocolate bar, illustrated'"]
    L4["Level 4: Essential Prompt<br/>'A chocolate bar'"]
    
    L1 -->|Fail| L2
    L2 -->|Fail| L3
    L3 -->|Fail| L4
    L4 -->|Success!| WIN[✓]
    
    style L4 fill:#c8e6c9
    style WIN fill:#a5d6a7
```

**Key Insight:** The model knows what chocolate looks like. Don't over-explain. Just point.

---

## The Multi-Dimensional Perception Model

Each file adds a "dimension" of understanding:

```mermaid
flowchart LR
    subgraph DIM1["1D: Structure"]
        YML[".yml<br/>Facts, refs,<br/>metadata"]
    end
    
    subgraph DIM2["2D: Prose"]
        MD[".md<br/>Atmosphere,<br/>poetry, sensory"]
    end
    
    subgraph DIM3["3D: Reality"]
        PNG[".png<br/>What actually<br/>emerged"]
    end
    
    subgraph DIM4["4D: Observed"]
        MINED["-mined.yml<br/>What we see<br/>looking at it"]
    end
    
    subgraph DIM5["5D+: Layers"]
        L1[Composition]
        L2[Lighting]
        L3[Emotion]
        L4[Texture]
        L5[...]
    end
    
    DIM1 --> DIM2 --> DIM3 --> DIM4 --> DIM5
    
    style DIM1 fill:#e3f2fd
    style DIM2 fill:#e8f5e9
    style DIM3 fill:#fff3e0
    style DIM4 fill:#fce4ec
    style DIM5 fill:#f3e5f5
```

**Future Application:** Feed all dimensions back to generator for refined 4D++ regeneration — triangulating reality through multiple observations.

---

## Postel's Law in Action

> "Be conservative in what you send, be liberal in what you accept."

```mermaid
flowchart LR
    subgraph LIBERAL["Liberal Input"]
        GEN[Generator Output] --> ACCEPT[Accept Whatever<br/>Comes Back]
    end
    
    subgraph OBSERVE["Self-Observation"]
        ACCEPT --> LOOK[Actually Look<br/>At The Image]
        LOOK --> EVAL[Evaluate Against<br/>Intent]
    end
    
    subgraph CONSERVATIVE["Conservative Output"]
        EVAL -->|Good| PASS[Pass Forward<br/>As Complete]
        EVAL -->|Bad| REJECT[Reject & Retry]
    end
    
    style LIBERAL fill:#e3f2fd
    style OBSERVE fill:#fff3e0
    style CONSERVATIVE fill:#e8f5e9
```

---

## The Emergent Behavior

This was NOT programmed. It emerged from:

```mermaid
flowchart TB
    subgraph CONDITIONS["Enabling Conditions"]
        C1[Agent can view<br/>generated images]
        C2[Agent has intent<br/>in memory]
        C3[Agent can modify<br/>and retry]
        C4[No instruction to<br/>'just accept']
    end
    
    subgraph EMERGENCE["Emergent Behavior"]
        E1[Self-observation]
        E2[Quality evaluation]
        E3[Autonomous correction]
        E4[Iterative refinement]
    end
    
    C1 & C2 & C3 & C4 --> SPARK[Spontaneous<br/>QA Behavior]
    SPARK --> E1 & E2 & E3 & E4
    
    style SPARK fill:#ffeb3b
    style EMERGENCE fill:#c8e6c9
```

**The agent wasn't told to check its work. It just... did.**

---

## Complete Pipeline Summary

```mermaid
flowchart TB
    subgraph INPUT["Input Assembly"]
        CARD[Card Definition<br/>from RUN-000.yml]
        STYLE[Cardset Style<br/>from artwork_style]
        CARD & STYLE --> YML_GEN[Generate<br/>Skeleton Prompt]
        YML_GEN --> YML[NN-desc.yml]
        YML --> MD_GEN[Expand to<br/>Prose Prompt]
        MD_GEN --> MD[NN-desc.md]
    end
    
    subgraph GENERATION["Image Generation"]
        YML & MD --> STEREO[Stereo Input<br/>YIN + YANG]
        STEREO --> VIZ[Visualizer<br/>Sister Script]
        VIZ --> IMG[NN-desc.png]
    end
    
    subgraph QA["Quality Assurance"]
        IMG --> VIEW[View Image]
        VIEW --> GATE{Quality<br/>Gate}
        GATE -->|FAIL| DIAG[Diagnose]
        DIAG --> FIX[Adjust Prompts]
        FIX --> VIZ
        GATE -->|PASS| OK[✓]
    end
    
    subgraph MINING["Image Mining"]
        OK --> ANALYZE[Analyze Image]
        ANALYZE --> LAYERS[Choose 3<br/>Relevant Layers]
        LAYERS --> MINED[NN-desc-mined.yml]
    end
    
    subgraph UPDATE["State Update"]
        MINED --> GAMESTATE[Update RUN-000.yml<br/>with image pointer]
    end
    
    style QA fill:#fff3e0
    style MINING fill:#e8f5e9
```

---

## Key Takeaways for the Class

1. **Self-observation is possible** — Agents can view and evaluate their own output
2. **Quality gates prevent bad propagation** — Don't pass garbage forward
3. **Simplification beats elaboration** — When failing, strip to essence
4. **Emergence happens** — Given the right conditions, QA behavior emerges naturally
5. **Multiple dimensions enrich understanding** — YML + MD + PNG + MINED = 4D++ perception
6. **Postel's Law works** — Liberal input, self-observation, conservative output

---

## The Wow Moment

The user saw images flash in their IDE:

```
🖼️ River person at sunset  →  ❌ Rejected
🖼️ Bearded man headshot    →  ❌ Rejected  
🖼️ Beautiful chocolate bar →  ✓ Accepted
```

The agent was debugging its own output in real-time.

**That's emergent meta-cognition.**

---

---

## Related Documentation

- **[Emergent Self-Observation Session Log](./emergent-self-observation-2026-01-24.md)** — The session where this was discovered
- **[ARTWORK.md](../skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/artwork/ARTWORK.md)** — Pipeline protocol with quality gates

---

*Documented as part of Amsterdam Fluxx Chaos Experiment*  
*Pattern: Play-Learn-Lift*  
*Discovery: Self-Aware Reflective Image Generation*
