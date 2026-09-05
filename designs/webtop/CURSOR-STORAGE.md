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

## The layer above: branch-as-object makes a repo a polymorphic container

The orphan branch is only the **mechanism** — one clean tree with no shared history. The convention
layered on top has a name and a written protocol: **branch-as-object**, naming branches `type_id`
so the ref namespace becomes a typed object store. The branch *is* the object, its history is the
object's audit log, its HEAD is current state, and deleting it tombstones the object.

> Spec: `skills/github/protocols/branch-as-object.md` in Leela's `central`, which documents the
> convention and its live use. MOOLLM's own schemapedia already names the pattern in
> `[skills/schema/schemas/mechanisms/github/](../../skills/schema/schemas/mechanisms/github/)` —
> theory there, operational practice in central, and this document is the reading-cursor application.

```
cursor_a3f9        character_b21        issue_4471        room_narthex
└─ type ─┘└─id─┘   └── type ──┘└id┘     └type┘└─id─┘      └type┘└──id──┘
```

Three properties fall out, and one of them is weaker than it first looks:

- **Per-type ID spaces.** `cursor_1` and `issue_1` are different objects. IDs need only be unique
within a type, so each type mints its own without coordinating with any other.
- **The prefix enumerates.** `git branch --list 'cursor_*'` lists every cursor in the repository.
**But that is enumeration, not query** — asking *which cursors are stale* means checking out or
fetching each branch and scanning its files, which is a linear walk. The protocol doc is explicit
that this scales to thousands of objects per type and is not a substitute for a database with
indexes. Cheap listing, expensive field queries.
- **One repo holds many types**, which is what makes it a **polymorphic container** rather than a
place to keep one kind of thing.

**And MOOLLM binds the type to a skill.** `cursor_`* resolves to `skills/cursor/`, `character_*` to
`skills/character/`, and the instance inherits its behavior, schema, and permissions from there. The
prefix is not a label — it is the pointer to the prototype, so an object's type tells you what it can
do and where that is defined.

This is the constitution's plural-typed-container discipline on a different substrate. In the
filesystem the *directory* infers the type of its children; in git the *ref prefix* does. Same rule,
same first-guess-right behavior, and the ref namespace turns out to be a container like any other.

The precedent is running in production: **Leela's alerting system stores each alert as an**
`Issue_<id>` **branch**, holding evidence, query results, and working files in a tree of its own.

### Lowercase, and why the separator is an underscore

**Use** `type_id`**, lowercase.** This is a deliberate revision: the central protocol currently
recommends PascalCase or UPPERCASE type names, and its live branches are `Issue_<id>` and
`ALERT_<n>`. Lowercase is the better rule going forward for a reason that is not aesthetic. Loose
refs are literal files under `.git/refs/heads/`, so on macOS and Windows — case-insensitive
filesystems — `Issue_1` and `issue_1` are **the same ref**. A single-case convention makes that
class of collision unrepresentable; a mixed-case one fails silently and per-platform, which is the
worst way to fail. Worth deciding deliberately rather than by drift, since existing branches use the
old rule.

**The underscore is load-bearing, for two reasons.** The protocol's own: ids frequently contain
dashes (UUIDs, slugs), so `_` is the only separator that splits `type` from `id` unambiguously. And
a structural one: git refs are paths, and a ref cannot also be a directory of refs — adopt `cursor/1`
and you permanently burn `cursor` as a usable ref name, and `refs/heads/cursor/1` versus
`refs/heads/cursor/1/notes` becomes a hard conflict the first time you want a sub-ref. Underscores
keep the namespace flat and sidestep the whole class.

Sanitize ids while you are at it: ref names cannot contain spaces, `..`, `~^:?*[`, or end in `.lock`.

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


| Field      | Repo                                      | Access            |
| ---------- | ----------------------------------------- | ----------------- |
| `home:`    | **yours** — where the orphan branch lives | write             |
| `targets:` | **theirs** — what the cursor points into  | read only, pinned |


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

### Fork the location repo: the polite way to get write access without asking

There is a better move than keeping a wholly separate storage repo, and it is the ordinary GitHub
one: **fork the repo you are reading, put your cursors in the fork, and open pull requests for
whatever is worth sending back.**

