# biomes/ — Data layer + example biome stubs

Parallel to [`schemas/`](../../schema/schemas/) in the sister skill. This directory serves two purposes:

1. **Shared grammar** — machine-readable convention and family taxonomy that every daughter biome inherits.
2. **Reference examples** — six stub biomes illustrating the distinct shapes a biome can take.

## Shared grammar

| File | Role |
|---|---|
| [`convention.yml`](convention.yml) | **Normative shape** — required core files, required subdirectories, family-specific subdirectories, inheritance declaration rules. Machine-checkable. |
| [`families.yml`](families.yml) | **Canonical taxonomy** — the families biomes belong to (cloud / edge / collaboration / meta / overlay / execution) with definitions and example members. |

(The `registry.yml` and `gateways.yml` files are **consumer-repo concerns**, not shipped here. Each repo that adopts this skill maintains its own.)

## Example biomes (stubs)

| Directory | Family | Emoji | Illustrates |
|---|---|---|---|
| [`gcp/`](gcp/) | cloud | ☁️ | Canonical cloud hyperscaler (GCP) |
| [`aws/`](aws/) | cloud | ☁️ | Cloud hyperscaler with distinct vocabulary (AWS) |
| [`azure/`](azure/) | cloud | ☁️ | Cloud hyperscaler with enterprise-IT flavor (Azure) |
| [`github/`](github/) | collaboration / cross-cutting | 🐙 | Forge + CI + social graph; touches every other biome |
| [`tailscale/`](tailscale/) | overlay / cross-cutting | 🕸️ | Mesh overlay that threads through every biome by design |
| [`cloudflare/`](cloudflare/) | overlay / multi-role | ☁️✈️ | CDN + Workers + R2 + DNS + Tunnels + Pages |

Each stub ships with the **minimal skeleton** — `GLANCE.yml`, `CARD.yml`, `README.md` — populated with CLI-tool-ecosystem docs and general-purpose vendor pointers. They are **vendor-neutral reference material**, not production biome knowledge. Private or site-specific knowledge lives in consumer repos (inheriting from these stubs via `inherits: [biome, biome.<name>]`).

**Cross-cutting biomes** — `github`, `tailscale`, and (partially) `cloudflare` are explicitly called out as *cross-cutting*: they don't just coexist with other biomes, they pass *through* every other biome. Every cloud/edge biome's gateways.yml tends to have many entries whose `kind:` points at one of these.

## How to read it

- **Want the convention?** [`convention.yml`](convention.yml) is the machine-readable shape rules.
- **Want the taxonomy?** [`families.yml`](families.yml) is the canonical family list.
- **Want to see a concrete biome?** Pick one of the six stubs — each is a 3-file minimal example.
- **Want to add a new biome in a consumer repo?** Read [`convention.yml`](convention.yml), copy [`../templates/BIOME/`](../templates/BIOME/) (or a stub closer to your target shape), declare `inherits: [biome]`, and register it in your consumer repo's `biomes/registry.yml`.

## Why split across multiple files

Schemapedia tried both monolithic and split. Split won because:

- Each file has a different lifecycle (convention changes rarely; families change very rarely; each biome stub evolves independently).
- Different audiences: convention is for biome authors, families for taxonomic decisions, individual stubs for people learning the pattern.
- Diffs are smaller and easier to review.
