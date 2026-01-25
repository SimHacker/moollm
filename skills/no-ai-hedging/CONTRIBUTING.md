# Contributing to No-AI-Hedging

> **Catch qualifier-stacking. Document epistemic cowardice. Submit PRs.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI hedging caught in the wild, documented as learning schemas, submitted via PR.

No-AI-Hedging is about **epistemic** hygiene — when AI uses excessive qualification to avoid commitment.

---

## Privacy-First Workflow

**You are under NO obligation to contribute.** Your catches can remain entirely private.

### Two Locations, Standard Git Flow

```
PRIVATE    .moollm/skills/no-ai-hedging/examples/   → Gitignored, never shared
                                                      Your local overrides
                                                      Compiled into .cursorrules

REPO       skills/no-ai-hedging/examples/           → Git-tracked, shareable
                                                      Edit in place
                                                      git diff / add / commit / push
                                                      PR when ready
```

When you edit repo files, git sees them as modified. That's your "working" state — you INTEND to share these changes. Drescherize before committing.

### Drescherization for Hedging

Before sharing, **integrate** with existing examples:

- **ADD NEW** — Catch a qualifier pattern not yet documented
- **MERGE** — Your catch is a variant (add to `sub_examples`)
- **ABSTRACT** — Multiple catches reveal a hedge → direct mapping
- **FINE-TUNE** — Improve analysis, add confidence calibration

**Hedging-specific**: Consider whether your example suggests a new entry in the Confidence Scale table.

---

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

Create a YAML file. Two naming patterns:

#### Timestamped Examples (Lower Bar)

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

- **Lower bar** — your raw catch, dated
- Easy to submit — just document what you found
- Can be mass-analyzed later and promoted

**Examples:**
- `2026-01-24-triple-hedge-perhaps-might-possibly.yml`
- `2026-01-25-weasel-certainty-experts-say.yml`

#### Timeless Examples (Primary/Canonical)

```
{descriptive-iconic-name}.yml
```

- **No date prefix** — considered "eternal"
- **Higher bar** — refined, Drescherized, canonical
- Promoted from timestamped examples after analysis
- THE example for this pattern

**Examples:**
- `qualifier-stacking-microservices.yml`
- `weasel-certainty-research-suggests.yml`

#### Promotion Lifecycle

```
CATCH      →    SUBMIT       →    ANALYZE      →    PROMOTE
(raw)           (timestamped)     (mass review)     (timeless)

2026-01-24-my-catch.yml  →  qualifier-stacking-microservices.yml
```

Multiple timestamped catches of the same pattern get analyzed,
the best one gets refined and promoted to timeless status.

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
