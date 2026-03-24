# MOOGLANCE — Moo CLI at a glance (LLM-optimized)

Dense reference for the Moo VM CLI. Copy into prompts or `.cursor` rules. More: MOONUAL.md (full manual), RUNBOOK-TESTS.md (tests).

## What moo is

- **Moo** = GitHub branch as object (e.g. `Issue_42`). Files on branch = state.
- **Moorl** = URL to a moo + optional file + fragment (drill). Schemes: `moo://`, `moollm://`.
- **Config** = REPOS.yml; `moo repos` lists. User-level only: `~/.moollm/skills/moo/REPOS.yml` or `~/.moollm/skills/moocroworld/REPOS.yml` (no repo_root guessing). Override: `MOO_REPOS_FILE`. Cache: under `MOOLLM_WORKSPACE` (default cwd); set `MOOLLM_WORKSPACE=~` for user-level.

## Global options

| Option | Meaning |
|--------|--------|
| `--repo` | Repo (owner/name or alias). Default: `MOO_REPO`. |
| `--why TEXT` | Caller's reason (traceability). Moo does not answer; use `--help` for docs. |

## Commands (one-line)

| Command | Purpose |
|---------|--------|
| `repos` | List configured repos (REPOS.yml). |
| `resolve <moorl>` | Parse moorl → JSON (scheme, repo, branch, path, fragment, query). |
| `ls [repo]` | List branches. `--type PREFIX` `--glance` `--all`. |
| `tree [repo] <branch>` | List files. `-r` recursive. |
| `read (repo branch path \| moorl)` | Read file. `-k PATH` extract key. `-L START[-END]` lines. |
| `sniff (...)` | Structural lines or key-skeleton. `-k` `--depth` `--skeleton` `--skeleton-depth` `--skeleton-format`. |
| `glance` / `card` | Read GLANCE.yml or CARD.yml from branch. |
| `scan [repo] --type PREFIX -k KEY` | Per-branch extract key from file (default GLANCE.yml). `--all`. |
| `write [repo] <branch> <path>` | Write file. Content: arg, `--file`, or stdin. |
| `rm [repo] <branch>` | Delete branch. |
| `batch-glance [repo]` | GLANCE.yml per branch. `--type` `--all`. |
| `focus [overlay.yml]` | Fetch by overlay (depth, at_depth, fragments). `-o text|json`. |
| `summarize (...)` | LLM summary (Gemini). `--provider` `--model` `--no-cache`. Needs GEMINI_API_KEY. |

## Moorl (short)

- `moo://branch/path` — repo from MOO_REPO/--repo.
- `moollm://repo/branch/path` — full form.
- Fragment `#key/path` = drill (key path). `#path:L3-L10` = line range. Query `?` reserved for transforms (sniff, etc.); not used for navigation.
- Drill = moorl only (not https). See **MOOGLANCE-moorl.md**.

## Env

- `MOO_REPO` — default repo.
- `MOO_REPOS_FILE` — path to REPOS.yml.
- `MOOLLM_WORKSPACE` — cache base (default cwd). Cache: `MOOLLM_WORKSPACE/.moollm/skills/moo/cache/`.

See **MOOGLANCE-env.md**.

## Help commands (by scenario)

| Scenario | Run |
|----------|-----|
| List repos / see config | `moo repos` |
| List branches for a repo | `moo ls <repo>` or `moo ls --repo <repo>` |
| Parse a moorl | `moo resolve 'moo://Issue_0/ALERT.yml#payload'` |
| Read one file | `moo read repo branch path` or `moo read 'moorl'` |
| Read key from file | `moo read repo branch path -k payload/camera_name` or use fragment in moorl |
| Structural outline (smelly) | `moo sniff repo branch path [--depth glance|structure|full]` |
| Key skeleton (JSON/YAML) | `moo sniff repo branch file.json --skeleton [--skeleton-depth N]` |
| Sniff sub-tree | `moo sniff repo branch file.yml -k payload/items` |
| Batch GLANCE | `moo batch-glance repo --type Issue` |
| Overlay fetch | `moo focus [overlay.yml]` |
| Full command list | `moo --help` |
| Command-specific help | `moo read --help` `moo sniff --help` etc. |

## Learn more

- **Full manual:** MOONUAL.md (concepts, moorl, overlay, library API).
- **Moorl detail:** MOOGLANCE-moorl.md (fragment, query, drill, # vs /).
- **Commands detail:** MOOGLANCE-commands.md (flags per command).
- **Env/config:** MOOGLANCE-env.md (REPOS, cache, overlay path).
- **Tests:** RUNBOOK-TESTS.md (how to run, add tests).

## File layout (skill)

`moo.py` → `lib/cli.main()`. Lib: `config`, `storage`, `urls`, `sniff`, `overlay`, `gh`, `cache`, `util`; commands in `lib/commands/`. Entry from repo: `python skills/moo/moo.py` or ensure skill root on PATH.
