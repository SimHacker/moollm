# 💬 Soul Chat

> Everything is alive. Everything can speak.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Rooms can speak |
| [card/](../card/) | Card instances speak |
| [mind-mirror/](../mind-mirror/) | Personality influences voice |
| [yaml-jazz/](../yaml-jazz/) | Embedded data in dialogue |
| [speed-of-light/](../speed-of-light/) | Multi-character in one call |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | Pub conversations live |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: CHAT.md](CHAT.md.tmpl) — chat template

## Overview

Dialogues between characters, objects, rooms, documents, concepts—anything with a soul. **Give anything a voice.**

Characters share data by embedding YAML/JSON blocks in their dialogue — YAML Jazz in action.

## Format

**Prefer Markdown** — more human readable, can embed any typed code block.

```markdown
## The Gardener

I've been tending these patterns for a while now.

```yaml
observation:
  pattern: "Files cluster by prefix"
```

## The Archivist

Let me add some context...
```
