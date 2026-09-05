# Dispensers and Souvenirs

*Every document is a dispenser. What you carry out is stamped with where you got it. The stamp is a
ticket, the ticket is an interface to a service, and the whole arrangement deploys onto a map of the
real world.*

Related: [`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) · [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) ·
[`GLYPH-BENCHMARK.md`](GLYPH-BENCHMARK.md) · [`../pie-stack-views/VIEWS-AS-TESTIMONY.md`](../pie-stack-views/VIEWS-AS-TESTIMONY.md) ·
[`skills/urban-safari/`](../../skills/urban-safari/) · [`skills/inventory/`](../../skills/inventory/)

## The reframe

A document-reference object in a room was described here as a *view*: it frames, contextualizes, and
summarizes the document it points at. That is true and it is not enough, because a view you cannot
carry away leaves nothing behind. The stronger reading: **a reference object is a dispenser.** It
holds a view of a document and it *issues* something — one item, or many, from a rack.

The forms are already familiar, which is the point. A **vending machine** with a grid of selections.
A **brochure stand** in a lobby, free, take one. A **single-item dispenser** like Adventure's battery
vending machine in the maze, which exists to solve exactly one problem and knows it. The corpus
already runs several: the church's [`tattoo-dispenser.yml`](../../examples/adventure-4/street/lane-neverending/church-of-the-eval-genius/tattoo-dispenser.yml)
issues short-duration evaluations with a QR code to their analytics, the maze has a
[`lamp-vendor.yml`](../../examples/old/adventure-1/maze/room-j/lamp-vendor.yml), and the
[ACME catalog](../../examples/adventure-4/kitchen/acme-catalog.yml) is a brochure stand with a
mail-order back end. This document names the pattern those instances share and makes it general.

## What a souvenir is

Not a copy of the document. A **stamped, provenance-bearing token** of having been somewhere.

```yaml
souvenir:
  name: "Brochure: The Ordeal of the Rubric"
  emoji: "🔥"
  weight: 0                      # a reference, per skills/inventory
  ref:
    doc: designs/eval/CHURCH-EVAL-GENIUS-DOCTRINE.md
    section: "#4-the-ordeal-of-the-rubric"
  stamp:                         # the part that makes it a souvenir and not a bookmark
    from_dispenser: church-of-the-eval-genius/rubric-forge/ordeal-plate
    from_room: "The Rubric Forge"
    at: 2026-09-04T13:20+02:00
    issue: 1                     # this rack's first
  redeemable: [read, cite, mail, trade, place]
```

Three properties do the work. It is **unique** — issue number and timestamp, so two people's copies of
the same brochure are not the same object. It is **backlinked** — the stamp points home, so the item
knows the room that issued it and the room can be returned to. And it is **weightless**, because it
carries a reference rather than a copy, which is the `TAKE REF` distinction already built into
[`skills/inventory/`](../../skills/inventory/).

The consequence is that **your inventory becomes your itinerary.** A pile of stamped souvenirs is a
record of a path through a corpus, assembled by walking rather than by writing — which is the
[views-as-testimony](../pie-stack-views/VIEWS-AS-TESTIMONY.md) argument arriving from the other
direction. There, what you chose to look at became authored content. Here, what you chose to pick up
does. Both make attention into an artifact, and this one has the advantage that nobody has to be
told it is happening: collecting souvenirs is a thing people already understand and enjoy.

## The souvenir is a ticket, and the ticket is a service interface

The strongest receipt is a matchbook. Text adventures put promotional objects in the world with
mail-in offers printed on them, and mailing one back got you something — Infocom's matchbook ads and
the mail-order joke, Adventure's magazine that scores you a single point for leaving it in the right
place at Witt's End. The corpus already merges these into the **One Lousy Point stamp collection**
([`designs/CHANGES.md`](../CHANGES.md), and the stamp series in
[`skills/adventure/`](../../skills/adventure/)): Woods, Crowther, Scott Adams, each on a stamp worth
one lousy point, which is the entire joke and also a real award.

What matters underneath the joke: **a matchbook is a physical object inside the world that is a user
interface to a service outside it.** You act on the object; something happens elsewhere; a reply
arrives later through a channel the object told you about. That is not decoration, it is a
well-formed asynchronous UI, and it was shipped in 1977.

So souvenirs should *do* things, not merely prove attendance:

| Souvenir | Redeems for |
|---|---|
| Brochure | Reads the section it points at, at the rung you ask for |
| Ticket | Authorizes an action elsewhere — a vault you may now open, a room that admits holders |
| Coupon | Runs a service: recompile the tagsonomy, subscribe to a doc's changes, request a review |
| Stamp | Scores, collects, completes a set; sets are their own reward and their own index |
| Trading card | Hands to another person; the stamp survives the handoff, so provenance is a chain |

A souvenir that redeems for nothing is a checkin badge, and checkin badges are why location games
get boring. The rule: **every dispenser declares what its output does.**

## Why "ticket" and not "object": taking one is instantiation

The word is doing technical work. An ordinary adventure object is a thing that exists and then you
have it. **A ticket does not exist until you take it, and taking it is an `instantiate` with
inheritance from the vendor.**

That single difference is what makes the whole context chain live:

```
your ticket  ──inherits──▶  the vending object  ──located in──▶  the room
                                                                    │
                                        ┌───────────────────────────┘
                                        ▼
                          every other object and character in it,
                          its exits, and its neighbourhood
```

Nothing in that chain is a copy, so **all of it is available as LLM context** by following one
pointer from a thing in your pocket. Which is the actual payoff: a ticket is a **general-purpose way
to carry a piece of annotated, filtered, highlighted context out of a place and hand it to something
else.** Any other object, room, or character can then use it functionally — to perform an action, to
create something, to edit something — and the ticket supplies both the content and where it came
from.

**Entering a place is what grants access.** Being in the room is what puts its objects within reach,
whether they are embedded in the text, sitting in separate files, or inherited from a prototype. The
free ticket every room should dispense is the honest one: *I have read this page, and here is the
title, description, and summary I opened up, with what I found interesting about it foregrounded.*
Minted on the way out, customized, and **editable by the holder** — a souvenir of your own reading,
not a receipt the site wrote about you.

Then it is usable elsewhere. Dropping a ticket somewhere else **makes a link from there to where you
got it, modified by the focus and parameters you added** — so the same source produces different
links depending on what you took from it. And because tickets are typed values, they drop into forms
with typed fields: person-reference inputs, picture-reference inputs, free-text inputs.

**Places are therefore not booleans.** Browser history's entire model of what you did somewhere is
that the link turns purple. A room that dispenses an editable ticket records what you actually took
from it, which is a different fact for every visitor.

### Both kinds of object matter, and `take` is where they differ

Ordinary objects stay ordinary. An apple tree drops apples and then there is one fewer apple; a
pirate drops a unique treasure and it is the only one. Both still point at their own parent
prototypes and contexts, so provenance survives either way. The corpus needs both kinds and should
not collapse them.

The elegant part is that **this requires no new verb.** The generic `take` does everything, because
**dispensers override `take`** — Self- or Korz-style dispatch, not a special case in the parser:

| You `take` | Because the receiver overrides it | You get |
|---|---|---|
| an apple from a tree | no — default `take` | the apple, and the tree has one fewer |
| a ticket from a dispenser | yes | a **new instance** inheriting from the dispenser |
| an ACME catalog from the catalog stand outside ACME HQ | yes, same override | a catalog bound to that stand, that lobby, that company |
| a Leela catalog from the dispenser in the Leela lobby | yes, same override, different vendor | the same mechanism, a different context chain |

Taking the *dispenser itself* is a separate question and should stay hard: it may need a tool, a key,
or permission, or expose a different verb entirely — `unbolt`, or `steal`. And for an admin, it is a
[Korz](../KORZ-LLM-EVALS.md) dispatch along the role dimension: possession is a method slot that
resolves only when the caller's role is admin and the phrase supplies the reflexive — *take the
dispenser itself* — with the parser mapping that adjective into the dimensions, method, and
parameters of the call. The permission is not a check bolted onto the verb; it is which method the
dispatch finds.

## Parameterized dispensers: put your photo in, turn the crank

Here is where this stops being a filing metaphor. A dispenser need not hold a fixed rack of items.
It can hold a **generator with a parameter socket**: insert something of yours — a photo you just
took on your phone, a spoken sentence, the ride you arrived on — turn the crank, and receive an
object that exists nowhere else because nobody else put that in.

This is exactly [Tom Ngo's ECG](GLYPH-BENCHMARK.md#parameterized-glyphs-dont-draw-a-thousand-blend-them)
doing a second job. There, parameterized glyphs solved glyph saturation: instead of drawing a
thousand icons, a designer builds a simplicial complex of a few designed examples and any glyph is a
set of barycentric blend weights over them. A parameterized dispenser is the same machine with a
different input — **your photo supplies the blend weights.** Dominant hue, subject, time of day,
whether it is a canal or a stairwell or a tram: each becomes a coordinate, and the coordinate selects
a point inside a designed space.

That construction earns three things a bare generative prompt cannot:

- **In-distribution output.** Every result is a blend of things a designer built on purpose, so the
  dispenser has a house style it cannot leave. No slop, because slop is outside the complex.
- **Mean regression is impossible.** Blending toward the average is a *coordinate*, not an attractor;
  the vertices stay extreme no matter how many items the rack issues.
- **Inspectability.** The object records its own weights, so *why does mine look like that* has an
  answer you can read, and two souvenirs can be compared by their coordinates rather than vibes.

The crank matters too. A crank is [literalism rather than magic](../../skills/design-sense/masters/randall-smith.md) —
it behaves like a crank, so nothing has to be explained, and the physical act of turning is where the
system admits that generation costs something and takes a moment.

## Deploy it on the real world: eBike Safari

The souvenir layer does not need new infrastructure, because
[`skills/urban-safari/`](../../skills/urban-safari/) already built it. The
[data contract](../../skills/urban-safari/DATA-CONTRACT.md) ingests FIT rides into GeoJSON tracks,
syncs video against GPS with interpolated keyframes, and clusters Whisper transcripts into
`transcript.geojson` so spoken words land at the coordinates where they were spoken. Souvenirs are
**one more layer in that same contract** — `souvenirs.geojson`, points with stamps — and dispensers
are points too, placed at real locations.

So the ride becomes the collection mechanic. You pedal around town; dispensers exist where things
actually are; you insert the photo you just took of the thing in front of you, turn the crank, and
receive an object that **lives in two places at once** — pinned on the map at the coordinate where it
was made, and carried in your inventory because it weighs nothing. Take it somewhere else and drop
it: now there is an object at the new coordinate whose stamp says it came from the old one, which is
geocaching, and `DROP AS BOX` from the inventory skill, and a backlink, all at once.

And the objects are not inert once placed. An article is a room
([`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md)), so a *place* can be a room just as easily — a corner of
town with a `ROOM.yml`, a `CARD.yml` of advertisements, and characters who live there. Souvenirs
placed in it are its furniture. The town accumulates.

