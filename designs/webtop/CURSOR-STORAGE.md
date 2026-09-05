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

## The layout

```
character_a3f9/              ← orphan branch, one character
  CHARACTER.yml              ← identity, voice, register, consent settings
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
