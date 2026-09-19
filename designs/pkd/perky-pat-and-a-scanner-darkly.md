# PKD wrote three of these design documents first

*Part of [designs/pkd/](README.md). Siblings:
[palmer-eldritch-captured-purpose.md](palmer-eldritch-captured-purpose.md) reads the 1965 novel again
for the dimension it breaks rather than the business it describes · [ubik.md](ubik.md).*

Philip K. Dick specified the dollhouse with an aftermarket, the incompatible-rules problem two doll
worlds hit when they meet, and the job where you watch your own household on a screen. 1963, 1965,
1977. The mechanisms are the same mechanisms, and in two cases his version states the constraint more
clearly than our specs did.

**This document argues *same mechanism* and stops deliberately short of *influence*, because those
are two claims and only one of them is established here.** Don makes the stronger one — that Perky
Pat inspired The Sims, and that he can support it — and it is recorded as his claim, with the
specific citation still outstanding, in
[the Eldritch doc](palmer-eldritch-captured-purpose.md#dons-claim-about-the-sims-recorded-as-a-claim).
Do not read the hedge here as a rebuttal of it; read it as the weaker claim being separately true.

## The Days of Perky Pat (1963) — the layout is the rule set

Survivors of a nuclear war live in California fallout shelters, kept alive by airdrops. The adults
are obsessed with **layouts**: a Barbie-like doll called Perky Pat, her boyfriend, and a miniature
world through which they run the routines of pre-war life — putting a dime in a parking meter — while
their children ignore all of it and hunt mutants on the surface. Store-bought accessories are
supplemented with handmade furniture, and the better-furnished layouts confer status.

That is the dollhouse, its content economy, and its modding community, in a short story published
thirty-seven years before The Sims shipped.

But the part worth stealing is the plot. Pinole's shelter wagers Perky Pat against Oakland's rival
doll, **Connie Companion**, and the visitors discover two things at once: Connie is carved wood with
real hair rather than plastic, and Connie and her companion Paul are **married and living together**,
while Pat and Leonard can only date — *because the Pinole layout has no way to express a change in
marital status.* The Pinole players object that this is an unfair advantage.

Two implementations of the same doll world, with different fidelities and different expressible
states, meeting for the first time, and the argument at the border is about whose rules govern and
whether the richer state is legitimate. That is the [soul bridge](../../skills/soul-city/SOUL-BRIDGES.md)
problem, worked as fiction, in 1963. Our version of Pinole's complaint is stated in
[`SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md#the-errand-a-job-in-another-game): anything
the origin cannot express, it cannot receive. Dick got there first and made it a wager.

## The Three Stigmata of Palmer Eldritch (1965) — the business model, and the warning

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

The novel also supplies the counter-example. Palmer Eldritch returns from Proxima selling **Chew-Z**,
which does not need a layout: it gives each user a private world, authored by something that claims
divine authority and cannot be audited or reliably exited. Can-D translation is at least
**communal and grounded in a physical layout everyone can see** — the shared object is what makes the
experience checkable against someone else's. Chew-Z is a generated world with no shared referent and
no way to tell whose intentions are running it.

That is the strongest argument I know of for the thing this repo does structurally: worlds made of
files that people can inspect, edit, and compare, rather than worlds generated on demand for one
person by a system that cannot be examined. The analogy has limits — generation is not sinister and
Eldritch is not a language model — but the distinction it draws is exactly the one that matters.
Shared, inspectable layout, or private, unauditable world.

**The sharper version of that paragraph has its own document now**, because "cannot be audited" was
the right instinct aimed slightly wrong: Chew-Z withholds nothing and is *better* than Can-D on every
axis a user would name, so the failure is not a missing capability but a captured `whose_purpose` —
the vendor bound as a silent co-receiver on every dispatch inside the world. Worked out, with the
Can-D/Chew-Z pair mapped onto The Sims Online and Spore and with *Do Androids Dream* as the control
group, in [palmer-eldritch-captured-purpose.md](palmer-eldritch-captured-purpose.md).

## A Scanner Darkly (1977) — the job of watching your own household

Bob Arctor is an undercover narcotics agent whose assignment is to surveil a house full of drug users
under continuous holographic scanners. The house is his own. Reporting to his superiors in a
**scramble suit** that makes him an unidentifiable blur, he is known to them only as Fred, and Fred's
job is to review the recordings of Bob. Substance D is meanwhile splitting his hemispheres into two
competing halves, and the halves stop being able to recognize that they are one person.

This is the [bicameral mind](../../skills/soul-city/CHARACTER-ENDOSYMBIOSIS.md#two-minds-two-layers)
with the failure mode attached, which is why it is worth citing rather than just admiring.

**The mechanic it licenses.** A character can take a job in the Soul Angel layer itself — not in
another game, but in the layer that watches the games. She leaves the house, an
[egg](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/EGGS.yml) sits at the
door where she vanished, and her other mind spends the day watching her own family on screen: who
visited, who fought, who fixed the sink, what the children did while nobody was home. She comes back
with a journal, and the journal is a souvenir like any other
([SOUVENIRS.md](../../skills/soul-city/SOUVENIRS.md)). Her body was absent; her attention was not.
Nothing about that requires the game to cooperate, because watching the screen and writing prose is
the job that [needs no gate](../../skills/soul-city/SOUL-BRIDGES.md#the-job-that-needs-no-gate).

**The failure mode it names.** Fred does not know he is watching Bob. The two minds are severed
because the *credit* is severed — the scramble suit exists precisely so that the watcher has no
identity. Our safeguard is the thing that looked like bookkeeping: both organelles publish into
**one credited event stream**, and both feed **one album** attributed to one soul. A journal written
by the watching mind says who wrote it and about whom. The moment an observing mind's output stops
being attributed to the person it belongs to, you have built the scramble suit.

**And the consent line.** Watching your own household is a domestic diary. Watching someone else's
is surveillance, and it needs a grant from them, per the portrayal and consent rules that already
govern recording real people
([UNIVERSAL-JOBS.yml](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/UNIVERSAL-JOBS.yml),
consent). Dick's whole plot is what happens when that grant is manufactured by an institution
instead of given by a person.

## Why he keeps turning up

He is already in the vocabulary. *The Transmigration of Timothy Archer* is the citation under
[**transmigration**](../../skills/soul-city/GLOSSARY.md), the word this project uses instead of
import and export. *Ubik* is half the name of Ubikam, the semantic camera in the LLOOOOMM corpus,
crossed with Mark Weiser's ubiquitous computing — **and it turned out to owe a document of its own**,
because its regression of form is specificity ordering failing downward, dramatised
([ubik.md](ubik.md)). The three texts above cover the dollhouse, its economy, the bridge, and the
observer.

The reason is not mysticism. Dick wrote almost exclusively about the two questions this whole design
keeps hitting: **is this world authored, and by whom** — and **when a person is split across
substrates, which one is them.** Those are the load-bearing questions of a save file with people in
it, so anyone who thought hard about them in 1963 was doing our work early.

## What we take, and what we refuse

**Take:** the layout as an inspectable shared object; the expressible-state argument from the Connie
Companion wager; the aftermarket as the business; the observing mind as a real job; and the credited
stream as the thing that keeps a split person one person.

**Refuse:** the scramble suit. No unattributed observer, no institution that assigns you to watch
your own house without telling you it is your house, and no private world nobody else can check.

## Sources

- "The Days of Perky Pat", *Amazing Stories*, December 1963 — collected in *The Minority Report and Other Classic Stories*
- *The Three Stigmata of Palmer Eldritch*, 1965 — [Can-D, translation, P. P. Layouts, minning, Chew-Z](https://en.wikipedia.org/wiki/The_Three_Stigmata_of_Palmer_Eldritch)
- *A Scanner Darkly*, 1977
- Will Wright's hobby model, in his own words: [`sims-will-wright-microworlds-1996.md`](../sims/sims-will-wright-microworlds-1996.md)
- The mechanisms: [`SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md) · [`CHARACTER-ENDOSYMBIOSIS.md`](../../skills/soul-city/CHARACTER-ENDOSYMBIOSIS.md) · [`GLOSSARY.md`](../../skills/soul-city/GLOSSARY.md)
