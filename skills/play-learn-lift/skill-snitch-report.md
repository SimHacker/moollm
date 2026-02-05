# SKILL-SNITCH DEEP PROBE REPORT
## play-learn-lift — Jazz first, then standards

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: METHODOLOGY SKILL
**Status**: Tier 1, requires read_file and write_file

---

## EXECUTIVE SUMMARY

Three-stage knowledge development cycle: PLAY (explore freely, fail safely), LEARN (notice patterns, document), LIFT (share as reusable skill). The anti-pattern is Lift-Learn-Play — writing specs nobody tested. Jazz musicians are good because they played before they studied.

**Overall Assessment**: APPROVE — pure methodology, minimal risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 131 lines | NONE |
| GLANCE.yml | 54 lines | NONE |
| SKILL.md | 282 lines | NONE |
| README.md | 52 lines | NONE |
| Templates (.tmpl) | 2 files, 102 lines | NONE |
| Executable code | None | NONE |
| Total skill size | 621 lines (excl. report) | NONE |
| Required tools | read_file, write_file | LOW |
| Tier | 1 | LOW |

---

## WHAT IT DOES

Four methods for the development cycle:

| Method | Purpose | Output |
|--------|---------|--------|
| PLAY | Enter exploration mode | Guidance, framing |
| LEARN | Reflect on patterns | Documented learnings |
| LIFT | Share as reusable skill | Skill files |
| STAGE | Assess current stage | Status check |

The cycle:
```
PLAY → discoveries → LEARN → patterns → LIFT → skills → (repeat)
```

Session state tracks stage, domain, explorations, patterns, and outputs. Templates (CYCLE.yml.tmpl, PLAY_LOG.md.tmpl) scaffold the process.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Three stages, jazz principle |
| CARD.yml | YES | 4 methods, tier 1, templates listed |
| SKILL.md | YES | Full methodology with anti-pattern documentation |
| README.md | YES | Landing page |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

| Concern | Severity | Detail |
|---------|----------|--------|
| File creation via LIFT | LOW | LIFT stage creates skill files. Output goes to designated skill directories. |
| Learning artifacts | LOW | Documentation produced during LEARN could contain session-specific information. |

Mitigations: all outputs are visible files, user controls what gets lifted, skill files go to standard locations. The methodology itself has no execution capability — it shapes how the LLM approaches tasks.

---

## TRUST TIER

**GREEN** — Methodology skill. Shapes behavior, doesn't execute. File writes are the standard skill creation path.

---

## VERDICT

The MOOLLM development methodology. LOW risk from LIFT-stage file creation, otherwise pure cognitive framing. APPROVE.
