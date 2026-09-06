# HyperLook: HyperCard for NeWS, and the browser that should have been

**In 1992 you could flip a running copy of SimCity into edit mode, point at the transportation-fund
slider, open its property sheet, read the script that sent `SetTransportationFund` to the stack, and
change it — while the city kept simulating.** That shipped. It is the webtop thesis with a
thirty-four-year-old receipt, and most of what this design cluster argues for is an attempt to get
back to it on a substrate that did not die.

## The lineage, with the credit straight

| When | What | Who |
|---|---|---|
| 1987 | **HyperCard** — stacks, cards, direct-manipulation editing, HyperTalk for everyone | Bill Atkinson, Apple |
| — | **NeWS** — PostScript as code, graphics *and* data; networked, extensible, multithreaded | James Gosling, Sun |
| early 1989 | **GoodNeWS** — HyperCard's ideas rebuilt on NeWS and given away free on the nascent internet | **Arthur van Hoff**, Turing Institute, Glasgow |
| ~1990–91 | Renamed **HyperNeWS** | van Hoff and colleagues |
| 1992 | **HyperLook** — productized for Sun's OpenWindows X11/NeWS: TNT and OPEN LOOK components, shared-memory image views, a sound mixer server, a stripped non-editable runtime for shipping products | van Hoff **and Don**, who moved his SparcStation 2 to Glasgow for it |
| 1992 | **SimCity for HyperLook**, released alongside it so each demonstrated the other | Don, on Maxis's game |
| later | **Bongo** — a Java GUI toolkit and interface editor inspired by HyperCard *and HyperLook*, shipped over Castanet | van Hoff at Marimba |

**HyperLook was designed by Arthur van Hoff.** Don joined in 1992 to help turn HyperNeWS into a
product, ported SimCity to it, and wrote the Cellular Automata Machine and Happy Tool. That
distinction matters and is easy to blur, because the SimCity demo is the most-seen artifact.

## Alan Kay on what Apple blew

Quoted in Don's own HyperLook article:

> "I thought HyperCard was quite brilliant in the end-user problems it solved. (It would have been
> wonderfully better with a deep dynamic language underneath, but I think part of the success of the
> design is that they didn't have all the degrees of freedom to worry about, and were just able to
> concentrate on their end-user's direct needs.
>
> "HyperCard is an especially good example of a system that was 'finished and smoothed and
> documented' beautifully. It deserved to be successful. **And Apple blew it by not making the design
> framework the basis of a web browser** (as old PARC hands advised in the early 90s …)"
>
> — Alan Kay

More of his argument — the browser as an operating system rather than an app, *symmetry* as the
property that matters, and his two criticisms of Don's own work — is collected in [kay/](kay/).

That last clause is this whole cluster's thesis, stated by someone with standing, decades ago. The
web we got is a document viewer that grew scripting; the web we could have had was an authoring
environment that grew documents. **HyperLook is the closest anybody came to shipping the second
one**, and it ran on a window system that lost.

Pair it with Kay's other line — *things that only kind of work tend to hang on* — and you have both
halves: the browser only kind of works, and it hangs on.

*(Provenance: quoted by Don in the Medium article below. Original venue — mailing list, email,
forum — should be pinned down before this is cited as a primary source.)*

## What it had, item by item, and where each one lands here

### Edit mode, at any time, while running

> "Now I'll flip this into edit mode, while the program's running. That's a unique thing. […] this
> reset button here is just a user interface component that I can move around, and I can hit the
> 'Props' key, and get a property sheet on it."

No separate authoring tool, no build step, no mode you leave the application to enter. The document
and its editor are the same artifact. This is what [TREE-NAVIGATION.md](TREE-NAVIGATION.md) is
reaching for when it insists edit mode be a first-class state rather than a different program.

### The stripped runtime is the compilation thesis, already shipped

HyperLook had a **non-editable stripped-down runtime** for publishing commercial products — which is
how SimCity went out. The authoring environment was fully live and reflective; the published artifact
was sealed and fast.

