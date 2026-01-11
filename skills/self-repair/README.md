# 🔧 Self Repair

> Missing state triggers repair, not failure

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [robust-first/](../robust-first/) | Stay alive, heal |
| [bootstrap/](../bootstrap/) | Repair on startup |
| [honest-forget/](../honest-forget/) | Graceful degradation |
| [session-log/](../session-log/) | Log repairs |
| [coherence-engine/](../coherence-engine/) | Orchestrates repair |
| [debugging/](../debugging/) | Investigate when repair fails |
| [postel/](../postel/) | Be conservative in what you emit |
| [kernel/self-healing-protocol.md](../../kernel/self-healing-protocol.md) | The self-healing protocol |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

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
