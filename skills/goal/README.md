# Goal

Quest objectives that drive the adventure forward.

## Quick Use

```yaml
id: find-treasure
name: "Find the Treasure"
description: "Locate the legendary treasure in the maze."
done_when: "player has the treasure"
reward:
  narrative: "Gold glitters in your hands!"
```

## Key Concepts

- **done_when** — Natural language condition (compiles to JS/PY); `complete_when` is read the same way
- **fail_when** — When goal becomes impossible
- **progress** — Track partial completion
- **children** — Nested sub-goals
- **history** — Events are stored; pending, active, done and failed are computed

A goal is a state someone wants. A [task](../task/) inherits goal and adds an owner who
claims the work. An [action](../action-queue/) is one queued step of that work.

See [SKILL.md](./SKILL.md) for full documentation.
