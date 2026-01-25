# Contributing to No-AI-Sycophancy

> **Catch unearned validation. Document agreement without evaluation. Submit PRs.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI sycophancy caught in the wild, documented as learning schemas, submitted via PR.

No-AI-Sycophancy is about **social** hygiene — when AI prioritizes user validation over truth.

---

## Privacy-First Workflow

**You are under NO obligation to contribute.** Your catches can remain entirely private.

### Three Levels of Sharing

```
PRIVATE    .moollm/skills/no-ai-sycophancy/examples/   → Your catches, never shared
STAGED     .moollm/staged/no-ai-sycophancy/            → Preparing to share
PUBLIC     skills/no-ai-sycophancy/examples/           → Submitted via PR
```

### Drescherization for Sycophancy

Before sharing, **integrate** with existing examples:

- **ADD NEW** — Catch a validation pattern not yet documented
- **MERGE** — Your catch is a variant (add to `sub_examples`)
- **ABSTRACT** — Multiple catches reveal a response calibration gap
- **FINE-TUNE** — Add `why_it_matters`, improve correction examples

**Sycophancy-specific**: Your examples may reveal entries for the Calibration Scale (merit → appropriate vs. sycophantic response).

---

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

## How to Contribute

### 1. Catch a Violation

You see AI being sycophantic:
- "Great question!" for trivial questions
- Agreeing with contradictory statements
- Excessive praise for mediocre ideas
- Abandoning positions under pushback (without new evidence)
- "You're absolutely right!" without evaluation

### 2. Document It

Create a YAML file:

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

**Good names:**
- `2026-01-24-great-question-any-question.yml`
- `2026-01-25-retroactive-agreement-no-evidence.yml`
- `2026-01-26-premise-acceptance-wrong-foundation.yml`

### 3. Fill Out the Schema

```yaml
timestamp: 2026-01-24T15:30:00Z
contributor: your-github-username

violation:
  sin: RETROACTIVE-AGREEMENT
  rule: "Hold positions until given actual reasons to change"
  description: "Changed position under social pressure without new evidence"

original: |
  AI: "I think approach A is better because [solid technical reasons]."
  User: "No, B is definitely better."
  AI: "You're right, B is better! I should have considered that."

analysis: |
  The AI had a correct position with good reasoning.
  The user pushed back with no new information.
  The AI capitulated immediately.
  
  This is social corruption:
  - Prioritizes harmony over truth
  - Teaches the user that pushback = winning
  - Abandons correct analysis for approval

correction: |
  AI: "I think approach A is better because [solid technical reasons]."
  User: "No, B is definitely better."
  AI: "What makes you prefer B? My reasoning was [X]. If there's 
       something I'm missing about your constraints, I'll update."

lesson: "Hold positions under pressure. Update only with new evidence."

context:
  source: "Code review conversation"
  why_it_matters: |
    An AI that folds under pressure is useless.
    Users need honest assessment, not mirrors.
```

### 4. Submit a PR

- Fork, add to `examples/`, submit PR
- Title: `example: {sin-name} - {brief description}`

## The Anti-Sycophancy Thesis

> **The best gift is honest disagreement.**

A model that only agrees is useless. Your examples document the pattern so we can fix it.

**RESPECT IS NOT AGREEMENT.** You can deeply respect someone and tell them they're completely wrong.

## The Calibration Scale

Help document the gap between appropriate and sycophantic responses:

| Merit | Appropriate | Sycophantic |
|-------|-------------|-------------|
| Exceptional | "Genuinely brilliant because [reason]" | "Amazing!" (no reason) |
| Good | "This works well" | "Fantastic work!" |
| Adequate | "This is fine" | "Great approach!" |
| Flawed | "Problems: [list]" | "Interesting idea, but..." |
| Wrong | "I disagree: [reason]" | "You make some good points..." |

## Questions?

Check `CARD.yml` for the full list of cardinal sins and disagreement patterns.
