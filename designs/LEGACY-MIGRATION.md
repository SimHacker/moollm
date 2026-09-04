# Legacy migration: resurrection, then reimagination

> *A running instance is the only honest specification of current behavior.*

Extracted from a real migration plan for a decades-old web application.
The client, the product, the stack, and the measurements are deliberately
absent; what is kept is the reusable shape. Every heading below survived
contact with an app whose framework generation nobody ships anymore and
whose largest file nobody wanted to open.

## Two paths, and they are sequential

**Resurrection** — get the old thing running again, as-is, in a container.
Cheap, mechanical, no architecture decisions. Modern hosts no longer ship
the interpreter it needs, and that is fine: the container is the point, so
the host does not have to care.

**Reimagination** — inventory it, write down the data contract, rearchitect
against that contract.

Do not start the second without the first. Do not mistake the first for a
destination. Resurrection carries an unsupported stack forward indefinitely
on a base image that is already years stale; it buys exactly one thing, and
that one thing is decisive: a live instance you can ask questions of. A
rewrite is compared against something. Make sure that something runs.

Related: [ENDOSYMBIOSIS](object-system/ENDOSYMBIOSIS.md) — engulf a working
system without digesting it. Resurrection is engulfment. The organelle keeps
its own genome and its own language while the host absorbs what it learned.

## Phase 0: the contract is the data

Before any architecture question, find the seam. In the case that produced
this doc, three unrelated systems shared one database namespace — the app,
a billing subsystem, and an off-the-shelf CMS — separated only by a
table-name convention, with one ORM module reaching across all three.

That seam is the actual work. **Once every table has exactly one owner, the
rest is ordinary software.**

Deliverable: a written contract, per table — **owner, readers, writers**, and
which ORM classes touch it. That document is what lets a new server be
*verified* rather than hoped about.

Three things that make this more tractable than it sounds, worth checking for
in any legacy schema:

- **No stored procedures, triggers, or views.** The contract is pure tables,
  so it can be documented completely and verified by reading rows.
- **ORM conventions are discoverable and few.** A naming style, a couple of
  renamed tables, explicit column overrides on foreign keys. A modern ORM
  maps all of that declaratively without touching the schema.
- **A fixture corpus already exists.** A rewrite normally has to invent its
  test data. Old apps often ship a demo-data module. That is an inherited
  test corpus; treat finding one as a windfall.

## Subtract from the old app first

The instinct is to remove dead subsystems *from the existing app*, before any
rewrite, rather than simply declining to port them. That is the right order,
for four reasons:

1. **Subtraction compounds where addition does not.** Every module removed is
   100% of its rewrite cost saved, plus its share of the data contract, plus
   its tests, plus its documentation.
2. **The old app is its own test oracle.** Delete a subsystem and "does it
   still work" is answerable *today*, by a running instance. Decline to port
   it and the same question can only be answered much later by the rewrite,
   tangled with a thousand other changes.
3. **It makes the code readable while reading it is the whole job.** The
   giant controller file is the main obstacle to understanding the system.
   One obsolete subsystem can be a tenth of it.
4. **Each removal is one small revertible commit with no architectural
   commitment.** This work is useful even if the rewrite never happens, and
   it does not need the language question settled first.

Much has changed since old code was written. Other systems now handle
concerns the app grew its own implementations of. The honest move is to trim
what is obsolete rather than faithfully carry it forward.

## Three dispositions, not one

"Drop it" means three different things, and the distinction is where the
judgment lives.

**Erase** — remove entirely. No stub, no config key, no trace. For things
that will never come back and whose presence is pure confusion.

**Stub** — remove the implementation, keep a named seam. A module that still
exists, still gets called, and does nothing but say so clearly. For
capabilities that may return in modern form: the stub is where the modern
implementation lands, and its existence documents the intent without
pretending to fulfill it.

**Decapitate** — keep the logic that decides what *would* happen, remove only
the transport that makes it happen. The subtlest and the most valuable. The
decision "this user should be nudged today" is domain knowledge worth years
of tuning; the delivery API is a commodity. Keep the head, drop the legs.

Decapitation pays a bonus if the intent record persists: log the generated
payload before the send, and the intent stays **observable, testable, and
reconnectable with evidence about what would have been sent.** Watch for code
that already does this — a disable flag plus a branch that logs instead of
sending means the work is not "invent a decapitated mode," it is "make the
disabled path the only path, delete the transport half, and give that log
line structure the monitoring stack can count."

## Look for what already stopped running

The single finding that most changes scope: **the async backbone was not
running.** A scheduler with an empty body, a queue runner commented out, a
webhook batch inside `if False:`, and every cron timer disabled. Reminders
and scheduled jobs were simply not happening in production.

