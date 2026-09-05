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

  - src: file:///Users/don/skills-dev
    at:  /skills/local
    mode: rw
    over: /skills/moollm        # union: this wins on collision
```

Three properties do most of the work:

**Pinned or live.** `@sha` is immutable and cacheable forever; `@branch` follows updates and needs
invalidation. Same split as [the two URL
forms](webtop/CURSOR-STORAGE.md#the-url-is-the-canonical-name--but-store-its-parts-not-the-string),
for the same reason, invalidated by the same webhook. A reproducible session pins everything; a
working session does not.

**Any subtree, cheaply.** `@sha:/designs/webtop` resolves to a tree object, so mounting a subdirectory
costs no more than mounting a repo, and never requires a clone. This is git being genuinely better
suited to the job than a filesystem: subtrees are already first-class addressable values.

**Write mode is declared, not inferred.** `ro` is the default. `rw` maps writes back to `moo write`
on that branch. `cow` buffers writes in a scratch overlay for later commit — the same
[buffer-and-checkpoint](webtop/CURSOR-STORAGE.md#postgres--github-not-bidirectional-sync-which-is-the-trap)
discipline, one layer down. A pinned mount **cannot** be `rw`, because there is nothing to write to;
that is a constraint, not a policy.

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

**Write ambiguity in unions.** If two mounts cover a path and one is `rw`, a write is unambiguous; if
both are, it is not. Declare exactly one writable layer per union or refuse the write. Guessing here
produces edits that land in the wrong repo and are found much later.

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
