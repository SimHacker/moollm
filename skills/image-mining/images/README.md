# Mineable Image Library

> *"Every image is a lode. Every pixel, potential ore."*

## What's Here

Pre-analyzed images ready for mining — a library of visual resources with quantified extractable materials.

These are **prompt-ready image concepts** with pre-defined resource yields. Use them for:
- Adventure game resource extraction
- Visualization prompts
- Mining skill testing
- Example outputs

## Image Categories

### Natural Resources
- `ore-vein` — Iron, copper, trace gold in cavern
- `forest-clearing` — Wood, leaves, mushrooms, seeds
- `gem-cave` — Gems, crystals, geodes
- `volcanic-vent` — Obsidian, sulfur, heat energy

### Treasure & Artifacts
- `treasure-room` — Gold, gems, ancient weapons
- `abandoned-workshop` — Tools, blueprints, components
- `ancient-library` — Scrolls, knowledge, ink

### Living Spaces
- `merchant-stall` — Trade goods, coins, exotic items
- `alchemist-lab` — Potions, ingredients, apparatus

## Resource Properties

Each image defines extractable resources with:

```yaml
resources:
  iron-ore:
    total: 150        # Total available
    remaining: 150    # What's left
    per_turn: 15      # Extraction rate
    rare: false       # Rarity modifier
```

## Usage

Reference from anywhere:
```yaml
ref: skills/image-mining/images/INDEX.yml#treasure-room
```

Mine with commands:
```bash
python ../scripts/mine.py mine treasure-room.png
```

## Philosophy

These images exist to be **depleted**. Mine them. Extract their resources. Watch the `remaining` count drop. When exhausted, the image changes state.

*"The camera is a pickaxe for visual reality."*

## Related

- `INDEX.yml` — Full image catalog with resources
- `../scripts/mine.py` — Mining CLI
- `../CARD.yml` — Full skill documentation
