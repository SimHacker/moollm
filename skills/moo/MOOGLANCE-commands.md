# MOOGLANCE — Commands and flags

Dense. Top-level: MOOGLANCE.md. Full: MOONUAL.md §3.

## Invocation

Targets: either one moorl or three (repo, branch, path). Repo: positional, `--repo`, or MOO_REPO. `--all` on ls/scan/batch-glance: all configured repos.

## Key flags by command

- **read:** `-k PATH` key path; `-L START[-END]` line range.
- **sniff:** `-k PATH` sub-tree then skeleton/smelly; `--depth glance|structure|full`; `--skeleton` key-skeleton (JSON/YAML); `--skeleton-depth N` `--skeleton-format text|yaml|json`; `--max-lines N` `--max-chars N`.
- **ls:** `--type PREFIX` `--glance` `--all`.
- **tree:** `-r` recursive.
- **scan:** `--type` (required) `-k KEY` `--file FILE` `--all`.
- **write:** content from arg, `--file LOCAL`, or stdin.
- **focus:** `-o text|json` `-f FILE` (overlay path).
- **summarize:** `--provider` `--model` `--no-cache`.

## Quick ref

`moo repos` | `moo resolve <url>` | `moo ls [repo]` | `moo tree [repo] branch` | `moo read (repo branch path | moorl)` | `moo sniff (...)` | `moo glance/card [repo] branch` | `moo scan --type X -k Y` | `moo write branch path` | `moo rm branch` | `moo batch-glance` | `moo focus [overlay]` | `moo summarize (...)`.
