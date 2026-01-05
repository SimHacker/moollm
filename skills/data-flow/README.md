# 🔄 Data Flow

> *"Rooms are nodes. Exits are edges. Thrown objects are messages."*

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Build processing pipelines using rooms and objects. The filesystem IS the data flow network.

## Pattern

```
Room → inbox → process → THROW → next Room's inbox
```

## Quick Commands

| Command | Effect |
|---------|--------|
| `THROW obj exit` | Send object through |
| `INBOX` | List waiting items |
| `NEXT` | Get next item |
| `STAGE obj exit` | Queue for later |
| `FLUSH` | Send all staged |

## Processor Types

| Type | Use |
|------|-----|
| Script | Deterministic transformation |
| LLM | Semantic analysis |
| Hybrid | Both together |

## Related Skills

- [room/](../room/) — Rooms as processing nodes
- [sister-script/](../sister-script/) — Scripts for deterministic stages
- [coherence-engine/](../coherence-engine/) — LLM as orchestrator

## Tools Required

- `file_read` — Read objects
- `file_write` — Move objects between inboxes
- `terminal_execute` — Run script processors

---

*See [SKILL.md](SKILL.md) for complete specification.*
