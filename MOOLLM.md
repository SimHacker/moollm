# MOOLLM Microworld Manifest (Narrative)

This repository is a MOOLLM-enabled microworld. It is not itself a skill, but it follows the skill-like pattern for discoverability:

- Metadata: `MOOLLM.yml` (world id, driver, indices, templates)
- Skills live in `skills/`
- Kernel and drivers live in `kernel/`
- Current adventure: `examples/adventure-4/ADVENTURE.yml`

See `kernel/drivers/cursor.yml` for Cursor advisory behavior and `skills/bootstrap/` for the bootstrap sequence (PROBE → DETECT-DRIVER → SETUP → WARM-CONTEXT → SELF-DESCRIBE → STARTUP).
