# HN thread: gwern's "Project Xanadu: Even More Hindsight"

**[news.ycombinator.com/item?id=49559522](https://news.ycombinator.com/item?id=49559522)** ·
[gwern.net/xanadu](https://gwern.net/xanadu) · submitted 2026-09-04 · 102 points · 42 comments ·
31 distinct commenters

An earlier gwern.net/xanadu submission
([45315196](https://news.ycombinator.com/item?id=45315196), 2025-09-20) got 3 points and 0 comments,
so this is the first time the piece has had a real thread.

## This thread is not a deadline

Two facts set the strategy, and both cut against rushing a reply.

**The essay is about a year old.** It was already up in September 2025; this is a resubmission
finding an audience the first one missed. Nothing about it is breaking, and nothing here expires.

**Gwern has not posted in the thread** (checked 2026-09-06, 42 comments, no `gwern`). He is not
reading over anyone's shoulder, so a comment here reaches the commenters — not him.

So the thread is **evidence, not a venue.** Its value is that twenty-odd strangers independently
converged on pieces of this corpus's position, which is worth recording as corroboration. The
audience worth writing for is gwern himself, and the artifact that reaches him is a document he
chooses to open, judged by whether it wastes his time. That is
[the hub's gwern route](../README.md#if-you-are-gwern), which leads with what he does not already
have and says where to stop reading.

A thread reply stays worth making if it is cheap and additive — `Rochus` and `xnorswap` below are
both people missing a receipt someone here happens to hold. It is just not the thing that matters.

## Four comments that are answerable with primary sources nobody else has

Ranked by how much of the answer is already sitting in this corpus. These are not "someone is wrong
on the internet" targets; each one independently arrived at a piece of the argument and is missing
the receipt.

### `Rochus` ([49562486](https://news.ycombinator.com/item?id=49562486)) — reinvented definition previews

> I agree that transclusion, particularly based on byte offsets, is not very useful for the WWW. But
> the concept is much more useful than what the author suggests. Maybe you have heard of Ivar
> Jacobson's Objectory tool… it was able to transclude terms and definitions wherever they were
> linked, even integrated in the text flow where they appeared. **That was true added value.**

**This is HyperTIES definition previews, described from the nineties by someone who found the same
thing valuable and built his own (CrossLine).** He has separated the two claims correctly — byte-offset
transclusion is a bad idea, definition-level transclusion is a good one — which is precisely the
distinction [ARTICLE-SCHEMA.md](../hyperties/ARTICLE-SCHEMA.md) draws with the 1988 `.definition`
field, and which the `newsdoc/compile-all` build script proves was a *separate compilation unit*.
The reply writes itself: the distinction he is groping toward was shipped in 1988, the granularity
that works is the author-declared definition rather than the byte range, and here is the build
script.

Best single target in the thread. He is not arguing, he is corroborating.

### `xnorswap` ([49561910](https://news.ycombinator.com/item?id=49561910)) — trackbacks, and can't find the history

> the short-lived "webhooks for backlinks" trend, which didn't last long before spammers found and
> abused it… **Unfortunately google is now so bad, it's impossible to find genuine history of the
> phenomena I'm describing, so I just have to trust my memory that I'm not inventing a past that
> didn't exist.**

Trackbacks, named correctly by `taybin` downthread ("Back when we were using MovableType?"). Two
things Don can supply and almost nobody else can: **the primary history** — this is the Winer
lineage, and Don built a Technorati IE toolbar that did backlink overlay against Technorati's
database ([winer/README.md](../winer/README.md)) — and **the diagnosis**, which is that the spam
failure was structural rather than incidental. An unauthenticated inbound write to someone else's
page is a spam vector by construction; a *pull*-side index computed at build time over a corpus you
control is not. That is the difference between trackbacks and the compiled backlink index.

And his last sentence is a linkrot testimonial delivered by accident: a documented phenomenon from
twenty years ago is now unfindable, so he has to trust his memory. That is the argument for local
archives, in the voice of someone who did not realize he was making it.

### `gritzko` ([49560300](https://news.ycombinator.com/item?id=49560300), [49562783](https://news.ycombinator.com/item?id=49562783)) — git as the Xanadu substrate

> I always believed that **side-by-side diff view is a transclusion interface.**… permalinks can work
> on top of git quite nicely… If git's pack index gets refactored slightly, it can do anything from
> trigram-indexed search to metadata indexing to **hyperlinking both ways across repos**…
> Xanadu-like functionality is perfectly within reach. We don't get what we want or what we need.
> Instead, we move erratically in very small, easy, local steps.

**The closest independent arrival at this corpus's own position**, and he has running code
(`replicated.live`). Then in the follow-up he adds the agent argument unprompted:

> It is especially helpful if agents leave cross-references to have some trail for the decisions.
> **Agents, generally speaking, have no memory, so each time they recover the context from scratch.**
> When I read what they coded, I essentially do the same.

That is the context-cost problem and the [AUTO-FAQ](../AUTO-FAQ.md) K-line argument, stated by someone
who hit it in practice: the cross-reference trail exists so the derivation does not have to be
re-run. He is describing stringing K-lines and calling it permalinks.

This one is a *collaborator*, not a target. The reply should agree, add
[GitHub-as-slow-server](../PLAYABLE-CORPUS.md#github-is-a-slow-server-and-slow-is-the-correct-speed),
and ask about the pack-index work.

### `kmeisthax` ([49560457](https://news.ycombinator.com/item?id=49560457)) — the demo was the problem, not the feature

> The crazy irritating zig-zagging split document view has always struck me as a demo that would be
> rounded off after "initial release", **because it's still a useful feature underneath the stupid
> viewer-friendly UI.** Anyone who has ever reviewed a Git PR or negotiated a contract has already
> had to do what Xanadu was built to do. It's just that lawyers and programmers invented user
> interfaces that actually make sense for that, while the Xanadu version is hyper-optimized for the
> worst possible case.

Separates the *idea* from the *demo*, which is the fair version of gwern's critique and a better one.
Worth engaging because it is the strongest form of the opposition: the mechanism was right and the
presentation was tuned for a pathological case. The [focus-flow](../hyperties/FOCUS-FLOW.md)
chevron argument is the direct answer to "how should the visible bridge have looked."

## The rest of the thread, briefly

- `Rygian` ([49562460](https://news.ycombinator.com/item?id=49562460)) rebuts "solution in search
of a problem" with a list of still-unsolved everyday problems mapped to numbered Xanadu principles.
Substantive; `huurtehoog` and `iFreilicht` reply that intent to solve is not solving, and
`iFreilicht` lands the fair point — "it was simply never finished enough."
- `foul` ([49563819](https://news.ycombinator.com/item?id=49563819)) quoting the
links-as-annotation-overlay argument, which is the peripheral-views position arrived at
structurally.
- `kryptiskt` and `huurtehoog` give the best two-sentence critique in the thread: the world is
too mutable, and a design with no adversarial dynamics settles nowhere. Honest, and the
static-tier argument is the answer.
- `nekusar` — micropayments as libertarian dystopia, hostile and not engageable productively.
- `doublerabbit` — a one-line smear about Nelson's personal life. **Do not engage.** Noted only
because it is the ambient condition that the portrayal standards exist for, showing up on cue in a
thread about his work.
- Assorted "not to be confused with" jokes: the ATS-Xanadu compiler, the Olivia Newton-John film,
Kubla Khan. `taybin`'s "Gaze upon my blogs, and despair" is the best line on the page.



## What this changes about the pending reply

The reply task was queued as a general statement of the transclusion/context-cost thesis. Two
revisions, in order of importance.

**Demote it.** With gwern absent and the essay a year old, a thread reply is a small additive act,
not the main move. The prepared document is the main move.

**If it does get written, make it specific.** Reply to `Rochus` with the Objectory/HyperTIES
convergence and the `compile-all` receipt, and to `xnorswap` with the trackback history and the
pull-versus-push diagnosis. Both found the right idea and lack the evidence, which beats restating a
thesis at a thread already halfway to it. Restating the thesis at strangers is the version that
wastes everyone's time, including ours.

Standing constraint from `[copy-that](../../../skills/copy-that/)`: drafts ship in a fenced block
formatted for HN, notes outside the fence.

## Related

- [nelson/README.md](README.md) — the Nelson study
- [gwern/README.md](../gwern/README.md) — the gwern study
- [hyperties/HN-ARCHIVE.md](../hyperties/HN-ARCHIVE.md) — the earlier HyperTIES HN threads
- [hyperties/ARTICLE-SCHEMA.md](../hyperties/ARTICLE-SCHEMA.md) — the `.definition` receipt for `Rochus`
- [winer/README.md](../winer/README.md) — Technorati and the backlink lineage for `xnorswap`

↑ [webtop hub](../README.md)