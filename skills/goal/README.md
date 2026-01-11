# Goal

Quest objectives that drive the adventure forward.

## Quick Use

```yaml
goal:
  id: find-treasure
  name: "Find the Treasure"
  description: "Locate the legendary treasure in the maze."
  complete_when: "player has the treasure"
  reward:
    narrative: "Gold glitters in your hands!"
```

## Key Concepts

- **complete_when** — Natural language condition (compiles to JS/PY)
- **fail_when** — When goal becomes impossible
- **progress** — Track partial completion
- **children** — Nested sub-goals

See [SKILL.md](./SKILL.md) for full documentation.
