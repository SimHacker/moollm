# github — Example Biome Stub (collaboration family, CROSS-CUTTING)

🐙 **GitHub** — forge + CI + social graph + MMPORG + branch-as-object store biome shipped with `moollm/skills/biome/`.

GitHub is **cross-cutting** — every other biome (cloud, edge, overlay) consumes it in some way. Gateway entries in consumer repos' `biomes/gateways.yml` frequently bridge to/from here.

## Reading order

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What does github add to the ecosystem?" |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "Sniffable interface — CLI, methods, gateway role, branch-as-object" |

## Why github is a first-class cross-cutting biome

Sister to `tailscale` and (partially) `cloudflare`. What they have in common:

- **Every other biome consumes them.** Cloud biomes receive deploy dispatches; edge biomes pull config; overlay biomes federate auth.
- **They are the substance of gateway bridges.** "Actions → GCP deploy via OIDC" is a gateway whose `via:` is this biome.
- **When they fail, multiple biomes degrade.** GitHub outage means no deploys anywhere, no new code landing, no CI validation.

## GitHub is more than a code host

GitHub actually provides all of these in one surface:

| Role | Surface |
|---|---|
| FORGE | repos, branches, tags, LFS |
| REVIEW | PRs, reviews, CODEOWNERS, required-review policy |
| CI/CD | Actions, workflows, runners, environments |
| SOCIAL GRAPH | stars, follows, orgs, teams; drives reputation + recruiting signal |
| MMPORG | issues, PRs, discussions, projects — perpetual multi-player coordination with reputations, badges, emergent culture |
| ARTIFACT REGISTRY | Packages (containers, npm, Maven, RubyGems, NuGet) |
| IDENTITY PROVIDER | OIDC federation → every cloud's IdP |
| SECURITY COORDINATION | Advisories, code scanning, secret scanning, CODEOWNERS |
| VERSIONED OBJECT DATABASE | via BRANCH-AS-OBJECT pattern (branches named `<Type>_<id>`) |

## Flagship protocol: branch-as-object

A branch named `<TypeName>_<id>` (e.g. `Issue_45345`, `Character_alice`, `GameSave_game-abc`) stores one versioned object. The branch history IS the edit log; PR diffs are transactions; merges are consolidated commits. Extensible to any versionable non-code artifact — design docs, incident records, character sheets, configuration snapshots.

Stub: `protocols/branch-as-object.md` (consumer repos fill in full protocol docs).

## Skeleton

| Directory | What goes there |
|---|---|
| `recipes/` | `gh` one-liners, Actions workflow snippets, OIDC config examples, branch-as-object scripts |
| `instances/` | Per-org state caches (one subdir per GitHub org you operate) — org settings, repo inventory, workflow index |
| `runbooks/` | Rotate an org admin, publish a security advisory, migrate an Action to OIDC, set up a new self-hosted runner pool |
| `gotchas/` | Rate limits, workflow cache corruption, OIDC token audience mismatch, shallow clone surprises, Action tag vs SHA pinning |
| `protocols/` | `branch-as-object.md`, `oidc-federation.md`, `environments-and-approvals.md`, CODEOWNERS semantics |
| `scripts/` | gh-api automations, PR-batch operations, runner pool management |
| `cost/` | Actions minute consumption, storage (Packages, Artifacts), runner economics |

## Cross-biome relationships

```yaml
# typical consumer biomes/gateways.yml entries
- { kind: oidc_federation, from: github, to: gcp,   via: workload-identity-pool }
- { kind: oidc_federation, from: github, to: aws,   via: iam-oidc-provider }
- { kind: oidc_federation, from: github, to: azure, via: entra-federated-credential }
- { kind: deploy_dispatch, from: github, to: cloudflare, via: wrangler-action }
- { kind: artifact_pull,   from: github, to: edge-on-prem, via: git-pull }
- { kind: private_runner,  from: github, to: gcp,   via: tailscale }    # chained through tailscale
```

## Not included

No org names, no repo lists, no actual workflow YAML, no real advisories. Consumer repos populate those under `instances/<org-name>/`.