A rewrite does not have to preserve behavior that has already stopped. But
somebody must confirm the stoppage is **deliberate rather than an outage
nobody noticed.** Inventory first; that question is cheap to ask and
expensive to skip.

Corollary for secrets: if credentials were ever committed, deleting them from
`HEAD` does not remove them from history. They are **burned, not secret** —
revoke, do not tidy. And a privacy policy that mentions a removed feature is
not code; that edit needs a human, possibly a lawyer, not a global replace.

## Content is not state

The single biggest simplification available, and it is upstream of every
other decision.

Authored material — the program's steps, definitions, tips, copy, the
thousand content templates — gets installed into the database and read back
through an ORM on every render. **None of that is state.** It does not change
because a user did something; it changes because an author edited it. It is
source code wearing a database costume.

**The test for which side a thing belongs on: restore last month's backup.
Should this be last month's version, or today's?** Logs, selections, and
users must be last month's — that is state. Step text and definitions should
be today's — that is content, and content belongs in git.

The cost comparison is stark once named: rendering one page costs several SQL
round trips — the step, its branch, its tips, its copy — every time, for
content that never changes between deploys. **The database is not storing
this data so much as charging rent on it.**

Losing the ORM here is not a sacrifice; it is the point.

Related: [GIT-AS-FOUNDATION](GIT-AS-FOUNDATION.md) — files ARE state;
[kernel/DIRECTORY-AS-OBJECT.md](../kernel/DIRECTORY-AS-OBJECT.md) — the
directory tree is source of truth, JSON is a compiled artifact.

## Check whether it is half-built already

The strongest argument for content-on-disk is usually sitting in the repo.
Look for:

- Exported content files already committed, sometimes hundreds of kilobytes.
- `exportToJSON` / `importFromJSON` on the content classes — **a complete
  file⇄database round trip, already written and already exercised.**
- Spreadsheets in the tree: authoring already happens outside the database.
- Another subsystem in the same product that already reads compiled content
  from disk, in production, on the fast path.

When those exist, the migration is not "invent a format and hope." It is
**stop importing.** The authored content already lives in files; the database
copy is a redundant cache with worse tooling.

And it deletes a whole subsystem. The flow goes from

```
spreadsheet -> CSV -> import tool -> database rows -> ORM -> render
```

to

```
YAML in repo -> (bundle at build time) -> render
```

which removes the import/export machinery, the cloud-drive dependency, and a
large slice of the ops tooling.

## Flattened names are a directory tree in disguise

The variant mechanism was filename mangling. Real shape, sanitized:

```
EditAccountSettings_EmailDeliveryOptions_OptIn_getting-started_VARIANT.html
```

That is a five-level path with `_` standing in for `/`, and the variant
appended on the end. **These filenames are already directory paths** — the
hierarchy was flattened into the name because the system had nowhere else to
put it. And the encoding had already drifted inconsistent: `_VARIANT` in one
file, bare `VARIANT` in another. That is precisely the bug class a real
directory tree makes impossible.

So this is not replacing one convention with another. It is **undoing an
encoding** and letting the filesystem express what the filenames were
imitating:

```
programs/
  base/
    steps/getting-started/opt-in.yaml
    wiki/health-note/eating-out.md
    goals/hydration.yaml
  variant/                             # delegates to base
    wiki/health-note/eating-out.md     # overrides only this
```

## Prototype delegation, by directory

The semantics worth adopting are the old prototype ones — Self, LambdaMOO,
and the selfish-object idea that each object stores only **its own
differences** and delegates everything else upward. Here the parent chain is
the directory chain: a customer program is a directory containing nothing but
its diffs, and a lookup walks up until it finds a definition.

A variant becomes a directory with a handful of files instead of a hundred
name-mangled ones, and **"what did we change for this customer" becomes
`ls -R`.**

Two levels of override granularity, and the choice matters:

- **File-level replacement** — the whole file wins. Predictable, and "where
  did this come from" always has a one-word answer.
- **Key-level deep merge** — DRYer, but list semantics get ambiguous and
  provenance gets hard to trace.

Recommendation: **file-level by default**, with key-level merge only via an
explicit `_extends:` inside a file that asks for it. Deep-merge-everywhere
config systems fail the same way every time: nobody can answer why a value is
what it is.

Whichever is chosen, one tool is non-negotiable: **a resolver that prints the
delegation chain for any key.**

```
content explain variant steps/getting-started/opt-in.yaml
```

**Prototype systems are pleasant exactly as long as the delegation is
inspectable.**

Related: [SELF-ISH-INFLUENCES](SELF-ISH-INFLUENCES.md) ·
[MOO-HERITAGE](MOO-HERITAGE.md) · [skills/prototype/](../skills/prototype/) ·
[skills/file-system-object/](../skills/file-system-object/)

## Measure, do not assume

