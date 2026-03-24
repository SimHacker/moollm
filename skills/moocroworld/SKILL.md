# Moocroworld

Each branch is an actor. Crows fly between them.

A moocroworld is a typed object stored as an orphan git branch.

## What moo can do (and what more)

**moo.py today:** List repos (`repos`), list and filter branches (`ls`, `tree`), read files with optional key path or line range (`read`, `glance`, `card`), scan branches for a key (`scan`), write files (`write`), delete branches (`rm`). **Resolve moorls:** `moo resolve <moorl>` parses a moorl and outputs JSON (repo, branch, path, fragment key path, fragment line range, query). **Drill-down and lines:** `read` accepts a moorl; the fragment drills into YAML/JSON (key path), selects line ranges (`L3`, `L3-L10`, or `key/path:L3-L10`), and can be combined with `-k` and `-L` when using repo/branch/path args. **Intent (--why):** Moo universally supports `--why` as **designer-authored intent passed to the executor** — not the executor describing why. The designer (skill author, pipeline author) supplies the "why"; the executor (LLM, script, log) receives it. It acts as a declarative comment of intent; in some contexts it is a no-op. Use it to guide LLMs, document log entries, or pass intent from designer to executor. `moo --why` or `moo read --why` (with any command) emits that intent.

**What more:** Query parameters on read (e.g. `?crop`, `?frame`, `?where`) are defined for the orchestrator and type-aware extraction; moo.py can stay focused on URL resolve and fragment handling. **File editing:** A documented **file editor protocol** (EDIT-PROTOCOL.md) defines pluggable, self-documenting edit techniques per file type (YAML path, JSON path, line range, spreadsheet, HTML, regexp) so the LLM can edit files robustly via a single protocol surface; implementations are added incrementally.

**User space and URL-based extension.** Moo reimplements platform file tools (read, write, list, etc.) in user space via terminal, shell, gh, and Python — no platform-specific file APIs required. It also has its own **plugin extension points and services**, all **URL-based (moorls)**. That makes moo a **device-driver replacement** for native tools that are less efficient, less powerful, and less integrated: moorl-based access is more efficient (batch glance/focus, targeted fetch), more powerful (fragments, query params, edit protocol, attention tree), and more integrated (one addressing scheme across repos and branches). Resolve a moorl → dispatch to a command or handler; query params and fragment → type-aware services; edit protocol → plugins by file type. See CARD.yml `plugins_and_services` and EDIT-PROTOCOL.md.

The repo's main branch is the "main world" with shared rooms and structure. Moocroworlds orbit outside it — independent existences paged into context on demand by mooco.

## Lineage

- **Hewitt** (1973) — Actor model: independent processes, message passing, no shared mutable state. Each moocroworld branch is an actor.
- **Kahn** — Concurrent actors in computational media. Ken Kahn's programming actors realized in git: each branch-actor receives messages (commits from any agent), processes them (file tree evolves), and can communicate with other actors (cross-references, merge actions, issue comments).
- **Papert** — Microworlds: small, complete universes to think with. Each branch is a microworld you can enter, explore, and manipulate.
- **Minsky** — K-lines, society of mind. Branch names are K-lines (activators). The repo is a society of branch-actors; behavior emerges from their interactions.

MOO (MOOLLM) + crow (intelligent agent) + microworld (Papert) = moocroworld.

## The main world and moocroworlds

A git repo has one main branch (the "main world") and any number of orphan branches (moocroworlds). They coexist in the same repo but do not share git history.

**Main branch:** Shared structure. Config, skill definitions, room layouts, navigation, indexes. Directories are rooms (see: room skill). This is the world everyone enters first.

**Moocroworlds:** Independent branches named `ClassName_ObjectID`. Each has its own file tree, its own git log, its own MOOLLM interface (GLANCE → CARD → instance data). Created when an object is born, grows as agents act on it, archived when the object is done.

The main branch may reference moocroworlds (an index file, a room with links to branches), but the moocroworld's data lives entirely on its own branch. The mooco orchestrator pages moocroworlds into context on demand — bring it in when relevant, release it when done.

## Branch naming: ClassName_ObjectID