This is more polite than requesting write access, and the asymmetry is exactly what the pull request
was invented for. Asking for write access asks a maintainer to **trust you and accept risk**, before
they have seen anything. A fork asks **nobody for anything** — it is unilateral — and the PR that
follows asks only for **review of one specific change.** The maintainer's cost drops from "assess
this person" to "read this diff," which is why the answer is so much more often yes.

**Forks and orphan branches compose unusually well.** Your fork's `main` mirrors upstream and stays
clean; your `cursor_<id>` branches share no history with it, so they never touch the code, never
collide when you sync upstream, and never appear in a PR diff unless you aim one at them. The fork's
branch namespace becomes your polymorphic container **for that corpus specifically**, which is a
tidier arrangement than one storage repo holding cursors into a dozen unrelated places.

**Correcting the discovery pessimism above: the fork network *is* an index.** GitHub lists a repo's
forks, and forks with `cursor_*` branches are annotation layers. "Who has read and marked up this
corpus" becomes a query against machinery that already exists and that nobody has to maintain —
federated, opt-out, and outliving any company. It is not a good index (fork lists get enormous, the
UI is poor, and forks-of-forks nest badly), but claiming there was none was wrong, and a PR is also
exactly the backlink and notification I said the arrangement could not produce.

**But a PR is not the right destination for most of a cursor**, and conflating the two would be a
mistake. Your reading positions, your marginalia, and your disagreements are *yours*; nobody is
merging your reading notes into their essay, nor should they. Only a **subset** of what a cursor
accumulates is an offer to the upstream — a correction, a dead link, a missing citation, a genuine
addition. The fork holds everything; the PR carries only the part that was meant for them.

**The constraint that decides where private cursors live: you cannot privately fork a public repo.**
On GitHub, forks of a public repository are public, always. Since a cursor records where you stopped
reading — which is where you got bored, lost, or angry, and more intimate than a bookmark — this is
not a small detail. It splits the design cleanly:

| Intent | Where it goes |
|---|---|
| annotation you mean to share, or contribute upstream | **a fork** of the location repo |
| reading position and private marginalia | **a separate private storage repo**, never a fork |

