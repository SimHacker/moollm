# Fluxx and Nomic: the context, made physical

*Part of the [Korz cauldron](../../README.md). Sidecar: [`fluxx-nomic.yml`](fluxx-nomic.yml).
**Spectrum: self-contained** — the published rules and the designers' own
statements are the canon.*

**What this teaches.** [`mtg-layers`](mtg-layers.md) showed a shipped
*dispatcher*: a slot sea with a legislated total order over it. Fluxx supplies
the other half of Korz's mechanism, the part Magic never modeled — **the
context itself, as physical state on the table.** A Korz context is a set of
`dimension: coordinate` bindings, one value per dimension. Fluxx's tableau is
literally that, and the only operation on it is **rebinding**. And behind
Fluxx stands Peter Suber's **Nomic**, which asks the question the Korz papers
stop just short of: can the rule that changes rules change itself?

## Fluxx is a Korz context you can knock over with your elbow

Andrew Looney built Fluxx on 24 July 1996; Looney Labs released it in 1997.
The whole game state that matters here is a few cards in the middle of the
table.

The **Basic Rules** card sits in the center and never leaves: *draw one card,
play one card.* **New Rule** cards go next to it, and the conflict rule is the
thing to look at closely:

> There can only be one of each kind of New Rule card in play (i.e. one Draw
> rule, one Play rule). When a New Rule gets played that contradicts one
> that's already in play, the one in play gets discarded.
> — [Fluxx wiki](https://fluxx.fandom.com/wiki/Introduction)

Mystery Fluxx states the shape outright: *"Max of 4 Rules in play at a time:
one each of Draw, Play, Limit, and Other. Each New Rule replaces any previous
such rule."*

Read that as Korz and there is nothing left to translate. `Draw`, `Play`,
`Limit`, `Other` are **dimensions**. A New Rule card is a **coordinate**.
Exactly one coordinate is bound per dimension at any moment. Playing a card
is a **rebind**, and the displaced binding goes to the discard pile.

No layers. No timestamps. No dependency graph. Where Magic needed CR 613
because it stacks conflicting effects and must order them, Fluxx makes
conflict *impossible to represent*: two Draw rules cannot coexist, so there
is nothing to order. That is the whole argument for declared dimensions,
demonstrated in a $16 card game a decade before the Korz papers.

**The physical layout even shows the shadowing.** From the Chemistry Fluxx
rules: *"New Rules that override the Basic Rules are placed overlapping the
part they supersede."* A more specific slot is placed **on top of** the slot
it shadows, covering exactly the part it overrides — Self-style overriding as
a gesture with your hand. Every diagram in every prototype-language paper,
done with cardboard.

## The win condition is a slot, and it starts unbound

This is the part that goes past Magic, and past most languages.

**Goal** cards define how to win. Only one is in play at a time, and playing
a new one discards the old. And: *"The game begins with no Goal in play, so no
one can win until one is played."*

So the **termination predicate is a coordinate on a dimension**, and its
initial state is *unmentioned* — Korz's "don't care" guard stance applied to
the question of whether the program can halt. A game of Fluxx with no Goal is
a program that has not yet been told what would count as finishing.

The check is continuous, not turn-based: the moment anyone satisfies the
current Goal they win, *no matter who played it*. Someone can play a Goal and
hand the win to the player across the table, instantly, because the
projection is re-derived rather than announced. Same pull discipline as
Magic's continuous effects, same shape as the state projector — and here it
governs the halt condition.

**Surprise** cards add one more Korz detail worth naming: each has two
different functions, one for use on your turn and one for out of turn. One
card, two guards, dispatching on a `whose_turn` coordinate. A Surprise can
also cancel another Surprise, which is a guard on a slot that is itself
mid-dispatch.

And **Meta Rules** close the loop: they stay in force for the whole game, and
the rulebook itself is one of them — *"(The Basic Rules are a Meta Rule.)"*
There is no privileged rulebook layer. The base rules are in the sea with
everything else, wearing a marker that says immovable.

## Nomic: the fixpoint, stated as law

Looney names his source directly:

> Fluxx was inspired by a conceptual game engine called Nomic, in which the
> game rules are created by the players as the game is played. I found Nomic
> to be an interesting idea, but felt I could do better…
> — [Andrew Looney, 2016](https://puzzculture.com/2016/07/22/5-questions-with-game-designer-andrew-looney/)

**Nomic** was invented by the philosopher **Peter Suber** in 1982 and
published, with commentary by Suber and reflections by Douglas Hofstadter, in
Hofstadter's *Metamagical Themas* column in *Scientific American*, June 1982.
Its initial rule set does almost nothing except **regulate the rule-changing
process**; the one substantive rule is deliberately boring so players will
amend it. Suber is explicit about why the game exists:

> It was intended to illustrate and embody the thesis of my book, *The Paradox
> of Self-Amendment*, that a legal "rule of change" such as a constitutional
> amendment clause may apply to itself and authorize its own amendment.
> — [Suber's Nomic page](https://legacy.earlham.edu/~peters/nomic.htm)

That is [`ask-david.md`](../../ask-david.md)'s guard-mutation question, posed in
1982, in jurisprudence, with a book-length answer attached. Magic's rule
613.8a is a *procedure* for handling effects that rewrite other effects.
Suber's paradox of self-amendment is the *theory* of whether the procedure can
apply to itself. A dispatcher whose specificity lattice is data has this
problem whether or not it names it, so it is worth knowing that a legal
philosopher got there first and did not find it fatal.

Two historical details that belong in this repo. Nomic games "were regularly
played, and kicked off, the ARPANET." And Nomic games "sent ambassadors to
other Nomic games, formed federations, and played Meta-Nomic" — federated
rule systems negotiating across a boundary, on the network Don was on.

## The real axis: when is the lattice authored, and by whom?

With Fluxx and Nomic in, this collection's shipped systems line up on one
question, and it is a better axis than "does it have dimensions":

| System | Who authors the lattice | When |
|--------|------------------------|------|
| [The Sims](sims-advertisements.md) | designers | design time; dimensions frozen, ambiguity handled by scoring and dither |
| [Magic](mtg-layers.md) | designers, on cards | press time; conflict handled by legislated order |
| **Fluxx** | designers, on cards | **play time by rebinding** — one coordinate per dimension, conflict unrepresentable |
| **Nomic** | players | **play time by amendment**, including amending the amendment rule |
| **1000 Blank White Cards** | players | play time by **invention** — the cards start blank ⚠ |
| [Dwarf Fortress](df-procedural-magic.md) | a generator | world-gen, from a creation myth, with runtime rule flips |
| Korz (as specified) | a programmer | compile time |
| [Korz′](../README.md) | programmer + model | compile time, plus soft-tier improvisation that crystallizes |

Korz sits at the *most static* end of a spectrum whose other end has been
commercially successful since 1997. That is not an argument against Korz —
declared dimensions are what make dispatch decidable, and Fluxx's own
elegance comes from *fixing* the dimension set and letting only the
coordinates move. It is an argument that the interesting design space is the
**middle**, and that Korz′'s two tiers are one way of straddling it. Fluxx is
the proof that you can move coordinates at runtime and keep the semantics
trivial, as long as you refuse to let two bindings share a dimension.

One more data point on authorship, from the designers themselves: Creepers
were introduced in Fluxx 4.0 and then removed in 5.0 — *"we took those cards
back out because we decided the original game is better without them."* A
dimension retracted by its author after shipping, which is a maintenance
story any language designer will recognize.

## Where Korz′ takes it

Fluxx is the best available **UI** for a Korz context, and that matters
because the Korz prototype needed an IDE to show slot groupings
([`ask-david.md`](../../ask-david.md) asks how much of that was the language and
how much was the Self image). Fluxx answers with cardboard: put the current
bindings in the middle of the table, face up, one per dimension, with
overrides physically covering what they shadow. A MOOLLM room could render a
live context exactly that way — the dimensions as named piles, the bound
coordinate face up on each, the discard pile as the rebinding history — and
[`hosting-moollm.md`](../hosting-moollm.md)'s interface files are already the
durable version of that view.

Nomic points somewhere sharper. Korz′'s soft tier improvises coordinates the
strict tier never declared, and stable improvisations crystallize downward. In
Nomic terms that is **an amendment process with a ratification step**, and the
game has forty years of played-out experience with what goes wrong: Suber
notes that Nomic games "experienced revolution, oppressive coups, and the
restoration of popular sovereignty." A self-amending dispatcher is a
constitution, and constitutions have a failure literature. It would be
strange not to read it.

*See also:* [`mtg-layers.md`](mtg-layers.md) for the dispatch half;
[`df-procedural-magic.md`](df-procedural-magic.md) for a generator authoring
the lattice; and Mao, Aight and Dvorak — the other rule-changing card games
Suber's page and Fluxx's own references point at, if a second specimen is
ever wanted.
