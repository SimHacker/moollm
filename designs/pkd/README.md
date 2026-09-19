# Philip K. Dick wrote the design documents first

*The literary-deconstruction room. Four texts that specify mechanisms this project independently
arrived at, in two cases more clearly than our own specs did. Moved out of
[`designs/sims/`](../sims/) because the material cross-cuts the sims work, Korz, soul-city and the
webtop, and belongs to none of them.*

## The pile

| Text | Year | What it specifies | Read it for |
|---|---|---|---|
| **The Days of Perky Pat** | 1963 | the dollhouse, its accessory aftermarket, its modding community, and the incompatible-doll wager | [perky-pat-and-a-scanner-darkly.md](perky-pat-and-a-scanner-darkly.md) |
| **The Three Stigmata of Palmer Eldritch** | 1965 | the business model; and separately, **a capability that works perfectly with a captured `whose_purpose`** | [business model](perky-pat-and-a-scanner-darkly.md) · [captured purpose](palmer-eldritch-captured-purpose.md) |
| **Ubik** | 1969 | **specificity ordering failing downward, as an experience**; a receiver metered by reading it; the audit log as the thing that convicts the operator | [ubik.md](ubik.md) |
| **Do Androids Dream of Electric Sheep?** | 1968 | the control group — a **fraudulent** product with an **uncaptured** purpose, which keeps working after exposure | [inside the Eldritch reading](palmer-eldritch-captured-purpose.md#the-control-group-arrives-three-years-later) |
| **The Man in the High Castle** | 1962 | **the bright pass applied to ontology** — a book containing a re-reading of its own world | [below](#the-man-in-the-high-castle-is-the-re-reading-novel) |
| **A Scanner Darkly** | 1977 | the job of watching your own household; the scramble suit as the failure mode of an unattributed observer | [perky-pat-and-a-scanner-darkly.md](perky-pat-and-a-scanner-darkly.md) |

## The three findings, if you read nothing else

**A real product with a captured purpose is worse than a fake product with a clean one.** Chew-Z is
genuine and better than its competitor in every dimension a user would name, and it binds the vendor
as a silent co-receiver on every dispatch. Mercerism is a proven fraud filmed on a soundstage, and it
keeps working after the exposure, because the binding was never the vendor's to hold. Authenticity
audits cannot see the difference; `whose_purpose` can.
→ [palmer-eldritch-captured-purpose.md](palmer-eldritch-captured-purpose.md)

**Plasticity is purchased by admitting the vendor.** Can-D's world is a rigid physical layout you
cannot change from inside, and that rigidity is what makes it auditable — the shared object is the
referent that lets two users compare notes. Chew-Z's world is infinitely plastic and has the
proprietor in it. Every migration from a local artifact to a hosted service is this trade.

**Graceful degradation is invisible from inside.** *Ubik*'s regression of form is a prototype chain
showing through: the specific binding stops matching and dispatch resolves against an ancestor that
was always there, producing a world that is internally consistent at every stage of the slide. The
1939 car runs. So if a system may fall back, **the view must say which rung it is standing on** —
which is the bill for [`robust-first`](../../skills/robust-first/SKILL.md), presented by a novel.
→ [ubik.md](ubik.md)

## The Man in the High Castle is the re-reading novel

Don raised it as a specimen of a work that survives its own ending, and it earns a place here rather
than only in the mystery essay, because **Dick built the second pass into the first.**

The Axis won. The United States is partitioned. And inside that world circulates a banned novel,
*The Grasshopper Lies Heavy* by Hawthorne Abendsen — an alternate history **in which the Allies
won**, which is not quite our history either. So the book contains a re-reading of its own world,
performed by its own characters, as a plot device. Then Juliana takes *Grasshopper* to the Oracle and
gets **Inner Truth**: Abendsen's book is the true one. The world you have been reading is the false
one.

**Which makes the second reading a re-binding of the ontology rather than of the plot.** The mystery
essay's [two passes](../korz/case-mystery-and-art/README.md#two-passes-minimum-and-the-second-one-is-lit)
are normally shadowed-then-lit about *who did it*; here the lit pass knows that **the depicted world
is the counterfactual**, and every scene in it reads as a report from a place that lost. Nothing is
retracted. The facts are the facts. Their frame moved.

And the method is the same move again: **Dick composed the novel by consulting the I Ching**, letting
the Oracle make plot decisions, and his characters consult it too — Abendsen admits the book wrote
itself that way. A novel produced by repeated consultation, whose subject is a consultation that
reveals the world to be false, **re-read by a reader performing another consultation.** The form, the
method, and the plot are one gesture at three scales.

Don's version is about the adaptation and about character rather than cosmology: *"the second watching
you see the characters the first time as who they really are and can understand what they're doing
better."* That is the **revelation** mode in the essay's table — concealed allegiance, where the
second pass satisfies a guard the first could not bind — and it is a different mechanism from the
ontological flip above. The novel supports both, which is why it keeps paying past two readings.

## Why he keeps turning up

Not mysticism. Dick wrote almost exclusively about the two questions a save file with people in it
cannot avoid: **is this world authored, and by whom**, and **when a person is split across
substrates, which one is them.** Anyone thinking hard about those in 1963 was doing this work early.

He is also already load-bearing in the vocabulary: *The Transmigration of Timothy Archer* is the
citation under **transmigration**, the word this project uses instead of import and export
([soul-city GLOSSARY](../../skills/soul-city/GLOSSARY.md)), and **Ubikam** — the semantic camera in
the LLOOOOMM corpus — is *Ubik* crossed with Weiser's ubiquitous computing.

## Where the Korz vocabulary lands

| Korz thing | The PKD case |
|---|---|
| [`whose_purpose`](../korz/korz-prime/examples/purpose-dimension.md) | Chew-Z: symmetric capability, captured coordinate. Filed there as its specimen. |
| specificity ordering, fallback | *Ubik*'s regression of form |
| the advertisement economy | *Ubik*'s chapter epigraphs, addressed to a frame **above** the story |
| a shared inspectable referent | the Perky Pat layout, versus a generated private world |
| expressible state at a boundary | the Connie Companion wager — Pinole's layout cannot represent marriage |

## One open claim, kept open

Don has consistently held that **Perky Pat inspired The Sims** and says he can support it. The
structural case is strong and documented; the citation that would settle *influence* rather than
*parallel* is not in hand, and the two claims are kept separate on purpose. Details and the specific
question outstanding:
[Don's claim, recorded as a claim](palmer-eldritch-captured-purpose.md#dons-claim-about-the-sims-recorded-as-a-claim).

## Adjacent case files elsewhere

The `case-*` pattern in [`designs/korz/`](../korz/) does the same work for other literature:
[case-mystery-and-art](../korz/case-mystery-and-art/) — detection and painting as one dispatch
mechanism · [case-zork](../korz/case-zork.md) · [case-cellular-automata](../korz/case-cellular-automata.md)