You can mirror-push a public repo into a private one, but that is not a fork: you lose the upstream
link and the PR path, so it buys privacy at the cost of the whole reason to fork. Better to keep both
and promote a cursor from the private repo into the fork at the moment you decide to publish it —
which is the same [transition-is-a-commit](READING-CURSORS.md#the-two-tiers-again-and-the-transition-is-a-commit)
move, with a repo boundary as the privacy gate.

**What is still genuinely lost.** Discovery via fork network only works when your layer lives in a
fork, so the private tier remains invisible by construction — which is the correct behavior, not a
bug. And a corpus published somewhere other than a forge has no fork network to inherit, so for
those the original pessimism stands.

## Three things git gives away that we would otherwise have to build

**The commit history is the path — and therefore the return stack.** Every move the cursor makes is a
commit on its own branch. That means the itinerary is not a log we maintain alongside the state; it
*is* the state's history, with timestamps, diffs, and authorship. The [mark
ring](READING-CURSORS.md#a-selection-is-a-cursor-with-width) that reading interfaces lack comes free,
and it is better than Emacs's because each position also records what changed when you were there.

`git worktree` **is the body plan.** `git worktree add` checks out several branches into several
directories from one repository, simultaneously. Which is literally
[a creature in several places at once](READING-CURSORS.md#body-plans-cursors-are-limbs-and-a-creature-has-more-than-one):
the worm with its head in document A and its butt in document B is two worktrees, and each limb is a
checkout. The thing that sounded like a metaphor is a plumbing command.

**Forking is handing someone your character.** A fork copies the branch with its history intact, so
the recipient gets the position, the inventory, and the route that produced it — and their divergence
is a diff. Pull requests are how a character brings something back. This is the social tier without a
social feature: identity, sharing, review, and merge are the host's, not ours.

## One design decision, with a real tradeoff

You could store cursors **outside** `refs/heads/` **entirely** — in a custom ref namespace like
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


| Rung              | Requires                                   | Durability                          | Shareable             |
| ----------------- | ------------------------------------------ | ----------------------------------- | --------------------- |
| **LocalStorage**  | nothing at all                             | until you clear site data           | no                    |
| **Export a file** | nothing at all                             | as durable as your Downloads folder | by sending it         |
| **Storage repo**  | a repo + credentials, both supplied by you | archival, versioned                 | fork, cite, hand over |


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

### Credentials: what is actually safe, and what only sounds safe

The useful fact that shapes everything: `api.github.com` **sends CORS headers and**
`github.com/login/*` **does not.** Reading and writing repository contents from a browser works with
no server at all; only the token-*minting* dance is blocked. So the two auth rungs have very
different infrastructure costs.

**Rung A — fine-grained PAT, zero infrastructure.** The user creates a
[fine-grained personal access token](https://github.com/settings/personal-access-tokens), scoped to
**one repository**, with `Contents: Read and write` **and nothing else**, and an expiry. Paste it in.
Because the API is CORS-enabled this is genuinely backend-free, which keeps the no-server thesis
intact. The instruction that matters: **never a classic PAT** — classic `repo` scope grants every
repository the user owns, including private ones, which is the difference between a bounded mistake
and an unbounded one.

**Rung B — GitHub App + device flow, for people who should not be handling tokens.** Device flow
needs only a `client_id` and **no client secret**, which is exactly why it suits a static site. Three
real advantages over a pasted PAT: the user grants access through GitHub's own per-repository
installation UI rather than by trusting your instructions; tokens **expire** (8 hours, with refresh)
instead of lasting a year; and the token request accepts a `repository_id` **parameter that pins the
token to a single repository** regardless of what else the installation can see.

The catch is the CORS gap above: `login/device/code` and `login/oauth/access_token` cannot be called
from a browser. The fix is **a stateless relay that forwards exactly those two paths with CORS
headers attached** — a Cloudflare Worker of roughly 150 lines. Worth being precise about what it is
and is not, because it looks like the central server this design exists to avoid: it holds **no
client secret** (device flow has none), stores nothing, keeps no tokens, has no database, and its
path allow-list is deliberately narrow. Tokens pass through once and are forgotten. It is a CORS
shim, not an auth backend, and the moment it holds a secret it has become the thing we were avoiding.

### The threat that is specific to this design

**A cursor app renders content from repositories it does not control, in the same origin that holds
a write token.** That is the actual attack surface, and it is worse here than in an ordinary SPA,
because [location repos](#a-cursor-names-two-repos-and-they-are-not-the-same-repo) are by definition
other people's. Untrusted markdown and HTML being rendered next to a credential is the whole problem
in one sentence.

No token storage choice fixes this. LocalStorage, `sessionStorage`, and IndexedDB are all readable by
any script on the origin, and a static site cannot use the real answer (`httpOnly` cookies) because
that needs a backend. Encrypting the token with a non-extractable `CryptoKey` sounds like a fix and
is not — script that can call `decrypt` does not need to read the key. What actually helps is
**isolation and blast radius**:

- **Keep the token on a different origin from the renderer.** A small auth frame owns the token and
exposes a narrow `postMessage` API — "commit these files to this repo." XSS in the renderer can
then ask for a commit but cannot exfiltrate the credential, and the API only ever writes to the
one cursor repo.
- **Render foreign content sandboxed**, in a `sandbox`ed iframe on a separate origin, so a location
repo's content cannot reach the parent's storage at all.
- **CSP with** `connect-src` **limited to** `api.github.com` and the relay, so a stolen token has
nowhere to be sent from.
- **A dedicated private repo.** Cursors record where you stopped reading, which is more intimate
than a bookmark — default the created repo to **private**, and never point the token at anything
else the user owns.



### Two footguns worth naming

- **Never let the export include the token.** "Download my data" that serialises LocalStorage will
cheerfully write a live credential into the user's Downloads folder. Store credentials under a key
the exporter explicitly excludes, and test that.
- **"Forget my token" is not revocation.** Clearing local state leaves the token valid on GitHub's
side. Say so, and link straight to the revocation page.



### The rest of the free rung's costs

- **Clearing site data destroys an un-synced cursor**, silently and completely. That is the price of
requiring nothing, and it argues for offering the export rung *early*, before someone has
accumulated enough to mourn.
- **LocalStorage is roughly 5–10 MB per origin.** Cursors that
[cache the quoted spans they annotate](#a-cursor-names-two-repos-and-they-are-not-the-same-repo)
will reach that, and the answer is IndexedDB rather than a smaller cursor.



## Use dedicated repos for objects, never mix them with source

A cursor repo should contain **nothing but objects**. Not your code, not your site, not your notes
as prose — one repo whose entire job is holding `type_id` branches.

This is worth a rule because it converts several separate problems into non-problems at once:

- **The orphan-branch surprise becomes the repo's stated purpose.** Every branch is an orphan, none
  of them merge, and `main` exists only to say so. Nobody is confused by a repo that is consistently
  one thing; they are confused by a source repo with strange branches hiding in it.
- **`main` is the place for the explainer and the index**, so the per-branch generated `README.md`
  can be one terse line pointing at it rather than repeating the whole story.
- **CI does not fire.** A repo with no build has no workflow assuming descent from `main`.
- **The token's blast radius is exactly this repo**, which contains only objects. That is what makes
  "scoped to one repository" meaningful rather than nominal.
- **Clones stay small**, and the object history never inflates a source repo's.

## How big an ask is bring-your-own-repo, honestly

It depends entirely on the flow, and the two flows are not close:

| Flow | Steps | Realistic |
|---|---|---|
| **Paste a fine-grained PAT** | navigate settings → create token → choose fine-grained → scope to one repo → set contents-write → set expiry → copy → paste | **No.** Eight steps, several with a wrong-but-tempting option next to the right one. Most people will over-scope it or give up |
| **Install a GitHub App** | click Install → pick the repo → done | **Yes.** Three clicks, and the scoping is GitHub's UI rather than your instructions |

So the PAT path is a developer affordance and should be presented as one. The App path is the real
answer for anyone else — *provided they already have a GitHub account*, which is the actual gate.
For a general audience most people do not, and no amount of flow polish fixes that. Which is why
[the LocalStorage and export rungs](#the-on-ramp-most-readers-will-never-have-a-storage-repo) are
not a consolation prize: they are the tier most readers will ever use, and they have to be complete
on their own.

## Server-side is fine. Holding credentials is not.

The instinct that "no server" and "safe" are the same goal is worth separating, because they are
different goals and only one of them matters here. **A server is not the risk; a server that holds
other people's authority is the risk.** Once you say that plainly, most of the design falls out.

There are two server architectures and they are not variations on a theme:

| | **Server holds user tokens** | **Client holds the token; server holds nothing** |
|---|---|---|
| User OAuths, server stores the access token and acts for them | ✅ typical | ❌ |
| Browser gets the token, writes directly to `api.github.com` | ❌ | ✅ |
| A database breach leaks | **every user's credentials** | nothing |
| The user's protection is | your promises and your security | **arithmetic — you do not have it** |
| Revocation | asks you, or GitHub-wide | GitHub's settings page, without telling you |

The second column is what "provably safe" actually means, and note *why*: not that the credentials
are well protected, but that **there is nothing to protect.** That is a claim a skeptical user can
verify from the outside — they can watch the network tab and see the token go only to
`api.github.com`, and they can read the App's permissions on GitHub's own installation page rather
than believing your privacy policy. Verification, not trust.

**So keep the server, and give it only work that needs no authority:**

| Component | Holds | Job |
|---|---|---|
| **Browser** | the user's token | every write. Never sends it anywhere but `api.github.com` |
| **CORS relay** | nothing — device flow has no client secret | forwards two token endpoints. Stateless, ~150 lines |
| **Index / cache** | **public data only** | crawl, search, aggregate, render heavy views |
| **GitHub** | the objects, the identity, the permissions | system of record |

### Attack surface, component by component

| Component | If fully compromised | Bounded by |
|---|---|---|
| Browser client | that one user's cursor repo is writable | fine-grained scope on one repo containing only objects |
| CORS relay | nothing — it stores nothing and holds no secret | keep the path allow-list narrow; **the moment it holds a secret it becomes the crown jewel** |
| Index server / Postgres | nothing that was not already public | public-only crawling, enforced as a rule not a habit |
| **GitHub App private key** *(only if the server acts as the App)* | **every installed repo, for every user** | this is the one high-value secret in the design. KMS, rotation, and a strong reason before you create it |

Two residual risks that no architecture diagram removes:

- **XSS in the client is the whole game**, because that is where the token is, and this app renders
  content from repos it does not control. Covered [above](#the-threat-that-is-specific-to-this-design);
  it remains the top risk and the reason for origin isolation.
- **Indexing public data is itself a privacy act.** Aggregating public cursors into a searchable
  index makes inference easy that was merely *possible* before — who reads what, how long they
  linger, when they stopped. Public-but-scattered and public-and-indexed are different conditions,
  and the honest position is that building the index creates exposure even though every input was
  already public.

## Git or Postgres is a false choice: git is the log, Postgres is the projection

The temptation to "just do it in Postgres and forget GitHub" is really a complaint about **queries**,
and it is a fair complaint: branch-as-object [cannot do field
queries](../../skills/github/protocols/branch-as-object.md#querying-across-branches-when-you-need-it)
without walking every branch. But queries are
the *only* thing Postgres wins, and the list it would have to reimplement is long:

| What GitHub already provides | Cost to rebuild |
|---|---|
| accounts, 2FA, SSO, password reset | an identity system, plus breach liability you did not have |
| a permissions UI and **revocation the user controls** | a consent product |
| version history of every object | temporal tables or event sourcing |
| three-way merge and conflict resolution | genuinely hard |
| **PRs — review of a state change** | a review product |
| **Actions — automation triggered by state change** | a CI system, on your compute bill |
| forking, and the fork network as an index | a sharing model |
| **the user's data survives your service dying** | impossible to rebuild; it is the opposite of what a database gives you |
| storage paid by GitHub | your hosting bill |

And what Postgres wins: indexed queries, millisecond writes, no account required, multi-writer
concurrency, low-latency reads. All real, none of them overlapping with the list above.

**They are complementary, so use both with a strict direction of authority:**

```
GitHub  ──(webhook on push)──▶  indexer  ──▶  Postgres  ──▶  fast queries, search, aggregate views
  ▲                                                                    │
  └────────────── writes go here, always, from the client ◀────────────┘
```

- **Git is the system of record.** Every write lands in the user's repo, from the client.
- **Postgres is a derived read model**, built by crawling public repos and kept warm by webhooks.
- Actions run in the *user's own* repo — validating their cursor, linting anchors, regenerating
  branch READMEs — which is automation you do not host, on data you do not hold.

**The discipline that keeps it honest is one sentence: you must be able to `DROP DATABASE` and
rebuild the index from the repos.** If that is true, Postgres is a cache and the user still owns
their data. If it drifts and becomes untrue — one field that exists only in Postgres, one write that
never lands in git — you have quietly reinvented the lock-in the whole design exists to avoid, and
you will not notice on the day it happens.

This is the ordinary CQRS split with git as the event log, which is worth saying because it means
none of it is novel and all of it is known to work. The beauty Don is reluctant to give up —
everything visible, versionable, PR-able, Actions-able — is preserved exactly, because those
properties live in the log and the projection never has to have them.

## Wiring the bridge: webhooks in, commits out, simulations on both

### The trigger gotcha: Actions will not fire on a bare object branch

The obvious plan — a GitHub Action that runs when a `type_id` branch changes — **does not work**, and
the reason is worth knowing before building on it. A `push` workflow is loaded **from the ref that
was pushed**. A cursor branch is an orphan containing only object files, with no `.github/workflows/`
in its tree, so a push to `cursor_a3f9` finds no workflow and nothing runs.

| Option | Verdict |
|---|---|
| Put `.github/workflows/` in every object branch | works, and pollutes every object with CI config it does not own |
| **Repo webhook (or a GitHub App subscribing to `push`)** | **the right answer** — fires on any ref regardless of tree contents, and the payload carries `ref` plus before/after SHAs, which is exactly an incremental sync cursor |
| Scheduled workflow on `main` that polls branches | works, laggy, and wasteful |

So the announcement channel is a **webhook**, not Actions. Actions still matter — see simulations
below — but they are triggered *by* the receiver, not by the object push.

### GitHub → Postgres: the easy direction, with two requirements

The receiver takes `(ref, before, after)`, reads the changed files at `after`, and upserts. Two
properties it must have, because webhooks are at-least-once and unordered:

- **Idempotent.** Duplicate deliveries must be harmless. Dedupe on the delivery ID, and store the
  last-indexed commit SHA per branch so a replay is a no-op.
- **Gap-tolerant.** Deliveries get dropped. On any doubt — an unexpected `before`, a missed
  branch — re-read the branch head and reconcile rather than trying to replay history.

Both are easy here for a structural reason: **the projection is rebuildable, so recovery is always
just "re-read."** There is no repair procedure to get wrong.

### Postgres → GitHub: not bidirectional sync, which is the trap

Bidirectional sync means two writers and a merge policy, and it is how the projection quietly becomes
authoritative. Do not build it. There are two legitimate write paths and it is worth being strict
about which is which:

**Write-through — for meaningful state changes.** The write goes to *GitHub* as a commit; Postgres is
updated optimistically in the same breath so the UI is instant, and marked unconfirmed until the
webhook returns the canonical version. Postgres never originates anything; it just gets to be early.

```
edit ──▶ commit to GitHub ──▶ (webhook) ──▶ Postgres canonical
   └────▶ Postgres optimistic ────────────────────▲ replaced
```

**Buffer-and-checkpoint — for high-frequency state that does not deserve a commit.** Scroll position
is the obvious case; a commit per scroll is the [granularity
problem](#honest-costs) in its worst form. Let it live in Postgres alone, declared **ephemeral and
lossy by design**, and commit only at checkpoints — the same meaningful-position boundaries that
[segment a ride](EBIKE-PATH-GRAMMAR.md#pauses-are-the-natural-cleavage-points). Losing the buffer
must cost you nothing but the tail.

The line between them is the honest bit: **anything you would be upset to lose must not live only in
the buffer.** If that rule starts bending, you have built write-back after all.

**Concurrency comes free.** `PUT /contents/{path}` takes the existing blob `sha` and rejects the
write if it has moved — that is compare-and-swap, so a conflicting write fails loudly with a 409
instead of silently clobbering. Optimistic concurrency control you do not have to design.

### Simulations run on both, and Actions is the free compute

A MOOLLM simulation is **just another writer**, and it uses the same paths: read from Postgres when
it wants queries, read from git when it wants provenance, and write through git like everyone else.
Nothing special, which is the point.

Running them **inside Actions** is the attractive part — automation triggered by object change, on
compute you do not host, with results committed back as objects. Two constraints shape it:

- **Dispatch, do not push-trigger.** Because of the gotcha above, the webhook receiver fires the
  simulation with `repository_dispatch` or `workflow_dispatch`, passing the branch as an input. The
  workflow itself lives on `main` where workflows belong.
- **Guard the loop.** A workflow that commits can trigger a workflow that commits. GitHub's default
  `GITHUB_TOKEN` deliberately does not trigger new runs, which makes the naive version safe by
  accident — but the moment you swap in a PAT or App token to get cross-repo writes, **recursion
  becomes live** and needs an explicit guard (actor filter, path filter, or a marker in the commit
  message). This is the bug that shows up as a runaway bill rather than an error.

And the best target for it is validation the user's own repo can run on itself: lint the object
against its type's schema, check that permalink anchors still resolve, regenerate the branch
`README.md`. Automation on data you do not hold, paid for by the platform.

## `main` is the type registry, and the URL is the join key

### The repo carries its own schema

The object branches hold instances; **`main` holds the types** — schema, skill, tools, validators, one
directory per type at a well-known path:

```
main:/types/cursor/SCHEMA.yml     # what a cursor_* branch must contain
main:/types/cursor/SKILL.md       # what MOOLLM does when it binds one
main:/types/cursor/tools/         # migrations, validators, renderers
```

This finishes the [type-prefix binding](../../skills/github/protocols/branch-as-object.md): the prefix
in `cursor_a3f9` was always a promise that something knew what a cursor is, and now that something has
an address. The repo becomes self-describing — schema shipped alongside data, which relational
databases have in `information_schema` and object stores almost never do.

The nuance is that schema and instances live on **different branches, so they move independently.**
That is the feature (migrate the type without touching a million objects) and the hazard (an object
can have been validated against a schema that no longer exists in that form). So an object records
the schema commit it was written against — the same `(ref, commit)` discipline as [the cursor
permalink](READING-CURSORS.md#the-cursor-is-a-permalink-remote-commit-path-anchor), applied to types
instead of positions. Validation failures then read "written against schema `a1b2c3`, current is
`f4e5d6`, here is the diff" rather than just "invalid."

### The URL is the canonical name — but store its parts, not the string

Don is right that keeping identity in-band is the beautiful part: the branch name is on the public
web, so **the absolute URL is already a global name** and nobody has to mint one. Two refinements.

**There are two URLs and they are not interchangeable.** A branch-ref URL is a mutable *identity*
(follows updates, always current). A SHA URL is an immutable *citation* (never moves, may be
garbage). Identity for the row, citation for anything reproducible — cached bytes, a rendered
figure, a claim in an essay.

**Store the components and derive the URL.** A repo rename or transfer invalidates every stored URL
string, including the ones buried in JSONB where no `UPDATE` will find them. GitHub redirects renamed
repos, but that is a courtesy that dies the moment someone squats the old name. Components in
columns, URL as a generated column, and a rename is one `UPDATE`:

```sql
create table object (
  owner       text not null,
  repo        text not null,
  type        text not null,
  id          text not null,
  branch      text generated always as (type || '_' || id) stored,
  url         text generated always as (
                'https://github.com/'||owner||'/'||repo||'/tree/'||type||'_'||id) stored,
  head_sha    text not null,          -- current tip; the citation form
  schema_sha  text,                   -- which type commit it validated against
  updated_at  timestamptz not null,
  meta        jsonb not null default '{}',
  primary key (owner, repo, type, id)
);
```

### It is `jsonb`, and that distinction is the whole feature

Postgres's binary JSON type is **`jsonb`**, not BSON — worth being exact about because `json` (the
other one) stores text verbatim and cannot take a GIN index, which is precisely the "slap indexes on
as needed" capability being asked for. Choose wrong and the long-tail column becomes unqueryable.

With `jsonb` there is a three-stage promotion path, and each stage is cheap:

| Stage | Cost | When |
|---|---|---|
| Land in `meta` | free | unexpected or one-off metadata |
| Expression index on the path | one `CREATE INDEX`, no migration | it started showing up in `WHERE` |
| Promote to a real column | a migration | it is stable, typed, and hot |

```sql
create index on object using gin (meta jsonb_path_ops);          -- containment, everything
create index on object ((meta->>'title')) where type = 'cursor'; -- one hot field, no migration
```

That path is what keeps `meta` from rotting into a junk drawer: it is a **staging area for fields
that have not earned a column yet**, with a clear graduation ceremony.

### The rule for what stays in git

**Postgres stores what you query on; git stores what you read.** If a value would only ever be
selected and never filtered, sorted, joined, or aggregated, it is bulk — leave it in the branch and
keep a URL. Objects are polymorphic and some carry megabytes of images, transcripts, and GPS tracks;
none of that belongs in a row.

The cache then falls out for free, because URL → path is total and reversible:

```
https://github.com/OWNER/REPO/tree/cursor_a3f9/notes/2026-09.md
                 → ~/.cache/moollm/OWNER/REPO/cursor_a3f9/notes/2026-09.md
```

And the two URL forms have exactly the caching behavior you would want them to: **SHA-keyed entries
are immutable and cacheable forever; branch-keyed entries are mutable and need invalidation** — which
is what [the webhook](#github--postgres-the-easy-direction-with-two-requirements) already delivers.
The push that updates the row is the same event that busts the cache.

## Honest costs

**Orphan branches are unusual enough to confuse tooling and people.** CI that assumes every branch
descends from `main` will do something surprising. Anyone cloning the repo will see branches that do
not merge and should not. This wants a `README.md` at the root of every cursor branch explaining what
it is, which is cheap and should be generated — and it is most of the argument for
[dedicated object repos](#use-dedicated-repos-for-objects-never-mix-them-with-source), below, which
make the surprise the *rule* of the repo instead of an exception inside it.

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
- `[skills/inventory/](../../skills/inventory/)` — refs versus boxes, and why boxing is irreversible
- `[skills/worm/](../../skills/worm/)` — the two-cursor organism whose limbs these worktrees are
- [EBIKE-PATH-GRAMMAR.md](EBIKE-PATH-GRAMMAR.md) — the same storage question for rides

↑ [webtop hub](README.md)