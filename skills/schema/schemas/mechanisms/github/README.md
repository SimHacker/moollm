# GitHub (schemapedia: `github`)

**Collaboration family.** Hosted **git**, **REST/GraphQL** APIs, **Issues/PRs**, reviews, **Actions**, Packages, Pages, and a **social graph** (stars, follows, orgs). One product, several **schema-shaped** layers—JSON APIs, workflow YAML, and raw git objects are not the same thing.

## Why it matters here

MOOLLM adds **branch-as-object** work: typed orphan branches (`ClassName_ObjectID`, e.g. **`Issue_<IssueID>`**), **moorl** URLs, and the **moo** CLI. That model is **delegated**—do not duplicate it in this folder.

| Role | Skill | Purpose |
|------|---------|---------|
| Theory | [moocroworld](../../../../moocroworld/SKILL.md) | Branches as actors; Issues as conversation vs branch state |
| Tooling | [moo](../../../../moo/MOONUAL.md) | `moo://`, `moollm://`, read/write/list |

## What’s distinctive

- **Issues** (API) vs **Issue_*** branches (git state)—two layers; see [`MECHANISM.yml`](./MECHANISM.yml) `objects_in_repo`.
- **Actions** overlap [shell-orchestration](../shell-orchestration/README.md) (workflow YAML, runners).
- API payloads pair naturally with [json-schema](../json-schema/README.md) ([`../../gateways.yml`](../../gateways.yml): `github-api-json-schema`).

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [git](../git/README.md) | GitHub stores git; PRs = refs + metadata—`github-over-git`. |
| [json-schema](../json-schema/README.md) | REST/GraphQL JSON bodies. |
| [sqlite](../sqlite/README.md) | Local caches / extensions—not server truth. |
| [shell-orchestration](../shell-orchestration/README.md) | `gh`, Actions, scripted workflows. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Docs | [GitHub Docs](https://docs.github.com/) — [REST](https://docs.github.com/en/rest), [GraphQL](https://docs.github.com/en/graphql) |
| CLI | [GitHub CLI](https://cli.github.com/) (`gh`) |
| Company / product | [github.com](https://github.com) |
| Overview | [Wikipedia: GitHub](https://en.wikipedia.org/wiki/GitHub) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Systems index: [`../../systems.yml`](../../systems.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
