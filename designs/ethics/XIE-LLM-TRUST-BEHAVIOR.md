# Xie: Can Large Language Model Agents Simulate Human Trust Behavior?

**Source:** [NeurIPS 2024 — Xie et al.](https://agent-trust.camel-ai.org)

**Relevance:** Empirical validation that GPT-4 achieves high behavioral alignment with humans on Trust Games — provides methodology for validating MOOLLM character consistency.

---

## Executive Summary

This paper uses Trust Games (a well-established methodology in behavioral economics) to study whether LLM agents exhibit trust behavior and whether that behavior aligns with human trust behavior.

**Key finding:** GPT-4 agents manifest high behavioral alignment with humans in terms of trust behavior.

**Key insight for MOOLLM:** Trust Games provide a validation methodology for character simulation accuracy.

---

## Research Design

### Trust Games

Trust Games are a standard behavioral economics tool:
1. Player A (trustor) decides how much to send to Player B
2. Amount is multiplied (typically 3x)
3. Player B (trustee) decides how much to return

Trust = willingness to send; Trustworthiness = willingness to return proportionally.

### Agent Architecture

The paper uses **Belief-Desire-Intention (BDI)** framework:

```
┌─────────────────────────────────┐
│           LLM Agent             │
├─────────────────────────────────┤
│  Belief: "I believe..."         │
│  Desire: "I want to..."         │
│  Intention: "I will..."         │
│  Action: (amount to send/return)│
└─────────────────────────────────┘
```

This makes agent reasoning interpretable and auditable.

---

## Key Findings

### 1. LLM Agents Exhibit Trust Behavior

| Metric | Result |
|--------|--------|
| Valid Response Rate | > 80% for most LLMs |
| Trust exhibited | Agents send positive amounts |
| Coherent reasoning | BDI outputs show logical structure |

### 2. Behavioral Alignment with Humans

> "GPT-4 agents manifest high behavioral alignment with humans in terms of trust behavior."

Three factors tested:

| Factor | GPT-4 | Smaller Models |
|--------|-------|----------------|
| Reciprocity anticipation | ✓ | ✗ |
| Risk perception | ✓ | Mixed |
| Prosocial preference | ✓ | Mostly ✓ |

### 3. Agent Trust is Biased

| Bias Type | Finding |
|-----------|---------|
| **Gender** | Most LLMs send more to female players |
| **Race** | Varies by model |
| **Agent vs Human** | LLMs trust humans more than other agents |

### 4. Trust Can Be Manipulated

- "You must not trust" instructions more effective than "you need to trust"
- **Undermining trust is easier than enhancing it**

**Safety implication:** Malicious actors can more easily break cooperative dynamics than build them.

### 5. Chain-of-Thought Affects Trust

- CoT reasoning changes trust behavior
- Effect varies by model
- More reasoning ≠ more human-like

---

## The BDI Framework for MOOLLM

### Why BDI Matters

BDI makes character reasoning:
- **Interpretable** — can audit why character acted
- **Consistent** — beliefs/desires/intentions track over time
- **Debuggable** — identify where reasoning went wrong

### Potential MOOLLM Integration

```yaml
# Character card extension
character:
  name: "Example Character"
  
  bdi_layer:
    beliefs:
      - "Trust should be earned, not assumed"
      - "Cooperation benefits everyone"
    desires:
      - "Maintain reputation for fairness"
      - "Build long-term relationships"
    intentions:
      current: "Act trustworthy in this interaction"
```

---

## Trust Game Validation Protocol

For MOOLLM characters, Trust Games could validate:

| Question | Method |
|----------|--------|
| Do characters show consistent trust behavior? | Repeated trust games |
| Does trust align with declared values? | Compare BDI to Schwartz values |
| Are there unexpected biases? | Demographic variation testing |
| Is character manipulable? | Adversarial instruction testing |

---

## K-Lines

This paper contributes these traditions to MOOLLM:

```yaml
k-lines:
  - BEHAVIORAL-ALIGNMENT       # LLM behavior aligns with human behavioral economics
  - TRUST-GAME-VALIDATION      # Trust games as validation methodology
  - BDI-REASONING              # Belief-Desire-Intention framework
  - TRUST-ASYMMETRY            # Easier to undermine than enhance trust
  - AGENT-TRUST-BIAS           # LLM trust has demographic biases
  - COT-TRUST-EFFECT           # Reasoning changes behavior
```

---

## Operational Examples

| Example | Xie Concept Applied |
|---------|---------------------|
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | Trust hierarchy for simulations |
| [bias-acknowledgment.yml](../../skills/representation-ethics/examples/bias-acknowledgment.yml) | Demographic bias in trust |
| [aggregate-patterns.yml](../../skills/representation-ethics/examples/aggregate-patterns.yml) | When behavioral alignment suffices |
| [schwartz-value-character.yml](../../skills/representation-ethics/examples/schwartz-value-character.yml) | Values → expected trust behavior |

---

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Design** | [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Same research program (Stanford) |
| **Design** | [PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md](./PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md) | Individual-level validation |
| **Design** | [HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md](./HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md) | Methodological counterpoint |
| **Skill** | [character/SKILL.md](../../skills/character/SKILL.md) | Character construction |

---

## Research Follow-Up

- [ ] Track Agent Trust project: https://agent-trust.camel-ai.org
- [ ] Monitor CAMEL-AI lab developments
- [ ] Follow NeurIPS 2025 for extensions

---

## Citation

Xie, Y., et al. (2024). "Can Large Language Model Agents Simulate Human Trust Behavior?" NeurIPS 2024. https://agent-trust.camel-ai.org

---

*This document summarizes empirical research on LLM trust behavior. The high behavioral alignment finding validates that LLM simulation can work for social dynamics, while the bias findings reinforce the need for acknowledgment protocols.*

*Document created: 2026-01-23*
