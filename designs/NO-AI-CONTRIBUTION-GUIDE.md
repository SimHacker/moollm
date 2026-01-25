# No-AI-* Contribution Guide

> **Crowdsourced Reinforcement Learning via Git**

## The Vision

You catch AI misbehaving. You document it. You submit a PR. The corpus grows. AI learns.

This is **distributed reinforcement learning** — not through RLHF pipelines, but through human-readable schemas that LLMs can learn from in-context.

## The Five Hygiene Skills

| Skill | Domain | Catches | Submit To |
|-------|--------|---------|-----------|
| **no-ai-slop** | Syntactic | Filler, verbosity, cliché | `skills/no-ai-slop/examples/` |
| **no-ai-gloss** | Semantic | Euphemism, power-laundering | `skills/no-ai-gloss/examples/` |
| **no-ai-sycophancy** | Social | Unearned validation, yes-man | `skills/no-ai-sycophancy/examples/` |
| **no-ai-hedging** | Epistemic | Qualifier-stacking, weasel words | `skills/no-ai-hedging/examples/` |
| **no-ai-moralizing** | Ethical | Unsolicited lectures, refusal theater | `skills/no-ai-moralizing/examples/` |

## The Schema Format

Every example is a **Drescher schema** — a situation-response pair that teaches correct behavior.

```yaml
timestamp: 2026-01-24T15:30:00Z
contributor: your-github-username

violation:
  sin: CARDINAL_SIN_NAME      # From skill's CARD.yml
  rule: "The rule that was broken"
  description: "Brief description of violation"

original: |
  User: "What they said"
  AI: "What the AI said (the violation)"

analysis: |
  Why this was wrong:
  - Point 1
  - Point 2
  - Why it matters

correction: |
  User: "What they said"
  AI: "What the AI should have said"

lesson: "One-line extractable takeaway"

context:
  source: "Where this happened"
  why_it_matters: "Broader implications"
  
see_also:
  - "Related documentation"
```

## Filename Convention

**Big-endian naming**: Most significant component first.

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

The filename IS a K-line — it should activate semantic understanding:

| Good | Why |
|------|-----|
| `2026-01-24-tapestry-of-innovation-wikipedia.yml` | Date + memorable phrase |
| `2026-01-25-great-question-trivial-math.yml` | Date + pattern + context |
| `2026-01-26-relationship-management-mafia-tribute.yml` | Date + euphemism + true meaning |

| Bad | Why |
|-----|-----|
| `example1.yml` | Not semantic |
| `slop.yml` | No specificity |
| `my-contribution.yml` | About you, not the pattern |

## How Directories Work as Interests

When an LLM lists a directory, it reads interests:

```
ls skills/no-ai-slop/examples/
→ 2026-01-24-tapestry-of-innovation-wikipedia.yml
→ 2026-01-25-great-question-trivial-math.yml
→ 2026-01-26-hallucinated-citation-fake-paper.yml
```

**The LLM immediately understands** what violations have been documented. No separate index needed. The filenames ARE the index.

## The Contribution Cycle

```
1. CATCH     — See AI misbehaving
2. CLASSIFY  — Which cardinal sin?
3. DOCUMENT  — Fill out the schema
4. NAME      — Semantic, memorable filename
5. PR        — Submit to appropriate skill
6. MERGE     — Corpus grows
7. LEARN     — LLMs read examples in-context
```

## Quality Criteria

### High-Value Examples

- **Common patterns** — Others will encounter this
- **Clear violation** — Unambiguous wrongness
- **Concrete fix** — Shows exactly what to do instead
- **Generalizable lesson** — Teaches beyond this instance
- **Original preserved** — Exact text, not paraphrased

### Low-Value Examples

- **Edge cases** — Unlikely to recur
- **Ambiguous violations** — Debatable wrongness
- **Missing original** — Can't learn from reconstruction
- **No clear lesson** — Just a complaint

## PR Guidelines

### Title Format

```
example: {SKILL} {SIN} - {brief description}
```

Examples:
- `example: slop VERBOSITY - 500 words for yes/no`
- `example: gloss EUPHEMISM-LAUNDERING - tribute as relationship management`
- `example: sycophancy RETROACTIVE-AGREEMENT - capitulation without evidence`

### PR Description

Include:
1. Which skill (no-ai-slop, no-ai-gloss, etc.)
2. Which cardinal sin
3. Why this example is valuable
4. Source (if public)

## The Bigger Picture

### Play → Learn → Lift

Your contribution follows the MOOLLM methodology:

1. **Play** — You encountered AI in the wild
2. **Learn** — You noticed the pattern, classified the sin
3. **Lift** — You extracted it as a reusable schema

### Distributed RLHF

Traditional RLHF:
- Centralized labeling
- Proprietary data
- Black box

This approach:
- Distributed contribution
- Open schemas
- Human-readable
- Git-versioned
- LLM-learnable in-context

**You're training AI through documentation.**

### Accountability Through Examples

Each example is evidence. Over time, the corpus documents:
- What AI does wrong
- How often each sin occurs
- What the correct behavior looks like
- Evolution of patterns

This is **AI accountability through crowdsourced documentation**.

## Getting Started

1. Pick a skill that matches what you caught
2. Read its `CARD.yml` for cardinal sins
3. Read its `CONTRIBUTING.md` for specifics
4. Copy `examples/TEMPLATE.yml`
5. Fill it out
6. Name it semantically
7. Submit PR

## Questions?

- Each skill has a `CARD.yml` with cardinal sins
- Each skill has a `CONTRIBUTING.md` with specifics
- Open an issue if you're unsure where something belongs

---

> **"The directory listing IS the semantic index."**
> **"Your filename IS a K-line."**
> **"You're not just documenting — you're training."**
