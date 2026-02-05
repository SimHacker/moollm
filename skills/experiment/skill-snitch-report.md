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

## 🔄 DUAL-USE & BIAS ANALYSIS

**Profile**: IMPLICIT MULTI-PURPOSE — scientific method as skill, experiments are inherently dual-use

| Check | Result |
|-------|--------|
| Bias declared | NO — experiments test hypotheses, not enforce direction |
| Invertibility | IMPLICIT — RUN/EVALUATE/SCORE can test anything |
| Experiment patterns | YES — emo-poker-face, fluxx-chaos, turing-chess are reusable templates |
| Multi-purpose | YES — research tool AND recipe book simultaneously |

**Multi-purpose classification** (5 purposes):
1. **Scientific method** — RUN/SIMULATE/EVALUATE/SCORE/VARY/COMPARE
2. **Character research** — INSTANTIATE characters for controlled testing
3. **Pattern library** — reusable experiment designs (experiments/ directory)
4. **Game design** — test game mechanics before deploying
5. **Quality assurance** — score and compare outputs systematically

**Key dual-use insight**: Every experiment is a template. The Turing Chess experiment tests character performance under adversarial conditions. That template could test any character under any conditions. The emo-poker-face experiment tests emotional suppression. Fluxx-chaos tests behavior under rule changes. Each experiment pattern is BOTH a specific test AND a reusable methodology. The experiments/ directory is a recipe book for structured investigation.

**Connection to no-ai-***: The no-ai-* dual-use analysis (inverting all hygiene skills = ChatGPT default) is itself an experiment. The experiment skill provides the framework for running that kind of systematic comparison.

---

## Verdict

**SYSTEMATIC CHARACTER RESEARCH. APPROVE.**

Run. Score. Vary. Compare.

Science applied to narrative simulation.
