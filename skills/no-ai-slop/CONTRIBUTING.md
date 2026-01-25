# Contributing to No-AI-Slop

> **Submit your catches. Grow the corpus. Train better AI.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI violations caught in the wild, documented as learning schemas, submitted via PR.

Each example is a **Drescher schema**: a situation-response pair that teaches the correct behavior. The examples/ directory IS the training data.

---

## Privacy-First Workflow

**You are under NO obligation to contribute.** Your examples can remain entirely private.

### Two Locations, Standard Git Flow

```
┌─────────────────────────────────────────────────────────────────┐
│  PRIVATE (default)                                              │
│  .moollm/skills/no-ai-slop/examples/                           │
│  → Gitignored — never leaves your machine                      │
│  → Your personal catches, your user profile                    │
│  → Compiled into .cursorrules for YOUR sessions                │
│  → MOOFS layer: overrides repo versions locally                │
├─────────────────────────────────────────────────────────────────┤
│  REPO (shareable)                                               │
│  skills/no-ai-slop/examples/                                   │
│  → Git-tracked — edit in place                                 │
│  → When you edit, git sees changes (git diff)                  │
│  → Drescherize your changes before committing                  │
│  → git add / commit / push / PR                                │
└─────────────────────────────────────────────────────────────────┘
```

When you edit files in `skills/*/examples/`, git tracks them as modified.
That's your "working" state — changes you INTEND to share.
Drescherize before you commit.

### Keeping Examples Private

Your examples are YOUR user profile. To keep them private:

1. **Store in `.moollm/`** — gitignored, never committed
2. **Compile into `.cursorrules`** — the optimizer can include your examples in your personal boot context
3. **Learn from them yourself** — they improve YOUR sessions

```bash
# Your private examples location
.moollm/skills/no-ai-slop/examples/
  my-catch-2026-01-24.yml
  personal-pattern-1.yml
  ...
```

The compiler (`cursor-mirror optimize`) can read your private examples and incorporate their lessons into your `.cursorrules` without sharing the raw data.

---

## Choosing to Share

If you WANT to contribute, we make it easy — but intentional.

### The Drescherization Process

**Before sharing, integrate your examples with the existing corpus:**

```
DON'T: Dump raw examples into the PR
DO:    Drescherize — refine and integrate
```

**Four ways to Drescherize:**

1. **ADD NEW UNIQUE** — Your example catches a pattern not yet documented
   ```yaml
   # New file: 2026-01-25-quantum-buzzword-abuse.yml
   # (No existing example for quantum BS)
   ```

2. **MERGE VIA SUB-EXAMPLES** — Your catch is a variant of an existing pattern
   ```yaml
   # Existing: 2026-01-24-tapestry-of-innovation.yml
   # Your addition: Add a sub_examples section
   sub_examples:
     - variant: "tapestry of understanding"
       source: "Your catch"
     - variant: "rich fabric of possibilities"
       source: "Your catch"
   ```

3. **ABSTRACT TO SCHEMA** — Multiple specific examples reveal a general pattern
   ```yaml
   # Before: 3 separate files for similar violations
   # After: 1 schema file with 3 instances
   pattern:
     name: "metaphor-inflation"
     description: "Using grand metaphors for mundane topics"
     instances:
       - tapestry-of-innovation
       - rich-fabric-of
       - symphony-of-progress
   ```

4. **FINE-TUNE EXISTING** — Improve an existing example's analysis
   ```yaml
   # Existing example had weak analysis
   # Your PR improves the explanation, adds see_also links
   ```

### Why Drescherize?

- **Prevents corpus bloat** — 50 good schemas > 500 redundant examples
- **Reveals patterns** — Abstraction is where learning happens
- **Protects privacy** — Your raw catches get transformed, not exposed
- **Adds value** — Fine-tuning is as valuable as new examples

---

## How to Contribute

### 1. Catch a Violation

You see AI slop in the wild:
- Verbosity where brevity would do
- Filler phrases ("tapestry of innovation")
- Hallucinated citations
- "Great question!" cheerleading
- Over-enthusiasm for mediocre content

### 2. Document It

Create a YAML file. Two naming patterns:

#### Timestamped Examples (Lower Bar — Submit These!)

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

- **Lower bar** — your raw catch, dated
- Just document what you found
- Can be mass-analyzed and promoted later

**Good names:**
- `2026-01-24-tapestry-of-innovation-wikipedia.yml`
- `2026-01-25-great-question-trivial-math.yml`

#### Timeless Examples (Primary/Canonical)

```
{descriptive-iconic-name}.yml
```

- **No date prefix** — considered "eternal", primary
- Promoted from timestamped examples after mass review
- THE canonical example for this pattern

**Good names:**
- `tapestry-of-innovation.yml` (the pattern)
- `great-question-trivial.yml` (the archetype)

#### Promotion Lifecycle

```
CATCH → SUBMIT (timestamped) → ANALYZE (mass review) → PROMOTE (timeless)
```

Many timestamped catches → analysis reveals the best → promote to eternal.

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

---

## The Full Workflow

### 1. COLLECT (Private — Default)

```bash
# Catch violations, document in your user profile
# This is YOUR space — stays private forever by default

cp skills/no-ai-slop/examples/TEMPLATE.yml \
   .moollm/skills/no-ai-slop/examples/my-catch-2026-01-25.yml

# Edit, refine, collect more...
# The compiler can learn from these without exposing them
```

### 2. PROMOTE (Intentional — Ask First)

```bash
# Decide to share? PROMOTE from private to working copy
# This is the intentional step — you're choosing to contribute

cp .moollm/skills/no-ai-slop/examples/my-catch-2026-01-25.yml \
   skills/no-ai-slop/examples/2026-01-25-descriptive-name.yml

# Now it's in the repo. Git sees it.
```

### 3. DRESCHERIZE (In Working Copy)

```bash
# Edit in place. Integrate with existing corpus.
ls skills/no-ai-slop/examples/    # What exists?
git diff                           # What are you changing?

# Merge, abstract, refine — don't just dump
vim skills/no-ai-slop/examples/2026-01-25-descriptive-name.yml
```

### 4. COMMIT & PR (Celebrate!)

```bash
# Nice commit message, push, PR
git checkout -b example/no-ai-slop/descriptive-name
git add skills/no-ai-slop/examples/
git commit -m "$(cat <<'EOF'
example: VERBOSITY - 500 words for yes/no question

Catches the common pattern where AI responds to binary questions
with paragraphs of unnecessary context. Includes analysis of
cheerleading opener and correction showing direct answer.

Drescherized: Checked existing examples, this pattern not yet documented.
EOF
)"
git push -u origin HEAD
gh pr create --title "example: VERBOSITY - 500 words for yes/no question"

# 🎉 Celebrate!
```

### What NOT to Share

- **Personal context** — Scrub identifying information
- **Employer data** — No proprietary conversations  
- **Raw dumps** — Always Drescherize first
- **Duplicates** — Check existing examples

### Compiler Integration

The `cursor-mirror` optimizer reads your private examples:

```bash
# Your private overrides
.moollm/skills/no-ai-slop/examples/

# Compiled into your .cursorrules
# Lessons extracted, raw data not exposed
cursor-mirror optimize --include-private-examples
```

Your catches improve YOUR sessions even if you never share.

---

## Summary

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

## Questions?

Open an issue or check `CARD.yml` for the full list of cardinal sins.
