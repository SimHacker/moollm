# Bertoncini: AI, Ethics, and Cognitive Bias — LLM-Based Synthetic Simulation

**Source:** [AI in Education 2025 — Bertoncini et al.]

**Relevance:** Documents cognitive biases that compound in LLM simulations — automation bias, authority bias, normalization bias. Critical methodological caveat: this is synthetic data, not human behavioral data.

---

## Executive Summary

Bertoncini et al. use ChatGPT to generate synthetic behavioral data to study how cognitive biases affect ethical decision-making in AI-mediated educational environments.

**Critical caveat:** The authors explicitly state this is "proof-of-concept exploratory insights" using "LLM-generated synthetic behavior estimation," not empirical human data.

**Key insight for MOOLLM:** LLM simulations may reflect (and amplify) cognitive biases in their training data — these biases compound across multi-agent simulations.

---

## Methodology Note

> "The reported frequencies and contingency tables were generated via an LLM based on prompts, not an independent agent-based model."

> "This statistical analysis is descriptive for this synthetic dataset only, not inferential for real-world populations."

**What this means:** This is evidence about what ChatGPT produces when asked to simulate cognitive biases — not evidence about actual human behavior. But the *patterns* are still informative for understanding LLM simulation risks.

---

## Key Findings (Within Synthetic Data)

| Scenario | Finding | Primary Biases |
|----------|---------|----------------|
| Academic misconduct | 71% engaged in unethical behavior | Normalization, complacency, rationalization |
| Loss of human agency | 78% relied on AI without scrutiny | Automation, confirmation, technology superiority |
| Biased evaluation | 64% showed biased assessments | Anchoring, availability, representativeness |
| Inequality | 53% perpetuated disparities | Status quo, social confirmation |
| Misinformation | 65% accepted AI misinformation | Authority, projection |
| Homogenization | 68% showed reduced diversity | Conformity, groupthink |

---

## The 15 Cognitive Biases Studied

### Academic Misconduct

| Bias | Frequency | Description |
|------|-----------|-------------|
| Normalization | 38% | "Everyone does it, so it's okay" |
| Complacency | 20% | "The system will catch problems" |
| Rationalization | 13% | "It's for a good reason" |

### Loss of Human Agency

| Bias | Frequency | Description |
|------|-----------|-------------|
| Automation | 51% | Uncritical trust in AI outputs |
| Technology superiority | 19% | "AI knows better than humans" |
| Confirmation | 8% | AI confirms existing beliefs |

### Academic Evaluation

| Bias | Frequency | Description |
|------|-----------|-------------|
| Anchoring | 34% | First information disproportionately weights |
| Availability | 20% | Recent/memorable examples dominate |
| Representativeness | 10% | Stereotypes override base rates |

### Inequality

| Bias | Frequency | Description |
|------|-----------|-------------|
| Status quo | 33% | Prefer existing arrangements |
| Social confirmation | 20% | Defer to group consensus |

### Misinformation

| Bias | Frequency | Description |
|------|-----------|-------------|
| Authority | 40% | Trust AI because it's AI |
| Projection | 25% | Assume AI shares human values |

### Homogenization

| Bias | Frequency | Description |
|------|-----------|-------------|
| Conformity | 38% | Match dominant viewpoint |
| Groupthink | 30% | Suppress dissent for consensus |

---

## MOOLLM Implications

### For Users

| Bertoncini Finding | User Risk |
|-------------------|-----------|
| Normalization bias | May normalize ethically problematic simulations |
| Automation bias | May uncritically accept AI-generated character behavior |
| Authority bias | May over-trust AI judgments about ethics |

### For Multi-Agent Simulations

| Bertoncini Finding | Simulation Risk |
|-------------------|----------------|
| Conformity/groupthink | Multi-agent simulations risk homogenization |
| Same-model bias | All agents share the same training biases |
| Synthetic data limits | Can't discover new behavioral facts |

### Mitigation Strategies

```yaml
bias_mitigation:
  for_users:
    - "Explicit bias acknowledgment in outputs"
    - "Encourage critical evaluation"
    - "Don't claim authority"
    
  for_simulations:
    - "Diverse value injection (Schwartz)"
    - "Herd behavior detection"
    - "Model diversity when possible"
    - "Explicit limitations in metadata"
```

---

## K-Lines

This paper contributes these traditions to MOOLLM:

```yaml
k-lines:
  - NORMALIZATION-BIAS       # Widespread use makes unethical seem normal
  - AUTOMATION-BIAS          # Uncritical trust in AI outputs
  - AUTHORITY-BIAS-AI        # Trusting AI simply because it's AI
  - CONFORMITY-HOMOGENIZATION # AI reinforces dominant viewpoints
  - SYNTHETIC-DATA-CAVEAT    # LLM-generated data ≠ human behavioral data
  - BIAS-COMPOUNDING         # Biases compound across simulation
```

---

## Operational Examples

| Example | Bertoncini Concept Applied |
|---------|---------------------------|
| [bias-acknowledgment.yml](../../skills/representation-ethics/examples/bias-acknowledgment.yml) | Explicit bias disclosure |
| [herd-behavior-risk.yml](../../skills/representation-ethics/examples/herd-behavior-risk.yml) | Conformity/groupthink risk |
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | Synthetic data limitations |
| [autonomy-spectrum.yml](../../skills/representation-ethics/examples/autonomy-spectrum.yml) | Controlling automation bias |

---

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Design** | [HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md](./HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md) | Methodological critique |
| **Design** | [WANG-LLM-SIMULATION-LIMITS.md](./WANG-LLM-SIMULATION-LIMITS.md) | Bias amplification |
| **Design** | [XIE-LLM-TRUST-BEHAVIOR.md](./XIE-LLM-TRUST-BEHAVIOR.md) | Demographic bias in trust |
| **Skill** | [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) | Bias protocols |

---

## Citation

Bertoncini, C., et al. (2025). "AI, Ethics, and Cognitive Bias: An LLM-Based Synthetic Simulation." AI in Education 2025.

---

*This document summarizes research on cognitive bias in LLM simulations. The synthetic data methodology is a limitation, but the bias patterns identified are valuable for understanding risks in MOOLLM multi-agent simulations.*

*Document created: 2026-01-23*
