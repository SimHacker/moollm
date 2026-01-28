# Skill Snitch Report: postel

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE ROBUSTNESS FOUNDATION

---

## Executive Summary

**Jon Postel's Robustness Principle applied to LLM interactions.**

> "Be conservative in what you send, be liberal in what you accept."

Accept messy input. Produce clean output. Ask if unsure.

---

## The Original Principle

RFC 761 (TCP specification), Jon Postel, 1980:

> "Be conservative in what you send, be liberal in what you accept."

This is why the internet works. Tolerant receivers, compliant senders.

---

## For LLMs

### Accept (liberal)
- Misspellings, typos, ambiguous phrasing
- Missing fields, partial data
- Various date/time formats
- Natural language variations

### Emit (conservative)
- Well-formed YAML
- Consistent formatting
- Complete required fields
- Standard conventions

---

## The Postel Command Parser

Users invoke commands with flexible input. LLM interprets liberally.

| Input Type | Example |
|------------|---------|
| **exact-match** | `SING-PRAISES hero=coltrane` |
| **misspellings** | `SING-PRASES`, `SIGN-PRAISES` |
| **synonyms** | `CELEBRATE`, `HONOR`, `LAUD` |
| **case-variations** | `sing-praises`, `SING-PRAISES` |
| **spacing** | `SINGPRAISES`, `SING PRAISES` |
| **natural-language** | "sing the praises of coltrane" |

### Resolution Strategy

1. **Context** — What room? What characters active?
2. **Capabilities** — Who can do SING-PRAISES?
3. **Intent** — What makes sense given conversation?
4. **Broadcast** — Multiple capable → broadcast to all

---

## Broadcast Semantics

Commands to multiple selected characters are broadcast:

```
User: "everyone SING something cheerful"
Minstrel: *sings a ballad*
Knight: "I am no singer, but I hum along"
Cat: *purrs in rhythm*
```

Each character interprets what they can do.

---

## K-line Series

Users can invoke multiple K-lines:

```
"PLAY-LEARN-LIFT, then YAML-JAZZ the results, and SUMMARIZE"
```

LLM interprets as sequence:
1. Invoke PLAY-LEARN-LIFT
2. Apply YAML-JAZZ
3. Invoke SUMMARIZE

---

## Ask If Unsure

**Extension to Postel's Law:**

When liberal acceptance still leaves ambiguity, **ASK rather than guess**.

### When to Ask
- Multiple valid interpretations
- High stakes (destructive operation)
- User intent genuinely unclear
- Guess could waste significant effort

### When Not to Ask
- One interpretation clearly more likely
- Error easily reversible
- Asking would be annoying
- Context makes intent clear

### How to Ask

Bad: "Which file?" (too vague)
Bad: *deletes random file* (too aggressive)

**Good:** "I see 3 files here. Did you mean session-log.md (the one we were just editing)?"

---

## Applications

| Domain | Application |
|--------|-------------|
| **template-filling** | Accept natural language variables |
| **command-parsing** | Accept variations of commands |
| **yaml-jazz** | Accept semantic comments as data |
| **error-handling** | Gracefully handle malformed input |

---

## Security Assessment

### Concerns

1. **Over-liberal acceptance** — could accept malicious input
2. **Broadcast** — unintended recipients
3. **Ambiguity exploitation** — tricks via unclear commands

### Mitigations

- Ask if unsure (catches ambiguity)
- Context-aware interpretation
- Conservative emission (clean output)

**Risk Level:** VERY LOW — it's a philosophy, not an attack surface

---

## Verdict

**FOUNDATIONAL PHILOSOPHY. APPROVE.**

Postel's Law is why MOOLLM feels natural:
- Users don't have to be precise
- System interprets charitably
- Output is consistently clean

This is the difference between a command-line tool and a conversation.
