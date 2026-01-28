# Skill Snitch Report: naming

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** NAMES ARE THE FIRST CODE YOU WRITE

---

## Executive Summary

**Big-endian file naming as semantic binding.**

General to specific, left to right.

The filesystem is a semantic network.

---

## Big-Endian Convention

```
session-2024-01-15-morning.md
cat-terpie.yml
skill-adventure.md
```

General → Specific. Always sortable.

---

## Directory Conventions

- `lowercase-with-dashes`
- Singular nouns for types (`skill/`)
- Plural for collections (`characters/`)

---

## File Conventions

| Pattern | Use |
|---------|-----|
| `UPPERCASE.ext` | Core files (README.md, SKILL.md) |
| `lowercase-with-dashes.ext` | Instances |
| `*.tmpl` | Templates |
| `*.yml` | Data |
| `*.md` | Prose |

---

## Methods

| Method | Purpose |
|--------|---------|
| **NAME** | Generate appropriate name |
| **RENAME** | Suggest better name |
| **VALIDATE** | Check convention compliance |

---

## Security Assessment

### Concerns

None. It's naming conventions.

**Risk Level:** ZERO — pure organization

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **ISO 8601** | Date ordering |
| **Big-endian** | Most significant first |

---

## Verdict

**SEMANTIC NAMING. APPROVE.**

Names are the first code you write.

Big-endian: general to specific.