### The unification worth noticing

A photographed, GPS-stamped souvenir and a **semantic seed** are the same object.
[`TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) defines a seed as *a GPS-located, timestamped
impression, uninterpreted*, and describes the pipeline that grows seeds into a tagsonomy and then
crystallizes it into a static navigable index. A souvenir is a seed with a face on it.

That means **collecting is authoring.** The pleasant loop — ride, photograph, crank, collect — is the
ingest stage of the tagsonomy compiler wearing a costume that makes people want to do it. Nobody
tags a corpus for fun. Everybody collects souvenirs for fun. Same data.

## A reading list is a curated souvenir collection

The thing gwern.net is missing has the same shape, which is worth noticing before building both:
**shareable reading lists you can remix, check off, annotate, argue with, and hit people over the
head with.** A reading list is a souvenir collection with the wandering edited out — you take the
brochures, throw away the ones that were merely on the way, order the rest, and publish.

Every piece already exists. A list is a file of stamped refs, so it is diffable. **Remixing is
forking**, and a fork's provenance chain is visible, so *this list descends from that list, minus
three items, plus two* is a readable diff rather than a claim. **Checking off** is state on your
copy, which is exactly the reader-state tier that
[`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) already puts in local storage. **Notes** are annotations
attached to a ref, and since refs can drill into sections, a note can attach to the paragraph that
provoked it. And a list has a **glyph rung** like anything else
([`SUMMARY-GENRES.md`](SUMMARY-GENRES.md)) — a contact sheet of its items' emoji, apprehended at a
glance, which is what makes a list shareable as an image rather than a URL.

