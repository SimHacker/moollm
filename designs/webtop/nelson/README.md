# Nelson: visible connection

Ted Nelson coined *hypertext*, *hypermedia*, *transclusion*, and *intertwingularity*. He is also the
person whose central demand the web never implemented, and which this hub is an attempt to pay off.

This is the public study: themes, ideas, and quotes already on the public record. Correspondence
stays private by default — see the note at the bottom.

---

## The one idea: a link should be a bridge, not a diving board

From *Xanadu Basics 1a — VISIBLE CONNECTION*, on YouTube, transcribed by Don:

> Here we have a Xanadoc. Right now it's disguised as plain text. But if we want to see connections,
> here they are. The ones outlined in blue are Xanalinks. **They aren't just jumplinks, what other
> people call hyperlinks. I've called them jumplinks since before the web. You're jumping to you know
> not where: it's a diving board into the darkness.** Whereas Xanalinks visibly connect to other
> content, with a visible bridge. The other documents open and I can scroll around in them!

His framing of the stakes, same source:

> The original hypertext concept of the 1960s got lost on the way to the Web — and all current
> document standards oppose it. This is an important fight.

Everything else follows from this. A jumplink destroys your context to show you something; you
cannot see where it goes without going; and once you go, the relationship between what you were
reading and what you are now reading exists only in your head. A Xanalink draws the relationship and
leaves both ends visible.

## Transclusion, and the receipt Ted rarely gets credited with

Transclusion — quoting by reference, so the quotation stays connected to and current with its
source — is Ted's term, from *Literary Machines* (1980). The mechanism has an older ancestor that
strengthens rather than weakens his case:

> Ted Nelson coined the term for his 1980 nonlinear book *Literary Machines*, but the idea of master
> copy and occurrences was applied 17 years before, in **Sketchpad**.

Sutherland had master-copy-and-instances in 1963. Nelson's contribution was seeing that documents
need it as badly as drawings do. Don's list of who this idea belongs to is deliberately plural: *"Ted
Nelson's, Ivan Sutherland's, Douglas Engelbart's, and Ben Shneiderman's important ideas about
transclusion."*

Ted's position has always been that transclusion is **infrastructure**: automatic, built in, invisible
to the author. Not something you do by hand.

## Self-revealing

Ted's term for the property good interfaces have and the word "intuitive" fails to name. From a
public talk:

> The term "intuitive" is stupid. Because, is a mouse "intuitive"? You look at it, and oooh, oooh,
> oooh. **But the moment you see it work, it has revealed itself. So it's "self revealing", is the
> term.** Pac-Man is another very nice example of a "self revealing" piece of software. I've often
> used it as an example of how software ought to work. Because you learn the rules within three
> quarters, putting three quarters into the machine.

And the corollary, which is a business observation rather than a design one:

> Whereas, it is in the interest of companies like Microsoft, and alas now Apple, to make things
> entangling and unclear, because that way you become committed to them.

He credited "self revealing" to a former supervisor. Don wrote to ask who, and Ted answered — the
reply is quoted in Don's published Medium archive, so it is already public record. It corrects the
spelling to **Klavs Landberg**, who in Denmark had written an operating system for the Datapoint 2200
*"before they would acknowledge that it was a computer"*, and who with Harry Pyle worked on an
operating system meant to "Outdo Unix" — *"which was a bad idea, but I documented that system till
Datapoint folded."*

The last line of that reply is the one worth sitting with:

> Don't know how to put this in Wikipedia.

The man who designed the system for publishing connected knowledge, unable to get a fact about his
own life into the encyclopedia, because the encyclopedia requires a citation and his source is his
memory. Xanadu's whole point was that provenance should travel with content. This is what its
absence costs, in one sentence.

Don's use of the term: pie menus are self-revealing in exactly Ted's sense — *"they either lead,
follow, or get out of the way,"* revealing themselves the first time and disappearing once your hand
knows the gesture.

## Intertwingularity

> everything is deeply intertwingled

*Computer Lib / Dream Machines* (1974) was printed as a two-front-cover paperback to enact the
claim — no canonical reading order, two entry points, flip it over. It was later republished by
Microsoft Press, which remains one of the better jokes in computing history.

The MOOLLM position is downstream of this: hierarchy is a *view*, not the truth. Directories are
rooms you can walk between, the graph is layered over the tree, and no single spine is privileged.

## The tension, stated fairly

Ben Shneiderman, in his own list of formative books, on *Computer Lib*:

> Ted Nelson's clever and innovative *Computer Lib* (1974) book and other writings demonstrated what
> truly innovative thinking was like. I've had the chance to meet Ted occasionally and am constantly
> impressed by his innovative thinking, but **I am among those who wish he would link himself more
> closely to practical realities.** Maybe that is too pedestrian of me, but it reflects my desire to
> be innovative while also having an impact.

