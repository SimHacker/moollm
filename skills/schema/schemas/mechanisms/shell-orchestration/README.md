# Shell orchestration (schemapedia: `shell-orchestration`)

**Execution family.** Compose **shell**, scripts, and skill procedures into runnable automation—**sister-script** lift, **plan-then-execute** gates, **mooco** orchestration, **runtime** duality. Natural fit for IDEs with terminals (e.g. Cursor).

## Why it matters here

“Schema” includes **how work runs**, not only data shapes. After a run, [cursor-mirror](../cursor-mirror/README.md) can inspect **what actually happened** (timeline, tools, thinking)—[`../../gateways.yml`](../../gateways.yml): `shell-then-mirror`.

## What’s distinctive

- **Delegates** (reading order in [`MECHANISM.yml`](./MECHANISM.yml)): [sister-script](../../../../sister-script/SKILL.md), [plan-then-execute](../../../../plan-then-execute/SKILL.md), [mooco](../../../../mooco/SKILL.md), [runtime](../../../../runtime/SKILL.md).
- **POSIX vs bash**: choose portability vs convenience explicitly.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [cursor-mirror](../cursor-mirror/README.md) | Observability: execute, then introspect session DB / traces. |
| [git](../git/README.md) | Hooks and CI glue are shell-shaped; not the git object model. |
| [github](../github/README.md) | Actions workflows + local `gh`/`git` scripts. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Shell | [GNU Bash](https://www.gnu.org/software/bash/) |
| Standard | [POSIX shell](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
