# Palmer Eldritch: the capability works perfectly and the purpose is captured

*Part of [designs/pkd/](README.md). The Korz reading of* The Three Stigmata of Palmer Eldritch
*(1965). Its sibling [perky-pat-and-a-scanner-darkly.md](perky-pat-and-a-scanner-darkly.md) reads the
same novel for its business model; this one reads it for the dimension it breaks.*

## The mistake worth correcting first

The obvious reading of Chew-Z is that Eldritch **withholds** something — that he stands between the
user and a capability, a gatekeeper taking a cut. That reading is wrong, and getting it wrong is the
whole lesson.

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

Don has consistently held that **this story inspired The Sims**, and says he can support it.
Recording it as *his* claim rather than as settled history, because the two are different objects and
the sibling doc deliberately made the weaker one.

**What is structurally established**, and it is a lot — the dollhouse, the perpetual accessory
aftermarket, the taste-forecasting department, status conferred by furnishing — is laid out in
[perky-pat-and-a-scanner-darkly.md](perky-pat-and-a-scanner-darkly.md), which argues *same
mechanism* and stops short of *influence* on purpose. The Sims began at Maxis as **Project
Dollhouse**, and the name was a liability internally, which is a fact about the project's own
understanding of what it was.

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

## See also

- [`purpose-dimension.md`](../korz/korz-prime/examples/purpose-dimension.md) — where `whose_purpose`
  is specified, and where this novel is filed as its specimen
- [perky-pat-and-a-scanner-darkly.md](perky-pat-and-a-scanner-darkly.md) — the same novel for its
  business model, plus the 1963 story and the 1977 one
- [ubik.md](ubik.md) — the third variation: the world is fake, the vendor is *inside the frame*, and
  the product is a can of reality
- [`interfaces-to-agency`](../../skills/design-sense/lenses/interfaces-to-agency.md) — symmetry of
  capability with asymmetry of throughput; Chew-Z is symmetric capability with captured purpose,
  the case the lens has to answer
- [`TELEOLOGY.md`](../TELEOLOGY.md) — setpoints installed from outside

## Sources

- *The Three Stigmata of Palmer Eldritch*, Philip K. Dick, Doubleday, 1965
- *Do Androids Dream of Electric Sheep?*, Philip K. Dick, Doubleday, 1968
- Wright's "massively single-player online game" for Spore — his own phrase for the Sporepedia
  architecture
- `needs-check: the Chew-Z advertising slogan is quoted from memory as "GOD PROMISES ETERNAL LIFE.`
  `WE CAN DELIVER IT." Verify wording and capitalisation against the text before quoting publicly.`
