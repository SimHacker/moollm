# Skill Snitch Report: world-generation

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** QUESTIONS CREATE PLACES

---

## Executive Summary

**Dynamic world creation.**

Ask about a place and it exists. Exploration IS creation.

"What's north?" makes north exist.

---

## The Principle

> "Don't pre-generate everything. Generate on demand."

Questions expand the world. The undefined becomes defined when observed.

---

## Methods

| Method | Purpose |
|--------|---------|
| **CREATE** | Generate a new place |
| **EXPAND** | Add to existing area |
| **CONNECT** | Link two areas |
| **TOWER** | Generate vertical structure |
| **FLOOR** | Add floor to tower |

---

## Tower Generation

```yaml
TOWER:
  name: "No-AI Tower"
  floors:
    - ground: "lobby, security desk"
    - 1: "offices"
    - 2: "server room"
    - rooftop: "helipad"
  central_column: "elevator"
```

Generates directory structure with linked floors.

---

## Security Assessment

### Concerns

1. **Infinite expansion** — world grows unbounded
2. **Inconsistency** — generated places conflict
3. **Directory explosion** — too many rooms

### Mitigations

- Coherence engine checks consistency
- Generation respects existing world
- Lazy creation means only what's needed

**Risk Level:** LOW — creation is additive

---

## Verdict

**GENERATIVE EXPLORATION. APPROVE.**

Ask about a place and it exists.

Questions create reality.
