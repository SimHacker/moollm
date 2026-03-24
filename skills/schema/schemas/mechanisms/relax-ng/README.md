# RELAX NG (schemapedia: `relax-ng`)

**Interchange family (XML grammar).** Describe **classes of XML documents**—often more readable and composable than large W3C XSD graphs for authoring-centric workflows.

## Why it matters here

When MOOLLM or adjacent tools speak **XML** (configs, legacy enterprise formats, publishing pipelines), RELAX NG is a serious alternative to [xml-schema](../xml-schema/README.md). The registry records it so gateways ([`../../gateways.yml`](../../gateways.yml)) can name **Trang**-style translation and validator choices explicitly.

## What’s distinctive

- **Two syntaxes**: compact (`.rng` compact) and XML; same semantics.
- **Oasis of clarity** for many authors vs XSD’s sprawling feature set—tradeoff is ecosystem: some stacks are XSD-first.
- **Interops** with XSD via **Trang** (common path: RNG ↔ XSD for tooling compatibility).

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [xml-schema](../xml-schema/README.md) | Same problem domain (XML validity); translation via Trang and project policy—not drop-in equivalent. |
| [json-schema](../json-schema/README.md) | Different wire (XML vs JSON); meet at application boundaries. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Home | [relaxng.org](https://relaxng.org/) |
| Overview | [Wikipedia: RELAX NG](https://en.wikipedia.org/wiki/RELAX_NG) |
| Tooling | [Jing](https://relaxng.org/jclark/jing.html) (validation), [Trang](https://relaxng.org/jclark/trang.html) (RNG↔XSD) — see [`MECHANISM.yml`](./MECHANISM.yml) for `xmllint` / `trang` notes |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
