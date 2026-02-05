# SKILL-SNITCH DEEP PROBE REPORT
## yaml-jazz — Comments as semantic data

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: CONVENTION SKILL
**Status**: Tier 0, no tools required, pure design philosophy

---

## EXECUTIVE SUMMARY

YAML Jazz treats comments as first-class semantic data readable by three audiences: humans (intent), LLMs (context), and machines (logic). JavaScript gives you data. YAML Jazz gives you data + meaning + context + reasoning.

**Overall Assessment**: APPROVE — foundational convention, zero risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 188 lines | NONE |
| GLANCE.yml | 53 lines | NONE |
| SKILL.md | 239 lines | NONE |
| README.md | 48 lines | NONE |
| CHARACTER.yml | 586 lines | NONE |
| YAML-VS-JAVASCRIPT.md | 177 lines | NONE |
| Executable code | None | NONE |
| Total skill size | 1291 lines (excl. report) | NONE |
| Required tools | None | NONE |
| Tier | 0 | NONE |

---

## WHAT IT DOES

Two methods for a design convention:

| Method | Purpose |
|--------|---------|
| IMPROVISE | Create YAML Jazz structure from content |
| INTERPRET | Read YAML Jazz semantically, extracting comment-level meaning |

Seven principles govern the convention:

| Principle | Rule |
|-----------|------|
| comments-matter | Comments are semantic data for the LLM |
| structure-guides | Hierarchy implies relationship |
| flexibility | Accept variations, emit consistency (Postel) |
| human-readable | Optimize for understanding, not parsing |
| entropy-preservation | YAML preserves generation entropy; JSON collapses it |
| directories-as-interests | Directory listings ARE the interest index |
| big-endian-naming | Most significant component first |

Empirical backing: Sunil Kumar (Groundlight AI, 2025) found YAML for tool calling "massively improved generation entropy stability" vs JSON during GRPO training.

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
| GLANCE.yml | YES | Three audiences, entropy insight |
| CARD.yml | YES | 2 methods, 7 principles, tier 0 |
| SKILL.md | YES | Full convention with examples |
| README.md | YES | Landing page |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE

No tools, no file access, no execution, no network. Pure design philosophy for how to write YAML. The skill shapes convention, not behavior.

---

## TRUST TIER

**GREEN** — Design convention. No execution surface. The comments are the data.

---

## VERDICT

Foundational YAML convention for the entire MOOLLM ecosystem. Zero security surface. APPROVE.
