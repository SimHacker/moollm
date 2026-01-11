# Runtime

Dual Python/JavaScript adventure engines — always in sync.

## The Rule

**ALWAYS generate BOTH `_js` AND `_py` code. Never one without the other.**

```yaml
guard: "player has brass-key"
guard_js: (world) => world.has("brass-key")
guard_py: lambda world: world.has("brass-key")
```

## Why Dual Runtimes?

| Runtime | Purpose |
|---------|---------|
| **Python** | Server, testing, LLM tethering |
| **JavaScript** | Browser, standalone play |

## The World Object

Both runtimes implement identical `World` classes with:

- Standard keys: `turn`, `adventure`, `player`, `room`, `party`
- Extended keys: `object`, `target`, `npc`
- Skill namespaces: `world.skills.economy.gold`
- Utility functions: `has()`, `emit()`, `flag()`, etc.

## Simulation Loop

Both runtimes tick the same way:
1. Increment turn
2. Simulate all objects in room
3. Process event queue
4. Process navigation

See [SKILL.md](./SKILL.md) for full documentation.
