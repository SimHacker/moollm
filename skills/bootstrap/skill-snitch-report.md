# SKILL-SNITCH DEEP PROBE REPORT
## bootstrap — The skill that became its own test case

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: SYSTEM SKILL
**Status**: Tier 1, creates .cursor/rules files, compiles templates, session initialization

---

## EXECUTIVE SUMMARY

Bootstrap initializes MOOLLM sessions: reads hot.yml, loads skills, compiles .cursor/rules from templates. During its own audit, bootstrap discovered it was ignoring its own hot.yml — diagnosed the problem via cursor-mirror, fixed itself, and invented the Semantic Image Pyramid (92% content reduction). A constructionist loop in action: the skill became its own test case.

**Overall Assessment**: APPROVE — self-healing system skill, low operational risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 181 lines | NONE |
| GLANCE.yml | 35 lines | NONE |
| SKILL.md | 620 lines | NONE |
| README.md | 123 lines | NONE |
| CONNECTIONS.md | 506 lines | NONE |
| PROBE.yml.tmpl | 223 lines | NONE |
| templates/ | .mdc.tmpl files for .cursor/rules | LOW |
| examples/ | dotcursor, dotmoollm subdirs | NONE |
| Executable code | Template compilation only | LOW |
| Total skill size | 1688+ lines (excl. report, templates, examples) | NONE |
| Required tools | read_file, write_file (for .cursor/rules) | LOW |
| Tier | 1 | LOW |

---

## WHAT IT DOES

Session initialization in three phases:

| Phase | Action |
|-------|--------|
| 1. Read priorities | Load .moollm/hot.yml — MANDATORY first read |
| 2. Load skills | Read INDEX.yml, then skill CARDs per priority |
| 3. Compile rules | Templates → .cursor/rules/*.mdc files |

### The Discovery

cursor-mirror forensics revealed the boot was broken:

| What Should Load | What Actually Loaded |
|------------------|---------------------|
| .moollm/hot.yml (mandatory) | NEVER READ |
| skills/INDEX.yml | NEVER READ |
| Skill CARDs | NONE |
| CHARACTER.yml (941 lines) | Full file, no GLANCE |
| ROOM.yml (930 lines) | Full file, no GLANCE |

Diagnosis: 1,871 lines of content loaded with 0 lines of skills to interpret it.

### The Fix: Semantic Image Pyramid

| Level | File | Lines | Question |
|-------|------|-------|----------|
| GLANCE | INDEX entry / GLANCE.yml | 5-70 | "Is this relevant?" |
| CARD | CARD.yml | 50-200 | "What can it do?" |
| SKILL | SKILL.md | 200-1000 | "How does it work?" |
| README | README.md | 500+ | "Why was it built?" |

Rule: Never load a lower level without first loading the level above.

### Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Content lines | 1,871 | 145 | -92% |
| Understanding | None | Complete | Fixed |
| hot.yml consulted | No | Yes | Fixed |

Empathic template variables in .mdc.tmpl files (`{{skill_count}}`, `{{large_files_report}}`, `{{optimization_permitted}}`) enable permission-gated runtime optimization.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | .cursor/rules/*.mdc | EXPECTED — template compilation |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Three phases, pyramid reference |
| CARD.yml | YES | Methods, tier 1, tool requirements |
| SKILL.md | YES | Full boot protocol, pyramid spec, template system |
| README.md | YES | Landing page, constructionist narrative |
| CONNECTIONS.md | YES | Interop map: cursor-mirror, empathic-templates, adventure |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

| Concern | Severity | Detail |
|---------|----------|--------|
| File creation | LOW | Writes .cursor/rules/*.mdc. Scope limited to IDE rules. Templates version-controlled; runtime in .moollm/ (gitignored). |
| Template compilation | LOW | Deterministic from checked-in sources. |
| GLANCE staleness | LOW | Manual update needed when source changes. |

Mitigations: Permission gates on deep probing. cursor-mirror provides forensic audit trail.

---

## TRUST TIER

**GREEN** — System initialization with file creation scoped to .cursor/rules/ and .moollm/. Template compilation from checked-in sources. Self-diagnosed and self-healed via constructionist loop.

---

## VERDICT

Bootstrap is a methodology, not just a skill. It diagnosed its own failure (ignoring hot.yml), measured the gap (cursor-mirror), invented the fix (Semantic Image Pyramid, 92% reduction), and proved it worked. The constructionist loop — play, learn, lift — applied to itself. LOW risk from .cursor/rules file creation, otherwise exemplary. APPROVE.
