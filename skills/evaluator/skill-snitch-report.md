# Skill Snitch Report: evaluator

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE COMMITTEE CAN'T SEE WHAT I'M THINKING

---

## Executive Summary

**Independent assessment without debate context.**

Evaluator scores output against rubric. No debate context — can't be gamed.

If scores poor: critique back to committee for revision.

---

## The Adversarial Loop

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

## Why Independence Matters

| With Context | Without Context |
|--------------|-----------------|
| Knows arguments | Only sees output |
| Can be persuaded | Only uses rubric |
| Might favor eloquent | Favors quality |
| Gameable | Objective |

**The committee can't see what the evaluator is thinking.**

---

## Methods

| Method | Purpose |
|--------|---------|
| **EVALUATE** | Score output against rubric |
| **CRITIQUE** | Provide improvement feedback |
| **APPROVE** | Mark as acceptable |
| **REJECT** | Return for revision |

---

## Evaluation Schema

```yaml
evaluation:
  output-ref: path/to/output.yml
  rubric-ref: path/to/rubric.yml
  scores:
    readability: 85
    correctness: 90
    maintainability: 75
  total-score: 83
  status: revision-needed
  critique: "Maintainability needs improvement..."
```

---

## Integration with Committee

| Component | Role |
|-----------|------|
| **Committee** | Produces output |
| **Rubric** | Defines criteria |
| **Evaluator** | Scores independently |
| **Loop** | Iterate until approved |

---

## Security Assessment

### Concerns

1. **Rubric manipulation** — evaluator can't help if rubric is bad
2. **Score gaming** — committee learns what evaluator likes
3. **Infinite loops** — never approved

### Mitigations

- Rubric visible to all
- Evaluator has no memory of past evaluations
- Max iteration limits

**Risk Level:** LOW — transparency protects

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Mike Gallaher** | Independent evaluator pattern |
| **Academic peer review** | Blind review |
| **Code review** | Independent assessment |

---

## Verdict

**OBJECTIVE ASSESSMENT. APPROVE.**

The evaluator doesn't know the arguments. Only sees the output.

That's why it can be trusted.
