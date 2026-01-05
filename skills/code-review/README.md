# 🔍 Code Review

> *"Read with intent. Question with purpose. Document with care."*

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Systematic code analysis with evidence collection. Code review IS an [adventure](../adventure/) — the codebase is the dungeon, findings are clues.

## Process

```
READ → NOTE → CLASSIFY → REPORT
```

## Finding Severity

| Level | Symbol | Action |
|-------|--------|--------|
| Blocking | 🚫 | Must fix |
| Important | ⚠️ | Should fix |
| Minor | 💡 | Nice to fix |
| Praise | 🎉 | Celebrate |

## Review Categories

- **Security** — Injection, auth issues
- **Correctness** — Logic errors, edge cases
- **Performance** — N+1 queries, memory
- **Style** — Naming, formatting

## Templates

| File | Purpose |
|------|---------|
| [REVIEW.yml.tmpl](REVIEW.yml.tmpl) | Tracking state |
| [REVIEW.md.tmpl](REVIEW.md.tmpl) | Formatted output |

## Related Skills

- [adventure/](../adventure/) — Code review IS adventure
- [debugging/](../debugging/) — Fix what you find
- [research-notebook/](../research-notebook/) — Deep investigation

## Tools Required

- `file_read` — Read code files
- `terminal_execute` — Run tests, linters

---

*See [SKILL.md](SKILL.md) for complete specification.*
