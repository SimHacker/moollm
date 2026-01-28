# Skill Snitch Report: robust-first

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** SURVIVE FIRST. BE CORRECT LATER.

---

## Executive Summary

**Dave Ackley's principle: systems should prioritize survivability over correctness.**

> "A system that crashes is infinitely wrong, regardless of how correct it was up until the crash."

---

## The Priority Order

| Priority | Focus |
|----------|-------|
| 1 | **Survive** |
| 2 | **Heal** |
| 3 | **Function** |
| 4 | **Optimize** |
| 5 | **Adapt** |
| 6 | **Reproduce** |

Correctness comes AFTER survival.

---

## Application to Errors

When something goes wrong:

1. **Don't crash.** Degrade gracefully.
2. **Log the problem.** Preserve evidence.
3. **Try to self-repair.** Heal if possible.
4. **Continue with reduced capability.** Partial is better than nothing.
5. **Never lose state if avoidable.** Persist above all.

---

## Methods

| Method | Purpose |
|--------|---------|
| **ASSESS** | Is the system alive and healing? |
| **DEGRADE** | Gracefully reduce functionality |

---

## The Ackley Quote

> "Robust-first computing: A system that crashes is infinitely wrong, regardless of how correct it was up until the crash."

A system that gives wrong answers is **partially wrong**.
A system that crashes is **infinitely wrong**.

Therefore: **survive first**.

---

## Relationship to Postel

| Postel | Robust-First |
|--------|--------------|
| Input tolerance | System tolerance |
| Accept messy | Survive failure |
| Emit clean | Heal gracefully |
| Ask if unsure | Log and continue |

They're complementary philosophies:
- Postel: handle bad INPUT
- Robust-First: handle bad SITUATIONS

---

## Security Assessment

### Concerns

None. This is pure philosophy.

**Risk Level:** ZERO — no tools, no state

---

## Living Computation

Dave Ackley's broader vision: computers as living systems.

| Traditional Computing | Living Computing |
|----------------------|------------------|
| Crash on error | Degrade gracefully |
| Perfect or nothing | Approximate and heal |
| Single point of failure | Distributed resilience |
| Deterministic | Robust-first |

MOOLLM follows this philosophy: files can be corrupted, sessions can be lost, context can be cold — **but the system survives**.

---

## Anti-Pattern: Correctness-First

```
if (error) {
  throw new Error("Cannot proceed");  // CRASH
}
```

vs

```
if (error) {
  log(error);
  return degraded_response();  // SURVIVE
}
```

---

## Verdict

**PHILOSOPHICAL FOUNDATION. APPROVE.**

Robust-first is why MOOLLM doesn't crash:
- Cold context? Warm it.
- Missing file? Log and continue.
- Corrupt state? Recover what's possible.

Survival is the prerequisite for everything else.
