# Simopolis Houses

**Every Sim needs a home. Every home tells a story.**

Houses in Simopolis are imported lots from The Sims — the actual floor plans, furniture layouts, and object placements that defined how Sims lived. In The Sims 1, the house *is* the game: buy objects, place them, watch your Sims interact with them. Every chair, every toilet, every television is a decision that shapes Sim behavior.

## Available Houses

### Goth Manor
**`goth-manor/`** — The most expensive lot in the original game. Three stories of Victorian architecture. Library, laboratory, music room, pool, telescope, and the famous backyard gravestones. Budget: unlimited (old money). Where Mortimer grieves and Cassandra watches.

### Newbie House
**`newbie-house/`** — The starter home. One bedroom, one bathroom, basic kitchen, cheapest TV. Budget: what's left of §20,000 after the lot. Where Bob learns not to cook and Betty keeps everything from falling apart.

### Templates
**`templates/`** — Starter home template for creating new lots.

## House Structure

Each house is a directory containing:

```
house/
├── README.md          # Description, history, notable features
├── ROOM.yml           # MOOLLM room definition with exits
├── floor-plan.yml     # Room layout and object placement
└── objects.yml        # Inventory of all objects in the house
```

## The Sims 1 Lot System

In The Sims 1, lots are stored in `House##.iff` files within the save directory. Each lot contains:
- Floor tiles and wall placements
- Object instances (each with position, rotation, state)
- Terrain modifications (swimming pools, trees)

SimObliterator reads these files and extracts the layout data. The MOOLLM representation preserves the spatial relationships while adding narrative context.

## See Also

- [Objects](../objects/README.md) — Catalog of available objects
- [Neighborhoods](../neighborhoods/README.md) — Where houses are located
- [Exchange](../exchange/README.md) — Import more houses
