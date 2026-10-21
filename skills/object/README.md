# Object

Interactable things in the adventure world.

## Quick Use

```yaml
# pub/brass-key.yml
id: brass-key
name: "Brass Key"
emoji: "🔑"
description: "A heavy brass key."
takeable: true

advertisements:
  EXAMINE:
    description: "Look closely"
    score: 50
```

## Key Concepts

- **Advertisements** — Objects announce what they can do (SimAntics)
- **State** — Mutable properties (lit, fuel, uses)
- **Inherits** — Prototype chain (Self-style)
- **Container** — Can hold other objects
- **Prototype** — [OBJECT.yml](OBJECT.yml) holds what every object has; [examples/](examples/) has worked objects

See [SKILL.md](./SKILL.md) for full documentation.
