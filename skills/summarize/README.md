# 📦 Summarize

> Compress without losing truth. Backlink to sources.

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: SUMMARIES.yml](SUMMARIES.yml.tmpl) — summary template

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

## Related Skills

- [honest-forget](../honest-forget/) — graceful compression
- [session-log](../session-log/) — logs to summarize
- [memory-palace](../memory-palace/) — organized knowledge