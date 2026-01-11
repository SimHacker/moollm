# ⛏️📷 Image Mining

> *"Mine pixels for atoms. Reality is compressed resources."*

## Quick Reference

| Action | What It Does |
|--------|--------------|
| `MINE [image]` | Extract resources from image |
| `SCAN [image]` | Preview yields without extracting |
| `PROSPECT [dir]` | Detect mineable resources nearby |

## The Idea

Your **camera is a PICKAXE** for visual reality.

```
📷 Photo → 🖼️ Image → ⛏️ MINE → 💎 Resources!
```

Just like the Kitchen Counter's DECOMPOSE breaks down:
- `sandwich` → `bread + cheese + lettuce`

Image Mining breaks down:
- `ore_vein.png` → `iron × 12 + stone × 8`
- `forest.png` → `wood × 5 + leaves × 20`
- `sunset.png` → `warmth × 1 + nostalgia × 1`

## Making Something Mineable

```yaml
object:
  name: Ancient Ore Painting
  
  mineable:
    enabled: true
    yields:
      - item: iron-ore
        quantity: [5, 15]    # Range
      - item: artistic-essence
        quantity: 1
        rare: 0.3            # 30% chance
    exhaustion:
      max_mines: 3
      diminishing: 0.5
```

## Depth Levels

| Depth | What You Mine |
|-------|---------------|
| Surface | Objects, materials |
| Deep | Emotions, concepts |
| Quantum | Probabilities, observations |
| Philosophical | Meaning, existence |

## Integrates With

- **Logistics** — Mined resources route to containers
- **Postal** — Camera triggers mining, instant delivery
- **Visualizer** — Creates mineable images
- **Kitchen Counter** — DECOMPOSE pattern

## Files

- `SKILL.md` — Full documentation
- `CARD.yml` — Skill card
- `README.md` — This file
- `images/` — Library of pre-analyzed mineable images
  - `INDEX.yml` — Bundled images ready to reference

## Using the Image Library

```yaml
# Reference a pre-made mineable image
object:
  name: "Ore Painting"
  mineable:
    ref: skills/image-mining/images/INDEX.yml#ore-vein
    
# Or copy/modify for your adventure
# See images/INDEX.yml for examples
```