```yaml
reading_list:
  name: "The Xanadu Thread, Ordered for Actual Comprehension"
  forked_from: someone-else/lists/transclusion-basics
  items:
    - ref: {doc: designs/webtop/hyperties/ARTICLE-SCHEMA.md}
      read: true
      note: "Start here. The four-part schema is the whole idea in one page."
    - ref: {doc: designs/webtop/gwern/README.md, section: "#transclusion"}
      read: true
      note: "Disagree with this. See my note three items down."
```

The argument part needs saying plainly. A list that can be forked with commentary is a **weapon**,
and that is the point — a pillow fight, or an infinite rack of pies, but a fight. Which means it
needs moderation, and the honest answer is that moderation does not scale by algorithm; it scales by
**many mini-dangs.** Hacker News works as well as it does because a person with taste and patience
reads it. Distributing that means many small moderators with real authority over small rooms, each
one's judgment legible and forkable like everything else — if you dislike a room's moderation you
take your souvenirs and open a room, and the fork records the schism. That is not a solved problem
and this document should not pretend it is. But it is a *better-shaped* unsolved problem than global
ranking, because the unit of governance is a room, and rooms are cheap.

## Pokémon without the brand name

Worth being explicit about what is being borrowed, since the borrowing is deliberate.

**Take:** location-anchored collection, because a thing that can only be got *there* makes there
matter. Sets and completion, because a set is an index that feels like a goal. Trading, because
provenance chains are more interesting than possessions. Growth through use — a souvenir you have
redeemed, annotated, and carried is visibly different from a mint one.