That is exactly the **crystallize / melt** split in
[`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md): the expensive, dynamic, self-modifying
version is what the author works in, and the thing readers get is compiled and closed. The design
cluster arrived at that independently. HyperLook billed for it in 1992.

### Metacircular property sheets

**Every property sheet was itself a HyperLook stack.** So editing the interface used the same
mechanism as editing anything else, and you could edit the property sheets — or write new ones for
object types you invented. One tool, all the way down, which is the argument
[DIRECTORY-AS-OBJECT](../../kernel/DIRECTORY-AS-OBJECT.md) makes about the filesystem being the only
mechanism.

### Delegation with a network tier

HyperCard's chain was Object → Card → Background → Stack. HyperLook added one:

> Object → Card → Background → Stack → **Client, over the network**

A message unhandled locally travels outward, and the last resort is a remote process that can reply
by addressing any stack, background, card, or object **by a path of names**. Local negotiation with a
remote fallback, addressed by name rather than pointer — the same shape as
[`DIRECTORY-AS-IUNKNOWN.md`](../DIRECTORY-AS-IUNKNOWN.md), and name-addressing is the HyperTIES
resolution argument arriving from a second direction.

### Warehouses: a prototype library that is just a document

> "This clock stack is a warehouse of objects […] I hit the 'Install' button, this now installs them
> into the user interface editor. […] That 'Install' button has added this 'Neat Clocks' submenu to my
> edit menu."

Any stack could be declared a warehouse; its pages became submenus of the *New Object* menu, each
page a category. You made a new prototype by copying an existing object, naming it, and customizing
its properties and script.

**A plugin was a document you opened.** Not a registry entry, not a build artifact, not a manifest —
open the file and its contents appear in your tool palette. That is the plural typed container idea
with a 1992 implementation, and it is a better answer than anything COM shipped.

### PostScript as the three axes at once

Programming, graphics, and data in one language — Don calls it "the three axes of AJAX," and NeWS was
architecturally AJAX-shaped years before the acronym. Practical homoiconicity rather than the
theoretical kind: see [`../object-system/HOMOICONICITY.md`](../object-system/HOMOICONICITY.md).

### PdB: the dual path, again

People complained about scripting in PostScript, so van Hoff wrote **a C-to-PostScript compiler**.
One system, two entry points: a dynamic interpreted path and a compiled typed one. Which is OLE's
dual interfaces, and the LLM-at-build-time-versus-read-time split, and the stripped runtime, all
being the same idea for the third time on this page.

## Why this is the strongest card for gwern.net specifically

Gwern.net is a **statically compiled corpus with a dynamically composed chrome layer** — the
architecture note says so. HyperLook is the same shape with one difference that changes everything:
**the chrome was editable from inside, by the reader, at runtime, using the same tool that built it.**

So the question to put to him is not "should documents be programmable," which invites a shrug. It is:
*your popup system is a window manager, your annotations are a second corpus, and your build is a
compiler — you have already rebuilt three quarters of HyperLook. What would it cost to let a reader
open the property sheet?* And the honest follow-up is the reason it might be a bad idea: the stripped
runtime existed because live editability and publishable stability are genuinely in tension, and he
has chosen stability deliberately.

## Honest costs, including Don's own verdict

- **NeWS lost.** Every bit of this ran on a window system that no longer exists, which is the whole
  argument for git and static files as the substrate this time.
- **Don's own assessment, from the article:** HyperCard also inspired Scratch, Snap!, and Lively
  Kernel, "which go much further than HyperLook ever did in many ways," using Smalltalk or JavaScript
  rather than HyperTalk or PostScript. The lineage is not a claim of superiority.
- **Kay's actual criticism of this work, which lands.** He read Don's NeWS and HyperLook material and
  replied that his "only real regret about this terrific work is that **your group missed the
  significance for personal computing of the design of Hypertalk in Hypercard**" — that Winkler and
  Atkinson broke rules of good language design but built "the first overall system in which end-users
  'could see their own faces'." **PdB is the evidence he was right:** HyperLook chose PostScript,
  users declined to write it, and van Hoff had to ship a C compiler so they could avoid the scripting
  language. A dynamic language end users won't write is not an end-user authoring system, whatever
  else it is. The full exchange is in [kay/](kay/).
- **Kay's caveat cuts at HyperLook too:** HyperCard partly succeeded *because* it lacked degrees of
  freedom. HyperLook added the deep dynamic language Kay wished for and did not inherit HyperCard's
  audience, which is evidence for his point rather than against it.
- **Live editing has no version control story.** Flipping a running program into edit mode and
  changing it is wonderful and leaves no record of what you did. The webtop's answer is that the
  substrate is git, so the edit is a commit — the thing HyperLook could not offer.

## Sources

- [SimCity, Cellular Automata, and Happy Tool for HyperLook (nee HyperNeWS (nee GoodNeWS))](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) — the main article; the Kay quote and the feature-by-feature comparison to HyperCard
- [HyperLook SimCity Demo Transcript](https://donhopkins.medium.com/hyperlook-simcity-demo-transcript-17f627eab14a) — the live demo, filmed by **Abbe Don** at the San Francisco Exploratorium; source of the edit-mode and warehouse quotes
- [donhopkins.com/home/catalog/hyperlook/](https://www.donhopkins.com/home/catalog/hyperlook/index.html) — the archive: README, product and technical info in PostScript, the runtime tarball, SimCity for HyperLook, demo images
- [HyperTIES Discussions from Hacker News](https://donhopkins.medium.com/hyperties-discussions-from-hacker-news-937d156f0330) — the HyperCard → GoodNeWS → HyperLook → Bongo chain in Don's own words
- [`../VISUAL-PROGRAMMING-LINEAGE.md`](../VISUAL-PROGRAMMING-LINEAGE.md) — where this sat before it had a document of its own

## Related

- [hyperties/](hyperties/) — the *other* 1988 system Don worked on, and the two are complementary: HyperTIES had the article schema and name resolution, HyperLook had the editable object model
- [temkin/](temkin/) — Declare and Mesa: the same in-browser argument, thirty years later
- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — SimCity-in-a-stack is the receipt that a document environment can host a live simulation
- [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) — crystallize and melt, which the stripped runtime already implemented
- [`../pie-stack-views/README.md`](../pie-stack-views/README.md) — pie menus were in this system too

↑ [webtop hub](README.md)
