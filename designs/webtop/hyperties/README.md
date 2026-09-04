# HyperTIES: the parts that already worked together

This is not nostalgia and it is not a survey. It is a parts list from a system Don built and used,
where the parts were **designed to fit each other**, and which has not been equalled since on the
one axis that matters here: browsing a large corpus without losing your place.

## This pack

| File | What it is |
|---|---|
| **README.md** (this file) | The parts list, and the argument for who it is for |
| [**ARTICLE-SCHEMA.md**](ARTICLE-SCHEMA.md) | **Start here.** Title, synonyms, description, body — the four-part node contract, sourced from the storyboard markup. It is the semantic pyramid with an addressing layer, and it was mandatory |
| [**LINK-RESOLUTION.md**](LINK-RESOLUTION.md) | The protocol: **two link syntaxes** — `.~ phrase~` in the FORTH prototype, where the space was required by the FORTH word parser, and the clean `~phrase~` in Weiland's final C version, which is the one to revive; the inline prose form is 798 of 830 uses in the archive; Weiland's three typed index namespaces generalized to MOOLLM's plural containers; scope-walking resolution as Self-style delegation; ambiguity as a pie menu or a definition editor; resolution as ranked results scored like Sims advertisements; the collision lint spec and its canonicalization equivalence class; and the build-time index that makes a published corpus browse with no server and no API key |
| [**EMACS-INDEX-MANAGER.md**](EMACS-INDEX-MANAGER.md) | The MockLisp authoring tool, reverse engineered from `yahtittie.ml` and a master index dated 10 July 1988. A **stack** of scoped typed indexes searched innermost-first — the same algorithm as the MOOLLM §14 discovery rule; `narrow-to-sub-index` pluralizing a singular type name to find or create its container, which is the plural-container rule in 1988 code; per-namespace completion lists rebuilt top-of-stack-first, the ancestor of ranked-advertisement resolution; `new-synonym` refusing duplicate claims, which is half the lint we need; and `canonicalize` stripping the tilde as whitespace, so `~Founders~` *is* `founders`. Plus the **buffers-as-objects** finding: MockLisp had arrays but no dictionaries, so the per-buffer abbrev table was repurposed as one — with `abbrev-mode 0` to disable the typing behavior, the buffer text holding the key set and the abbrev table holding the map, and dictionary buffers named `owner:space` (`master-index<2>:articles`) so a name encodes scope frame *and* type namespace. A persistent dictionary in a language with no dictionaries, which is MOOLLM's own architecture thirty-eight years early. Includes the surviving note-to-self — *"Make synonyms use the abbrev mechinism"* and `define-hooked-local-abbrev` to make `.commands` prompt for arguments with completion over known names, neither of which was built |
| [**FOCUS-FLOW.md**](FOCUS-FLOW.md) | Reveal-all-links plus the missing dimension, order: OpenLaszlo's animated chevrons between tab stops applied to the whole focus sequence, text and pop-out image targets on one path, with the 1991 paper's own "slight movement... readily detectable to the eye" as the argument that the motion is load-bearing |
| [**HN-ARCHIVE.md**](HN-ARCHIVE.md) | Don's Medium archive of the HN threads and Shneiderman correspondence, **distilled** — sorted by claim, receipts attached, redundancy collapsed |
| [**TEAM.md**](TEAM.md) | Shneiderman's lab: who did what, over a decade, with the timeline and the papers |

