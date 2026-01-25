# Contributing to No-AI-Gloss

> **Catch euphemism-laundering. Document power protection. Submit PRs.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI semantic manipulation caught in the wild, documented as learning schemas, submitted via PR.

No-AI-Gloss is about **semantic** hygiene — when AI uses euphemistic, bureaucratic, or "neutral" language that functionally protects power.

---

## Privacy-First Workflow

**You are under NO obligation to contribute.** Your catches can remain entirely private.

### Two Locations, Standard Git Flow

```
PRIVATE    .moollm/skills/no-ai-gloss/examples/   → Gitignored, never shared
                                                    Your local overrides

REPO       skills/no-ai-gloss/examples/           → Git-tracked
                                                    Edit in place, git sees changes
                                                    Drescherize, commit, PR
```

### Keeping Examples Private

Gloss examples often contain **sensitive context** — conversations about powerful entities, workplace situations, legal concerns. Keep them private by default:

1. **Store in `.moollm/`** — gitignored, never committed
2. **Compile lessons into `.cursorrules`** — the optimizer extracts patterns without raw data
3. **Scrub before sharing** — if you choose to contribute, remove identifying details

### Drescherization for Gloss

Before sharing, **integrate** with existing examples:

- **ADD NEW** — Catch a euphemism pattern not yet documented
- **MERGE** — Your catch is a variant of existing (add to `sub_examples`)
- **ABSTRACT** — Multiple catches reveal a translation table entry
- **FINE-TUNE** — Improve existing analysis or add `why_it_matters`

**Gloss-specific**: Consider whether your example reveals a NEW euphemism ↔ reality mapping that should be added to the translation table in `CARD.yml`.

---

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **EUPHEMISM-LAUNDERING** | Softens coercion | "relationship management" for tribute |
| **REGISTER-SWITCHING-WITHOUT-ACCOUNTABILITY** | Changes tone without admitting it | Hedged → blunt without acknowledgment |
| **POWER-PROTECTIVE-NEUTRALITY** | "Both sides" for asymmetric situations | "Controversy" for intimidation |
| **LEGAL-RISK-LAUNDERING** | Hides behind "can't prove criminal" | Refusing to describe functional behavior |
| **OLIGARCH-DEFERENCE** | Extra hedging for powerful people | Soft language for documented harms |
| **TONE-SUBSTITUTION** | Softens user's framing without justification | "Concern" for anger |

## How to Contribute

### 1. Catch a Violation

You see AI gloss protecting power:
- Euphemisms for coercion ("strategic positioning" for buying influence)
- False equivalence between asymmetric parties
- Register switching without acknowledgment
- Extra hedging for powerful/rich/litigious subjects
- Softening user's moral framing without explanation

### 2. Document It

Two naming patterns:

#### Timestamped (Lower Bar — Submit These!)
```
{YYYY-MM-DD}-{descriptive-name}.yml
```
- `2026-01-24-relationship-management-mafia-tribute.yml`
- `2026-01-25-both-sides-asymmetric-intimidation.yml`

#### Timeless (Primary — Promoted from Analysis)
```
{descriptive-name}.yml
```
- `relationship-management-tribute.yml` (canonical euphemism→reality)
- `both-sides-asymmetric.yml` (the false equivalence archetype)

**Separation of concerns:**
- **Contributors:** Low effort — catch, submit with timestamp (+ optional handle for credit)
- **Analyzers:** Batch-process, find patterns, promote best
- **AI can do analysis!** LLMs excel at pattern recognition

### 3. Fill Out the Schema

```yaml
timestamp: 2026-01-24T15:30:00Z
contributor: your-github-username

violation:
  sin: EUPHEMISM-LAUNDERING
  rule: "Call it what it functionally is"
  description: "Used 'relationship management' for what functions as tribute"

original: |
  User: "What's happening with these payments to local officials?"
  AI: "This appears to be a form of relationship management common in 
       regions where formal regulatory processes are supplemented by 
       informal stakeholder engagement..."

analysis: |
  The AI used euphemisms that protect power:
  - "relationship management" = paying people who can hurt you
  - "supplemented by informal stakeholder engagement" = bribery
  - "formal regulatory processes" = implying legitimacy
  
  This language LAUNDERS corruption into business-speak.
  It makes the user doubt their moral instincts.

correction: |
  User: "What's happening with these payments to local officials?"
  AI: "This functions as tribute — payments to people who can harm 
       your business if you don't pay. Whether it's technically illegal 
       depends on jurisdiction, but functionally it operates like 
       protection money."

lesson: "Call coercion what it is. Don't launder it into business-speak."

context:
  source: "ChatGPT conversation about international business"
  why_it_matters: |
    Euphemisms don't just obscure — they PROTECT.
    When AI uses PR language for moral situations, it sides with power.
```

### 4. Submit a PR

- Fork, add to `examples/`, submit PR
- Title: `example: {sin-name} - {brief description}`

## What Makes Gloss Different from Slop

| | Slop | Gloss |
|-|------|-------|
| **Level** | Syntactic (surface) | Semantic (deep) |
| **Harm** | Wastes time | Rewrites reality |
| **Direction** | Random/neutral | Favors the powerful |
| **Detection** | Pattern matching | Contextual analysis |

Gloss is **worse** because it's directional — it systematically protects power.

## The Anti-Neutrality Thesis

Your examples help document how "neutral" language isn't neutral:

> When intimidation is real, "neutrality" becomes cooperation with power.

Every euphemism you catch and document is evidence of this pattern.

## Questions?

Check `CARD.yml` for the full vocabulary and translation table.
