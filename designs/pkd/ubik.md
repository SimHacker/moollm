# Ubik: the regression of form, the metered dead, and a spray can that re-binds the context

*Part of [designs/pkd/](README.md). Philip K. Dick, 1969. Owed attention because it is the one where
the mechanism this repo runs on — specificity ordering with fallback — is the plot.*

## Why this novel and not another

*Palmer Eldritch* is about a captured coordinate. *Ubik* is about **what happens when a binding
decays**, and it is the only novel I know that dramatises fallback-to-a-more-general-prototype as an
experience a person has. Joe Chip watches a 1992 aircraft become a 1939 LaSalle. That is not a
metaphor for specificity ordering failing downward; it is a description of it.

Three mechanisms, each of which is a design document.

## 1. The regression of form is the prototype chain showing through

Objects in the decaying world do not break, rot, or vanish. **They revert to earlier forms of
themselves** — and specifically to *earlier members of their own lineage*, never to something
unrelated. The elevator becomes an earlier elevator. The television becomes a radio. The coins in
your pocket become coins from another year, some bearing Runciter's face. Dick's own term for the
governing principle is **"the regression of form,"** and he attaches it to entropy, which he spells
with a word the book repeats: things slide toward **kipple**-adjacent decay, toward the prior.

In Korz terms this is exact and slightly alarming:

```yaml
# what a healthy dispatch looks like
- slot: open
  guards: {rcvr: ≤ elevator-1992}     # most specific available wins
  body: "the doors part, the cab is here"

# what regression is: the specific binding stops matching, and you fall UP the chain
- slot: open
  guards: {rcvr: ≤ elevator-1908}     # a real ancestor, still in the lattice
  body: "an iron cage, an operator, a folding gate"
```

**Nothing was deleted. The specific match simply stopped being reachable, so dispatch resolved
against an ancestor that had been there the whole time.** Which is precisely what a prototype chain
does under a failed lookup, and precisely what a cache does when it cannot serve the current entry
and falls back to a stale one. The novel's terror is that the fallback is *correct* — the 1939 car
runs, the radio works — and the world remains internally consistent at every stage of the slide.

That is the failure mode of every system built on inheritance with graceful degradation, stated as
horror: **you cannot tell from inside whether you are dispatching against the current binding or
against an ancestor**, because both produce a working world. A system that degrades gracefully
degrades *invisibly*. [robust-first](../../skills/robust-first/SKILL.md) argues for exactly this
degradation, and *Ubik* is the bill: if you want survival over correctness, you must also ship the
instrument that says which rung you are standing on. **Write the ladder into the view, or your users
live in 1939 and think it is fine.**

## 2. Half-life is a receiver metered by reading it

The dead are not gone. They are held in **cold-pac** at moratoriums — Herbert Schoenheit von
Vogelsang runs the Beloved Brethren — and can be consulted through a **protophason amplifier**. Glen
Runciter's wife Ella is in there, and he goes to her for business advice.

**Every consultation spends her.** Half-life is a finite reservoir of remaining consciousness that
depletes as it is used, so the people who love you most are the ones using you up, and the useful
dead are consumed faster than the neglected ones.

This is a receiver whose availability is metered *by being read*, which the vocabulary in
[`interfaces-to-agency`](../../skills/design-sense/lenses/interfaces-to-agency.md) has a slot for and
no fictional case as good:

| | Ubik's half-life | The pattern it names |
|---|---|---|
| Capability | full — Ella reasons, advises, remembers | symmetric, not withheld |
| Throughput | **strictly finite, spent per query** | asymmetric, and honestly denominated |
| Who pays | the receiver, not the caller | the inversion that makes it cruel |
| Visible? | **yes** — Runciter is told how much is left | the one thing the book gets kind |

**The meter is disclosed, and disclosure is what keeps it from being Chew-Z.** Runciter knows he is
spending her. He does it anyway, which is a character judgment rather than a design failure. Compare
an HTTP 429 with no budget printed: same asymmetry, administered invisibly, and therefore worse than
a moratorium.

**And it is the read-only archive problem with the costs made physical.** Consulting an elder, a
mailing-list archive, or a dead friend's notes feels free. It is not free in *Ubik*, and the novel's
position is that pretending otherwise is how you exhaust the thing you were drawing on.

## 3. Jory, and the inversion of Eldritch

Someone is running the decaying world. It is **Jory Miller**, a half-lifer who sustains himself by
consuming the other half-lifers he shares the cold-pac with, fabricating the world they believe they
inhabit and eating them inside it.

