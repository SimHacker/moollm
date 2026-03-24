# moo — Moo virtual machine CLI

The moo skill is the implementation of the moo CLI. Moocroworld is the skill that defines the model (branches as actors, moorls, crows); moo is the engine that runs the commands.

- **REPOS.yml**: Resolved from moocroworld (skills/moocroworld/REPOS.yml or MOO_REPOS_FILE). Moo does not ship its own REPOS.yml.
- **Ephemeral cache**: `.moollm/skills/moo/cache/` — file cache (per repo/branch/path), persisted to disk, loaded on first use, saved at exit. Clear that directory to reset cache.
- **Entry point**: `skills/moo/moo.py`. The moocroworld skill provides a thin wrapper so `python skills/moocroworld/moo.py` (or the installed `moo` command) delegates to the moo skill.

**Full reference**: [MOONUAL.md](MOONUAL.md) (Moo Manual) — commands, moorl syntax, overlay format, environment, library API.

Part of MOOLLM. See repo README and skills/README.
