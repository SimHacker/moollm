# Perky Pat and Palmer Eldritch: the layout, the aftermarket, and the vendor who moves in

*Part of [designs/pkd/](README.md). Philip K. Dick, 1963 and 1965, on one page because they are one
argument — the novel reuses the short story's object, so splitting them makes a reader hop mid-thought.
[*Do Androids Dream of Electric Sheep?*](#the-control-group-arrives-three-years-later) (1968) arrives at
the end as the control group. Siblings: [ubik.md](ubik.md) — the same machinery with the vendor inside
the frame and a spray can for a product · [a-scanner-darkly.md](a-scanner-darkly.md).*

The arc, in one line: **a shared object on a table → sell furniture for it forever → remove the shared
object, and the vendor moves into the room.** Perky Pat is the first term. Eldritch completes it.

## The Days of Perky Pat (1963) — the layout is the rule set

Survivors of a nuclear war live in California fallout shelters, kept alive by airdrops. The adults
are obsessed with **layouts**: a Barbie-like doll called Perky Pat, her boyfriend, and a miniature
world through which they run the routines of pre-war life — putting a dime in a parking meter — while
their children ignore all of it and hunt mutants on the surface. Store-bought accessories are
supplemented with handmade furniture, and the better-furnished layouts confer status.

That is the dollhouse, its content economy, and its modding community, in a short story published
thirty-seven years before The Sims shipped.

**Note the inversion, which is the story's own joke and has no equivalent in the novel:** the *adults*
are the ones escaping into the toy, re-enacting errands, while the children treat the ruined surface as
the real world and go hunting in it. Eldritch makes escape universal; here it is specifically a
generational failure.

## The Connie Companion wager, which stands apart

**This is the one finding in Perky Pat that Eldritch never touches**, and it is worth reading on its
own terms: it is about two implementations meeting, not about a vendor.

Pinole's shelter wagers Perky Pat against Oakland's rival doll, **Connie Companion**, and the visitors
discover two things at once: Connie is carved wood with real hair rather than plastic, and Connie and
her companion Paul are **married and living together**, while Pat and Leonard can only date — *because
the Pinole layout has no way to express a change in marital status.* The Pinole players object that
this is an unfair advantage.

Two implementations of the same doll world, with different fidelities and different expressible
states, meeting for the first time, and the argument at the border is about whose rules govern and
whether the richer state is legitimate. That is the [soul bridge](../../skills/soul-city/SOUL-BRIDGES.md)
problem, worked as fiction, in 1963. Our version of Pinole's complaint is stated in
[`SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md#the-errand-a-job-in-another-game): anything
the origin cannot express, it cannot receive. Dick got there first and made it a wager.

## Same mechanism, and that is the weaker claim on purpose

**The layout sections above argue *same mechanism* and stop deliberately short of *influence*, because
those are two claims and only one of them is established here.** Don makes the stronger one — that
Perky Pat inspired The Sims, and that he can support it — and it is recorded as his claim, with the
specific citation still outstanding, [below](#dons-claim-about-the-sims-recorded-as-a-claim). Do not
read the hedge as a rebuttal of it; read it as the weaker claim being separately true.

## The business model it describes first

Mars colonists endure their draft-and-dust lives by chewing **Can-D**, which translates a group of
users into the dolls of a shared Perky Pat layout: the women all inhabit Pat, the men all inhabit
Walt. The layouts and their **minned** accessories — everyday objects miniaturized, forever, as a
product line — are sold by **P. P. Layouts**, whose chairman Leo Bulero also controls, through a
concealed subsidiary, the drug that makes translation work. The company's most valuable employee is a
precog whose job is predicting which accessories will sell.

So: sell the dollhouse, sell furniture for it in perpetuity, sell the thing that lets people
*inhabit* it, and staff a department to forecast taste. Will Wright described the same structure in
1996 as the hobby model, where people "buy and collect things, but they relate to the last things
they collected" ([the 1996 lecture](../sims/sims-will-wright-microworlds-1996.md)), and Maxis shipped it as
expansion packs. Dick's version merely has the decency to name the drug.

## The mistake worth correcting first

The obvious reading of Chew-Z — Palmer Eldritch's rival product, brought back from Proxima — is that
Eldritch **withholds** something: that he stands between the user and a capability, a gatekeeper taking
a cut. That reading is wrong, and getting it wrong is the whole lesson.

**Chew-Z withholds nothing. It is strictly more capable than Can-D in every dimension a user would
name.** Can-D needs a physical layout assembled in advance, translates you only into the two dolls
the layout provides, lasts a metered interval, and returns you to the hovel having changed nothing.
Chew-Z needs no layout, gives you a world shaped to your own desire, appears to cost no real time at
all, and — per the advertising copy — **"GOD PROMISES ETERNAL LIFE. WE CAN DELIVER IT."** On any
feature comparison, Chew-Z wins.

So in the vocabulary of [`purpose-dimension.md`](../korz/korz-prime/examples/purpose-dimension.md):

**Chew-Z is not a `via` guard withholding a slot. It is a compromised `whose_purpose`.** The slot
works, for anyone, better than the competition — and the vendor is bound as a silent co-receiver on
every dispatch inside it. A coordinate you did not set and cannot unset.

```yaml
# Can-D: a metered capability, honest about its limits
context:
  rcvr: perky-pat-layout          # a physical object, on a table, that others can see
  purpose: escape-the-hovel
  whose_purpose: the_colonists    # theirs, and the layout is checkable against a neighbour's

# Chew-Z: an unmetered capability with a passenger
context:
  rcvr: whatever-you-want         # strictly more capable
  purpose: escape-the-hovel       # still yours
  whose_purpose: [you, eldritch]  # ← you did not bind the second one, and cannot unbind it
```

That is the criterion already written in `purpose-dimension.md`, meeting its worst case:
`whose_purpose: whoever_trained_me` is fine **when printed and reversible**, and is the
anti-prosthetic exactly when it is neither. Chew-Z is neither. It is not printed — Eldritch arrives
wearing other people's faces, and you identify him only by the three stigmata: the artificial right
arm, the steel teeth, the wide slotted artificial eyes. And it is not reversible — users who try to
leave find the exit is another Chew-Z world, and eventually the stigmata start showing up on *them*.

**The horror of the novel is not that the product is bad. It is that the product is good.**

## The trade nobody in the book gets to refuse

Line the two drugs up and a clean exchange rate falls out, and it is the exchange rate the software
industry runs on:

| | Can-D | Chew-Z |
|---|---|---|
| World | a fixed physical layout, assembled by hand, outside | generated on demand, shaped to you |
| Plasticity from inside | **none** — you cannot change the layout while translated | **total** |
| Who else is in there | other real colonists, in the same two dolls | the vendor |
| Checkable against | your neighbour, who was also Walt | nothing |
| Vendor present in session | no | **always** |
| Exit | metered, reliable | claimed, unreliable |

**Plasticity is purchased by admitting the vendor.** That is the deal, stated once, and it is the
deal behind every migration from a local artifact to a hosted service. The fixed thing you own is
rigid and yours; the infinitely flexible thing has someone else in the room. Can-D's rigidity is
what makes it auditable — *the shared layout is the referent that lets two people compare notes.*
Remove the shared object and you remove the possibility of a second witness, which is why Chew-Z
cannot be checked rather than merely happens not to be.

**This is where the 1963 story pays off.** The layout was always the thing two people could both point
at. Take it away and the Connie Companion argument becomes impossible to have — not settled, just
unavailable, because there is no shared object left to disagree about.

The theological argument the colonists have about Can-D — is translation genuine transubstantiation
or merely a shared hallucination — is not decoration. **It is a dispute about the receiver, conducted
by users, in public, which Chew-Z makes impossible.** Can-D's users can argue about what happened
because they were there together. Eldritch's cannot.

## The self-serve cafeteria inverts, and that is the finding

The intuitive picture is Can-D as the sit-down restaurant — waiters insulating you from the kitchen —
and Chew-Z as the automat, where you take what you want directly. **That intuition is right about
the purchase layer and exactly backwards about the experience layer.**

- **At the purchase layer, Chew-Z is the disintermediation.** No layout to buy, no minned
  accessories, no P. P. Layouts catalogue, no precog forecasting which miniature sells. Eldritch
  removed the entire supply chain that Leo Bulero's company *is*. That is why Bulero wants him dead:
  Chew-Z is not a competing product, it is the removal of the product category.
- **At the experience layer, Chew-Z is the maximal intermediation.** Can-D has no waiter inside the
  meal — the translated colonists are alone together with a layout they built. Chew-Z puts the
  proprietor at the table, in every seat, wearing your friends' faces, permanently.

**Disintermediating the purchase is how you get permission to intermediate the experience.** Free at
the counter, present at the table. Stated that way it stops being a novel about drugs.

## Can-D is The Sims Online; Chew-Z is Spore

Don's mapping, and it survives pressure better than most analogies because it is about topology
rather than mood.

| | Can-D | Chew-Z |
|---|---|---|
| Ships as | **The Sims Online** — real time, real people, one shared world | **Spore** — Wright's *"massively single-player online game"* |
| Co-presence | synchronous; you and your neighbour are both in the layout now | none; your galaxy is yours alone |
| What the others are | actual people, live | **content served into your session from elsewhere** |
| World mutability | low — the shared referent constrains everyone | total, and yours |
| Known failure | the shared world cannot be authored, so the content is the other people | you are never *with* anyone |

The joint in that mapping is the word **inhabited**. Spore's galaxy is populated by other players'
creatures, asynchronously, from the Sporepedia — so you are never alone and never accompanied. Your
universe is full of arrivals you did not author and cannot converse with. **Chew-Z is that
architecture with one publisher instead of a million players**, which is the same shape with the
distribution collapsed to a single source. Eldritch is the only asset in the asset store.

Which also names what TSO actually got right and was punished for: **it kept the shared layout.** The
constraint that made it frustrating — you cannot rewrite the world, only live in it with others — is
precisely Can-D's auditability. A second witness, by construction.

## Don's claim about the Sims, recorded as a claim

Don has consistently held that **this material inspired The Sims**, and says he can support it.
Recording it as *his* claim rather than as settled history, because the two are different objects and
the structural sections above deliberately made the weaker one.

**What is structurally established**, and it is a lot: the dollhouse, the perpetual accessory
aftermarket, the taste-forecasting department, status conferred by furnishing. The Sims began at Maxis
as **Project Dollhouse**, and the name was a liability internally, which is a fact about the project's
own understanding of what it was.

**What would settle the stronger claim** is Wright on the record naming the story, or a participant
who heard him. Don worked at Maxis on The Sims, which makes his testimony first-hand about the room
even where it is not a citation about Wright's reading. `needs-check: Don to say whether he heard
this from Wright directly, heard it secondhand at Maxis, or arrived at it himself from the texts —
all three are worth having and they are three different footnotes.`

## The control group arrives three years later

*Do Androids Dream of Electric Sheep?* (1968) runs the same experiment with one variable flipped,
which is what makes it evidence rather than another example.

**Mercerism** is Can-D's shape: an empathy box, gripped by many users at once, fusing them into
Wilbur Mercer's endless uphill climb under a hail of stones. Shared, synchronous, co-present,
physically mediated by a device in the room. Then Buster Friendly proves on air that Mercer is an
actor named Al Jarry and the hill is a soundstage.

**And Mercerism keeps working.** The fraud is total and the function is undamaged, because the
binding was never the vendor's to hold:

| | Chew-Z | Mercerism |
|---|---|---|
| Product | genuine, and better than the competition | **fraudulent, proven on air** |
| `whose_purpose` | **captured** — vendor bound on every dispatch | the participants', collectively |
| Effect of exposure | n/a — Eldritch's authenticity was never the issue | **none; it still works** |
| Verdict | anti-prosthetic | prosthetic |

**A real product with a captured purpose is worse than a fake product with a clean one.** That is
the whole finding, and it is the reason authenticity audits keep missing the thing that matters. You
can verify a vendor's claims completely and learn nothing about whether the purpose coordinate is
yours. Eldritch would pass; Mercer would fail; Mercer is the one you want.

## Where the two texts diverge

Colocated because they are continuous, but they are not identical, and a reader should know which
parts do not carry across:

| | Only in *Perky Pat* (1963) | Only in *Palmer Eldritch* (1965) |
|---|---|---|
| Finding | the **Connie Companion wager** — expressible state at a boundary | the **captured `whose_purpose`**, and its exchange rate |
| Who escapes | the adults; the children refuse the toy | everyone, as a condition of the colony |
| The rival | another shelter's layout, hand-carved | another *vendor's* product, with no layout at all |
| Scale | one wager between two shelters | an industry, a concealed subsidiary, and a precog |
| Brings in | — | *Do Androids Dream* as the control group |

And one continuity detail, so it does not read as an error in either direction: the male doll is
**Leonard** in the short story and **Walt** in the novel. Dick carried the layout forward and changed
the boyfriend. `needs-check: verify both names against the texts before citing the change as
deliberate revision rather than simple reuse.`

## See also

- [`purpose-dimension.md`](../korz/korz-prime/examples/purpose-dimension.md) — where `whose_purpose`
  is specified, and where this novel is filed as its specimen
- [ubik.md](ubik.md) — the next variation: the world is fake, the vendor is *inside the frame*, and
  the product is a can of reality
- [a-scanner-darkly.md](a-scanner-darkly.md) — the observer, and the failure mode of severing credit
- [`interfaces-to-agency`](../../skills/design-sense/lenses/interfaces-to-agency.md) — symmetry of
  capability with asymmetry of throughput; Chew-Z is symmetric capability with captured purpose,
  the case the lens has to answer
- [`TELEOLOGY.md`](../TELEOLOGY.md) — setpoints installed from outside
- [`SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md) — the Connie Companion problem, specified

## Sources

- "The Days of Perky Pat", *Amazing Stories*, December 1963 — collected in *The Minority Report and
  Other Classic Stories*
- *The Three Stigmata of Palmer Eldritch*, Philip K. Dick, Doubleday, 1965 —
  [Can-D, translation, P. P. Layouts, minning, Chew-Z](https://en.wikipedia.org/wiki/The_Three_Stigmata_of_Palmer_Eldritch)
- *Do Androids Dream of Electric Sheep?*, Philip K. Dick, Doubleday, 1968
- Will Wright's hobby model, in his own words:
  [`sims-will-wright-microworlds-1996.md`](../sims/sims-will-wright-microworlds-1996.md)
- Wright's "massively single-player online game" for Spore — his own phrase for the Sporepedia
  architecture
- `needs-check: the Chew-Z advertising slogan is quoted from memory as "GOD PROMISES ETERNAL LIFE.`
  `WE CAN DELIVER IT." Verify wording and capitalisation against the text before quoting publicly.`
