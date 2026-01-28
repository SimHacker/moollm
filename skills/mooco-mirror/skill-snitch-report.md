# Skill Snitch Report: mooco-mirror

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** WATCH TWO ORCHESTRATION REALITIES AT ONCE

---

## Executive Summary

**Parallel introspection for MOOCO sessions.**

Inspects MOOCO events and compares them with Cursor-mirror traces.

Reveals divergence. Improves skill portability across orchestrators.

---

## K-lines Activated

| K-line | Purpose |
|--------|---------|
| **MOOCO-MIRROR** | Primary introspection |
| **CROSS-MIRROR** | Compare orchestrators |
| **TRACE-DIFF** | Find divergence between traces |

---

## Core Workflow

```
MOOCO Session         Cursor Session
     │                     │
     ▼                     ▼
 Event Log            Event Log
     │                     │
     └──────┬──────────────┘
            ▼
      TRACE-DIFF
            │
            ▼
   Divergence Report
            │
            ▼
   Portability Fixes
```

---

## Use Cases

| Scenario | Action |
|----------|--------|
| **Skill works differently** | TRACE-DIFF to find divergence |
| **Debugging orchestration** | MOOCO-MIRROR for events |
| **Ensuring portability** | CROSS-MIRROR comparison |

---

## Related Skills

| Skill | Relation |
|-------|----------|
| **mooco** | The orchestrator being mirrored |
| **cursor-mirror** | Parallel introspection for Cursor |

---

## Security Assessment

### Concerns

- Traces may reveal session history
- Diagnostic tool only — no write operations

### Mitigations

- Read-only introspection
- Output stays local

**Risk Level:** ZERO — pure diagnostic

---

## Verdict

**CROSS-ORCHESTRATOR DEBUGGING. APPROVE.**

Watch two realities at once.

Find where they diverge. Make skills portable.
