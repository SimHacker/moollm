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

**Does the practice generate a claim that could embarrass you, and is the grade
recorded somewhere you cannot quietly lose it?**

Second test, for a person or a field: **what did the last update cost?** If no
position has been given up in years, no check is attached — and volume of argument
is evidence of the disease rather than the cure.

Third test, for a design review: **what leaves the room?** A decision is reasoning.
A thing someone outside the room can operate is science.

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

And the reason to keep the prosthetic on: the Palaeolithic brain does not get
upgraded. Announcing that you have debiased yourself is the most Palaeolithic move
available.

**Go deeper:**
Richard Feynman, ["Cargo Cult Science"](https://calteches.library.caltech.edu/51/2/CargoCult.htm)
— "the first principle is that you must not fool yourself, and you are the easiest
person to fool" ·
[Wikipedia: Bias blind spot](https://en.wikipedia.org/wiki/Bias_blind_spot) ·
[Wikipedia: Replication crisis](https://en.wikipedia.org/wiki/Replication_crisis) ·
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
