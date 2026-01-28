# Skill Snitch Report: rubric

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** HOW DO WE KNOW IT'S GOOD?

---

## Executive Summary

**Measurable criteria translating qualitative debate to quantitative scores.**

Define explicit success criteria. Score objectively. Compare options.

---

## The Problem Rubrics Solve

Committee debates qualitatively: "I think option A is better."
Rubrics translate to quantitative: "Option A scores 85/100."

---

## Methods

| Method | Purpose |
|--------|---------|
| **CREATE** | Design a rubric |
| **SCORE** | Apply rubric to output |
| **EXPLAIN** | Show rubric criteria |

---

## Rubric Schema

```yaml
rubric:
  name: "Code Quality"
  criteria:
    - name: "Readability"
      weight: 0.3
      levels: [poor, acceptable, good, excellent]
    - name: "Performance"
      weight: 0.25
      levels: [poor, acceptable, good, excellent]
    - name: "Maintainability"
      weight: 0.25
      levels: [poor, acceptable, good, excellent]
    - name: "Test Coverage"
      weight: 0.2
      levels: [poor, acceptable, good, excellent]
  threshold: 70  # Pass/fail line
```

---

## The RUBRIC-BRIDGE Pattern

From Mike Gallaher:

```
Qualitative Discussion
        │
        ▼
    RUBRIC (bridge)
        │
        ▼
Quantitative Decision
```

The rubric is the bridge between debate and decision.

---

## Integration with Adversarial Committee

```
Committee DELIBERATES
        │
        ▼
Output generated
        │
        ▼
Evaluator SCORES with rubric
        │
   Score < threshold?
        │
    ┌───┴───┐
   Yes      No
    │        │
    ▼        ▼
CRITIQUE  APPROVE
    │
    ▼
Re-DELIBERATE
```

---

## Security Assessment

### Concerns

1. **Criteria manipulation** — biased rubrics
2. **Weight gaming** — inflate certain criteria
3. **Threshold manipulation** — lower bar

### Mitigations

- Rubrics visible
- Weights explicit
- Thresholds documented

**Risk Level:** LOW — transparent, auditable

---

## Example: Commit Message Rubric

```yaml
rubric:
  name: "Commit Message Quality"
  criteria:
    - name: "Why over What"
      description: "Explains motivation, not just changes"
    - name: "Conciseness"
      description: "Brief but complete"
    - name: "Convention"
      description: "Follows project style"
  threshold: 75
```

---

## Verdict

**QUALITY BRIDGE. APPROVE.**

Rubrics translate "I think it's good" to "It scores 85/100."

Essential for objective decision-making.
