# Axes, not camps

**The distinctions are real. The tribes are a map that does not hold.**

Five dichotomies do most of the background work in arguments about system
design: right-thing versus worse-is-better, neat versus scruffy, augmentation
versus automation, direct manipulation versus interface agents, and
language-carries-the-meaning versus environment-carries-the-meaning. Every one
of them names a genuine choice that a designer actually faces.

**The failure mode is turning a choice into an identity.** An axis tells you what
a decision costs and what it buys. A camp tells you who to dismiss. The same
words serve both jobs, which is how "that's just worse-is-better" can sound like
analysis while doing no work at all.

So this document separates the axes from the alleged camps, and then gets to the
part that actually matters: **most of these dichotomies were resolved long ago,
and the resolution was the same one every time — composition.** Neat and scruffy
settled into hybrids. Symbolic and connectionist settled into neuro-symbolic.
Direct manipulation and interface agents settled into an architecture that
shipped in a game. The arguments have outlived their own answers, and are still
quoted as though open.

## The axes, stated as choices

| Axis | One pole | The other pole |
|---|---|---|
| **Right thing / worse-is-better** | Correctness, consistency and completeness are non-negotiable; simplicity of *interface* over simplicity of implementation | Simplicity of *implementation* is the highest value; ship, spread, then fix to 90% |
| **Neat / scruffy** | Formal methods, provable properties, one clean mechanism | Many mechanisms, biologically or psychologically motivated, judged by whether they work |
| **Augmentation / automation** | Build the thing that makes a person more capable | Build the thing that does the task without the person |
| **Direct manipulation / interface agents** | Show the user the state and let them act on it; predictability and user responsibility above all | Let a proactive, personalized agent act on the user's behalf; the interface should not need more sliders |
| **Language / environment** | Meaning lives in the notation; keep syntax simple enough that dumb tools suffice | Meaning lives in the live system; the environment is the artifact |

Worse-is-better already has a full treatment as a *working method* in
[`../skills/design-sense/methods/worse-is-better.md`](../skills/design-sense/methods/worse-is-better.md),
including Gabriel's decade of arguing against himself. This file is not about
how to use the axis. It is about why the axis is not a place.

## The coastal story, dispatched briefly

East coast versus west coast is a rap feud. It was never a research programme,
and it does not survive five minutes of contact with the sources — so it gets
one section here and then no more attention.

**Gabriel's own poles are not coasts.** The essay names them **"the MIT/Stanford
approach"** and **"the New Jersey approach"** — MIT in Massachusetts and
Stanford in California, filed *on the same side*, against an industrial lab in
New Jersey. Two research cultures sharing a taste, and a phone company that had
a different one.

**In AI the alignment reverses.** The neats were the logicists around McCarthy
at Stanford; the scruffies were Minsky and Papert at MIT and Schank at Yale. If
the folk story says east means formal rigor, AI says the opposite during the same
decades.

**And people move.** McCarthy took the logicist program from MIT to Stanford.
X descends from Stanford's W. NeWS was thought up at CMU and built at Sun.
Smalltalk was PARC and its ancestry is Norwegian. Ideas travel in people, and
the people kept relocating.

`verified: the "MIT/Stanford" and "New Jersey" labels are Gabriel's own, from
"Lisp: Good News, Bad News, How to Win Big." The neat/scruffy poles and
principal figures are standard. needs-check: Gabriel's date, cited variously as
the 1989 talk and the 1990–91 publication.`

That is the whole of it. **The interesting question was never where people
worked — it is what the choice costs**, and that is what the rest of this file
is about.

## The augmentation axis cuts across the others

Jaron Lanier's framing, in the review cited in
[`../skills/no-ai-parrot/corpus/CANON.md`](../skills/no-ai-parrot/corpus/CANON.md),
is a genuinely independent axis: human-centered augmentation at SRI against the
automation program at the AI lab. Engelbart's question to Minsky — *what are you
going to do for the people?* — is the augmentation pole addressing the
automation pole directly.

It does not line up with the others at all. Engelbart and Kay were both firmly
augmentation; McCarthy was firmly automation; and you cannot predict any of it
from the neat/scruffy position. **Which is the test for a real axis: it varies
independently of the rest.**

## Direct manipulation versus interface agents

