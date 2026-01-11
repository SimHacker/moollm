# Exit

Navigation links between rooms. The edges of the memory palace.

## Quick Use

```yaml
exits:
  north:
    destination: ../maze/room-a/
    description: "A dark passage leads north."
    
  east:
    destination: ../treasury/
    guard: "player has the key"
    locked: true
```

## Key Concepts

- **Direction** — N/S/E/W are highways, diagonals are grids
- **Guard** — Natural language condition (compiles to JS/PY)
- **Hidden** — Discoverable exits
- **Metaphysical** — Non-physical transitions

See [SKILL.md](./SKILL.md) for full documentation.
