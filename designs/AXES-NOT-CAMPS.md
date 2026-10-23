# Axes, not camps

Five dichotomies come up again and again in arguments about system design:
right-thing versus worse-is-better, neat versus scruffy, augmentation versus
automation, direct manipulation versus interface agents, and
language-carries-the-meaning versus environment-carries-the-meaning. Each names
a real choice that designers face.

The problem comes when a choice is treated as an identity. Used as an axis, the
distinction says what a decision costs and what it buys. Used as a camp, it says
who to dismiss. The same words can do either job, which is how "that's just
worse-is-better" can sound like analysis without saying what the choice costs.

This document separates the axes from the supposed camps. It also argues that
several of these dichotomies have been answered in practice by composition, with
both poles used in one system at different layers: neat and scruffy methods in
hybrid systems, symbolic and connectionist methods in neuro-symbolic work, and
direct manipulation and interface agents in the architecture of a shipped game.
The arguments are still often quoted as though they were open.

## The axes, stated as choices

| Axis | One pole | The other pole |
|---|---|---|
| Right thing / worse-is-better | Correctness, consistency and completeness are non-negotiable; simplicity of *interface* over simplicity of implementation | Simplicity of *implementation* is the highest value; ship, spread, then fix to 90% |
| Neat / scruffy | Formal methods, provable properties, one clean mechanism | Many mechanisms, biologically or psychologically motivated, judged by whether they work |
| Augmentation / automation | Build the thing that makes a person more capable | Build the thing that does the task without the person |
| Direct manipulation / interface agents | Show the user the state and let them act on it; predictability and user responsibility above all | Let a proactive, personalized agent act on the user's behalf; the interface should not need more sliders |
| Language / environment | Meaning lives in the notation; keep syntax simple enough that dumb tools suffice | Meaning lives in the live system; the environment is the artifact |

Worse-is-better already has a full treatment as a working method in
[`../skills/design-sense/methods/worse-is-better.md`](../skills/design-sense/methods/worse-is-better.md),
including Gabriel's decade of arguing against himself. This file is not about
how to use the axis. It is about why the axis is not a place.

## The East Coast / West Coast story

East coast versus west coast is folklore rather than a research programme, and
it does not match the sources.

Gabriel's own poles are not coasts. The essay names them "the MIT/Stanford
approach" and "the New Jersey approach": MIT in Massachusetts and Stanford in
California on the same side, against an industrial lab in New Jersey. That is
two research cultures with a shared taste, and a phone company with a different
one.

In AI the alignment reverses. The neats were the logicists around McCarthy at
Stanford; the scruffies were Minsky and Papert at MIT and Schank at Yale. If the
folk story says east means formal rigor, AI in the same decades says the
opposite.

People also moved. McCarthy went from MIT to Stanford in the early 1960s and the
logicist program went with him, so the figure most often cited for "east coast
rigor" founded the west coast lab. X came out of MIT's Project Athena, named as
the successor to Stanford's W. NeWS was thought up at CMU and built at Sun.
Smalltalk was PARC and its ancestry is Norwegian. By the late 1980s the coasts
shared mailing lists: the EDUCOM account in
[`../skills/no-ai-parrot/examples/educom-jobs.md`](../skills/no-ai-parrot/examples/educom-jobs.md)
was written the same night and sent to `lectroids@ucbvax.Berkeley.EDU`, a
Maryland graduate student's account of a Washington trade show posted to a list
at Berkeley within hours.

`verified: the "MIT/Stanford" and "New Jersey" labels are Gabriel's own, from
"Lisp: Good News, Bad News, How to Win Big." The neat/scruffy poles and
principal figures are standard. needs-check: Gabriel's date, cited variously as
the 1989 talk and the 1990–91 publication.`

The folk map persisted as a style label that could be used as a put-down. The
more useful question is what each choice costs, which is what the rest of this
file is about.

## Two proverbs from the OLPC Sugar list

A short instance of right-thing versus worse-is-better in this archive is two
messages on a mailing list, from two people who wanted the same outcome.

