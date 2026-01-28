# Skill Snitch Report: self-repair

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE DEMON WATCHES. THE DEMON HEALS.

---

## Executive Summary

**Checklist-based self-healing.**

Missing state triggers repair. The repair demon watches for problems.

---

## Checklist Items

- Required files exist
- YAML is valid
- References resolve
- State is consistent
- No orphaned files

---

## Methods

| Method | Purpose |
|--------|---------|
| **CHECK** | Run repair checklist |
| **REPAIR** | Fix identified issues |
| **STATUS** | Show repair demon status |

---

## The Repair Demon Pattern

```
startup → CHECK → issues found?
    ↓
  yes → REPAIR → create missing, fix state
    ↓
continue with healthy system
```

---

## When to Run

| Trigger | Purpose |
|---------|---------|
| **startup** | Clean start |
| **periodic** | Catch drift |
| **strange behavior** | Something's wrong |

---

## Integration with robust-first

This is the operational implementation of robust-first philosophy:
- Prioritize survival
- Graceful degradation
- Self-repair over crash

---

## Security Assessment

### Concerns

1. **Auto-repair side effects** — unintended changes
2. **Repair loops** — fix causes new problem

### Mitigations

- Repairs logged
- Checklist explicit
- Status visible

**Risk Level:** LOW — healing, not hurting

---

## Verdict

**SELF-HEALING SYSTEMS. APPROVE.**

The demon watches. The demon heals.

Missing files appear. Invalid state repairs.
