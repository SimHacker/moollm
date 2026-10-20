# 📦 Container

> Intermediate scopes that pass values down, like OpenLaszlo's `<node>`.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Navigable locations (containers aren't) |
| [object/](../object/) | Things in containers |
| [adventure/](../adventure/) | Root state |
| [prototype/](../prototype/) | Delegation; `resolve.py` applies container defaults |
| [logistic-container/](../logistic-container/) | Factorio-style extension |
| [examples/adventure-4/maze/](../../examples/adventure-4/maze/) | Container for dark rooms |

## Quick Start

Create `CONTAINER.yml` in a directory:

```yaml
# maze/CONTAINER.yml
name: "The Twisty Maze"
defaults:
  room:
    lighting: 0
```

Every room inside `maze/` now has `lighting: 0` unless it says otherwise.

## When to Use

| Use Case | Example |
|----------|---------|
| Shared room values | All maze rooms are dark |
| Character categories | All animals have instincts |
| Object collections | All appliances need power |
| Regional rules | No magic works in this zone |

## Container vs Room

- **Container**: not navigable; its `defaults:` reach what's inside
- **Room**: navigable, has exits

## Files

- `CONTAINER.yml.tmpl`: template with every field
- `SKILL.md`: lookup order, merge rules, tools
