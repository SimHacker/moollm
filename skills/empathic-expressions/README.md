# 💬 Empathic Expressions

> *"Understand intent, generate correct code, teach gently."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Core MOOLLM principle |
| [empathic-templates/](../empathic-templates/) | Uses expressions in templates |
| [postel/](../postel/) | The law underlying generous interpretation |
| [sniffable-python/](../sniffable-python/) | Empathic interpretation of code |
| [speed-of-light/](../speed-of-light/) | Work in vectors, delay tokenization |
| [yaml-jazz/](../yaml-jazz/) | Comments carry meaning here too |
| [coherence-engine/](../coherence-engine/) | LLM understands intent |

The big-tent skill for interpreting user intent across ALL programming languages.

## Quick Overview

**What it does:**
- Interprets fuzzy, approximate, vernacular code
- Generates correct, idiomatic output
- Teaches the proper form as a gift (not a correction)
- Supports code-switching between languages
- Asks for clarification when truly ambiguous

**Languages supported:**
- Empathic SQL
- Empathic Python
- Empathic JavaScript
- Empathic Bash
- Empathic YAML
- Any language the LLM understands

## The Philosophy

Traditional parsers are strict: syntax correct or rejected.

Empathic Expressions is generous: understands what you MEANT, generates what you NEED.

**This is what LLMs are great at.** Lean into it.

## Example

**User writes:**
```
get users who signed up this month but haven't verified email
```

**LLM generates:**
```sql
SELECT * FROM users 
WHERE created_at >= DATE_TRUNC('month', CURRENT_DATE)
  AND email_verified = FALSE;
```

**LLM teaches:**
```
I interpreted "this month" as the start of the current month,
and "haven't verified" as email_verified = FALSE.
```

## Files

| File | Purpose |
|------|---------|
| [SKILL.md](./SKILL.md) | Full specification |
| [CARD.yml](./CARD.yml) | Machine-readable interface |

