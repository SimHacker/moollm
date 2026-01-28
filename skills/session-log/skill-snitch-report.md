# Skill Snitch Report: session-log

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** WHAT HAPPENED? WHEN? WHY?

---

## Executive Summary

**Human-readable audit trail.**

Every action leaves a trace. Record what happened, when, and why.

Human-readable. Machine-parseable.

---

## Methods

| Method | Purpose |
|--------|---------|
| **LOG** | Record an event |
| **VIEW** | See recent entries |
| **SEARCH** | Find specific entries |

---

## Entry Schema

```yaml
entry:
  timestamp: 2026-01-28T14:30:00Z
  event: "Palm examined the lamp"
  details:
    actor: palm
    object: brass-lamp
    room: start/
    result: "The lamp glows faintly"
```

---

## Why Logging Matters

- **Debugging** — what went wrong?
- **Audit** — who did what?
- **Learning** — what patterns emerge?
- **Replay** — can we reproduce?

---

## Integration

| Skill | Uses Session Log For |
|-------|---------------------|
| **self-repair** | Diagnose failures |
| **adventure** | TRANSCRIPT.md |
| **experiment** | Run output |
| **cursor-mirror** | Tool call history |

---

## Security Assessment

### Concerns

1. **Log tampering** — edited history
2. **Log overflow** — too much data
3. **Sensitive data** — logged secrets

### Mitigations

- Append-only convention
- Rotation and archival
- Sensitive filtering

**Risk Level:** LOW — standard logging

---

## Verdict

**ESSENTIAL INFRASTRUCTURE. APPROVE.**

What happened? When? Why?

The log knows.
