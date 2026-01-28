# Example .cursor Directory

This is an example of what a filled-out `.cursor/` directory looks like after bootstrap.

**Source:** These files were compiled from `skills/bootstrap/templates/cursor-rules/*.mdc.tmpl` with real values from a working session.

**Paths trekified:** Personal paths like `/Users/🖖/` have been masked per the trekify protocol.

## Contents

```
.cursor/
└── rules/
    ├── moollm-core.mdc    # Always on — identity and reading order
    ├── adventure.mdc      # Glob: examples/** — adventure mode
    └── introspection.mdc  # Glob: skills/cursor-mirror/** — debugging
```

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
cp skills/bootstrap/templates/cursor-rules/*.mdc.tmpl .cursor/rules/
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
