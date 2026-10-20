# 📦 Container

> Intermediate scopes for inheritance — like OpenLaszlo's `<node>`.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Navigable locations (containers aren't) |
| [object/](../object/) | Things in containers |
| [adventure/](../adventure/) | Root state |
| [prototype/](../prototype/) | Self-like delegation |
| [logistic-container/](../logistic-container/) | Factorio-style extension |
| [examples/adventure-4/maze/](../../examples/adventure-4/maze/) | Container for dark dangerous rooms |

## Quick Start

Create `CONTAINER.yml` in a directory to define shared properties:

```yaml
# maze/CONTAINER.yml
container:
  name: "The Twisty Maze"
  
  inherits:
    lighting: 0
```

All rooms inside `maze/` automatically inherit these properties!

## When to Use

| Use Case | Example |
|----------|---------|
| Shared room properties | All maze rooms are dark |
| Character categories | All animals have instincts |
| Object collections | All appliances need power |
| Regional rules | No magic works in this zone |

## Container vs Room

- **Container**: NOT navigable, provides inheritance
- **Room**: IS navigable, has exits

## Files

- `CONTAINER.yml.tmpl` — Template with all fields
- `SKILL.md` — Full documentation