Direct manipulation versus interface agents got the most explicitly staged
version of any of these arguments: **Ben Shneiderman against Pattie Maes**, on a
stage, at CHI 97 in Atlanta, moderated by Jim Alty, published as a transcript.

> "Our goal is to create environments where users comprehend the display, where
> they feel in control, where the system is predictable, and where they are
> willing to take responsibility for their actions. **To me, responsibility will
> be the central issue in this debate.**"
> — Shneiderman

> "A software agent knows the individual user's habits, preferences, and
> interests. Second, a software agent is proactive. […] There are real limits to
> what we can do with visualization and direct manipulation because our computer
> environments are becoming more and more complex. **We cannot just add more and
> more sliders and buttons.**"
> — Maes

`verified: Shneiderman, B. and Maes, P., "Direct Manipulation vs. Interface
Agents," interactions 4(6), 1997, 42–61 — a transcribed debate. Alty's opening
("My name is Jim Alty. I think I am supposed to be the moderator") is verbatim
from the transcript. The published piece draws on debates staged at both IUI 97
and CHI 97.`

**On Ted Selker occupying the middle.** The middle ground is real and Selker
held it, but the receipt is not the CHI 97 stage — Alty moderated and the
debaters were two. Selker's claim to the middle is **Lieberman and Selker,
"Agents for the User Interface," Handbook of Agent Technology (2003)**, plus his
adaptive-coaching work at IBM, and Henry Lieberman is the other half of that
citation and the editor of *Watch What I Do: Programming by Demonstration*
(MIT Press, 1993). `needs-check: whether Selker appeared on the IUI 97 staging,
which the published transcript does not cover.`

### The composition already existed, and it was previewed a year early

Here is the part that makes this more than a historical note. **The debate was
framed as either/or, and the synthesis had already been demonstrated — in the
lecture archived in this repository, in April 1996, eleven months before CHI
97.**

Wright's Dollhouse preview, in
[`sims/sims-will-wright-microworlds-1996.md`](sims/sims-will-wright-microworlds-1996.md):

> "So a person's in a room, they have certain motivations, needs, they might be
> hungry, sleepy, lonely, angry. They scan the room for people and objects, and
> the objects are all kind of advertising: 'If you're angry, pick up me and
> throw me!', 'If you're hungry, eat me!'"

> "In the person's data structure, there's no knowledge of any objects in this
> environment whatsoever. The object itself contains the descriptions of how a
> person interacts with it, and why."

