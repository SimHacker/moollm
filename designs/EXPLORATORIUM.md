# The Exploratorium

> The site is an exploratorium. Not a museum with better JavaScript.

Frank Oppenheimer opened the Exploratorium in 1969 in San Francisco's Palace of Fine Arts,
and the choice of word was the whole argument. A museum has a collection and the visitor is a
witness to it. An exploratorium has phenomena, and the visitor is the one who makes them happen.
Nothing is behind glass, because behind glass it does nothing.

That is the model for this site, and naming it is most of the work. Everything below is either
what the word already carries or a note on what it forbids.

## Each property of the building lands on the site as a constraint

Each of these is a real property of the place, and each one lands on the site as a constraint.

| The building | The site |
|---|---|
| No velvet rope. The exhibit is broken by hands all day and built to be. | A page that cannot be poked, rearranged, opened up or taken apart is a brochure. Read-only is the degraded mode, not the default. |
| The machine shop is on the floor, in view. Exhibits are built and repaired where visitors can watch. | View source is not a footer link. The shop is visible from the exhibit, and the path from looking to changing is short enough to walk while curious. |
| Explainers play alongside you. They are young, they are not lecturing, and they do not know everything. | Guidance from inside the activity, not above it. No authority voice. |
| "No one ever flunks a museum." — Frank Oppenheimer | There is no wrong input and no failure state. Breaking something is a result, and an interesting one. |
| The Cookbooks: three volumes of exhibit plans, published so any other museum could build them. | The GitHub backing store *is* the Cookbook. Publishing the plan alongside the thing is the original practice, not a modern nicety. |
| It is loud. The ambient sound is delighted screaming. | The felt target. A quiet room means the exhibits are behind glass again. |

The Cookbooks deserve the emphasis. In the 1970s a museum published its exhibit recipes so
competitors could copy them, for the reason that more people playing with the phenomenon was the
entire point. That is the disposition this whole repository is built on, arrived at independently,
fifty years earlier, by people building plywood and mirrors instead of files.

## Why this document names no exhibits

Deliberately, and the reason is the interesting part.

**Examples become the spec.** Write down three exhibits and those three are what the word means
from then on. Everything proposed afterward gets measured against them instead of against the
phenomenon it is supposed to elicit. The frame collapses into a checklist of the first ideas
anyone happened to have.

**Any example is worse than the thing it names.** "Exploratorium" already invokes the room, the
noise, the kids, the smell of the machine shop. A list of scenarios replaces all of that with a
to-do list, and a to-do list has never made anyone shriek.

**Building the exhibit is the fun.** Enumerating them here takes other people's turn. The word is
an invitation, and an invitation that arrives pre-answered is a work order.

**The pressure to enumerate is strong and should be resisted on purpose.** Anything asked to
elaborate this frame — human or model — will immediately want to sketch concrete benches, because
sketching benches is easy and holding a frame open is not. Notice the urge and decline it. The
idea that the site is an exploratorium is enough, and it is better undiluted.

## What a candidate has to have

Properties, not scenarios. If something is proposed for this site, these are the questions, and
they can be answered without anyone having named a single exhibit in advance:

- Does it do nothing until someone acts on it?
- Can the visitor break it, and does breaking it teach the thing?
- Is there any input that counts as wrong?
- Can it be understood by playing, before and without reading?
- Is the plan published next to it, so someone can build their own?
- Would a room full of people using it be loud?

Six yeses is an exhibit. Anything less is a page, and pages are fine — they are just not the point
of the building.

## Lineage

- **Frank Oppenheimer**, physicist, founded the Exploratorium in 1969 in the Palace of Fine Arts;
  the museum moved to Pier 15 in 2013. The Explainer program and the open machine shop are his
  design, not later additions.
- **The Exploratorium Cookbooks** (I, II, III) — exhibit plans published for others to build.
- **Seymour Papert** — constructionism and microworlds, the same claim from the education side:
  you learn the phenomenon by building with it, not by being shown it. Already load-bearing
  throughout this repository.
- **HyperLook SimCity** was demoed on that floor, filmed by Abbe Don at the Exploratorium. The
  interactive lineage this site is trying to continue was literally exhibited in the building the
  site is named after. See [webtop/HYPERLOOK.md](webtop/HYPERLOOK.md).

## See also

- [webtop-gwern-inheritance/TWO-LAYER-VIEW-SOURCE.md](webtop-gwern-inheritance/TWO-LAYER-VIEW-SOURCE.md)
  — the publication architecture this is the disposition of
- [GITHUB-AS-MMORPG.md](GITHUB-AS-MMORPG.md) — the substrate, and the Cookbook made literal
- [QUOTES.md](QUOTES.md) — attributed playback, for exhibits that put words in the room
- [webtop/HYPERLOOK.md](webtop/HYPERLOOK.md) — browse mode and edit mode, demoed at the Exploratorium
