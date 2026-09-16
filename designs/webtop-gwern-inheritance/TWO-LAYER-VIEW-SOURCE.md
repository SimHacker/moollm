# Two layers and the view-source move

**Status:** Design (harvested from a bike ride and a Gemini session, 2026-09)
**Depends on:** [GITHUB-AS-MMORPG.md](../GITHUB-AS-MMORPG.md) as substrate
**Feeds:** the Gwern correspondence, and the corpus problem measured in
[LATENT-SPACE-REPUTATION.md](../LATENT-SPACE-REPUTATION.md)

The decision is already made: **GitHub repos are the single source of truth.** This document is
about what sits on top, and about the one move that makes the whole arrangement worth building —
being able to point at a rendered page and drop through it to the files that produced it.

## Layer 1: the brutalist girders

GitHub already renders a `README.md` in whatever directory you visit. You get two things stacked:
the directory listing of every file and subdirectory, then the meant-for-human-consumption layer of
the README, which can link to other human-facing `.md` files or straight into raw directories.

This layer costs nothing, has no build step, and cannot break. It is the permanent fallback. If the
compiler is broken, unmaintained, or thirty years dead, the repository is still readable by a human
with a browser and still ingestible by a scraper. Everything below is an enhancement of this, never
a replacement for it.

What the raw layer does badly is indexes. A directory listing is alphabetical and flat; it tells you
what exists but not what matters, what belongs together, or where to go next. The presentation layer
exists to **lift the directory indexes into curated overlay networks** — clustering, categorizing,
and curating the links, with cross, up, down, and out links. (Out, and down, in Beverly Hills.)

## Layer 2: the compiler

A gwern.net-class compiler over the repo that emits a static site which is deeply interactive
locally, and which points back at the backing store with absolute URLs.

**As static as possible.** A server may exist, but it earns its existence one feature at a time.
The read path stays static, because static is what survives: cacheable, mirrorable, archivable by
third parties, and not dependent on the author continuing to pay for anything. The only things that
justify a server are the authenticated write path below and whatever genuinely cannot be
precomputed.

## The view-source move

This is the load-bearing idea, and it is not the same as the "Edit this page on GitHub" footer link
that every docs site already has.

A reader can point at a URL on the rendered human-facing site. From that page, they can also
discover — through metadata in the HTML — **which GitHub files contributed to it.** So when they
want to make a change, a suggestion, or a correction, they do not address it to the rendered page.
They drop down to the source and open a pull request or a comment there.

The difference from a single edit link is plurality. One rendered page is typically compiled from
many sources: a `README.md`, several `.yml` files, an index it was lifted into, and possibly
material transcluded from another repo entirely. So view-source resolves to a **contribution set**,
not one file, and the interface has to show the set and let the reader pick the right target. A
correction to a quote goes to a different file than a correction to how that quote was categorized.

## Reparsing the phrase

"View source" has always been read as **view** the verb and **source** the noun: look at the thing
underneath. Invert the parts of speech and it reads the other way — **view** the noun and **source**
the verb. You have a view. Sourcing is what you do with it.

Both parses are live, and the second one is the interesting one, because the browser's View Source
was only ever a read. It is the great pedagogical accident of the web — a generation learned HTML
because every page shipped its own source — but it never let you write back. Reparsing the phrase
turns the same two words into the contribution primitive.

"Source" as a verb carries three senses here and the design wants all three. To source a view is to
**establish its provenance** — which files and which evidence back each thing it chose to show, in
the journalist's sense of well-sourced. It is to **procure** one — adopt someone else's view as your
own lens, the way you source a material. And it is to **become a source** — publish your view so
others can draw on it.

## Pages are views, and readers write views

This follows from [Views as Testimony](../pie-stack-views/VIEWS-AS-TESTIMONY.md), where a saved view
is an opinion about what matters recorded as data, and view trees are saveable, exchangeable,
diffable documents that can view each other.

Carried into the publication layer: **a page is not a document, it is the default view of a region
of the graph.** The author's initial view is a starting perspective, and it is offered as
*editable*, *adoptable*, or *arguable* — fork it and change it, stand in it as your own lens, or
disagree with it, where the disagreement is itself a view and therefore diffable against the
original. Readers create content by creating, editing, and interlinking views.

That is a better response vocabulary than "comment." A comment is a reply attached to someone else's
artifact. A view is an artifact, with its own URL, provenance, and standing.

## Two layers of contribution, and the same discipline in both

