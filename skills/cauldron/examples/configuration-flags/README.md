# 🍲 Example: configuration-flags (placeholder)

**Status:** pending — trekified artifacts not yet generated.

This directory will hold the trekified teaching copy of a real-world cauldron brew:
a 30-turn Phase-1 monolith (1917 lines) plus a Phase-2 tree (27 files, 240+ internal
links, 13 playbooks) from the Leela AI configuration-flags refactor.

## What will land here

```
configuration-flags/
  README.md                — this file, filled out
  SUBSTITUTIONS.yml        — the trekify dictionary used
  MONOLITH.md              — trekified Phase-1 artifact (analogue of CONFIGURATION-FLAGS-PLAN.md)
  sharded/
    README.md
    01-overview.md .. 10-open-questions.md
    design-wisdom.md
    META-PLAN.md
    playbooks/
      README.md
      PB-01-*.md .. PB-13-*.md
  LESSONS.md               — wisdom extracted from this brew
```

## How to produce it

Run the SERVE pipeline over `leela-ai/central/docs/configuration/` using:

1. `trekify MASK-FILE` with a `SUBSTITUTIONS.yml` (dictionary draft lives in cauldron's CARD.yml).
2. `skill-snitch SCAN` on the masked output. Iterate any leaks.
3. `cauldron:LINK` (this repo's `scripts/link_check.py`) on the trekified tree.
4. `thoughtful-commitment COMMIT` the example as a PR against this directory.

See [../README.md](../README.md) for the contribution flow.

## Patron

🖖 Geordi La Forge — "Captain, I've routed the configuration refactor through the privacy buffers. The narrative is intact, the architecture is teachable, and every substitution is flagged for audit."
