# Where the rubber meets the road: storing cursors in git

*Don Hopkins · September 2026*

**Thesis:** a [reading cursor](READING-CURSORS.md) needs a body, and the body needs to live
somewhere. The answer is an **orphan branch** per cursor. MOOLLM supplies the object protocols, git
supplies the storage layer, and GitHub supplies the social, collaboration, and multi-user layer. No
new database, no server, no format.

---

## The technique has a name: orphan branches

`git switch --orphan <name>` (older spelling: `git checkout --orphan`) creates a branch with **no
parent commit** — a fresh root, an empty history, disconnected from `main`. A clean tangent universe
in the same repository, where you can put anything you want in its own directory tree without it
being a version *of* anything.

The convention everyone has already seen is the old `gh-pages` branch: a site that lives in the same
repo as the code and shares none of its history.

What makes it the right substrate here rather than merely a trick:

- **It is a typed, addressable object with its own filesystem.** The branch name carries the class
  and the id — `cursor_<id>`, `character_<id>` — which is [the plural-typed-container
  convention](../../.cursorrules) applied to refs. The prefix is the class; the suffix is the
  instance.
- **Its history is the object's history**, not a snapshot. Editable, evolvable, diffable, with
  timestamps and authors, going back to the object's creation.
- **The object store is shared.** Orphan branches are separate histories over the *same* blobs, so a
  cursor whose inventory is mostly references costs almost nothing, and a boxed copy that happens to
  be identical to the original is stored once.

**The pattern is already in production.** Leela's alerting system represents alerts as GitHub issues,
and stores each alert's data — loaded evidence, database query results, whatever the alert
accumulated — in an `Issue_<issueid>` branch. A little tree of files, isolated, with a type and an id
you can look it up by. `cursor_<id>` is the same move pointed at a different noun.

## The layer above: `Type_ID` branches make a repo a polymorphic container

The orphan branch is only the **mechanism** — one clean tree with no shared history. The convention
layered on top of it is what does the real work: **name branches `Type_ID`**, and the ref namespace
becomes a typed object store.

```
cursor_a3f9        character_b21        Issue_4471        room_narthex
└─ type ─┘└─id─┘   └── type ──┘└id┘     └type┘└─id─┘      └type┘└──id──┘
```

Three properties fall out of it, and none of them needed a database:

- **Per-type ID spaces.** `cursor_1` and `Issue_1` are different objects. IDs only have to be unique
  within a type, so each type mints its own without coordinating with any other.
- **The prefix is a type query.** `git branch --list 'cursor_*'` enumerates every cursor in the
  repository — `SELECT * FROM cursors` with no index to maintain, because the ref namespace already
  is one.
- **One repo holds many types**, which is what makes it a **polymorphic container** rather than a
  place to keep one kind of thing.

**And MOOLLM binds the type to a skill.** `cursor_*` resolves to `skills/cursor/`, `character_*` to
`skills/character/`, and the instance inherits its behavior, schema, and permissions from there. The
prefix is not a label — it is the pointer to the prototype, so an object's type tells you what it can
do and where that is defined.

This is the constitution's plural-typed-container discipline applied to a different substrate. In the
filesystem, the *directory* infers the type of its children; in git, the *ref prefix* does. Same rule,
same first-guess-right behavior, and the ref namespace turns out to be a container like any other.

The precedent is running in production: **Leela's alerting system stores each alert as an
`Issue_<id>` branch**, holding evidence, query results, and working files in a tree of its own.

### Two gotchas that decide the naming scheme

**The underscore is load-bearing; a slash would break it.** Git refs are paths, and a ref cannot also
be a directory containing other refs. Adopt `cursor/1` and you have permanently burned `cursor` as a
usable ref name, and any later wish for a sub-ref under an instance is a hard
`refs/heads/cursor/1` versus `refs/heads/cursor/1/notes` conflict. `Type_ID` keeps the namespace flat
and sidesteps the whole class of directory/file collisions. The choice looks cosmetic and is not.

**Pick one case convention and lint it.** Loose refs are literal files under `.git/refs/heads/`, so on
macOS and Windows — case-insensitive filesystems — `Issue_1` and `issue_1` are **the same ref**. A
repo mixing capitalized types (`Issue_`) with lowercase ones (`cursor_`) is fine until two types'
names differ only by case, at which point the collision is silent and platform-dependent, which is
the worst kind. Also sanitize IDs: ref names cannot contain spaces, `..`, `~^:?*[`, or end in
`.lock`.

## The layout

```
character_a3f9/              ← orphan branch, one character
  CHARACTER.yml              ← identity, voice, register, consent settings
  home.yml                   ← which repo this cursor lives in (yours, writable)
  targets.yml                ← which repos it reads (theirs, pinned SHAs, no write access)
  location.yml               ← where the cursor is standing right now
  body.yml                   ← limbs: which surfaces, which positions
  inventory/                 ← the portable graph
    refs/                    ← weightless pointers (TAKE REF)
    boxes/                   ← things that became their own objects (DROP AS BOX)
    outlines/                ← ongoing documents, each with an insertion cursor
  path/                      ← the itinerary
  notes/                     ← questions, disagreements, marks
```

