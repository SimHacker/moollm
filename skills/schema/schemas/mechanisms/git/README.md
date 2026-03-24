# Git (schemapedia: `git`)

**VCS family.** **Distributed** version control: objects (blobs, trees, commits), **DAG** history, refs, remotes, merges, **hooks**. Timeline and provenance for files—MOOLLM’s **self-object** story assumes git history.

## Why it matters here

Git is **not** “just a format”: packfiles and protocols are interchange-shaped, but the product is **history + identity** for trees. [github](../github/README.md) hosts git; [shell-orchestration](../shell-orchestration/README.md) wraps hooks and CI glue.

## What’s distinctive

- **Branches** are refs to commits—parallel lines of development; merge/rebase are first-class.
- **Hooks** (`pre-commit`, etc.) bridge to execution without mixing layers ([`../../gateways.yml`](../../gateways.yml): `git-hooks-execution`).
- **Signing**, `blame`, and archaeology are **trust and attribution** on top of content.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [github](../github/README.md) | Hosted remotes, PRs, API—`github-over-git`. |
| [shell-orchestration](../shell-orchestration/README.md) | Hooks and automation around git events. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Docs | [git-scm.com](https://git-scm.com/doc) |
| Book | [Pro Git](https://git-scm.com/book/en/v2) (free) |
| Overview | [Wikipedia: Git](https://en.wikipedia.org/wiki/Git) |
| Source | [github.com/git/git](https://github.com/git/git) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
