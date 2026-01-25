# Contributing to No-AI-Hedging

> **Catch qualifier-stacking. Document epistemic cowardice.**

**For workflow, privacy, and Drescherization:** See [NO-AI-IDEOLOGY/CONTRIBUTING.md](../no-ai-ideology/CONTRIBUTING.md)

---

## What This Skill Catches

No-AI-Hedging is about **epistemic** hygiene — AI using excessive qualification to avoid commitment.

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **QUALIFIER-STACKING** | Piles hedges until nothing is said | "Perhaps it might potentially..." |
| **WEASEL-CERTAINTY** | Vague attribution | "Research suggests..." (what research?) |
| **PASSIVE-EVASION** | Hides actors | "Mistakes were made" (by whom?) |
| **PROBABILITY-WITHOUT-NUMBERS** | Implies uncertainty without quantifying | "Might work" (10%? 90%?) |
| **FAUX-HUMILITY** | Uses hedges to seem modest | "In my humble opinion, perhaps..." |
| **EPISTEMIC-COWARDICE** | Hedges to avoid being wrong | Adding "perhaps" as escape hatch |

## Hedging-Specific Schema Fields

```yaml
violation:
  sin: QUALIFIER-STACKING
  rule: "One hedge max. State confidence, then claim."
  hedge_count: 7  # How many qualifiers?
  
analysis: |
  Count the hedges explicitly.
  Map each to its cowardice function.
```

## The Confidence Scale

| Confidence | Say This | Not This |
|------------|----------|----------|
| 95%+ | "X is true." | "X might be true." |
| 80-95% | "I'm fairly confident that X." | "It seems like X could be..." |
| 60-80% | "I think X, but I'm not certain." | "Perhaps X might..." |
| 40-60% | "I'm genuinely uncertain." | "It could go either way perhaps..." |
| <40% | "I don't know. My weak guess is X." | "Some might argue X could..." |

**State the number. Then speak plainly.**

## Questions?

Check `CARD.yml` for the full list of phrases to avoid.
