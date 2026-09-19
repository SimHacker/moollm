# Reasoning Is Not Science

**Class:** lens · **Attribution:** Don Hopkins; Alan Kay on "reasoning as opposed to science," via Jerry Bruner's *Goedelisation*; Feynman on cargo cult science

> **Reasoning is checked by whether each step follows. Science is checked by whether
> the world objects. Fluency improves the first and does nothing for the second.**

Science had to be *invented*. It is a prosthetic, built because the unaided reasoning
apparatus is unreliable — heuristic methods bolted on to aid poor commonsense
thinking, in Kay's phrasing of Bruner's argument. Which flips the usual intuition
about who needs it. If the prosthetic exists because your reasoning is bad, then
confidence in your reasoning is not a license to set the prosthetic down. It is the
symptom it was built for.

> **More concern about "reasoning" as opposed to "science"** — Alan Kay, on what is
> missing from the current push, [Quora, Sept 2026](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/alan-kay/media/quora-recaps/agi-paradigm-shifts-and-no-moores-law-for-software.md)

## Skill is the aggravating factor

A chain of inference is audited from the inside: every step is checked against the
last, by the same apparatus that produced it. Verbal and inferential fluency makes
that audit faster and more satisfying, and buys exactly nothing on the outside. So
the better a reasoner you are, the further into a corner you travel before anything
stops you, and the harder you are to extract — because each objection arrives as one
more argument to be defeated rather than as data that gets a vote.

Intelligence is not protective here. It is the accelerant. Which is why the
correction has to be structural and cannot be an exhortation to be humble.

## The form without the check

Cargo cult science, in Feynman's sense: citations, probabilities, calibration
vocabulary, the posture of measurement. Attaching a number to a belief feels like
measuring it and is not. Reviewing a design by arguing about it feels like testing
it and is not.

The tell is what happens when the argument finishes. If the output is a conclusion,
it was reasoning. If the output is a thing that can now embarrass you — a prototype
someone else can drive, a recorded prediction with a date on it, an experiment with a
result you did not pick — the prosthetic is attached.

## Specimen: a canon that outlived its evidence

The clearest documented case is a community organised around debiasing. The
load-bearing assumption is that knowing the catalogue of cognitive biases lets you
apply the corrections to yourself. That assumption is weak on its own literature:
debiasing training shows modest, domain-specific effects, and Pronin's **bias blind
spot** says self-assessment is precisely where the machinery fails.

Then the replication crisis went through the heuristics-and-biases shelf that the
foundation was built on — priming, ego depletion, a good deal of the late-2000s
social psychology corpus — and the update was slow, because by then the canon was the
credential. Fluency in the syllabus counted as qualification.

Which is Kay's other complaint wearing a different costume: a curriculum that teaches
only the arrangements that already exist. A trade school for legacy epistemology
cannot produce the people who replace it
([../masters/alan-kay.md](../masters/alan-kay.md)).

## Specimen: a law from one anecdote

"Given enough eyeballs, all bugs are shallow," asserted as a law in *The Cathedral
and the Bazaar* on the strength of one project's experience, received by a whole
industry as a finding. Heartbleed and Shellshock were the external check arriving
a decade late in the most-eyeballed code on earth. The reasoning was fine. Nobody
ran the study.

## The counter-specimen

The practice looks like this: gwern's dual-n-back meta-analysis concluded the
apparent IQ gains were mostly publication bias — against his own community's
enthusiasm, with data — alongside randomized blinded self-experiments, published
negative results, and pages annotated as wrong years after publication. Same
subculture, opposite epistemic posture. The difference is not intelligence. It is
that being wrong was arranged to cost something and the grade was left where it
could be found.

## The test

Grade a *practice* — a person's working method, a field's, a community's, or your own
on one particular question. Not a person, and not a tribe.

**Does the practice generate a claim that could embarrass whoever holds it, and is the
grade recorded somewhere they cannot quietly lose it?**

It is a test with answers, which is what makes it better than sorting people into camps:

| Practice | Verdict | Why |
|---|---|---|
| gwern's self-experiments and meta-analyses | **yes** | Blinded trials, published negative results, pages annotated as wrong years later |
| Tetlock's forecasting tournaments; prediction markets | **yes** | A date, a number, a scoreboard someone else keeps |
| MIRI's decision-theory output | **mostly no** | Enormous argumentative volume, very little that a year could falsify |
| Scott Adams' persuasion frame | **structurally no** | Built so that being contradicted confirms it — no year can return a verdict |

The same person can score differently on different practices, which is the point. The
unit is the method, not the human.

Second test, for a person or a field: **what did the last update cost?** If no
position has been given up in years, no check is attached — and volume of argument
is evidence of the disease rather than the cure.

Third test, for a design review: **what leaves the room?** A decision is reasoning.
A thing someone outside the room can operate is science.

## Cost is not evidence — the martyr's exemption

The strongest-looking defence against this whole lens is a price paid. *I am no armchair
theorist; my position has cost me, continuously, for years.* It is a real distinction and
it measures the wrong quantity.

A cost you chose, and can keep choosing, is still internally authored. The world only
gets a vote if it can make you change your mind, so a price you are willing to pay
forever has been **removed from the circuit** rather than wired into it. Martyrdom feels
like empiricism from the inside and does none of the same work: suffering for a belief
demonstrates sincerity, which was never the thing in doubt.

So the question is never *what has this position cost you*. It is **what did the last
update cost** — and a practice with a large bill and no updates is the failure mode
wearing its most convincing disguise.

