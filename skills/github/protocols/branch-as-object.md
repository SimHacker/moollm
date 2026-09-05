# Branch-as-Object — Versioned Non-Code Storage in Git

> Store an object with filesystem history in a repo by giving it its own branch named `type_id`.

Git is accidentally an excellent key-value store for append-mostly objects with history. This is the
protocol for using it that way deliberately.

**The branch IS the object.** Its history is the object's audit log, its HEAD is the object's current
state, and deleting it tombstones the object.

## The one-paragraph summary

Pick a type name (`cursor`, `character`, `issue`, `alert`, `run`, `ticket`, `review`). Pick an id
unique within that type (numeric, UUID, slug). Create a git branch named `type_id` off an **empty
root** — `git switch --orphan` — so the object's tree shares no history with your code. Store the
object's state as files on that branch. Every state change is a commit. Delete the branch to
tombstone the object.

## Why this works

Git already is:

- A **content-addressed store** — dedupe is free; identical object states across branches share blobs
- A **DAG with refs** — a branch ref is exactly "pointer to the latest version of this object"
- **Distributed** — every clone holds the full history; a forge is just a synchronization hub
- **Review-aware** — PRs let you review a *state change* with the same rigor as a code change
- **Tooling-rich** — diff, blame, log, grep, patch, cherry-pick, and bisect all apply to object
  history for free

Costs, stated up front:

