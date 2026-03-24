# JSON Schema (schemapedia: `json-schema`)

**Interchange family.** Describe and validate JSON *instances* (API bodies, configs, tool arguments). The parsed tree is what validators see; this mechanism is **not** Drescher causality and **not** YAML Jazz commentary.

## Why it matters here

MOOLLM uses JSON Schema at wire boundaries and in OpenAPI-style stacks. The registry keeps it **separate** from [yaml-jazz](../yaml-jazz/README.md) (notation) and [drescher](../drescher/README.md) (causal “schema”): same word, different jobs—see [`../../drescher-mapping.yml`](../../drescher-mapping.yml) when you must bridge.

## What’s distinctive

- **Draft 2020-12** is the common modern baseline; declare `$id` / `$defs` for reuse.
- Validates **data after parse**; if the source is YAML, the schema applies to the **loaded value**, not to comment text ([yaml-jazz](../yaml-jazz/README.md) owns comments).
- Natural pairing with HTTP/OpenAPI; rows in [sqlite](../sqlite/README.md) need an explicit app-level mapping ([`../../gateways.yml`](../../gateways.yml): `json-row-sqlite`).

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [yaml-jazz](../yaml-jazz/README.md) | Complementary: schema = tree shape; Jazz = file + comments. Bridge: `json-schema-with-yaml-jazz`. |
| [zod](../zod/README.md) | Translation/codegen between JSON Schema and Zod—subset and gaps are project-defined. |
| [sqlite](../sqlite/README.md) | API validates with JSON Schema; persistence uses SQL DDL—two contracts to document. |
| [github](../github/README.md) | REST/GraphQL bodies are JSON; often validated with JSON Schema or OpenAPI fragments. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Specification | [JSON Schema (2020-12)](https://json-schema.org/draft/2020-12/schema) |
| Project / org | [json-schema.org](https://json-schema.org/) |
| Overview | [Wikipedia: JSON Schema](https://en.wikipedia.org/wiki/JSON_Schema) |
| Tooling | [ajv](https://ajv.js.org/) (JS), [jq](https://jqlang.org/) (filter instances—[`MECHANISM.yml`](./MECHANISM.yml) lists `jq`, `ajv-cli`) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent skill: [`../../../SKILL.md`](../../../SKILL.md)
