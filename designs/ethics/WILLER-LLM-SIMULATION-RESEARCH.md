# Willer: LLMs Accurately Simulate Human Behavior

**Source:** [Stanford Cyber Policy Center Workshop — Rob Willer, Feb 18, 2025](https://www.youtube.com/watch?v=EkSpNxPvXWU)

**Relevance:** Direct empirical validation of LLM simulation accuracy — raises ethical stakes for representation-ethics.

---

## Executive Summary

Rob Willer (Stanford Sociology, Director of Polarization & Social Change Lab) presented research showing that GPT-4 can predict experimental effect sizes in social science studies with **85% correlation** to actual results. This works even for **unpublished studies**, suggesting LLMs genuinely simulate human behavior rather than retrieving known results.

**Key implication for MOOLLM:** When simulation is this accurate, the ethical framework matters more, not less.

---

## Research Overview

### Project 1: Predicting Experimental Effect Sizes

**Team:** Luke Hewitt (MIT → Stanford postdoc), Aashish Ashok Kumar (Stanford → NYU → Harvard), Isaiah Gazai (Harvard PhD)

**Method:**
- Grabbed 70 nationally representative survey experiments from TESS (Time-sharing Experiments for the Social Sciences)
- Extracted 476 experimental effect sizes from 100,000+ participants
- Prompted GPT-4 to simulate participants with demographic characteristics randomly drawn from GSS
- Compared predicted vs observed effect sizes

**Key findings:**

| Metric | Result |
|--------|--------|
| Overall correlation | **0.85** |
| Direction accuracy | **90%** |
| Unpublished studies | Same accuracy (not retrieval) |

### Accuracy by Model Generation

```
GPT-3     → Low accuracy
GPT-3.5   → Medium accuracy  
GPT-4     → 0.85 correlation
```

Accuracy improves with model capability and appears to be asymptoting toward (but never reaching) 100%.

### Project 2: Individual-Level Prediction

**Method:**
- 1,000 nationally representative participants
- Completed GSS (180 questions), Big Five, 5 economic games, 5 survey experiments
- **Plus:** 2-hour semi-structured AI-administered interviews (adapted from American Voices Project)

**Key findings:**

| Data Source | GSS Prediction Accuracy |
|-------------|------------------------|
| Interview-based agents | **Highest** (approaching ceiling) |
| Demographic-only agents | Lower |
| Self-description persona | Middle |
| Random guessing | Baseline |
| Same person 2 weeks later | **~82%** (effective ceiling) |

**Critical insight:** Qualitative interview data dramatically improves prediction accuracy.

---

## Demographic Bias Assessment

**Prior expectation:** Training data overrepresents white male American speech → should see accuracy gaps.

**Actual findings:**

| Comparison | Accuracy Gap |
|------------|--------------|
| White vs Black participants | Small (white slightly higher) |
| Gender | Negligible |
| Party | Negligible |

**Noah Goodman's explanation:** Models may be "past threshold" — training data exceeds minimum needed for accurate simulation across groups. Interview-based agents further reduce demographic bias (less reliance on stereotypes when you have real information).

---

## Dual-Use Risk Assessment

**Test case:** Anti-vaccine Facebook posts (Jenny Allen, Science 2024)

**Method:**
- 90 anti-vaccine posts with measured effect sizes on vaccine intentions
- Used LLM method to predict which posts would be most effective
- Identified top 5 predicted posts

**Result:** Successfully identified posts with largest negative effect on vaccine intentions.

**Implication:** 
- Guard rails block *generation* of harmful content
- But LLMs can *evaluate* which harmful content is most effective
- "That's almost as bad to a really smart malicious actor"

**Response:** Notified top 3 LLM providers 2 months before publication.

---

## Limitations and Open Questions

### Field Experiments Harder Than Surveys

| Type | Accuracy |
|------|----------|
| Survey experiments | Higher |
| Field experiments | Lower |

**Why:** Harder to convey full context of real-world situations to LLM. Text-based surveys are native to LLMs; "you got a text message while driving" is harder to simulate.

### Social Dynamics Gap (Milgram Problem)

**Concern raised (Sandy):** Milgram experiment — LLM would say "I wouldn't shock someone" but real humans did under social pressure.

**Current status:** Multi-agent interaction research underway (David Brasa, Yona, others) but limited ground-truth datasets exist.

### Interaction Effects

Predicting effects that vary by demographic subgroup is harder (~0.5 correlation vs 0.85 for main effects). Functional form of interactions is tricky.

---

## Applications Highlighted

### Scientific Applications

1. **Pilot testing** — Predict experimental results before running expensive studies
2. **Theory building** — Run "thought experiments" with relatively valid predictions
3. **Power analysis** — Estimate effect sizes for study design

### Intervention Identification (The Funnel)

```
Stage 1: GENERATE ideas (crowdsource, brainstorm)
    ↓
Stage 2: EVALUATE ideas (LLM predictions match expert forecasts)
    ↓
Stage 3: APPLY best ideas (field test, implement)
```

**LLM advantage:** "They don't sleep, they don't get tired. You can test a million ideas."

### Policy Applications

- Office of Evaluation Sciences uses expert forecasts for policy implementation decisions
- LLM predictions match expert forecast accuracy
- Could augment (not replace) expert judgment

---

## Implications for MOOLLM Representation Ethics

### 1. Accuracy Raises Stakes

When LLMs genuinely simulate human behavior (not just retrieve), ethical frameworks matter more:

- **Consent hierarchy** — Simulating real people accurately requires clearer consent
- **Framing** — Performance vs deception distinction becomes critical
- **Recording** — Accurate simulations have higher stakes if recorded/published

### 2. Qualitative Grounding Reduces Stereotyping

Interview-based agents rely less on demographic generalizations. This supports:

- **Self-consent cards** — Let people define themselves
- **Rich character files** — More detail = less stereotyping
- **The Sims lesson** — Player agency and rich context matter

### 3. Dual-Use Evaluation Risk

Current guard rails focus on generation, not evaluation. MOOLLM should consider:

- Can our tools be used to identify most effective harmful content?
- Is "evaluate which approach works best" a capability we want to expose?
- How does skill-snitch apply to this risk?

### 4. Social Dynamics Matter

Isolated simulation misses social pressure effects. For MOOLLM:

- **Speed-of-light multi-agent** — May capture some social dynamics
- **Soul-chat format** — Characters influencing each other
- **Room framing** — Social context shapes behavior

---

## Suggested K-Lines

```yaml
k-lines:
  new:
    - SIMULATION-ACCURACY    # Accuracy increases ethical stakes
    - DUAL-USE-EVALUATION    # Evaluation can be as harmful as generation
    - QUALITATIVE-GROUNDING  # Interviews reduce stereotyping
    - SOCIAL-DYNAMICS-GAP    # Isolated simulation misses pressure effects
    - THRESHOLD-HYPOTHESIS   # Past minimum data, accuracy equalizes
```

---

## Operational Examples

These YAML files operationalize the concepts from this research:

| Example | Willer Concept Applied |
|---------|----------------------|
| [bias-acknowledgment.yml](../../skills/representation-ethics/examples/bias-acknowledgment.yml) | Acknowledging training data limitations |
| [aggregate-patterns.yml](../../skills/representation-ethics/examples/aggregate-patterns.yml) | When 85% aggregate accuracy is appropriate |
| [interview-grounded-character.yml](../../skills/representation-ethics/examples/interview-grounded-character.yml) | Qualitative grounding for individual simulation |
| [herd-behavior-risk.yml](../../skills/representation-ethics/examples/herd-behavior-risk.yml) | Same-model convergence problems |
| [dual-challenge-frame.yml](../../skills/representation-ethics/examples/dual-challenge-frame.yml) | Both LLM + design limits matter |
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | When to trust simulations |

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Skill** | [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) | Core ethical framework |
| **Skill** | [speed-of-light/SKILL.md](../../skills/speed-of-light/SKILL.md) | Multi-agent simulation |
| **Skill** | [character/](../../skills/character/) | Rich character representation |
| **Skill** | [incarnation/](../../skills/incarnation/) | Characters writing their own souls |
| **Design** | [PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md](./PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md) | 85% individual accuracy with interviews |
| **Design** | [WANG-LLM-SIMULATION-LIMITS.md](./WANG-LLM-SIMULATION-LIMITS.md) | Counterpoint — simulation limits |
| **Design** | [HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md](./HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md) | Methodological critique |
| **Character** | [Palm's paper on simulation](../../examples/adventure-4/pub/stage/palm-nook/study/the-inner-state-question.md) | Fictional perspective on validity |

---

## Citation

Willer, R. (2025, February 18). *Leveraging LLMs to Accurately Simulate Human Behavior* [Video]. Stanford Cyber Policy Center Workshop. https://www.youtube.com/watch?v=EkSpNxPvXWU

Related papers (mentioned in talk):
- Hewitt, L., Ashok Kumar, A., et al. — Experimental effect size prediction (forthcoming)
- Park, J., et al. — Individual-level prediction with generative agents (forthcoming)
- Horton, J. — Early LLM simulation validation work
- Allen, J. (2024) — Anti-vaccine Facebook post effects (Science)

---

*This document summarizes external research relevant to MOOLLM's representation ethics framework. The findings validate that LLM simulation is increasingly accurate, which raises rather than lowers the ethical stakes of our work.*
