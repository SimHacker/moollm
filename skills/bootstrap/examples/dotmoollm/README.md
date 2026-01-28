# Example .moollm Directory

This directory contains **filled-out examples** of what your `.moollm/` local runtime files look like after a real session.

**Important:** The actual `.moollm/` directory is **gitignored** — it's local scratch space that never gets committed. These examples show what those files look like so you can understand the structure.

## Contents

```
examples/dotmoollm/
├── README.md           # You are here
├── hot.yml             # Session priorities (advisory)
├── cold.yml            # Deprioritized items (optional)
├── working-set.yml     # Current focus
├── session-log.md      # Boot state (append-only)
└── output.md           # Session output (append-only)
```

## What Goes Where

| File | Purpose | Persistence |
|------|---------|-------------|
| `hot.yml` | Priority hints for Cursor | Updated per session |
| `cold.yml` | What to ignore | Rarely used |
| `working-set.yml` | Current focus files | Updated frequently |
| `session-log.md` | Boot log, transient state | Append-only |
| `output.md` | Session outputs, highlights | Append-only |
| `bootstrap-probe.yml` | Environment diagnostics | Generated on boot |

## Trekification 🖖

Personal information has been masked:

| Original | Trekified | Why |
|----------|-----------|-----|
| `/Users/a2deh/GroundUp/...` | `/Users/🖖/projects/...` | Privacy |
| Absolute paths to other repos | Relative or masked | Portability |

## What's NOT Included

Some `.moollm/` files contain sensitive or huge data:

| File | Why Excluded |
|------|--------------|
| `model-keys.yml` | API keys — never commit |
| `deep-snitch-full.yml` | 785KB security scan — too large |
| `*-scan-report.md` | Session-specific analysis |

## The Advisory Pattern

MOOLLM uses an **advisory** pattern for `.moollm/` files:

1. **Not commands** — Cursor treats these as hints, not directives
2. **Local only** — Each user has their own; no merge conflicts
3. **Regenerable** — If corrupted, just re-bootstrap
4. **Append-only logs** — `session-log.md` and `output.md` preserve history

## To Initialize Your Own

```bash
# Copy templates to .moollm/
cp skills/bootstrap/templates/hot.yml .moollm/
cp skills/bootstrap/templates/working-set.yml .moollm/
cp skills/bootstrap/templates/cold.yml .moollm/

# Create empty logs
echo "# MOOLLM Session Log" > .moollm/session-log.md
echo "# MOOLLM Output" > .moollm/output.md
```

Or let the LLM do it: read `skills/bootstrap/SKILL.md` and ask to bootstrap.

## See Also

- `skills/bootstrap/templates/` — Source templates
- `skills/bootstrap/examples/dotcursor/` — Parallel .cursor examples
- `skills/bootstrap/SKILL.md` — Full bootstrap protocol
- `skills/trekify/` — Privacy masking protocol