```
Issue_abc123           # alert event
Issue_0                # prototype alert (the schema IS the example)
Definition_Motion      # alert definition
Camera_BADHOEVEDORP_1  # camera config
Character_Rocky        # adventure character
Report_2026-02-weekly  # generated report
Session_abc123         # chat session archive
```

ClassName is the type. ObjectID is the instance. `git branch --list 'ClassName_*'` lists all instances of a type. The prefix prevents collisions between object types and makes the branch list self-documenting.

## Addressing: moorls (moo:// and moollm://)

A **moorl** is a moo:// or moollm:// URL — the term for any such URL in this skill. A moo is a top-level typed object mounted in the local mooco VM. It can come from anywhere — a GitHub repo, a local git repo, a database, an API. Two URL schemes:

**`moo://`** — local namespace. What's mounted in the VM right now, regardless of origin. Like a Unix mount or a Python import: the agent sees `moo://Issue_0/ALERT.yml`, not the full repo path. The mount abstracts the origin.

**`moollm://`** — origin namespace. The full path to where a moo actually lives: `moollm://repo/ClassName_ObjectID/path`. Used for cross-repo references, mounting, and provenance.

```
moo://Issue_0/ALERT.yml                        ← local (mounted)
moollm://leela-alerts/Issue_0/ALERT.yml        ← origin (where it lives)

moo://Character_Rocky/CARD.yml                 ← local
moollm://moollm/Character_Rocky/CARD.yml       ← origin

moo://Camera_BADHOEVEDORP_1/GLANCE.yml         ← local
moollm://central/Camera_BADHOEVEDORP_1/GLANCE.yml ← origin
```

Mooco mounts moos into the `moo://` namespace on demand:

```
mount: moo://Issue_0      ← from moollm://leela-alerts/Issue_0
mount: moo://Issue_abc123 ← from moollm://leela-alerts/Issue_abc123
mount: moo://Character_Rocky ← from moollm://moollm/Character_Rocky
```

Once mounted, every agent addresses them the same way. The agent doesn't need to know (or care) whether the moo came from `leela-alerts` or `moollm` or a customer repo. This is the same abstraction as LambdaMOO's `#123` — a local object number that doesn't encode where the object was defined. The `moo://` scheme is the MOOLLM equivalent of `#`.

## Drilling into files: fragment paths

Moo and moollm URLs can drill into YAML, JSON, and other structured files using fragment paths. The URL points to the file; the fragment (`#`) navigates inside it.

```
moo://Issue_0/ALERT.yml#severity                          → "info"
moo://Issue_0/ALERT.yml#payload/camera_name               → ""
moo://Issue_0/ALERT.yml#github_issues/0/issue_url         → first issue URL
moo://Issue_0/data/query-result.json#confidence            → 0.0
moo://Issue_0/CARD.yml#evidence/frames                     → 1
moo://Issue_0/actions/004-approve.yml#message              → approval message text
moo://Issue_0/evidence/frames/frame-000-t0.yml#annotations/0/top_label → "Person"
```

Fragment syntax:
- `/` separates keys (YAML/JSON object traversal)
- Numeric segments index into arrays (`github_issues/0` = first element)
- **Line range:** `L3` (line 3), `L3-L10` (lines 3–10, 1-based inclusive). Use for text files or to slice the string value at a path.
- **Path + lines:** `key/path:L3-L10` — lines 3–10 of the value at that path (e.g. a multi-line field).
- Works on YAML, JSON, CSV (column name or row/column), and any structured format with a defined path convention

**Resolving URLs.** The CLI resolves moo URLs to concrete repo, branch, path, and fragment:

- `moo resolve <url>` — parses a `moo://` or `moollm://` URL and prints JSON: scheme, repo, branch, path, fragment_key_path, fragment_line_start/end, query.
- `moo read <url>` — same URL form; if the fragment is a key path, the value at that path is returned; if `Ln` or `Ln-Lm`, that line range is returned. Combines with `-k` and `-L` for explicit key or line range when using repo/branch/path args.

