# cursor-mirror design docs

Design and process documents for the cursor-mirror skill. Reference data (KEY-CATALOG, assimilated YAML, universal model) stay in **reference/**; design docs live here.

| Doc | Purpose |
|-----|---------|
| [ASSIMILATION-PROCESS.md](ASSIMILATION-PROCESS.md) | Stage 1 -> 2 -> 3: per-source import, universal model synthesis, validate -> evolve. Attribution, reverse-engineered dir, pipeline. |
| [VALIDATION-DESIGN.md](VALIDATION-DESIGN.md) | Summary + ref. Full design: **skills/skill-test/designs/cursor-mirror/VALIDATION-SUITE.md**. |
| [INPUT-OUTPUT-PIPELINE.md](INPUT-OUTPUT-PIPELINE.md) | Vision: quit Cursor -> read state.vscdb -> transform -> write back. Full import/export. |
| [REVERSE-ENGINEERED-DIR.md](REVERSE-ENGINEERED-DIR.md) | One dir for all reverse-engineered artifacts; big-endian naming; shared metadata core; by project. |
| [MOOCO-INTEGRATION.md](MOOCO-INTEGRATION.md) | MOOCO + cursor-mirror: precise context, k-line diffusion, cursor-mirror as tools, MOOCO-in-the-middle. |
