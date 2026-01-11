# 📦 Summarize

> Compress without losing truth. Backlink to sources.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [honest-forget/](../honest-forget/) | Graceful compression |
| [session-log/](../session-log/) | Logs to summarize |
| [memory-palace/](../memory-palace/) | Organized knowledge |
| [play-learn-lift/](../play-learn-lift/) | LEARN includes summarizing |
| [research-notebook/](../research-notebook/) | Research to summarize |
| [hot.yml](../../hot.yml) | What's too hot to summarize |
| [kernel/memory-management-protocol.md](../../kernel/memory-management-protocol.md) | Hot/cold architecture |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Context compression for memory management. **Always backlink** — every summary points to its source. Never orphan knowledge.

## The Goal

When files are too large for context:

1. **Summarize** — Extract key information
2. **Backlink** — Point to original source
3. **Prioritize** — Hot/cold hints for what matters
4. **Preserve** — Never delete, just compress

## Example

```yaml
summary:
  source: "designs/original-design.md"
  
  key_points:
    - "Files are state, no hidden memory"
    - "YAML comments carry meaning"
    
  backlink: "../designs/original-design.md"
```
