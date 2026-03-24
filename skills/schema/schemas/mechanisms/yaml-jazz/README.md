# YAML Jazz (schemapedia: `yaml-jazz`)

**Notation family.** MOOLLM’s convention: **comments are first-class data**—three audiences (human, LLM, machine), semantic commentary beside the parsed tree, and **COP** (Comment-Oriented Programming): constraints and transforms **authored in comments** where the stack preserves them.

## Why it matters here

[json-schema](../json-schema/README.md) validates the **value tree** after parse; it cannot see comments. YAML Jazz is how MOOLLM keeps **intent, history, and instance-specific instructions** in the **same file** as data—without pretending JSON can round-trip that layer.

## What’s distinctive

- **Not** a substitute for interchange validation: pair with JSON Schema or [zod](../zod/README.md) when you need both **shape** and **source-file semantics**.
- **Round-trip** requires comment-preserving parsers (e.g. `ruamel.yaml` in Python); many stacks **drop** comments on save—know your toolchain.
- **Delegate**: [`yaml-jazz`](../../../../yaml-jazz/SKILL.md), examples under `skills/yaml-jazz/examples/`.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [json-schema](../json-schema/README.md) | Complementary; gateway `json-schema-with-yaml-jazz` in [`../../gateways.yml`](../../gateways.yml). |
| [zod](../zod/README.md) | TS stacks: Zod + Jazz same as JSON Schema + Jazz. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| MOOLLM | [`skills/yaml-jazz/SKILL.md`](../../../../yaml-jazz/SKILL.md) |
| Format | [YAML](https://yaml.org/) — [Wikipedia: YAML](https://en.wikipedia.org/wiki/YAML) |
| Tooling | `yq` (verify comment preservation per implementation)—[`MECHANISM.yml`](./MECHANISM.yml) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
