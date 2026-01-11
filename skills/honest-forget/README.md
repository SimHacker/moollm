# 🌫️ Honest Forget

> Summarize before forgetting. Never fabricate.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [summarize/](../summarize/) | Compression mechanism |
| [self-repair/](../self-repair/) | Triggers forgetting when needed |
| [session-log/](../session-log/) | Log what was forgotten |
| [memory-palace/](../memory-palace/) | Archive in palace before forgetting |
| [postel/](../postel/) | Graceful handling of gaps |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol and schemas

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

