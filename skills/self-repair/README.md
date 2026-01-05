# 🔧 Self Repair

> Missing state triggers repair, not failure

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: CHECKLIST.yml](CHECKLIST.yml.tmpl) — repair checklist

## Overview

Checklist-based self-healing demons. **NEVER-CRASH** — the core principle. Repair instead of fail. Always.

## The Principle

When something's wrong:

1. **Detect** — Checklist finds missing/invalid state
2. **Repair** — Demon creates/fixes what's needed
3. **Log** — Document what was repaired
4. **Continue** — Never crash, always converge

## Repair Demons

| Demon | Watches For |
|-------|-------------|
| `checklist_repairer` | Missing canonical files |
| `sticky_note_maintainer` | Missing sidecar metadata |
| `membrane_keeper` | Files outside boundaries |

## Related Skills

- [session-log](../session-log/) — log repairs
- [coherence-engine](../coherence-engine/) — orchestrates repair
- [debugging](../debugging/) — investigate when repair fails