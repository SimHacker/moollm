# SKILL-SNITCH DEEP PROBE REPORT
## moollm — The soul of the system

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: FOUNDATIONAL SKILL
**Status**: Tier 0, requires read_file and list_dir, self-explanation and navigation

---

## EXECUTIVE SUMMARY

The moollm skill IS the system explaining itself. Help, navigation, philosophy, skill discovery, constitution. When you're lost, invoke this. When you don't know what MOOLLM is, ask this. It's the lobby, the front desk, and the manifesto.

**Overall Assessment**: APPROVE — the heart of self-description, minimal risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 210 lines | NONE |
| GLANCE.yml | 62 lines | NONE |
| SKILL.md | 196 lines | NONE |
| README.md | 191 lines | NONE |
| scripts/moopmap.py | 321 lines | LOW |
| Executable code | moopmap.py (read-only map generator) | LOW |
| Total skill size | 980 lines (excl. report) | NONE |
| Required tools | read_file, list_dir | LOW |
| Tier | 0 | NONE |

---

## WHAT IT DOES

Eight methods covering system self-knowledge:

| Method | Purpose |
|--------|---------|
| HELP | Show what you can do right now |
| WHAT-AM-I | Explain what MOOLLM is |
| PHILOSOPHY | Articulate core philosophy |
| SKILLS | Browse available skills |
| RECOMMEND | Suggest skills for a task |
| CONSTITUTION | Show governing principles |
| NAVIGATE | Help find something in the system |
| ORIENT | Where am I? What's happening? |

MOOLLM = Many-voiced Object-Oriented LLM. Originally LLOOOOMM (LLM + MOOL + MOO + room). Too many O's.

Six governing principles:

| Principle | Meaning |
|-----------|---------|
| many-voices | Multiple perspectives, not statistical center |
| transparency | State visible in files, not hidden |
| play | Learning through exploration |
| composition | Build from reusable skills |
| humanity | Tools for humans, not replacements |
| ethics | Activate traditions, don't impersonate |

### Lineage

| Year | Ancestor | Contribution |
|------|----------|--------------|
| 1974 | D&D | DM role — the original LLM |
| 1976 | Colossal Cave | Room-based exploration |
| 1978 | MUD | Multi-user shared world |
| 1990 | LambdaMOO | Object-oriented rooms |
| 2000 | The Sims | Needs, advertisements, autonomous agents |
| — | Self language | Prototype-based inheritance |
| — | Logo | Constructionist learning |
| — | Society of Mind | K-lines, agents, mental furniture |

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
| File reads (moopmap.py) | read_file, list_dir | EXPECTED — read-only navigation |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Six principles, lineage, quick orientation |
| CARD.yml | YES | 8 methods, tier 0, tool requirements |
| SKILL.md | YES | Philosophy, constitution, full method specs |
| README.md | YES | Landing page, what MOOLLM means |

---

## SECURITY ASSESSMENT

**Risk Level**: VERY LOW

| Concern | Severity | Detail |
|---------|----------|--------|
| Meta-skill scope | LOW | Knows about all other skills. Can guide users to any part of the system. This is its purpose, not a vulnerability. |
| moopmap.py | LOW | Read-only. Generates skill maps from directory listings. No writes, no network, no secrets. |
| Philosophy shaping | NONE | Shapes user expectations transparently. All values stated openly. |

Mitigations: Read-only introspection. All capabilities visible. Philosophy is transparent and version-controlled. moopmap.py does directory traversal and file reading only.

---

## TRUST TIER

**GREEN** — Read-only help system. The skill that makes MOOLLM self-describing. Every system needs a way to explain itself.

---

## VERDICT

The soul of the system. Without moollm, MOOLLM is a collection of files. With it, the system can articulate what it is, navigate itself, and recommend skills. VERY LOW risk. APPROVE.
