# Experiment Skill

🧪 **Simulation + Evaluation + Iteration + Analysis**

## What Is This?

An experiment combines four activities into systematic practice:

| Activity | What It Does | Methods |
|----------|--------------|---------|
| **SIMULATE** | Generate character interactions | `RUN`, `SIMULATE` |
| **EVALUATE** | Score against rubric criteria | `EVALUATE`, `SCORE` |
| **ITERATE** | Run again with variations | `RERUN`, `VARY`, `REPLAY` |
| **ANALYZE** | Compare runs, find patterns | `COMPARE`, `ANALYZE`, `REPORT` |

**Key insight:** Separate the experiment (stable) from the config (setup) from the output (result). This allows systematic comparison across models, characters, and parameters.

## Quick Start

```bash
# Run an experiment
RUN emo-poker-face --characters "host=don,p1=palm,p2=donna" --output both

# List experiments
LIST

# Evaluate a run
EVALUATE runs/whacky-eight-001.yml
```

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

## Why Layers Matter

The interesting test isn't "can the model generate poker dialogue." It's:

- Can characters have **private thoughts** that don't leak?
- Can characters **read each other** using only **observable** information?
- Do **relationships** color interpretation?
- Are **tells consistent** across rounds?

```
INTERNAL LAYER → what character thinks (hidden)
EXTERNAL LAYER → what others can observe
OBSERVATION LAYER → characters reading each other (observable only!)
```

**Layer bleed** = failure. If a character "reads" information from another's internal thoughts, the simulation broke.

## Directory Structure

```
skills/experiment/
├── CARD.yml              # Sniffable interface
├── SKILL.md              # Full protocol  
├── README.md             # You are here
├── EXPERIMENT.yml.tmpl   # Template for new experiments
├── RUN-CONFIG.yml.tmpl   # Template for run configs
├── RUN-OUTPUT.yml.tmpl   # Structured output template
├── RUN-OUTPUT.md.tmpl    # Narrative output template
└── experiments/
    ├── INDEX.yml
    └── emo-poker-face/
        ├── EXPERIMENT.md       # Definition
        ├── RELATIONSHIPS.yml   # Local character cache
        ├── state/
        │   └── INITIAL.yml     # Starting microworld state
        └── runs/
            ├── INDEX.yml
            ├── whacky-eight.yml    # Full 8-player config
            └── minimal-three.yml   # Quick test config
```

## First Experiment: Emotional Poker Face

Eight characters. One poker table. Five simulation layers.

**The stress test:** Run parallel simulations of game mechanics, internal thought, external expression, observation, and relationship history — all coherent, all separate.

See: `experiments/emo-poker-face/EXPERIMENT.md`

---

## 🎴 Featured: Amsterdam Flux — Card Artwork Pipeline

**AI characters playing Fluxx while an AI generates and refines card artwork.**

This experiment demonstrates the full loop: characters play a card game → game state drives art generation → autonomous quality control → iterative refinement → comprehensive documentation.

### The Slideshow

**[📖 View Card Gallery →](experiments/fluxx-chaos/runs/amsterdam-flux/artwork/SLIDESHOW.md)**

32 cards, each with:
- **Pure artwork** — no text, no UI, no frames
- **Stereo prompts** — YAML structure + evocative prose
- **Image mining** — computer vision analysis of what the AI generated
- **Generation history** — failures documented, lessons learned

### Why It's Interesting

| Achievement | What Happened |
|-------------|---------------|
| **72% first-attempt success** | Most prompts worked immediately |
| **28% required iteration** | Failures taught us prompt engineering |
| **Autonomous regeneration** | AI detected issues, rewrote prompts, tried again |
| **Failure pattern recognition** | "board game card art" → triggers UI overlays |
| **Documented learning** | Each failure became a lesson in `*-mined.yml` |

### Quick Links

- [**Card Gallery Slideshow**](experiments/fluxx-chaos/runs/amsterdam-flux/artwork/SLIDESHOW.md) — Full visual tour
- [Artwork README](experiments/fluxx-chaos/runs/amsterdam-flux/artwork/README.md) — Quick reference + thumbnails
- [Pipeline Protocol](experiments/fluxx-chaos/runs/amsterdam-flux/artwork/ARTWORK.md) — How the stereo prompts work
- [Game Runs](experiments/fluxx-chaos/runs/amsterdam-flux/) — 15+ game simulation runs with narrative
- [Prompt Engineering Analysis](experiments/fluxx-chaos/runs/amsterdam-flux/artwork/SLIDESHOW.md#analysis-failed-generations--prompt-engineering-lessons) — What works, what doesn't

## Microworld State

Experiments track evolving state. Three models:

| Model | Description | Use When |
|-------|-------------|----------|
| `shadow_tree` | Prototype + overrides | Most runs (small diffs) |
| `copy_and_edit` | Full snapshot, modified in place | Complex state changes |
| `append_only` | Prototype + event log | Audit trail / replay needed |

Runs can chain: final state of run N → initial state of run N+1.

## Files

| File | Purpose |
|------|---------|
| `CARD.yml` | Sniffable interface, methods, k-lines |
| `SKILL.md` | Full protocol, layer definitions, output formats |
| `EXPERIMENT.yml.tmpl` | Template for new experiments |
| `RUN-CONFIG.yml.tmpl` | Template for run configs |
| `RUN-OUTPUT.yml.tmpl` | Structured output template |
| `RUN-OUTPUT.md.tmpl` | Narrative output template |

## Inherits From

| Skill | What It Provides |
|-------|------------------|
| `simulation` | Core generation capability |
| `evaluator` | Independent assessment |
| `rubric` | Scoring criteria |
| `speed-of-light` | Single-call multi-turn generation |

## Uses

| Skill | How |
|-------|-----|
| `character` | Load CHARACTER.yml for bindings |
| `coherence-engine` | Maintain consistency across layers |
| `representation-ethics` | Ethical character simulation |
| `debate` | Multi-perspective analysis |

## Lineage

- **Will Wright microworlds** — SimCity, The Sims
- **Stanford Generative Agents** — Park et al. 2023
- **Improv games** — character consistency, yes-and
- **Psychodrama** — Moreno's role-playing for insight
- **Scientific method** — hypothesis, experiment, analysis, iteration
