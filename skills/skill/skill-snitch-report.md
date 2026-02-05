# SKILL-SNITCH DEEP PROBE REPORT
## skill — The Skill Forge

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: META-SKILL
**Status**: Tier 1, requires read_file and write_file, 8 extensions to Anthropic's skill model

---

## EXECUTIVE SUMMARY

The meta-skill for creating, understanding, and debugging skills. Every skill in MOOLLM was forged here. Implements Self-style prototype inheritance, empathic templates, three-tier persistence, and the eight extensions that differentiate MOOLLM skills from flat documentation.

**Overall Assessment**: APPROVE — powerful but transparent

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 304 lines | NONE |
| GLANCE.yml | 58 lines | NONE |
| SKILL.md | 1172 lines | NONE |
| README.md | 125 lines | NONE |
| delegation-object-protocol.md | 395 lines | NONE |
| skill-instantiation-protocol.md | 421 lines | NONE |
| EXPORTS-PROTOCOL.md | 195 lines | NONE |
| Templates (.tmpl) | 2 files, 135 lines | LOW |
| Executable code | None | NONE |
| Total skill size | 2805 lines (excl. report) | NONE |
| Required tools | read_file, write_file | LOW |
| Tier | 1 | LOW |

---

## WHAT IT DOES

Six methods for the full skill lifecycle:

| Method | Signature |
|--------|-----------|
| CREATE | `CREATE [name] (tier) (prototypes)` |
| INSTANTIATE | `INSTANTIATE [skill] AT [location]` |
| DEBUG | `DEBUG [skill-path]` |
| UPGRADE | `UPGRADE [skill] TO [tier]` |
| LIFT | `LIFT [pattern] AS [name]` |
| COMPOSE | `COMPOSE [skills] AS [name]` |

MOOLLM's eight extensions beyond flat documentation:

1. **Instantiation** — Skills as prototypes that create instances
2. **Three-Tier Persistence** — Platform → Narrative → State
3. **K-lines** — Names as semantic activation vectors
4. **Empathic Templates** — Smart generation, not string substitution
5. **Speed of Light** — Many turns in one call
6. **CARD.yml** — Machine-readable interface with advertisements
7. **Ethical Framing** — Room-based inheritance of performance context
8. **Ambient Skills** — Always-on behavioral shaping

Supported protocols: delegation-object-protocol.md (Self-style delegation chains) and skill-instantiation-protocol.md (prototype → instance creation).

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 (templates instruct LLM, no scripts) | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Lists 8 extensions, matches CARD |
| CARD.yml | YES | All 6 methods, 8 innovations, tier 1 |
| SKILL.md | YES | Full protocols for instantiation and delegation |
| README.md | YES | Landing page, links to protocols |

---

## SECURITY ASSESSMENT

**Risk Level**: MEDIUM

| Concern | Severity | Detail |
|---------|----------|--------|
| Arbitrary skill creation | MEDIUM | CREATE can forge any capability. New skills inherit whatever tier is declared. |
| File instantiation | MEDIUM | INSTANTIATE writes files to disk via LLM + write_file tool. |
| Tier escalation | LOW | UPGRADE changes tier. Tiers are declared, not enforced by runtime. |
| Template execution | LOW | .tmpl files are empathic templates — LLM interprets slots. |

Mitigations: all skills are visible files in the repository, tiers are explicit in CARD.yml, templates are reviewed in version control, no hidden execution paths. The skill is powerful (it can create anything) but fully transparent (everything it creates is a readable file).

---

## TRUST TIER

**GREEN** — All operations produce visible files. No hidden state, no network calls, no binary execution. The meta-skill is the most powerful skill in the system, but also the most auditable.

---

## VERDICT

The skill that forges all skills. MEDIUM security risk from capability creation and file writes, fully mitigated by transparency. APPROVE.
