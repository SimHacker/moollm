# Context

The runtime world passed to compiled closures.

## Quick Reference

```javascript
// Standard — always present
world.turn              // Simulation turn
world.adventure         // Root state
world.player            // Current player
world.room              // Current room
world.party             // Party state

// Extended — when relevant
world.object            // Object being simulated
world.target            // Action target
world.npc               // NPC being simulated

// Skill state — namespaced with underscores!
world.skills.economy.gold        // skill "economy"
world.skills.pie_menu.selection  // skill "pie-menu" → pie_menu

// Utility functions
world.emit("message")
world.has("item-id")
world.flag("flag-name")
world.trigger_event("EVENT_NAME")
world.go("../room/")
```

## Why "world" not "ctx"?

- More evocative — closures see the WORLD
- Self-documenting — `world.player`, `world.room`
- Matches the mental model

## Why underscores in skill namespaces?

Dashes aren't valid JS/Python identifiers:
- `pie-menu` skill → `world.skills.pie_menu`
- `foo-bar` skill → `world.skills.foo_bar`

See [SKILL.md](./SKILL.md) for full documentation.
