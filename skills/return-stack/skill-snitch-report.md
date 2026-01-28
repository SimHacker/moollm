# Skill Snitch Report: return-stack

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** REMEMBER WHERE YOU CAME FROM

---

## Executive Summary

**Navigation history as first-class continuation.**

Browser back/forward for adventure exploration.

PLUS: Self-inspired dynamic deoptimization — reconstruct causal traces after the fact.

---

## Methods

### Navigation
| Method | Purpose |
|--------|---------|
| **PUSH** | Save current position |
| **POP** | Return to previous position |
| **BACK** | Go back N steps |
| **HISTORY** | Show navigation history |
| **GOTO** | Jump to bookmarked position |

### Dynamic Deoptimization (Self-inspired)
| Method | Purpose |
|--------|---------|
| **TRACE** | Reconstruct causal trace |
| **WHY** | Ask why something has current value |
| **BLAME** | Find what caused a change |

---

## Dynamic Deoptimization

From Self (the language):

> Self aggressively inlines for performance, eliminating the return stack. But when you hit a breakpoint, it DYNAMICALLY DEOPTIMIZES — reconstructing what the stack WOULD have looked like.

**MOOLLM Application:**

MOOLLM doesn't maintain explicit call stack. But at any point it can RECONSTRUCT the causal trace:

```
🔍 CAUSAL TRACE (reconstructed):

┌─ [1] User: "TAKE the key"
├─ [2] Advertisement matched: pub/key.yml → TAKE
├─ [3] Method invoked: adventure/TAKE
├─ [4] Effect: key.location ← "inventory"
└─ [5] Narrative generated: "You pick up..."
```

---

## Security Assessment

### Concerns

1. **Privacy** — traces reveal history
2. **Storage** — traces can be large

### Mitigations

- Traces are diagnostic
- Reconstruction on demand (no overhead)

**Risk Level:** LOW — debugging tool

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Dave Ungar & Self Team** | Dynamic deoptimization |
| **Git blame** | Attribution for changes |
| **Browser** | Back/forward history |

---

## Verdict

**SELF-INSPIRED DEBUGGING. APPROVE.**

Remember where you came from.

Reconstruct what WOULD have been.
