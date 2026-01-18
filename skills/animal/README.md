# 🐾 Animal

> Species-appropriate behavior, not human projection.

## What Is This?

The **base skill for all non-human creatures**. Dogs, cats, dragons, aliens — all inherit from here.

Animals are not humans in fur suits. They have:
- **Different senses** (smell-dominant, different hearing/vision)
- **Different social structures** (pack, pride, herd, solitary)
- **Different communication** (scent, body language, vocalization)
- **Different motivations** (territory, food, safety, bonds)

This skill provides shared behaviors while respecting animal nature.

## Inherited By

| Species | Adds |
|---------|------|
| [dog/](../dog/) | FETCH, WALK, GOOD-BOY, pack loyalty |
| [cat/](../cat/) | HEADBUTT, KNEAD, SLOW-BLINK, independence |
| [puppy/](../puppy/) | Baby dog energy, learning |
| [kitten/](../kitten/) | Baby cat chaos, pouncing |

## Shared Behaviors

All animals can:

| Advertisement | What It Does |
|---------------|--------------|
| `PAT` | Respond to friendly touch |
| `FEED` | Receive food/treats |
| `OBSERVE` | Be watched (reveals personality) |
| `SNIFF` | Investigate via smell |
| `GREET` | Species-appropriate hello |
| `VOCALIZE` | Make species sounds |
| `FOLLOW` | Accompany someone |
| `FLEE` | Run from danger |

Species override these with specific implementations.

## Inheritance Types

### Species Inheritance
```
animal → dog → puppy
       → cat → kitten
```
Methods and behaviors flow down the chain.

### Parental Inheritance
```
Stroopwafel (mother) → kitten-1, kitten-2, kitten-3
```
Personality traits and learned behaviors from parents.

### Adoptive Inheritance
```
Don (adopter) → adopted-puppy-1, adopted-puppy-2
```
Home, family bonds, some learned behaviors.

## Real vs Fictional

| Type | Tags | Ethics |
|------|------|--------|
| **Real animal** | `[real-being, animal]` | Portray accurately, respect actual nature |
| **Fictional animal** | `[fictional, animal]` | Creator authority, can anthropomorphize more |
| **Mythic creature** | `[mythic, animal]` | Cultural sensitivity, creature behavior |

## Quick Example

```yaml
# A real dog
biscuit:
  inherits: skills/dog
  ontology:
    tags: [real-being, animal]
  personality:
    friendly: 10
    loyal: 10

# A fictional dragon
smaug:
  inherits: skills/dragon  # (which inherits animal)
  ontology:
    tags: [fictional, animal, mythic]
```

## Related

- [dog/](../dog/) — Canine specifics
- [cat/](../cat/) — Feline specifics
- [ontology/](../ontology/) — Tag system
- [character/](../character/) — Character creation
