# biome — Mother Skill for Platform Descriptors

> 🌱 The mother prototype that platform-descriptor sister skills inherit from. Every daughter biome declares `inherits: biome` in its CARD.yml, GLANCE.yml, and SKILL.md frontmatter.

A **biome** is a bounded region of an operational ecosystem — one platform you operate (a cloud, an edge fleet, a forge, a mesh network) — **coexisting with sister biomes** and **exchanging matter, energy, and information** with them along defined gateways. Cloud ≠ edge ≠ forge ≠ overlay; but workloads, artifacts, secrets, and humans flow between them constantly.

## Reading order (Semantic Image Pyramid)

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What does this skill do? What inherits from it?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — methods, advertisements, example daughters" |
| 📜 **SKILL** | [SKILL.md](SKILL.md) | "Full protocol: skeleton, conventions, parallel to schemapedia, cross-cutting biomes" |

## Data layer (shared grammar)

| File | Purpose | Schemapedia parallel |
|---|---|---|
| [biomes/convention.yml](biomes/convention.yml) | Machine-readable shape rules for what a daughter biome must contain | `schemas/plugin-convention.yml` |
| [biomes/families.yml](biomes/families.yml) | Canonical taxonomy (cloud / edge / meta / overlay / collaboration / execution) | (families embedded in schemapedia registry) |
| [biomes/README.md](biomes/README.md) | Index of example biomes shipped with this skill | — |

The **registry** and **gateways** files are consumer-repo concerns — each repo that adopts this skill maintains its own `biomes/registry.yml` (which biomes are in play, at what status) and `biomes/gateways.yml` (cross-biome bridges). The mother skill defines the *shape*; the consumer supplies the *contents*.

## Templates

[`templates/BIOME/`](templates/BIOME/) — directory scaffold to copy when adding a new daughter biome. After cloning, fill in the placeholders and add `inherits: biome` to CARD.yml + GLANCE.yml + SKILL.md.

## Example biomes shipped with this skill

Six reference stubs, each illustrating a distinct biome shape:

| Biome | Family | Emoji | What it exemplifies |
|---|---|---|---|
| [biomes/gcp/](biomes/gcp/) | cloud | ☁️ | Canonical cloud hyperscaler (GCP) |
| [biomes/aws/](biomes/aws/) | cloud | ☁️ | Cloud hyperscaler with distinct vocabulary (accounts, AZs, SSO) |
| [biomes/azure/](biomes/azure/) | cloud | ☁️ | Cloud hyperscaler with enterprise-IT flavor (subscriptions, RGs, MI) |
| [biomes/github/](biomes/github/) | collaboration / cross-cutting | 🐙 | Forge + CI + social graph + branch-as-object; touches every other biome |
| [biomes/tailscale/](biomes/tailscale/) | overlay / cross-cutting | 🕸️ | Mesh overlay that threads through every biome by design |
| [biomes/cloudflare/](biomes/cloudflare/) | overlay / multi-role | ☁️✈️ | CDN + Workers + R2 + DNS + Tunnels + Pages; one brand, many roles |

Two of these (**github** and **tailscale**) are explicitly called out as **cross-cutting biomes** — they don't just coexist with the others, they pass *through* every other biome. See SKILL.md §"Cross-cutting biomes" for the pattern.

## Pattern lineage

This skill is patterned after [`schema`](../schema/) (schemapedia) and inherits from [`skill`](../skill/) (the meta-skill) + [`prototype`](../prototype/) (Self-style delegation). The registry/convention/gateways triad is deliberately parallel to schemapedia's.

## Origin

This skill was lifted from three sister biomes (`edgebox`, `gcs`, `azure`) that accreted independently in a consumer infrastructure repo until the shared shape became obvious enough to extract into a MOOLLM meta-skill. The PLAY-LEARN-LIFT arc — three concrete biomes → extracted pattern → publishable meta-skill — is the archetypal MOOLLM lift.

## Part of MOOLLM

This skill is part of [MOOLLM](../../) (Microworld Object-Oriented Large-Language Models), an ecosystem of composable skills for LLM-native software. See [`skills/README.md`](../README.md) for the skill index.