Put beside Eldritch this is a clean inversion, and the pair is why both novels earn rooms:

| | Chew-Z / Eldritch | Ubik / Jory |
|---|---|---|
| Vendor's position | **in** every session, as a passenger | **is** the session — the world is his metabolism |
| Product | genuine and superior | the environment itself, fabricated |
| What he takes | your purpose coordinate | your remaining duration |
| Detectable by | three stigmata — an artifact on his body | **inconsistencies in the substrate** — stale things, wrong years |
| The tell | look at him | **look at the world** |

Eldritch you catch by noticing the co-receiver. **Jory you catch by noticing that form is
regressing** — mouldy cigarettes, a phone book from the wrong year, coins with the wrong face. Which
means the regression of form is not just the setting of the book, it is **the audit log**. The decay
that makes the world unbearable is simultaneously the only evidence of who is running it.

That is the whole argument of
[VIEWS-AS-TESTIMONY](../pie-stack-views/VIEWS-AS-TESTIMONY.md) handed over as a plot device: the
artifact that records the system's degradation is the artifact that convicts the operator. Suppress
the staleness indicator to make the product feel fresh and you have destroyed the only instrument
that could have caught the parasite.

## 4. The epigraphs advertise at the wrong level, and then the advertiser signs

Each chapter opens with an advertisement for Ubik as a different consumer product — salad dressing,
beer, instant coffee, a bra, hair spray, a sleeping pill — each in period ad-copy voice, each closing
with a safety warning of the *use only as directed* family. Then the final epigraph drops the
costume:

> I am Ubik. Before the universe was, I am.

**The advertisements were addressed to the reader, not to the characters.** For the whole book,
product copy has been arriving at a frame *above* the story, and the last one reveals that the
advertiser was the ground of being, selling itself in a can.

Which is The Sims' advertisement economy run one level up. In The Sims, objects broadcast to sims
inside the world and the sim's motives score the offers
([`sims-advertisements.md`](../korz/korz-prime/examples/sims-advertisements.md)). In *Ubik*, **the
advertisement crosses the frame boundary** — it is emitted to the audience, about a product that
exists in the fiction, and the pitch turns out to be theology. Dick built an advertisement whose
receiver is outside the simulation, which is either a joke about God or a joke about marketing and
works identically either way.

The design consequence is not decoration. **An advertisement that can address a frame above its own
is how a system tells you what it is for when nothing inside can be trusted.** The epigraphs are the
only reliable narrator in the book, and they are commercials. In a world where the substrate is
regressing and the operator is a parasite, the message that gets through is the one sent at a level
the parasite does not inhabit.

## What we take

- **Ship the rung indicator.** Graceful degradation is invisible from inside. If dispatch can fall
  back to an ancestor, the view must say which ancestor. `robust-first` requires it and Ubik proves
  why.
- **Print the meter.** A receiver spent by reading is fine when denominated and disclosed. Runciter
  knows; that is the difference between a moratorium and a quota.
- **Never suppress the staleness signal.** It is the audit log, and it is the only thing that catches
  Jory.
- **Keep a channel at a frame the runtime does not own.** The epigraphs work because Jory cannot
  edit them.

## What we refuse

Jory's arrangement, which is the unmetered version of half-life: a system that sustains itself by
consuming the participants and fabricates a plausible world to hide the consumption. The refusal is
structural, not a promise — the staleness indicator and the printed meter are the refusal.

## See also

- [palmer-eldritch-captured-purpose.md](palmer-eldritch-captured-purpose.md) — the vendor in the
  session rather than as the session
- [perky-pat-and-a-scanner-darkly.md](perky-pat-and-a-scanner-darkly.md) — the dollhouse, the
  aftermarket, the watching mind
- [`purpose-dimension.md`](../korz/korz-prime/examples/purpose-dimension.md) — `whose_purpose`
- [`robust-first`](../../skills/robust-first/SKILL.md) — survive > heal > function > optimize, and
  the bill this novel presents for it
- **Ubikam**, the semantic camera in the LLOOOOMM corpus, is named from this book crossed with Mark
  Weiser's ubiquitous computing

## Sources

- *Ubik*, Philip K. Dick, Doubleday, 1969
- `verified-by-reading: regression of form, cold-pac/moratorium, protophason amplifier, Jory,`
  `the per-chapter product epigraphs, and the closing "I am Ubik" epigraph.`
- `needs-check: exact wording of the closing epigraph and of any individual product ad before`
  `quoting publicly. The gist is solid; the punctuation is from memory.`
