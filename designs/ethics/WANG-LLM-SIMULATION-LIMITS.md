# Wang et al. — LLM Simulation Limitations

**Source:** [Can LLM Simulations Truly Reflect Humanity? A Deep Dive](https://d2jud02ci9yv69.cloudfront.net/2025-04-28-rethinking-llm-simulation-84/blog/rethinking-llm-simulation/)  
**Authors:** Qian Wang (NUS), Zhenheng Tang (HKUST), Bingsheng He (NUS)  
**Venue:** ICLR Blogposts 2025  
**Date:** April 28, 2025

---

## Executive Summary

A critical examination of LLM-based social simulations. While acknowledging cost/scalability advantages, the authors identify fundamental limitations in modeling human psychology, motivation, and diversity. Provides important counterbalance to optimistic findings (cf. Willer).

**Key thesis:** LLMs can't access inner psychological states, lack intrinsic motivation, and reflect training data biases — making them fundamentally limited for simulating *individual* humans, even if useful for aggregate social dynamics.

---

## Core Limitations Identified

### 1. Missing Inner Psychological States

**Problem:** Training data lacks nuanced representations of inner psychological states.

- Humans decide based on rationale + personal psychological state
- LLM training data captures *expressed* thoughts, not *inner* experience
- "Can LLM simulate these states without getting enough data related to them?" (rhetorical — answer is no)

**MOOLLM relevance:**
- CHARACTER.yml can specify personality traits but not *inner experience*
- Our framing-based approach explicitly acknowledges this gap
- Shanahan's "no true voice" supports treating this as feature, not bug

### 2. Missing Life Experiences

**Problem:** Training data lacks comprehensive life histories that shape decision-making.

- Past betrayal → future interaction tendencies
- Childhood experiences → adult personality
- "The vast scope of a human's past living experiences makes them difficult to collect comprehensively"

**MOOLLM relevance:**
- `backstory` in CHARACTER.yml is summary, not lived experience
- RAG/memory systems can add context but not genuine experience
- This is why `TRIBUTE` framing requires explicit acknowledgment of incompleteness

### 3. Same-Model Diversity Problem

**Problem:** Using the same LLM to simulate multiple agents creates false homogeneity.

> "Can a single LLM genuinely simulate diverse psychological profiles?"

- Prompts guide varied behaviors, but core knowledge is unchanged
- "Herd behavior" — multiple agents make identical decisions
- Amplifies market movements rather than creating realistic dynamics

**MOOLLM relevance:**
- Speed-of-light multi-agent simulation faces this directly
- Different temperature/sampling helps but doesn't solve fundamentally
- May need explicit diversity injection or model mixing

### 4. Absence of Human Incentives

**Problem:** LLMs lack intrinsic motivations that drive human behavior.

Human incentive hierarchy (Maslow):
- Survival, financial security
- Social belonging, emotional fulfillment
- Self-actualization

**Three barriers:**
1. **Data collection:** People won't share true incentives; incentives change over time; many are subconscious
2. **Representation:** Hard to model incentive→decision relationships via next-word prediction
3. **Consciousness:** Even with perfect data, LLMs lack the intrinsic drive to *care*

**MOOLLM relevance:**
- We can specify `motivations` in CHARACTER.yml but they're declarative
- No way to make LLM genuinely *want* something
- Shanahan's point: it's roleplay of wanting, not wanting itself

### 5. Training Data Biases

| Bias Type | Description |
|-----------|-------------|
| **Cultural** | English-speaking, Western-centric |
| **Occupational** | Missing manufacturing, agriculture workers |
| **Socioeconomic** | Favors digitally literate, affluent |
| **Gender** | 3-6x more likely to assign stereotypical occupations |
| **Skewed voice** | Internet data = digital population's views |

**MOOLLM relevance:**
- Representation-ethics already addresses this via TRIBUTE framing
- CHARACTER.yml should flag when representing underrepresented groups
- Need explicit bias acknowledgment in simulation outputs

---

## Why Use LLM Simulations Anyway?

Despite limitations, authors argue LLM simulation is still valuable:

| Aspect | Traditional Simulation | LLM-Based Simulation |
|--------|----------------------|---------------------|
| **Cost** | High (10-30 SGD/hour/person) | Low (compute only) |
| **Scalability** | Limited | High |
| **Flexibility** | Rigid, rule-based | Adaptive, emergent |
| **Ethical concerns** | High (real participants) | Lower (no real harm) |
| **Emergent behaviors** | Limited | Can surprise researchers |
| **Interpretability** | High | Moderate |

**Key insight:** LLMs are useful for *exploration* and *hypothesis generation*, not *accurate prediction of individuals*.

---

## CryptoTrade Case Study

Real-world validation using cryptocurrency trading simulation:

### Findings

1. **LLM simulation can't outperform Buy and Hold** — 2% worse in bear market
2. **Inherent factual bias** — prioritizes facts over sentiment signals
3. **Herd behavior** — same-model agents make identical decisions

### Lessons

1. **Hybrid approaches needed** — LLM + human oversight, especially for edge cases
2. **Bias mitigation essential** — factual preference bias distorts decisions
3. **Evaluation metrics unclear** — what if different individuals prefer different strategies?

**MOOLLM relevance:**
- Validates need for human-in-loop in simulation systems
- Herd behavior problem directly relevant to speed-of-light multi-agent
- "Evaluation metrics" problem maps to Lazar's moral sensitivity challenge

---

## Proposed Solutions (from paper)

### 1. Enrich Training Data
- Reflective diaries, first-person narratives
- Personal psychological profiles
- Life experience data

### 2. Improve Agent System Design
- Reward functions that mirror human behavior
- Agent "memories" that persist across interactions
- Emotion-like response functions

### 3. Careful Environment Design
- Social roles, resource scarcity, moral dilemmas
- Trade-offs that force long-term thinking
- RAG for dynamic societal context

### 4. External Knowledge Injection
- Fine-tuning with ethical principles
- Cultural norms and societal rules
- Structured knowledge bases

### 5. Robust Evaluation Metrics
- Alignment with psychological theories
- Diversity of agent responses
- Stability of social systems over time

---

## Implications for MOOLLM

### 1. Framing as Explicit Limitation Acknowledgment

Our approach already positions framing as *setting expectations*, not claiming accuracy:
- `TRIBUTE` frame explicitly acknowledges incompleteness
- `EDUCATION` frame positions as illustration, not prediction
- This paper validates that approach

### 2. Diversity Problem in Speed-of-Light

Multi-agent simulations using single LLM risk herd behavior:
- Consider explicit diversity injection (varied temperatures, personas)
- Consider mixing models for different agent types
- Log and detect convergent behavior as quality signal

### 3. Motivation as Declared, Not Felt

CHARACTER.yml `motivations` are *descriptive*, not *causal*:
- LLM doesn't *want* to achieve goals — it roleplays wanting
- This is fine if acknowledged; problematic if mistaken for genuine motivation
- Supports Shanahan's "roleplay all the way down"

### 4. Bias Acknowledgment Protocol

Should add explicit bias acknowledgment:
- When simulating underrepresented groups
- When training data likely lacks relevant experience
- In research outputs using LLM simulation

### 5. Hybrid Human-LLM Validation

Paper's CryptoTrade finding suggests:
- Pure LLM simulation underperforms in some domains
- Human oversight/intervention improves results
- Maps to our thoughtful-commitment pattern

---

## New K-Lines to Consider

| K-Line | Meaning |
|--------|---------|
| `INNER-STATE-GAP` | LLMs can't access genuine inner psychological states |
| `EXPERIENCE-DEFICIT` | Training data lacks lived experience depth |
| `SAME-MODEL-HERD` | Single-model multi-agent creates false homogeneity |
| `MOTIVATION-ROLEPLAY` | Declared motivations are performed, not felt |
| `BIAS-AMPLIFICATION` | Training biases amplify in simulation outputs |

---

## Tension with Willer Research

| Dimension | Willer (2025) | Wang et al. (2025) |
|-----------|---------------|-------------------|
| **Accuracy claim** | 85% correlation with human survey responses | Can't outperform simple baselines |
| **Domain** | Survey/experimental responses | Market behavior, social dynamics |
| **Individual vs. aggregate** | Aggregate patterns | Individual agent behavior |
| **Conclusion** | "Genuinely simulating" | "Cannot truly reflect" |

**Resolution:** Both can be true:
- LLMs capture *statistical patterns* in human responses (Willer)
- LLMs fail at *individual psychological depth* (Wang)
- Aggregate accuracy ≠ individual fidelity

**MOOLLM implication:** Use LLM simulation for exploration and aggregate patterns, not for predicting specific individual behavior.

---

## Connection to Other Ethics Docs

| Document | Connection |
|----------|------------|
| [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Counterpoint — aggregate vs. individual accuracy |
| [SHANAHAN-ROLEPLAY-FRAMING.md](./SHANAHAN-ROLEPLAY-FRAMING.md) | Philosophical support — "no true voice" explains limitation |
| [LAZAR-ETHICAL-COMPETENCE.md](./LAZAR-ETHICAL-COMPETENCE.md) | Evaluation challenge — what metrics for simulation quality? |

---

## Actionable Items for MOOLLM

### Documentation Updates
- [ ] **wang-limitation-ack**: Add limitation acknowledgment section to representation-ethics
- [ ] **diversity-injection**: Document herd behavior risk in speed-of-light
- [ ] **motivation-roleplay**: Clarify motivation-as-declared in character skill

### Architecture Considerations
- [ ] **multi-model-agents**: Consider model mixing for diverse agent simulation
- [ ] **convergence-detection**: Add herd behavior detection to simulation logging
- [ ] **hybrid-validation**: Document human-in-loop validation pattern

### Example Files
- [ ] **bias-acknowledgment-example**: Create `examples/bias-acknowledgment.yml`
- [ ] **aggregate-vs-individual-example**: Create `examples/aggregate-patterns.yml`

### New K-Lines
- [ ] Add to `representation-ethics/CARD.yml`:
  - `INNER-STATE-GAP` — LLMs can't access genuine inner psychological states
  - `EXPERIENCE-DEFICIT` — Training data lacks lived experience depth
  - `SAME-MODEL-HERD` — Single-model multi-agent creates false homogeneity
  - `MOTIVATION-ROLEPLAY` — Declared motivations are performed, not felt
  - `BIAS-AMPLIFICATION` — Training biases amplify in simulation outputs

### Research Follow-Up
- [ ] **track-simulacra**: Monitor Park et al. Generative Agents follow-up work
- [ ] **personalized-llm**: Investigate personalized LLM approaches (ref 27)
- [ ] **rag-simulation**: Investigate RAG-based simulation enrichment (ref 28)

---

## Four-Talk Synthesis (Updated)

| Dimension | Willer | Shanahan | Lazar | Wang |
|-----------|--------|----------|-------|------|
| **Core finding** | 85% accuracy | Roleplay all the way down | Understanding ≠ behavior | Missing inner states |
| **Key insight** | Simulation works (aggregate) | No true voice | Need scaffolding | Can't simulate individuals |
| **Risk identified** | Dual-use evaluation | Fabrication default | Moral sensitivity gap | Herd behavior, bias |
| **Solution direction** | Qualitative grounding | Performance framing | LLM Modulo verifier | Hybrid human-LLM |

**Combined thesis (revised):** LLMs can accurately simulate *aggregate* moral reasoning patterns (Willer) because they roleplay moral agents (Shanahan), but this understanding doesn't produce moral behavior without scaffolding (Lazar), and fundamentally cannot capture *individual* psychological depth or genuine motivation (Wang). **Use for exploration, not prediction; acknowledge limitations explicitly.**

---

*This document summarizes critical research on LLM simulation limitations. Wang et al. provide important counterbalance to optimistic findings, emphasizing that aggregate pattern-matching ≠ individual psychological fidelity. Directly relevant to how MOOLLM should frame its simulation capabilities and acknowledge inherent limitations.*