The performance objection to reading content from disk evaporates when
measured, so measure it before arguing about it. Count the files, sum the
bytes, time three passes (cold, warm, warm again).

Authored corpora — years of human writing — reliably land in the low
megabytes and read in milliseconds warm. Set that against several SQL round
trips *per page render* and the conclusion is not close.

The engineering that follows: read it once at boot, hold it in memory, serve
from RAM; in dev, re-read on mtime change. Precompile to a single bundle at
build time and the runtime cost rounds to one parse — or to nothing, if the
bundle is imported as a module and tree-shaken into the build.

## GitHub is the CMS — and teaching it is the point

The obvious objection to content-on-disk is that non-technical authors lose
the admin UI. The well-trodden answer is a small CMS that writes YAML and
opens a pull request. **Don't.** And the reason is not expedience.

Every capability the custom CMS would reimplement badly already exists and is
already excellent: edit a file in the browser with no clone and no command
line, see a line-by-line diff of exactly what changed, leave review comments
on a specific *sentence*, get an approval before it goes live, revert a bad
edit years later with the paper trail intact. No admin UI you build will
reach that — and the version you build is the one where **"who changed this
wording and why" has no answer**, which is the same question the database
could not answer either.

The rest of the argument is the call to action.

**Version control is arguably the single most useful skill an information
worker can have, and it is not a programming skill.** It is: *propose a
change, discuss it, accept it, keep the history.* Authors already do that
work — today they do it in email threads wrapped around a form that silently
overwrites. Teach it far and wide: young and old, geek and otherwise, worker
bee and artist. It is a durable win for the person, not a tax imposed on them.

GitHub-as-CMS works only if four things are actually built. They are the
deliverable, and they are far less work than a CMS:

1. **A preview deploy per pull request.** The one that makes or breaks it.
   Editing prose without seeing it rendered is editing blind, and blind
   editing is where "give me the form back" comes from. Non-negotiable.
2. **Validation that speaks English.** CI must catch a YAML syntax slip, a
   schema violation, and a broken reference, and report them as a
   plain-language PR comment pointing at a line — not a stack trace. An
   author who gets a traceback for a missing quote has been told the tool is
   not for them.
3. **Prose in Markdown, not YAML scalars.** YAML block scalars are
   whitespace-sensitive, and multi-paragraph copy inside them is exactly
   where a careful non-programmer gets burned for reasons invisible on
   screen. YAML holds structure and short labels; anything paragraph-length
   is a Markdown sidecar the YAML points to. Authors then mostly edit
   Markdown, which forgives indentation and which they may already know.
4. **CODEOWNERS plus branch protection.** Content changes route to the person
   who owns that content, and nothing reaches production without review.
   This is the part the old admin UI did not do at all.

Remaining friction is real but small: accounts with 2FA on a private repo,
and somebody eventually hits a merge conflict and needs help. One-time human
problems. Neither is a reason to build a CMS.

Related: [GITHUB-AS-MMORPG](GITHUB-AS-MMORPG.md) ·
[skills/content-rescue/](../skills/content-rescue/) ·
[skills/constructionism/](../skills/constructionism/) ·
[email/sunny-street-outreach.md](email/sunny-street-outreach.md)

## Two costs, stated honestly

**1. Referential integrity moves from the database to CI.** A foreign key
guarantees a state row points at a real definition. If definitions are files,
the state row holds a key, and validity is enforced by a validator rather
than a constraint. That is a genuine loss. It must become a real CI check,
not an intention.

**2. Historical content needs a version stamp.** A user completed step 7 in
2019; step 7's text has changed since. To reconstruct what they actually saw,
the state row must record which content revision was live — a git SHA or
content version on the log row. Easy to overlook, and it matters more than
usual anywhere the question "what advice did we give this person" may need
answering years later.

## Split the hybrids

Most tables sort cleanly into state or content. The interesting ones are
hybrids and need splitting rather than assigning. A group's **program**
(which path, which branding, which wording) is content. The same group's
**instance** (its members, enrollment dates, its invite code) is state. One
table, two lifetimes, two homes.

## Sequence it safely

Four moves, in order:

1. **Contract first.** The per-table document. Nothing is written until each
   table has one owner.
2. **Build beside.** New server, same database, no schema changes. It starts
   by serving one read-only page correctly.
3. **Toggle and compare.** An admin-only switch between old and new for the
   same user and session. Render both ways and diff the output.
   **Divergence is a bug with a reproduction, not an argument.**
4. **Flip the default per surface, not all at once.** Admin last, because ops
   depends on it and it is the largest.

**Reads before writes throughout:** a new server that only reads cannot
corrupt production data while being evaluated.

The same non-destructive translation pipeline applies to the content move:
export using the round-trip methods that already exist, restructure flat
names into the tree, factor variants into override directories, validate in
CI, render both ways and diff — and only then stop reading the tables.

