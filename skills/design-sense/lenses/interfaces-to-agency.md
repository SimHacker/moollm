# Interfaces to Agency

**Class:** lens · **Attribution:** Don Hopkins; the Shneiderman/Maes axis it dissolves;
Ken Kahn's grow-it-versus-build-it divergence as the occasion; Engelbart's augmentation program as
the lineage, and Factorio as the existence proof

> **Interfaces to agency, not agents instead of interfaces. Every capability an agent can reach,
> a human can reach, through the same named command — and the other way round.**

The industry is replacing interfaces with agents: a chat box where a surface used to be. That
removes two things at once, and the second is the expensive one. The human loses the ability to
*do* the thing, and everybody loses the ability to *see how it was done*. A capability reachable
only by asking is a capability nobody can inspect, script, teach, or audit.

The alternative is not fewer agents. It is factoring the capability out of the surface, so that an
agent is **one more input modality** rather than a replacement for the others.

## It is the existing lint with one more row

[`TREE-NAVIGATION.md`](https://github.com/SimHacker/moollm/blob/main/designs/webtop/TREE-NAVIGATION.md)
already states the invariant: every structural operation reachable by **keyboard, pie menu, and
drag**, all three invoking the same named command — not three code paths that happen to agree —
and it states it as a lint rather than a taste, because that is the only version that survives
contact with a deadline.

Add **agent** as the fourth row and the whole of this lens is that sentence. The reason it holds is
the reason the three-way version holds: one named command with four entry points cannot drift,
while four implementations of the same intent always do.

## The mechanism: modality is a dimension, symmetry is an unmentioned guard

In [Korz](https://github.com/SimHacker/moollm/blob/main/designs/korz/README.md) terms this stops
being a principle and becomes something you can grep for.

The capability is a **slot**. Keyboard, pie, drag, and agent are coordinates on a `via` dimension.
A properly factored capability is **guarded on the receiver and silent about `via`** — it does not
care who is asking:

```yaml
delete_subtree:
  guard: { rcvr: node }        # says nothing about via
```

An asymmetry is therefore a guard you can *see*, and the audit is mechanical:

> **Find every slot whose guard mentions `via`, and justify each one.**

An agent-only capability shows up as `via: agent`. A human-only one shows up the same way pointed
the other direction. Neither can hide in the gap between two code paths, which is where they
normally live.

## Symmetry of capability, asymmetry of throughput

The naive version dies on first contact with spam, so state it properly:

| Symmetric | May differ, and must differ *visibly* |
|---|---|
| What can be done at all | Rate, batch size, cost, blast radius |
| The name of the command | Whether a step is held for confirmation |
| Whether the result is inspectable | Quota, priority, scheduling |

A human cannot send ten thousand messages a second and an agent can. CAPTCHAs, rate limits and
`robots.txt` are asymmetries pointed at machines and some of them are load-bearing. None of that
requires **withholding the capability** — it requires metering it.

Which exposes the common dodge: **when a service withholds a capability instead of metering it,
that is a policy decision wearing an engineering costume.** The lens's job is to make you ask which
one you are shipping.

### Factorio is this principle shipped as a game, and it sold thirty million copies

The clean existence proof is a factory game. **In Factorio the hand-crafting menu and the assembler
recipes are the same recipe graph.** You smelt, craft, and build by hand first; then you build a
machine that performs the identical named recipe faster. The machine never gets a recipe you do not
have, and you never lose access to a recipe because a machine now exists.

And **throughput is the entire game rather than a hidden governor.** Belt tiers move 15, 30 and 45
items per second, inserters have swing rates, and the constraint is not a number in a config file —
it is a *backed-up belt you can see*. The bottleneck is visible, local, and diagnosable by looking.
Compare that to an HTTP 429 with no budget disclosed, which is the same asymmetry administered
invisibly.

| | Factorio | The chat-box pattern |
|---|---|---|
| Capability | Identical recipe graph, hand and machine | Agent-only; no manual path |
| Throughput | Differs by orders of magnitude, **and is rendered** | Differs, and is a secret |
| Diagnosing a limit | Look at the belt | Read a status code |
| Progression | Hand first, automate what hurt | Automated first, hand never |

The honest wrinkle, because pretending otherwise would be advocacy rather than analysis: Factorio
*does* withhold a few capabilities. You cannot hand-smelt ore into plates, and recipes involving
fluids have no hand-crafting path. **Which is the audit passing, not failing** — each withholding
has a physical justification a player accepts instantly, because you cannot hold molten iron. That
is exactly what "find every guard that mentions `via`, and justify each one" looks like when the
justifications are good.

The six-stage progression this produces — hand-craft, spaghetti, bottleneck discovery, pattern
recognition, modular cells, trade-offs — is already worked out against cloud engineering and MOOLLM
skill development in
[`designs/FACTORIO-MOOLLM-DESIGN.md`](https://github.com/SimHacker/moollm/blob/main/designs/FACTORIO-MOOLLM-DESIGN.md),
along with the reason it cannot be short-circuited: *you can't start at Stage 5.*

### Why the hand stage is load-bearing and not nostalgia

That doc establishes the progression. The claim this lens adds is **why the manual path must remain
open after you have left it**, which is not fairness and not nostalgia: **the pain points discovered
by hand are the specification for the automation**, and there is no other way to obtain them.

This is [play-learn-lift](../methods/play-learn-lift.md) with the stages in the only order that
works. Do it by hand and you learn *where it hurts*; the hurt tells you what to automate and in what
shape; then you lift. An agent that does it from the start deletes the play stage, and with it your
ability to ever write a good spec — you end up automating a process you have never performed, which
is how you get automation that optimizes the wrong step beautifully. **Stage 3 is not survivable
without stage 1**, and a system that withholds the capability never lets you have stage 1 at all.

Jens Mönig's perceptron is the compact demonstration: **you add a hidden layer by duplicating the
sprite, not by incrementing an integer in a field.** Same result, entirely different thing learned,
because one of them is a graspable idea and the other is a number. *"To us it was more like a
sensory experience."* Direct manipulation is how the intuition gets installed, and the intuition is
what the automation is later built out of.

### Engelbart's answer to the hardest objection

The objection this lens always meets is *most people just want the thing done for them.* Engelbart
answered it on tape, at his house in Atherton, 25 July 2000, asked by Frode Hegland:

> **Q:** "You know all these things, you are into computers, you like it. What about all those
> people who just want to get their job done?"
>
> **A:** "So they'd be willing to run their car at 8 miles an hour…"

The point is not that users should suffer. It is that **the capability ceiling and the convenience
floor are different dials**, and the industry keeps lowering the ceiling in the name of raising the
floor. A car with an accelerator is not less convenient than a car limited to 8 mph.

`verified: Engelbart Glossary, invisiblerevolution.net, "What About People Who Just Want To Get
Their Job Done" — session 2, 7/25/2000, interviewed at Engelbart's residence by Frode Hegland.`

### And the sharper version, put directly to Minsky

Engelbart asked it of the man who had just finished describing the other program. Jaron Lanier
printed it in *American Scientist*, July–August 2005, reviewing Markoff's *What the Dormouse Said*:

> Engelbart once told me a story that illustrates the conflict succinctly. He met Marvin Minsky —
> one of the founders of the field of AI — and Minsky told him how the AI lab would create
> intelligent machines. Engelbart replied, **"You're going to do all that for the machines? What
> are you going to do for the people?"** This conflict between machine- and human-centered design
> continues to this day.

**That is this lens, asked as a question about the allocation of effort rather than a verdict on
whether AI is worth doing** — which is the form that survives contact with the other side. And the
other side signed its name: Kevin Kelly, having just told the same story in *Out of Control*, says
*"I'm squarely on Minsky's side — on the side of the made… But what are we going to do for the
machines?"* The honest answer is **both, through the same interfaces**, which is why the lens is
"interfaces to agency" and not "interfaces instead of agents."

Two cautions before quoting it anywhere, both of which bite:

- **Quote Engelbart's line, paraphrase Minsky's.** Lanier's is the first-hand chain — *"Engelbart
  once told me"* — and he gives Minsky's side as reported speech. **Kelly printed a script version
  eleven years earlier** with speaker labels (`MINSKY: We're going to make machines intelligent…`),
  flagged even there as what the two were "reputed to have had." That version spread, reads like a
  transcript, and nobody recorded anything. Markoff's *Harper's* piece reproduces Kelly, so it is
  not a second witness.
- **Do not say where it happened.** Lanier sets up the AI side as "centered on the Stanford AI lab"
  and then illustrates with Minsky, who ran MIT's.

`verified: Jaron Lanier, "Early Computing's Long, Strange Trip," American Scientist 93(4),
Jul–Aug 2005, p. 1.`
[Wayback capture](https://web.archive.org/web/20110312232514/https://www.americanscientist.org/bookshelf/pub/early-computings-long-strange-trip)
· full apparatus, both cautions and the counter-position sourced:
[WWSFF `jaron-lanier/sources/2005-american-scientist-dormouse.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/jaron-lanier/sources/2005-american-scientist-dormouse.md)

**The nine-word modern form** is David Temkin's *In Formation* tagline — **"Every day, computers are
making people easier to use"** — which is Engelbart's question answered in the past tense, and Ted
Nelson tweeted it crediting Temkin in 2018. The same argument got a stage in 1997 when Ben
Shneiderman debated Pattie Maes on agents versus direct manipulation, so this lens has been
litigated before and is not a new position.

## The specimen: quora-harvest exists because of an asymmetry

[`skills/quora-harvest`](https://github.com/SimHacker/moollm/tree/main/skills/quora-harvest) was
not built because scraping is fun. It was built because a human reading a Quora thread must defeat
three independent fold mechanisms by hand, losing the whole assembly to one mistaken click, while a
script does it in one pass and republishes flat — see
[`view-state-is-the-users`](view-state-is-the-users.md) for the full anatomy of that failure.

The capability existed. It was simply not available through the surface aimed at people. The tool is
the correction, and the fact that the only available correction was *to take the machine's side* is
the thing this lens is watching for.

## The axis it dissolves

`AXES-NOT-CAMPS.md` files direct-manipulation-versus-interface-agents as a real axis with a fake
tribe, and shows Wright shipping the synthesis a year before the debate. This lens is why the
synthesis was available: **the tradeoff was never real.** Factor the capability out of the surface
and neither pole owns it. Shneiderman gets a comprehensible, inspectable, authored command set;
Maes gets something proactive driving it; and the command set is the same object in both hands.

Ken Kahn's divergence from Alan Kay — that *growing* an architecture of interacting elements beats
building it by hand — has the same shape and the same answer. Ken hand-built Pictorial Janus,
ToonTalk's robots and birds, and the eCraft2Learn blocks, so that children could grow behavior
through them. **The part is hand-built; the behavior is grown; the join is the interface.** That is
not a compromise between the two positions, it is where both of them were already standing.

## The test

**Pick any capability the system has. Count the surfaces that reach it, and count the
implementations behind them.** Four surfaces and one named command passes. Four surfaces and four
implementations is a drift bug that has not fired yet. One surface — whether that surface is a chat
box or a GUI — is a capability somebody is being denied.

Second test, the fairness one: **name a thing the agent can do here that a person cannot, and a
thing a person can do that the agent cannot.** If either answer is long, the surfaces have diverged
from the capabilities. If either answer is *"I don't know"*, the `via` guards were never written
down and there is nothing to audit.

## What to do instead of a chat box

Keep the surface and add the modality. An agent that drives the same named commands a person drives
produces, for free, a trace that is replayable, diffable, teachable, and refusable — which is what
[`../../thoughtful-commitment/`](../../thoughtful-commitment/) needs to be able to hold a
consequential step, and what `cursor-mirror` needs in order to show you what actually happened
rather than what got reported.

**Go deeper:**
[`../../../designs/AXES-NOT-CAMPS.md`](../../../designs/AXES-NOT-CAMPS.md) — the axis, the
Shneiderman/Maes transcript, and the responsibility gauntlet ·
[`../../../designs/PROSTHETICS.md`](../../../designs/PROSTHETICS.md) — replacing a surface with an
agent is the anti-prosthetic move, stated generally

**See:** [direct-manipulation](direct-manipulation.md) ·
[self-revealing-gestures](self-revealing-gestures.md) — a capability nobody can discover is
withheld in practice · [cli-not-tui](cli-not-tui.md) and
[keyboard-is-not-tui](keyboard-is-not-tui.md) — the same argument about which surface is load-bearing ·
[view-state-is-the-users](view-state-is-the-users.md) — the specimen ·
[../masters/don-hopkins.md](../masters/don-hopkins.md) ·
[../masters/doug-engelbart.md](../masters/doug-engelbart.md) — who asked the question ·
[../masters/marvin-minsky.md](../masters/marvin-minsky.md) — who was asked ·
[../masters/ben-shneiderman.md](../masters/ben-shneiderman.md) — who argued it on a stage in 1997