March 2007, the OLPC Sugar list. Guido van Rossum had asked whether the presence
of Etoys on the XO was *"a complete anathema to the sugar philosophy"* (the XO
had standardised on Python), and the thread ran for two weeks. Don's position:

> "**Just because something sucks isn't a reason not to use it if there is
> currently no better alternative.** Can you suggest or implement better
> alternatives to any of those modules? If not, then let's keep using them until
> we have enough time and experience to replace them, so we can learn from their
> strengths and weaknesses. **It would be unwise to attempt to reinvent the wheel
> without ever using one.**"

Vanessa Freudenberg, who was maintaining Etoys on the XO, answered in one
sentence:

> "Indeed. However, **as Alan likes to point out, a lot of effort nowadays goes
> into attempting to reinvent flat tires.**"

`verified: sugar@laptop.org, messages 001729 and 001731, 10 March 2007,
lists.laptop.org/pipermail/sugar/2007-March/. Full thread archived and read in
Don's repo under characters/don-hopkins/correspondence/threads/2007-03-sugar-python-etoys-visual-programming/.`

"Don't reinvent the wheel" and "don't reinvent flat tires" are both reasonable,
and they give opposite instructions. That is what an axis looks like. The
worse-is-better reading is that the installed system contains information your
redesign lacks, so build on it. The right-thing reading is that the installed
system has a defect built into its shape, so building on it carries the defect
forward however good the work above it is.

Neither of them was defending a side. Freudenberg put Squeak on her own list of
things that prevent popping the hood, alongside X11 and gtk. Don was arguing for
Python while citing Etoys, HyperCard, HyperLook, Robot Odyssey and Body Electric
as systems to learn from. The disagreement was about what to build on, not about
whose side to be on, and the camp framing cannot express that difference.

## The augmentation axis cuts across the others

Jaron Lanier's framing, in the review cited in
[`../skills/no-ai-parrot/corpus/CANON.md`](../skills/no-ai-parrot/corpus/CANON.md),
is an independent axis: human-centered augmentation at SRI against the
automation program at the AI lab. Engelbart's question to Minsky (*what are you
going to do for the people?*) is the augmentation pole addressing the automation
pole directly.

It does not line up with the others. Engelbart and Kay were both on the
augmentation side and McCarthy on the automation side, and none of that can be
predicted from their neat/scruffy positions. An axis that varies independently
of the others is a real axis.

## Direct manipulation versus interface agents

This axis was argued in public: Ben Shneiderman and Pattie Maes debated it at
IUI 97 in Orlando, moderated by Jim Alty, and again at CHI 97, and the IUI
session was published as a transcript. See
[`AGENTS-DEBATE-1997.md`](AGENTS-DEBATE-1997.md) for a fuller reading.

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

Ted Selker is sometimes described as occupying the middle ground. He did, but
the evidence is not the debate stage, where there were two debaters and one
moderator. It is Lieberman and Selker, "Agents for the User Interface,"
*Handbook of Agent Technology* (2003), and his adaptive-coaching work at IBM.
Henry Lieberman, the other author of that chapter, is also one of the editors of
*Watch What I Do: Programming by Demonstration* (MIT Press, 1993).
`needs-check: whether Selker appeared on the IUI 97 staging,
which the published transcript does not cover.`

### The Sims design, previewed in 1996

The debate was framed as a choice between the two. A design that combined them
had been described in public in April 1996, before either 1997 session, in the
Will Wright lecture archived in this repository.

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

The term "Braitenberg Machine" is in the transcript because it was checked by
hand. YouTube's speech recognizer garbled it; recovering it took looking it up
and then asking Wright what he had said. The phrase names the mechanism and
places it in a lineage, and an automatic transcript would have dropped it
without any sign. See [`NOISY-CHANNEL.md`](NOISY-CHANNEL.md) on why a fluent
mistranscription is worse than a gap, and on what repair costs.

