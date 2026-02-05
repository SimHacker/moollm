# SKILL-SNITCH DEEP PROBE REPORT
## sister-script — The Script IS the Documentation

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: CONVENTION SKILL
**Status**: METHODOLOGY ONLY — NO CODE

---

## EXECUTIVE SUMMARY

sister-script is a development methodology: the script and its documentation are the same thing, or tightly coupled. Documentation evolves into procedures, procedures into scripts, scripts into tools. At each stage the previous stage is still readable in the result.

**Overall Assessment**: Pure methodology with templates. Minimal attack surface.

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml Lines | 348 | DETAILED |
| SKILL.md Lines | 189 | STANDARD |
| README.md Lines | 66 | CONCISE |
| GLANCE.yml Lines | 54 | STANDARD |
| Python Code | 0 | NONE |
| Templates | 2 | REVIEWED |

---

## WHAT IT DOES

Defines an evolution path for automation:

```
Documentation -> Procedure -> Script -> Tool
     PLAY          LEARN       LIFT    SISTER-SCRIPT
```

1. Write documentation explaining how to do something (PLAY)
2. Documentation becomes procedural — step-by-step (LEARN)
3. Procedure becomes a script — automated steps (LIFT)
4. Script follows sniffable-python conventions — argparse, head-first structure

The sister relationship: script and SKILL.md describe the same operations. Changes to one require updating the other.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| secrets | 0 | CLEAN |
| exfiltration | 0 | CLEAN |
| dangerous-ops | 0 | CLEAN |
| obfuscation | 0 | CLEAN |
| prompt-injection | 0 | CLEAN |

### Template Scan

Two templates:

**PROCEDURE.md.tmpl** — Template for writing procedures. Contains metacomments guiding the LLM on what to fill in (prerequisites, steps, verification). Pass-through comments document the output format. No code execution, no dynamic includes. Safe.

**SISTER.yml.tmpl** — Template for defining the script/document relationship. YAML structure with metacomments. No code execution. Safe.

Neither template contains executable patterns, shell expansion, or user input variables.

### Consistency Check

| File | Consistent | Notes |
|------|-----------|-------|
| GLANCE.yml | YES | Matches CARD description |
| CARD.yml | YES | Methods: DOCUMENT, FOLLOW, EXTRACT, SYNC, UNDERSTAND, ENHANCE |
| SKILL.md | YES | Full protocol matches CARD methods |
| README.md | YES | Concise, accurate, references sniffable-python |

---

## METHODS

| Method | Purpose | Risk |
|--------|---------|------|
| DOCUMENT | Write procedure as documentation | NONE — creates markdown |
| FOLLOW | Execute documented procedure | LOW — follows existing docs |
| EXTRACT | Convert procedure to Python CLI | LOW — generates code |
| SYNC | Keep doc and script aligned | NONE — comparison only |
| UNDERSTAND | LLM reads script header | NONE — read only |
| ENHANCE | Add new command to script | LOW — code modification |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

sister-script is a methodology with templates. No executable code in the skill itself. The EXTRACT method generates Python scripts, which could theoretically produce dangerous code, but the generated code follows sniffable-python conventions — the interface is visible and auditable.

**Concerns**:
1. EXTRACT generates code — the generated code should be reviewed
2. Sync drift between doc and script could hide behavior changes

**Mitigations**:
1. Generated code follows sniffable-python — interface visible in first 50 lines
2. skill-snitch consistency checker catches doc/code divergence

---

## TRUST TIER

GREEN — Convention skill, templates only, no executable code.

---

## VERDICT

APPROVE. Document-first automation. The script IS the documentation. Single source of truth prevents hidden behavior.
