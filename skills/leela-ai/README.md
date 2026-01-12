# 🏭 Leela AI

> *"Manufacturing Intelligence"*

> *AI for Manufacturing. Building AI. Constructing Knowledge. And the question of consent.*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | MOOLLM IS Leela's microworld philosophy made manifest |
| [manufacturing-intelligence/](../manufacturing-intelligence/) | The slogan unpacked -- seven readings |
| [society-of-mind/](../society-of-mind/) | Henry Minsky's father invented the theory |
| [k-lines/](../k-lines/) | Minsky's activation vectors power Leela's inference |
| [schema-mechanism/](../schema-mechanism/) | Drescher's causal learning IS Leela's foundation |
| [constructionism/](../constructionism/) | Papert's philosophy -- build to understand |
| [simulator-effect/](../simulator-effect/) | Implication over simulation -- efficiency through semantics |
| [speed-of-light/](../speed-of-light/) | Many inferences in one call -- real-time industrial AI |
| [representation-ethics/](../representation-ethics/) | Manufacturing Consent awareness |
| [yaml-jazz/](../yaml-jazz/) | Semantic configuration for industrial systems |
| [coherence-engine/](../coherence-engine/) | Orchestrating distributed AI across edge devices |

**Quick Links:**
- [leela.ai](https://leela.ai) -- the company
- [schema-mechanism/](../schema-mechanism/) -- Drescher's foundation

---

## The Slogan: Manufacturing Intelligence

| Reading | Meaning |
|---------|---------|
| **AI for Manufacturing** | Industrial applications -- factories, edge devices, production lines |
| **Building AI** | We manufacture intelligence systems |
| **Constructionism** | Papert -- intelligence is constructed, not innate |
| **Society of Mind** | Minsky -- intelligence manufactured from simple agents |
| **Manufacturing Consent** | Chomsky -- awareness of engineered agreement |
| **Growth Mindset** | Intelligence as product, not gift |
| **The Question** | Are we manufacturing genuine intelligence, or its appearance? |

The slogan is a K-line. Every reading reinforces the others.

---

## The Lineage

```
Marvin Minsky (Society of Mind, K-lines, 1985)
  │
  ├── Seymour Papert (Constructionism, Logo, 1980)
  │     └── Build to understand
  │
  └── Gary Drescher (Made-Up Minds, 1991)
        └── Schema mechanism -- causal learning
              │
              v
          Leela AI (2024)
              ├── Neural-symbolic computer vision
              ├── Symbolic inferencing ("why")
              └── MOOLLM (microworld OS)
                    │
                    v
                Manufacturing Intelligence
```

---

## The Team

| Person | Role | K-Lines |
|--------|------|---------|
| **Henry Minsky** | CTO | [Society of Mind](../society-of-mind/) (his father invented it), [K-lines](../k-lines/), MIT AI Lab, Google Nest |
| **Dr. Cyrus Shaoul** | Chief Evangelist | Computational neuroscience, cognitive modeling, Digital Garage |
| **Dr. Milan Singh Minsky** | VP Product | Technology startups, RayVio (UV-C LED) |
| **Sheung Li** | VP Applications | Machine vision in manufacturing, product/marketing |
| **Dr. Steve Kommrusch** | Senior AI Research Scientist | Deep learning, CPU/chip design (AMD, HP, National Semiconductor) |
| **Don Hopkins** | AI Architect | [The Sims](../../designs/sims-design-index.md), [NeWS](../../designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#7-news-james-gosling-sun-1986), [MOOLLM](../moollm/), pie menus |

---

## The Technology Stack

### 1. Neural-Symbolic Vision

Traditional computer vision answers **what**. Leela's neural-symbolic system answers **why**.

```yaml
# Traditional CV
detection:
  object: forklift
  confidence: 0.94
  
# Leela's neural-symbolic
inference:
  object: forklift
  confidence: 0.94
  context: loading_dock
  state: stationary_with_pallet
  
  why_stationary: |
    Waiting for clearance. 
    Worker in path (detected).
    Safety protocol active.
    
  causal_chain:
    - worker entered zone at T-3s
    - proximity sensor triggered
    - forklift brake engaged
    - waiting for zone_clear event
```

This is Drescher's [schema mechanism](../schema-mechanism/) applied to vision:
- **Context** -- what situation is this?
- **Action** -- what happened?
- **Result** -- what follows?
- **Why** -- causal chain explaining the inference

### 2. Edge Box Management

Industrial AI runs on edge devices -- compute boxes at the factory floor, not in the cloud.

```yaml
# edgebox-001.yml
edgebox:
  id: edgebox-001
  location: assembly_line_3
  status: healthy
  
  capabilities:
    - video_inference
    - sensor_fusion
    - local_alerting
    
  # MOOLLM pattern: box as room
  room:
    type: [compute, edge, industrial]
    contains:
      - camera_feed: rtsp://...
      - sensor_array: modbus://...
      - inference_engine: local
      
  # Speed of light: many inferences per second
  throughput:
    mode: real-time
    latency: low
```

The edgebox IS a [room](../room/). It has location, contains objects, processes state.

### 3. PDA App

Personal Data Assistant for field workers:

```yaml
pda_app:
  purpose: |
    Bring AI insights to the human at the edge.
    Not just alerts -- explanations.
    Not just data -- actionable knowledge.
    
  features:
    - live_video_annotation: "What is happening?"
    - causal_explanation: "Why is it happening?"
    - action_recommendation: "What should I do?"
    - voice_interaction: "Ask questions naturally"
    
  # MOOLLM pattern: soul-chat with industrial objects
  interaction:
    user: "Why did the line stop?"
    pda: |
      Thermal sensor on Station 7 exceeded threshold.
      Root cause: bearing friction on motor M-7-3.
      Predicted time to failure: 2-4 hours.
      Recommended: Replace bearing during next break.
```

Everything speaks. The factory floor IS a [soul-chat](../soul-chat/).

### 4. DevOps Integration

MOOLLM patterns for infrastructure management:

```yaml
# Leela DevOps uses MOOLLM's files-as-state
infrastructure:
  pattern: |
    Directories are deployment targets.
    YAML files are configuration.
    Git is the audit trail.
    LLM is the coherence engine.
    
  applications:
    - deploy_orchestration
    - config_management
    - incident_response
    - root_cause_analysis
    
  # The coherence engine maintains consistency
  coherence:
    - detect drift between desired and actual state
    - propose remediation
    - explain changes in plain language
    - audit all modifications
```

---

## Drescher's Foundation

Gary Drescher's *Made-Up Minds* (1991) extended Piaget's developmental psychology with Minsky's computational framework:

| Drescher Concept | Leela Application |
|------------------|-------------------|
| **Schema** | Context → Action → Result patterns in vision |
| **Marginal Attribution** | Learning which features cause which outcomes |
| **Synthetic Items** | Inferred entities not directly observed |
| **Instrumental Conditioning** | Reward signals for system optimization |

The key insight: **You can learn causality from experience.**

Leela's vision system doesn't just detect patterns. It learns *why* those patterns matter.

```yaml
# Schema learning in action
schema:
  context: forklift_approaching_dock
  action: worker_enters_zone
  result: forklift_stops
  
  learned: |
    When workers enter forklift zones,
    forklifts stop (safety interlock).
    This is causal, not coincidental.
    
  marginal_attribution:
    worker_position: 0.92  # highly predictive
    time_of_day: 0.03      # not predictive
    lighting: 0.05         # minor factor
```

See: [schema-mechanism/](../schema-mechanism/)

---

## MOOLLM → Leela Mappings

| MOOLLM Concept | Leela Implementation |
|----------------|---------------------|
| **Rooms** | Edgeboxes, factory zones, equipment clusters, workstations |
| **Characters** | Workers, vehicles, robots, equipment |
| **Skills** | Vision models, inference rules, safety protocols |
| **K-lines** | Equipment IDs, zone names, event types |
| **Speed of Light** | Real-time inference from live video |
| **Coherence Engine** | Multi-camera, multi-sensor fusion |
| **Soul Chat** | PDA natural language interface |
| **Files as State** | YAML configs, audit logs, state snapshots |
| **Society of Mind** | Multiple specialized models collaborating |
| **Schema Mechanism** | Causal learning from observation |

---

## The Manufacturing Consent Question

Chomsky warned about manufactured consent in media.

Leela asks the question honestly: **What are we manufacturing?**

```yaml
ethics:
  transparency:
    - All inferences are explainable
    - Causal chains are auditable
    - No black box decisions for safety
    
  consent:
    - Workers know when they're observed
    - Data stays at the edge when possible
    - Privacy by design, not afterthought
    
  accountability:
    - Human in the loop for critical decisions
    - AI advises, humans decide
    - Audit trail for every action
```

Manufacturing intelligence responsibly means manufacturing *informed* consent.

---

## See Also

### Theory
- [society-of-mind/](../society-of-mind/) -- Minsky's agent theory
- [k-lines/](../k-lines/) -- Activation vectors
- [schema-mechanism/](../schema-mechanism/) -- Drescher's causal learning
- [constructionism/](../constructionism/) -- Papert's philosophy

### Implementation
- [coherence-engine/](../coherence-engine/) -- Distributed AI orchestration
- [speed-of-light/](../speed-of-light/) -- Real-time inference
- [yaml-jazz/](../yaml-jazz/) -- Semantic configuration
- [room/](../room/) -- Spatial organization

### Ethics
- [representation-ethics/](../representation-ethics/) -- Responsible AI
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](../../designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) -- Full philosophy

---

## References

- **Minsky, M. (1985).** *The Society of Mind.* Simon & Schuster.
- **Drescher, G. (1991).** *Made-Up Minds: A Constructivist Approach to Artificial Intelligence.* MIT Press.
- **Papert, S. (1980).** *Mindstorms: Children, Computers, and Powerful Ideas.* Basic Books.
- **Chomsky, N. & Herman, E. (1988).** *Manufacturing Consent.* Pantheon Books.
- **Leela AI.** [leela.ai](https://leela.ai)

---

*"The question is not whether intelligent machines can have any emotions, but whether machines can be intelligent without any emotions."* -- Marvin Minsky

*Manufacturing intelligence means manufacturing understanding. Not just pattern matching -- causal reasoning. Not just detection -- explanation. Not just AI -- knowledge.*
