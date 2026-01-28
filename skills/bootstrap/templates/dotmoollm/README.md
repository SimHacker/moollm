# .moollm Templates

Templates for MOOLLM local runtime files.

## Contents

```
dotmoollm/
├── hot.yml          # Session priorities (advisory)
├── cold.yml         # Deprioritized items
├── working-set.yml  # Current focus
└── startup.yml      # Startup commands
```

## Usage

Copy these to `.moollm/` and customize:

```bash
mkdir -p .moollm
cp skills/bootstrap/templates/dotmoollm/*.yml .moollm/

# Create empty logs
echo "# MOOLLM Session Log" > .moollm/session-log.md
echo "# MOOLLM Output" > .moollm/output.md
```

## File Purposes

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `hot.yml` | Priority hints for Cursor | Per session |
| `cold.yml` | What to ignore | Rarely |
| `working-set.yml` | Current focus | Frequently |
| `startup.yml` | Commands to run on boot | Per project |

## The Advisory Pattern

These files are **advisory** — hints, not commands:

1. Cursor treats them as suggestions
2. Each user has their own (no merge conflicts)
3. Regenerable if corrupted
4. Not version controlled (gitignored)

## See Also

- `../dotcursor/` — Parallel .cursor templates
- `../../examples/dotmoollm/` — Filled-out examples
