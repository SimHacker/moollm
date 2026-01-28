# Example .cursor and .moollm Files

This directory contains **filled-out examples** of what your `.cursor/` and `.moollm/` files look like after a real bootstrap session.

**Source:** Compiled from `skills/bootstrap/templates/` with actual values from a working MOOLLM session.

**Purpose:** Learn by example. Compare these to the templates to understand what gets filled in.

## Contents

```
examples/dotcursor/
├── README.md               # You are here
├── bootstrap-probe.yml     # Environment diagnostics + mipmap metrics
└── rules/
    ├── moollm-core.mdc     # Always on — identity and reading order
    ├── adventure.mdc       # Glob: examples/** — adventure mode
    └── introspection.mdc   # Glob: skills/cursor-mirror/** — debugging
```

## Trekification 🖖

Personal information has been **trekified** — masked with Star Trek technobabble or the 🖖 emoji.

| Original | Trekified | Why |
|----------|-----------|-----|
| `/Users/a2deh/GroundUp/...` | `/Users/🖖/moollm` | Privacy — no real usernames |
| `121971` messages | kept as-is | Not personally identifying |
| `claude-4-sonnet` | kept as-is | Model names are public |

The trekify protocol (see `skills/trekify/`) replaces sensitive data with plausible-looking nonsense. In examples, we use the 🖖 emoji as a visible marker that something was masked.

**What gets trekified:**
- Absolute paths containing usernames
- API keys, tokens, secrets
- Personal identifiers

**What stays:**
- Relative paths (they're portable)
- Public information (model names, counts)
- Technical metrics (they're educational)

## How Cursor Uses These

| File | `alwaysApply` | `globs` | When Active |
|------|---------------|---------|-------------|
| `moollm-core.mdc` | `true` | — | Every conversation |
| `adventure.mdc` | `false` | `examples/**` | Only in adventure world |
| `introspection.mdc` | `false` | `skills/cursor-mirror/**,.moollm/**` | Only when debugging |

## To Generate Your Own

1. Delete `.cursor/rules/` (or start fresh)
2. Run bootstrap: read `skills/bootstrap/SKILL.md`
3. The LLM will compile templates → rules

Or manually copy templates and remove `.tmpl` extension:

```bash
mkdir -p .cursor/rules
cp skills/bootstrap/templates/dotcursor/rules/*.mdc.tmpl .cursor/rules/
cd .cursor/rules
for f in *.tmpl; do mv "$f" "${f%.tmpl}"; done
```

## Template Variables

These examples show template expressions filled in. In the templates, you'll see:
- `{{skill_count}}` → `117`
- `{{world_tree}}` → actual directory tree
- `{{#if optimization_permitted}}` → conditional content
- `{{probe_results}}` → output from cursor-mirror

The LLM fills these during bootstrap based on actual state.

## File Descriptions

### `bootstrap-probe.yml`

Environment diagnostics and optimization metrics. Contains:
- **Platform info**: OS, shell, workspace path (trekified)
- **Cursor status**: Composers, messages, MCP servers, model
- **Semantic mipmap**: Real word/token counts at each resolution level
- **Boot order**: Recommended file loading sequence
- **Efficiency analysis**: Example showing 69% savings via GLANCE files

### `rules/moollm-core.mdc`

Always-on identity rule. Injected every conversation. Contains:
- Core MOOLLM concepts (filesystem = space, YAML Jazz, K-lines)
- Mandatory first actions (read hot.yml, read INDEX.md)
- Semantic image pyramid (GLANCE → CARD → SKILL → README)
- Optimization protocol and example results

### `rules/adventure.mdc`

Adventure mode context. Only active when working in `examples/`. Contains:
- Boot sequence for characters
- World structure tree
- Large file warnings (use GLANCE first!)
- Character and room rosters

### `rules/introspection.mdc`

Debugging tools. Active when in cursor-mirror or .moollm/. Contains:
- cursor-mirror command reference
- Probe results example
- skill-snitch overview
- .moollm/ directory inventory

## See Also

- `skills/bootstrap/templates/` — The source templates with `{{handlebars}}`
- `skills/bootstrap/SKILL.md` — Full bootstrap protocol
- `skills/trekify/` — Privacy masking protocol
- `.moollm/` — Your local (gitignored) runtime files