The reparse resolves most of the contribution-set problem. The reader does not have to guess which
of five source files to edit, because the thing they are producing is usually **a view**, which is a
single new artifact rather than a contested change to an existing one. The split:

| Contribution | Touches | Example |
|---|---|---|
| **View-level** | emphasis, curation, path, framing, argument | "these three quotes belong together and this one is the key" |
| **Source-level** | the words and the evidence | "that quote is misdated" |

This is the same discipline as the Quote object in [QUOTES.md](../QUOTES.md), one layer up. There,
interpretation is stored separately from attribution so that disagreement about what someone meant
can never edit what they said. Here, views are stored separately from prose so that disagreement
about what matters can never edit the text. Two people can argue at full volume about emphasis while
being structurally unable to touch the record.

It also lowers the temperature of contributing, which is the actual answer to toxic comment sections.
A reader who disagrees does not have to win an argument for a change to your text. They publish
their view, and it stands beside yours, and the difference between them is inspectable and
animatable. A view is a fork of attention, not an attack on prose.

**The cost, stated honestly:** if every view is a page with a URL, the site's page count is the view
count rather than the file count, and views are cheap to make. That is a combinatorial explosion with
real consequences for duplicate content, crawl budget, and the reader's ability to tell which view is
the author's.

## The site is a mapping from URLs to canonical views

Which is the thing that distinguishes the author's view from the long tail, and it is a definition
rather than a heuristic:

> **The website is a mapping from URLs to canonical views.**

So there is exactly one canonical view per URL, and it is canonical *because the mapping says so*.
What is not canonical is the idea that it is the only possible view of that material. Everything a
reader derives is a real view with real standing and no entry in the mapping, and a pull request is
the operation that proposes changing the mapping. Canonicity becomes a reviewable commit rather than
a property anyone has to infer.

This also settles the crawl question mechanically. The mapping is the sitemap: exactly those URLs get
pre-rendered, indexed, and served with `rel=canonical` pointing at themselves. Derived views live in
a namespace that is `noindex` until promoted. Crawl budget is spent on the mapping's range, which is
file-count-sized, not view-count-sized.

## The write path, in two tiers

**Tier 1, unauthenticated.** The page links out to GitHub. The reader is on their own from there,
and needs to already know what a fork is. This tier always works and requires nothing from us.

**Tier 2, GitHub App connected.** The reader connects a GitHub App that grants permission to fork,
branch, commit, push, and open a pull request. Then the whole loop happens through a friendly
interface inside the reading experience: no git vocabulary, no leaving the page, no understanding of
what a remote is. The App is what makes "as static as possible" compatible with "anyone can
contribute."

This is the part that distinguishes a repo show from a blog with a comments section. The product of
a repo show is a **living repo** — not a dead text blog, an mp3 podcast, or an mp4 with toxic
YouTube comments underneath. The reader's contribution lands in version control with attribution and
a review trail, or it does not land at all.

## The Ajaxian tension, and why it is not a compromise

The interface should be Ajaxian — a term coined decades after NeWS evangelized the approach, and
after PIXIE did it at Cambridge on a PDP-7 and the Titan. Client-side programmability, asynchronous
fetches, no full-page reloads.

That is straightforwardly at odds with SEO and with AI training scrapers. Search crawlers allocate a
rendering budget and give up; most AI scrapers do not execute a client-side state engine at all. A
site that assembles itself in the browser hands both of them an empty div.

The resolution is the same discipline as Layer 1: **the semantic HTML is complete before any
JavaScript runs.** Bots read a finished document with real paragraphs and real anchors. Humans get
that same document progressively enhanced into a spatial, asynchronous canvas. Interactivity is
added on top of a complete artifact rather than being the mechanism that produces it.

Worth adding for the machine readers specifically: serialize the structured data — the `CARD.yml`
and character metadata — into JSON-LD in the head, so a scraper registers the entities and their
relationships instead of inferring them from prose. This is the polite version of the corpus
argument: rather than hoping a model correctly extracts that Heinz Lemke is tied to PIXIE, the Titan
and the PDP-7, say so in a format built for saying so.

## What a URL ships

Each URL in the mapping is pre-rendered server-side into a small bundle rather than one file, because
the audiences want different serializations of the same view and none of them should have to parse a
format built for another.