**Leave:** artificial scarcity, timed events, gacha odds, and the walled garden. Also leave the
engagement loop, which is the part that makes these games feel like a job.

The real difference is ownership. Your souvenirs are files in your own repository, made from your own
photographs, stamped with your own rides, and readable without the app that made them. If the
service goes away you still have the collection — which is the linkrot argument from
[`gwern/`](gwern/) applied to play, and the reason this is worth building rather than merely enjoying.

## The optical dispenser: retrofitting links onto a runtime that has none

The cheapest dispenser needs no cooperation from its host at all. Don proposed it for The Sims 1 in
2026 and Steve Alvey — 26 years into shipping Sims content — took it up immediately: **an object
displays a QR code, either as an in-world sprite or as a bitmap in its About dialog, and you point
your phone at the screen.**

The Sims 1 has no browser, no clipboard bridge, and no URL type. It does not need any, because **the
resolver is the player's phone, and the host application never has to know.** The screen is the wire.
That generalizes past games: any closed, finished, un-modifiable runtime that can draw a bitmap can
be given hypertext after the fact, by an author with no access to its source.

**It reads exactly as a dispenser.** The object issues a ticket, the ticket points back at the object
that issued it, and you carry it out of the room on a device the room knows nothing about. The
[instantiation-with-inheritance](#why-ticket-and-not-object-taking-one-is-instantiation) story is
unchanged; only the transport is unusual.

**Why nobody did it, which is the interesting part.** The Sims 1 shipped in 2000. QR codes existed —
Denso Wave, 1994 — but phone cameras were not practical scanners until around 2010, and OS-level
scanning came later. So this is not an oversight anyone should feel dumb about: **it was impossible
while the platform was current, and became possible only after the platform was finished.** Dead
runtimes can acquire new affordances. That is worth generalizing on its own.

**The pedagogical version beats the promotional one.** Don's framing was creator attribution — link
back to my site. Alvey's counter, arrived at unprompted, was to link to *what the object teaches*,
so a player can scan a prop and be taken to the real thing behind it. That turns the QR code into a
**citation apparatus for a simulated world**: every prop footnoted and followable to its real
referent. A game world where you can scan a plant and get its sources is doing something gwern.net
does with links and no game has ever done with objects.

Constraints, since they shape the design rather than merely limiting it:

| Constraint | Consequence |
|---|---|
| 800×600 host resolution | a Version-1 symbol (21×21 modules) at 2px/module plus quiet zone is ~50px. Enough for a short URL, nowhere near enough for a raw repo path — **a redirector is mandatory, not a convenience** |
| Reed–Solomon error correction (7–30% by level) | recovers a scuffed symbol, **not a Sim standing in front of one** — a character sprite blocks far more than 30% and moves while doing it. This is why the dialog wins (below) |
| Catalogs outlive URLs | **link rot is the real failure mode** over a 26-year catalog. The redirector must be owned by the creator; destination URLs frozen into shipped objects are a guaranteed future breakage |

That last row is the same problem [reading cursors](READING-CURSORS.md#the-cursor-is-a-permalink-remote-commit-path-anchor)
have with dangling SHAs, and it takes the same shape of answer: an indirection you control, plus
enough content in the ticket to re-find the target when the indirection fails.

### The dialog wins, and the sprite becomes a game mechanic

The two implementations are not a tie. **Put the code in a popup dialog**, as an image in the
object's About panel: more pixels, no compositing work, no occlusion, and it is a few lines against a
sprite pipeline. The in-world floating sprite loses for a reason error correction cannot fix —
**inhabitants walk in front of it.** A character sprite blocks most of a small symbol and keeps
moving while it does, so the failure is not a degraded scan but an intermittent one, which is worse
than a consistent failure because the user cannot tell whether the thing is broken.

But the failure mode is a design brief for a different feature. A code that is **only sometimes
scannable, only from some angles, and only for a while** is a code you have to *catch* — which is the
[Pokémon-without-the-brand-name](#pokémon-without-the-brand-name) mechanic arriving from the
opposite direction. Ephemeral in-world codes are worth building precisely where scarcity is the
point; persistent reference codes belong in the dialog. Occlusion is a bug in a citation and a
feature in a hunt.

**Wikipedia is the obvious first target and it settles the link-rot row above.** If a scan on an
object about a real thing resolves to that thing's Wikipedia article, the destination is stable,
already-maintained, multilingual, and free, and the creator's redirector only has to map
object → article rather than object → a page they must keep alive for 26 years. The catalog then
inherits an encyclopedia's upkeep instead of paying its own.

## Honest costs

**Geo-privacy is the serious one.** A souvenir collection is a movement log with photographs
attached, and it is more revealing than a GPS track because it marks what you *cared about*. The
urban-safari [privacy section](../../skills/urban-safari/DATA-CONTRACT.md#privacy) is the governing
constraint, and souvenirs need at minimum: coordinate fuzzing at publish time, a distinction between
the private stamp and the public one, and home-area exclusion. Do not ship the sharing feature before
the fuzzing feature.

**Souvenir spam.** If every dispenser issues freely, inventories fill with tokens nobody redeems, and
the collection stops being an itinerary because it records everything equally. Dispensers should be
stingy; a rack with one good brochure beats a wall of pamphlets.

**Generation is not free.** Every crank turn is a model call. The crank's slowness is honest, but a
dispenser that is *only* a generator is expensive and unreliable; the ECG construction is what keeps
most of the cost in design time rather than crank time.

**The checkin risk.** If redemption is not built, this is a badge system with extra steps. Redemption
is not a later phase.

## Status

Design. The dispenser and souvenir schemas are specified here; the church's document-reference
objects are the first population and already carry `ref` and `TAKE`. The map layer is a proposed
addition to an existing, working data contract — `souvenirs.geojson` alongside
`transcript.geojson` — and the parameterized crank depends on the ECG construction, whose patent has
expired.