That is the honest disagreement between two people in this hub, and both positions have receipts.
Ben's method — measure it, ship it, let Berners-Lee take the blue and run — produced the link every
person on earth clicks daily, and a narrower claim than Ted's. Ted's method produced the description
of what we are still missing thirty-five years later, which no amount of shipping has retired.

Don has also written critically about the 1999 Xanadu open-source release: the code had been written
in Smalltalk, machine-translated to C++, and it was the translator's output that was published —
unreadable and effectively unusable, which missed the purpose of releasing source. That critique is
about an artifact and it stands. His 1999 write-up also characterized Ted personally in terms that
are harsher than anything this pack should carry forward; **that language is deliberately not
reproduced here.** The technical point does not need it.

## What the webtop owes him, and where it still falls short

| Ted's demand | What we have | Honest gap |
|---|---|---|
| Visible connection — the bridge is drawn | Popups, backlinks, annotations | A popup is **a better jumplink, not a bridge.** You still cannot see the relationship, only the destination |
| Transclusion as infrastructure | Hand-copied quotes with hand-written attributions | Nothing machine-checks that our quotes still match their sources |
| Spans, not points | Anchors at best | *"There's no way to indicate the end of the relevant excerpt"* — Don's own diagnosis. Transclusion needs a stable start **and** end |
| Two-way links | Backlinks derived from the repo graph | Only inside our own corpus; across the open web, one-way |
| Documents open side by side, scrollable | Tabs, stacks, windows | Closest thing we have; the pieces exist, the relationship rendering does not |
| Self-revealing interfaces | Pie menus, reveal-all-targets | Genuinely satisfied. This one we have |

The uncomfortable conclusion, and it is worth stating plainly: **Temkin's Mesa is closer to Xanadu
than gwern.net is.** Gwern's ladder — link-icon, title, abstract, section — makes the jumplink
cheaper to inspect, and that is a large practical gain. But it still treats the link as a doorway.
Mesa opens the thing where it lives, on a shared surface, with position carrying meaning and both
ends simultaneously visible. That is the parallel-documents interface Ted has been demonstrating for
decades, minus the visible bridge. Drawing the bridge on Mesa's canvas is a smaller step than adding
it to a page of popups.

HyperTIES's contribution, for the record, is the cheapest partial answer anyone has shipped: the
mandatory per-article definition means a single click shows you what is across the bridge without
crossing it. Not visible connection. But it makes the diving board survivable.

## Personal

Ted is a long-standing hero and north star for this work — HyperTIES at Maryland was built by people
who had read *Computer Lib*. Don transcribes Ted's videos into illustrated text because, as he puts
it, hypertext deserves text artifacts too, and because *"it took him a lifetime to know what to say
on the video, so it was well worth my time transcribing what he had to say, to save other people
their own time."*

**Hugh Daniel**, who worked closely with Ted on Xanadu, is remembered in the private people
directory. That thread is a memorial one and is handled there.

## Provenance and permission

Everything quoted above is from a public source: Ted's own recorded talks, *Computer Lib*, Ben
Shneiderman's published book notes, or Don's own published Medium archive.

**Private by default.** Don's direct correspondence with Ted is captured under
`characters/don-hopkins/correspondence/` and the green room in the DonHopkins repo, and is not
summarized here beyond what Ted has already said publicly or Don has already published. At least
one thread carries an explicit hard rule against publication without Ted's permission, and that rule
holds.

**Quotes awaiting clearance** are collected in the private repo rather than staged here, so that
nothing lands in a public design document before Ted has been asked. Anything drawn from personal
conversation is stated as theme and idea, never as quotation, unless and until he says yes.

↑ [webtop hub](../README.md) · [hyperties](../hyperties/) · [gwern](../gwern/) · [temkin](../temkin/)

## Live threads

- [**HN-XANADU-2026.md**](HN-XANADU-2026.md) — the 2026-09-04 HN thread on gwern's *Project Xanadu: Even More Hindsight* ([49559522](https://news.ycombinator.com/item?id=49559522), 102 points, 28 comments, 23 commenters). **gwern has not appeared in it, and neither has Don.** Four comments are answerable with primary sources nobody else holds: `Rochus` independently reinvented definition previews via Ivar Jacobson's Objectory and correctly separates byte-offset transclusion from definition-level transclusion; `xnorswap` remembers trackbacks and cannot find the history, which is the Winer/Technorati lineage plus a linkrot testimonial delivered by accident; `gritzko` arrives independently at git-as-Xanadu-substrate with running code, and adds the agents-have-no-memory argument unprompted; `kmeisthax` separates the idea from the demo, which is the strongest form of the opposition.