| Serialization | Who it is for |
|---|---|
| Semantic HTML, complete before any JS | search crawlers, AI scrapers, reader-mode, curl, the thirty-year fallback |
| JSON-LD in the head | scrapers that model entities instead of prose |
| JSON / YAML | the client's rehydration, and anyone scripting against a view |
| CSV | tabular views, straight into a spreadsheet without a parser |
| XML | feed readers and XSLT-shaped tooling |
| JS | the rehydration payload, loaded last and never required |

The rule from the Ajaxian section still governs all of it: **the HTML is a finished document, and
everything else is an enhancement of a page that already worked.** A human downloading the bundle
sees the document instantly, and only then does it come alive.

## Browse mode and edit mode

The interaction model is HyperCard's, and it is worth naming precisely because the web mostly failed
to inherit it. A stack was not a published artifact with a separate authoring tool somewhere else.
**The reading tool was the authoring tool**, and you moved between them with a mode switch, at a user
level you chose: browsing, typing, painting, authoring, scripting. HyperLook carried the same
arrangement onto NeWS.

So a page arrives in **browse mode**, carrying all the metadata needed to flip into **edit mode**
without a round trip. Nothing is fetched to start editing, because the view arrived as data and the
editor is already local. Open, close, expand, annotate, rearrange, adjust the semantic and visual
level of detail — all of it operates on the overlay described in
[Transclusion Frames](../pie-stack-views/TRANSCLUSION-FRAMES.md), which is the thing that was
serialized into the bundle in the first place.

The two tiers of the write path are then exactly HyperCard's user levels, and the escalation is the
same shape:

| Level | Where the edited view goes |
|---|---|
| **Browse** | nowhere; the default view of the mapping |
| **Local** | `localStorage` or IndexedDB — your own copies, private, no account, no server |
| **Shared** | uploaded to our origin, given a URL, `noindex`, still not canonical |
| **Sourced** | GitHub App: fork, branch, commit, PR — a proposal to change the mapping |

Only the last one touches the source of truth, and it is the only one that needs an account.

## Incremental navigation is content-addressed, so there is no cache invalidation

The requirement is that moving to another page must not re-download the whole page, or any piece
already held. Git makes this nearly free, because **git objects are content-addressed: a blob's name
is a hash of its contents.** Two consequences fall out with no invalidation logic at all.

A pre-rendered bundle ships a **manifest** of the pieces its view is assembled from — each markdown
file, each YAML node — with each piece's blob SHA. Navigating to another URL fetches that URL's
manifest, diffs the SHAs against what is already cached, and requests only the misses. A piece whose
SHA you hold is *provably* the same bytes, so it is never revalidated, never re-fetched, and cacheable
forever. Shipping the manifest inside the pre-rendered page means the client needs no API call to
learn what to fetch, which turns out to matter enormously below.

The same property makes the CDN cheap: a URL pinned to a commit SHA is immutable by construction, so
it can be served with a one-year `immutable` cache directive honestly rather than optimistically.

## How much can be palmed off on GitHub

Most of it, but the read path and the write path have completely different economics, and the numbers
matter because two of them are low enough to be architectural constraints rather than details.

| Traffic | Route | Real limit |
|---|---|---|
| First paint of canonical views | GitHub Pages | 1 GB site, **100 GB/month soft** bandwidth, 10 builds/hr unless a custom Actions workflow publishes |
| The compile itself | GitHub Actions | free for public repos — their CPU, not ours |
| Piece fetches during navigation | jsDelivr, pinned `@<commit-sha>` | a CDN built to front GitHub; global edge cache; the intended answer |
| Piece fetches, direct | `raw.githubusercontent.com` | **~5,000/hr per IP** — and a 429 blocks that IP from *all* GitHub HTTPS for 30 minutes |
| Trees, metadata, search | `api.github.com` | **60/hr per IP unauthenticated**; 5,000/hr per authenticated user |
| Fork, branch, commit, PR | `api.github.com` as the reader | 5,000/hr, spent from **the reader's own quota** |
| Review, discussion, CI | Issues, Discussions, PRs, Actions | the intended use; no bandwidth question at all |

`verified: 2026-09-08 — GitHub REST rate-limit docs (60/hr unauthenticated, 5,000/hr authenticated,
15,000/hr for Enterprise-owned Apps); GitHub Pages limits page (1 GB, 100 GB/mo soft, 10 builds/hr);
raw's 5,000/hr-per-IP and the 30-minute block from a GitHub engineer's answer rather than from docs,
so treat it as the safe number and not a contract.`

