# The commit is the conversational turn

**Pushing to a branch is how you say something.** Not storage underneath a conversation — the
utterance itself. A contribution, an assessment, an annotation, a correction, a reading list, a
character's accumulated path: each is a commit, the back-and-forth is a branch's history, and the
review is a pull request. That is the entire protocol, and its most valuable property is that
**nobody has to learn it**, because millions of people already know how GitHub works and the ones who
don't can be carried through it without ever seeing it.

This is the piece [CURSOR-STORAGE.md](CURSOR-STORAGE.md) leaves open. That document establishes where
objects live (`type_id` branches), what git gives away for free, and why holding user credentials is
the thing to avoid. This one covers the layer that lets **a reader with no GitHub account
participate anyway** — a bot that makes the branch, writes the commits, opens the pull request, runs
the checks, decides the obvious cases, and escalates the rest to a human.

## The author/committer split is already the right primitive

Git has carried the mechanism for thirty years and almost nobody uses it deliberately: **a commit has
an author and a committer, and they can be different people.**

```
Author:    Jane Reader <jane@example.com>      ← the contributor
Committer: corpus-bot <bot@example.org>        ← whoever held the credential
```

So the bot holds the write credential and the contributor holds the claim. GitHub renders both.
`Co-authored-by:` trailers extend it to several people on one commit. No account required, no token
handed over, attribution preserved in the artifact rather than in a database beside it.

**The catch is the whole security story: an author string is a claim, not an identity.** Anyone can
set `--author` to anything. For a project whose subject matter is *portraying real people*, this is
not a footnote — it is the primary abuse case. Somebody will sign an assessment as Alan Kay.

So identity is two-tier, matching the on-ramp tiering already in CURSOR-STORAGE:

| Tier | How | Rendered as | May sign |
|---|---|---|---|
| **Claimed** | Typed a name into a box | Visibly marked unverified, and **never** as a bare name | Assessments in a quarantine namespace; own cursors and notes |
| **Verified** | GitHub device flow once, or a signing key | Their identity, with the provenance of the verification | Assessments that count toward any aggregate |

**Unverified contributions must not be able to impersonate.** A claimed name that collides with any
real person in the corpus gets rejected at submission, not at review — and that check is a lint over
the character directories, which the repo already has.

## Commits are cheap and frequent; the pull request is the reviewable bundle

Don's constraint is the load-bearing one: **a changeset has to be big enough that reviewing it is
worth a human's attention.** Forty pull requests each fixing one typo is worse than no contribution
system, because it converts a gift into a chore and the maintainer stops looking.

Split the two rates apart:

- **Commits: as often as anything happens.** Every turn, every assessment, every note. This is the
  conversation advancing, it costs nothing, and the history is the record of how the thinking went.
  A branch accumulates them, publicly visible and readable the whole time.
- **Pull request: opened at a boundary.** Session end, an explicit *publish*, a size threshold, or a
  timeout. One PR per meaningful body of work.

The PR body is **generated, not typed**: what changed grouped by kind, counts, the specific files, a
plain-language summary, and the bot's checks already run with results inline. The reviewer opens one
thing and sees a curated bundle with its homework done.

Two consequences worth stating because they are not obvious:

- **The branch is publishable before the PR is merged.** Otherwise batching punishes the contributor
  with delay — they said something and nothing appeared. Render the branch as a preview and the wait
  costs nothing. GitHub is a slow-moving server, and slow is only a problem when the fast path is
  missing.
- **History is the part people forget to curate.** CURSOR-STORAGE's rule holds: publishing may be a
  squash. The conversational commits are the working record; what lands on the shared branch is
  edited.

## What the bot decides by itself, stated as a rule rather than a vibe

"Humans decide the fate except in obvious cases" needs *obvious* to be a predicate, or the bot
becomes an unaccountable editor.

The distinction that makes it tractable: **merging someone's own signed opinion into their own
namespace is not a judgment about whether they are right.** That is the auto-mergeable class.

