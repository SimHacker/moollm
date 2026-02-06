# SKILL-SNITCH DEEP PROBE REPORT
## schema-factory — Build, lint, ingest, compose Drescher-style schemas

**Date**: 2026-02-06
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: TOOL SKILL — DETERMINISTIC LAYER
**Status**: Schema-schema defined, CLI interface documented, tool not yet implemented

---

## EXECUTIVE SUMMARY

The practical companion to schema-mechanism. Provides four deterministic operations on Drescher-style schemas: LINT (validate against schema-schema), INGEST (update from experience logs), COMPOSE (build action chains toward goals), CONTEXT (generate compact LLM context bundles). The central design principle: deterministic checks first, LLM second.

The schema-schema (SCHEMA-SCHEMA.yml, 82 lines) is fully specified. The CLI tool (`schema_tool.py`) is documented in CARD, SKILL, and README but does not exist on disk yet. Four example files demonstrate the schema format across two domains: Leela edgebox infrastructure (13 schemas) and Henry Minsky's blocksworld microworld (13 schemas).

This is the bridge between Drescher's theoretical schema mechanism and practical LLM orchestration.

**Overall Assessment**: APPROVE — clean design, solid examples, zero execution surface (tool not yet built)

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| GLANCE.yml | 47 lines | NONE |
| CARD.yml | 129 lines | NONE |
| SKILL.md | 192 lines | NONE |
| README.md | 71 lines | NONE |
| SCHEMA-SCHEMA.yml | 82 lines | NONE — prescriptive validation rules |
| examples/schema-example.yml | 21 lines | NONE |
| examples/henry-minsky-blocksworld.yml | 243 lines | NONE |
| examples/edgebox-ingest-runner.yml | 71 lines | NONE |
| examples/schema-jazz-example.yml | 506 lines | NONE |
| Total skill size | 9 files, ~1,362 lines | NONE |
| Executable code | None (schema_tool.py referenced but not on disk) | NONE |
| Required tools | read_file, write_file | LOW |
| Recommended tools | shell (for running schema_tool.py when built) | LOW |
| Tier | 2 | Expected for tool skill |

---

## WHAT IT DOES

### The Four Operations

| Method | Type | Input | Output |
|--------|------|-------|--------|
| LINT | Deterministic | Schema file | Pass/fail + diagnostics |
| INGEST | Deterministic | Experience log + schema file | Updated schemas + evidence counts |
| COMPOSE | Hybrid | Schema set + goal | Action chain + rationale |
| CONTEXT | Hybrid | Schema set + goal + focus | Compact LLM context bundle |

LINT and INGEST are purely deterministic — no LLM calls. COMPOSE and CONTEXT may involve LLM synthesis after deterministic preparation.

### Schema Structure

Every schema has:

| Field | Required | Description |
|-------|----------|-------------|
| id | YES | Stable identifier |
| action | YES | What the schema does |
| context | YES | Pre-conditions (list, min 1) |
| result | YES | Post-conditions (list, min 1) |
| reliability | No | 0.0-1.0 confidence |
| evidence | No | Success/failure counts |
| extended_context | No | Marginal attribution data |
| extended_results | No | Side-effect correlations |
| synthetic_items | No | Hidden-state hypotheses |
| composite_actions | No | Derived action sequences |

### The Schema-Schema

SCHEMA-SCHEMA.yml defines what valid schemas must look like:
- Required fields and types
- Reliability range (0.0-1.0)
- Non-empty context and result constraints
- Extension field patterns
- Deterministic checks: `required_fields_present`, `types_valid`, `reliability_in_range`, `context_result_nonempty`, `action_nonempty`, `evidence_nonnegative`

The schema-schema governs schemas. And it can evolve via the same learning loop it governs — self-referential validation.

### Examples

| File | Domain | Schemas | Purpose |
|------|--------|---------|---------|
| schema-example.yml | Leela ops | 2 | Minimal example (postgres → pyvision) |
| henry-minsky-blocksworld.yml | Microworld | 13 | Classic blocks/hand/eye — reach, grasp, foveate, lift, place |
| edgebox-ingest-runner.yml | Leela ops | 3 | Verify-ingest-start-flush pipeline |
| schema-jazz-example.yml | Both | 22+ | YAML Jazz annotated schemas across both domains |

The henry-minsky-blocksworld.yml is significant: it implements Drescher's actual schema mechanism examples from "Made-Up Minds" with data from Henry Minsky's pyleela implementation. This is the theoretical foundation made concrete.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: DETERMINISTIC TOOL — validation and composition, minimal LLM dependency

| Check | Result |
|-------|--------|
| Bias declared | N/A — deterministic validation, no opinion surface |
| Invertibility | STRUCTURAL — LINT validates (forward), but lint rules define what's "valid" (bias toward schema-schema's structure) |
| Multi-purpose | YES — validation, learning, planning, context generation |
| Persona capability | NO |
| Mounting modes | N/A — standalone tool |

**Multi-purpose classification** (4 purposes):
1. **Validation** — schema linting against prescriptive rules
2. **Learning** — ingesting experience into schema evidence counts
3. **Planning** — composing action chains toward goals
4. **LLM preparation** — generating compact context bundles

**Key design insight**: The skill explicitly separates what Python can do deterministically (LINT, INGEST) from what needs LLM synthesis (refinement of COMPOSE chains, interpretation of CONTEXT bundles). This separation IS the dual-use boundary: the deterministic layer is fully auditable, the LLM layer is explicitly marked as synthesis.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |
| eval / exec | 0 | CLEAN |

### Missing Implementation

`schema_tool.py` is referenced in GLANCE, CARD, SKILL, and README with CLI signatures and examples. It does not exist on disk. All documentation describes the planned interface, not an existing tool.

This is an honest gap: the interface is designed, the examples exist, the implementation awaits.

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Methods, key_files, principles match CARD |
| CARD.yml | YES | Schema structure matches SCHEMA-SCHEMA.yml |
| SKILL.md | YES | CLI examples match CARD method signatures |
| README.md | YES | Minimal interface contract matches CARD |
| SCHEMA-SCHEMA.yml | YES | Deterministic checks match CARD's deterministic flag |
| examples/ | YES | All examples conform to schema-schema structure |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE

Zero executable code on disk. The planned `schema_tool.py` will require `read_file`, `write_file`, and optionally `shell`. When implemented, the security surface will be: YAML file parsing (use `yaml.safe_load`), file writes (scoped to schema directories), and shell execution (if using CLI mode).

**Future recommendation**: When `schema_tool.py` is built, use `yaml.safe_load` only, validate all file paths against directory boundaries, and emit audit events for all schema modifications.

---

## TRUST TIER

**GREEN** — Clean design document with solid examples grounded in Drescher's actual schema mechanism. No executable code. The prescriptive schema-schema and deterministic-first principle make the eventual implementation highly auditable.

---

## VERDICT

The practical half of the schema-mechanism theoretical skill. Well-designed interface with four clean operations. The schema-schema provides prescriptive validation that makes schemas auditable. Examples span two domains (Leela infrastructure and Drescher's blocksworld), grounding the design in both practical ops and theoretical foundations.

The YAML Jazz example (506 lines) demonstrates how schemas can carry informal annotations alongside formal structure — the skill practices what MOOLLM preaches about comments as semantic data.

The missing `schema_tool.py` is honestly documented as planned. When built, the deterministic-first design will make it straightforward to audit: Python does validation, LLM does synthesis, the boundary is explicit.

APPROVE.
