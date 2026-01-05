# 💬 Soul Chat

> Everything is alive. Everything can speak.

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: CHAT.md](CHAT.md.tmpl) — chat template
- [Template: CHARACTERS.yml](CHARACTERS.yml.tmpl) — character definitions
- [Template: ENTITIES.yml](ENTITIES.yml.tmpl) — entity definitions

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

## Related Skills

- [room](../room/) — rooms can speak
- [card](../card/) — card instances speak
- [mind-mirror](../mind-mirror/) — personality influences voice
- [yaml-jazz](../yaml-jazz/) — embedded data in dialogue