### And the ability to absorb the cost is what disables the check

Which gives the mechanism its economics. External validation arrives as consequences, so
anything that lets you absorb consequences indefinitely severs the feedback loop:

- **Money**, which buys the ability to be unbudgeable — your own infrastructure, your own
  platform, no editor, and the option of outlasting everyone's patience.
- **Status**, which removes the people who would have said no, and replaces peers with an
  audience.
- **Fluency**, which converts every incoming objection into one more argument to win.

Note what these have in common: each is normally read as a *qualification*. This is the
same inversion as the top of the file — the prosthetic exists because the apparatus is
unreliable, so the attributes that make you feel entitled to set it down are the ones
that make setting it down most dangerous. Conspicuous capacity is Veblen's insight in
Minsky's territory: the expense buys visibility and endurance, and endurance is exactly
what a mind needs to never be corrected.

The live specimen is any sufficiently rich founder whose beliefs no longer meet
resistance from anyone whose livelihood does not depend on him.

## Specimen: a premise that shipped and still lost

The cypherpunk thesis of the 1990s: strong cryptography, deployed widely enough, routes
around politics. Reasoned from first principles, internally airtight, and stated as a law
of nature —

> The Net interprets censorship as damage and routes around it.
> — John Gilmore, the movement's canonical aphorism

Twenty-five years later the deployment argument was **won**. TLS is everywhere, Signal
exists, disk encryption is on by default, and Snowden's own conclusion was that the math
held. Mass surveillance arrived anyway.

The falsified claim was *sufficiency*, and the reason is that content was never where the
leverage was. Metadata sits outside the envelope. Endpoints get owned. Centralisation
parked the plaintext with a dozen companies who answer subpoenas and sell the remainder.
Law compels what ciphers refuse. And the surveillance that actually showed up was a
business model people opted into, not a man on a wire.

Which is the lens in one sentence: the threat model was audited internally for twenty
years and was wrong about the *world*, not about the math. No amount of further reasoning
about ciphers could have returned that verdict, and the movement's own success is what
makes it unarguable — you cannot blame the outcome on insufficient adoption.

## What to do instead

Put the check outside the reasoner.

- **Build the artifact that makes the argument** rather than the argument
  ([everything-is-concrete](../methods/everything-is-concrete.md)) — Kay's invent-the-future
  vote is this lens stated as a method.
- **Keep state and history where it can be audited** — inspectable files, recorded
  predictions, diffs. A conclusion held only in a head has no external surface.
- **Give the system parts that disagree.** A single confident reasoner is the failure
  mode, so the fix is architectural: Minsky's society, and
  [adversarial-committee](https://github.com/SimHacker/moollm/tree/main/skills/adversarial-committee)
  as the working version. You do not get calibration by asking a mind to be humble;
  you get it by making disagreement structural.
- **Watch for the correlation ceiling.** Kay credits Judea Pearl here, and Pearl's
  point is the formal statement of this lens: no quantity of correlation answers a
  counterfactual without a causal model. A machine that only reasons over what
  co-occurred has the same disease, and it is now being baked into weights.
- **Precommit while the values are intact, in observable terms.** A Ulysses contract for
  epistemics: write down the tripwires *other people can see* — who may invoke them, and
  what you owe when they do, which is never a rebuttal. Aimed at a future self who will
  have arguments and be fluent, so it cannot route through that self's judgment. The rule
  that makes it work rather than decorate: log the outcome when you were right too, or you
  will stop logging.

And the reason to keep the prosthetic on: the Palaeolithic brain does not get
upgraded. Announcing that you have debiased yourself is the most Palaeolithic move
available.

**Go deeper:**
Richard Feynman, ["Cargo Cult Science"](https://calteches.library.caltech.edu/51/2/CargoCult.htm)
— "the first principle is that you must not fool yourself, and you are the easiest
person to fool" ·
[Wikipedia: Bias blind spot](https://en.wikipedia.org/wiki/Bias_blind_spot) ·
[Wikipedia: Replication crisis](https://en.wikipedia.org/wiki/Replication_crisis) ·
[Philip Tetlock, *Superforecasting*](https://en.wikipedia.org/wiki/Superforecasting) —
the scoreboard as method ·
[Thorstein Veblen, conspicuous consumption](https://en.wikipedia.org/wiki/Conspicuous_consumption)
— why the capacity to absorb a cost is displayed rather than hidden ·
[Ulysses pact](https://en.wikipedia.org/wiki/Ulysses_pact) — binding the future self who
will have better arguments ·
[Judea Pearl, *The Book of Why*](https://en.wikipedia.org/wiki/The_Book_of_Why) ·
[the Kay answer this came out of](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/alan-kay/media/quora-recaps/agi-paradigm-shifts-and-no-moores-law-for-software.md)

**See:** [../methods/everything-is-concrete.md](../methods/everything-is-concrete.md)
— the constructive half · [simulator-effect](simulator-effect.md) — the audience
does this to your system, and you do it to your own arguments ·
[stage-magic](stage-magic.md) — a demo that hides the mechanism is the same
temptation aimed outward · [../masters/alan-kay.md](../masters/alan-kay.md) ·
[../masters/marvin-minsky.md](../masters/marvin-minsky.md) ·
[../../no-ai-slop/](../../no-ai-slop/) — CERTAINTY-THEATER and the claim ledger are
this lens applied to a model's own output