The design is not at either pole, and it meets requirements from both. The
player does not command the Sim, and the Sim is not a conversation partner. The
player directly manipulates the objects, and the objects advertise to an
autonomous decision loop that chooses among them much like an auction.

| Shneiderman wanted | The advertisement architecture gives him |
|---|---|
| Comprehensible display | The advertisements are data you can inspect and author |
| User in control | You control placement; that *is* the input channel |
| Predictable system | Highest bid wins; the rule is one sentence long |
| No anthropomorphic deception | They are dolls, and are labelled dolls |
| User responsibility | You furnished the room; the outcome is yours |

| Maes wanted | The same architecture gives her |
|---|---|
| Proactive behavior | The Sim acts without being told |
| Personalization | Motives are per-Sim state |
| Not more sliders and buttons | Zero sliders; you put down a toilet |

Shneiderman objected that anthropomorphic representation "misleads, deceives,
increases anxiety, interferes with predictability, reduces user control, and
undermines users' responsibility". Wright had reached a similar conclusion from
focus testing with toys. In the same lecture he describes the Julie doll: a
talking doll was given to girls in focus groups, and after half an hour they
took the batteries out, because "the doll was telling them what the fantasy
was, and it was conflicting with what the girls were saying." Wright's
conclusion was that "if this is a doll house, we don't want the dolls to be
sentient things."

That is close to Shneiderman's argument against anthropomorphism, reached from a
different kind of evidence and stated in public before the 1997 sessions.

### What has changed since 1997

In 1997 neither side could fully show its approach working at scale. What has
changed is that the parts a combined design needs can now be built together:

- Teitelman's Interlisp "Do What I Mean" (DWIM), an early example of a system
  that edited your work without asking, and an early demonstration of why that
  can be alarming
- PBD: programming by demonstration, per Lieberman and Cypher. The user
  supplies examples and the system generalizes, which is delegation *with* an
  inspectable trace
- Drescher's schema mechanism: constructivist schema learning, treated at
  length in
  [`ongoingness/CURIOSITY-SCHEMA-LINEAGE.md`](ongoingness/CURIOSITY-SCHEMA-LINEAGE.md)
- Korz guarded slots: Ungar, Ossher and Kimelman's context-oriented dispatch,
  where a slot's applicability is itself declarative and inspectable; see
  [`korz/korz-prime/llm-evals.md`](korz/korz-prime/llm-evals.md)
