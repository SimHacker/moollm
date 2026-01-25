# Contributing to No-AI-Slop

> **Submit your catches. Grow the corpus. Train better AI.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI violations caught in the wild, documented as learning schemas, submitted via PR.

Each example is a **Drescher schema**: a situation-response pair that teaches the correct behavior. The examples/ directory IS the training data.

## How to Contribute

### 1. Catch a Violation

You see AI slop in the wild:
- Verbosity where brevity would do
- Filler phrases ("tapestry of innovation")
- Hallucinated citations
- "Great question!" cheerleading
- Over-enthusiasm for mediocre content

### 2. Document It

Create a YAML file following the naming convention:

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

**Good names** (semantic, memorable, LLM-recognizable):
- `2026-01-24-tapestry-of-innovation-wikipedia.yml`
- `2026-01-25-great-question-trivial-math.yml`
- `2026-01-26-hallucinated-citation-fake-paper.yml`

**Bad names** (not semantic):
- `example1.yml`
- `slop-instance.yml`
- `my-contribution.yml`

### 3. Fill Out the Schema

Copy `examples/TEMPLATE.yml` and fill in:

```yaml
timestamp: 2026-01-24T15:30:00Z
contributor: your-github-username

violation:
  sin: VERBOSITY  # Which cardinal sin?
  rule: "Say it once. Say it clearly. Stop."
  description: "500 words for a yes/no question"

original: |
  User: "Is Python dynamically typed?"
  AI: "That's a fantastic question! Python is indeed a dynamically 
       typed language, which means that variable types are determined
       at runtime rather than at compile time. This provides tremendous
       flexibility for developers, allowing them to write code without
       explicitly declaring types. The dynamic typing system in Python
       is one of its most celebrated features, enabling rapid prototyping
       and... [250 more words]"

analysis: |
  The user asked a yes/no question. The answer is "Yes."
  
  Problems:
  - "That's a fantastic question!" — cheerleading slop
  - 300 words for a one-word answer
  - Explained benefits no one asked about
  - Filler that adds no information

correction: |
  User: "Is Python dynamically typed?"
  AI: "Yes."

lesson: "Yes/no questions get yes/no answers."

context:
  source: "ChatGPT conversation"
  date: "2026-01-24"
  
see_also:
  - "../CARD.yml#verbosity"
```

### 4. Submit a PR

1. Fork the repo
2. Add your example to `skills/no-ai-slop/examples/`
3. Submit PR with title: `example: {sin-name} - {brief description}`

Example PR titles:
- `example: VERBOSITY - 500 words for yes/no question`
- `example: HALLUCINATION - fake Nature citation`
- `example: CHEERLEADING - great question for trivial query`

## Schema Quality Checklist

- [ ] **Filename is semantic** — LLM can understand from name alone
- [ ] **Cardinal sin identified** — Maps to one in CARD.yml
- [ ] **Original preserved** — Exact text, not paraphrased
- [ ] **Analysis explains WHY** — Not just what, but why it's wrong
- [ ] **Correction is concrete** — Shows the right way
- [ ] **Lesson is one line** — Extractable takeaway

## What Makes a Good Example

**High Value:**
- Common patterns others will encounter
- Clear violation with clear fix
- Teaches a generalizable lesson
- Original text is available verbatim

**Low Value:**
- Edge cases unlikely to recur
- Ambiguous violations
- Missing original text
- No clear lesson

## The Bigger Picture

### Play → Learn → Lift

Your example follows the MOOLLM methodology:
1. **Play** — You encountered AI in the wild
2. **Learn** — You noticed the pattern
3. **Lift** — You're extracting it as a reusable schema

### Directories as Interests

The `examples/` directory IS the semantic index:

```
ls examples/
→ 2026-01-24-tapestry-of-innovation-wikipedia.yml
→ 2026-01-25-great-question-trivial-math.yml
→ 2026-01-26-hallucinated-citation-fake-paper.yml
```

An LLM listing this directory immediately understands what violations exist. Your filename is a K-line — it activates semantic understanding.

### Crowdsourced Reinforcement

Each PR grows the corpus. Each example teaches the pattern. The more diverse the catches, the more robust the learning.

**You're not just documenting — you're training.**

## Questions?

Open an issue or check `CARD.yml` for the full list of cardinal sins.
