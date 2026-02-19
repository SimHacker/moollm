# Showboat Skill

Simon Willison's CLI for coding agents to build executable demo documents.

Agents use `showboat init/note/exec/image` to construct a Markdown document
section by section, with real command output captured inline. The result is
shareable proof that code works -- not just "tests pass."

## Files

| File | Purpose |
|------|---------|
| GLANCE.yml | Quick orientation |
| CARD.yml | Interface: methods, ecosystem, cursor-mirror integration |
| SKILL.md | Full protocol: commands, streaming, ecosystem, design decisions |
| README.md | This file |

## Quick Start

```bash
# No install required
uvx showboat --help

# Or tell your agent:
# "Run 'uvx showboat --help' and use showboat to demo the feature you just built."
```

## Ecosystem

| Tool | Purpose | Install |
|------|---------|---------|
| Showboat | Core demo doc builder | `uvx showboat` |
| Rodney | Browser automation + screenshots | `uvx rodney` |
| Chartroom | Charts from CSV/SQL | `uvx chartroom` |
| datasette-showboat | Real-time streaming to Datasette | `datasette install datasette-showboat` |

## Connection to MOOLLM

Showboat's `--help` as complete agent instruction set is the same pattern
as MOOLLM's semantic image pyramid (GLANCE -> CARD -> SKILL.md). Simon
arrived at this independently. Both solve: "how does the agent learn to
use this tool with minimum context?"
