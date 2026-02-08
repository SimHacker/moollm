# Simopolis Objects

**Every object has a purpose. Every purpose serves a need.**

Objects in The Sims aren't decorative — they're functional. Every object in the game "advertises" to Sims, broadcasting what needs it can satisfy. A fridge advertises Hunger relief. A bed advertises Energy. A TV advertises Fun. The Sim's AI evaluates all advertisements from nearby objects and chooses the one that best satisfies their most urgent need.

In Simopolis, objects are cataloged from the original game data files, organized by category, and described with their advertisement values and behavioral effects.

## Categories

| Category | Directory | Description |
|----------|-----------|-------------|
| Furniture | `furniture/` | Seating, beds, tables, storage |
| Electronics | `electronics/` | TVs, computers, phones, stereos |
| Plumbing | `plumbing/` | Toilets, showers, sinks, bathtubs |
| Decorative | `decorative/` | Art, plants, rugs, lighting |
| Collections | `collections/` | Expansion pack and community content sets |

## The Advertisement System

The Sims' object interaction system works through advertisements:

```yaml
object:
  name: "Expensive TV"
  advertisements:
    watch_tv:
      fun: +30            # Satisfies Fun need
      comfort: +10        # Also provides Comfort (if seated)
      social: +5          # Small social boost (shared watching)
    turn_off:
      fun: 0
```

Every object broadcasts what it can do. Every Sim evaluates all broadcasts against their current needs. The Sim with low Fun sees the TV's +30 Fun advertisement and walks toward it. The Sim with low Energy ignores the TV and walks toward the bed's +50 Energy advertisement.

This is the behavioral engine that makes The Sims work. Objects don't just exist — they *call* to the Sims who need them.

## Object Sources

| Source | Path | Contents |
|--------|------|----------|
| Base game | `simprov/GameData/Objects/Objects.far` | All default objects |
| Expansion packs | `simprov/Downloads/` | Additional object sets |
| Community | `TheSimsDownloads/` | 3,313 community-created .iff objects |
| Custom | User-created via Transmogrifier | AI-assisted object creation |

## Catalog Format

Each object category has a README.md index. Individual objects (when fully imported) get YAML files describing their properties, advertisements, and narrative context.

## See Also

- [Houses](../houses/README.md) — Where objects live
- [Tools / Transmogrifier](../tools/transmogrifier/) — AI-powered object editor
- [Exchange / Collections](../exchange/collections/) — Curated object sets
- [SimObliterator Suite](../../../../SimObliterator_Suite/) — Binary format parser for .iff objects
