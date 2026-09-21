# Visible revisioned branching merging multi-user timelines

The proposal in one sentence: **a clipping is a commit, the clipboard is a repo, and the forge
supplies everything the editors left out.**

Not a metaphor. A repo, with the actual tooling. When the clipping is a commit, the whole list of
demands stops being a wish list and becomes a configuration of things that already work.

## The mapping

| Requirement | What supplies it | Status |
|-------------|------------------|--------|
| Visible | A working tree and a log you can look at | shipped |
| More than one | Branches, tags, stash entries, refs | shipped |
| Editable | It is a file in a repo | shipped |
| Never destroyed by a new copy | Content addressing: a new object cannot overwrite an old one | shipped |
| Survives the phone call | It is on disk, and it is pushed | shipped |
| History of the clipping itself | The commit log for that path | shipped |
| Who changed it and when | `git blame` | shipped |
| Why it was changed | Commit messages, PR description, review thread | shipped |
| Review, request changes, reject | Pull requests | shipped by the forge |
| Multi-user | Remotes, forks, permissions | shipped by the forge |
| Wired to the copy gesture | nothing | **this is the whole job** |

Every row but the last is boring, debugged, and installed on hundreds of millions of machines. The
last row is the entire remaining problem, and it is a user interface problem, not a systems problem.

## Why content addressing is the load-bearing part

Nelson's third property -- "whatever you put there destroys the previous contents" -- is not a
policy choice in the clipboard, it is a consequence of the storage model: one named slot, written in
place. Content addressing makes destruction structurally impossible. A new clipping hashes to a new
object. The old object is still exactly where it was, still reachable by its name.

You do not need to remember to save. You cannot clobber. The overwrite bug is not fixed, it is
**unrepresentable**.

Honest caveat: git is append-only by default, not by law. Unreachable objects are eventually
collected, and reflog entries expire (90 days reachable, 30 unreachable, by default). For a
clipboard those defaults are wrong and should be set to never expire, which is a config line.

## Blame is provenance, merge is transclusion's working cousin

Nelson showed his cousin a mockup where you drag a paragraph into a new document and a **stripe
stays behind showing where it came from**. That is transclusion: the content keeps its origin, and
the origin remains visible in place.

`git blame` is that stripe, computed after the fact, at line granularity, in every editor's gutter,
today. It is weaker than Xanadu -- it tracks the line, not the fragment, and it tracks within one
repo rather than across the literature -- and it is the closest thing to visible provenance that
anybody actually ships. **Merge** is the other half: two divergent histories of the same content
reconciled, with the conflict shown rather than silently resolved. Nelson wanted parallel
consideration of alternative structure. A three-way merge view is parallel consideration of
alternative structure.

## The part that is mine, and why it needs a forge

Nelson's demand stops at visible and more than one. The additions are editability, history, blame,
and **collaborative review**, and the last one is why plain git is insufficient.

Plain git gives one person a perfect private history. The interesting operations on a shared
clipping are social:

- A **pull request** against a clipping. You want to change the snippet everyone pastes.
- **Discussion on the PR.** Why are you changing this? What broke? Who asked?
- **Review** -- approve, comment, request changes, reject. A clipping can be **curated** instead of
  merely accumulated.
- **Commendation.** The good clipping gets found, starred, reused, credited.
- **Blame as an invitation**, not an accusation: the history tells you who to ask.

That is a GitHub-class feature set, not a git-class one. So: git for the substrate, a forge for the
social layer.

GitHub is dominant, so it is what we build against first. It also has real problems -- proprietary,
centralized, a single point of policy -- and there are self-hostable alternatives (Forgejo, Gitea,
GitLab, Sourcehut) implementing much of the same workflow. The requirement is **the workflow, not
the vendor**, and the option to move stays open for whatever materializes and qualifies. Pinning the
design to one forge would repeat the original mistake at a larger scale.

## It already exists and it is called a gist

