# tailscale — Example Biome Stub (overlay family, CROSS-CUTTING)

🕸️ **Tailscale** — mesh network overlay biome shipped with `moollm/skills/biome/`.

Tailscale is **cross-cutting** — unlike cloud biomes, which are bounded regions, Tailscale's entire purpose is to pass THROUGH every other biome. A tailnet knits GCP VMs, AWS EC2 instances, Azure VMSS members, on-prem edge boxes, developer laptops, and CI runners into one private address space with one identity plane and one policy file (the ACL).

Same structural skeleton as any biome — but semantically, this biome IS the gateway. Many entries in your consumer repo's `biomes/gateways.yml` will have `kind: mesh_overlay` pointing here.

## Reading order

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What does tailscale add to the ecosystem?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — CLI, methods, gateway role" |

## Why tailscale is a first-class cross-cutting biome

Sister to `github` and (partially) `cloudflare`. What they have in common:

- **Every other biome consumes them.** A cloud VM boots and joins the tailnet. A forge's CI runner joins the tailnet to deploy. An edge box at a customer site joins the tailnet for remote access.
- **They are often the substance of gateway bridges**, not endpoints of them. "GCP ↔ edge-on-prem via tailscale" is a gateway whose `via:` is this biome.
- **When they fail, multiple biomes become unreachable.** Tailnet outage ≈ partial outage of every biome that depends on private-network reachability through it.

## Skeleton

| Directory | What goes there |
|---|---|
| `recipes/` | `tailscale up` patterns for CI / cloud VMs / edge boxes; Funnel/Serve patterns; ACL snippets |
| `instances/` | One subdir per tailnet (most orgs have one; larger orgs may have prod / staging / dev tailnets) — ACL file, subnet router map, tag taxonomy |
| `runbooks/` | Key rotation, ACL migration, adding a new subnet router, exit-node rollout |
| `gotchas/` | Magic DNS propagation delay, ACL shadow-deny debugging, NAT-behind-CGNAT issues, double-NAT with Docker, SSH cert expiry |
| `protocols/` | How Magic DNS works, how WireGuard session rekey affects long-lived flows, how DERP relays interact with direct connections |
| `scripts/` | Tailnet inventory dumps, ACL lint, auth-key rotation automation |
| `cost/` | Per-device / per-user licensing analysis (tailscale has a per-device pricing model) |

## Cross-biome relationships

Cross-cutting biomes' relationships are different in shape: every other biome lists tailscale as a gateway. A consumer repo's `biomes/gateways.yml` might look like:

```yaml
- id: cloud-to-edge-via-tailscale
  kind: mesh_overlay
  from: [gcp, aws, azure]
  to: edge-on-prem
  via: tailscale
  authoritative_policy: "instances/<tailnet-id>/acl.hujson"
```

## Not included

No tailnet names, no actual ACL content, no device IDs, no auth keys. Consumer repos populate those under `instances/<tailnet-id>/`.
