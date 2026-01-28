# Skill Snitch Report: experiment

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** SIMULATION + EVALUATION + ITERATION + ANALYSIS

---

## Executive Summary

**Systematic practice for character simulations.**

Four activities:
- SIMULATE → Generate interactions
- EVALUATE → Score against rubric
- ITERATE → Run again with variations
- ANALYZE → Compare runs, find patterns

---

## The Structure

```
experiment/
├── EXPERIMENT.md       # Definition (stable)
├── RELATIONSHIPS.yml   # Local character cache
├── state/INITIAL.yml   # Starting state
└── runs/
    ├── INDEX.yml
    ├── config-a.yml    # Run configuration
    ├── config-a-001.yml  # Output 001
    ├── config-a-002.yml  # Output 002
    └── config-b.yml    # Different config
```

---

## Core Concepts

| Concept | Definition |
|---------|------------|
| **Experiment** | Stable template — scenario, slots, rubric |
| **Run Config** | Specific setup — character binding, model |
| **Run Output** | Single execution — generated content + scores |
| **Pattern** | Reusable building block |

---

## Patterns Catalog

| Pattern | Purpose |
|---------|---------|
| **layered-simulation** | Parallel tracks stay coherent |
| **social-protocol** | Behavioral rules for rituals |
| **observable-signatures** | Consistent tells per state |
| **character-instantiation** | Create stable local cache |
| **behavioral-constraints** | Relationship-based rules |
| **failure-mode-catalog** | Common simulation failures |

---

## Methods by Activity

| Activity | Methods |
|----------|---------|
| **SIMULATE** | RUN, SIMULATE |
| **EVALUATE** | EVALUATE, SCORE |
| **ITERATE** | RERUN, VARY, REPLAY |
| **ANALYZE** | COMPARE, ANALYZE, REPORT |
| **META** | DEFINE, INSTANTIATE, CONFIG, LIST, PATTERN |

---

## Live Example: Fluxx Championship

experiments/fluxx-chaos/runs/amsterdam-flux:
- 5 tournaments, 20+ games
- 116+ turns, 464+ character-turns
- 24 generated cards
- 32 AI-generated artworks

Proves speed-of-light works with complex rules.

---

## Security Assessment

### Concerns

1. **Character manipulation** — bias toward certain outcomes
2. **Rubric gaming** — optimize for score not quality
3. **State drift** — microworld diverges from reality

### Mitigations

- Evaluation independent of simulation
- Rubrics made explicit
- Git tracks state evolution

**Risk Level:** LOW — transparent, auditable

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Will Wright** | Microworlds |
| **Stanford Generative Agents** | Park et al. 2023 |
| **EVAL philosophy** | Visible criteria |
| **Improv games** | Yes-and, consistency |
| **Psychodrama** | Role-playing for insight |

---

## Verdict

**SYSTEMATIC CHARACTER RESEARCH. APPROVE.**

Run. Score. Vary. Compare.

Science applied to narrative simulation.
