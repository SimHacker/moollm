# 📜 Session Log

> Human-readable markdown log with embedded YAML

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: SESSION.yml](SESSION.yml.tmpl) — session template
- [Template: session-log.md](session-log.md.tmpl) — log format

## Overview

Append-only audit trail that humans can actually read. **Never modify, never delete** — the audit trail is sacred.

## Format

Each entry is a markdown heading with embedded YAML:

```markdown
## 12:00:05 — Tool Call: fs.read

Reading parser to understand recursive descent.

```yaml
type: tool_call
tool: fs.read
args:
  path: src/parser.ts
  why: "Check implementation"
```
```

## Why Markdown + YAML

| Feature | Benefit |
|---------|---------|
| Human readable | Easy to scan |
| Machine parseable | YAML blocks extractable |
| Semantic comments | YAML Jazz in action |
| Append-only | Natural audit support |

## Related Skills

- [summarize](../summarize/) — compress old logs
- [honest-forget](../honest-forget/) — safe compression