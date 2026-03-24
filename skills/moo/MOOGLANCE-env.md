# MOOGLANCE — Environment and config

Dense. Top-level: MOOGLANCE.md. Full: MOONUAL.md §4–5.

## Env vars

| Var | Purpose |
|-----|--------|
| MOO_REPO | Default repo (owner/name or alias). |
| MOO_REPOS_FILE | Path to REPOS.yml. If unset: user-level only (see REPOS.yml below). |
| MOOLLM_WORKSPACE | Cache base (default cwd). Cache: `$MOOLLM_WORKSPACE/.moollm/skills/moo/cache/`. User-level: set to `~`. |
| GEMINI_API_KEY | For `moo summarize` (optional). |

## REPOS.yml

Maps alias → github, description, default_type, gh_token_env. **User-level only** (spans repos): `~/.moollm/skills/moo/REPOS.yml` or `~/.moollm/skills/moocroworld/REPOS.yml`. No repo_root/.moollm. Override: MOO_REPOS_FILE.

## Overlay (attention tree)

YAML: defaults.depth, defaults.at_depth; repos[].repo, type, depth, at_depth, fragments. depth = max depth (0-based); at_depth = files per depth; fragments = key paths to extract per file. Default overlay: moocroworld ATTENTION-TREE.example.yml. `moo focus [overlay]` loads it.
