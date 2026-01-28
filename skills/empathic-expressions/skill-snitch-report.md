# Skill Snitch Report: empathic-expressions

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE LLM AS COMPILER

---

## Executive Summary

**Intent-based code interpretation across all languages.**

> "Understand intent, generate correct code, teach gently."

One pipeline. Many syntaxes. Code-switching supported.

---

## The Core Insight

Traditional compiler: exact syntax required.
Empathic expressions: **intent is enough**.

| Input | Output |
|-------|--------|
| Fuzzy description | Working code |
| Wrong syntax | Correct syntax |
| Pseudocode | Real code |
| Typos | Fixed code |

---

## Methods

| Method | Purpose |
|--------|---------|
| **INTERPRET** | Understand fuzzy/approximate code |
| **GENERATE** | Produce correct, idiomatic code |
| **TEACH** | Echo back correct form as gift |
| **CLARIFY** | Ask when ambiguous |
| **SWITCH** | Handle code-switching between languages |

---

## Languages Supported

| Type | What It Does |
|------|--------------|
| empathic-sql | Natural language → SQL |
| empathic-python | Intent → Python |
| empathic-javascript | Behavior → JS/TS |
| empathic-bash | Tasks → shell commands |
| empathic-yaml | Structure → YAML Jazz |
| empathic-natural | Vague → specific in any language |

---

## Generous Interpretation

**Accepts:**
- Fuzzy syntax
- Vernacular descriptions
- Misspellings and typos
- Wrong language (will translate)
- Pseudocode
- Incomplete fragments

**Generates:**
- Correct syntax
- Idiomatic patterns
- Best practices
- Appropriate comments
- Edge case handling

**Teaches:**
- Shows input → output mapping
- Explains interpretations
- Gentle, not pedantic
- Gift, not correction

---

## Clarification Protocol

| Stakes | Clarity | Action |
|--------|---------|--------|
| Low | Clear | Interpret and proceed |
| Low | Ambiguous | Make reasonable choice, note it |
| High | Clear | Proceed with confirmation |
| High | Ambiguous | **ASK FIRST** |

**High-stakes triggers:**
- DELETE operations
- DROP TABLE
- Production deployments
- Payment processing
- User data exports
- Irreversible operations

---

## Code-Switching

```python
# Start in Python
users = get_all_users()

# Switch to SQL (explicit)
```sql
SELECT * FROM orders WHERE user_id IN (?)
```

# Back to Python (implicit from context)
for user in users:
    orders = run_query(query, user.id)
```

Variables and context preserved across switches.

---

## The LLM as Code Processor

| Role | Function |
|------|----------|
| **Pseudocode interpreter** | Executes high-level intent |
| **Empathic pretty-printer** | Formats with understanding |
| **Generous linter** | Catches errors, suggests kindly |
| **Intent compiler** | Translates intent → working code |
| **Depseudofier** | Converts vague to precise |

---

## Used In

| System | Use |
|--------|-----|
| empathic-templates | `{{expressions}}` in templates |
| buff-expressions | Trigger conditions |
| advertisements | Capability conditions |
| action-queue | Dynamic parameters |
| mind-mirror | Fuzzy state descriptions |
| room-exits | Gate conditions |

---

## Security Assessment

### Concerns

1. **Code generation** — produces executable code
2. **High-stakes operations** — could be destructive
3. **Intent misinterpretation** — wrong code generated

### Mitigations

- Clarification protocol for high stakes
- ASK FIRST on dangerous operations
- Generated code visible before execution

**Risk Level:** MEDIUM — mitigated by clarification protocol

---

## Relationship to Postel

| Postel | Empathic Expressions |
|--------|---------------------|
| Accept messy input | Accept fuzzy code |
| Emit clean output | Emit correct code |
| Ask if unsure | Clarify on ambiguity |

Empathic expressions ARE Postel's Law applied to code.

---

## Verdict

**THE LLM AS A COMPILER. APPROVE.**

The insight: LLMs understand intent. Use that understanding.

Accept pseudocode. Generate working code. Teach gently.

The compiler of the future accepts natural language.