The strongest argument that this is not speculative: **people already use GitHub gists as a shared
clipboard, constantly, by hand.** Snippet to paste somewhere, config to hand a colleague, error log
to show in a thread, a scrap you want on the other machine.

A gist is a git repo. That means the thing people reached for as a clipboard already has, today,
without anyone designing it for the purpose:

| Property | How a gist has it |
|----------|-------------------|
| Visible | It is a web page |
| More than one | Every gist is a separate one, listed |
| Editable | Edit in the browser or clone and push |
| Versioned | Full revision history per gist |
| Blame | It is a git repo |
| Forkable | Fork button |
| Discussable | Comments |
| Shareable | A URL, public or secret |
| Embeddable | Embed script for any page |
| Multi-user | Anyone with the link, plus forks and comments |

Every requirement in the table at the top of this page is **already shipped** in a product millions
of developers use daily. What is missing is exactly one thing: it is not wired to the copy gesture,
the desktop, or the applications. You reach it by opening a browser, clicking New, pasting, naming,
clicking Create, copying the URL. That is the manual version of what `Ctrl+C` should have been doing
all along.

So the ask is concrete and unromantic: **make the clipboard a gist-class object, and integrate it
with the desktop and every app.** Copy puts a clipping in a repo. Paste picks one from a visible
list. The list is versioned, editable, reviewable, and shareable with the people you work with,
because it is the same substrate that is already holding your source code. The forge is the
[multi-user world](../GITHUB-AS-MMORPG.md); the clipboard is the smallest object in it.

(Working term in these notes is "cliprepo", which remains **forbidden as the actual name** -- it is a
metaphor mashup and the [naming challenge](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-rosenthal/07-cliprepo-naming-challenge.md)
is still open.)

## The objections worth taking seriously

**Passwords go through the clipboard.** A permanent, visible, pushable history of everything you
ever copied is a security liability, and this is the strongest objection. It needs an answer at the
design level, not a bolt-on: clippings default to a local unsynced ref; a secret marking that keeps
a clipping out of history entirely; source applications able to declare a selection sensitive (X11
already has the concept of negotiated targets, so there is a place to put it); encryption for
anything that leaves the machine. A clipboard that remembers everything must let you tell it what
to forget, which is a different thing from forgetting by accident, which is what we have now.

**Commit per keystroke is absurd.** Right, so do not do that. Vim already solved the granularity
problem with undo blocks, and git already has squash and amend. Clippings coalesce; the commit
boundary is the gesture boundary.

**Git is bad at big binaries.** True, and a clipboard full of images and video is exactly that
case. This is the real engineering risk in the proposal.

**Latency.** A copy must feel instant. Writing an object and updating a ref is fast; talking to a
forge is not. Local first, push in the background, which is how every good sync system works.

## Prior art that had the interface right

HyperLook (NeWS, around 1990) had a **visible clipboard with history** holding **live objects**, not
bytes. You could copy and paste running components between stacks while they ran: pull the RCI gauge
out of SimCity into a graphics editor to keep watching it while you worked, or paste a clock into
the SimCity window so you would notice when it was time to stop playing and get some sleep.

https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4

The gap between HyperLook and this proposal is not the data structure. HyperLook had the visible,
multi-item, live clipboard thirty-five years ago and did not have revisioning, blame, merge, or
review. Git has all four and no gesture. Nobody has built both halves at once.

## MOOLLM angle

A clipboard that is a repo is a clipboard an **agent** can read, write, review, and be reviewed in.
The PR thread is the place where a human and an agent argue about a change with the diff between
them, which is the interface-to-agency argument applied to the smallest possible artifact.

- [`designs/INTERFACE-TO-AGENCY.md`](../INTERFACE-TO-AGENCY.md)
- [`designs/GIT-AS-FOUNDATION.md`](../GIT-AS-FOUNDATION.md)
- [`designs/GITHUB-AS-MMORPG.md`](../GITHUB-AS-MMORPG.md)

And the naming rule from [README.md](README.md) applies to every idea on this page: no metaphors.
The thing is not *like* a repo. It is one.