- Branches are effectively free (refs are tiny, blobs are deduped)
- **Cross-object queries are expensive.** This is not a database with indexes — see
  [Querying](#querying-across-branches-when-you-need-it)
- Concurrent writers on one branch need the same merge discipline as code, which is usually fine
  because each object has a single conceptual owner

## Naming convention: `type_id`

| Field | Convention | Examples |
|---|---|---|
| `type` | **lowercase**, singular, matches the object type | `cursor`, `character`, `issue`, `alert`, `run`, `ticket` |
| `id` | unique **within the type**; numeric, UUID, or slug | `42`, `a7b2c3d4`, `che7-2026-03-occupancy` |

Because ids are scoped per type, `cursor_1` and `issue_1` are different objects and each type mints
ids without coordinating with any other. **A repo therefore holds many types at once — it is a
polymorphic container**, not a place to keep one kind of thing.

### Three naming rules that are not cosmetic

**Use lowercase.** Loose refs are literal files under `.git/refs/heads/`, so on macOS and Windows —
case-insensitive filesystems — `Issue_1` and `issue_1` are **the same ref**. A single-case convention
makes that collision unrepresentable; a mixed-case one fails silently and per-platform, which is the
worst way to fail. Deployments predating this rule use PascalCase or UPPERCASE (`Issue_<id>`,
`ALERT_<n>`) and still work — the hazard is *mixing* conventions in one repo, not any single choice.

**Use an underscore, never a slash or dash.** Two independent reasons. Ids routinely contain dashes
(UUIDs, slugs), so `_` is the only separator that splits `type` from `id` unambiguously. And git refs
are *paths*: a ref cannot also be a directory of refs, so adopting `cursor/1` permanently burns
`cursor` as a usable ref name and makes `refs/heads/cursor/1` versus `refs/heads/cursor/1/notes` a
hard conflict the first time you want a sub-ref. Underscores keep the namespace flat.

**Sanitize ids.** Ref names cannot contain spaces, `..`, `~`, `^`, `:`, `?`, `*`, `[`, or end in
`.lock`.

## File layout inside the branch

Each `type_id` branch is a tiny filesystem scoped to one object:

```
type_id/                    ← branch root
├── README.md               ← what this object IS; pointer to its type docs
├── TYPE.yml                ← canonical state (YAML Jazz preferred)
├── <object>.md             ← human narrative (optional)
├── attachments/            ← binary artifacts
└── history.md              ← notable state changes (optional — git log also has it)
```

Keep paths consistent across all instances of a type so scripts can iterate. For very lightweight
objects, a single `<id>.yml` at the root is enough.

## The MOOLLM binding: type resolves to a skill

This is what makes the pattern more than a storage trick in MOOLLM. **The type prefix is a pointer to
a prototype.** `cursor_*` resolves to `skills/cursor/`, `character_*` to `skills/character/`, and the
instance inherits its schema, behavior, and permissions from there.

It is the same discipline as [`file-system-object`](../../file-system-object/): in the filesystem a
*directory* exports interfaces declared by its UPPERCASE marker files, and the branch root does
exactly that in ref space. An `ALERT.yml` at a branch root means "this branch exports the ALERT
interface," and the branch *name* encodes both the interface and the instance id. Same grammar,
different storage backend — only the substrate changes.

## Lifecycle

| Operation | Command |
|---|---|
| **Create** | `git switch --orphan type_id; <create files>; git add .; git commit; git push -u origin type_id` |
| **Create** from template | `git switch -c type_id origin/type_template` |
| **Read** current state | `git fetch; git switch type_id; cat TYPE.yml` |
| **Update** | switch → edit → commit → push |
| **History** (audit log) | `git log type_id` |
| **Diff** two states | `git diff type_id@{yesterday} type_id` |
| **List** all of a type | `git branch --list 'type_*'` |
| **Tombstone** | `git push origin --delete type_id` (recoverable from reflog until GC) |
| **Revive** | recreate the branch from reflog or the last known commit SHA |

> `git switch --orphan` (git ≥ 2.23) starts from an empty index. The older
> `git checkout --orphan` inherits the current index, so it needs `git rm -rf .` immediately after.

## Integration with issues and PRs

- **Name an `issue_<id>` branch to match a real issue number.** The issue is the discussion; the
  branch is the versioned artifacts.
- **PRs into a `type_id` branch** make state changes peer-reviewable — the same rigor you apply to
  code, applied to data.
- **Link the branch from the issue body** for cross-navigation.

## Querying across branches (when you need it)

The pattern is append-mostly and per-object. Be clear about what is cheap:

- **Listing is cheap.** `git branch -a --list 'type_*'`, or the forge's branches API.
- **Field scans are not.** Checking *which objects are in state X* means fetching each branch and
  scanning its canonical file — a linear walk, not an index.
- **Graph queries: use a real database.** The pattern comfortably handles thousands of objects per
  type. It does not handle millions.

Empirical ceiling: around 10k branches per repo before forge UIs and `git clone` feel slow. Split by
month or subtype past that.

## When to use this pattern

**Good fits:** low write rate (seconds between commits, not milliseconds) · per-object audit history
is valuable · state changes benefit from PR review · a single conceptual owner per object · the
object is code-adjacent enough that living in a repo makes sense.

**Bad fits:** high write rate · heavy cross-object relational queries · many-writer contention on one
object (use a CRDT or a database) · very large per-object blobs (git dislikes individual files over
~100 MB — use LFS or external storage with pointers).

## Relation to schemapedia

Schemapedia's [`github` mechanism](../../schema/schemas/mechanisms/github/) names this pattern and
delegates the model rather than duplicating it; the [`git`
mechanism](../../schema/schemas/mechanisms/git/) describes the underlying content-addressed DAG.
**This document is that delegation's destination** — the theory is in schemapedia, the protocol is
here, and operational specifics belong in whichever repo is operating it.

## Recipes

### Create a `ticket_42` object from scratch

```bash
git switch --orphan ticket_42
mkdir -p attachments
cat > TICKET.yml <<'EOF'
id: 42
type: ticket
title: "Occupancy threshold exceeded"
severity: warning
created: 2026-04-24T12:00:00Z
state: active
EOF
cat > README.md <<'EOF'
# ticket_42 — Occupancy threshold exceeded

See TICKET.yml for canonical state. This branch's history is the audit log.
EOF
git add .
git commit -m "create ticket_42 from threshold breach"
git push -u origin ticket_42
```

### Update its state

```bash
git fetch && git switch ticket_42
# edit TICKET.yml — state: active → acknowledged
git commit -am "acknowledge ticket_42"
git push
```

### List every object of a type

```bash
gh api /repos/<org>/<repo>/branches --paginate \
  | jq -r '.[].name | select(startswith("ticket_"))' | sort
```

### Scan state across all objects of a type

```bash
for branch in $(gh api /repos/<org>/<repo>/branches --paginate \
                  | jq -r '.[].name | select(startswith("ticket_"))'); do
  state=$(gh api "/repos/<org>/<repo>/contents/TICKET.yml?ref=$branch" \
            -H 'Accept: application/vnd.github.raw' | yq -r .state)
  echo "$branch: $state"
done
```

Reading a single file per branch through the contents API avoids checking anything out — the
cheapest form of the linear walk, but still linear.

### Tombstone when resolved

```bash
git tag "ticket_42-final" ticket_42     # keep the final state discoverable
git push origin "ticket_42-final"
git push origin --delete ticket_42
```

## Open questions

1. **Template branches.** Should each type have a `type_template` branch that instances fork from?
   Standardizes initial layout; costs a branch per type.
2. **Tombstone convention.** Delete the branch, or merge into a `type_archive`? Delete is cleaner but
   irreversible; archive preserves everything and makes listing noisier. Tagging the final state
   before deletion is the compromise used above.
3. **Cross-repo references.** Store the target's commit SHA as a field — which is the same
   `(remote, commit, path, anchor)` permalink used by
   [reading cursors](../../../designs/webtop/CURSOR-STORAGE.md), and it dangles the same way if the
   target rewrites history.
4. **Multi-writer safety.** Normal git conflict resolution applies; not a problem for single-owner
   objects.
5. **Create is the missing verb in `moo`.** See below — everything else is implemented.

## Tooling status: what `moo` already does, and the one gap

The [`moo` CLI](../../moo/) ([`skills/moocroworld/`](../../moocroworld/) holds the repo registry and
overlays) is a working implementation of this protocol — roughly 1000 lines of Python under
`skills/moo/lib/` with a test suite. It operates entirely through `gh api` against the REST API and
never touches a local checkout, so nothing needs to be cloned to read or write an object.

| Verb | Command | Notes |
|---|---|---|
| List objects of a type | `moo ls --type <type>` | the prefix type-query, implemented |
| List an object's files | `moo tree` | |
| Read state | `moo read` | accepts `repo/branch/path` or a `moorl` URL, and can index into YAML/JSON with a slash path |
| Read at a resolution | `moo glance` · `moo card` · `moo sniff` | the semantic pyramid, per object |
| Scan a field across objects | `moo scan` · `moo batch-glance` | the linear walk from [Querying](#querying-across-branches-when-you-need-it), automated |
| Update state | `moo write` | Contents API `PUT`, handles the existing-blob SHA |
| Tombstone | `moo rm` | deletes the ref |
| Resolve a `moorl` | `moo resolve` | `moo://` / `moollm://` → components |

**The gap: there is no `moo create`.** You can write into an object that exists and delete one, but
nothing mints a new one — which also means nothing in the toolchain creates an *orphan* branch, the
one step this whole protocol depends on.

It is a small gap with a non-obvious implementation, which is probably why it is still open. The
Contents API cannot do it: `PUT /contents/{path}` requires the branch to already exist. Creation has
to go through the Git Data API, and the orphan-ness is one field:

```
POST /repos/{owner}/{repo}/git/trees     → tree_sha        (omit base_tree)
POST /repos/{owner}/{repo}/git/commits   → commit_sha      with "parents": []   ← the orphan part
POST /repos/{owner}/{repo}/git/refs      → refs/heads/type_id pointing at commit_sha
```

An empty `parents` array is what makes it a root commit, so the object's tree shares no history with
`main` — the API equivalent of `git switch --orphan`, without needing a working copy at all.

## Known deployments

| Repo | Type | Branch | Stores |
|---|---|---|---|
| `leela-ai/leela-alerts` | `Issue` | `Issue_<id>` | per-alert state, evidence, query results |
| `leela-ai/leela-alerts` | `ALERT` | `ALERT_<n>` | alert definition + evolution |
| reading cursors | `cursor`, `character` | `cursor_<id>` | position, inventory, path — [CURSOR-STORAGE.md](../../../designs/webtop/CURSOR-STORAGE.md) |

## References

- [`skills/file-system-object/`](../../file-system-object/) — the same interface grammar in
  filesystem space; this is its git-branch backend
- [schemapedia `github` mechanism](../../schema/schemas/mechanisms/github/) — structural ancestor
- [schemapedia `git` mechanism](../../schema/schemas/mechanisms/git/) — the underlying VCS model
- [CURSOR-STORAGE.md](../../../designs/webtop/CURSOR-STORAGE.md) — an application, with the
  storage-repo / location-repo split
- Pro Git, §3 "Branching" — <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>
