# 📦 Adventure Export System

Export definitions for publishing interactive web experiences from MOOLLM adventures.

**Inspiration:**
- **Myst** (1993) — Navigable worlds, point-and-click exploration
- **The Sims** (2000) — Family/house web export, album pages, storytelling
- **Both were on the #1 spot for years, The Sims knocking Myst off its long run in 2000!**

We inherit from both traditions:
- Myst's **mystery and exploration**
- The Sims' **object catalogs and family albums**

## Export Manifest Format

```yaml
# EXPORT.yml — What to include in published web app
name: "My Adventure Export"
version: "1.0.0"
description: "Interactive showcase of..."

# What to include
include:
  rooms:
    - path/to/room1
    - path/to/room2/**    # Recursive
  objects:
    - specific-object-id
    - category: weapons   # All in category
  characters:
    - npc-1
    - npc-2
  prototypes:
    - skills/no-ai-overlord/archetypes/*
  slideshows:
    - id: my-slideshow
      path: path/to/slideshow
      image: generated.png

# Starting point
entry:
  room: lobby
  view: overview       # overview, room, catalog, album

# Views to generate
views:
  overview: true       # Landing page with map
  rooms: true          # Individual room pages
  catalog: true        # Object showcase (like Sims buy mode)
  album: true          # Story/screenshot pages
  prototypes: true     # Archetype gallery

# Features
features:
  speech: true         # Text-to-speech
  recognition: false   # Speech-to-text
  source_viewer: true  # View YAML on GitHub
  inventory: true      # Drag-drop inventory
  pie_menus: true      # Radial action menus

# NOT pay-to-play!
monetization: none     # MOOLAH is free, this is NOT crypto scam
```

## Export Types

### 1. Room Export
Individual rooms with exits, objects, characters.

### 2. Catalog Export  
Object showcase — browse, examine, "buy" (collect for free).

### 3. Album Export
Story pages with screenshots, captions, narrative.

### 4. Prototype Gallery
Archetype showroom — browse, invoke, instantiate.

### 5. Slideshow Export
Photo archives with generated images, served from GitHub CDN.

### 6. Narrative Session
Interactive story with hyperlinked objects and navigation.

## Narrative Sessions

A **narrative session** is browsable hypertext:
- Object references are **links** — click to examine
- Nav structures: outlines, tables, breadcrumbs
- Export as story (markdown, HTML, PDF)
- Render as interactive web page
- **Round-trip URLs** back to source

### URL Scheme: `moollm://`

```
moollm://github/org/repo/path/to/file.yml
  ↔
https://github.com/org/repo/blob/main/path/to/file.yml
```

**Address space:**
| Prefix | Source |
|--------|--------|
| `moollm://github/leela-ai/moollm/...` | GitHub repos |
| `moollm://moo/...` | MOO services |
| `moollm://pocket/...` | Universe-in-a-pocket |
| `moollm://local/...` | Local workspace |

**Examples:**
```yaml
# Reference an archetype
prototype: moollm://github/leela-ai/moollm/skills/no-ai-overlord/archetypes/doctor-no.yml

# Reference a room
location: moollm://github/leela-ai/moollm/examples/adventure-4/street/lane-neverending/no-ai-tower

# Translates to browsable GitHub URL
# https://github.com/leela-ai/moollm/blob/main/skills/no-ai-overlord/archetypes/doctor-no.yml
```

**Round-trip translation:**
- Export renders `moollm://` as clickable GitHub links
- Import can parse GitHub URLs back to `moollm://`
- Source viewer shows both

**Images:** Display directly from `raw.githubusercontent.com`
```
moollm://github/org/repo/images/photo.png
  → https://raw.githubusercontent.com/org/repo/main/images/photo.png
  → <img src="..."> in browser
```

## Example Exports

See `exports/` directory for ready-to-use manifests.
