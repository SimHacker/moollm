# MOOFS Namespace: bind mounts, typed object mounts, and `/proc`

**Status:** Design. Nothing here is implemented; `moo` ships the transport it would sit on (see
[status](#status-what-exists-and-what-does-not) at the bottom, and do not read past it as a shipped
feature).
**Companions:** [MOOFS-DESIGN.md](MOOFS-DESIGN.md) — overlay resolution ·
[MOOCO-MOO-VM.md](MOOCO-MOO-VM.md) — composition ·
`mooco/designs/MOOCO-REPOS.md` — repo model (private repo)

---

## Two primitives, and MOOFS only has one

[MOOFS-DESIGN](MOOFS-DESIGN.md) specifies a **layer stack** — ambient over room over character over
shadow over working over upstream over base, top wins. That is an *overlay*, and it answers exactly
one question:

> **Overlay:** many sources, one path. *Which version of this file do I get?*

It cannot express the other question, which is the one being asked here:

> **Bind:** one source, one path, placed anywhere. *Where in the tree does this subtree appear?*

The layer stack is a total order over whole repos, fixed at configuration time. A bind mount is a
placement of an arbitrary subtree at an arbitrary point, made and unmade at will. Docker's `-v` is a
bind; Plan 9's `bind`/`mount` is the same primitive with union semantics folded in, and is the right
thing to steal from — the union flags are how the two primitives compose.

**They compose cleanly and both are needed:** binds build the tree, overlays resolve collisions
inside it. Everything below is the missing bind half.

---

## A mount is `(repo, ref, subpath) → mountpoint`

```yaml
mounts:
  - src: github://SimHacker/moollm@main:/skills
    at:  /skills/moollm
    mode: ro

  - src: github://SimHacker/moollm@a1b2c3d:/designs/webtop   # pinned to a commit
    at:  /ref/webtop
    mode: ro

  - src: github://SimHacker/moollm@main
    at:  /obj
    sparse:                     # sparse-checkout patterns, not one path
      - /skills/moo/
      - /designs/webtop/
      - '!**/node_modules/'

  - src: file:///Users/don/skills-dev
    at:  /skills/local
    mode: rw
    over: /skills/moollm        # union: this wins on collision
```

Four properties do most of the work:

**Pinned or live.** `@sha` is immutable and cacheable forever; `@branch` follows updates and needs
invalidation. Same split as [the two URL
forms](webtop/CURSOR-STORAGE.md#the-url-is-the-canonical-name--but-store-its-parts-not-the-string),
for the same reason, invalidated by the same webhook. A reproducible session pins everything; a
working session does not.

**Any subtree, cheaply.** `@sha:/designs/webtop` resolves to a tree object, so mounting a subdirectory
costs no more than mounting a repo, and never requires a clone. This is git being genuinely better
suited to the job than a filesystem: subtrees are already first-class addressable values.

**Sparse selection, not one path.** A mount takes a **sparse-checkout pattern set**, so you pick and
choose exactly which files and directories appear. Git's two matching modes have a real cost
difference worth inheriting rather than hiding: **cone mode** is directory-level and matches by
prefix, so it stays cheap on large trees; **pattern mode** takes full gitignore-style globs and must
test every path. Default to cone, allow patterns, and say which one a mount is using — an
accidentally non-cone mount over a big repo is a silent performance cliff.

**Write mode is declared, not inferred.** `ro` is the default. `rw` maps writes back to `moo write`
on that branch. `cow` buffers writes in a scratch overlay for later commit — the same
[buffer-and-checkpoint](webtop/CURSOR-STORAGE.md#postgres--github-not-bidirectional-sync-which-is-the-trap)
discipline, one layer down. A pinned mount **cannot** be `rw`, because there is nothing to write to;
that is a constraint, not a policy. What happens when you write *through* a union is
[below](#writeback-copy-up-whiteouts-and-where-new-files-land).

---

## Typed object mounts: the layout is the tagsonomy

A [`type_id` branch](../skills/github/protocols/branch-as-object.md) mounts as an object, and the
mountpoint carries the type:

```
github://SimHacker/objects@cursor_a3f9:/   →   /obj/cursor/a3f9/
github://SimHacker/objects@room_library:/  →   /obj/room/library/
```

Two things fall out of that path shape. `/obj/cursor/` is **browsable without a query** — `ls` is the
type index, so the projection is a speedup and never a dependency. And the container infers the type
of its children, which is the constitution's rule about
[plural directories](../.cursorrules) holding instances of their singular skill, arrived at from the
other direction: here the *mount table* is what enforces it.

The type binding resolves against `main` — `main:/types/cursor/SKILL.md` says what MOOLLM does with
anything under `/obj/cursor/`. Mounting an object of an unknown type is allowed and inert: you get
files, no behavior, and a warning naming the missing type directory.

---

## Gitmapping: the namespace is `mmap` and reading is the page fault

The [Postgres projection](webtop/CURSOR-STORAGE.md#main-is-the-type-registry-and-the-url-is-the-join-key)
gets a mountpoint too, and once it does the shape of the whole system becomes familiar:

| MOOFS | Virtual memory |
|---|---|
| mount table | address space |
| `ls`, query, index hit | consulting the page table — cheap, no I/O |
| reading a file | **page fault** → fetch from git → cache |
| pinned `@sha` cache entry | clean page, never needs re-fetch |
| token cost | the actual cost of paging in |

"[Mounting is not loading](#the-mount-table-is-the-context-manifest)" is precisely *mapping is not
paging in*. Map ten thousand objects for free, touch four. The index exists so you can decide
**whether** to fault, and that decision is where all the leverage is: a predicate over 10,000 objects
is one SQL query instead of 10,000 API reads, which is the difference between a feasible operation
and an impossible one.

**Memory-mapping to git instead of RAM** — *gitmapping*, and the name is doing real work, because git
already implements most of it:

```bash
git clone --filter=blob:none --sparse   # trees and commits now; blobs on touch
```

**Partial clone** defers blob download and fetches from the promisor remote on access. **Sparse
checkout** selects which paths materialize. Together that *is* demand paging, with the remote as
backing store, shipped and battle-tested at scale. So the honest scope is narrow and much more
achievable than it first sounds:

> MOOFS supplies **naming and policy** — where a tree appears, which layer wins, what is writable.
> Git supplies the **paging**.

Which also means the fallback is not a rewrite. A gitmapped mount can always be materialized as a
real partial-clone worktree on disk and handed to a compiler, an editor, or a shell — the same
[MOOT reification](#status-what-exists-and-what-does-not) idea, now with a mechanism.

### Two ways in: by name and by predicate

`/obj/` is the by-name index and needs no query at all — `ls /obj/cursor/` is already the type
listing. Queries get the Plan 9 `/net` idiom, because it keeps query syntax out of pathnames:

```
/q/clone                    read it → allocates /q/7/, returns "7"
/q/7/ctl                    write the query here
/q/7/results/               ls the matches; each entry is a bind into /obj/<type>/<id>/
/q/7/status                 rows, ms, index used, and index lag
```

**Results are binds, not copies.** A result entry *is* the object mount, so navigating into a hit
navigates the real object and the bytes arrive on read. No new mechanism — the
[bind primitive](#a-mount-is-repo-ref-subpath--mountpoint) already does it.

**Results are pinned.** The query captures each object's `head_sha` and binds at that commit, so the
result set is a consistent snapshot and reading it twice gives the same bytes. Which means a saved
search is literally a [`namespace_<id>` object](#the-mount-table-is-the-context-manifest): a list of
pinned mounts, versioned and shareable. Searching and context-assembly turn out to be the same
operation.

Writes do not go through `/q/`. It is read-only; edits go to the object mount, which is the
[write-through path](webtop/CURSOR-STORAGE.md#postgres--github-not-bidirectional-sync-which-is-the-trap).

### Making "speedup, not dependency" checkable at runtime

The architecture guarantees the projection is rebuildable. It does **not** guarantee the projection is
*current*, and a filesystem is very good at hiding the difference — twelve entries in a directory
look equally authoritative whether the index is three seconds or three days behind. Three things have
to be surfaced or the guarantee is decorative:

- **Lag, always.** `status` reports per-type last-indexed position against branch heads. An answer
  from a stale index is still useful; an answer from a stale index *presented as current* is a
  fabrication with a directory listing for evidence.
- **Empty is two different answers.** "No rows" and "no rows, index current, type covered" must not
  render identically, or the model concludes something false from an indexing gap. Absence of
  evidence is the failure mode LLMs are worst at catching, so `/q/` must never report a bare zero.
- **Verify escapes to git.** A flag that re-runs the predicate against branch heads, slow and
  authoritative. Without it, "you could always check git" is a claim nobody can execute.

**And the index can outlive the data.** Deleted branches, force-pushes, and GC'd commits leave result
entries pointing at objects that no longer resolve — the [dangling-permalink
problem](webtop/READING-CURSORS.md#the-cursor-is-a-permalink-remote-commit-path-anchor) arriving
through search instead of through a bookmark. Detect it at page-in, report the miss with the commit
that vanished, and never silently drop the row: a result that quietly shrinks is worse than one that
reports damage.

---

## Writeback: copy-up, whiteouts, and where new files land

Writing through a union should work wherever it means anything, and the cases where it means
something are enumerable. All three mechanisms are overlayfs's, already solved, and worth taking
rather than reinventing.

| You write to | What happens |
|---|---|
| a file in a `rw` layer | write to that layer's branch. Unambiguous, the common case. |
| a file resolved from a lower `ro` layer | **copy-up**: copy into the topmost writable layer covering that path, then modify. The file now exists twice and the top wins. |
| a new file | lands in the topmost writable layer whose mount covers the path — the most local layer, as Don says. |
| a delete of a lower-layer file | **whiteout**: a tombstone in the upper layer that masks the lower entry. A union delete is a masking record, not a delete. |
| anything under a pinned mount | refused; copy-up is the only route. |

Layer order resolves the ambiguity, and it is **list order, declared as significant** — with
`/proc/self/whence` reporting which mount actually won, because an order you can only infer from
behavior is not an order anyone can debug.

Two placement rules keep the edge case from becoming a bug. If **no** writable layer covers the path,
fail loudly rather than inventing a home; a write that lands somewhere plausible is discovered weeks
later in the wrong repo. If **two** writable layers cover it, require an explicit target instead of
picking by ordinal — tie-breaking is right for reads and wrong for writes.

### The cost that is not an edge case

Copy-up **silently forks content**. You edit what looks like the upstream file, get a private copy in
your local layer, and from that moment upstream changes stop reaching you at that path — invisibly
and permanently. In a container that is fine, because the image is meant to be frozen. Here it is
corrosive, because the entire value of the arrangement is that upstream keeps flowing.

So a copy-up is not a silent side effect. It records its provenance — source layer, source commit,
the bytes it forked from — which makes two things possible that are otherwise impossible: a
**divergence report** (your copy-ups whose sources have moved, and the diffs you are now missing) and
a **rebase** of a copy-up onto the current upstream. Without that record, a union filesystem over
live repos quietly becomes a stale private fork of everything you ever touched.

And whiteouts committed into a git layer are real files that mean nothing outside the union. They
travel with the branch, confuse anyone reading it directly, and want a naming convention obvious
enough to be ignorable.

---

## `/proc`: introspection with no new verbs

The reason to make the namespace visible as files rather than as a tool API is narrow and practical:
**the LLM already has read, write, and ls.** Every capability expressed as a path is a capability
that needs no new tool, no new schema, and no retraining on a bespoke call signature. A mount API
adds a verb. A writable `/proc` file adds none.

```
/proc/self/ns.yml          # the mount table — read it, write it, that IS mounting
/proc/self/cursor.yml      # where am I: (repo, commit, path, anchor)
/proc/self/context.yml     # what is loaded, with token costs
/proc/self/whence?path=…   # which mount produced this file, and at which commit
/proc/objects/             # mounted objects, by type
/proc/types/               # types resolvable from main, and which are missing
/proc/index.yml            # index lag per type, and whether /q/ can be trusted right now
```

The load-bearing one is the first. **Writing to `/proc/self/ns.yml` is how you mount**, so the whole
namespace-manipulation surface is one file that the model reads, edits, and writes back — an ordinary
edit of an ordinary YAML file. Unmounting is deleting a list entry. This is the
[magic dictionary](MOOFS-DESIGN.md#the-magic-dictionary-pattern) pointed at the namespace itself, and
it is the same argument as [homoiconicity](object-system/HOMOICONICITY.md): the configuration is in
the substrate the tools already manipulate, so no second mechanism exists to learn or to keep in sync.

`whence` earns its place because of a real hazard — see costs.

---

## The mount table is the context manifest

The namespace is `(repo, ref, subpath, at, mode)` tuples, which means it is **data, small, and
serializable**. That has consequences worth naming, because they are the actual payoff:

- **A session's world is reproducible.** Pin every ref and the namespace replays exactly. This is
  [the cursor permalink](webtop/READING-CURSORS.md#the-cursor-is-a-permalink-remote-commit-path-anchor)
  generalized from one position to a whole world.
- **A namespace is itself an object.** `namespace_<id>` on a branch, versioned, diffable, PR-able.
  Handing someone your working context becomes handing them a branch name.
- **Per-agent namespaces make mounting safe.** If the table is global, two agents fight over the
  tree. If each cursor or character owns one, mounting is a private act — and a cursor with mounts in
  several repos at once is literally [the worm with limbs in different
  substrates](webtop/READING-CURSORS.md#a-selection-is-a-cursor-with-width), with the mount table as
  its limb roster.

**And mounting is not loading.** A mount costs one line of YAML; only reading costs tokens. The
namespace can therefore be large and speculative without any context penalty, which is the property
that makes free mounting and unmounting affordable in the first place. Mount everything plausible,
read almost none of it.

---

## Honest costs

**Union provenance is genuinely hard, and matters more here than in Plan 9.** When a path resolves
through overlapping mounts, "where did this text come from" stops being obvious — and for an LLM,
provenance is not a debugging nicety, it is the difference between a citation and a fabrication. The
mitigation is that resolution must be *recorded*, not reconstructible: every read carries its
originating mount and commit, and `/proc/self/whence` is the query. Any resolution path that cannot
answer it is a bug.

**This is a resolver, not a kernel mount.** The namespace exists only for callers that go through
MOOFS. A shell command, a `cat`, or any tool reaching the real disk sees the real disk and knows
nothing about `/obj/cursor/a3f9/`. That leak is permanent short of FUSE, and the honest framing is
that MOOFS paths are a *convention the tools honor* — which is worth saying plainly given that the
MOOCO repo model doc has already had to delete one round of design fiction on exactly this subject,
after a 3400-line spec described a mount layer that did not exist.

**Live mounts multiply staleness.** Twenty `@branch` mounts are twenty things that can move under you
mid-session. Pinning fixes it and costs currency; the default should probably be pin-on-first-read,
so a session is internally consistent even when nobody thought about it.

**Write ambiguity and silent forking.** Union writes have real hazards — ambiguous placement, and
copy-up quietly detaching a file from upstream forever. Both are handled
[above](#writeback-copy-up-whiteouts-and-where-new-files-land); the second is the one that does not
announce itself.

---

## Status: what exists and what does not

| Piece | Status | Where |
|---|---|---|
| Remote branch read/write/ls/tree transport | **ships** | `skills/moo/` (`ls`, `tree`, `read`, `write`, `rm`, `sniff`, `glance`, `focus`, …) |
| `moorl` URL parsing (`moollm://repo/branch/path`) | **ships** | `moo resolve` |
| Branch-as-object convention | **ships** (spec) | [protocols/branch-as-object.md](../skills/github/protocols/branch-as-object.md) |
| Overlay layer stack | design | [MOOFS-DESIGN.md](MOOFS-DESIGN.md) |
| Local repo registry | stub | `mooco/apps/mooco/src/lib/workspace.ts` |
| **Bind mounts, typed object mounts, `/proc`** | **design — this document** | — |

The gap between `moo read` and a mount is smaller than it looks: `moo` already resolves
`(repo, branch, path)` and caches. A mount table is a rewrite rule applied before that resolution.
The first honest increment is `/proc/self/ns.yml` as a read-only view of the existing workspace
config, which makes the namespace inspectable before it is manipulable.

---

## Related

- [MOOFS-DESIGN.md](MOOFS-DESIGN.md) — the overlay half
- [webtop/CURSOR-STORAGE.md](webtop/CURSOR-STORAGE.md) — branches as objects, git/Postgres bridge
- [skills/github/protocols/branch-as-object.md](../skills/github/protocols/branch-as-object.md) — the `type_id` convention
- [object-system/HOMOICONICITY.md](object-system/HOMOICONICITY.md) — why configuration lives in the substrate
