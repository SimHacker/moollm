# Slideshow

> *"The camera is the pickaxe. The slideshow is the museum."*

Present generated images as linear visual narratives. Synthesize metadata from prompts and mining sidecars into scrollable stories.

## Quick Start

```yaml
---
inherits: slideshow
title: "My Gallery"
created: 2026-01-19
---
```

## Methods

| Method | Purpose |
|--------|---------|
| CREATE | Generate SLIDESHOW.md for a directory |
| UPDATE | Add new images to existing gallery |
| SUMMARIZE | Synthesize metadata into narrative |
| ORGANIZE | Encapsulate into subdirectory |
| COMPARE | Cross-image comparison section |

## Organization Pattern

```
BEFORE:
  pub/
    SLIDESHOW.md
    image-1.png
    image-1.yml
    ...many files...

AFTER:
  pub/
    dons-pub-photos-2026-01-19/
      SLIDESHOW.md
      image-1.png
      image-1.yml
      ...encapsulated...
```

## Related Skills

- **visualizer** — Creates images (we present them)
- **image-mining** — Extracts resources (we summarize them)
- **storytelling-tools** — Narrative structure
- **yaml-jazz** — Metadata as fuel

See CARD.yml for advertisements, SKILL.md for full protocol.
