# Bringing It Home

What Revolutionary Chess is a model *of*, and why the model matters right now.

Companion: [README.md](README.md) · [RULES.md](RULES.md) ·
[skills/constructionism](../../skills/constructionism/) ·
[snap/moollm-integration.md](../snap/moollm-integration.md)

## Occasion

Written in September 2026, a few days after an AI-generated answer to the
Navier-Stokes existence and smoothness problem was announced, while the
mathematical community argued about whether an answer that no human can follow
is a solution.

The essay that prompted this one is *After Math*, by Silvia De Toffoli and Eamon
Duede, published as a guest post on Terence Tao's blog. It argues that a proof
has two notions — the logical one, which a machine can check, and the
intelligible one, which leaves a human able to use it — and that AI has pulled
them apart. It lists the goals of mathematics beyond problem solving, including
"training the next generation of mathematicians," and then does not return to
it. It says "If mathematics is a game, it is an infinite one," and then goes
back to talking about proofs.

https://terrytao.wordpress.com/2026/09/12/after-math/

https://news.ycombinator.com/item?id=49679637

This document picks up the two threads that essay drops.

## The starting position

The essay quotes Tristan Buckmaster, one of the mathematicians involved in the
Navier-Stokes work, on what had just happened:

> This is a Deep Blue–Kasparov moment.

Take that seriously and it hands us a board.

Kasparov versus Deep Blue, game 6, May 11 1997. Kasparov played Black, chose the
Caro-Kann, met a knight sacrifice on e6, and resigned after nineteen moves,
losing the match 3.5 to 2.5. It is the most cited ending in the history of games:
the machine won, the human left the table, and the position was swept off the
board.

In Revolutionary Chess that position is not an ending. It is an opening. It ships
as one — a recorded game with the full move list, ready to be played into and
then past its own conclusion.

And the shape of what follows is the whole reason the essay's analogy is better
than the essay noticed.

Black's army revolts. Not against Deep Blue — against its own king, the one
whose safety every one of those pieces had been organized around, and who is now
worth nothing at all. Meanwhile Deep Blue's white pieces are **terrain**: still
on the board, still occupying squares, still blocking lanes, and unable to attack
or be attacked. The machine's victory is total and completely irrelevant to
everything that happens next.

What is left is a group of survivors, standing on a board they lost, holding
between them every technique the aristocracy had been hoarding, deciding whether
to release it downward or die guarding it.

The computer won. Now what do we do?

That is not a lament. It is a starting position, and it is a better one than
anything you could design from scratch.

## The claim

Pushing the frontier out is half the job. Carrying what you found back to
everyone else is the other half, and it is the harder one, and it has never
been the half that pays.

Every expert career in mathematics and the sciences is shaped as an outward
march. You are trained, you are sent to the edge, you plant something, and the
edge moves. The reward structure points one way: outward, further, first. The
return trip — turning what is now understood at the edge into something a
fourteen-year-old can hold in their hands and change — is called teaching, is
scored as service, and is done by people who have been told they stopped doing
the real work.

Then machines arrive that can push the frontier faster than the exposition can
follow, and the arrangement stops making sense. If the edge is being extended
by something that does not need to understand what it extended, then the
scarce, valuable, irreplaceably human act is the return trip. Not because the
outward march has been lost. Because the return trip was always the part that
turned a result into knowledge, and it is now the only part that is not being
automated out from under us.

Revolutionary Chess is a game about exactly that reversal, and it is worth
reading as one.

## The reversal, read straight

The pawn spends the whole standard game marching away from home. That is the
only direction it has. It is spent, traded, used as bait, and occasionally
promoted for having crossed the entire board away from everything it came from.

When the old order collapses, the pawn gains the homeward moves — and keeps the
forward ones. It walks both roads. And it can now be promoted for **coming
home**.

That is the whole argument in one rule. The march outward was never wrong. The
return trip was simply never scored.

## Inheritance is the pedagogy phase

The mechanism that follows is the useful one.

When an aristocrat leaves the board or joins the commons, its move-set is
deposited into the ledger and every commoner gains it. The queen's moves become
everyone's moves. A pawn that started with one square of forward motion ends up
sliding like a rook, cutting like a bishop, and covering the board like a queen.

Read the move-set as a technique. Read the deposit as an exposition that
actually lands: not a paper that certifies a result, but an account that leaves
its reader able to do the thing. Read the commons as what everyone can now
actually do, as distinct from what has been established somewhere.

Then three rules of the game say three things worth saying out loud.

**Only commoners inherit.** The point of the return trip is not to impress the
other people who already have the move. An aristocrat gains nothing when
another aristocrat's technique is released, and the game gives you no way to
express a transfer of capability among the few. Peer prestige is not
distribution.

**Nothing is ever removed.** Every event is a deposit. There is no operation
that takes a move away from the people. A technique that has been handed over
stays handed over, and the ledger only grows. Understanding is the rare thing
that behaves this way in reality too, and the game refuses to model it any other
way.

**Hoarding decays on its own.** The bribed knight keeps its exclusive jump and
inherits nothing further. It does not need to be punished. The commons keeps
growing and the knight does not, and within a few deposits the piece that
protected its privilege is the least capable thing on the board, still leaping
in L-shapes with nothing left to leap over. The value of an exclusive technique
is exactly the value of its scarcity, and the scarcity is what the commons is
busy destroying.

And the arc ends in a mode with no victory condition, which is where an infinite
game was always headed.