| Class | Condition | Action |
|---|---|---|
| **Own namespace** | Confined to `assessments/<verified-author>/`, `cursors/cursor_<id>/`, or the contributor's own character directory; schema-valid; no shared files touched | **Auto-merge.** Their opinion, their shelf |
| **Malformed or hostile** | Schema invalid, path outside the allowlist, secret detected, oversized binary, name collides with a real person, edits *someone else's* signed record | **Auto-reject** with the failing check named and a way to fix it |
| **Shared content** | Any change to corpus text, indexes, schemas, or another person's directory | **Human**, always |
| **Lint-flagged** | Synonym collision, broken link, a distinctness-filter hit — the failure modes the tagsonomy compiler warns about | **Human**, with the lint output as the first comment |
| **New identity** | First contribution from an identity, whatever it contains | **Human.** One-time cost, and the only cheap spam filter that works |

**Editing another person's signed assessment is never auto-anything, and arguably never allowed at
all** — a signed record is theirs. Disagreement is expressed by adding your own, which is what
[SIGNED-ASSESSMENTS.md](SIGNED-ASSESSMENTS.md) means by rendering the split rather than resolving it.

### The bot's own decisions are signed assessments

The bot is an assessor with a name. Every auto-merge and auto-reject is a signed, dated record with
its rule cited, in the same format as any other assessment, in the bot's own namespace.

This is not tidiness. It makes three things possible that are otherwise impossible: the bot's
**false-accept rate is measurable** against later human reversals; a contributor can **contest a
rejection** using the same mechanism they would use to contest a claim; and the bot's judgment is
**visible rather than ambient**, which is the [ambient-layer critique](OBJECTIONS.md) applied to our
own infrastructure. An automated gatekeeper that leaves no ledger is exactly the
system-operational move this project claims to avoid.

## Where it runs, and what it may touch

Everything already established in [CURSOR-STORAGE.md](CURSOR-STORAGE.md#credentials-what-is-actually-safe-and-what-only-sounds-safe)
applies, with one change in blast radius worth naming: the App private key is now used to write **on
behalf of people who did not authenticate.** That raises the stakes on scoping.

- **GitHub App, installation-scoped**, never a personal access token, and never one App across
  unrelated repos.
- **Branch protection makes `main` unreachable for the App.** The permission model, not the code, is
  what prevents a bug from writing to the published corpus. Code that checks paths is a second layer,
  never the first.
- **Path allowlist enforced twice** — server-side at submission, and again in Actions on the branch,
  because the two can disagree and the disagreement is the interesting case.
- **Checks run in Actions**, which is free compute on the repo's own terms. Note the trigger gotcha
  already documented: Actions will not fire on a bare object branch, so the webhook is the trigger of
  record.
- **Rate limits per identity, quarantine namespace for unverified**, and unmerged branches never
  affect the build — which means the worst case for spam is storage and noise, not a corrupted
  corpus.

## Honest costs

- **The bot is a chokepoint, and that cuts against the no-server thesis.** If it is the only door,
  its operator is a gatekeeper and the project has quietly acquired the thing it said it did not
  need. The mitigation is that it must be an **accelerator, not a monopoly**: anyone with a GitHub
  account forks and opens a PR directly, exactly as CURSOR-STORAGE describes, and the bot exists for
  the people who will not do that. If the direct path ever stops working, the design has failed
  regardless of how well the bot works.
- **Someone runs it, pays for it, and is liable for what it hosts.** Anonymous write-through to a
  repo you own means hosting other people's content under your name. Quarantine and human review for
  shared content are the answer, and they are a real operational burden rather than a clever
  sidestep.
- **Batching trades contributor latency for reviewer sanity.** Branch previews reduce the pain but
  do not remove it.
- **Auto-merge into own-namespace will be wrong sometimes.** Someone will publish something in their
  own directory that should not be hosted. That is a moderation problem, not a schema problem, and no
  predicate solves it — which is why the bot's ledger and a reversal path matter more than tuning the
  rule.
- **Review still does not scale past the maintainer's attention.** Curated bundles raise the ceiling;
  they do not remove it. At volume, the honest options are delegating review to trusted contributors
  or letting the queue grow, and pretending otherwise is how contribution systems die.

## Related

- [CURSOR-STORAGE.md](CURSOR-STORAGE.md) — orphan branches, the credential analysis, forking as the polite path, and the Postgres projection this pipeline feeds
- [SIGNED-ASSESSMENTS.md](SIGNED-ASSESSMENTS.md) — what most of these contributions *are*: signed assessments, free to conflict
- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the static and social tiers, and why GitHub is the slow-moving server
- [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) — the lints that decide which PRs a human must see

↑ [webtop hub](README.md)
