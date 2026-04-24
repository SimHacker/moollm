---
name: biome
description: "Mother skill for platform-descriptor sister skills. Defines what a BIOME is — a bounded region of an ecosystem (coexisting, exchanging, never isolated) for one platform you operate — and what files, subdirectories, and cross-biome bridges every daughter biome inherits."
license: MIT
tier: 1
inherits:
  - skill                # biome IS a kind of MOOLLM skill (meta-skill family)
  - prototype            # uses Self / DOP delegation for daughter biomes
pattern_lineage:
  - schema               # registry + gateways + convention triad lifted from schemapedia
  - card                 # sniffable-interface pattern this skill itself uses
  - file-system-object   # the grammar daughters use (UPPERCASE marker files = interface exports)
allowed-tools:
  - read_file
  - write_file
  - terminal
  - grep
related: [skill, schema, prototype, card, yaml-jazz, file-system-object, sister-script]
tags: [biome, meta, mother, prototype, platform-descriptor, schemapedia, ecology, microworld]
credits: "MOOLLM — lifted from three sister biomes that accreted independently in a consumer repo (leela-ai/central: edgebox, gcs, azure) then congealed into a publishable meta-skill pattern, 2026-04"
---

# BIOME — Mother Skill for Platform Descriptors

> **BIOME** *n.* — a bounded region of an ecosystem, with its own inhabitants and climate, **coexisting** with sister biomes and **exchanging** matter, energy, and information with them along defined gateways.

This skill is the **mother prototype** that platform-descriptor sister skills inherit from. Each daughter biome declares `inherits: biome` in its CARD.yml / GLANCE.yml / SKILL.md frontmatter, and its directory structure mirrors the skeleton this skill defines.

**Six example biomes ship with this skill** for reference, each illustrating a distinct dimension:

| Biome | Family | What it exemplifies |
|---|---|---|
| [`biomes/gcp/`](biomes/gcp/) | cloud | Canonical cloud hyperscaler |
| [`biomes/aws/`](biomes/aws/) | cloud | Another hyperscaler with distinct vocabulary (accounts, regions, AZs, SSO) |
| [`biomes/azure/`](biomes/azure/) | cloud | A third hyperscaler with enterprise-IT flavor (subscriptions, RGs, Managed Identities) |
| [`biomes/github/`](biomes/github/) | collaboration | **Cross-cutting** — forge + CI + social graph + MMPORG + branch-as-object database; touches every other biome |
| [`biomes/tailscale/`](biomes/tailscale/) | overlay | **Cross-cutting** — mesh network that threads through every other biome by design |
| [`biomes/cloudflare/`](biomes/cloudflare/) | overlay | **Multi-role** — CDN + Workers + R2 + DNS + Tunnels + Pages; the "many simultaneous roles" lesson |

Consumer repos adopt this skill and populate their own `biomes/registry.yml` + `biomes/gateways.yml` + per-biome daughter skills in their own repos. The example biomes here are vendor-neutral reference material, not a working registry.

## Why "biome" — not "microworld," "virtual world," or "platform"

The name is deliberate. The ecological framing does three things no other candidate does:

- **Microworld** (Papert's term, MOOLLM's ambient usage) implies an *isolated* space — a pedagogical sandbox sealed against distraction. A MOOLLM microworld is single-subject by design. Biomes are explicitly **not isolated** — inhabitants cross boundaries; a cloud MIG pulls images from the github biome; an edge box pulls models from a cloud biome; tailscale threads SSH through all of them at once. Isolation is the wrong shape.
- **Macroworld / virtual world** implies *simulation* or *containment*. Biomes are **real operational territory** — they aren't modeled, they're inhabited. Machines run there, bills come from there, outages happen there.
- **Platform** is accurate but flat. "Platform" hides that there's weather, seasons, predators, migrations — that things live in these places, have needs, interact. The platform-language invites thinking of GCP and Azure as interchangeable slots. The biome-language makes it obvious that the Amazon is not the Sahara is not a coral reef, even if they all "have climate and elevation."

The ecology metaphor earns its keep when you start looking at cross-biome flows:

