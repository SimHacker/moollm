# Schema Factory

Build, lint, ingest, compose, and generate context for Drescher-style schemas.

This skill is the practical companion to `schema-mechanism`. It provides a schema-schema, a deterministic linter, an ingestor for experience logs, and a context generator that emits events and a compact context bundle for LLM reasoning.

## Why This Exists

Gary Drescher's schema mechanism is strongest when it has:

- A **prescriptive schema-schema** (what valid schemas must look like)
- A **deterministic layer** that can evaluate and refine before asking the LLM
- A **context generator** that emits only the needed patterns and evidence

The goal is hybrid orchestration: Python does the deterministic work, Cursor/LLM handles synthesis, and MOOLLM stays explicit about what came from where.

## Key Files

- `SCHEMA-SCHEMA.yml` — the schema-schema that drives linting and ingestion
- `schema_tool.py` — lint, ingest, compose, and context generation
- `examples/schema-example.yml` — a compact schema set
- `examples/henry-minsky-blocksworld.yml` — blocks/hands/eyes microworld data examples (Drescher/Henry Minsky)
- `examples/edgebox-ingest-runner.yml` — edgebox ingest runner data examples (hypothetical hosts)
- `examples/schema-jazz-example.yml` — YAML Jazz schemas with annotated ad‑hoc notes

## Quick Use

```bash
python3 skills/schema-factory/schema_tool.py lint skills/schema-factory/examples/schema-example.yml
python3 skills/schema-factory/schema_tool.py compose --schemas skills/schema-factory/examples/schema-example.yml --goal postgres-running
python3 skills/schema-factory/schema_tool.py context --schemas skills/schema-factory/examples/schema-example.yml --goal pyvision-running
```

## Minimal Interface (Docs Only)

The schema-factory interface is intentionally small and deterministic. This is the minimal contract that any implementation should provide.

### Lint

- **Input:** one or more schema files (YAML)
- **Output:** pass/fail + diagnostics
- **Emits:** `schema_lint`
- **Deterministic checks:** required fields, type validation, reliability range, non-empty context/result

### Ingest

- **Input:** experience logs or observed transitions
- **Output:** updated schema set + evidence counts
- **Emits:** `schema_ingest`
- **Deterministic behavior:** no LLM calls; only schema updates

### Compose

- **Input:** schema set + goal
- **Output:** composed action chain (if available) + rationale
- **Emits:** `schema_compose`

### Context

- **Input:** schema set + goal + optional focus items
- **Output:** compact context bundle for LLM synthesis
- **Emits:** `context_generate`
- **Default include:** id, action, context, result, reliability, extended_context, extended_results

## Principles

- Deterministic checks first, LLM second.
- Emit events for traceability.
- Prefer small, explicit context bundles.
- The schema-schema can evolve via the same learning loop it governs.
