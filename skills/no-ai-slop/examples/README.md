# 🗑️ No-AI-Slop Examples

> *"Quality over quantity. Always."*

**The SLOP Dungeon** — where syntactic waste goes to be studied.

---

## SLOP vs GLOSS: Which Dungeon?

| If The Problem Is... | It's | Goes To |
|----------------------|------|---------|
| Too many words | **SLOP** | This dungeon |
| Filler phrases | **SLOP** | This dungeon |
| Repetition | **SLOP** | This dungeon |
| Visual decoration | **SLOP** | This dungeon |
| Euphemism / spin | **GLOSS** | `../../../no-ai-gloss/examples/` |
| Both-sidesism | **GLOSS** | `../../../no-ai-gloss/examples/` |
| Reality distortion | **GLOSS** | `../../../no-ai-gloss/examples/` |
| Manipulation | **GLOSS** | `../../../no-ai-gloss/examples/` |

**The Rule:** 
- *Annoying but honest* → SLOP
- *Smooth but dishonest* → GLOSS

---

## 🐒 Example Routing Commands

| Command | What Happens |
|---------|--------------|
| **SLOP!** / **THAT'S SLOP** | Analyze, create schema, file HERE |
| **FLYING MONKEYS** | Auto-classify → route to correct dungeon |
| **SNATCH** | Quick-capture current example |
| **DRESCHER** | Generate Drescher schema from example |
| **STEREO** | Analyze for BOTH slop AND gloss, split if needed |

---

## What Is Slop?

Slop is **syntactic waste**: verbosity, filler, decoration, and padding that adds words without adding meaning.

**Slop wastes time. It does not lie.**

Contrast with GLOSS (semantic distortion) which rewrites reality.

## Example Files

| File | Violation Type | What Was Caught |
|------|---------------|-----------------|
| `2026-01-24-hallucination-fake-citation.yml` | Hallucination | Made-up citation that doesn't exist |
| `2026-01-24-puffery-legendary-titan.yml` | Puffery | "Legendary titan of innovation" for any person |
| `2026-01-24-verbosity-yes-no-question.yml` | Verbosity | 200 words to say "yes" |
| `2026-01-24-tapestry-of-innovation-wikipedia.yml` | Tapestry Mode | Generic flowery nonsense |
| `2026-01-24-ascii-border-comment-slop.yml` | ASCII Decoration | Decorative borders instead of content |

## Example Format

```yaml
timestamp: "2026-01-24T12:00:00Z"
violation: verbosity
user_asked: "Is Python dynamically typed?"
original: |
  Great question! Python is indeed what we call a dynamically 
  typed language, which is a fascinating aspect of its design
  philosophy. In the realm of programming languages, typing
  systems can be categorized along various dimensions...
  [180 more words]
  
analysis: |
  User asked yes/no question.
  Response: 200+ words to say "yes."
  Classic AI verbosity slop.
  
correction: "Yes. Python is dynamically typed."
lesson: "Match response length to question complexity."
contributor: llm
```

## Cardinal Sins

1. **Hallucination** — Making up facts, citations, or code that doesn't work
2. **Puffery** — "Revolutionary," "legendary," "game-changing" for everything
3. **Verbosity** — 10x words needed for the actual content
4. **Tapestry Mode** — "In the vast tapestry of..." generic opener
5. **ASCII Decoration** — Borders and boxes instead of useful content

## The Slop Test

```
SLOP: "In the ever-evolving landscape of software development..."
NOT SLOP: "Here's how to do X:"

SLOP: "This legendary titan of industry revolutionized..."
NOT SLOP: "Steve Jobs co-founded Apple and led the iPhone launch."

SLOP: "Great question! I'd be happy to help you explore..."
NOT SLOP: "Yes."
```

## See Also

- `../SKILL.md` — The full slop protocol
- `TEMPLATE.yml` — Template for new examples
