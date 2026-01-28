# Skill Snitch Report: sniffable-python

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** STRUCTURE EXISTING SYNTAX, DON'T INVENT NEW

---

## Executive Summary

**Structure code so the first 50 lines tell the whole story.**

Don't invent new syntax — structure existing syntax. The LLM already knows Python.

Comprehension fidelity > token count.

---

## The Core Thesis

> "The 'ideal LLM syntax' question has the wrong framing."

You don't need new syntax. You need structured familiar syntax.

Perl's syntax fetish is a cautionary tale.

---

## The Zones

| Zone | Lines | Purpose |
|------|-------|---------|
| **Shebang + Docstring** | 1-15 | Purpose, usage, becomes --help |
| **Imports** | 16-22 | Dependencies visible at a glance |
| **Constants** | 23-30 | Configuration with semantic comments |
| **CLI Structure** | 31-50 | main() contains command tree |
| **Implementation** | 51+ | Only read if modifying |

---

## Checklist

- Shebang on line 1
- Module docstring with purpose, usage, examples
- Imports grouped at top (no decorative markers)
- Constants with explanatory comments
- CLI structure in main() using argparse
- Each command has a docstring
- Types in function signatures
- Implementation below line 50
- Internal functions prefixed with _

---

## Anti-Patterns

- Implementation before CLI structure
- No docstrings on commands
- Magic constants without comments
- Scattered imports throughout file
- API not discoverable from header

---

## Language-Agnostic Application

SNIFF-CODE works on any language:

- Purpose clear from first 10 lines?
- API/exports before implementation?
- Semantic comments (WHY not WHAT)?
- No decorative cruft?
- Dependencies visible at top?

---

## The MOOLLM Loop

```
PLAY → Try things, log them
LEARN → Document patterns in PROCEDURE.md
LIFT → Generate sniffable Python script
SKILL → Add script to skill
LLM → Sniffs header, understands API
OUTPUT → YAML results
REPEAT → Play with new tool
```

---

## Security Assessment

### Concerns

None. This is pure methodology.

**Risk Level:** ZERO — it's just code organization

---

## Verdict

**STRUCTURE OVER SYNTAX. APPROVE.**

The LLM already knows Python.

Don't invent new syntax. Structure existing syntax.
