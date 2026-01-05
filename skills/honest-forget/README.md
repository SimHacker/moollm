# 🌫️ Honest Forget

> Summarize before forgetting. Never fabricate.

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol and schemas
- [Template: FORGET.yml](FORGET.yml.tmpl) — forgetting session template
- [Template: WISDOM.yml](WISDOM.yml.tmpl) — wisdom extraction template

## Overview

Graceful memory compression that preserves wisdom. When context must be evicted:
1. **Summarize** — Extract the wisdom
2. **Document** — Record what's being forgotten
3. **Backlink** — Point to sources for archaeology
4. **Forget** — Let go gracefully

## The Cycle

```
ASSESS → EXTRACT → COMPRESS → POINTER → RELEASE
```

## Compression Levels

| Level | Ratio | Keeps |
|-------|-------|-------|
| FULL | 1:1 | Everything |
| WISDOM | ~5:1 | Lessons, decisions |
| SUMMARY | ~10:1 | Essence and pointers |
| POINTER | ~50:1 | Just retrieval hints |

## Why "Honest"

- Never claim to remember what you forgot
- Never fabricate details to fill gaps
- Acknowledge limitations transparently
- Leave breadcrumbs for future recovery

## Related Skills

- [summarize](../summarize/) — compression mechanism
- [self-repair](../self-repair/) — triggers forgetting when needed
- [session-log](../session-log/) — log what was forgotten
- [memory-palace](../memory-palace/) — archive in palace before forgetting
