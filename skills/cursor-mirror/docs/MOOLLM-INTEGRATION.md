# Integration with MOOLLM

*Broken out of the cursor-mirror [README](../README.md).*

If you're using [MOOLLM](../../../MOOLLM.md) (a microworld operating system for LLM agents), cursor-mirror becomes the introspection layer. Not required, but powerful together.

**Optimize boot sequences**: Analyze what context MOOLLM loaded vs. what was used. Trim the fat.

**Refine kernel drivers**: The Cursor driver (`kernel/drivers/cursor.yml`) needs real data. cursor-mirror provides it.

**Debug simulations**: MOOLLM runs multi-agent simulations. cursor-mirror traces what each turn actually did.

### Kernel/Drivers

The kernel driver (`kernel/drivers/cursor.yml`) adapts MOOLLM to Cursor. cursor-mirror populates it with real data:

```bash
# Discover actual tool names (v2 suffix)
cursor-mirror tools @1 | grep -oE '\w+_v2'

# Discover limits
cursor-mirror status-config --yaml

# Discover MCP servers
cursor-mirror status-mcp --yaml
```

### Bootstrap/Probe

The bootstrap skill (`skills/bootstrap/`) wakes MOOLLM and probes the environment. cursor-mirror provides the `CURSOR-PROBE` method:

```bash
# Generate probe cache
cursor-mirror status --yaml > .moollm/cursor-probe-cache.yml
cursor-mirror status-config --yaml >> .moollm/cursor-probe-cache.yml
cursor-mirror status-mcp --yaml >> .moollm/cursor-probe-cache.yml
```

### Advisory Files

MOOLLM uses `hot.yml`, `cold.yml`, `working-set.yml` for context hints. On Cursor, these are **advisory** — Cursor makes its own decisions. cursor-mirror reveals what Cursor actually focused on:

```bash
# See actual file focus
cursor-mirror context-sources @1 --yaml

# Reverse-generate working-set from observed behavior
cursor-mirror files @1 --yaml > .moollm/working-set.yml
```
