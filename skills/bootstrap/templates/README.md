# Bootstrap Templates

Source templates for MOOLLM configuration files.

## Structure

```
templates/
├── README.md           # You are here
├── GLANCE.yml.tmpl     # Template for skill GLANCE files
├── dotcursor/          # → .cursor/
│   ├── README.md
│   └── rules/
│       ├── moollm-core.mdc.tmpl
│       ├── adventure.mdc.tmpl
│       └── introspection.mdc.tmpl
└── dotmoollm/          # → .moollm/
    ├── README.md
    ├── hot.yml
    ├── cold.yml
    ├── working-set.yml
    └── startup.yml
```

## Parallel Examples

Each template directory has a corresponding example:

| Templates | Examples | Purpose |
|-----------|----------|---------|
| `templates/dotcursor/` | `examples/dotcursor/` | .cursor rules |
| `templates/dotmoollm/` | `examples/dotmoollm/` | .moollm runtime |

**Templates** have `{{handlebars}}` expressions.
**Examples** show filled-out real values (trekified for privacy).

## Quick Start

```bash
# Initialize .cursor
mkdir -p .cursor/rules
cp templates/dotcursor/rules/*.tmpl .cursor/rules/
cd .cursor/rules && for f in *.tmpl; do mv "$f" "${f%.tmpl}"; done

# Initialize .moollm
mkdir -p .moollm
cp templates/dotmoollm/*.yml .moollm/
echo "# MOOLLM Session Log" > .moollm/session-log.md
echo "# MOOLLM Output" > .moollm/output.md
```

Or let the LLM do it: read `skills/bootstrap/SKILL.md` and ask to bootstrap.

## See Also

- `../examples/` — Filled-out examples (trekified)
- `../SKILL.md` — Full bootstrap protocol
- `../../trekify/` — Privacy masking