**The unauthenticated API cannot run a browsing app.** Sixty requests per hour per IP is not a
budget, it is a wall, and hitting it is the single most likely way this architecture fails in
practice. Which is why the manifest ships inside the pre-rendered page: **the read path must not
touch `api.github.com` at all.** Pre-rendered bundle for structure, CDN for pieces, API never.

**Then authentication pays for itself twice, and this is the part worth designing around.** The
GitHub App is already wanted for the write path — fork, branch, commit, PR without git vocabulary.
The same login raises that reader's API budget from 60/hr to 5,000/hr *spent from their own account*.
So connecting GitHub is not only how a reader contributes; it is how the read path scales, because
every logged-in reader brings their own quota with them. The feature that looked like a write feature
is the read feature.

**The dangerous denominator is per-IP.** Universities, corporate NAT and mobile CGNAT put thousands
of readers behind one address. One enthusiastic reader can 429 an entire institution, and raw's
penalty is a half-hour block on all GitHub HTTPS from that IP — which would break `git clone` for
everyone behind it, not just this site. That makes the CDN the default read path rather than an
optimization, and it makes graceful degradation mandatory in the robust-first sense: **on 429, fall
back to our own origin and keep working.**

**What cannot be offloaded.** Search, because the search endpoints have their own much tighter bucket
— ship a prebuilt static index as a CDN asset instead of querying anything. Shared-but-unauthenticated
views, since giving an anonymous reader a URL requires a store we control. And the origin that the
CDN and Pages both fall back to, which has to exist precisely so that nothing above is load-bearing.

The one clause worth knowing rather than discovering: the Pages terms exclude using it as free
hosting for a commercial service, which this is not. The constraint that will actually bite is the
rate limits, and the documented consequence of exceeding the bandwidth quota is a polite email from
GitHub Support suggesting you put a CDN in front — which the design already does.

## Why this connects to the Gwern discussion

The [baseline probe](../LATENT-SPACE-REPUTATION.md) found that the model's picture of Don Hopkins is
assembled almost entirely from his own first-person writing, scattered across Hacker News, Medium,
`donhopkins.com` and `art.net`, with almost no outside-authored material — and that confidence
tracks posting volume rather than significance. Gwern's name resolves to something coherent because
his body of work is one obsessively cross-linked self-hosted site.

So the architecture above is not only a publishing preference. Consolidating a scattered corpus into
a linked one with explicit provenance is the intervention the measurement argues for, and the public
write path is what lets third parties add the outside-authored material that a self-narrated corpus
structurally lacks.

**What gwern.net does better, stated plainly:** single-author coherence, no build fragility, and
typography and reader-attention design that took years to tune. The two-layer scheme trades some of
that coherence for a write path and a machine-readable backing store. That is a real trade, not a
free win.

## Undecided

- **Build language.** Python with a markdown library and a graph library, or a JavaScript build
  pipeline. Not settled, and the choice should follow from what the compiler needs to do to the
  graph, not from preference.
- **How the contribution set is surfaced.** Showing a reader five source files and asking them to
  pick the right one is a UI problem that could easily end up worse than a single wrong edit link.
  A radial fan is the candidate answer — see
  [Transclusion Frames](../pie-stack-views/TRANSCLUSION-FRAMES.md), which also pairs *view source*
  with its antipode *source view*.
- **Transclusion across repos.** `moollm` is public, `DonHopkins` is not. A rendered page compiled
  from both has to know which halves of its own provenance it is allowed to name. Proposed
  mechanism: a **clearance** parameter on the frame, shared with [Quotes](../QUOTES.md).
- **Manifest granularity.** A blob SHA names a whole file, but views transclude *nodes* — one YAML
  key, one section. Sub-file pieces need either their own content hashes computed at compile time or
  a byte range against a blob SHA, and the first costs build time while the second breaks on edit.
- **Who pays for anonymous sharing.** The shared tier needs an origin store, which is the one place
  the design cannot palm the cost off, and it is also the one place abuse arrives.

## See also

- [GITHUB-AS-MMORPG.md](../GITHUB-AS-MMORPG.md) — the substrate this assumes
- [GWERN-WHAT-TO-INHERIT.md](GWERN-WHAT-TO-INHERIT.md) — the explicit inheritance list
- [K-PYRAMID-ATTENTION-MAPS.md](K-PYRAMID-ATTENTION-MAPS.md) — what the lifted indexes are made of
- [../QUOTES.md](../QUOTES.md) — the attributed-playback content type this has to render
- [../EXPLORATORIUM.md](../EXPLORATORIUM.md) — the disposition this architecture is in service of
