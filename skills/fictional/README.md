# 📖 Fictional

> They exist because imagination allows it.

## What Is This?

The ontological tag for **anything invented**. Characters, places, objects, entire worlds. If we made it up, this tag applies.

## When To Use

Tag with `[fictional]` when the entity:
- Was invented by imagination
- Doesn't exist in reality
- Can be freely modified by creators
- Follows fiction's rules, not physics

## Examples

| Type | Example | Why Fictional |
|------|---------|---------------|
| Character | Zaphod Beeblebrox | Invented by Douglas Adams |
| Place | The Pub (in game) | Invented game location |
| Object | The Vorpal Sword | Invented artifact |
| World | Middle-earth | Invented setting |
| NPC | Donna Toadstool | Original creation |

## The Core Freedoms

1. **Creator authority** — Author decides fate
2. **Internal consistency** — Follow fiction's rules
3. **No real-world claims** — It's made up
4. **Transformation allowed** — Can change anything
5. **Play freely** — Creative exploration

## Quick Start

```yaml
character:
  id: bumblewick
  inherits:
    - skills/fictional  # ← This tag
  # Now full creative freedom applies
```

```yaml
room:
  id: enchanted-garden
  tags: [fictional]
  # Now can have magic, impossible geometry, etc.
```

## Adapting Existing Fiction

When playing with characters from books, movies, games:

```yaml
adaptation:
  respect: "Acknowledge the source"
  celebrate: "Capture what makes them great"
  transform: "Put them in new situations"
  crossover: "Mix universes creatively"
```

## Protocol

Uses **CREATIVE** protocol — freedom within story logic.

## Related

- [character/](../character/) — Character creation
- [room/](../room/) — Room creation
- [ontology/](../ontology/) — Tag system
- [real-being/](../real-being/) — The opposite tag
