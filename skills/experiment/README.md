# Experiment Skill

🧪 **Simulation + Evaluation + Iteration + Analysis**

> *"The Cosmic Dealer sees all. The mirror remembers. The Harper numbers never lie."*

---

## TL;DR for Hackers

This skill turns LLM sessions into **reproducible experiments** with state snapshots, rubrics, and analytics. Think:

- **Git for game simulations** — every turn is a commit
- **Scientific method for character AI** — hypothesis → run → measure → iterate
- **Speed of Light protocol** — 30+ turns per API call

**Proof that it works:** We ran a 5-tournament Fluxx championship. 116 turns. 731 tool calls. 24 AI-generated cards. 32 AI-generated artworks. One underdog champion. [Jump to results →](#experiment-showcase)

---

## What Is This?

An experiment combines four activities into systematic practice:

| Activity | What It Does | Methods |
|----------|--------------|---------|
| **SIMULATE** | Generate character interactions | `RUN`, `SIMULATE` |
| **EVALUATE** | Score against rubric criteria | `EVALUATE`, `SCORE` |
| **ITERATE** | Run again with variations | `RERUN`, `VARY`, `REPLAY` |
| **ANALYZE** | Compare runs, find patterns | `COMPARE`, `ANALYZE`, `REPORT` |

**Key insight:** Separate the experiment (stable) from the config (setup) from the output (result). This allows systematic comparison across models, characters, and parameters.

---

## Experiment Showcase

### Currently Active Experiments

| Experiment | Status | Description | Key Result |
|------------|--------|-------------|------------|
| **[Fluxx Chaos](#fluxx-chaos-championship)** | ✅ COMPLETE | Card game + dynamic rules + AI artwork | 94/100 score |
| **[Turing Chess](#turing-chess)** | 🔄 DESIGNED | Chess performance simulation | Protocol proven |
| **[Emo Poker Face](#emo-poker-face)** | 📋 TEMPLATE | Layer separation stress test | Pattern library |

---

## Fluxx Chaos Championship

**The flagship experiment.** Multi-session, multi-tournament Fluxx simulation with:

- 🎴 **Dynamic rule changes** — Rules mutate during play (Draw 5, Play All, etc.)
- 🎭 **Character AI** — 4 distinct personalities with evolving arcs
- 🎨 **AI artwork pipeline** — 32 card images with stereo prompts
- 🃏 **Dynamic card generation** — 24 personalized cards forged from gameplay

### Quick Links

| Resource | Description |
|----------|-------------|
| [**📊 SCORE.md**](experiments/fluxx-chaos/runs/amsterdam-flux/SCORE.md) | Full tournament scoring, Harper numbers, roundtable |
| [**🔍 CURSOR-MIRROR-ANALYSIS.md**](experiments/fluxx-chaos/runs/amsterdam-flux/CURSOR-MIRROR-ANALYSIS.md) | Meta-analysis of the AI's own process |
| [**🖼️ Card Gallery**](experiments/fluxx-chaos/runs/amsterdam-flux/artwork/SLIDESHOW.md) | 32 AI-generated card artworks |
| [**📜 Experiment Design**](experiments/fluxx-chaos/EXPERIMENT.md) | Full modular architecture |
| [**🎮 Game Runs**](experiments/fluxx-chaos/runs/amsterdam-flux/) | 24 run files (RUN-000 to RUN-023) |

### The Numbers

| Metric | Value |
|--------|-------|
| **Total turns simulated** | 116 |
| **Total games played** | 20+ |
| **Tournaments completed** | 5 |
| **Tool calls** | 731 |
| **API calls** | ~50 (Speed of Light = many turns per call) |
| **YAML lines written** | 12,947 |
| **Card images generated** | 32 |
| **Custom cards created** | 24 |
| **Overall score** | **94/100** |

### Character Arcs

| Character | Arc | Signature Moment |
|-----------|-----|------------------|
| **Bumblewick** 🎩 | 0-8 underdog → Long Shot champion | *"I had to let you go."* (signing Love card) |
| **Donna** 🍄 | Dominant champion → FAFO victim → survivor | *"Six creepers. SIX."* |
| **Don** 🍪 | Cookie theft victim → silent champion | *"271 cookie mentions. 14 thefts. Finally mine."* |
| **Palm** ☕ | Observer → pattern-cracker | *"..."* (wins by saying nothing) |

### Emergent Mechanics

Things the AI **invented during gameplay**:

| Mechanic | What Happened |
|----------|---------------|
| **FAFO Token Paradox** | Token holder can't win even with perfect combo (it's a creeper!) |
| **Melodramatic Loophole** | Lamentation ≠ confidence — wailing escapes FAFO punishment |
| **Silent Victory Protocol** | Winners must stay silent or suffer cosmic consequences |
| **Card Signatures** | Players sign cards at dramatic moments (Love: 9 signatures) |

### The Cursor-Mirror Analysis

**This is the coolest part.** We used [cursor-mirror](../cursor-mirror/) to analyze the AI's own session:

```yaml
Session Overview:
  - Total Events: 1045+
  - Tool Calls: 731
  - Thinking Bubbles Captured: 20
  - Fateful Moments Identified: 4

Phases Detected:
  1. Boot & Initialization (7 min)
  2. First Simulation Runs (22 min)
  3. Artwork Pipeline Creation (77 min)
  4. Mass Image Generation (44 min)
  5. Extended Gameplay (37 min)
  6. Generated Cards System (15 min)
```

**Key finding:** The AI spent 77 minutes (longest phase) developing and debugging the artwork pipeline. It learned from failures, mined generated images for semantic data, and iteratively improved prompts.

---

## Turing Chess

**Simulating the *performance* of chess, not the chess itself.**

> *"We are not simulating chess. We are simulating the performance of chess."*

The moves are fixed (replayed from historical games). What we simulate:

- **Human player**: Inner monologue, body language, micro-expressions
- **Robot player**: LEDs, servo sounds, Grafana dashboards, thermal drama
- **Audience**: Factions (human vs robot supporters), betting pool, squabbling
- **Broadcast**: Howard Cosell sports drama + James Burke historical connections

### Key Innovation: The READ → SIM → WRITE Protocol

```yaml
simulation-protocol:
  name: "READ → SIM → WRITE"
  alias: "The Immutable Stride"
  
  the-stride:
    read: "Load entire previous state"
    sim: "Process one chess move + all reactions"
    write: "Output entire new state (NEW FILE!)"
    
  why: |
    Never EDIT a RUN file. Each RUN is a sacred snapshot.
    Branch from any point. Full history preserved.
    Rhythmic. Relaxing. Reliable.
```

### Plugins

| Plugin | Description |
|--------|-------------|
| **Revolutionary Chess** | When checkmate happens, the game *continues* — pawns reverse direction |
| **Betting Pool** | Quark runs the book; audience members have stakes |
| **Spy Mic** | Capture inner thoughts as they happen |

### Links

- [**Experiment Design**](experiments/turing-chess/EXPERIMENT.md) — Full 1200+ line protocol
- [**Object Model**](experiments/turing-chess/engine/OBJECT-MODEL.yml) — HyperCard-style event system
- [**Revolutionary Chess**](experiments/turing-chess/plugins/revolutionary-chess/) — The post-checkmate revolution

---

## Emo Poker Face

**The original stress test.** Eight characters. One poker table. Five simulation layers.

Tests the hardest problem in character AI: **layer separation**.

```
INTERNAL LAYER → what character thinks (hidden)
EXTERNAL LAYER → what others can observe
OBSERVATION LAYER → characters reading each other (observable only!)
```

**Layer bleed = failure.** If a character "reads" information from another's internal thoughts, the simulation broke.

### Pattern Library

This experiment contributed patterns now used across all experiments:

| Pattern | Description |
|---------|-------------|
| `layered-simulation` | Parallel tracks stay coherent |
| `social-protocol` | Behavioral rules for rituals |
| `observable-signatures` | Consistent tells per state |
| `character-instantiation` | Stable local character cache |
| `behavioral-constraints` | Relationship-based information sharing |
| `failure-mode-catalog` | Common simulation failures and fixes |

---

## The Skill-Snitch Report

This skill was audited by [skill-snitch](../skill-snitch/):

```yaml
verdict: "SYSTEMATIC CHARACTER RESEARCH. APPROVE."

what_it_does:
  - SIMULATE → Generate interactions
  - EVALUATE → Score against rubric
  - ITERATE → Run again with variations
  - ANALYZE → Compare runs, find patterns

risk_level: LOW
reason: "transparent, auditable, git-tracked state evolution"
```

[Full report →](skill-snitch-report.md)

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Experiment** | A reusable simulation template with layers, rubric, scenarios |
| **Run Config** | Specific setup: character binding, model, parameters |
| **Run Output** | Single execution result: narrative, state, evaluation |
| **Layer** | Parallel simulation track (mechanics, internal, external, etc.) |
| **Binding** | Mapping character slots to actual characters |
| **Microworld State** | Evolving world state across rounds and runs |
| **Rubric** | Evaluation criteria for scoring runs |

---

## Why Layers Matter

The interesting test isn't "can the model generate poker dialogue." It's:

- Can characters have **private thoughts** that don't leak?
- Can characters **read each other** using only **observable** information?
- Do **relationships** color interpretation?
- Are **tells consistent** across rounds?

---

## Directory Structure

```
skills/experiment/
├── CARD.yml              # Sniffable interface
├── SKILL.md              # Full protocol  
├── README.md             # You are here
├── skill-snitch-report.md # Security audit
├── patterns/             # Reusable simulation patterns
│   ├── layered-simulation.yml
│   ├── observable-signatures.yml
│   ├── social-protocol.yml
│   └── ...
└── experiments/
    ├── INDEX.yml         # Registry of all experiments
    ├── fluxx-chaos/      # Card game championship
    │   ├── EXPERIMENT.md
    │   ├── engine/       # Modular game engine
    │   ├── cardsets/     # Pluggable card definitions
    │   └── runs/
    │       └── amsterdam-flux/   # THE BIG ONE
    │           ├── RUN-000.yml through RUN-023.yml
    │           ├── artwork/      # 32 AI-generated images
    │           ├── SCORE.md      # Full analysis + roundtable
    │           └── CURSOR-MIRROR-ANALYSIS.md
    ├── turing-chess/     # Chess performance drama
    │   ├── EXPERIMENT.md
    │   ├── engine/
    │   ├── plugins/      # Revolutionary Chess, Betting Pool
    │   └── runs/
    └── emo-poker-face/   # Original layer separation test
```

---

## Files

| File | Purpose |
|------|---------|
| `CARD.yml` | Sniffable interface, methods, k-lines |
| `SKILL.md` | Full protocol, layer definitions, output formats |
| `EXPERIMENT.yml.tmpl` | Template for new experiments |
| `RUN-CONFIG.yml.tmpl` | Template for run configs |
| `RUN-OUTPUT.yml.tmpl` | Structured output template |
| `RUN-OUTPUT.md.tmpl` | Narrative output template |

---

## Quick Start

```bash
# Run an experiment
RUN fluxx-chaos --characters "p1=don,p2=palm,p3=donna,p4=bumblewick" --turns 30

# List experiments  
LIST

# Evaluate a run
EVALUATE experiments/fluxx-chaos/runs/amsterdam-flux/RUN-023.yml

# Analyze patterns
ANALYZE experiments/fluxx-chaos/runs/amsterdam-flux/ --pattern emotional-arc
```

---

## Harper Numbers

Oddball statistics from the Fluxx Championship:

```
The Cookie Constant:
  Total cookie mentions: 271
  Cookie thefts: 14+
  Cookie Insurance uses: 1
  Cookie Insurance triggered: 0 (irony: MAXIMUM)
  Don's cookie win rate: 75%

The Love Metric:
  Love card signatures: 9 (most signed card)
  Times Love was stolen: 7
  Times Love led to victory: 4
  Most devastating signature: "I had to let you go."

The Bumblewick Coefficient:
  Games before first win: 8
  Games in winning streak: 3
  Hot chocolate mentions: 7

The FAFO Token Journey:
  Transfers: 4
  Gloat punishments: 2
  Silent victories: 3
  Ironic reversals: 5+
```

---

## Inherits From

| Skill | What It Provides |
|-------|------------------|
| `simulation` | Core generation capability |
| `evaluator` | Independent assessment |
| `rubric` | Scoring criteria |
| `speed-of-light` | Single-call multi-turn generation |

---

## Uses

| Skill | How |
|-------|-----|
| `character` | Load CHARACTER.yml for bindings |
| `coherence-engine` | Maintain consistency across layers |
| `representation-ethics` | Ethical character simulation |
| `debate` | Multi-perspective analysis |
| `cursor-mirror` | Meta-analysis of session behavior |
| `visualizer` | AI artwork generation |
| `image-mining` | Semantic analysis of generated images |

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Will Wright** | Microworlds (SimCity, The Sims) |
| **Stanford Generative Agents** | Park et al. 2023 |
| **Looney Labs** | Fluxx game mechanics, FAQ wisdom |
| **Alan Turing** | Turing Test, chess as testbed |
| **Improv games** | Character consistency, yes-and |
| **Psychodrama** | Moreno's role-playing for insight |
| **Scientific method** | Hypothesis, experiment, analysis, iteration |

---

## Design Documents

For the full architectural context:

- [**Speed of Light vs Carrier Pigeon**](../../designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) — Why this architecture enables 30-turn runs
- [**MOOLLM for Hackers**](../../designs/MOOLLM-FOR-HACKERS.md) — Quick tour for technical readers
- [**SICP-MOOLLM**](../../designs/SICP-MOOLLM.md) — Teaching MOOLLM like Abelson taught Scheme

---

## The Bottom Line

```yaml
what_we_proved:
  - LLMs can simulate games where rules change mid-play
  - Characters maintain distinct voices across 100+ turns
  - Emergent mechanics arise without being programmed
  - AI can generate and integrate artwork into narratives
  - The READ → SIM → WRITE protocol is rhythmic and reliable

final_score: "94/100 — Grade A-"

invitation: |
  Run your own experiment.
  Fork the Fluxx Championship.
  Create the next emergent mechanic.
  The Cosmic Dealer is waiting.
```

---

*"Run. Score. Vary. Compare. Science applied to narrative simulation."*