> "All we have to do is deal with them at a very local kind of a state machine,
> [**Braitenberg Machine**](https://en.wikipedia.org/wiki/Braitenberg_vehicle)
> kind of level."

`verified: verbatim from the lecture transcript. Valentino Braitenberg,
"Vehicles: Experiments in Synthetic Psychology," MIT Press, 1984.`

**That term is in the transcript only because someone went and got it.**
YouTube's speech recognizer mangled it, and recovering it took looking it up and
then **asking Wright directly** what he had said. It is the single most
load-bearing citation in the passage — it names the mechanism and places it in a
lineage — and an automatic transcript would have silently dropped it.
See [`NOISY-CHANNEL.md`](NOISY-CHANNEL.md) on why a fluent mistranscription is
worse than a gap, and on what repair actually costs.

**This is neither pole, and it satisfies both.** The player never commands the
agent and the agent is never a chat partner. The player does direct manipulation
*of the objects*, and the objects advertise to an autonomous decision loop that
resolves them like an auction. So:

| Shneiderman wanted | The advertisement architecture gives him |
|---|---|
| Comprehensible display | The advertisements are data you can inspect and author |
| User in control | You control placement; that *is* the input channel |
| Predictable system | Highest bid wins; the rule is one sentence long |
| No anthropomorphic deception | They are dolls, and are labelled dolls |
| **User responsibility** | You furnished the room; the outcome is yours |

| Maes wanted | The same architecture gives her |
|---|---|
| Proactive behavior | The Sim acts without being told |
| Personalization | Motives are per-Sim state |
| **Not more sliders and buttons** | Zero sliders; you put down a toilet |

And Shneiderman's sharpest objection — that anthropomorphic representation
"misleads, deceives, increases anxiety, interferes with predictability, reduces
user control, and undermines users' responsibility" — Wright had **already
reached from the other direction, empirically, via toys.** The Julie doll
lesson in the same lecture: a talking doll was given to girls in focus groups,
and after half an hour they took the batteries out, because "the doll was
telling them what the fantasy was, and it was conflicting with what the girls
were saying." Wright's conclusion was that "if this is a doll house, we don't
want the dolls to be sentient things."

**That is Shneiderman's anti-anthropomorphism argument, derived from a
children's toy, a year before he made it on stage.** Neither man was arguing
from the other's evidence, and they converged.

### Why the rematch is worth having now

The debate never resolved because in 1997 the agent side could not deliver and
the direct-manipulation side could not scale, exactly as each accused the other.
What has changed is that the pieces the synthesis needs are all now buildable at
once:

- **DWIM** — Teitelman's Interlisp "Do What I Mean" was the earliest agent that
  edited your work without asking, and the earliest demonstration of why that is
  frightening
- **PBD** — programming by demonstration, per Lieberman and Cypher: the user
  supplies examples and the system generalizes, which is delegation *with* an
  inspectable trace
- **Drescher's schema mechanism** — constructivist schema learning, treated at
  length in
  [`ongoingness/CURIOSITY-SCHEMA-LINEAGE.md`](ongoingness/CURIOSITY-SCHEMA-LINEAGE.md)
- **Korz guarded slots** — Ungar, Ossher and Kimelman's context-oriented
  dispatch, where a slot's applicability is itself declarative and inspectable;
  see [`KORZ-LLM-EVALS.md`](KORZ-LLM-EVALS.md)
- **Selfish objects and advertisement auctions** — Wright's mechanism as this
  repository runs it, in [`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md)
  and [`SELFISH-CONFIG-IN-PRODUCTION.md`](SELFISH-CONFIG-IN-PRODUCTION.md)

**The specific new capability is that an advertisement no longer has to be a
number.** In 1996 an object advertised `hunger: 40` because the resolver was
arithmetic. A resolver that reads language can accept an advertisement that
states its conditions, its cost, and its reasons — so the Braitenberg machine
that answers *what do I do next* can consult a rich, human-readable market
instead of a scalar one, while the market stays inspectable, authorable and
diffable in exactly the way Shneiderman demanded.

### The gauntlet

> **"To me, responsibility will be the central issue in this debate."**
> — Ben Shneiderman, 1997

That is the most durable sentence anyone said in that room, and he threw it down
as a challenge rather than a prediction. **This repository is an attempt to live
up to it, and the attempt should be judged on that.**

Composing the two poles is not an answer to him. An advertisement market is
auditable and an auction result is explicable, and neither of those tells you
who is accountable when the agent acts. So the architecture has to carry the
answer in its construction, which is what the following are for:

- **Advertisements are authored artifacts, not emergent behavior.** Somebody
  wrote each one, it is in version control, and it can be read before it runs —
  see [`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md).
- **The record is kept and is inspectable after the fact**, which is the
  [`cursor-mirror`](../skills/cursor-mirror/) and
  [`skill-snitch`](../skills/skill-snitch/) function: you can go back and see
  what the system actually did rather than what it reported.
- **Provenance travels with content**, so an artifact says where it came from —
  the discipline argued in [`voicewashing/`](voicewashing/README.md) and
  enforced by [`../skills/no-ai-parrot/`](../skills/no-ai-parrot/).
- **Consequential steps are held for a human**, per
  [`../skills/thoughtful-commitment/`](../skills/thoughtful-commitment/) and the
  boundary argument in
  [`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md).
- **Deterministic checks at the boundary**, so the parts that must be right are
  verified rather than trusted — the *Determinishtic* position below.

None of that discharges the obligation. It makes the obligation *locatable*,
which is the most any architecture can do: responsibility cannot be delegated to
a mechanism, but a mechanism can refuse to hide where it went. **Shneiderman
asked who is answerable. The honest reply is a person, named, with the record
kept so the question can be asked at all.**

## The people moved, and the receipts are specific

The reason the camps dissolve is that the individuals kept relocating, and ideas
travel in people.

- **McCarthy went from MIT to Stanford** in the early 1960s, and the logicist
  program went west with him. The single most cited "east coast rigor" figure
  founded the west coast lab.
- **X descends from W, which was at Stanford.** The X Window System came out of
  MIT's Project Athena, and it is named for being the successor to the W Window
  System from Stanford. The canonical east-coast window system has west-coast
  parentage in its own name.
- **NeWS was thought up in Pittsburgh.** Its ideas germinated at CMU and stewed
  in Andrew and X10; Gosling had written the Andrew window manager and Gosling
  Emacs there, and Rosenthal had worked on X. Then both authors moved to Sun in
  California and built it. Filing NeWS as a west coast system describes the
  return address, not the origin.
- **Emacs crossed twice before reaching a single demo.** MIT origin, then
  Gosling Emacs at CMU, then UniPress commercially — and then UniPress Emacs
  running on NeWS at the Sun booth at EDUCOM in Washington, in the case study at
  [`../skills/no-ai-parrot/examples/educom-jobs.md`](../skills/no-ai-parrot/examples/educom-jobs.md).
  A "west coast" window system running an "east coast" editor, demoed on the
  east coast, by a Maryland grad student, to the man who had just unveiled a
  machine built in California.
- **Smalltalk was PARC, and its ancestry is Norwegian.** Simula is not on
  anybody's coastal map.

`verified: needs-check on the NeWS lineage details, which are Don's own account
and consistent with the published history — confirm Rosenthal's X involvement
and the Andrew window manager attribution before asserting them flatly.`

### The internet finished the job, and there is a primary source

By the late 1980s the coasts were one mailing list.

The EDUCOM account in the case study was written the same night and sent to
`lectroids@ucbvax.Berkeley.EDU` — **an east-coast graduate student, writing from
Maryland, publishing his account of a Washington trade show to a list hosted at
Berkeley, within hours.** The header is the argument. Whatever coastal divide
existed in the folklore, the actual communication topology was already flat.

Which is also why the folk map survived: it stopped being a description and
became a *style label*, free-floating, available for use as a put-down long
after the thing it described had stopped being geographic.

## The axis underneath the language/environment split

This is the one still live in daily practice, so it deserves the most care. It
is also the one where the crossover cases are most instructive.

**Notation-side.** Keep the syntax simple enough that stupid tools work. Lisp's
homoiconic s-expressions mean a text editor can edit code structurally, and it
means `grep`, `diff`, patch, and version control all work on the real artifact.
Emacs edits Lisp well *because* the syntax is trivial to parse. The artifact is
an inert file, and inertness is the feature: it can be mailed, archived,
reviewed, and diffed by things that know nothing about the language.

**Environment-side.** Keep the live system as the truth. Smalltalk's syntax is
harder to parse mechanically, and the answer is not better parsers but a better
place to work: the class browser, the inspector, the debugger, and the image.
You edit a method in a browser and it is live immediately; the snapshot is the
deliverable.

**The trade is real and neither side is free.** Text files buy you
version control, review and archaeology, and cost you liveness. Images buy you
liveness and cost you everything that depends on the artifact being a file — the
diff, the merge, the code review, the thirty-year-old tape you can still read.

**And the crossovers prove it is an axis rather than a camp.** Lisp machines had
the whole live environment — window system, inspectors, debuggers, incremental
compilation — while still keeping s-expressions in files. That combination is
not a compromise between two tribes; it is a point in a two-dimensional space
that the tribal story cannot represent.

**A second crossover, from a shipped commercial game rather than a research
lab.** Edith — the internal Sims editor for the SimAntics visual programming
language — was deliberately compiled *into* The Sims instead of left standalone,
and Don's stated reason is the environment-side argument exactly:

> "Edith has grown a lot and is much wiser, now that she's integrated into The
> Sims instead of running as a separate program, so she is actually able to debug
> and edit code and data **while it's running live in the game**."

`verified: Don Hopkins to SimWatch@egroups.com, 2000-08-26`
— recovered text and provenance in
[`sims/MEDIUM-RESCUE.md`](sims/MEDIUM-RESCUE.md)

That is the Smalltalk position, reached by a game studio for production reasons,
in a codebase that still shipped as files. And it cost what the axis says it
costs: Edith was never publicly released, and the blocker Don names is
documentation — the price of liveness is that the artifact does not explain
itself to anyone outside the room.

### The price was declined on purpose, and the reason is a roster

Calling that a failure assumes reaching outside the room was the goal. **It was
not.** In the beginning SimAntics had four people around it:

| | |
|---|---|
| **Jamie Doornbos** | wrote the language — "Soul of the Sims" |
| **Don Hopkins** | ported it to Windows and made it easier to use |
| **Patrick J Barrett III** | used it heavily, and *"made it much more colorful"* |
| **Will Wright** | the only other user |

`verified: Doornbos and Barrett credited with SimAntics in
[sims/sims-team-history.md](sims/sims-team-history.md); the "more colorful"
phrase is Barrett's own, to Don.`

**A tool with four users can justify unbounded effort if one of the users is
Will Wright.** That is the argument, and it is an argument about leverage rather
than sentiment: Wright is a rare enough designer that lowering the cost of his
iteration changes what gets designed at all. The work was not amortized over a
user base. It was spent on one person's creative throughput, and then on
Patrick's, and it paid off in the game.

Which resolves the axis properly instead of splitting it. **The environment side
is correct exactly when your users are in the room** — known, few, reachable,
able to ask. Documentation is the tax you pay to leave the room, and if you are
not leaving, declining to pay it is not a debt. The axis does not say liveness
is worse; it says liveness does not travel. Edith was never trying to travel.

The flip side is real and shows up later: the moment Wright *did* want Edith
released, the undone documentation was the blocker, and the release did not
happen. **The tax comes due only when the audience changes, and by then it is
expensive.** That is the actual shape of the trade, and it is the same reason
this repository keeps skills as files even though the running session is more
convenient — see
[`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md) on a prompt
expiring into a checked-in artifact.

There is also a small delight worth keeping, because it says something about
notation. Barrett made SimAntics more colorful, and he writes **email** in huge
colorful text too — the same expressive instinct in both media. Color in a
visual language is usually treated as decoration; for a heavy user of that
language it was signal, and he reached for it in whatever medium he was handed.
Voice does not respect the boundary between a programming notation and a mail
client.

The choice is still in front of everyone, in current words: **is the running
system the truth, or is the checked-in file the truth?** Notebooks, containers,
live-reload, infrastructure-as-code and prompt-versus-file are all this argument
wearing new clothes. See
[`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md), where the same
question appears as *a prompt should expire into a checked-in file* — a
notation-side answer, chosen deliberately, for the notation-side reasons.

## The resolution is composition, not victory

For neats and scruffies specifically, the honest historical answer is that
**both won, at different layers, and the winning systems use both at once.**

The pattern generalizes and it is worth stating as a rule:

> **Scruffy where you are exploring. Neat where it counts. Deterministic checks
> at the boundary between them.**

That is not a compromise position, it is an architecture, and it is the one this
repository keeps arriving at independently. It has a name harvested from someone
else's comment: **"Determinishtic"** — deterministic-ish, formal exactly where
the formality buys something, loose elsewhere. See
[`../skills/no-ai-parrot/corpus/CORRECTIONS.md`](../skills/no-ai-parrot/corpus/CORRECTIONS.md)
for the coinage and its author.

The neuro-symbolic version of the same resolution has its own document:
[`NEURO-SYMBOLIC.md`](NEURO-SYMBOLIC.md).

## How these labels go wrong, which is the point of writing this down

An axis used to *describe a choice* is a design tool. The same axis used to
*assign someone a camp* is a thought-terminating cliché with a distinguished
pedigree.

"That's just worse-is-better" as a verdict does exactly what "just a next token
predictor" does: it names a real property, stops, and presents the stopping as
an argument. Gabriel's essay is an analysis with a reluctant conclusion, and he
spent a decade rebutting himself in public — quoting the title as a dismissal
inverts the thing.

The test is the same one in
[`../skills/no-ai-parrot/`](../skills/no-ai-parrot/): **does a claim follow the
label?** "This is the New Jersey choice, and here is what it costs us in
correctness and buys us in adoption" is design. "That's New Jersey" is a
sneer with a citation.

## See also

- [`../skills/design-sense/methods/worse-is-better.md`](../skills/design-sense/methods/worse-is-better.md)
  — the axis as a working method, with Gabriel's self-rebuttals
- [`../skills/design-sense/methods/power-of-simplicity.md`](../skills/design-sense/methods/power-of-simplicity.md)
  — Ungar on the language kernel, which rhymes with Gabriel and argues with him
- [`NEURO-SYMBOLIC.md`](NEURO-SYMBOLIC.md) — neats and scruffies, current era
- [`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md) — the
  notation-side choice, made deliberately
- [`../skills/no-ai-parrot/`](../skills/no-ai-parrot/) — what happens when a
  label stops describing and starts dismissing
