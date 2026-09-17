# Archive

Superseded material, kept because deleting it would break the record and because the reasoning in
it is sometimes still worth reading. Nothing in here is current.

**The rules.**

- Current material never links into `archive/`. If a live document needs something from here, the
  thing it needs has a modern home — link that instead.
- Archived skills are not invokable. They are out of the skill count and out of the indexes.
- Files are moved, not rewritten. Relative links were repaired for the new depth; the prose is as
  it was.
- Each entry below says what replaced it, so a reader who lands here from an old URL can get to the
  live version in one hop.

## sim-obliterator

The first cut at moving Sims characters between games. Retired because it shelled out to a Python
sister repo that has since been rewritten in TypeScript, and because its vocabulary — import,
export, obliterate — was replaced by the language the project actually uses now.

| What | Where it lives now |
|---|---|
| The protocol: two gates, conservation, fork-and-sync | [`skills/soul-city/SOUL-BRIDGES.md`](../skills/soul-city/SOUL-BRIDGES.md) |
| The vocabulary: transmigration, refugees, souvenirs | [`skills/soul-city/GLOSSARY.md`](../skills/soul-city/GLOSSARY.md) |
| The framing, and where to start reading | [`skills/soul-city/README.md`](../skills/soul-city/README.md) |
| Field mapping, `PersonData` ↔ soul file, in TypeScript | MicropolisCore [`packages/sims-io`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io) |
| Resource layers | MicropolisCore [`packages/vitamoo`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/vitamoo) |
| The build plan | MicropolisCore [`documentation/designs/soul-city-uplift-roadmap.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city-uplift-roadmap.md) |

- `sim-obliterator/designs/` — the design docs, including the per-document forwarding table in its
  own `README.md`.
- `sim-obliterator/skill/` — the retired skill, including the Python scripts it drove.
