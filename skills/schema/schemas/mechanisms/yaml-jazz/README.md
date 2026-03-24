# YAML Jazz (schemapedia: `yaml-jazz`)

**Notation family.** MOOLLM’s convention: **comments are first-class data**—three audiences (human, LLM, machine), semantic commentary beside the parsed tree, and **COP** (Comment-Oriented Programming): constraints and transforms **authored in comments** where the stack preserves and interprets them.

## Why it matters here

[json-schema](../json-schema/README.md) validates the **value tree** after parse; it cannot see comments. YAML Jazz is how MOOLLM keeps **intent, history, and instance-specific instructions** in the **same file** as data—without pretending JSON can round-trip that layer.

## What’s distinctive

- **Not** a substitute for interchange validation: delegate to **[json-schema](../json-schema/README.md)** (language-neutral wire shapes) and/or **[zod](../zod/README.md)** (TypeScript-first runtime schemas) when you need **validated tree shape** as well as **source-file semantics** (comments, COP). Same parsed value can satisfy both Jazz and a validator; Jazz still owns the comment channel.
- **Round-trip** requires comment-preserving parsers (e.g. `ruamel.yaml` in Python); many stacks **drop** comments on save—know your toolchain.
- **Delegate**: [`yaml-jazz`](../../../../yaml-jazz/SKILL.md), examples under `skills/yaml-jazz/examples/`.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [json-schema](../json-schema/README.md) | Complementary; gateway `json-schema-with-yaml-jazz` in [`../../gateways.yml`](../../gateways.yml). |
| [zod](../zod/README.md) | TS stacks: same pattern as JSON Schema—Zod on the **parsed tree**, Jazz on the **source YAML**; see [zod](../zod/README.md) `mechanism_relations` and [`../../gateways.yml`](../../gateways.yml) `json-schema-to-zod` when translating specs. |

### XML interchange peers (same registry, different text)

YAML Jazz is for **YAML** authoring. **[xml-schema](../xml-schema/README.md)** (W3C XSD) and **[relax-ng](../relax-ng/README.md)** (RELAX NG) are the **XML** interchange pair: both constrain XML infosets; RNG uses compact or XML syntax and different ergonomics than XSD’s type system. **Bridging:** **`gateways.yml`** lists **`xsd-relax-ng`** (translation; **Trang** is the usual RNG ↔ XSD tool; **Jing** validates RNG). **Fidelity** is not guaranteed for every XSD feature—treat as project policy, not automatic port. For **XML → JSON** shape work, see **`xml-json`** in [`../../gateways.yml`](../../gateways.yml) (design-time mapping, not a universal one-click bridge).

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| MOOLLM | [`skills/yaml-jazz/SKILL.md`](../../../../yaml-jazz/SKILL.md) |
| Format | [YAML](https://yaml.org/) — [Wikipedia: YAML](https://en.wikipedia.org/wiki/YAML) |
| Tooling | `yq` (verify comment preservation per implementation)—[`MECHANISM.yml`](./MECHANISM.yml) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