- Selfish objects and advertisement auctions: Wright's mechanism as this
  repository runs it, in [`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md)
  and [`SELFISH-CONFIG-IN-PRODUCTION.md`](SELFISH-CONFIG-IN-PRODUCTION.md)

The specific new capability is that an advertisement no longer has to be a
number. In 1996 an object advertised `hunger: 40` because the resolver was
arithmetic. A resolver that reads language can accept an advertisement that
states its conditions, its cost and its reasons. The Braitenberg machine that
decides what to do next can then consult a human-readable market instead of a
scalar one, and the market stays inspectable, authorable and diffable, as
Shneiderman required.

### Symmetry of access as a checkable rule

The Sims shows that both sets of requirements can be met at once, but it is an
example, not a rule. The rule underneath it is symmetry of access, and this
repository already has a three-modality version of it.

[`webtop/TREE-NAVIGATION.md`](webtop/TREE-NAVIGATION.md) requires that every
structural operation be reachable by keyboard, pie menu and drag, all three
invoking the same named command rather than three code paths that happen to
agree, and states this as a lint rather than a preference. Adding the agent as a
fourth modality turns the 1997 argument into a property that can be checked:

> **Every capability an agent can reach, a human can reach, through the same named command — and
> the other way round.**

In [Korz](korz/README.md) terms this becomes mechanical. The capability is a
slot; keyboard, pie, drag and agent are coordinates on a `via` dimension; and a
properly factored capability is guarded on its receiver and says nothing about
`via`. An asymmetry is then a guard you can see, and the audit is a search:
*find every slot whose guard mentions `via`, and justify it.* Agent-only and
human-only powers both show up in the same place, instead of hiding in the gap
between two implementations of the same intent.

On this view the tradeoff the axis assumes need not be forced. Shneiderman
wanted a comprehensible, predictable, authored command set in which
responsibility can be located. Maes wanted something proactive that did not need
more sliders. If the capability is factored out of the surface, the agent drives
the same commands a person drives, and so leaves a trace that can be replayed,
diffed, taught from and refused.

The claim needs one refinement: symmetry of capability, asymmetry of throughput.
A human cannot send ten thousand messages a second and an agent can, so rate
limits and `robots.txt` are legitimate. Withholding a capability is different
from metering it, and when a service withholds instead of metering, that is a
policy choice rather than an engineering constraint.

An example in this repository points the other way.
[`skills/quora-harvest`](../skills/quora-harvest/) exists because a person
reading a Quora thread has to undo three separate folding mechanisms by hand,
while a script does it in one pass. The capability existed but was not offered
through the interface people use, and the only available fix was to automate it.
Full treatment, with the tests:
[`../skills/design-sense/lenses/interfaces-to-agency.md`](../skills/design-sense/lenses/interfaces-to-agency.md).

Ken Kahn's position has the same shape. He argues that *growing* an
architecture of interacting elements is more promising than building it by
hand, and he hand-built Pictorial Janus, ToonTalk's robots and birds, and the
eCraft2Learn blocks so that children could grow behavior through them. The
parts are built by hand, the behavior is grown, and the interface is where they
meet. This corresponds to the crystallize/deoptimize loop of
[`korz/korz-prime/`](korz/korz-prime/) with people in it: his "grow it" is the
deopt direction, Alan's "design the organisation of the parts" is the
crystallize direction, and the architecture is the movement between them rather
than a choice of side.

### Responsibility

> **"To me, responsibility will be the central issue in this debate."**
> — Ben Shneiderman, 1997

He put this as a challenge rather than a prediction. This repository tries to
meet it, and should be judged on that.

Combining the two poles does not by itself answer him. An advertisement market
is auditable and an auction result can be explained, but neither tells you who
is accountable when the agent acts. The architecture has to address that in how
it is built, which is what the following are for:

- Advertisements are authored artifacts, not emergent behavior. Somebody wrote
  each one, it is in version control, and it can be read before it runs. See
  [`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md).
- The record is kept and can be inspected afterwards. This is what
  [`cursor-mirror`](../skills/cursor-mirror/) and
  [`skill-snitch`](../skills/skill-snitch/) do: you can see what the system
  actually did rather than what it reported.
- Provenance travels with content, so an artifact says where it came from. This
  is argued in [`readings/`](readings/README.md) and enforced by
  [`../skills/no-ai-parrot/`](../skills/no-ai-parrot/).
