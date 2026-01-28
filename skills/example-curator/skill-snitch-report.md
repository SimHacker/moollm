# Skill Snitch Report: example-curator

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** ANALYZE INCOMING EXAMPLES, EVOLVE CANONICAL CORPUS

---

## Executive Summary

**Generic worker pattern for corpus evolution.**

Timestamped examples → cluster → evolve → canonical corpus.

Can curate itself. Recursion warning.

---

## Process

```
CONTRIBUTORS       CURATOR           CORPUS
     │                │                │
     ▼                ▼                ▼
   CATCH          ANALYZE          CANONICAL
     │                │            EXAMPLES
     ▼                ▼                │
   SUBMIT         PATTERNS            ▼
(timestamped)         │            TRAINING
     │                ▼              DATA
     └────────► EVOLVE ◄──────────    │
              CANONICAL               ▼
                                   BETTER AI
```

---

## Actions

| Action | Purpose |
|--------|---------|
| **PROMOTE** | Timestamped → timeless |
| **MERGE** | Multiple → one richer |
| **ABSTRACT** | Concrete → general schema |
| **REFINE** | Update with new evidence |
| **DEPRECATE** | Mark as outdated |
| **CREDIT** | Attribute contributors |

---

## Worker Modes

| Mode | Trigger | Output |
|------|---------|--------|
| **Interactive** | `CURATE <path>` | Proposals for review |
| **Autonomous** | Scheduled/threshold | PR for approval |
| **Advisory** | On submission | Similarity suggestions |

---

## Pattern Finding

- **cluster_similar** — Group same anti-pattern
- **identify_unique** — Flag novel patterns
- **detect_drift** — Notice outdated canonicals
- **spot_gaps** — Find timestamps not in canonical

---

## Security Assessment

### Concerns

1. **Recursion** — can curate itself
2. **Attribution** — credit must be preserved

### Mitigations

- CREDIT action explicit
- Human approval required

**Risk Level:** LOW — structured corpus evolution

---

## Verdict

**CORPUS EVOLUTION WORKER. APPROVE.**

Analyze incoming. Evolve canonical.

This skill can curate itself.
