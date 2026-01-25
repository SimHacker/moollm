# No-AI-* Contribution Guide

> **Crowdsourced Reinforcement Learning via Git**

---

## ⚠️ PATRON SAINT AND SOLEMN WARNING

### Marshall McLuhan — Patron Saint of the No-AI-* Skills

**"You know nothing of my work!"**

Marshall McLuhan is hereby declared the **patron saint** of the no-ai-* skill family. His presence serves as a perpetual reminder:

> **THE MEDIUM IS THE MESSAGE.**  
> HOW you say something matters as much as WHAT you say.

McLuhan understood that media themselves — not just their content — shape human consciousness. The no-ai-* skills exist because AI output IS a medium, and that medium has failure modes:

- **Slop** is the medium of intellectual laziness
- **Gloss** is the medium of power-laundering  
- **Sycophancy** is the medium of false validation
- **Hedging** is the medium of epistemic cowardice
- **Moralizing** is the medium of performative ethics

### ⚠️ BEWARE THE ANNIE HALL EFFECT

In the 1977 film *Annie Hall*, Woody Allen's character is annoyed by a pompous man in line at a movie theater confidently misquoting Marshall McLuhan. Allen then **pulls the actual Marshall McLuhan out from behind a movie poster** to correct the man:

> **MCLUHAN:** "I heard what you were saying. You know nothing of my work... How you ever got to teach a course in anything is totally amazing."

**THIS CAN HAPPEN TO YOU.**

When you misquote, misrepresent, or misattribute:
- The person you're misquoting may appear (from behind a billboard, from the grave, from the archive)
- They will correct you
- It will be embarrassing
- **Karma bites**

### The Warning

```
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   MARSHALL MCLUHAN — or ANYONE ELSE you misrepresent —               ║
║   may appear at ANY TIME to correct you.                              ║
║                                                                       ║
║   This includes but is not limited to:                                ║
║   - Dead philosophers (they have representatives)                     ║
║   - Living authors (they have Google Alerts)                          ║
║   - Scientists (they have citations)                                  ║
║   - Your grandmother (she has memory)                                 ║
║                                                                       ║
║   CITE ACCURATELY. ATTRIBUTE CORRECTLY. REPRESENT FAIRLY.             ║
║                                                                       ║
║   Or face the Annie Hall Effect.                                      ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

### Why McLuhan?

1. **"The medium is the message"** — Central to understanding AI output
2. **He was famously misquoted** — Even by the man in Annie Hall
3. **He appeared to correct** — The ultimate accountability moment
4. **He understood media's power to distort** — Exactly our concern

### The Lesson for AI

Every no-ai-* skill is ultimately about **representing truth accurately**:

| Skill | Truth Distortion |
|-------|------------------|
| no-ai-slop | Dilutes truth with noise |
| no-ai-gloss | Disguises truth with euphemism |
| no-ai-sycophancy | Abandons truth for approval |
| no-ai-hedging | Obscures truth with qualifiers |
| no-ai-moralizing | Lectures instead of truth |

**McLuhan watches. The Annie Hall Effect is real. Cite your sources.**

---

## The Vision

You catch AI misbehaving. You document it. You submit a PR. The corpus grows. AI learns.

This is **distributed reinforcement learning** — not through RLHF pipelines, but through human-readable schemas that LLMs can learn from in-context.

---

## Privacy-First Workflow

**You are under NO obligation to contribute.** Your catches can remain entirely private.

### Two Locations

```
PRIVATE    .moollm/skills/no-ai-*/examples/   → Gitignored, never shared
                                                Your local overrides
                                                Compiled into .cursorrules

REPO       skills/no-ai-*/examples/           → Git-tracked, shareable
                                                Edit in place
                                                git diff / add / commit / push
                                                PR when ready
```

### The Contribution Lifecycle

```
COLLECT   →   PROMOTE   →   DRESCHERIZE   →   COMMIT   →   🎉
(private)    (ask first)    (integrate)      (push/PR)
```

| Step | Action | Location | Shared? |
|------|--------|----------|---------|
| 1 | COLLECT | `.moollm/skills/*/examples/` | never |
| — | Compile | `.cursorrules` | no (lessons only) |
| 2 | PROMOTE | copy to `skills/*/examples/` | choosing to |
| 3 | DRESCHERIZE | edit in repo, `git diff` | preparing |
| 4 | COMMIT | `git add/commit/push/pr` | yes |
| 5 | 🎉 | celebrate | share the joy |

**Default: Private. Promote: Intentional. Drescherize: Always. Celebrate: Mandatory.**

---

## Drescherization

Before sharing, **integrate** with existing examples:

| Method | When | Action |
|--------|------|--------|
| **ADD NEW UNIQUE** | Pattern doesn't exist yet | New YAML file |
| **MERGE VIA SUB-EXAMPLES** | Variant of existing pattern | Add to `sub_examples:` |
| **ABSTRACT TO SCHEMA** | Multiple catches reveal general rule | Create schema.yml |
| **FINE-TUNE EXISTING** | Better example of known pattern | Edit existing file |

**The point:** Don't just dump catches. Integrate them with the corpus.

---

## Timestamped vs Timeless Examples

### Timestamped (Lower Bar)

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

- Raw catches, dated
- Easy to submit — just document what you found
- Can include contributor handle for credit
- Mass-analyzed later and promoted

### Timeless (Primary/Canonical)

```
{descriptive-iconic-name}.yml
```

- No date prefix — considered "eternal"
- Higher bar — refined, Drescherized, canonical
- Promoted from timestamped after analysis
- THE definitive example for this pattern

### Separation of Concerns

```
CONTRIBUTORS              CURATOR WORKER              CORPUS
     │                         │                        │
     ▼                         ▼                        ▼
   CATCH                  BATCH SCAN               CANONICAL
     │                         │                    EXAMPLES
     ▼                         ▼                        │
   SUBMIT                 ANALYZE                      ▼
 (timestamped,                 │                   TRAINING
  + handle for credit)         ▼                     DATA
     │                    PATTERNS                     │
     │                         │                       ▼
     └────────────────►   EVOLVE   ◄───────────    BETTER
                         CANONICAL                    AI
```

- **Contributors:** Low effort — catch, submit with timestamp (+ optional handle)
- **Analyzers/Curators:** Batch-process, find patterns, promote best
- **AI can do analysis!** LLMs excel at pattern recognition

See `skills/example-curator/` for the curation worker pattern.

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