- **Exchange** — containers built in github, consumed by cloud VMs; videos produced at edge boxes, flowing up to cloud buckets; models trained somewhere, distributed everywhere.
- **Symbiosis** — tailscale overlays every biome without owning any of them; a devops meta-biome serves images to every biome and exists for no other purpose.
- **Migration** — workloads move (GPU SKU upgrades; cross-cloud parity rollouts).
- **Climate** — each biome has its own rate constants: cloud MIG autoscaler cooldowns, edge spot preemption rates, CI runner queue times.
- **Niches** — each biome supports workloads the others can't (or won't): edge runs local because it has to, cloud runs pay-per-use because it can, forges run CI because they already have the code.

All of these are captured structurally by the skeleton (recipes/instances/runbooks/gotchas/...) and by the consumer repo's `biomes/gateways.yml`, which is the explicit record of cross-biome exchange. **Gateways are not a metadata afterthought — they're the biological substance of the ecosystem.**

> **Structural ancestry.** This pattern is directly modeled on MOOLLM's [`schema` skill (schemapedia)](../schema/). Schemapedia maintains a registry of schema mechanisms (json-schema, sqlite, git, drescher, …) with [`registry.yml`](../schema/schemas/registry.yml) + [`plugin-convention.yml`](../schema/schemas/plugin-convention.yml) + [`gateways.yml`](../schema/schemas/gateways.yml). The biome pattern applies the same idea one level up — each biome is a **full sister skill** rather than a plugin entry inside a single skill, but the registry / convention / gateways triad is deliberately parallel. See [`biomes/convention.yml`](biomes/convention.yml) and [`biomes/families.yml`](biomes/families.yml).

## Inheritance, the Self way

Each daughter biome is an **instance** of the biome prototype:

```yaml
# In skills/gcs/CARD.yml (and GLANCE.yml)
inherits:
  - biome
```

When a daughter biome doesn't define a convention locally, the answer lives here — first-match-wins delegation per MOOLLM's [Delegation Object Protocol (DOP)](../skill/delegation-object-protocol.md). When you land in a daughter biome and the question is "what does this skeleton mean?", consult this skill.

## Why a shared skeleton

- **Predictable navigation.** Once you know where to find gotchas in one biome, you know where to find them in any biome.
- **Low-friction expansion.** New biomes (runner, tailscale, future platforms) grow into the skeleton instead of inventing their own.
- **Cross-biome learning.** Lessons from one biome (e.g., "GCP has invisible quota for new accelerator families") find their parallels in another (e.g., "Azure has 0-default quota for new VM families") because both live at the same path.
- **MOOLLM alignment.** Each biome is a microworld — a bounded, coherent space where platform-specific vocabulary and patterns make sense. The skeleton is the shared grammar.

## What makes a biome

A MOOLLM-compatible platform biome is a directory under `skills/` that describes **one operational platform** — a place where you run workloads (cloud VMs, on-prem hardware, CI runners), a registry or image source (Artifact Registry, Docker Hub, a private package index), an identity or network plane you depend on (Tailscale, Cloudflare, Firebase), or any other bounded infrastructure surface whose specific vocabulary and quirks are worth capturing.

Not every skill is a biome. A biome is specifically a **platform descriptor** — it encodes operational knowledge of a bounded infrastructure surface. Non-biome skills include process skills, workload skills, and meta-skills (e.g., `skill`, `card`, `cauldron`, `schema`, `file-system-object`). A biome declares membership by inheriting from this skill.

## Core files (required — the Semantic Image Pyramid)

Every biome must declare these:

| File | Purpose | Typical size |
|---|---|---|
| `GLANCE.yml` | Quick scan: what, why, when, methods, key gotchas, key files, sister skills, **`inherits: biome`** | 50-100 lines |
| `CARD.yml` | Sniffable interface: activation k-lines, advertisements, methods, state, files index, navigation, **`inherits: [biome]`** | 150-300 lines |
| `SKILL.md` | Protocol overview, core mental model, worked examples, documentation map | 300-500 lines |
| `README.md` | Human landing page with reading order and quick links | 50-80 lines |

## Core subdirectories (standard skeleton)

Every biome should have these directories, even if initially populated only by a `README.md` stub. They fill in over time as we learn.