Primary source: [HyperTIES Discussions from Hacker News](https://donhopkins.medium.com/hyperties-discussions-from-hacker-news-937d156f0330),
Don Hopkins, Medium, 13 January 2022 — 74 minutes of "rough wall of text and redundancy" that he
never had time to distill. [`HN-ARCHIVE.md`](HN-ARCHIVE.md) is that distillation; the Medium post
stays canonical for anything not carried over.

Paper of record: *Designing to Facilitate Browsing: A Look Back at the Hyperties Workstation
Browser* — Shneiderman, Plaisant, Botafogo, Hopkins, Weiland, *Hypermedia* 3:2 (1991) 101–117.
Source, papers, and scans: [donhopkins.com/home/ties/doc/ties/](https://donhopkins.com/home/ties/doc/ties/).

## Who this is for, and why that is not a hedge

Gwern's argument against personal knowledge systems is correct and it does not apply to us:

> This is what people always miss about Zettelkasten: are you writing a book? Are you a historian or
> German scholar? Do you publish a dozen papers a year? No? Then why do you think you need a
> Zettelkasten? If you are going to be pulling out a decent chunk of those references for an essay
> or something, possibly decades from now, then it can be worth the upfront cost...

Yes. A dozen a year, references pulled out decades later, a corpus that has to survive its author's
memory. Don has that. Gwern has that — and says so in the same breath in the Xanadu footnote: *"I am
willing to do this work in part to explore website design, but the idea that many websites should be
like English Wikipedia or Gwern.net is crazy."*

So the design target is **not** most people. It is the long-tail writer with decades of corpus, for
whom the upfront cost has already been proven worth paying — by both of them, independently, for
twenty-plus years. Everything downstream follows from refusing to design for mass adoption. Build
what the two of us already need and already pay for by hand; if the LLM lowers the cost enough that
the audience widens, good, but that is a consequence and not the goal.

The ambition, stated plainly: make it good enough that **gwern could run his own site on it** — not
by porting him, but by [endosymbiosis](../../object-system/ENDOSYMBIOSIS.md). Engulf without
digesting. His publishing organism keeps its own membrane, metabolism, and voice, and gains a shell.

## The parts list

Each of these shipped, in 1988, on a Sun workstation, in one system.

### Definition previews — the killer feature the web never got

> Every HyperTIES article had a short definition summarizing its contents, and single clicking on a
> link would show that definition at the bottom of the screen without leaving the current context.
> Double clicking followed the link, and a stroking gesture left or right with a pie menu would open
> the link up in different windows. ([`37200319`](https://news.ycombinator.com/item?id=37200319))

And the complaint, unchanged since:

> definition previews (sorely missing from the web: a way to read the definition of a link
> destination without actually following the link and losing your context)

This is gwern's popup, thirty-plus years earlier, with one difference that matters: the definitions
were **hand-written by the author** as part of authoring the article. Every article carried its own
abstract because writing one was part of writing the article.

**What changes now:** the LLM drafts the definition; the author edits or overrides it. The upfront
cost that made this unaffordable for anyone but a funded lab is the exact cost gwern's footnote says
LLMs remove. Authored-when-it-matters, generated-when-it-does-not.

### Click the background, see every link at once

From the 1991 paper:

> when confronted with an image with hidden targets, they tend to sweep across the image until a
> target is highlighted (becomes designated), or try to select what they think might be a target
> until one is found. This suggested that the system could highlight all of the targets
> automatically (for a short time) whenever it appears that the user is searching for targets, as
> when sweeping the display, or clicking in non-target areas. This latter strategy has been
> implemented in the NeWS version of Hyperties. Whenever a user attempts to select in a
> non-selectable region (like the background), all targets are revealed. **This technique was found
> effective and generally very well received by users.**

Don's version of the same:

> HyperTIES had a feature that you could click or press and hold on the page background, and it
> would blink or highlight ALL of the links on the page, either by inverting the brightness of text
> buttons, or by popping up all the cookie-cut-out picture targets (we called them "embedded menus")
> at the same time, which could be quite dramatic with the three Sun founders!

Note the design logic: the affordance is triggered by the *failure* gesture. Clicking nothing is
reinterpreted as asking "what is here?" That is the same move as a pie menu popping up under the
cursor on a press with no target — the null action becomes the discovery action.

### Embedded menus and pop-out targets

Links inside images, shaped by arbitrary PostScript paths, that pop out with a drop shadow when
pointed at — the Hubble Space Telescope demo, and a photo of the three Sun founders where each head
was a target. Cookie-cutter cutouts, not rectangles.

### Pie menus for multi-window navigation

A stroke left or right off a link routed it: same window, other window, new window. Navigation
*direction* expressed as gesture direction. Paging, open-in-other-window, show-definition, edit, and
command dispatch all lived in the same radial vocabulary, which is why they did not fight each
other — one gesture space, saturated deliberately.

### Embedded interactive applets, scriptable, in the page

> The coolest part was that you could script and configure reusable embedded NeWS "applets" in
> PostScript, like custom pie menus for font selection and other commands, text editors, user
> interface widgets, PostScript driven animations, interactive popup targets, buttons that sent
> commands to NeWS, Emacs, FORTH, the Unix shell, etc, not unlike Java applets or web components
> that web browsers eventually supported.

Three languages, on purpose: FORTH for the markup interpreter and formatter, PostScript for the UI
and applets, Emacs MockLisp for the authoring tool. Gosling's editor and Gosling's window system,
years before Gosling's Java did the same job worse.

### Authoring that a normal person could do

The markup language was designed against SGML precisely because SGML needed tooling: *"great for
publishing Boeing's 747 reference manual, but not for publishing poetry and cat pictures."*

It had macros, conditionals, and one detail worth stealing outright:

> shared definitions, kind of like style sheets (but using the same markup language, **not one
> language for markup and another for style**)

One language for content and presentation. The modern equivalent is YAML jazz carrying both, and
Declare expressing layout in the same notation as data.

### Storyboard compilation

Each article compiled to a FORTH word, threaded, dumped to a restartable binary image so pages came
up pre-formatted and instant — *"kind of like partial evaluation, and Smalltalk VM images."* The
webtop equivalent is a build step that pre-renders pyramid rungs so a zoom is a lookup, not a
generation round-trip.

### Article synonyms

Don's recollection: articles carried synonyms, so inline prose could link to an article by any of
its names and resolve correctly — link-by-meaning rather than link-by-path.

*Not yet sourced.* It is not in the Medium roll-up or the 1991 paper text checked so far; it needs a
citation from the TIES/HyperTIES documentation before it goes in anything public. Recorded here as
a claim to verify, because the feature matters: it is the ancestor of aliasing a node so that
[[wiki-style]] links, tags, and prose references all land on one canonical thing.

## The claim: these were one design, not a feature list

Definition previews only work because every article has a definition, which only works because
authoring makes writing one natural, which only works because the authoring tool is in the same
system as the browser. Pie menus only pay off because there are many windows to route into. Clicking
the background only makes sense because links are visually embedded rather than uniformly underlined.

Each part assumes the others. Pull one out and it looks like a gimmick — which is precisely what
happened as the web reinvented them one at a time, decontextualized: tooltips without abstracts,
tabs without gestural routing, previews without authoring, applets without a shared language.

> All this needs to be intentionally designed to fit together and synergize.

That is the brief. The webtop is not "add popups to a site." It is reassembling a system whose parts
were mutually justified, adding the one ingredient that was not available in 1988 — a machine that
can write the definitions, generate the intermediate rungs, and keep the corpus from rotting — and
then letting other people point it at their own content.

## The reunion

Don has used each of these systems and each embodied a different subset: HyperTIES (previews,
embedded menus, applets, authoring), NeWS/HyperLook (windows as scriptable objects, pie menus
everywhere, live editing), UniPress Emacs on NeWS (tabbed windows plus pie menus plus scripting as
one IDE), Frontier (outline as code and data, object DB, view state in the document), gwern.net
(popups as windows, annotation, local archives, semantic zoom), Declare and Mesa (constraints,
zoomable spatial canvas shared with an agent).

None of them ever met each other.

↑ [webtop hub](../README.md) · [gwern](../gwern/) · [winer](../winer/) ·
[view state as commentary](../../pie-stack-views/VIEW-STATE-ANCESTORS.md)
