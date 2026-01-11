# Container Skill

**Intermediate scopes for inheritance — like OpenLaszlo's `<node>`.**

## Quick Start

Create `CONTAINER.yml` in a directory to define shared properties:

```yaml
# maze/CONTAINER.yml
container:
  name: "The Twisty Maze"
  
  inherits:
    is_dark: true
    is_dangerous: true
    grue_rules:
      can_appear: true
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

## See Also

- [room](../room/) — Navigable locations
- [object](../object/) — Things in the world
- [adventure](../adventure/) — Root state
