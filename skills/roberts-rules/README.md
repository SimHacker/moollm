# 📜 Robert's Rules

> "Parliamentary procedure prevents jumping to statistically-likely conclusions."

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [adversarial-committee/](../adversarial-committee/) | Who follows these rules |
| [rubric/](../rubric/) | How to score outcomes |
| [evaluator/](../evaluator/) | Independent assessment |
| [session-log/](../session-log/) | Recording minutes |
| [designs/mike-gallaher-ideas.md](../../designs/mike-gallaher-ideas.md) | Mike Gallaher's methodology |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Robert's Rules of Order as a **forcing function** for LLM deliberation. The structure prevents the model from short-circuiting to familiar conclusions — it forces genuine exploration of the decision space.

## Why Parliamentary Procedure?

LLMs want to give you "the answer" immediately. But complex decisions require:

1. **Review of precedent** — What did we decide before?
2. **Formal proposals** — Someone must commit to a position
3. **Support requirements** — Others must agree it's worth discussing
4. **Structured debate** — Arguments for and against
5. **Recorded votes** — Positions are explicit

This slows down the rush to consensus and surfaces minority views.

## The Stages

```
CALL TO ORDER → REVIEW MINUTES → NEW BUSINESS → 
MOTION → SECOND → DEBATE → VOTE → ADJOURN
```

Each stage must complete before the next begins. No skipping.

## Credits

**Mike Gallaher** — Adaptation of Robert's Rules as LLM forcing function.

**Henry Martyn Robert** — Original *Robert's Rules of Order* (1876).

See: [designs/mike-gallaher-ideas.md](../../designs/mike-gallaher-ideas.md)

