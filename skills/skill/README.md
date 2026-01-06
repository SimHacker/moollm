# 🧩 Skill

> A skill is documentation that learned to do things

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Interface Card](CARD.yml) — machine-readable methods

## Overview

The meta-protocol: how skills work, how they evolve, how they live everywhere.

A skill is a **documented capability** that can be instantiated, composed, and automated.

## Skill Anatomy (Required Structure)

```
skills/
  my-skill/
    README.md         # Human entry point (GitHub renders this)
    SKILL.md          # Full spec with YAML frontmatter
    CARD.yml          # Machine-readable interface definition
    *.tmpl            # Templates at root level (optional)
```

Every skill has:
- **README.md** — Quick overview, links (you're reading one!)
- **SKILL.md** — Full protocol with YAML frontmatter defining name, tier, allowed-tools
- **CARD.yml** — Interface definition: methods, tools, state, advertisements

## The Evolution Path

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