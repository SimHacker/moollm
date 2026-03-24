# Drescher causal schema (schemapedia: `drescher`)

**Causal family.** “Schema” means **learned units** of Context → Action → Result (marginal attribution, composition)—**not** JSON/XML wire validation. Indexed so the word *schema* does not collapse into interchange alone.

## Why it matters here

MOOLLM separates **Drescher-style** causal structure from [json-schema](../json-schema/README.md) on purpose. Serialization between causal records and payloads is **project-specific**—see [`../../drescher-mapping.yml`](../../drescher-mapping.yml).

## What’s distinctive

- **Gary Drescher**’s framework (see *Good and Real* for philosophical grounding of deterministic decision and prediction—Wikipedia link below for author context).
- **Delegates** to [`schema-mechanism`](../../../../schema-mechanism/SKILL.md) (theory) and [`schema-factory`](../../../../schema-factory/) (tooling generation)—[`MECHANISM.yml`](./MECHANISM.yml) `delegate` map.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [json-schema](../json-schema/README.md) | Different sense of “schema”; bridge only via explicit mapping tables. |
| [sqlite](../sqlite/README.md) | Causal logs can persist as rows; DDL ≠ JSON Schema—document both. |
| [yaml-jazz](../yaml-jazz/README.md) | YAML may *carry* causal docs; validation of *meaning* is still not JSON Schema. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| MOOLLM theory | [`skills/schema-mechanism/SKILL.md`](../../../../schema-mechanism/SKILL.md) |
| Author | [Wikipedia: Gary Drescher](https://en.wikipedia.org/wiki/Gary_Drescher) |
| Book (context) | *Good and Real* (MIT Press)—philosophy of decision/prediction; not a JSON spec |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Mapping notes: [`../../drescher-mapping.yml`](../../drescher-mapping.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
