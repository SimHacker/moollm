# Hullman: Is Behavior-Generative AI Epistemically Problematic?

**Source:** [Columbia Data Science Blog — Jessica Hullman, 2025](https://statmodeling.stat.columbia.edu/)

**Relevance:** Critical methodological perspective — LLMs for exploration, not substitution. Directly informs MOOLLM's "methodological humility" stance.

---

## Executive Summary

Jessica Hullman (Northwestern → Columbia) offers a critical perspective on using LLMs to simulate human behavior for social science research. Her key argument:

> **"LLMs may be useful for exploration but should not substitute for human participants when discovering new facts."**

**Key insight for MOOLLM:** Speed-of-Light multi-agent simulations are for brainstorming and prototyping, not prediction or discovery.

---

## The Fundamental Problem

> "How do you discover new facts about the cognitive or social world until you've attempted to understand how generative models align with human behavior for those research questions?"

The circularity:
1. To validate LLM simulation, you need human data
2. If you have human data, why do you need the simulation?
3. To discover new facts, you need confidence in the simulation
4. But confidence requires prior validation... which requires human data

**Conclusion:** LLMs can *replicate* known effects but cannot *discover* new ones.

---

## Bias Compounding

> "Similar to how having a huge sample size doesn't necessarily give you better estimates in behavioral science when there's selection bias operating, the fact that LLM simulation results often differ in some ways—and in particular, tend to produce more 'extreme' results than humans—leaves the risk that we mislead ourselves."

### LLM Bias Patterns

| Bias Type | Effect |
|-----------|--------|
| **Lower variance** | Less diversity than human populations |
| **More pronounced stereotypes** | Training data biases amplify |
| **Reduced individuality** | Homogenization toward "average" |
| **Extreme results** | More polarized than human responses |

### Why This Matters for MOOLLM

Multi-agent simulations compound these biases:
- All agents share training biases → convergent behavior
- Herd behavior emerges from shared priors
- "Diversity" is surface-level, not deep

---

## When LLMs Work

| Use Case | Why It Works |
|----------|--------------|
| Replicating average treatment effects | LLMs capture central tendencies |
| Constant effects | Less heterogeneity to model |
| Representative samples | Training data roughly matches |
| Effect size correlation | "Impressionistic summary" is accurate |

**The key:** LLMs work for *aggregate* patterns in *known* domains.

---

## When LLMs Don't Work

| Use Case | Why It Fails |
|----------|--------------|
| Heterogeneous effects | LLMs flatten diversity |
| Particular subgroups | Training data underrepresents |
| New scenarios | No data to extrapolate from |
| Individual prediction | Idiosyncrasies lost |

**The key:** LLMs fail for *individual* variation in *novel* contexts.

---

## The Promise: Exploratory Theory Building

> "LLMs can play the role of economic models, where before conducting experiments you use them to understand the space of possible effects under particular assumptions about behavior."

### Valid Use Cases

| Use Case | Example |
|----------|---------|
| Brainstorm scenarios | "What might happen if...?" |
| Sample size calculations | "How many participants needed?" |
| Pilot testing | "Does this instruction make sense?" |
| Hypothesis generation | "What covariates might matter?" |
| Stress testing | "What could go wrong?" |

### Invalid Use Cases

| Use Case | Why Invalid |
|----------|-------------|
| Discovering new facts | No validation possible |
| Claims about real people | Stereotypes, not individuals |
| Policy recommendations | Biases compound |
| Replacing human participants | Circular validation |

---

## The Replication Problem

> "I'm not very enthusiastic about [using LLMs for replication prioritization] either, given the shaky foundations of replication as a hallmark of good science."

Even "replication" is problematic:
- What does "valid replication" mean with LLMs?
- Is matching past results evidence of accuracy or retrieval?
- Prompt sensitivity creates reproducibility issues

---

## Critical Questions Raised

| Question | Implication |
|----------|-------------|
| Do we need agent self-consistency? | Internal consistency ≠ accuracy |
| Is "explain behavior" meaningful? | Post-hoc rationalization risk |
| How handle prompt sensitivity? | Results depend on phrasing |
| What is "valid replication"? | Matching ≠ understanding |

---

## MOOLLM Implications

### Speed-of-Light Simulations

| Hullman Position | MOOLLM Response |
|------------------|-----------------|
| Exploration, not prediction | SOL for brainstorming, not oracle |
| Bias compounding | Diversity injection protocols |
| Extreme results | Calibrated expectations |
| Piloting use case | Prototyping tool, not ground truth |

### Methodological Humility

```yaml
simulation_metadata:
  methodology: "LLM-based exploration"
  validity_scope: "brainstorming and hypothesis generation"
  
  not_valid_for:
    - "discovering new behavioral facts"
    - "claims about specific individuals"
    - "policy recommendations without human validation"
    
  acknowledge:
    - "Biases compound across agents"
    - "Results reflect training data, not ground truth"
    - "Diversity is surface-level"
```

---

## K-Lines

This paper contributes these traditions to MOOLLM:

```yaml
k-lines:
  - EXPLORATION-NOT-SUBSTITUTION  # LLMs for exploration, not replacing humans
  - BIAS-COMPOUNDING              # Biases compound across simulations
  - EXTREME-RESULTS-TENDENCY      # LLMs produce more extreme, less diverse results
  - PILOTING-USE-CASE             # Valid for brainstorming and piloting
  - METHODOLOGICAL-HUMILITY       # Explicit acknowledgment of limitations
  - VALIDATION-CIRCULARITY        # Can't validate what you're trying to discover
```

---

## Operational Examples

| Example | Hullman Concept Applied |
|---------|------------------------|
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | Trust hierarchy |
| [herd-behavior-risk.yml](../../skills/representation-ethics/examples/herd-behavior-risk.yml) | Bias compounding |
| [aggregate-patterns.yml](../../skills/representation-ethics/examples/aggregate-patterns.yml) | When aggregate is valid |
| [bias-acknowledgment.yml](../../skills/representation-ethics/examples/bias-acknowledgment.yml) | Methodological humility |

---

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Design** | [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Optimistic counterpoint |
| **Design** | [XIE-LLM-TRUST-BEHAVIOR.md](./XIE-LLM-TRUST-BEHAVIOR.md) | Validation methodology |
| **Design** | [BERTONCINI-COGNITIVE-BIAS-SIMULATION.md](./BERTONCINI-COGNITIVE-BIAS-SIMULATION.md) | Bias patterns |
| **Skill** | [speed-of-light/SKILL.md](../../skills/speed-of-light/SKILL.md) | Multi-agent methodology |

---

## Research Follow-Up

- [ ] Follow Hullman lab's methodological work
- [ ] Track debates in computational social science community
- [ ] Monitor replication/reproducibility discussions

---

## Citation

Hullman, J. (2025). "Is Behavior-Generative AI Epistemically Problematic?" Columbia University Data Science Blog.

---

*This document summarizes a critical methodological perspective on LLM behavioral simulation. Hullman's "exploration, not substitution" principle is foundational for MOOLLM's Speed-of-Light multi-agent simulations.*

*Document created: 2026-01-23*
