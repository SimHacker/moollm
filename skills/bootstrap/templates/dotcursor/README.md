# .cursor Templates

Templates for Cursor IDE configuration files.

## Contents

```
dotcursor/
└── rules/
    ├── moollm-core.mdc.tmpl    # Always on — identity, mipmap
    ├── adventure.mdc.tmpl      # Glob: examples/** — adventure mode
    └── introspection.mdc.tmpl  # Glob: cursor-mirror/** — debugging
```

## Template Variables

These templates use Handlebars-style expressions:

| Variable | Example Value | Source |
|----------|---------------|--------|
| `{{skill_count}}` | `117` | Count of skills/*/CARD.yml |
| `{{world_tree}}` | Directory tree | Generated from examples/ |
| `{{probe_results}}` | Status output | cursor-mirror commands |
| `{{#if condition}}` | Conditional | Runtime state |

## Compilation

Templates are compiled to `.cursor/rules/` on first boot:

```bash
# Manual compilation
mkdir -p .cursor/rules
for f in skills/bootstrap/templates/dotcursor/rules/*.tmpl; do
  cp "$f" ".cursor/rules/$(basename "${f%.tmpl}")"
done
```

Or let the LLM do it during bootstrap — it fills in the variables.

## See Also

- `../dotmoollm/` — Parallel .moollm templates
- `../../examples/dotcursor/` — Filled-out examples
