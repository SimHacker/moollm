# The case against this whole directory

Fernando Borretti, ["Unbundling Tools for Thought"](https://borretti.me/article/unbundling-tools-for-thought)
(26 December 2022) — cited approvingly by gwern in the Roam thread: *"makes some of these points at
greater length and I largely agree with."*

It is the best argument against building what we are building. Read it before the hub, not after.
Anything below that we cannot answer, we should concede.

## His opening shot, which is aimed directly at us

> There's a joke in game development that there's two kinds of game devs: those who write engines,
> and those who make games. The people who make the engines do it for the intellectual pleasure of
> discovering a beautiful algebra of vectors, scenes, entities, and events; and watching a beautiful,
> crystalline machine in operation. The actual game—which is never finished, rarely started—is an
> afterthought.

> I've written something like six or seven personal wikis over the past decade. It's actually an
> incredibly advanced form of procrastination.

**Answer:** the only honest one is shipped games. Micropolis, SimCity on four platforms, The Sims
content pipeline, eBike Safari. The webtop is a shell for corpora that already exist and get used
daily, not a wiki awaiting content. But the charge is live and should stay pinned to the wall: *if
a year passes and the beautiful algebra has no game on it, he was right.*

## Unbundling

95% of tool-for-thought use cases separate cleanly into better single-purpose apps: journalling,
todos (Todoist), learning (spaced repetition subsumes prose notes entirely), contacts, fiction
writing, process notes, legal documents, lists. What survives unbundling is **collection
management** — and there he finds a genuine hole in app-space:

> It should be, essentially, an SQLite frontend with a fancy interface. You can define record
> templates (like `Book` or `Person` or `Song` or `Paper`) having typed fields... field types can be
> simple data like strings or dates, or links to other records, or lists of links, or a star
> rating... You can put records in hierarchical folders, but you can also retrieve them with search
> and tags.

**Answer:** that is `CARD.yml`. Typed record templates with fields, links, and lists of links,
browsable by folder *and* by search *and* by tag, one class per kind of thing —
`CHARACTER.yml`, `ROOM.yml`, `GLANCE.yml`. Borretti says the app that should exist does not; we
built it on git and YAML instead of SQLite and React, and the reason it survived where his seven
wikis did not is that **it is not a place you go to write, it is the shape the work already has.**

Note also where he unbundled *to* for the use case that mattered most to him — fiction:

> I quickly moved to a git repo with Markdown files because 1) I could compile the disparate files
> into a single PDF or HTML file for review, and 2) using git for version control (rather than my
> personal wiki's native change tracking) makes a lot more sense for writing projects.

He unbundled into our substrate and did not notice.

## Every node is a debt

> Every node in your knowledge graph is a _debt_. Every link doubly so. The more you have, the more
> in the red you are. Every node that has utility... is drowned in an ocean of banality.

**This is the strongest hit and it is correct** for hand-maintained graphs. Our answer is not
"discipline." It is that the debt is only incurred by nodes a **human** must maintain:

- Pyramid rungs between what you wrote and the glyph are **generated on demand** and never
  maintained. A node nobody has to keep true is not a debt.
- Rot service is automated — Nenex's outdated-pages sweep proposes the fix and you approve in
  batches ([`gwern/NENEX.md`](gwern/NENEX.md)).
- Backlinks come from the repo graph, not from you remembering to add them.

The residual debt is real: **stable anchors**. Views and backlinks both need every node
addressable, and that is work no model does for you.

## The single graph fallacy

> The idea of having this giant graph where all your data is hyperlinked is cute, but in practice,
> it's completely unnecessary. Things live in separate apps just fine. How often, truly, do you find
> yourself wanting to link a task in your todo list app to a file in Dropbox?

Plus the plugin critique: Obsidian's 700 plugins, and *"the user experience for this plugin-based app
universe is always going to be inferior to the user experience for domain-specific apps. It always
feels janky."*

**Partial concession.** We are not claiming one database of you. The webtop is a **shell over
many corpora that keep their own membranes** — the endosymbiosis model, deliberately not
assimilation. Instagram keeps the photos; Zotero keeps the papers; gwern.net keeps gwern.net.

On jank, he is describing a real failure mode and the mitigation is structural, not aspirational:
the Gonzo kernel / skin pack split, one interaction vocabulary saturating the gesture space, and
HyperTIES's rule of **one language for content and presentation** rather than markup plus a
separate style language. If we end up with a plugin marketplace, he wins that one.

## Links should follow usage, not potential

The aside, which is the most valuable paragraph in the essay and which he throws away:

> in the web, it makes sense that links should reflect _potential_, since you don't know what people
> reading your document will want to follow. But in a personal database it makes a lot more sense
> that links should follow _usage_: they should be **a crystallization of the trails you've
> followed**, rather than an a-priori structure that you impose before usage.

He has independently rederived Bush's associative trails as the *fix* for the thing he is
criticizing, and then does not build it. This is precisely
[`pie-stack-views/VIEW-STATE-ANCESTORS.md`](../pie-stack-views/VIEW-STATE-ANCESTORS.md): the link you actually traversed,
recorded, addressable, citable, replyable.

His supporting data makes the case sharper: *"upwards of 80% of the links in my wikis are essentially
structural, they basically replicate folder structures"* and the rest are duty-links added *"out of
some vague feeling of duty to link things."* Structural links should be **derived** from the
directory, never typed. Duty-links should never be typed at all. What is left is the trail — and the
trail is the only kind he says would be worth having.

## Uncertain payoff

> silver bullets are rare, and it's possible that after making a titanic effort to migrate all my
> data and build a great UI, the result is very underwhelming.

**No answer available.** This is a bet. The mitigations are that there is no migration (the corpora
are already in git and already used), and that each piece has standalone value — the pyramid without
the desk, the view records without the pies, the annotation layer without any of it.

## Exhibit: Roam's own encyclopedia entry

Roam is the app Borretti and gwern are both arguing against, and the neutral record of it is worth
looking at directly. [Wikipedia's article on Roam](https://en.wikipedia.org/wiki/Roam_(software)) is
**a three-sentence stub**, tagged as a stub, last edited 6 September 2024. Stable release: **0.0.18**,
six years after launch. Proprietary, commercial, and valued at $200 million at seed
(*The Information*, 11 September 2020).

An enormous discourse — courses, cults, consultants, "networked thought" — and the encyclopedic
substance is: it exists, it is a graph, it competes with Notion. Set that against gwern's remark that
the actually-effective method has *"nothing to create a social-media cult over or sell 'courses'
about (!)"*. The hype-to-substance ratio here is not a side observation; it is the evidence.

### The tree you fled

The article's single substantive design claim, sourced to Roam's own marketing:

> The system is built on a directed graph, **which frees it from the constraints of the classic
> filesystem tree.**

This is precisely the premise we invert. In MOOLLM the filesystem tree is not a constraint to escape
— **directories are rooms**, the path is the address, and the tree is the world. Winer got there
first: in Frontier the outline *is* the object database, not a view onto one.

And Borretti supplies the receipt against Roam's claim, from inside his own wikis:

> upwards of 80% of the links in my wikis are essentially structural, they basically replicate folder
> structures.

You flee the tree, then rebuild it by hand as links — worse, and with no `cd`, no `git log`, no `rg`,
no diff, no URL. The graph is real and worth having, but it should be *derived from* and *layered
over* the tree, not offered as an escape from it.

#### The tree is not one grouping mechanism, it is several

The objection above is only half an argument, because "keep the tree" sounds like accepting a coarse
tool for the sake of `git log`. It is not coarse. The naming protocols give you a **graded** set of
grouping mechanisms, all of which the filesystem enforces for free, and they are specified in
[`kernel/naming/NAMING.yml`](../../kernel/naming/NAMING.yml) and
[`skills/file-system-object/SKILL.md`](../../skills/file-system-object/SKILL.md):

Big-endian names plus lexical sorting produce **implicit trees with no directories at all** —
`alan-kay.yml`, `alan-kay-soul.yml`, `alan-kay-quotes.yml` cluster in `ls` because the significant
component leads, and the shared prefix *is* a virtual parent. A prefix and a directory are declared
equivalent (`don-hopkins-wish-list.md` ≡ `don-hopkins/wish-list.md`), so grouping is reversible: a
cluster of sidecar files is the lightweight form, and when it earns the weight it graduates into a
directory through a five-stage lifecycle that ends with the rule that a file named like its directory
*is* that directory. Plural directory names declare their element type, and a container can state its
own enumeration and ordering rules while carrying its own `CARD.yml` — so a collection is a typed
object with behavior rather than a bag, and non-conforming files are ignored metadata rather than
errors.

That is the constructive reply to the 80% figure. Those structural links are not *replaced* by the
tree grudgingly; they are replaced by four mechanisms of different weights, chosen per case, none of
which anyone has to author or maintain by hand. What Roam offers instead is one mechanism — the typed
link — priced the same whether the relationship is "these files are about the same person" or "this
idea refutes that one." The first should cost nothing and does. Only the second is worth typing, and
that one is the trail.

### Somebody else's computer

Borretti's footnote on why Notion loses despite being good at the one surviving use case:

> if a tool is to be my second brain, it can't live on somebody else's computer.

Roam is proprietary and hosted. Everything in gwern's linkrot discipline — local archives, mirrored
citations, stable URLs maintained for fifteen years — is the same argument at a longer time horizon:
**a corpus meant to outlive your memory must outlive its vendor.** Git and plain files are not
nostalgia. They are the only part of this stack with a demonstrated multi-decade survival record.

## What we concede outright

1. Most people do not need this, and the design target is explicitly not most people
   ([`hyperties/README.md`](hyperties/README.md#who-this-is-for-and-why-that-is-not-a-hedge)).
2. Hand-maintained knowledge graphs are a losing proposition and always were.
3. A plugin bazaar over a mediocre core is worse than good single-purpose apps.
4. Organizing for its own sake is waste. *"I can always find what I need... It is a waste of time to
   organize things too much."*
5. Building the engine is more fun than shipping the game, and that is a trap with our name on it.

## The reply, which is not a refutation

Alan Kay, in email to Don, opening an answer about why MVC was still standing thirty-two years after
nobody could say what a controller was:

> Things seem to hang on in computing just because they work a little bit.

That is the whole argument for doing this, in eleven words. The reason the web has jump links and no
transclusion, the reason no system in this hub has synonyms, the reason MVC outlived its own authors'
interest in it — none of it is that these were the good designs. It is that they worked a little bit,
early, and a little bit is enough to become the floor everyone else builds on. Borretti's "adequate
single-purpose apps" and Kay's "work a little bit" are the *same observation* with opposite morals:
he concludes settle, Kay concludes that settling is the mechanism of the disease.

Don pairs it with the standard to be held to:

> It is an unworthy design objective to aim for anything less than trying to do to the Macintosh what
> the Macintosh did to the previous state-of-the-art. — **Bill Buxton**

**And it cuts at us too, which is why it lives in the objections file rather than the hub.** A
half-working webtop that works a little bit is not exempt from Kay's lament; it is a candidate for
it. The line is not a permission slip to build something mediocre and novel instead of something
mediocre and popular. It is the reason the honest-costs discipline and Borretti's pinned charge —
*a year, and no game on the algebra* — are in this directory at all.

Provenance: Kay's email quoted verbatim by Don on
[Reddit, 2011](https://www.reddit.com/r/programming/comments/qs3zp/for_those_starting_with_the_model_view_controller/)
and again on [Hacker News, Jan 2015](https://news.ycombinator.com/item?id=8841428). Full text and
the rest of the email — watchers instead of controllers, the unsolved "automatic inverter" for
dimensions lost when a view is made, HyperCard-style end-user view construction — in
[`characters/alan-kay/media/discussions/hn-mvc-morphic-watchers-2015.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/alan-kay/media/discussions/hn-mvc-morphic-watchers-2015.md).
The watchers idea is upstream of Temkin's push-based constraints: a view that cannot affect what it
views is what Declare enforces at compile time. See [`temkin/`](temkin/README.md).

## Ground Up Software

Gwern's prescription:

> You need to rethink the entire system and rewrite it from the ground up on the basis of making
> neural nets do as much as possible... it would be better to start with a clean sheet (and an empty
> cap table).

Don's one-man company is named **Ground Up Software** — like coffee beans, or hamburger — and every
repo in this constellation lives under a directory called `GroundUp/`. The empty cap table is
literal.

Which is either the funniest possible coincidence or evidence that the diagnosis was obvious to two
people who had been carrying the same complaint for decades. Both readings are fine. Neither is a
reason to skip Borretti's objections.

↑ [webtop hub](README.md)
