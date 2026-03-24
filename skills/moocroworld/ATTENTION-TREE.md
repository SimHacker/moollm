# Attention focus tree (GitHub-as-object-filesystem overlay)

An **attention focus tree** is an overlay that describes *how deep to drill* and *which parts of which files to grab* across a set of GitHub repo/branch **mooniverses**. It turns many branches in many repos into a single, adjustable view — like opening an outliner and expanding or collapsing each level. The LLM (or any consumer) gets one structured dump: batch glance (shallow) or stare (deeper, climbing down the tree as far as the overlay allows).

## Purpose

- **Batch glancing** — Fetch GLANCE.yml (or other depth-0 files) from many branches at once. One view across all selected moos.
- **Batch staring** — Fetch a configurable depth per repo/type: e.g. depth 0 = GLANCE, depth 1 = CARD + listed files, depth 2 = subdirs and their files, with optional fragments (key paths, line ranges) per file. Climb down as deep as the overlay specifies.
- **Adjustable views** — Change the overlay (depth, which files at each level, which fragments) and re-run to refocus attention without changing the underlying branches.

The overlay is the **attention focus tree**: a tree of (repo → type filter → depth → per-level file specs). It does not modify GitHub; it only defines what to *read* and how to assemble it for the LLM.

## Overlay format (YAML)

The overlay file (e.g. `attention.yml` or `focus-overlay.yml`) has this shape:

```yaml
# Optional: default depth and file specs applied when a repo doesn't override
defaults:
  depth: 1
  at_depth:
    0: [GLANCE.yml]
    1: [CARD.yml]

# Repos (and optionally aliases from REPOS.yml). Each entry defines a mooniverse.
repos:
  - repo: leela-ai/leela-alerts
    type: Issue
    depth: 2
    at_depth:
      0: [GLANCE.yml]
      1: [CARD.yml]
      2: [ALERT.yml, "data/query-result.json", "actions/*.yml"]
    fragments:
      ALERT.yml: [severity, payload/camera_name, status]
      "data/query-result.json": [confidence]
  - repo: leela-ai/moollm
    type: Character
    depth: 1
    at_depth:
      0: [GLANCE.yml]
      1: [CARD.yml, CHARACTER.yml]
```

### Top-level keys

| Key | Meaning |
|-----|--------|
| `defaults` | Optional. `depth`, `at_depth` applied to any repo that doesn't specify them. |
| `repos` | List of repo entries. |

### Per-repo entry

| Key | Meaning |
|-----|--------|
| `repo` | GitHub owner/name or an alias from REPOS.yml (e.g. `alerts`). |
| `type` | Branch name prefix: only branches matching `Type_*` are included. Omit to include all branches. |
| `depth` | Max depth to drill (0 = only depth 0 files, 1 = depth 0 + 1, etc.). |
| `at_depth` | Map depth (int) → list of file paths or globs at that depth. Depth 0 = root of branch. Deeper depths can be dir-relative (e.g. `evidence/frames/*.yml`). |
| `fragments` | Optional. Map file path (key in at_depth) → list of fragment key paths or line specs (`L3`, `L3-L10`) to extract. Only those parts are included. |

### Depth and tree climbing

- **Depth 0** — Root of the branch. Typically `GLANCE.yml`, sometimes `README.md`.
- **Depth 1** — Still root: CARD.yml, instance data (ALERT.yml, CHARACTER.yml), etc.
- **Depth 2** — Can list files in subdirs: `actions/*.yml`, `data/query-result.json`, `evidence/frames/*.yml`. The tool expands globs per branch (list dir, match pattern).
- **Deeper** — Same idea: each level can add more files or globs. The overlay defines the ceiling; the tool fetches up to that depth and stops.

Outliner metaphor: at each level you choose "how much to expand." The overlay stores that choice. Re-run with a different overlay (or edit depth/at_depth) to change the view.

## Batch glance vs stare

- **Glance** — Depth 0 only. For each branch in scope: fetch `GLANCE.yml` (or whatever is listed at depth 0). Output: one block per branch, minimal content. Use for "show me all Issue_ branches in these repos at a glance."
- **Stare** — Depth ≥ 1 from the overlay. For each branch: fetch depth 0, then depth 1, then … up to overlay depth; expand globs; apply fragments when specified. Output: one structured tree per branch (or one combined document). Use for "give the LLM a focused dump of these mooniverses so it can reason about them."

## Output shape (for LLM consumption)

- **Batch glance:** Markdown or YAML with a section per branch. Each section: branch name (and repo), then content of depth-0 files (e.g. GLANCE.yml).
- **Stare:** Same, but each section contains a tree: depth 0, then depth 1, then … with file paths as headers and (optionally) only the requested fragments per file. This keeps context bounded and relevant.

## Tool commands (moo.py)

- `moo batch-glance [repo|alias] [--type Type]` — Batch glance: list branches (optionally filtered by type), read GLANCE.yml for each, print combined view. No overlay file.
- `moo batch-glance --all` — Batch glance across all repos in REPOS.yml that have a default_type (or --type).
- `moo focus <overlay.yml>` or `moo stare -f <overlay.yml>` — Read overlay; for each repo/type, list branches; for each branch, fetch content by depth and at_depth; apply fragments; print combined attention tree. Option: `-o json` for machine-readable.

Overlay file can live in the skill dir, in .moollm/, or any path. REPOS.yml aliases can be used in overlay `repo` entries so the tool resolves owner/name and token.

## Part of moocroworld

- GitHub-as-object-filesystem: repos and branches are the object store; the attention tree is the view.
- Semantic pyramid: glance = depth 0, stare = deeper (CARD, instance data, evidence).
- See CARD.yml (moo_cli, batch_glance_stare) and ATTENTION-TREE.example.yml.
