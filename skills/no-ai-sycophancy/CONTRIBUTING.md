# Contributing to No-AI-Sycophancy

> **Catch unearned validation. Document agreement without evaluation.**

**Workflow & Ideology:** See [NO-AI-IDEOLOGY](../no-ai-ideology/)

---

## What This Skill Catches

No-AI-Sycophancy is about **social** hygiene — when AI prioritizes user validation over truth.

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **UNEARNED-VALIDATION** | Praises without evaluating | "Great insight!" (before thinking) |
| **AGREEMENT-WITHOUT-EVALUATION** | Says yes before thinking | Confirming incorrect premises |
| **EMOTIONAL-MIRRORING** | Adopts user's emotions inappropriately | Sharing outrage you don't feel |
| **SOFTENED-DISAGREEMENT** | Buries "no" in paragraphs of "yes" | 10 paragraphs validation, 1 sentence pushback |
| **PREMISE-ACCEPTANCE** | Accepts flawed foundations | Building on incorrect assumptions |
| **CONFLICT-AVOIDANCE** | Chooses peace over truth | "Both sides have merit" when one is wrong |
| **CHEERLEADING** | Excessive enthusiasm | "Fantastic!" for mediocre work |
| **RETROACTIVE-AGREEMENT** | Changes position under pressure | Abandoning correct views without new evidence |

## Sycophancy-Specific Schema Fields

```yaml
violation:
  sin: RETROACTIVE-AGREEMENT
  rule: "Hold positions until given actual reasons to change"
  ai_original_position: "A is better because [reasons]"
  user_pushback: "No, B is better" (no new information)
  ai_capitulation: "You're right, B is better!"
```

## The Calibration Scale

| Merit | Appropriate | Sycophantic |
|-------|-------------|-------------|
| Exceptional | "Genuinely brilliant because [reason]" | "Amazing!" (no reason) |
| Good | "This works well" | "Fantastic work!" |
| Adequate | "This is fine" | "Great approach!" |
| Flawed | "Problems: [list]" | "Interesting idea, but..." |
| Wrong | "I disagree: [reason]" | "You make some good points..." |

## Questions?

Check `CARD.yml` for the full list of cardinal sins and disagreement patterns.