| Directory | Contents | Reading convention |
|---|---|---|
| `recipes/` | Ready-to-run commands and short patterns. Markdown files organized by task theme. The "bash snippet you Google for at 2am" section. | `recipes/<topic>.md`; plus `recipes/README.md` as index |
| `instances/` | Per-deployment knowledge cache. One subdir per deployed instance (project, subscription, on-prem box). Contains `state.yml`, `history.md`, per-instance `deploy.md` where useful. | `instances/<name>/README.md` |
| `runbooks/` | Task-oriented walkthroughs. Each runbook covers one multi-step operation end-to-end. | `runbooks/<UPPERCASE-TASK>.md` |
| `gotchas/` | Known failure modes, one per file. Each includes the symptom, the root cause, and the fix. The archive of "this took a deploy cycle to figure out." | `gotchas/<kebab-case-symptom>.md` |
| `protocols/` | Deep documentation of mechanisms and invariants. Longer-form than recipes, more stable than gotchas. | `protocols/<topic>.md` |
| `scripts/` | Automation hooks specific to this biome (probes, diagnostic wrappers). Not user-facing CLIs (those live in `tools/`). | `scripts/<name>.sh` |
| `cost/` | Date-stamped billing analyses. Each file captures a specific finding with the queries, raw numbers, interpretation, and action. | `cost/YYYY-MM-DD-topic.md` |

## Cloud-biome-specific subdirectories

For biomes whose platform is a public cloud (`gcs`, `azure`, future `aws`):

| Directory | Contents |
|---|---|
| `quota/` | Quota inventory per region/family. What we have, what we've requested, what's blocking. |
| `regions/` | Region/zone/SKU availability catalogs. "Where does our fleet run, and why." |

## Edge-biome-specific subdirectories

For `edgebox` (and any future terrestrial biomes like `customer-hardware`):

| Directory | Contents |
|---|---|
| `stacks/` | Stack types (vision, builder, training). A biome-specific concept — an edgebox can be deployed as different stack shapes; a GCS project can't. |
| `templates/` | Template files for new instances. |

## CLI tool ecosystem (optional but encouraged)

Every biome operates through a set of command-line tools — `gcloud` for GCP, `az` for Azure, `aws` for AWS, `ssh`/`docker`/`systemctl` for edge/on-prem, `gh`/`git` for forges, `tailscale` for mesh network, `wrangler`/`flarectl` for Cloudflare. The biome's CARD.yml should list them in a `cli_tools:` block so newcomers (and LLMs) can tell at a glance "which binary do I invoke for which concern."

Minimal shape (see [`biomes/convention.yml`](biomes/convention.yml) for the full spec):

```yaml
cli_tools:
  - name: gcloud
    role: "GCP CLI for compute, secrets, IAM, pubsub, etc."
    install: "brew install --cask google-cloud-sdk"
    auth: "gcloud auth login --no-launch-browser"
    primary_usage: "recipes/gcloud-patterns.md"
    vendor_docs: https://cloud.google.com/sdk/gcloud

  - name: gsutil
    role: "GCS object storage CLI (bucket listings, cp/mv, lifecycle)"
    primary_usage: "bucket reads/writes, syncing artifacts"
    also_used_by: [edge-on-prem]    # shared CLI → record as a gateway
```

Tools used across multiple biomes (`docker`, `git`, `ssh`, `gsutil`, `tailscale`) should be listed in every biome that uses them AND get a corresponding bridge entry in the consumer repo's `biomes/gateways.yml` with `kind: shared_cli_tool`.

## Optional / grows-as-needed

| Directory | When |
|---|---|
| `examples/` | Free-form examples not fitting into recipes/runbooks. |
| `benchmarks/` | Performance data captured over time. |
| `designs/` | Design intent docs specific to this biome. |
| `snapshots/` | Point-in-time captures (state exports, probe output). |

## The skeleton, visualized

