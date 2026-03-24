# MOONUAL — Moo Manual

*A tribute to the Lisp Machine Manual (Moon et al.).*

This is the reference manual for the Moo virtual machine CLI: concepts, commands, moorl syntax, overlay format, environment, and library API.

---

## 1. Concepts

### 1.1 Moo and moorl

- **Moo** — A single GitHub branch treated as an object. Branches are named like `ClassName_ObjectID` (e.g. `Issue_42`, `Character_Don`). The branch is the “object”; files on it are its state.
- **Moorl** — A URL that addresses a moo (and optionally a file and fragment). Schemes: `moo://` and `moollm://`. See [Moorl syntax](#2-moorl-syntax).
- **Mooniverse** — A configured set of repos (from REPOS.yml in the moocroworld skill). `moo repos` lists them.

### 1.2 Cache

Ephemeral file cache under `.moollm/skills/moo/cache/`. Layout: `cache/<repo_slug>/<branch>/<path>`. Whole-file; loaded on first read, written on write. Clear the directory to reset. Optional in-memory cache for the process.

### 1.3 Overlay (attention tree)

An overlay YAML (e.g. ATTENTION-TREE.example.yml) defines which repos and branches to scan and which files to fetch at each depth (e.g. depth 0: GLANCE.yml; depth 1: CARD.yml; depth 2: specific files or globs). Optional fragment extraction per file. Used by `moo focus` and (conceptually) by a future “render attention tree” command.

---

## 2. Moorl syntax

### 2.1 Forms

- **moo://**`branch`**/**`path`  
  Branch is the first path component (netloc in URL terms). Repo comes from `MOO_REPO` or `--repo`. Example: `moo://Issue_42/ALERT.yml`.

- **moollm://**`repo`**/**`branch`**/**`path`  
  Repo = netloc (owner/name). Path = `branch/path`. Example: `moollm://leela-ai/leela-alerts/Issue_42/ALERT.yml`.

### 2.2 Fragment and query

- **Fragment** (after `#`) — Path into the resource and/or line spec. Path format can be content-type-specific (see 2.2.2).
  - Current: slash-separated key path, e.g. `payload/camera_name`, `repos/0`.
  - Allowed: JSONPath or dotted notation for JSON/YAML; XPath or equivalent for HTML when supported.
  - Line spec: `L3` or `L3-L10` (1-based inclusive), optionally suffixed: `path:L3-L10`.
- **Query** (after `?`) — Reserved for *transformations* (sniff, skeleton, depth, future: image snippet, resize). On moorl we define semantics; see below. Not used for navigation — use fragment.

**Drill into a file** — Use the fragment only: `file.yml#payload/camera_name` or `file.yml#repos/0`. No need to put key path in the path segment or in the query; fragment is the place for key path and line spec.

#### 2.2.1 Drill: # vs / (moorl only)

We use **# (fragment)** for drill. Alternative would be **/ (path segments)** after the file, e.g. `path/to/file.yml/payload/camera_name`. Comparison:

- **# (fragment)** — **Current and recommended.** Standard URL semantics: fragment is client-side and not part of the resource path. Unambiguous: path is always the file (we have a tree), fragment is always key path (and optional line spec). No parsing rule needed. Downside: some shells may require quoting; a few tools strip fragments.
- **/ (path syntax)** — Would require a rule to split “file path” from “key path,” e.g. “last segment with a known extension (.yml, .json, .yaml) is the file; following segments are key path.” That is brittle (e.g. `data/config.yml.bak`, or keys that look like segments). It also mixes “path to resource” with “path inside resource” in one string. On moorl we could define it (GitHub doesn’t have a blob at `file.yml/payload`), but it adds a convention and edge cases.
- **Both** — Two ways to do the same thing; more to document and maintain; / has the parsing issues above.

**Decision: use # only for drill.** CLI `--key` remains the alternative when you already have a moorl or repo/branch/path. Non-goal: http(s) URLs do not support drill (see 2.3).

#### 2.2.2 Fragment path format (free format by content type)

Fragments can support a **freer, format-appropriate** path language instead of only slash-separated keys:

- **JSON** — JSONPath (e.g. `$.payload.camera_name`, `$.repos[0].name`) or JavaScript dotted/bracket notation (`payload.camera_name`, `repos[0].name`).
- **YAML** — Same as JSON for the loaded graph (YAML is a superset of JSON); equivalently a JSONPath-like or dotted path into the parsed structure.
- **HTML** — XPath or a CSS-selector-like fragment, depending on what the implementation uses for HTML trees.

The **current implementation** uses a single, simple rule: slash-separated path (`payload/camera_name`, `repos/0`) for both JSON and YAML, with numeric segments as array indices. That is a subset of what dotted or JSONPath can express.

**Design:** the fragment string is not fixed to one grammar. Implementations may interpret it by file type: JSONPath or dotted for .json/.yml/.yaml, XPath (or similar) for .html when supported. Line specs (e.g. `:L3-L10`) can remain a trailing suffix that is stripped before evaluating the path. This keeps moorl fragments flexible and allows adding JSONPath, XPath, or dotted notation without changing the URL shape.

### 2.3 Navigation vs transforms; https

- **Navigation** (what to fetch / where inside it): path (which file), fragment (key path, line range). So “drill” is always `#key/key/key` (and optional `:L3-L10`).
- **Transforms** (how to present or reduce): intended for the query string on moorl — e.g. `?sniff`, `?skeleton`, `?depth=glance`, `?snippet=...`, `?resize=...`. Commands can already express these via flags (`--key`, `--skeleton`, etc.); query would allow a single moorl to encode “fetch this and sniff it.”
- **HTTPS and other non-moo URLs** — They have valid, server-defined query strings. **Constraint: no query magic on non-moo URLs.** If we ever support fetching `https://...` (or similar), the URL is passed through unchanged to the fetch; we do not interpret query for transforms. Apply transforms via CLI flags only (e.g. `moo read https://... --key x` or a hypothetical fetch command with flags). Alternative if we need transforms in URL later: a single reserved param (e.g. `moo=sniff,skeleton`) that we strip before passing the URL to the server, so server params remain intact.
- **Drill only on moorl** — Fragment-based drill (`#key/key`) is defined and reliable only for `moo://` and `moollm://`. We have a tree (branch + path): we know which path segment is the file, so the fragment unambiguously means “key path into that file.” For http(s) we do not have a local directory or listing to discover where the “file” ends and the “key path” begins; the server could treat any path segment as part of the URL. So we cannot reliably drill into http-fetched resources by fragment. Use `--key` (CLI) when you have fetched an http resource and want to extract a sub-tree from the response.

### 2.4 Resolve

`moo resolve <moorl>` prints JSON: `scheme`, `repo`, `branch`, `path`, `fragment_key_path`, `fragment_line_start`, `fragment_line_end`, `query`. For `moo://`, `resolved_repo` may be set from `MOO_REPO`. Query is currently passed through; transform semantics (e.g. `?sniff`) are reserved for future use.

---

## 3. Commands

### 3.1 repos

```text
moo repos
```

Lists configured repos (from REPOS.yml). Shows alias, GitHub owner/name, description, default type prefix, and optional auth env. No repo/positional needed.

### 3.2 resolve

```text
moo resolve <moorl>
```

Parses the moorl and prints components as JSON. No repo/positional needed.

### 3.3 ls

```text
moo ls [repo] [--type PREFIX] [--glance] [--all]
```

Lists branches. `repo`: positional or `--repo` or `MOO_REPO`. `--type`: filter by branch name prefix (e.g. `Issue`). `--glance`: append a one-line summary from GLANCE.yml. `--all`: iterate all configured repos with a default type and list branches for each.

### 3.4 tree

```text
moo tree [repo] <branch> [--recursive|-r]
```

Lists files on the branch (type + path per line). `--recursive`: full tree.

### 3.5 read

```text
moo read (repo branch path | moorl) [--key PATH] [-L START[-END]]
```

Reads a file (or value at key path, or line range). Either three arguments (repo, branch, path) or one moorl. `--key`: slash-separated YAML/JSON path. `-L`: 1-based line range (e.g. `3` or `3-10`).

### 3.6 sniff

```text
moo sniff (repo branch path | moorl) [--key PATH] [--depth LEVEL] [--skeleton] [--skeleton-depth N] [--skeleton-format text|yaml|json] [--max-lines N] [--max-chars N]
```

Extracts “smelly” (structural) lines by file type (Python, YAML, Markdown, TS/JS). `--depth`: glance (1), structure (2), full (3). `--skeleton`: for .json/.yml/.yaml only; recursive key skeleton (object keys and array lengths). `--key PATH`: navigate to sub-tree (e.g. payload/items); then skeleton (dict/list) or smelly (string). `--skeleton-depth N`: max recursion depth (root = 0). `--skeleton-format`: text, yaml, or json. Optional caps: `--max-lines`, `--max-chars`.

### 3.7 glance, card

```text
moo glance [repo] <branch>
moo card [repo] <branch>
```

Reads `GLANCE.yml` or `CARD.yml` from the branch. Repo from positional, `--repo`, or `MOO_REPO`.

### 3.8 scan

```text
moo scan [repo] --type PREFIX --key KEY [--file FILE] [--all]
```

For each branch (optionally filtered by `--type`), reads the file (default GLANCE.yml) and prints the value at the given key. `--all`: all configured repos with default type.

### 3.9 write

```text
moo write [repo] <branch> <path> [content] [--file LOCAL_PATH]
```

Writes to the file on the branch. Content from argument, `--file`, or stdin.

### 3.10 rm

```text
moo rm [repo] <branch>
```

Deletes the branch.

### 3.11 batch-glance

```text
moo batch-glance [repo] [--type PREFIX] [--all]
```

Fetches GLANCE.yml for each branch (optionally filtered by type). `--all`: all configured repos with default type.

### 3.12 focus

```text
moo focus [overlay.yml] [-o text|json] [-f FILE]
```

Loads the overlay (default: moocroworld ATTENTION-TREE.example.yml), fetches branches per repo/type, and for each branch fetches files by depth/at_depth; applies fragment extraction when defined. Output: text (default) or JSON.

### 3.13 --why

```text
moo [--why TEXT] [command] ...
```

Optional. **Caller** (person, LLM, or script) supplies a reason for invoking (`--why "check severity for report"`). Moo accepts it for traceability or passing to an executor; moo does not answer “why” or print intent. For command documentation use the standard Python CLI help: `moo --help`, `moo read --help`, etc.

---

## 4. Environment and configuration

- **MOO_REPO** — Default repo (owner/name or alias) when not given by positional or `--repo`. Used for `moo://` and for commands that need a single repo.
- **MOO_REPOS_FILE** — Path to REPOS.yml. If unset, moo resolves via skill-relative and cwd paths (see moocroworld).
- **MOOLLM_WORKSPACE** — Base directory for cache; default is current working directory. Cache lives under `MOOLLM_WORKSPACE/.moollm/skills/moo/cache/`.
- **REPOS.yml** — In moocroworld: maps aliases to `github`, `description`, `default_type`, `gh_token_env`. Moo does not ship its own; it uses moocroworld’s or the path from MOO_REPOS_FILE.

---

## 5. Overlay format (attention tree)

Overlay YAML (e.g. ATTENTION-TREE.example.yml):

```yaml
defaults:
  depth: 1
  at_depth:
    0: [GLANCE.yml]
    1: [CARD.yml]

repos:
  - repo: owner/name   # or alias from REPOS
    type: Issue        # branch name prefix, or null for all
    depth: 2
    at_depth:
      0: [GLANCE.yml]
      1: [CARD.yml]
      2: [ALERT.yml, "data/*.json"]
    fragments:         # optional: extract keys per file
      ALERT.yml: [severity, payload/camera_name]
```

- **depth** — Max depth (0-based). For each depth, **at_depth** lists file paths or globs. **fragments** maps file path to list of key paths (slash-separated) to extract; only the extracted subset is emitted.

---

## 6. Library API

Add the skill root to `sys.path`, then:

```python
from lib import config, storage, urls, sniff, overlay, gh, cache, util
```

- **config** — `find_repos_file()`, `load_repos()`, `resolve_repo(name_or_alias, repos_config)`.
- **storage** — `read_file(repo, branch, path, token_env=None)`, `write_file(repo, branch, path, raw_bytes, token_env=None)`, `list_tree(...)`, `extract_at_path(content, path, path_str)`, `delete_branch(...)`.
- **urls** — `parse_moo_url(url)`, `parse_fragment(fragment)`, `is_moo_url(s)`.
- **sniff** — `sniff_smelly_lines(text, path, depth=None, max_lines=None, max_chars=None)`, `sniff_skeleton(content, path, max_depth=None, format="text")`, `sniff_skeleton_data(data, max_depth=None, format="text", path_prefix="")` (sub-tree skeleton), `SNIFFERS` (ext → function).
- **overlay** — `load_overlay(path, repos_config)`, `expand_globs(repo, branch, patterns, token_env)`, `default_overlay_path()`.
- **gh** — `gh_api(endpoint, method=..., body=..., jq=..., token_env=...)`, `get_token_env(repo_entry)`.
- **cache** — `get(repo, branch, path)`, `set_content(...)`, `invalidate(...)`, `cache_dir()`, `safe_path(path)`.
- **util** — `yaml_load(text)`, `yaml_dump(data)`, `apply_line_range(text, line_start, line_end)`.

Command handlers live in `lib.commands` (repos, ls, read, sniff_cmd, scan, write, resolve, focus); the CLI is in `lib.cli.main()`.

---

## 7. File layout (skill)

```text
skills/moo/
  moo.py              # Entry point; calls lib.cli.main()
  README.md           # High-level overview; points here
  MOONUAL.md          # This manual
  GLANCE.yml, CARD.yml, SKILL.md
  lib/
    __init__.py       # Re-exports modules
    cli.py            # Argparse and dispatch
    util.py, urls.py, sniff.py, cache.py, config.py, gh.py
    storage.py, overlay.py
    commands/
      repos.py, ls.py, read.py, sniff_cmd.py, scan.py
      write.py, resolve.py, focus.py
```

---

*Part of MOOLLM. See repo README and skills/README.*
