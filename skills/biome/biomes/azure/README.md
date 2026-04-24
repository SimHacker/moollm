# azure — Example Biome Stub (cloud family)

☁️ **Microsoft Azure** — stub reference biome shipped with `moollm/skills/biome/`.

Vendor-neutral reference for the Azure CLI tool ecosystem, key concepts, and biome skeleton. Consumer repos grow site-specific knowledge on top.

## Reading order

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What is this biome? What concepts?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — CLI tools, methods, sisters" |

## Skeleton

| Directory | What goes there |
|---|---|
| `recipes/` | `az` / `azcopy` / `func` / `kubectl` command patterns |
| `instances/` | Per-subscription state caches (one subdir per Azure subscription) |
| `runbooks/` | Task walkthroughs (new RG, VMSS rolling upgrade, Entra app creation) |
| `gotchas/` | Region pair quirks, VMSS capacity errors, Managed Identity propagation delays, SKU deprecations, ... |
| `protocols/` | Deep mechanism docs (RBAC evaluation, Managed Identity token flow, VMSS health probes) |
| `scripts/` | Azure-specific automation (subscription sweeps, quota probe) |
| `cost/` | Billing analyses (reservation planning, egress, AAD licensing) |
| `quota/` | Per-subscription quota inventory |
| `regions/` | Region / AZ / VM SKU availability (including the famously different availability of GPU SKUs per region) |

## How to adopt

**Fork**: `cp -r moollm/skills/biome/biomes/azure/ your-repo/skills/azure/`.

**Inherit**: `inherits: [biome, biome.azure]` in a consumer-repo skill — DOP lookup walks `your-skill → biome.azure → biome`.

## Cross-biome relationships

- **github** — Actions OIDC federates into Entra via federated credentials for passwordless deploys.
- **tailscale** — mesh overlay reaches Azure VMs on private-only networks without VPN gateway cost.
- **cloudflare** — public DNS + CDN + Tunnels; many teams run Cloudflare in front of Azure-hosted origins.
- **gcp / aws** — sister clouds; cross-cloud flows are gateway bridges.

## Not included

No tenant IDs, subscription names, resource IDs, or actual cost numbers.