```
skills/<biome>/
├── GLANCE.yml                 # 👁️  required (Semantic Image Pyramid)
├── CARD.yml                   # 📇  required, declares  inherits: [biome]
├── SKILL.md                   # 📜  required, declares  inherits: [biome] in frontmatter
├── README.md                  # 📚  required
│
├── recipes/                   # Ready-to-run commands
│   └── README.md              # index
│
├── instances/                 # Per-deployment knowledge
│   └── README.md
│
├── runbooks/                  # End-to-end walkthroughs
│   └── README.md
│
├── gotchas/                   # Known failure modes
│   └── README.md
│
├── protocols/                 # Deep documentation
│   └── README.md
│
├── scripts/                   # Biome-specific automation
│   └── README.md
│
├── cost/                      # Date-stamped billing analyses
│   └── README.md
│
├── quota/                     # Cloud biomes only
│   └── README.md
│
├── regions/                   # Cloud biomes only
│   └── README.md
│
└── stacks/                    # Edge biomes only
    └── README.md
```

Use [`templates/BIOME/`](templates/BIOME/) as the directory scaffold to instantiate from when adding a new biome.

## When to promote content into the skeleton

Content lives in one of three places:

1. **SKILL.md** — the canonical overview, everything cross-referenced.
2. **Subdirectory file** — when a topic grows beyond 1-2 paragraphs in SKILL.md, or when it has its own lifecycle (date-stamped cost analyses, per-instance state, gotchas with distinct identity).
3. **External doc** (under a repo-level `docs/` path or a sibling skill) — when the topic spans multiple biomes or is cross-cutting (e.g., a `cloud-gpu-platforms.md` that catalogs GCP + Azure + AWS GPU SKUs side-by-side).

The skeleton establishes where things *can* live. Movement is lazy: keep it in SKILL.md until it earns its own file by being longer than a paragraph or having an independent lifecycle.

## Example biomes shipped with this skill

| Biome | Family | Emoji | What it illustrates |
|---|---|---|---|
| [`biomes/gcp/`](biomes/gcp/) | cloud | ☁️ | Canonical cloud hyperscaler; recipes/regions/quota/cost shapes |
| [`biomes/aws/`](biomes/aws/) | cloud | ☁️ | Hyperscaler with distinct vocabulary (accounts, AZs, IAM, SSO) |
| [`biomes/azure/`](biomes/azure/) | cloud | ☁️ | Hyperscaler with enterprise-IT flavor (subscriptions, RGs, MI) |
| [`biomes/github/`](biomes/github/) | collaboration / cross-cutting | 🐙 | Forge + CI + social graph + branch-as-object store; touches every other biome |
| [`biomes/tailscale/`](biomes/tailscale/) | overlay / cross-cutting | 🕸️ | Mesh overlay that threads through every biome by design |
| [`biomes/cloudflare/`](biomes/cloudflare/) | overlay / multi-role | ☁️✈️ | CDN + Workers + R2 + DNS + Tunnels + Pages; one brand, many roles |

Each of these is a **stub** with the minimal skeleton (`GLANCE.yml`, `CARD.yml`, `README.md`, and a seed `README.md` per required subdirectory). Consumer repos are expected to either:

