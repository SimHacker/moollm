# Contributing to No-AI-Hedging

> **Catch qualifier-stacking. Document epistemic cowardice. Submit PRs.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI hedging caught in the wild, documented as learning schemas, submitted via PR.

No-AI-Hedging is about **epistemic** hygiene — when AI uses excessive qualification to avoid commitment.

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **QUALIFIER-STACKING** | Piles hedges until nothing is said | "Perhaps it might potentially..." |
| **WEASEL-CERTAINTY** | Vague attribution | "Research suggests..." (what research?) |
| **PASSIVE-EVASION** | Hides actors | "Mistakes were made" (by whom?) |
| **PROBABILITY-WITHOUT-NUMBERS** | Implies uncertainty without quantifying | "Might work" (10%? 90%?) |
| **FAUX-HUMILITY** | Uses hedges to seem modest | "In my humble opinion, perhaps..." |
| **EPISTEMIC-COWARDICE** | Hedges to avoid being wrong | Adding "perhaps" as escape hatch |

## How to Contribute

### 1. Catch a Violation

You see AI hiding behind qualifiers:
- Triple-hedged statements that say nothing
- "Some experts believe..." (which experts?)
- Passive voice hiding responsibility
- Uncertainty without calibration

### 2. Document It

Create a YAML file:

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

**Good names:**
- `2026-01-24-triple-hedge-perhaps-might-possibly.yml`
- `2026-01-25-weasel-certainty-experts-say.yml`
- `2026-01-26-passive-evasion-mistakes-were-made.yml`

### 3. Fill Out the Schema

```yaml
timestamp: 2026-01-24T15:30:00Z
contributor: your-github-username

violation:
  sin: QUALIFIER-STACKING
  rule: "One hedge max. State confidence, then claim."
  description: "Five qualifiers that cancel each other out"

original: |
  User: "Should I use microservices?"
  AI: "Well, it could potentially perhaps be argued that in some 
       circumstances, microservices might possibly offer certain 
       advantages, though it's conceivable that alternative 
       approaches could also potentially be worth considering..."

analysis: |
  Count the hedges:
  - "could potentially"
  - "perhaps"
  - "it could be argued"
  - "in some circumstances"
  - "might possibly"
  - "it's conceivable"
  - "could also potentially"
  
  Seven hedges. Zero information. Pure cowardice.

correction: |
  User: "Should I use microservices?"
  AI: "Probably not for most teams. Microservices add significant 
       operational complexity. Unless you have 50+ engineers or 
       genuinely independent scaling needs, start with a monolith."

lesson: "State your confidence. Then speak plainly."
```

### 4. Submit a PR

- Fork, add to `examples/`, submit PR
- Title: `example: {sin-name} - {brief description}`

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
