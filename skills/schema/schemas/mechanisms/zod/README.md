# Zod (schemapedia: `zod`)

**Interchange family (TypeScript-native).** Runtime schemas and inferred static types—`z.infer<typeof Schema>`—for configs, tool IO, and app boundaries where the stack is already TS-first.

## Why it matters here

Zod is the **ecosystem default** for “validate this object in Node/Bun/Deno” when you are not publishing a portable JSON Schema document first. The schemapedia lists it beside [json-schema](../json-schema/README.md) because pipelines often **port** between them ([`../../gateways.yml`](../../gateways.yml): `json-schema-to-zod`).

## What’s distinctive

- **TypeScript-first**: validation and types stay in one place; not a wire standard like JSON Schema’s IETF drafts.
- **Not** [drescher](../drescher/README.md): causal “Context → Action → Result” lives in `schema-mechanism`, not in Zod.
- Pairs with [yaml-jazz](../yaml-jazz/README.md) when YAML is authored: Zod validates the **parsed tree**; Jazz still owns comments and COP.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [json-schema](../json-schema/README.md) | Bidirectional codegen/hand ports; feature overlap is partial. |
| [yaml-jazz](../yaml-jazz/README.md) | Same tree, different layers: Zod = value; Jazz = source file semantics. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Docs | [zod.dev](https://zod.dev/) |
| Source | [GitHub: colinhacks/zod](https://github.com/colinhacks/zod) |
| Context | [Wikipedia: Data validation](https://en.wikipedia.org/wiki/Data_validation) (no dedicated Zod article; ecosystem is young) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