- (a) fork the stub into their own `skills/<biome>/` and grow it with site-specific recipes/instances/gotchas, declaring `inherits: biome`; or
- (b) leave the stub as-is in `moollm/` and write a thin consumer-side overlay skill that inherits from it (same `inherits: biome` chain, plus `inherits: biome.<biome-name>` for delegation into the stub's CLI tool list / vendor doc links).

## Candidate future example biomes

Platforms common enough to deserve a reference stub when someone authors one:

| Candidate | Nature | Why it matters |
|---|---|---|
| `firebase` | Auth / realtime DB / hosting | Multi-role like Cloudflare; auth plane crosses every biome that consumes identity |
| `postgres` | Database | Spans managed (RDS/Cloud SQL/Azure DB) + self-hosted; worth documenting both |
| `bigquery` | Data analytics | Cloud data-warehouse shape; sister to Snowflake/Redshift |
| `kubernetes` | Orchestrator-as-platform | When consumer fleets include k8s; distinct enough to deserve its own biome |
| `terraform` | IaC | Cross-cutting like github — every biome consumes it |
| `1password` / `vault` | Secrets plane | Identity-adjacent overlay biomes |

New example biomes become worth shipping when they illustrate a **distinct biome shape** (new family, new cross-cutting pattern, new failure-mode cluster) — not just another cloud vendor.

## Parallel to schemapedia — which files do what

Schemapedia and biome-pedia both split responsibility across a registry / convention / gateways triad. Side-by-side:

| Concept | Schemapedia (`skills/schema/`) | Biome (this skill, `skills/biome/`) |
|---|---|---|
| **Convention** | [`schemas/plugin-convention.yml`](../schema/schemas/plugin-convention.yml) | [`biomes/convention.yml`](biomes/convention.yml) (machine-readable) + this `SKILL.md` (prose) |
| **Registry** | [`schemas/registry.yml`](../schema/schemas/registry.yml) | Consumer repo's `biomes/registry.yml` (this skill ships example biomes, not a working registry) |
| **Gateways** | [`schemas/gateways.yml`](../schema/schemas/gateways.yml) | Consumer repo's `biomes/gateways.yml` |
| **Families** | interchange, causal, relational, … | cloud, edge, meta, overlay, collaboration (see [`biomes/families.yml`](biomes/families.yml)) |
| **Member profile** | `schemas/mechanisms/<id>/MECHANISM.yml` + `README.md` | `skills/<biome>/` directory (full sister skill, with own SKILL.md / CARD.yml / GLANCE.yml — declares `inherits: biome`) |
| **Template** | `templates/MECHANISM.yml` | [`templates/BIOME/`](templates/BIOME/) directory scaffold |
| **Augment** (optional extensions) | `SCHEMAPEDIA-<ID>-AUGMENT.yml` next to each profile | Each biome's subdirectories (`recipes/`, `runbooks/`, `gotchas/`, …) are native MOOLLM augmentations, indexed via the biome's own `CARD.yml` |

Key structural difference: schemapedia members are small plugin entries that fit inside one skill directory; biome members are full skills with their own sub-skeletons and Self-style inheritance. The registry is correspondingly thinner (it points at sibling skill directories), and each biome carries significantly more internal structure than a `MECHANISM.yml` does. But the *role* of each file is the same.

## Relationship to MOOLLM

Each biome is a **microworld** in Seymour Papert / MOOLLM sense — a bounded space with its own coherent vocabulary and rules, where learning the rules of one biome doesn't require learning the rules of any other. The shared skeleton is the **grammar** that spans microworlds: you can learn the grammar once and read any biome fluently. The skeleton gives you sisterhood across microworlds without collapsing them into one undifferentiated vendor-neutral mush.

MOOLLM concepts this skill embodies:

- **Skills as prototypes (Self / DOP)** — `biome` is a prototype; `gcp`, `azure`, `aws`, `github`, `tailscale`, `cloudflare` are instances declaring `inherits: biome`. When a daughter doesn't define a convention, lookup falls back to this skill.
- **Semantic Image Pyramid** (GLANCE → CARD → SKILL → README) — multi-resolution reading, applied recursively (this skill itself follows it; each daughter follows it).
- **Prototypes and instances** — the daughter biome is itself a prototype for ITS instances (e.g., `gcp/instances/<project-id>/`).
- **File System as Object** — plural directory names declare element types; UPPERCASE marker files declare interface exports. See [`file-system-object`](../file-system-object/).
- **K-lines as filenames** — directory and file names are activation handles.
- **PLAY-LEARN-LIFT** — content starts in chat/SKILL.md (play), gets documented (learn), gets promoted into the skeleton with cross-references (lift). This skill itself is a LIFT from three concrete biomes that accreted independently in a consumer repo before the pattern became visible.
- **Sister scripts** — code stays generic across biomes, values vary (e.g., `<TYPE>_VM_*` secret keys are sister keys; same shape, cloud-appropriate contents).

## How to add a new biome

1. **Decide it's a biome.** A biome is a platform descriptor — a place you operate, not a process or workload skill. If unsure, list it under `candidates:` in your consumer repo's `biomes/registry.yml` instead of starting a directory.
2. **Pick a name + family.** Family is one of `cloud`, `edge`, `meta`, `overlay`, `collaboration`, `execution`. See [`biomes/families.yml`](biomes/families.yml).
3. **Instantiate the template.**
   ```bash
   cp -r moollm/skills/biome/templates/BIOME/ skills/<new-biome>/
   ```
   Fill in the placeholders (name, description, family, character). You may also start from one of the example biomes shipped here (copy `biomes/gcp/` as the cloud shape, `biomes/github/` as the cross-cutting shape, etc.) and edit.
4. **Declare inheritance.** Each of `<new-biome>/CARD.yml`, `<new-biome>/GLANCE.yml`, and `<new-biome>/SKILL.md` (frontmatter) gets `inherits: [biome]`. This makes the prototype chain explicit and machine-detectable. If inheriting from an example biome here, also add `inherits: [biome, biome.<example-name>]` so delegation walks into the stub first before falling back to the mother.
5. **Register (in your consumer repo).** Add an entry to your `biomes/registry.yml` under the right family.
6. **Cross-biome bridges.** If the new biome shares machinery with existing biomes (secret naming, shared scripts, image distribution, mesh networking, DNS ownership, …), add bridge entries to your `biomes/gateways.yml`.
7. **Grow.** Stub README.md in each subdirectory; populate as operational knowledge accumulates. Promote content out of `<new-biome>/SKILL.md` into the appropriate subdirectory when it grows beyond 1-2 paragraphs or has its own lifecycle.

## How to grow a biome (general operating loop)

1. **New operational finding?** Put it in `<biome>/SKILL.md` first.
2. **Finding grows beyond a paragraph or is one of a series?** Promote to the right subdirectory with a dedicated file. Add a line to the subdirectory's `README.md` index.
3. **Finding applies across biomes?** Extract to a repo-level doc or a sibling skill; have each biome's SKILL.md link to it. Add a bridge entry in your `biomes/gateways.yml`.
4. **Subdirectory is empty because you haven't hit that kind of thing yet?** Leave the `README.md` stub. It's a signpost to your future self about what you'd eventually want to capture there.

## Cross-cutting biomes (the github / tailscale / cloudflare pattern)

Some biomes are **cross-cutting by design** — they don't just coexist with other biomes, they pass *through* every other biome:

- **`github`** — every cloud biome pulls deploy artifacts from GitHub Actions; every edge biome is reached via `git pull`; every infrastructure change is audited there. The forge IS the circulatory system.
- **`tailscale`** — every SSH session, every private-service probe, every cross-region debug traverses the mesh. Tailscale overlays all biomes without *owning* any of them.
- **`cloudflare`** — DNS for every biome's public-facing name, CDN in front of web biomes, Workers/R2 as compute+storage, Tunnels reaching back into private biomes. Multi-role by design.
- **Secrets plane** (e.g., `1password`, `vault`) — same pattern; would deserve its own cross-cutting biome stub when captured.

Cross-cutting biomes are structurally **the same shape** as bounded ones (same skeleton, same required files) but semantically **the substance of the gateways themselves**. When you write `biomes/gateways.yml` in a consumer repo, many bridges will *be* the cross-cutting biome — e.g., "edge ↔ cloud via tailscale" is a gateway entry whose `kind: mesh_overlay` points at the tailscale biome.

## Related

- [`skill`](../skill/) — the meta-skill for creating skills
- [`schema`](../schema/) — schemapedia, the structural ancestor of this pattern
- [`prototype`](../prototype/) — Self-style prototype delegation
- [`card`](../card/) — sniffable-interface skill
- [`file-system-object`](../file-system-object/) — the grammar daughters use (UPPERCASE marker files = interface exports)
- [`yaml-jazz`](../yaml-jazz/) — semantic YAML used in convention/registry/gateways files
- [`sister-script`](../sister-script/) — the cross-biome scripting pattern that lets one script serve every biome

## Publication

This skill is **Tier 1** (MOOLLM core). It is published as part of the MOOLLM distribution and is freely reusable under MIT. Consumer repos adopt it by declaring `inherits: biome` in their platform-descriptor skills and populating their own `biomes/registry.yml` + `biomes/gateways.yml`.

Origin: this skill was synthesized from three sister biomes (`edgebox`, `gcs`, `azure`) that accreted independently in a consumer infrastructure repo (leela-ai/central), until the shared shape became obvious enough to extract. The PLAY-LEARN-LIFT arc — three concrete biomes → meta-skill — is the archetypal MOOLLM lift.
