# SKILL-SNITCH DEEP PROBE REPORT
## sniffable-python — Structure Code So LLMs Read the Head

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: CONVENTION SKILL
**Status**: METHODOLOGY ONLY — NO CODE

---

## EXECUTIVE SUMMARY

sniffable-python is a code organization convention: structure Python scripts so the first 50-100 lines describe the entire API. The LLM reads the head, understands the script, doesn't need the rest.

**Overall Assessment**: Pure methodology. Zero executable code. Zero attack surface.

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml Lines | 209 | DETAILED |
| SKILL.md Lines | 876 | COMPREHENSIVE |
| README.md Lines | 120 | CLEAN (rewritten 2026-02-05) |
| GLANCE.yml Lines | 45 | STANDARD |
| Python Code | 0 | NONE |
| Templates | 1 (TEMPLATE.py.tmpl) | SAFE — example code |

---

## WHAT IT DOES

Defines a layout convention for Python scripts:

1. Docstring at top: all commands, arguments, gotchas
2. Use argparse with add_subparsers — CLI definition in one contiguous block in main()
3. Constants and path definitions after imports
4. set_defaults(func=cmd_xxx) routes to handlers
5. Implementation below — underground

Why argparse, not click/typer/fire: argparse puts the entire CLI definition in main() as one block. Decorator-based frameworks scatter argument definitions across functions. An LLM can't sniff a click app without reading every decorated function.

Same principle as the Semantic Image Pyramid applied within a file. The head sticks above ground. The body is below.

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

TEMPLATE.py.tmpl contains example Python code with argparse structure. No executable logic, no dynamic includes, no shell expansion. Safe — it's a copy-and-modify starter template.

### Consistency Check

| File | Consistent | Notes |
|------|-----------|-------|
| GLANCE.yml | YES | Matches CARD description |
| CARD.yml | YES | Methods match SKILL.md |
| SKILL.md | YES | Comprehensive specification |
| README.md | YES | Rewritten 2026-02-05, technical, no slop |

README.md was rewritten to remove James Burke "Connections" style prose and Steve Jobs "lickable pixels" tangent. Now technical: rules, pattern, argparse rationale, cursor-mirror as canonical example.

---

## CANONICAL EXAMPLE

cursor-mirror/scripts/cursor_mirror.py — 9,800 lines, 59 commands.

| Section | Lines | Content |
|---------|-------|---------|
| Docstring | 1-160 | All commands, reference syntax, gotchas |
| Imports + constants | 160-178 | Path constants, DB schema comments |
| main() + argparse | 183-260 | Every command in one block |
| Handlers | 260+ | 9,500 lines underground |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE

This is a code organization convention. It has no executable code, no network access, no file writes, no shell execution. The template is inert example code.

The convention itself improves security: sniffable code is auditable code. If the interface is visible in the first 50 lines, hidden behavior is harder to achieve.

---

## TRUST TIER

GREEN — Pure methodology, no code, no risk.

---

## VERDICT

APPROVE. Structure existing syntax, don't invent new. The LLM already knows Python.