## Unify only when it deletes things

The stack decision is not settled by language preference. It is settled by
**what stops existing** when two systems become one application:

- **One identity system.** The role model has to be built once either way.
  Two web tiers means building it twice or standing up an auth service
  between them.
- **One admin.** Two admin surfaces merge into one permission model — which
  also dissolves the "but the framework gives us a free admin" argument,
  since the admin is being written anyway.
- **No bridge.** Where one app embedded the other's JavaScript and reached
  into a join table to do it, in a single app that is not an integration at
  all. It is a route. **The most awkward seam in the system is deleted
  rather than reimplemented.**
- **One front end, already built.** The old UI has to be replaced regardless.
  If a sibling app already has the theme, the accessibility work, and the
  navigation primitives, the migrated app inherits all of it instead of
  growing a parallel version.

Plus one toolchain, one test runner, one lint config, one deploy.

**Name what you lose.** A template engine that fit the content well does not
come to the new server. Say so plainly rather than glossing. Two things often
soften it: the engine usually survives elsewhere in the project where it is
still earning its keep, and the content it rendered was frequently never
really *its* pages — fragments run through a hand-written renderer, which as
Markdown-plus-components lose a bespoke renderer and gain composition that a
browser and a type checker both understand.

## The rule of two languages

**Pipelines in one language, the request path in the other.** Batch tooling,
compilers, spreadsheet import/export, image rendering, content validation,
and data analysis stay where the libraries are strongest. The request path
goes where the front end and the type checker live. Both already exist in the
toolbox image, so the split costs no new infrastructure.

Say explicitly which side the job worker lands on, or mark it open and decide
when the queue is rebuilt. Unmarked ambiguity migrates into the code.

## Parked, not dead

When a system is put on hold rather than killed, write the constraints that
keep resurrection possible — as a list, in the plan, where the *other*
migration's cleanup passes will read them:

- Do not delete or restructure the old app's directories, its setup
  artifacts, its entry point, its vendored dependencies, or its Dockerfile in
  cleanup passes.
- Preserve existing couplings the old app depends on, even ugly ones, until
  its fate is decided.
- Keep the database self-hosted and dump-restorable — no managed-service
  lock-in that an old client library cannot talk to.
- Name the open questions and who can answer them.

**"Nothing in the migration may make resurrecting this impossible or
difficult"** is a design constraint, and it is cheap to honor if written
down before the cleanup starts, and expensive to discover afterward.

## MOOLLM resonances

| This doc | MOOLLM |
|---|---|
| Content belongs in git; files are the program | [GIT-AS-FOUNDATION](GIT-AS-FOUNDATION.md), [kernel/DIRECTORY-AS-OBJECT.md](../kernel/DIRECTORY-AS-OBJECT.md) |
| Override directories holding only diffs | [skills/prototype/](../skills/prototype/), [SELF-ISH-INFLUENCES](SELF-ISH-INFLUENCES.md) |
| Flattened names → directory tree | [skills/file-system-object/](../skills/file-system-object/), [skills/room/](../skills/room/) |
| Delegation must be inspectable | [MOO-HERITAGE](MOO-HERITAGE.md), [KORZ-LLM-EVALS](KORZ-LLM-EVALS.md) |
| Structure in YAML, prose in Markdown sidecars | [skills/yaml-jazz/](../skills/yaml-jazz/) |
| Strict core, rich overlay; contract both ways | [object-system/DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md](object-system/DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md) |
| Resurrect and keep the genome, then absorb | [object-system/ENDOSYMBIOSIS.md](object-system/ENDOSYMBIOSIS.md) |
| Teach the real tool; authoring as construction | [skills/constructionism/](../skills/constructionism/), [skills/content-rescue/](../skills/content-rescue/) |
| The document is the source of truth | [skills/sister-script/](../skills/sister-script/) |
| Play in the old app, learn the contract, lift the rewrite | [skills/play-learn-lift/](../skills/play-learn-lift/) |

A concrete instance of the git-versus-database split, with bidirectional sync
and comment preservation:
[ebike-safari `git-postgres-sync.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/git-postgres-sync.md).

## The short version

- Get it running before you judge it. The instance is the spec.
- Write the data contract. One owner per table.
- Subtract from the old app first; the old app is its own oracle.
- Erase, stub, or decapitate — keep the head, drop the legs.
- Restore last month's backup: state or content? Content goes in git.
- Undo the flattening; let directories delegate.
- Measure before you argue about performance.
- GitHub is the CMS. Preview deploys, English errors, Markdown prose,
  CODEOWNERS. Teach it to everyone.
- Build beside, toggle, diff, flip per surface. Reads before writes.
- Name your losses out loud.
