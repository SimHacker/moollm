# SKILL-SNITCH DEEP PROBE REPORT
## k-lines — Saying the name activates the constellation

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: PROTOCOL SKILL
**Status**: Tier 0, no tools required, Minsky's K-lines as semantic activation

---

## EXECUTIVE SUMMARY

Implements Marvin Minsky's K-lines as MOOLLM's protocol invocation mechanism. Saying the name reactivates the mental state from when it was learned. YAML-JAZZ invokes YAML Jazz patterns. ADVENTURE invokes text adventure. K-REF format provides typed file pointers with metadata.

**Overall Assessment**: APPROVE — naming as activation, minimal risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 87 lines | NONE |
| GLANCE.yml | 48 lines | NONE |
| SKILL.md | 377 lines | NONE |
| README.md | 96 lines | NONE |
| Executable code | None | NONE |
| Total skill size | 608 lines (excl. report) | NONE |
| Required tools | None | NONE |
| Tier | 0 | NONE |

---

## WHAT IT DOES

Five methods for protocol activation and reference:

| Method | Purpose |
|--------|---------|
| INVOKE | Activate protocol by name — the K-line fires |
| DEFINE | Create new protocol (name → behavior mapping) |
| LIST | Show available protocols, optional category filter |
| K-REF | Emit file pointer: `PATH[:LINE[-END]][#anchor]` with type and description |
| SISTER-SCRIPT | Tool emits K-REFs, LLM reads selectively (scan → emit pointers → read what's needed) |

K-REF format: `PATH[:LINE[-END]][#anchor][?search] # TYPE - DESC`

Examples:
- `/path/file.txt:42:10-46 # secret`
- `/path/screenshot.png # image - Cursor reads and analyzes`

Sister-script pattern enables parsimonious context usage: point to files instead of reading everything into context.

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
| GLANCE.yml | YES | Minsky insight, K-REF format, sister-script |
| CARD.yml | YES | 5 methods, tier 0, orchestrator capability note |
| SKILL.md | YES | Full K-line theory, K-REF spec, examples |
| README.md | YES | Landing page, Minsky attribution |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

| Concern | Severity | Detail |
|---------|----------|--------|
| K-REF scope | LOW | K-REFs can point anywhere on disk. Cursor reads absolute paths including images. The pointer itself is harmless; the read operation uses Cursor's native file access. |
| Protocol hijacking | LOW | Malicious K-line definitions could redirect protocol names to unintended behavior. Mitigated by PROTOCOLS.yml being version-controlled. |

Mitigations: K-REFs are pointers, not execution. Protocol definitions are visible in PROTOCOLS.yml and skill CARD.yml files. No tools required, no file writes, no network access.

---

## TRUST TIER

**GREEN** — Pure naming and reference convention. No tools, no execution. The name activates the tradition.

---

## VERDICT

Minsky's K-lines adapted for LLM protocol activation. LOW risk from K-REF file scope, otherwise pure semantic convention. APPROVE.
