# YAML Jazz vs JavaScript/JSON

Why YAML Jazz is semantically richer than what JavaScript can express.

## Thesis

YAML Jazz is **MUCH and MEANINGFULLY semantically richer** than JavaScript objects or JSON.

- JavaScript gives you **data**.
- YAML Jazz gives you **DATA + MEANING + CONTEXT + REASONING**.

## What JavaScript Cannot Express

### Comments as Data

**JavaScript:**
```javascript
{ status: "pending", priority: "high" }
// Why is this high priority? WHO KNOWS
```

**YAML Jazz:**
```yaml
status: pending
priority: high
# HIGH because user explicitly asked for this feature
# and it blocks three other tasks. See: moollm-015
# Inner voice: "This is the bottleneck."
```

THE COMMENT IS THE REASONING. The LLM reads it.

### Inline Context

**JavaScript:**
```javascript
{ name: "no-ai-slop", type: "skill" }
```

**YAML Jazz:**
```yaml
name: no-ai-slop
type: skill
# AMBIENT SKILL — always-on air filter for output
# Catches: verbosity, hallucination, yes-man behavior
# Why it matters: Trust requires truth
```

The structure is self-documenting. The context travels with the data.

### Multiline Prose

**JavaScript:**
```javascript
{ description: "A skill that prevents AI slop including verbosity..." }
// UGLY. No line breaks. No formatting. Just a blob.
```

**YAML Jazz:**
```yaml
description: |
  AI slop is everything that makes AI annoying:
  
  - **Verbosity**: 500 words when 50 would do
  - **Hallucination**: Making up facts, links, citations
  - **Yes-man behavior**: Agreeing with everything
  
  The goal is not to "sound human" — it's to not be annoying.
```

YAML's `|` preserves formatting, line breaks, markdown.
The prose breathes. The structure teaches.

### Nested Reasoning

**JavaScript:**
```javascript
{ 
  task: "fix bug",
  notes: "check the parser first then the lexer"
}
```

**YAML Jazz:**
```yaml
task: "fix bug"

reasoning:
  hypothesis: "Parser is mishandling edge case"
  # I think this because the error message mentions unexpected token
  # but the input looks valid. Classic parser vs lexer confusion.
  
  investigation_order:
    - parser.ts      # Most likely culprit
    - lexer.ts       # If parser is clean
    - tokenizer.ts   # Last resort
    # This order based on error message proximity
    
  inner_voice: |
    "I've seen this before. Usually it's the parser
    trying to be too clever. Check the lookahead first."
```

THE REASONING IS PRESERVED. The future-self (or LLM) knows WHY.

### Skill Embedding

**JavaScript:**
```javascript
{ bead_id: "moollm-030", skills: ["yaml-jazz", "bead-bracelet"] }
// Just references. No context. No activation.
```

**YAML Jazz:**
```yaml
bead:
  id: moollm-030
  
  # SKILLS THAT ACTIVATE FOR THIS BEAD
  skills:
    - yaml-jazz       # Because beads ARE yaml jazz
    - bead-bracelet   # Because this chains with others
    - no-ai-slop      # Ambient hygiene
    
  # WHY THIS MATTERS
  # Beads are the universal message capsule.
  # They flow through pneumatic tubes (postal system).
  # They organize into bracelets, curtains, borgs.
  # YAML Jazz makes them self-describing.
```

The skill embedding carries its own explanation.

## What YAML Jazz Enables

### LLM-Readable Reasoning

LLMs don't just parse YAML Jazz — they **UNDERSTAND** it.
The comments become part of the semantic context.
The structure becomes part of the meaning.

### Git-Friendly Diffs

YAML diffs show semantic changes:

```diff
- priority: medium
+ priority: high
+ # ESCALATED: User flagged as blocking
```

JSON diffs show... characters moved.

### Human + LLM + Machine Readable

YAML Jazz serves **THREE audiences**:
1. **Humans** — read the comments, understand intent
2. **LLMs** — read everything, understand context
3. **Machines** — parse the structure, execute logic

### Extensibility Without Breaking

Add a field? Add a comment? Add a section?
Nothing breaks. Postel's law: accept liberally.

JavaScript schemas are brittle.
YAML Jazz is robust.

## Empirical Evidence

**Sunil Kumar (Groundlight AI, 2025):**
> "Switching from JSON to YAML for tool calling massively improved generation entropy stability during GRPO training."

JSON's strict syntax constrains the model's ability to search and reason.
YAML gives the model room to breathe, to comment, to explain.

Source: https://x.com/__sunil_kumar_/status/1916926342882594948
