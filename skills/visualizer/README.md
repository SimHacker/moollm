# 🎨 Visualizer

> Every image is a semantic snapshot. The metadata IS the meaning.

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: PHOTO-SET.yml](PHOTO-SET.yml.tmpl) — photo set template

## Overview

A universal character prototype for image generation — a familiar that can compose prompts, invoke artistic traditions, and render visual sidecars for any entity.

## The Semantic Clipboard

Every image prompt includes full context as metadata:

- **Who** — Mind Mirror profiles, costumes, moods
- **Where** — room, lighting, atmosphere
- **What** — action, context, narrative moment
- **How** — camera angle, style, focus

```yaml
image_prompt:
  subject:
    name: "Captain Ashford"
    mind_mirror:
      confident: 6
    costume: "Space pirate with holographic eyepatch"
    mood: "victorious, exhausted"
```

## Related Skills

- [mind-mirror](../mind-mirror/) — personality informs visuals
- [card](../card/) — images can be cards
- [room](../room/) — room context affects visualization