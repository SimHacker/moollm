# Mechanism (schemapedia: `mechanism`)

**Registry_meta family.** Meta mechanism: the **shape of a schemapedia plugin**—`MECHANISM.yml`, optional **`SCHEMAPEDIA-*-AUGMENT.yml`**, **`mechanism_relations`**, hooks to **`registry.yml`** / **`gateways.yml`**, and **`templates/MECHANISM.yml`** as the empathic prototype. Indexed for navigation and self-description, **not** as a payload validator.

## Why it matters here

The registry already listed JSON Schema, YAML Jazz, git, and the rest as **mechanisms**; this entry makes **“mechanism qua mechanism”** explicit: agents can resolve `mechanism` as the id that describes **plugin conventions**, **standalone vs ensemble**, and **augment** files without conflating that with interchange or notation wire shapes.

## What’s distinctive

- **Delegate**: [`schema`](../../../SKILL.md) skill—full schemapedia protocol, families, checklist.
- **Normative rules**: [`plugin-convention.yml`](../../plugin-convention.yml).
- **Prototype**: [`templates/MECHANISM.yml`](../../../templates/MECHANISM.yml).

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [yaml-jazz](../yaml-jazz/README.md) | Profiles and augments are YAML; empathic comments bind instantiation. |
| [society-of-mind](../society-of-mind/README.md) | Parallel meta layer: registry plugins vs SoM architecture—not the same subject. |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Augment: [`SCHEMAPEDIA-MECHANISM-AUGMENT.yml`](./SCHEMAPEDIA-MECHANISM-AUGMENT.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
