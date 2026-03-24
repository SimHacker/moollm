# moo — Moo virtual machine CLI

**moo** is the command-line interface for the Moo virtual machine: GitHub branches as structured object storage. Each branch is a *moo* (e.g. `Issue_42`, `Character_Don`). You list repos and branches, walk trees, read and write files, resolve moorls, and run batch or attention-tree fetches (glance, focus). Everything goes through `gh api`; repo configuration and overlay definitions live in the moocroworld skill.

**High level:**

- **Repos and branches** — `moo repos` lists configured mooniverses (from REPOS.yml). `moo ls [repo]` lists branches (moos), optionally with a GLANCE summary. `moo tree repo branch` lists files on a branch.
- **Read and write** — `moo read` and `moo write` work on repo/branch/path or on a single moorl (moo:// or moollm:// URL). Read supports fragment key paths and line ranges.
- **Sniff** — `moo sniff` pulls out structural “smelly” lines (defs, classes, keys, headers) from Python, YAML, Markdown, and TS/JS, with optional caps.
- **Resolve** — `moo resolve <moorl>` prints the parsed URL as JSON (scheme, repo, branch, path, fragment, query).
- **Batch and focus** — `moo batch-glance` fetches GLANCE.yml for each branch (optionally by type or all repos). `moo focus [overlay.yml]` fetches by attention-tree overlay (depth, at_depth, fragments).

Entry point: `moo.py` in this directory. Logic is split into `lib/` (config, storage, urls, sniff, overlay, gh, cache, util, why) and `lib/commands/`; you can import the library for programmatic use. Cache is ephemeral under `.moollm/skills/moo/cache/`.

For full command reference, moorl syntax, overlay format, environment variables, and library API, see **[MOONUAL.md](MOONUAL.md)** (Moo Manual). For running and extending the test suite, see **[RUNBOOK-TESTS.md](RUNBOOK-TESTS.md)**.

Part of MOOLLM. See repo README and skills/README.