`character_<id>` **inherits from** `cursor_<id>` and adds the fields a cursor does not need — voice,
goals, consent policy, the things that make it somebody's rather than merely a position.

## A cursor names two repos, and they are not the same repo

The cursor must be **explicit about which repository it lives in**, because in the normal case it is
not the repository it is reading. You have no write access to gwern.net's repo, or to
`SimHacker/moollm`, or to whatever you are annotating — and you should not need any.

| Field | Repo | Access |
|---|---|---|
| `home:` | **yours** — where the orphan branch lives | write |
| `targets:` | **theirs** — what the cursor points into | read only, pinned |

Each entry in `targets:` is the [permalink from
READING-CURSORS](READING-CURSORS.md#the-cursor-is-a-permalink-remote-commit-path-anchor):
`(remote, commit, path, anchor)`. So the split needs no new mechanism — the pointer was already
cross-repo-shaped, and this just says out loud that the two ends belong to different people.

**This is the third-party annotation problem, and it is the one thing the web never solved.**
Annotating someone else's document has always required either the publisher's cooperation — which
they will not give — or a central annotation server, which becomes the single point of failure and
the single point of capture. Google Sidewiki shipped and died; hosted annotation services survive
only as long as the company does. The git arrangement needs **neither**: your notes live in your
repo, addressed by permalink into theirs, and the target never has to know, agree, or exist as a
willing party. The annotation layer becomes independently forkable, citable, and archivable, because
it is just a repo.

**One cursor points into many repos.** A real reading path crosses corpora in a single session — an
essay here, a design doc there, a paper somewhere else — so `path/` is a sequence of permalinks
against *different* remotes, and there was never a single-repo version of this to begin with. Fan-in
is the same shape from the other side: many people's cursors point into one public repo, and none of
them need to know about each other.

**Cache the quoted span, not just the pointer.** Since you control neither the target's history nor
its continued existence, your annotation should carry the text it is about. That costs bytes and buys
two things: your notes stay meaningful when the target is rewritten or deleted, and the
[dangling-SHA fallback](READING-CURSORS.md#the-cursor-is-a-permalink-remote-commit-path-anchor) has
something to search with. It is transclusion with a local cache, and here the cache is the point —
an archival copy of exactly what you were responding to.

**There is a live receipt for this arrangement in this project.** Don's private `DonHopkins` repo
holds correspondence, clearance decisions, and working notes whose `see_also` paths point into the
public `WillWrightShowForFood` and `moollm` repos. Private annotation layer, public target, pointers
across the boundary, no central service — already in daily use, just not yet called a cursor.

**Honest cost: discovery.** Out-of-band annotation trades **findability for independence**, and that
is a real trade, not a free lunch. Nobody reading the target repo can see that your layer exists;
there are no backlinks, and the target cannot be notified without opting in to something. A
publisher who *wants* the annotations can list known layers, and readers can share cursor URLs
directly, but neither is discovery at scale. The hosted services that died at least had an index.
Being clear-eyed: this design makes annotation possible without permission and does nothing to make
it findable, and those are separate problems that should not be solved by pretending the second one
is easy.

## Three things git gives away that we would otherwise have to build

**The commit history is the path — and therefore the return stack.** Every move the cursor makes is a
commit on its own branch. That means the itinerary is not a log we maintain alongside the state; it
*is* the state's history, with timestamps, diffs, and authorship. The [mark
ring](READING-CURSORS.md#a-selection-is-a-cursor-with-width) that reading interfaces lack comes free,
and it is better than Emacs's because each position also records what changed when you were there.

**`git worktree` is the body plan.** `git worktree add` checks out several branches into several
directories from one repository, simultaneously. Which is literally
[a creature in several places at once](READING-CURSORS.md#body-plans-cursors-are-limbs-and-a-creature-has-more-than-one):
the worm with its head in document A and its butt in document B is two worktrees, and each limb is a
checkout. The thing that sounded like a metaphor is a plumbing command.

**Forking is handing someone your character.** A fork copies the branch with its history intact, so
the recipient gets the position, the inventory, and the route that produced it — and their divergence
is a diff. Pull requests are how a character brings something back. This is the social tier without a
social feature: identity, sharing, review, and merge are the host's, not ours.

## One design decision, with a real tradeoff

You could store cursors **outside `refs/heads/` entirely** — in a custom ref namespace like
`refs/cursors/<id>`. This is well-trodden: `git notes` lives in `refs/notes/`, and Gerrit runs
enormous deployments on `refs/changes/*`. It keeps `git branch` clean no matter how many cursors
exist, which matters once a person has fifty.

**Use real branches anyway.** GitHub does not render custom refs — you cannot browse them in the web
UI, they do not appear in the branch dropdown, they are not forkable through the interface, and most
tooling will not see them. Since the entire argument for this design is that **GitHub is the social
layer**, storing the social objects where GitHub cannot display them defeats the purpose. Clutter in
the branch list is the price of the collaboration layer, and it is worth paying.

The mitigation is naming discipline, which we need anyway: the `cursor_`/`character_` prefixes make
the namespace filterable, and the branch list becomes a directory of readers rather than noise.

## The on-ramp: most readers will never have a storage repo

Everything above assumes a repo, and **the casual web guest does not have one and never will.** If
the design requires git to keep your place, it has no users. So the storage repo is the *top* rung,
not the entry, and the ladder has to work from the bottom with nothing.

| Rung | Requires | Durability | Shareable |
|---|---|---|---|
| **LocalStorage** | nothing at all | until you clear site data | no |
| **Export a file** | nothing at all | as durable as your Downloads folder | by sending it |
| **Storage repo** | a repo + credentials, both supplied by you | archival, versioned | fork, cite, hand over |

The middle rung matters more than it looks: it covers the person who wants their data out and has no
GitHub account and no intention of getting one. Download a file, keep it, re-import it later or on
another machine. No account, no git, no service — and it is the honest answer to *"can I have my
stuff?"* for the majority who will never climb higher.

**The upgrade is bring-your-own-repo, and that is the whole point.** You supply the repo and the
credentials; they are stored locally; the app syncs your LocalStorage tree into your storage repo.
There is no signup, because **there is nobody to sign up with** — the operator never holds your data,
your identity, or your token. That is the property worth protecting, and it is what makes the tiers
honest rather than a funnel.

### Make LocalStorage hold the repo's own file tree

This is the decision that determines whether the upgrade path works or quietly loses data.

If LocalStorage keeps an **opaque blob** and sync converts it, then two browsers with two blobs and
one repo is **last-write-wins**, and a browser's worth of notes disappears with no conflict, no
warning, and no recovery. If LocalStorage instead holds **the same file layout the branch holds**,
sync is an ordinary commit, divergence between your laptop and your phone is a **real merge with
real conflicts**, and git resolves it with machinery that already exists.

So the tiers are not two formats with a converter between them. They are **one format with two
backing stores**, and that is the only version where climbing a rung is free and reversible.

### Honest costs of the free rung

- **Credentials in LocalStorage are readable by any script on the origin.** This is the standard
  token-storage anti-pattern, and a static site with no backend cannot use the standard fix
  (`httpOnly` cookies), so there is no secure option here — only **small blast radii**. Use a
  fine-grained token scoped to *one* repo with contents-write and nothing else, prefer a GitHub App
  or device-flow token over a pasted PAT so it is revocable and expiring, and point it at a
  dedicated cursor repo rather than anything else you own. Compromise then means someone can write
  to your notes, which is bad and bounded — a different category from acting as you.
- **Clearing site data destroys an un-synced cursor**, silently and completely. That is the price of
  requiring nothing, and it argues for offering the export rung *early*, before someone has
  accumulated enough to mourn.
- **LocalStorage is roughly 5–10 MB per origin.** Cursors that
  [cache the quoted spans they annotate](#a-cursor-names-two-repos-and-they-are-not-the-same-repo)
  will reach that, and the answer is IndexedDB rather than a smaller cursor.

## Honest costs

**Orphan branches are unusual enough to confuse tooling and people.** CI that assumes every branch
descends from `main` will do something surprising. Anyone cloning the repo will see branches that do
not merge and should not. This wants a `README.md` at the root of every cursor branch explaining what
it is, which is cheap and should be generated.

**A commit per cursor move is a lot of commits.** Every scroll is not a commit; the granularity has
to be *meaningful positions*, which means something must decide what counts — probably the same
pause-detection that [segments a ride](EBIKE-PATH-GRAMMAR.md#pauses-are-the-natural-cleavage-points).
Getting this wrong in either direction produces either an unreadable history or a useless one.

**Publishing a cursor publishes its history, and history is the part people forget.** Curating the
current state of a cursor before sharing it is obvious; curating its *past* is not, and the git model
makes the past durable by design. The [three
gates](READING-CURSORS.md#honest-costs) have to apply to the branch, not just the tip — which in
practice means publishing a cursor is a squash or a filtered export, not a push.

**Nothing here is live.** Git is [a slow server](PLAYABLE-CORPUS.md#github-is-a-slow-server-and-slow-is-the-correct-speed),
which is the correct speed for everything except presence. That remains true and remains fine.

---

## Related

- [READING-CURSORS.md](READING-CURSORS.md) — what a cursor is and why it needs a body
- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the static-versus-social tiers, and GitHub as a slow server
- [`skills/inventory/`](../../skills/inventory/) — refs versus boxes, and why boxing is irreversible
- [`skills/worm/`](../../skills/worm/) — the two-cursor organism whose limbs these worktrees are
- [EBIKE-PATH-GRAMMAR.md](EBIKE-PATH-GRAMMAR.md) — the same storage question for rides

↑ [webtop hub](README.md)
