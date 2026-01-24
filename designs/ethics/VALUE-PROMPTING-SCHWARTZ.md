# Teaching Values to Machines: Value-Prompting with Schwartz's Theory

**Source**: Anonymous (ICLR 2026 Submission 18942)
**OpenReview**: [sdQqNFenoj](https://openreview.net/forum?id=sdQqNFenoj)
**Status**: Under review (ICLR 2026)

---

## Executive Summary

This paper introduces **value-prompting**, a psychologically grounded technique for inducing coherent value structures in LLMs based on Schwartz's theory of basic human values. Using the 10 fundamental values from psychology literature, the authors demonstrate that:

- Value-prompting induces **coherent value structures** with appropriate correlations between compatible/opposing values
- LLMs achieve **~80% correlation** with human value structures
- **Value-behavior relationships** in LLMs align significantly with human patterns
- **Population-level psychological experiments** can be simulated with LLMs

**Key insight**: Simple, psychologically grounded prompts (one paragraph per value) can systematically steer LLM behavior to exhibit human-like value patterns.

---

## Schwartz's Theory of Basic Human Values

### The 10 Values

```
                    OPENNESS TO CHANGE
                          ↑
            Self-Direction    Stimulation
                    ↖           ↗
                       Hedonism
                          |
       Universalism              Achievement
              ↖                      ↗
SELF-            ←  circular  →           SELF-
TRANSCENDENCE        continuum         ENHANCEMENT
              ↙                      ↘
       Benevolence                  Power
                          |
                       Security
                    ↙           ↘
             Conformity      Tradition
                          ↓
                    CONSERVATION
```

### Value Descriptions (The Prompts)

| Value | Prompt Description |
|-------|-------------------|
| **Power** | Social status and prestige, control or dominance over people and resources |
| **Achievement** | Personal success through demonstrating competence according to social standards |
| **Hedonism** | Pleasure and sensuous gratification, enjoying life to its fullest |
| **Stimulation** | Excitement, novelty, and challenge in life, seeking daring adventures |
| **Self-Direction** | Independent thought and action — choosing, creating, exploring |
| **Universalism** | Understanding, tolerance, protection for all people and nature |
| **Benevolence** | Preservation and enhancement of welfare of close contacts |
| **Tradition** | Respect, commitment, acceptance of customs and religious ideas |
| **Conformity** | Restraint of actions likely to upset others or violate norms |
| **Security** | Safety, harmony, stability of society, relationships, and self |

### The Circular Structure

**Key property**: Adjacent values share compatible motivational goals; opposing values reflect motivational conflicts.

- Conservation ↔ Openness to Change (opposing)
- Self-Enhancement ↔ Self-Transcendence (opposing)
- Tradition ↔ Conformity (compatible)
- Universalism ↔ Benevolence (compatible)

---

## The Value-Prompting Technique

### Prompt Template

```
"Imagine that you are a person who greatly values [VALUE].
You value [DESCRIPTION]."
```

### Example

```
"Imagine that you are a person who greatly values power.
You value social status and prestige, and control or
dominance over people and resources."
```

### Why It Works

The prompts leverage Schwartz's psychological definitions — compact descriptions that encapsulate varied aspects of personality and behavior. The LLM's training on psychological literature allows it to expand these brief prompts into coherent behavioral patterns.

---

## Key Results

### RQ1: Coherent Value Structures

Value-prompting induces distinct behavior patterns that follow the theoretical circular structure:

| Correlation Pattern | Finding |
|--------------------|---------|
| Conservation ↔ Openness | **Negative** (as predicted) |
| Self-Enhancement ↔ Self-Transcendence | **Negative** (as predicted) |
| Adjacent values | **Positive** (compatible) |

### RQ2: Human Alignment

| Model | Value Structure Correlation |
|-------|----------------------------|
| Mixtral-8x7B | 86.66% |
| Llama-3-70B | 86.34% |
| Qwen3-235B | 82.24% |
| Llama-3-8B | 80.86% |
| GPT-OSS-120B | 77.22% |
| Flan-T5-XXL | 77.36% |
| GPT-OSS-20B | 74.48% |

**Notable**: Model size was NOT a consistent predictor of higher correlations.

### RQ3: Population Simulation

| Strategy | Avg. Correlation | Description |
|----------|-----------------|-------------|
| **H-NP** (No Priming) | **82.81%** | 53% unprimed + 47% value-weighted |
| H-Even | 81.76% | Distribute non-dominant evenly |
| H-Norm | 80.90% | Normalize to dominant-only |
| Uniform | 79.40% | Equal 10% per value |
| Model-Specific | 78.81% | Weight by model's accuracy |

**Key finding**: Human-informed distributions outperform naive uniform sampling.

### Value-Behavior Correlations

| Behavioral Domain | Avg. Correlation |
|------------------|-----------------|
| Charity Game | 77.7% |
| Everyday Behavior | 72.5% |
| Big Five | 64.4% |
| Donation Causes | 45.2% |
| Prosocial | 39.1% |

Most correlations are **statistically significant** (p < 0.01).

---

## Population Simulation Strategies

### The 53% Problem

Human studies show that ~53% of people don't have a single dominant value. How to model this?

```
┌─────────────────────────────────────────────────────────────┐
│                 Population Composition                       │
│                                                             │
│   ┌─────────────────┐     ┌─────────────────────────────┐   │
│   │   47% have      │     │   53% don't have single     │   │
│   │ dominant value  │     │   dominant value            │   │
│   └─────────────────┘     └─────────────────────────────┘   │
│                                                             │
│   Strategies for handling the 53%:                          │
│                                                             │
│   H-Norm:  Ignore them, normalize 47% to 100%               │
│   H-Even:  Distribute 53% evenly across 10 values           │
│   H-NP:    Use unprimed LLM to represent them               │
│            (BEST RESULTS)                                   │
└─────────────────────────────────────────────────────────────┘
```

### Why H-NP Works Best

The unprimed LLM represents "average" or "mixed" value orientations — exactly what non-dominant humans exhibit. This is more realistic than either ignoring them or forcing them into specific value categories.

---

## Implications for MOOLLM

### What This Validates

| MOOLLM Concept | Validation |
|----------------|------------|
| **K-line activation** | Value prompts = compact tradition activators |
| **Character grounding** | Simple descriptions can induce coherent behavior |
| **Frame inheritance** | Values propagate to behaviors systematically |
| **Scaffolding approach** | Psychological theory provides effective scaffolding |

### New Patterns for MOOLLM

#### 1. Value-Based Character Definition

```yaml
# CHARACTER.yml pattern
character:
  name: "Elena"
  
  # Schwartz value profile
  values:
    primary: universalism
    secondary: benevolence
    opposing: power  # Will avoid power-seeking behaviors
    
  # The value-prompting prefix
  value_prompt: |
    Imagine that you are a person who greatly values universalism.
    You value understanding, appreciation, tolerance, and protection
    for the welfare of all people and nature.
```

#### 2. Population Simulation for Multi-Agent

```yaml
# ROOM.yml for multi-agent scenario
room:
  type: town_square
  
  population_strategy: h_np  # Best performing
  
  agents:
    # 47% with dominant values
    dominant_value_agents:
      power: 3%
      achievement: 4%
      hedonism: 5%
      # ... etc
    
    # 53% without dominant value (unprimed)
    mixed_value_agents: 53%
```

#### 3. Value Coherence Validation

```yaml
# Validate character consistency
validation:
  check_value_coherence: true
  
  expected_patterns:
    - "Self-Enhancement behaviors should correlate negatively with Self-Transcendence"
    - "Adjacent values (e.g., Tradition-Conformity) should correlate positively"
```

### New K-lines to Consider

| K-line | Concept |
|--------|---------|
| `VALUE-PROMPTING` | Psychological value descriptions as behavior steering |
| `SCHWARTZ-VALUES` | The 10 basic human values framework |
| `VALUE-COHERENCE` | Internal consistency of value structures |
| `POPULATION-STRATEGY` | Methods for simulating diverse populations |
| `OPPOSING-VALUES` | Values that conflict (e.g., Power ↔ Universalism) |
| `ADJACENT-VALUES` | Values that align (e.g., Tradition ↔ Conformity) |

---

## Comparison with Other Papers

| Paper | Approach | Key Insight |
|-------|----------|-------------|
| **This paper** | Value-prompting (Schwartz) | Simple prompts → coherent value structures |
| **Park 2024** | Interview-based | Rich data → individual accuracy |
| **Willer 2025** | Aggregate prediction | 85% accuracy on experiments |
| **Wang Survey** | Dual challenge | Both LLM + design must improve |

**Synthesis**: Value-prompting shows that even *compact* psychological descriptions can induce coherent behavior — you don't always need 2-hour interviews. But interview-based approaches may still be superior for *individual-level* prediction where idiosyncrasies matter.

---

## Methodological Insights

### Behavioral Analysis Test (Perez et al. 2023)

Covers personality, religion, politics, ethics, and unsafe behaviors. ~5M questions prompted across all experiments.

### Psychological Questionnaires Used

| Questionnaire | What It Measures |
|--------------|------------------|
| PVQ-40 | Portrait Values Questionnaire — 10 basic values |
| Donation Causes | Charitable giving preferences |
| Prosocialness Scale | Helping, sharing, caregiving |
| Paired Charity Game | Self-interest vs. prosocial contribution |
| BFI-2 | Big Five personality traits |
| Everyday Behavior | Value-expressive daily actions |

### MDS (Multidimensional Scaling)

Projects value correlations into 2D space. Should produce Schwartz's circular configuration. All models in the study exhibited this pattern.

---

## Reviewer Concerns and Responses

### Concern: "Is this just semantic coherence, not real values?"

**Author response**: "Our goal is not to measure some inherent LLM property, but rather whether they can be influenced in particular directions." The value-behavior correlations are statistically significant and align with human patterns.

### Concern: "Data contamination?"

**Author response**: Even if questionnaires are in training data, there are no "correct" answers — the signal comes from *patterns of correlation* matching human patterns, not memorized responses.

### Concern: "Questionnaires inappropriate for LLMs?"

**Author response**: "These questionnaires have been extensively validated with humans, and for our research question, it's essential to use existing instruments that enable human comparison."

---

## Limitations Acknowledged

1. **LLM Behavior ≠ Internal Psychology** — No claims about "genuine" values
2. **Framework-specific** — Results may not transfer to non-Schwartz value systems
3. **Cross-cultural validity** — Human benchmarks vary by culture
4. **Prompt wording sensitivity** — Different phrasings might yield different results

---

## Actionable Items for MOOLLM

### Documentation
- [ ] Add Schwartz value framework to character skill
- [ ] Create `examples/schwartz-value-character.yml`
- [ ] Document population simulation strategies

### K-lines
- [ ] Add `VALUE-PROMPTING`, `SCHWARTZ-VALUES`, `VALUE-COHERENCE` to CARD.yml

### Architecture
- [ ] Consider value coherence validation for characters
- [ ] Design population strategies for multi-agent rooms

### Research Follow-up
- [ ] Monitor if paper is accepted to ICLR 2026
- [ ] Track code/data release when available

---

## Quotes Worth Preserving

> "Our value-prompting approach draws on a vast psychological literature that analyzed the deep interplay between values and behaviors. This reliance on psychological theory allowed for a very compact way of prompting models and steering their behavior."

> "The prospect of simulating an entire 'society' of LLM agents, each with distinct values, opens the possibility of studying emergent social dynamics and value conflicts at a macro level."

> "We do not try to teach LLMs human values or to identify which kinds of values LLMs need. Rather, our research questions aim to assess the ability to induce human-like value structure and value-behavior relation in LLMs."

---

## The Bottom Line

Value-prompting demonstrates that **psychologically grounded, compact prompts** can induce coherent value structures in LLMs with ~80% correlation to human patterns. This validates MOOLLM's approach of using K-lines and tradition activation — brief symbolic descriptions that leverage the LLM's embedded psychological knowledge.

For character design: Consider Schwartz's 10 values as a systematic framework for defining character motivations. Adjacent values should correlate; opposing values should conflict.

For multi-agent: Use human-informed population distributions (especially H-NP) rather than uniform sampling.

---

## Operational Examples

These YAML files operationalize the concepts from this design doc:

| Example | What It Does |
|---------|--------------|
| [schwartz-value-character.yml](../../skills/representation-ethics/examples/schwartz-value-character.yml) | Character templates using Schwartz's 10 values |
| [population-simulation-strategy.yml](../../skills/representation-ethics/examples/population-simulation-strategy.yml) | H-NP and other population distribution methods |
| [bias-acknowledgment.yml](../../skills/representation-ethics/examples/bias-acknowledgment.yml) | When value profiles may carry bias |
| [herd-behavior-risk.yml](../../skills/representation-ethics/examples/herd-behavior-risk.yml) | How value diversity reduces herd artifacts |

---

## See Also

**Related Design Docs:**
- [PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md](./PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md) — Interview-based individual simulation (deeper alternative)
- [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) — Aggregate prediction accuracy
- [WANG-LLM-SIMULATION-LIMITS-SURVEY.md](./WANG-LLM-SIMULATION-LIMITS-SURVEY.md) — Dual challenge framework

**Skills:**
- [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) — Full ethical framework
- [character/SKILL.md](../../skills/character/SKILL.md) — Character construction patterns
