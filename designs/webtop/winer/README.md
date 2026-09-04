# Winer, outliners, and the tree that eats JSON

Dave Winer's line — ThinkTank, MORE, Frontier, Aretha, Manila, Radio UserLand, RSS, OPML, XML-RPC —
is the strand of the webtop that is about **structure**: outline as syntax for code *and* data, an
object database that is itself the outline, view state stored in the document, and scripting present
at the shell level rather than bolted onto one app.

Don has been making this argument on Hacker News since 2014, in pieces, across dozens of threads,
re-quoting himself each time. This directory deduplicates it into one statement and connects it to
what the argument turned into: **YAML jazz, MOOLLM, and the webtop.**

Full annotated index of the posts: [`HN-POSTS.md`](HN-POSTS.md) — 71 confirmed comments, 39 of them
naming Winer or a UserLand product, 2014-05-11 through 2026-09-03.

## The canonical statement

Posted first on 13 July 2019 ([`20425970`](https://news.ycombinator.com/item?id=20425970)) and
re-posted or re-linked at least six times since — the load-bearing paragraph, once:

> The thing that's missing from "Google Docs" is a decent collaborative outliner called "Google
> Trees", that does to "NLS" and "Frontier" what "Google Sheets" did to "VisiCalc" and "Excel". And
> I don't mean "Google Wave", I mean a truly collaborative extensible visually programmable
> spreadsheet-like outliner with expressions, constraints, absolute and relative xpath-like
> addressing, and scripting like Google Sheets, but with a tree instead of a grid. That eats drinks
> scripts and shits JSON and XML or any other structured data. Of course you should be able to link
> and embed outlines in spreadsheets, and spreadsheets in outlines, but "Google Maps" should also be
> invited to the party (along with its plus-one, "Google Mind Maps").

Where it has been posted, so nobody re-derives the list:

| Date | Thread | Post |
|---|---|---|
| 2019-07-13 | I was wrong about spreadsheets | [`20425970`](https://news.ycombinator.com/item?id=20425970) — the original |
| 2019-08-23 | A Pissed-Off Tutorial for Google Wave | [`20773851`](https://news.ycombinator.com/item?id=20773851) |
| 2019-10-06 | Representing and Editing JSON with Spreadsheets | [`21170434`](https://news.ycombinator.com/item?id=21170434) — Don's own index post |
| 2019-12-08 | Learning to code vs. learning to automate | [`21736782`](https://news.ycombinator.com/item?id=21736782) |
| 2022-03-31 | Excel 2.0 — better visual data model than a grid? | [`30871497`](https://news.ycombinator.com/item?id=30871497) |
| 2026-07-23 | Malleable computing, Emacs, and you | [`49022707`](https://news.ycombinator.com/item?id=49022707) — index post, second generation |

Two of those are already hand-made index posts. This directory is the permanent version of the thing
Don keeps rebuilding by hand in comment boxes.

## The lineage, compressed

**ThinkTank** (Winer, his brother Peter, and Doug Baron; Apple ][, keyboard-driven) → **MORE**
(Mac, 1986; drag-and-drop rearrangement without spoiling the keyboard interface; outlines rendered
as formatted charts and slide shows) → **Frontier** (UserLand, 1.0 in January 1992; UserTalk;
object database; the only system-level scripting environment on the Mac at the time) → **Aretha**
(May 1995, Frontier released free and repositioned for the web after AppleScript took the OS
namespace) → **Manila** and **Radio UserLand** (programmable blogging and podcasting: dynamic HTTP
server, static generator, structured XML editing, RSS publication, XML-RPC client and server, OPML
import/export).

Don's summary of the crucial move, from the 2019 post:

> After the success of MORE, he went on to develop a scripting language whose syntax (for both code
> and data) was an outline. **Kind of like Lisp with open/close triangles instead of parens!**

And the receipt that UserTalk was a real OS-level citizen rather than an app macro language, from
2026 ([`49022707`](https://news.ycombinator.com/item?id=49022707)):

> UserTalk wasn't bolted on. It was registered as an OSA dialect: Script Editor, HyperCard, Nisus
> ("Do Script"), and other OSA hosts could run UserTalk, not only Frontier. ... syntax is an outline
> (code and data are the same tree); object DB + interpreter + outliner in one app; and one of the
> most complete Apple Events client/server stacks on the Mac.

## What we inherit

### 1. Outline as syntax for code and data — this is YAML jazz

Frontier's syntax was the outline, for both program and data, a decade before JSON and two before
YAML got used this way. **YAML jazz is that idea with comments promoted to first-class semantic
data.** Same polymorphic tree, same code-and-data-are-the-same-shape, same
edit-the-structure-directly ergonomics — now with three audiences (humans, LLMs, machines) instead
of one interpreter.

Frontier's object database, where the persistent store *is* the outline you navigate, is the direct
ancestor of MOOLLM's filesystem-as-navigable-space: directories are rooms, the tree is the database,
and there is no separate schema layer.

### 2. View state belongs in the document

OPML 2.0 puts `expansionState`, `vertScrollState`, and window geometry in the document head. Widely
mocked; correct. Worked out at length in
[`VIEW-STATE-ANCESTORS.md`](../../pie-stack-views/VIEW-STATE-ANCESTORS.md), including what OPML got wrong
(one view per file, unaddressable, uncitable, un-repliable).

### 3. Rearranging the tree is the operation

From the Google Wave thread ([`20780928`](https://news.ycombinator.com/item?id=20780928)):

> One thing an outliner lets you do that you can't do with something like Wave or a tree structured
> discussion group is to arbitrarily rearrange the tree.

Threaded comments freeze structure at post time. An outliner lets a reader *restructure* the
argument, which is why the outliner is the right substrate for accumulating conversation and the
threaded list is not.

### 4. Scripting and outlining belong to the shell, not to one app

The webtop thesis, stated in 2019 before the webtop existed:

> I think the most important point that comes through in Dave's demos is that the operating system
> and user interface shell should support generic outlining and scripting at a very basic, built-in,
> ubiquitous level. But I believe Windows, OS/X, iOS and Android have a hell of a long way to go!

Still true. The webtop is the attempt.

### 5. Hypertext without a scripting language is hyper-crap

The 1999 UserLand Xanadu thread, restated on HN in 2018
([`16226209`](https://news.ycombinator.com/item?id=16226209)):

> It's not which scripting language you have, it's that you have a scripting language at all that's
> important. ... When you try to design something from the start without a scripting language, like
> a hypermedia browser or authoring tool, or even a window system or user interface toolkit, you end
> up getting fucked by Greenspun's Tenth Rule.

HyperTIES shipped with three (Forth for the markup formatter, PostScript for the UI and embedded
applets, MockLisp for the authoring tool). The webtop's answer to "which language" is
**several, plus the LLM** — Declare or Svelte for layout constraints, Python for pipelines, YAML
jazz for structure, and natural language as the outermost dialect.

## What "Google Trees" turned into

The 2019 wish list, item by item, against what now exists:

| Asked for in 2019 | Where it landed |
|---|---|
| Collaborative outliner | Git — branches, review, blame, merge, on a tree of files |
| Expressions and constraints | Declare's `[ ]` / `{ }` constraints; Svelte 5 runes |
| Absolute and relative xpath-like addressing | Stable node paths; the view record's `focus:` and `expanded:` |
| Scripting | MOOLLM skills; the LLM as the outer interpreter |
| Eats and emits JSON/XML/any structured data | YAML jazz in, anything out |
| Outlines in spreadsheets, spreadsheets in outlines | Transclusion at a chosen pyramid rung |
| "Google Maps invited to the party" | eBike Safari — the map *is* an outline layer, with camera in the view record |

The piece that was missing in 2019 and exists now: **the thing that fills in the levels you did not
write.** Gwern's footnote — outliners fail because they foist the hierarchy on the author; LLMs can
generate it while the author writes only what is necessary — is what makes Google Trees buildable
rather than merely desirable. See [`../gwern/`](../gwern/) and
[`../README.md`](../README.md#the-semantic-pyramid).

## The toolbar that spoke his protocols

Don shipped into this world, and the artifact is the most directly relevant precedent in the whole
hub: an **Internet Explorer toolbar for Technorati** that spoke the **Blogger API** and **Atom**.

What it did, in Don's account: bridged blogs, so you could **post to any blog whose API it knew**,
and look things up in **Technorati's database** from the browser chrome. Confirmed contemporaneously
by his 2007 résumé, which lists "Technorati (IE toolbar)" among the consulting work.

Three readings, each load-bearing somewhere else in this hub.

**It was a protocol adapter over other people's corpora, not a personal wiki.** The hub's answer to
Borretti is that this is a *publishing shell* over corpora that already exist
([OBJECTIONS.md](../OBJECTIONS.md)) — and here that answer is not a position, it is something that
shipped around 2004. The Blogger API and its MetaWeblog extension and Atom were mutually
incompatible in detail and identical in intent; a client that spoke all of them made the difference
invisible to the author. Write the post, pick the destination. Winer's protocols were the substrate
that made a bridge possible at all.

**It was endosymbiosis, two decades before the word.** Don put a **browser component inside the
toolbar** and wrote **most of the logic in JavaScript rather than C++**, keeping the native shell
thin and the soft language in charge. That is exactly the arrangement
[`DOMIsland`](../temkin/README.md#domisland-endosymbiosis-with-a-type-signature) formalizes — host
the foreign engine, script it from the language you actually want to write, do not reimplement it —
and exactly the **two-language rule** in [LEGACY-MIGRATION](../../LEGACY-MIGRATION.md). A browser
inside a browser's chrome, scripted.

**Technorati's product was backlinks**, which makes the third reading the sharpest. Technorati's
business was tracking who linked to whom across blogs. A toolbar that queries it about the page you
are currently on is a **backlink overlay on somebody else's document** — peripheral views
([PERIPHERAL-VIEWS.md](../../pie-stack-views/PERIPHERAL-VIEWS.md)) attached to the live web, from
outside, without the page's cooperation. gwern.net has backlinks because gwern controls gwern.net.
This had them for any URL.

**Open question for Don:** was the lookup specifically Technorati's *Cosmos* — the inbound-link view
for a URL — or general search against their index? The backlink-overlay reading above is much
stronger if it was Cosmos, and it should not be asserted until confirmed.

**The source is not in these repos.** Searched by filename and by band-object and blog-API code
markers across every workspace: nothing. What does exist is a physical hanging file labeled
"Technorati" in the Berkeley boxes, per
`characters/don-hopkins/expat/taxes/berkeley-files-index.yml`. Logged as a rescue target.

## Honest about the man

Winer invented or pioneered outliners-as-scripting, RSS, OPML, XML-RPC, blogging, and podcasting.
He is also, by broad account and by Don's own long-running public commentary, difficult — the
DaveNet unsubscribe story ([`36544675`](https://news.ycombinator.com/item?id=36544675)), the
"string them up" reaction to JSON that Crockford recounts
([`35674125`](https://news.ycombinator.com/item?id=35674125)), the RSS `<BLINK>` escaping thread
that Don has now retold on HN at least five times across twelve years.

Both are true and neither cancels the other. Record the work accurately; do not launder the
personality out of it and do not use the personality to discount the work.

## Contact status

There is no `characters/dave-winer/` room in WillWrightShowForFood yet. If one is created it should
inherit this directory as its source material, and the invitation writes itself: *you shipped view
state in a document format in 2000 and got mocked for it; here is the system that finally needed
it.*

↑ [webtop hub](../README.md) · [`HN-POSTS.md`](HN-POSTS.md) · [`data/`](data/)
