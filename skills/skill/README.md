# 🧩 Skill

> A skill is documentation that learned to do things

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

The meta-protocol: how skills work, how they evolve, how they live everywhere.

A skill is a **documented capability** that can be instantiated, composed, and automated.

```
Documentation → Procedure → Script → Tool
     ↑              ↑         ↑        ↑
   PLAY           LEARN     LIFT  SISTER-SCRIPT
```

## State Persistence

Skills persist state at three tiers:

| Tier | Where | Lifespan |
|------|-------|----------|
| **Platform chat** | Cursor session | Ephemeral |
| **Narrative log** | `LOG.md` data islands | Read-mostly |
| **State files** | `*.yml` | Read-write |

**Key patterns:**
- **Data islands**: Embed YAML in logs with `#object-id` addressing
- **Promotion**: Pop to `.yml` file when editing needed
- **Log inheritance**: `inherits: LOG.md#birth-state`

## Scripts in Skills

Python scripts serve both humans and LLMs:

| Consumer | Access Method |
|----------|---------------|
| Human | `./tool.py --help` |
| LLM | Reads source file directly |

**DRY:** Write command structure once as Python CLI code.

## Parallels with Anthropic Skills

| Anthropic Skills | MOOLLM Skills |
|------------------|---------------|
| Documentation-first | README.md + SKILL.md |
| Tool definitions | YAML frontmatter |
| Composability | Dovetails section |
| Stateless | **Three-tier persistence** |

## Related Skills

- [play-learn-lift](../play-learn-lift/) — how skills evolve
- [sister-script](../sister-script/) — automating procedures
- [session-log](../session-log/) — narrative logging
- [scratchpad](../scratchpad/) — ephemeral working memory