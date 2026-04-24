# gcp — Example Biome Stub (cloud family)

☁️ **Google Cloud Platform** — stub reference biome shipped with `moollm/skills/biome/`.

This is a **vendor-neutral reference biome**. It documents the GCP CLI tool ecosystem, key concepts, and skeleton. It does **not** contain site-specific knowledge (per-project state, actual cost analyses, real gotchas you hit in production). Consumer repos grow that material on top of this stub.

## Reading order

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What is this biome? What concepts?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — CLI tools, methods, sisters" |

## Skeleton (empty, ready to fill)

Every directory has a README.md stub indicating what goes there. Consumer repos fill these in with real content.

| Directory | What goes there |
|---|---|
| `recipes/` | Ready-to-run gcloud/gsutil/bq command patterns |
| `instances/` | Per-project state caches (one subdir per GCP project you operate) |
| `runbooks/` | Task-oriented walkthroughs (e.g., "create a new GPU MIG region") |
| `gotchas/` | Known failure modes (quota opacity, zone stockouts, driver mismatches, ...) |
| `protocols/` | Deep mechanism docs (IAM semantics, MIG autoscaler math, quota inheritance) |
| `scripts/` | GCP-specific automation (probe capacity, dump quota, etc.) |
| `cost/` | Date-stamped billing analyses |
| `quota/` | Per-region quota inventory |
| `regions/` | Region/zone/SKU availability catalogs |

## How to adopt this stub in a consumer repo

Two patterns:

### Option A: fork into your own skill

```bash
cp -r moollm/skills/biome/biomes/gcp/ your-repo/skills/gcp/
```

Then edit `your-repo/skills/gcp/CARD.yml` to declare `inherits: [biome]` (the stub's CARD already declares this), remove the `status: stub` marker, and start populating the subdirectories.

### Option B: inherit via delegation

Create `your-repo/skills/my-gcp/` with CARD.yml:

```yaml
inherits:
  - biome                # mother prototype
  - biome.gcp            # this stub (delegates to CLI tool docs, concept glossary, etc.)
```

DOP lookup will walk `my-gcp → biome.gcp → biome` for any field not defined locally. You get the vendor-neutral CLI tool docs for free, and your consumer repo's skill only carries the delta (site-specific recipes, real instances, real gotchas).

## Cross-biome relationships

- **github** — deploy pipelines dispatch from GitHub Actions via Workload Identity Federation.
- **tailscale** — mesh overlay lets operators SSH to GCE VMs on RFC1918 addresses without public IPs.
- **cloudflare** — often the public DNS + CDN in front of GCP-hosted origins; Cloudflare Tunnels can also bridge back.
- **aws / azure** — sister cloud biomes. Cross-cloud flows (e.g., GCS → S3 replication) are gateway bridges in the consumer repo's `biomes/gateways.yml`.

## Not included on purpose

- Real project names, billing account IDs, resource IDs.
- Actual quota numbers (they're per-account).
- Site-specific recipes (these are consumer-repo concerns).
- Anything proprietary to any organization.
