# House Builder

**Lot layout from descriptions.**

The Sims 1 lot system uses a grid-based floor plan with tiles, walls, floors, and object placements. The House Builder generates lot layouts from natural language descriptions, producing YAML floor plans compatible with both Simopolis and (via SimObliterator) the original game.

## From Description to Lot

```
Description: "A cozy two-bedroom cottage with a garden and a reading nook.
             Budget: §25,000. Style: warm, cluttered, homey."
       ↓
AI generates floor plan YAML:
  rooms, dimensions, wall placements, door positions
       ↓
Object placement based on budget and style:
  furniture, electronics, plumbing, decorative
  selected for need satisfaction + aesthetic
       ↓
Simopolis lot directory:
  README.md, ROOM.yml, floor-plan.yml, objects.yml
       ↓
(Optional) SimObliterator writes House##.iff
  compatible with The Sims 1
```

## Design Principles

The Sims 1 house design follows specific rules that make good lots:
- Every room needs a door (Sims can't walk through walls)
- Bathrooms need walls (privacy affects Hygiene recovery)
- The kitchen should be near the dining area (Sims carry plates)
- Bedrooms should be away from noise sources (TV, stereo)
- The front door should face the street (visitors, mail, carpool)

The House Builder encodes these rules as constraints in the generation pipeline.

## See Also

- [Houses](../../houses/README.md) — Existing lots
- [Objects](../../objects/README.md) — Available furniture
- [Templates](../../houses/templates/) — Base lot templates
