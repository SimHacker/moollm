# 📊 Rubric

> "Measurable criteria translate qualitative debate into quantitative decisions."

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [adversarial-committee/](../adversarial-committee/) | What gets scored |
| [evaluator/](../evaluator/) | Who applies the rubric |
| [scoring/](../scoring/) | Generic scoring principles |
| [advertisement/](../advertisement/) | Objects advertise against criteria |
| [designs/mike-gallaher-ideas.md](../../designs/mike-gallaher-ideas.md) | Mike Gallaher's methodology |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

A RUBRIC defines measurable quality criteria that translate qualitative discussion into quantifiable scores. The committee knows they'll be scored but doesn't see the evaluator's reasoning.

## Why Rubrics?

Without explicit criteria:
- "Good" means different things to different personas
- Debate has no grounding
- Decisions can't be compared across time
- Success is undefined

With rubrics:
- Criteria are explicit and weighted
- Each option scores against the same scale
- Decisions become defensible
- Learning accumulates

## Example Rubric

```yaml
rubric:
  name: "Client Engagement Evaluation"
  
  criteria:
    resource_efficiency:
      weight: 0.20
      scale: 1-5
      anchors:
        5: "Fits perfectly within current capacity"
        3: "Manageable with some adjustment"
        1: "Would require significant new resources"
        
    risk_level:
      weight: 0.30
      scale: 1-5
      anchors:
        5: "Minimal risk, strong track record"
        3: "Moderate risk, manageable concerns"
        1: "High risk, major red flags"
```

## Credits

**Mike Gallaher** — RUBRIC-based scoring as bridge between qualitative and quantitative.

See: [designs/mike-gallaher-ideas.md](../../designs/mike-gallaher-ideas.md)