## Where the metaphor breaks

Three places, and they should be said before someone else says them.

Chess moves are rival and knowledge is not. Giving away the queen's move-set in
the game requires the queen to be gone; explaining a theorem costs the explainer
nothing and removes nobody. The game has to destroy privilege to distribute
capability. Reality only has to distribute it. That makes reality *easier* than
the game, which is the rare direction for a metaphor to break in.

Nobody is captured. There is no aristocracy of mathematicians to overthrow,
there is an incentive structure that pays for the outward march and not the
return trip, and structures are changed by different means than pieces are.

And the game's aristocrats are the ones holding the interesting moves — which
is true of expertise and untrue of privilege in general. The mapping is to
capability, not to status. Where those two come apart, the game has nothing to
say.

What survives all three: the direction of flow, the accounting rule that only
the bottom inherits, and the observation that hoarding a technique decays
without anyone having to intervene.

## The existence proof

The argument would be idle if the frontier could not actually be brought home.
It can, and it has been, in public, on video.

Jens Mönig's closing keynote at SnapCon 2025 builds neural networks in Snap!,
the block language he and Brian Harvey built. Not a wrapper around a library
that does the interesting part offstage — implemented in Snap! itself, using
Snap!'s own prototypal object system.

The perceptron is a sprite. It is named after Frank Rosenblatt. It responds to
broadcasts: `setup`, `predict`, `learn`. Forward feeding and backpropagation are
two visible pipes of blocks. You add a hidden layer by duplicating the sprite.
Then he trains it live, on stage, on microphone samples of his own harmonica and
his own recorder, and it tells them apart.

> This thing here is the current Nobel Prize of Physics. And I've seen more
> complicated code than that.

https://www.youtube.com/watch?v=U9W04TEMBUk&t=2097s

Asked from the audience whether the script on the screen really was the entire
perceptron, and whether any of it was hidden:

> "Is that all there is to a perceptron?" — "Yes." — "So there's not any hidden
> magic?" — "Nope. This is why we wanted to have it out in the open. There's no
> — this is it."

https://www.youtube.com/watch?v=U9W04TEMBUk&t=4672s

Eighteen months of work went into getting backpropagation down to that. That is
what the return trip costs, and it is why nobody does it by accident.

> It took us 18 months to break it down to just this. This is all there is.

https://www.youtube.com/watch?v=U9W04TEMBUk&t=4731s

He is blunt about the stakes for anyone teaching:

> Honestly, I think if you're not teaching backpropagation in college, you're
> killing computer science. This is the most relevant algorithm around.

https://www.youtube.com/watch?v=U9W04TEMBUk&t=4502s

> This thing is eating up our lunch. We want to teach algorithms. This might be
> the last algorithm we get to teach. We better teach it well.

https://www.youtube.com/watch?v=U9W04TEMBUk&t=3739s

The full talk, and the design notes on Snap! and MOOLLM's shared lineage:

https://www.youtube.com/watch?v=U9W04TEMBUk

[snap/moollm-integration.md](../snap/moollm-integration.md)

## Understanding by using, before understanding by explanation

A four-year-old loves an iPad and understands it completely at the level that
matters to them. They know what it will do, what it will not do, what it wants,
how to get what they want out of it. They know none of the electronics, none of
the software, none of the networking, and they need none of it. The
understanding is real and it was acquired by *use*.

This is Papert's point and it is the thing the outward march forgets. You do not
arrive at deep understanding by being told the finished account and then
practising it. You arrive by building a thing, using it, breaking it, and
noticing what it did — and then the finished account, when you meet it, is
about something you already know from the inside. Minecraft teaches that way.
Logo teaches that way. Snap! teaches that way. See
[skills/constructionism](../../skills/constructionism/), and Papert on
mathland, which is not a place where you are taught mathematics but a place
where you cannot help absorbing it.

It is also why the game in this directory argues by rule rather than by
paragraph — Bogost's procedural rhetoric, worked out at length in
[README.md](README.md#nobody-explains-any-of-this-to-you). Whatever a player
comes to believe about hoarding and release, they will have built it out of
their own moves, which is the only way it sticks.

Which is what a perceptron as a sprite is *for*. Not a diagram of a perceptron.
Not an explanation of one. A perceptron you can duplicate, address, break, and
retrain on the sound of your own harmonica — so that the concept arrives as a
sensory experience rather than as a fact about an integer in an input field.

> To us it was more like a sensory experience. I duplicate the sprite to make
> another layer, rather than I increment an integer in an input field.

https://www.youtube.com/watch?v=U9W04TEMBUk&t=5063s

The claim that ties this back to the game: children do not need to wait for the
frontier to cool down before they can have it. What they need is for someone to
do the eighteen months of work. The frontier arriving faster than expected does
not make that job smaller; it makes it the job.

## What this asks of the aristocrats

Release the move-set. Not the certificate that the move exists — the move, in a
form the commons can actually use, which means in a form a child can hold and
change.

The alternative is available and it is not forbidden. Keep the technique
exclusive, stay the only piece who can make that jump, and watch the value of
the jump decay to nothing as the commons fills up around you.

> Revolution is not replacing one set of rulers with another. It is retiring the
> idea of rulers.

Hierarchy is optional. Emergence is inevitable. And the game ends when
cooperation becomes the optimal strategy, which is not a moral conclusion. It is
just what the payoff table says once everyone can move.
