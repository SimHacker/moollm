# aws — Example Biome Stub (cloud family)

☁️ **Amazon Web Services** — stub reference biome shipped with `moollm/skills/biome/`.

Vendor-neutral reference for the AWS CLI tool ecosystem, key concepts, and biome skeleton. Consumer repos grow site-specific knowledge on top.

## Reading order

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What is this biome? What concepts?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — CLI tools, methods, sisters" |

## Skeleton

Every required subdirectory has a README.md stub describing what goes there. Consumer repos populate them.

| Directory | What goes there |
|---|---|
| `recipes/` | aws / eksctl / sam / cdk command patterns |
| `instances/` | Per-account state caches (one subdir per AWS account you operate) |
| `runbooks/` | Task walkthroughs (new region, new VPC, IAM emergency rotation) |
| `gotchas/` | AZ-scoped outages, IAM eventual consistency, NAT GW cost traps, spot interruption, ... |
| `protocols/` | Deep mechanism docs (IAM evaluation logic, VPC routing, S3 request pricing) |
| `scripts/` | AWS-specific automation (account sweeps, quota probe, reserved-instance planner) |
| `cost/` | Billing analyses (reserved vs on-demand, egress per region, service split) |
| `quota/` | Per-region service-quota inventory (especially EC2 instance-family vCPU limits) |
| `regions/` | Region/AZ/instance-family availability |

## How to adopt

**Fork**: `cp -r moollm/skills/biome/biomes/aws/ your-repo/skills/aws/` and populate.

**Inherit**: declare `inherits: [biome, biome.aws]` in your consumer-repo's AWS skill — DOP lookup delegates to this stub for CLI tool docs and concept glossary.

## Cross-biome relationships

- **github** — GitHub Actions OIDC federates into AWS IAM roles for deploys.
- **tailscale** — mesh overlay reaches EC2 private IPs without SG/VPN rules; often preferred over SSM for interactive sessions.
- **cloudflare** — public DNS + CDN + Tunnels for AWS-backed origins.
- **gcp / azure** — sister clouds; cross-cloud flows are gateway bridges.

## Not included

No account IDs, no actual cost numbers, no site-specific runbooks. Those live in consumer repos.