This means a single URL can point to a specific value inside a specific file inside a specific moo. An agent (or a link in an issue comment, or a reference in another moo's YAML) can cite exactly the piece of data it means:

```yaml
# In an analysis file, referencing specific evidence
evidence_reviewed:
  - moo://Issue_abc123/evidence/frames/frame-002-reviewer.yml
confidence_source: moo://Issue_abc123/data/query-result.json#confidence
prior_severity: moo://Issue_abc123/ALERT.yml#severity
merged_from_camera: moo://Issue_def456/ALERT.yml#payload/camera_name
```

Origin URLs work the same way:

```
moollm://leela-alerts/Issue_abc123/ALERT.yml#severity
moollm://moollm/Character_Rocky/CARD.yml#autonomy_layers/emotional
```

The fragment is resolved by the reader (mooco, an LLM, a script). The file is loaded, the path is walked, the value is returned. For YAML this is natural — YAML is a tree, paths navigate it. For JSON the same. For CSV, `#column_name` or `#row/column` by convention.

## Plugin extension points and services (all URL-based)

Moo reimplements platform file tools in user space (terminal, shell, gh, Python) and exposes **plugin extension points and services** — all invoked by **moorl**. It can serve as a **device-driver replacement** for native tools that are less efficient, less powerful, or less integrated: one moorl-based layer gives batch and targeted fetch, drill-down and type-aware transforms, pluggable edit, and a single scheme across repos and branches. Extension points:

- **Resolve** — A moorl resolves to JSON; the result can dispatch to core commands (read, write, list) or to a registered handler (custom scheme or path pattern).
- **Query params** — `?crop`, `?frame`, `?where` are type-aware services; plugins register by file suffix or path.
- **Fragment** — Key path and line range are built-in drill-down; extraction can be extended per type.
- **Edit** — EDIT-PROTOCOL: plugins register by file type (yaml_path, json_path, line_range, spreadsheet, HTML, regexp); `edit(moorl, operation, payload)` routes to the right plugin.

Core read/write/list are built in; edit protocol, query-param transforms, and custom handlers are pluggable. You invoke a service by using the appropriate moorl (and optional query string or fragment).

## Orchestrator tool integration

Mooco's standard file tools (`read`, `write`, `list`) accept moorls as paths. No separate "moo tools" — the same tools agents already use for local files work transparently on moos. The URL scheme is the routing layer.

**read** — read a file or a value inside a file.

```
read("moo://Issue_0/GLANCE.yml")                     → full file contents
read("moo://Issue_0/ALERT.yml#severity")              → "info"
read("moo://Issue_0/ALERT.yml#payload/camera_name")   → ""
read("moollm://leela-alerts/Issue_abc123/ALERT.yml")  → full file from origin
```

If the path has no fragment, return the whole file. If it has a fragment, parse the file (YAML/JSON), walk the path, return the value. If the moo is not mounted, mooco auto-mounts it from the origin (lazy mount).

**write** — write a file or update a value inside a file.

```
write("moo://Issue_0/ALERT.yml#severity", "high")     → update severity in ALERT.yml, commit
write("moo://Issue_0/evidence/frames/frame-003.jpg", <binary>) → add file, commit
write("moo://Issue_0/actions/005-escalate.yml", <yaml>) → add action file, commit
```

Writing to a fragment parses the file, updates the value at the path, writes the file back, and commits. Writing a whole file replaces it. Writing a new path creates the file. Every write is a git commit on the moo's branch — the history is automatic.

**list** — list contents of a directory in a moo, or list keys in a structured file.

```
list("moo://Issue_0/")                       → [ALERT.yml, GLANCE.yml, CARD.yml, README.md, evidence/, data/, ...]
list("moo://Issue_0/evidence/frames/")       → [frame-000-t0.jpg, frame-000-t0.yml, ...]
list("moo://Issue_0/actions/")               → [001-triggered.yml, 002-vision-gate.yml, ...]
list("moo://Issue_0/ALERT.yml#")             → top-level keys: [id, alert_definition_id, severity, ...]
list("moo://Issue_0/ALERT.yml#payload")      → keys under payload: [project_id, bucket_name, ...]
list("moo://")                               → all mounted moos: [Issue_0, Issue_abc123, Character_Rocky, ...]
```

Listing a directory returns file/directory names. Listing a file with `#` returns its top-level keys (or keys at the fragment path). Listing `moo://` itself returns all mounted moos — like `ls /mnt/`.

**File-type-aware operations.** The fragment and query parameters support type-specific extraction based on file suffix. The tools know what kind of file they're working with and offer operations native to that type:

```
# Images (jpg, png, webp)
read("moo://Issue_0/evidence/frames/frame-000-t0.jpg?crop=100,200,300,400")   → cropped region
read("moo://Issue_0/evidence/frames/frame-000-t0.jpg?scale=0.5")              → half-size
read("moo://Issue_0/evidence/frames/frame-000-t0.jpg?scale=320x240")          → specific dimensions
read("moo://Issue_0/evidence/frames/frame-000-t0.jpg?region=face_0")          → crop to annotation bbox
read("moo://Issue_0/evidence/frames/frame-000-t0.jpg?format=png")             → convert format
read("moo://Issue_0/evidence/frames/frame-000-t0.jpg?blur=faces")             → dynamic face blur

# Video (mp4)
read("moo://Issue_0/evidence/video/clip-10s.mp4?frame=3.5")         → extract frame at 3.5s
read("moo://Issue_0/evidence/video/clip-10s.mp4?clip=2.0,5.0")      → extract subclip 2s-5s
read("moo://Issue_0/evidence/video/clip-10s.mp4?thumbnail")         → representative frame

# CSV
read("moo://Issue_0/data/detections.csv#confidence")                → column as array
read("moo://Issue_0/data/detections.csv?where=confidence>0.8")      → filtered rows
read("moo://Issue_0/data/detections.csv?sort=timestamp&limit=10")   → sorted, limited

# YAML/JSON (fragment paths, as above)
read("moo://Issue_0/ALERT.yml#severity")                            → "info"
read("moo://Issue_0/ALERT.yml#payload/camera_name")                 → ""
```

The suffix determines what operations are available. `?crop`, `?scale`, `?region`, `?blur` are image operations. `?frame`, `?clip` are video operations. `?where`, `?sort` are tabular operations. `#key/path` is structural navigation (YAML/JSON/CSV column). Query parameters (`?`) are transformations; fragments (`#`) are navigation.

### File editor protocol (pluggable techniques)

Editing files under moo URLs should be robust and self-documenting. Instead of one ad-hoc edit style, a **file editor protocol** defines a plugin surface: each file type (or family) can register edit techniques that know how to read a target region and apply an operation. The agent (or orchestrator) can list available techniques for a URL and then call a single `edit(target, operation, payload)` that the plugin implements.

- **Plugin interface:** `describe()` (capabilities, file suffixes, operations), `read_region(content, target)`, `apply(content, operation, payload)`.
- **Target:** Same as read — moo URL with optional fragment (key path, line range, or type-specific: cell range, CSS selector).
- **Documented techniques (examples):** YAML path (set/merge), JSON path (set/delete), line range (replace/insert/delete), spreadsheet (cell/range/row), HTML (selector replace), regexp (search-replace with optional scope). See **EDIT-PROTOCOL.md** in this skill for the full plugin surface and example capability records. Implementations are not required all at once; the protocol and documented examples define the contract so that orchestrators and moo can add plugins incrementally (e.g. YAML + line range first, then JSON, then others).

Write operations are also type-aware:

```
write("moo://Issue_0/evidence/frames/frame-003.jpg?scale=640x480", <raw image>)  → scale on write
write("moo://Issue_0/evidence/frames/frame-003.jpg?annotate", <annotation json>) → draw annotations
```

This means an agent can say "show me the face region from frame 0, scaled to 320x240" in a single read call. The orchestrator handles the image processing, the branch access, and the caching. The agent gets pixels back.

**The agent doesn't know or care** whether it's reading a local file, a moo branch, or a value inside a YAML file on a remote repo. The URL scheme handles routing, mounting, parsing, type-aware extraction, and git operations. The tools are the same tools. The namespace is the abstraction.

## MOOLLM interface (per moocroworld)

Every moocroworld has at minimum:

| File | Purpose |
|------|---------|
| `GLANCE.yml` | 5-line summary. Always read first. |
| `CARD.yml` | Machine-readable overview with links to everything. |
| `INSTANCE_DATA.yml` | Skill instance data, named by skill (e.g. `ALERT.yml`, `CHARACTER.yml`). ALL_CAPS convention. |

Recommended: `README.md` (human-readable narrative, auto-generated). Optional: `evidence/`, `actions/`, `analysis/`, `data/` — whatever the object type needs.

The semantic image pyramid (GLANCE → CARD → full data) works per-branch. A crow landing on a branch reads GLANCE first. If it needs more, CARD. If it needs the full state, the instance data file.

## Crows (agents)

Agents that fly between branches are called crows. They are intelligent, social, persistent, and they use tools.

| Crow type | Examples |
|-----------|---------|
| Human | Reviewer, editor, admin — acts via UI, GitHub, or CLI |
| LLM | Vision model, reviewer agent, analysis agent |
| Bot | GitHub bot, webhook handler, automation script |
| System | Alert server, orchestrator, pipeline |

A crow's lifecycle on a branch:

1. **Land** — Read GLANCE → CARD → specific files as needed.
2. **Act** — Add evidence, run analysis, approve/reject, update state.
3. **Commit** — Write changes to the branch (new files, updated GLANCE/CARD).
4. **Fly** — Move to the next branch (or return to the main world).

A crow never nests permanently on one branch. It visits, acts, and moves on.

## GitHub integration

When the repo is on GitHub, a moocroworld branch can be paired with a GitHub Issue. The issue is the conversation layer (comments, labels, notifications); the branch is the data layer (structured files, images, analysis). They complement each other:

- Issue body generated from the branch's README.md.
- Issue comments correspond to branch `actions/` entries.
- Issue labels track state (severity, review status).
- A bot watches issue comments for commands and commits to the branch.
- Webhooks sync actions between the issue and the branch in both directions.

## Applications

### Leela Alerts (first application)

Alert events stored as `Issue_` branches in `leela-ai/leela-alerts`. Each alert is a moocroworld with `ALERT.yml`, evidence (video frames, dashboards), analysis (vision/LLM, human reviewer), actions (approve, reject, escalate, resolve), and delivery log. `Issue_0` is the prototype alert — the null alert, the schema-as-example.

Design: `leela-ai/central` `apps/alerts/doc/ALERTS-NODE-POSTGRES-DESIGN.md` §13.

### Other candidates

- **Adventure characters** — each character as a `Character_` branch with their own soul file, inventory, history, mind mirror.
- **Chat sessions** — `Session_` branches archiving complete conversations with context.
- **Experiment runs** — `Experiment_` branches with parameters, results, analysis.
- **Model versions** — `Model_` branches with weights metadata, training data references, evaluation results.

## Batch glance and stare (attention focus tree)

GitHub-as-object-filesystem: many branches across many repos form a set of **mooniverses**. The LLM (or any consumer) can **batch glance** — fetch GLANCE.yml from many branches at once — or **stare** — fetch a configurable depth of content per branch using an **attention-tree overlay**.

The overlay is a YAML file that defines, per repo (and optional branch type filter): **depth** (how deep to drill), **at_depth** (which files or globs at each level), and **fragments** (which key paths or line ranges to extract from those files). Like an outliner: you choose how much to expand at each level. Change the overlay to refocus attention without touching the branches.

- **moo batch-glance** [repo] [--type X] — GLANCE.yml for each branch; add **--all** to run across all configured repos.
- **moo focus** [overlay.yml] — Load overlay; for each repo/type list branches; for each branch fetch content by depth and at_depth; apply fragments; print combined view (-o json for machine output).

See **ATTENTION-TREE.md** for the overlay format and **ATTENTION-TREE.example.yml** for an example.

## Part of MOOLLM

- Repository: https://github.com/leela-ai/moollm
- Skills index: `skills/INDEX.yml`
- Related skills: room, incarnation, mooco, adventure, object, yaml-jazz, k-lines, society-of-mind
