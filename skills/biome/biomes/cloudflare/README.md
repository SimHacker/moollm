# cloudflare — Example Biome Stub (overlay family, CROSS-CUTTING, multi-role)

☁️✈️ **Cloudflare** — edge-network platform biome shipped with `moollm/skills/biome/`.

Cloudflare is **cross-cutting** and **multi-role**. Unlike other biome stubs with one primary role (a cloud hyperscaler, a forge, a mesh), Cloudflare plays ten simultaneous roles that compose: DNS + CDN + WAF + Workers + R2 + D1/KV/DO + Queues + Tunnels + Pages + Access + Images/Stream + Email Routing.

## Reading order

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What is this biome? What roles does it play?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — CLI tools, methods, gateway role" |

## The multi-role lesson

Cloudflare is included as a biome stub to demonstrate that **a biome's boundary is logical, not functional**. A biome can contain many composable services, each of which would be a plausible biome on its own. The glue between them (shared auth, shared CLI tooling, shared account model, shared edge network) is what makes them one biome.

| Role | Service line |
|---|---|
| DNS + registrar | authoritative DNS for owned domains |
| CDN + WAF | public front door, caching, rate-limit, bot management |
| Edge compute | Workers (V8 isolates), Durable Objects (strongly consistent stateful workers) |
| Object storage | R2 (S3-compatible, zero egress) |
| Edge databases | D1 (SQLite), KV (edge KV store), Queues |
| Private ↔ public bridge | Tunnels (cloudflared) — reverse proxy into private origins |
| Identity plane | Access (ZTNA for SSH + internal web apps) |
| Static sites | Pages (static hosting + attached Workers) |
| Media | Images, Stream |
| Email | Email Routing (inbound email → Workers or forwards) |

## Cross-cutting pattern

Cloudflare often fronts the public traffic for biomes whose compute is on GCP / AWS / Azure. A request to `example.com` may traverse:

```
request → Cloudflare DNS → Cloudflare CDN+WAF → Cloudflare Worker (auth/rewrite) → GCP origin VM
```

That chain is entirely inside the cloudflare biome except for the last hop. The chain is a nested set of intra-biome gateways inside cloudflare plus one cross-biome gateway `cloudflare → gcp`.

## Skeleton

| Directory | What goes there |
|---|---|
| `recipes/` | wrangler / cloudflared / flarectl / terraform patterns |
| `instances/` | Per-account state caches (one subdir per Cloudflare account) — zones, Workers, R2 buckets, Tunnels, WAF rulesets, Access policies |
| `runbooks/` | New zone onboarding, Worker deploy rollback, Tunnel setup, Access policy migration |
| `gotchas/` | Proxied-vs-DNS-only gotchas, Worker CPU limits, R2 region semantics, Tunnel race conditions, WAF false positives |
| `protocols/` | How Workers interact with R2/D1/KV, Tunnel architecture, Access SSO flow |
| `scripts/` | Account sweeps, DNS audits, Tunnel inventory, Access policy export |
| `cost/` | R2 economics, Worker invocation pricing, bandwidth analyses, Tunnel free-tier limits |

## Cross-biome relationships

Cloudflare frequently appears as the `from:` of cross-biome gateways:

```yaml
- { kind: cdn_front,      from: cloudflare, to: gcp,   via: proxied-dns }
- { kind: cdn_front,      from: cloudflare, to: aws,   via: proxied-dns }
- { kind: private_tunnel, from: public,     to: gcp-private-vm, via: cloudflared-tunnel }
- { kind: ztna_access,    from: users,      to: internal-ssh,   via: cloudflare-access }
```

Overlap with Tailscale: `Cloudflare Tunnel` and `Tailscale Funnel` solve overlapping problems (reaching a private origin from the public internet). Document where your consumer repo prefers one over the other.

## Not included

No zone names, actual Workers code, R2 bucket names, Tunnel IDs, or Access policy content. Consumer repos populate those under `instances/<account-id>/`.
