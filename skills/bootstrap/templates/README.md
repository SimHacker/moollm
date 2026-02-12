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
│       ├── moollm-core.mdc.tmpl    # Always-on: includes ambient skill GLANCEs
│       ├── adventure.mdc.tmpl
│       └── introspection.mdc.tmpl
└── dotmoollm/          # → .moollm/
    ├── README.md
    ├── hot.yml
    ├── cold.yml
    ├── working-set.yml
    └── startup.yml
```

## Ambient Skill Inlining

The `moollm-core.mdc.tmpl` template includes an ambient skills section. At compile
time, the bootstrap process should:

1. Scan `skills/*/GLANCE.yml` for files with `ambient: true`
2. Inline their GLANCE content into the compiled `.cursor/rules/moollm-core.mdc`
3. This ensures the LLM sees ambient constraints (NO-AI hygiene suite, etc.)
   on every session without needing to discover or load them

The same ambient content is also inlined into `.cursorrules` for platforms that
read that file directly.

To find ambient skills manually: `grep -rl "^ambient: true" skills/*/GLANCE.yml`

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