- Consequential steps are held for a person, per
  [`../skills/thoughtful-commitment/`](../skills/thoughtful-commitment/) and the
  boundary argument in
  [`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md).
- Deterministic checks sit at the boundary, so the parts that must be right are
  verified rather than trusted (the *Determinishtic* position below).

None of this discharges the obligation. It makes it possible to locate:
responsibility cannot be delegated to a mechanism, but a mechanism can avoid
hiding where it went. Shneiderman asked who is answerable. The answer this
repository gives is a named person, with the record kept so that the question
can be asked.

## The axis underneath the language/environment split

This axis is the one most present in daily practice, and the cases that cross
it are the most informative.

Notation side: keep the syntax simple enough that simple tools work. Lisp's
homoiconic s-expressions mean a text editor can edit code structurally, and that
`grep`, `diff`, patch and version control all work on the real artifact. Emacs
edits Lisp well because the syntax is trivial to parse. The artifact is an inert
file, and that is useful: it can be mailed, archived, reviewed and diffed by
tools that know nothing about the language.

Environment side: keep the live system as the truth. Smalltalk's syntax is
harder to parse mechanically, and its answer is a better place to work rather
than better parsers: the class browser, the inspector, the debugger and the
image. You edit a method in a browser and it is live immediately; the snapshot
is the deliverable.

Both sides have costs. Text files give you version control, review and history,
and cost you liveness. Images give you liveness and cost you what depends on the
artifact being a file: the diff, the merge, the code review, the thirty-year-old
tape you can still read.

The cases that combine them show it is an axis rather than a camp. Lisp machines
had the whole live environment (window system, inspectors, debuggers,
incremental compilation) while keeping s-expressions in files. That is not a
compromise between two groups; it is a point in a two-dimensional space that the
two-camp story cannot represent.

A second case comes from a commercial game rather than a research lab. Edith,
the internal Sims editor for the SimAntics visual programming language, was
compiled into The Sims instead of left standalone, and Don's stated reason is
the environment-side argument:

> "Edith has grown a lot and is much wiser, now that she's integrated into The
> Sims instead of running as a separate program, so she is actually able to debug
> and edit code and data **while it's running live in the game**."

`verified: Don Hopkins to SimWatch@egroups.com, 2000-08-26`
— recovered text and provenance in
[`sims/MEDIUM-RESCUE.md`](sims/MEDIUM-RESCUE.md)

That is the Smalltalk position, reached by a game studio for production reasons,
in a codebase that still shipped as files. It also had the cost the axis
predicts: Edith was never publicly released, and the obstacle Don names is
documentation. A live environment does not explain itself to people outside the
team.

### Who Edith was for

Calling that a failure assumes that reaching people outside the team was the
goal. It was not. The people SimAntics was built for were all in the building:

| | |
|---|---|
| Jamie Doornbos | wrote the language ("Soul of the Sims") |
| Don Hopkins | ported it to Windows and made it easier to use |
| Patrick J Barrett III | the heaviest user and the resident expert; adopted it fully, and *"made it much more colorful"* |
| Will Wright | a user, and the one whose iteration cost mattered most |

Others wrote SimAntics too. Patrick wrote the most of it and became the person
you asked.

`verified: Doornbos and Barrett credited with SimAntics in
[sims/sims-team-history.md](sims/sims-team-history.md); the "more colorful"
phrase is Barrett's own, to Don.`

A tool can justify a lot of effort for a small group of users if lowering their
iteration cost changes what gets designed. That was the case here: the work was
spent on a handful of people's creative throughput, most of all Patrick's and
Will's, rather than spread over a user base, and it paid off in the game.

Teller has a general form of this answer to arguments from user count:

> "Magic is putting in more effort than any reasonable person would expect you to."

His illustration is cockroaches appearing from an empty top hat. They researched
and sourced special cockroaches, then found special styrofoam to trap them, and
arranged all of it for one trick. *"No reasonable person would do that, but they
do it."*

`verified: Teller, quoted by Gwern Branwen to Dwarkesh Patel, 13 November 2024. Harvested in
[LATENT-SPACE-REPUTATION](LATENT-SPACE-REPUTATION.md).`

On that view, effort beyond what a cost-benefit case would justify is part of
the method. A tool nobody outside the building used, polished well past that
point, is like the styrofoam: invisible in the result, and part of why the
result works.

A resident expert is what made skipping documentation workable. Questions went
to Patrick. That works as long as everyone who needs an answer can reach him,
which is the in-the-room condition stated as a staffing fact rather than a
design preference.

This gives the axis a more precise form. The environment side works well when
the users are in the room: known, few, reachable and able to ask. Documentation
is the cost of leaving the room, and a tool that is not leaving does not owe it.
The axis does not say liveness is worse; it says liveness does not travel, and
Edith was not meant to travel.

The other side of this came later. When Wright did want Edith released, the
missing documentation was the obstacle, and the release did not happen. The
cost comes due when the audience changes, and by then it is larger.

### Replacing the notation

There was a third option, and the franchise took it. The Sims could likely have
paid for documentation, but it never shipped Edith. Over four versions, the
notation was instead replaced by languages that were already documented:

- The Sims 1 and 2: SimAntics tree code, bespoke and undocumented outside the
  building
- The Sims 3: C# on .NET
- The Sims 4: Python

The third option is to stop maintaining your own notation and adopt one whose
manual, tools, community and hiring pool already exist. A bespoke visual
language needs its own documentation, debuggers and hiring. Python comes with
all of these, and a modding community can be productive without EA writing any
documentation.

The details are in
[`VISUAL-PROGRAMMING-LINEAGE.md`](VISUAL-PROGRAMMING-LINEAGE.md). The part that
matters for this axis is what survived the change: the advertisement and auction
model. It persisted through both migrations, and by Sims 3 it had become
declarative tuning data. The mechanism was attached to the execution model, not
to the visual notation. The environment-side commitment lasted, and the notation
was the part that could be replaced. This is the opposite of what the usual
framing of the axis would predict, and it is why this repository borrows the
mechanism from Sims 1 while writing ordinary files. It is also why this
repository keeps skills as files even though the running session is more
convenient; see
[`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md) on a prompt
expiring into a checked-in artifact.

A smaller observation about notation: Barrett made SimAntics more colorful, and
he writes email in large colorful text too. Color in a visual language is often
treated as decoration; for a heavy user of that language it carried meaning, and
he used it in whatever medium he had.

The choice is still open for everyone, in current terms: is the running system
the truth, or is the checked-in file the truth? Notebooks, containers,
live-reload, infrastructure-as-code and prompt-versus-file are all versions of
this question. See
[`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md), where it appears
as *a prompt should expire into a checked-in file*: a notation-side answer,
chosen deliberately, for notation-side reasons.

## Composition

For neats and scruffies, a reasonable historical reading is that both approaches
are in use at different layers, and many working systems use both at once.

The pattern can be stated as a rule:

> **Scruffy where you are exploring. Neat where it counts. Deterministic checks
> at the boundary between them.**

This is an architecture rather than a compromise position, and this repository
has arrived at it several times. It has a name taken from someone else's
comment: "Determinishtic", meaning formal where the formality buys something and
loose elsewhere. See
[`../skills/no-ai-parrot/corpus/CORRECTIONS.md`](../skills/no-ai-parrot/corpus/CORRECTIONS.md)
for the coinage and its author.

The neuro-symbolic version of the same approach has its own document:
[`NEURO-SYMBOLIC.md`](NEURO-SYMBOLIC.md).

## Labels used as verdicts

An axis used to describe a choice is a design tool. The same axis used to assign
someone to a camp ends the discussion without adding information.

"That's just worse-is-better" used as a verdict works like "just a next token
predictor": it names a real property and then stops, as if naming it were the
argument. Gabriel's essay is an analysis with a reluctant conclusion, and he
spent a decade rebutting himself in public, so quoting the title as a dismissal
reverses its sense.

The test is the one in [`../skills/no-ai-parrot/`](../skills/no-ai-parrot/):
does a claim follow the label? "This is the New Jersey choice, and here is what
it costs us in correctness and buys us in adoption" is a design argument.
"That's New Jersey" on its own is not.

## See also

- [`../skills/design-sense/methods/worse-is-better.md`](../skills/design-sense/methods/worse-is-better.md)
  — the axis as a working method, with Gabriel's self-rebuttals
- [`../skills/design-sense/methods/power-of-simplicity.md`](../skills/design-sense/methods/power-of-simplicity.md)
  — Ungar on the language kernel, which parallels Gabriel and argues with him
- [`NEURO-SYMBOLIC.md`](NEURO-SYMBOLIC.md) — neats and scruffies, current era
- [`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md) — the
  notation-side choice, made deliberately
- [`../skills/no-ai-parrot/`](../skills/no-ai-parrot/) — what happens when a
  label stops describing and starts dismissing
- [`../skills/cursor-mirror/characters/i-beam/CONSTITUTION.md`](../skills/cursor-mirror/characters/i-beam/CONSTITUTION.md)
  — the direct-manipulation-versus-agents axis applied to one agent's binding
  rules: Shneiderman's constraints as an acceptance test, Selker's COACH as the
  pattern, and the responsibility question above answered per article
