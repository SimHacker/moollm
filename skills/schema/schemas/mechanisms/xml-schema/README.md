# W3C XML Schema (XSD) (schemapedia: `xml-schema`)

**Interchange family (XML).** W3C **XML Schema 1.0/1.1**—the default validation layer in SOAP stacks, many enterprise configs, and legacy XML worlds.

## Why it matters here

If a skill or integration must consume **XSD-described XML**, the schemapedia names the mechanism explicitly so you do not confuse it with [relax-ng](../relax-ng/README.md) or [json-schema](../json-schema/README.md). Versioning, imports, and ** xsi:type** complexity are policy questions—document them per project.

## What’s distinctive

- **Huge surface area**: types, substitution groups, keys/unique, facets—powerful and easy to misuse at scale.
- **Pervasive** where industries standardized on XSD (SOAP, HL7 artifacts in some profiles, etc.).
- **Trang** and RELAX NG: see [`../../gateways.yml`](../../gateways.yml) for bridge narratives; conversion is **often** possible, not universally lossless.
- **Schematron** ([schematron.com](https://schematron.com/), ISO 19757-3): **rule** validation with XPath—not a competing XSD alternative for element grammar; use with XSD (or RELAX NG) when you need assertion-style checks and rich error reporting beyond what the type system encodes.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [relax-ng](../relax-ng/README.md) | Alternative XML grammar; Trang bridges common subsets. |
| [json-schema](../json-schema/README.md) | XML vs JSON instance models—meet at boundaries (REST body vs SOAP envelope). |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| W3C | [XML Schema](https://www.w3.org/XML/Schema) |
| Overview | [Wikipedia: XML Schema](https://en.wikipedia.org/wiki/XML_Schema_(W3C)) |
| Tooling | `xmllint` with libxml2 (see [`MECHANISM.yml`](./MECHANISM.yml)) |
| Rules | [Schematron](https://schematron.com/) — XPath assertions on instances; complements XSD ([`../../formats.yml`](../../formats.yml) `xml` notes). |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
