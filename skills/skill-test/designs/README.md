# skill-test design docs

K-line named design docs, grouped by **source** (runner vs per-skill). Names describe content and source.

| K-line | Path | Content / source |
|--------|------|-------------------|
| RUNNER-DESIGN | [runner/RUNNER-DESIGN.md](runner/RUNNER-DESIGN.md) | Harness, config schema, placement, relation to skill-snitch and cursor-mirror. Source: moollm designs. |
| CONTEXT-BENCHMARKS | [runner/CONTEXT-BENCHMARKS.md](runner/CONTEXT-BENCHMARKS.md) | Test skills against benchmarks with SKILL.md only, skill dir, MOOLLM subsets, or full ecosystem; measure alone vs ecosystem and which subsets suffice. Source: skill-test. |
| CURSOR-MIRROR-VALIDATION-SUITE | [cursor-mirror/VALIDATION-SUITE.md](cursor-mirror/VALIDATION-SUITE.md) | What to validate for cursor-mirror; layers; example test config; pipeline hook. Source: cursor-mirror. |

Big-endian convention: subdirs by source/skill; filenames = k-lines. Add new skills under `designs/<skill-id>/` with k-line filenames (e.g. `VALIDATION-SUITE.md`, `CONFIG-EXAMPLE.yml`).
