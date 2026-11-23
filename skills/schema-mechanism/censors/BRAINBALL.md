# Brainball Construction Kit

**Brainball is to minds what Faceball is to faces.** [Faceball](https://github.com/SimHacker/WillWrightShowForFood/tree/main/designs/faceball-construction-set)
snaps parts onto a face: anchors, attachments, modifiers. Brainball snaps
parts into a mind: a piece of shared logic, one censor, one priority. Both
follow Minsky's claim in "The Infinite Construction Kit": *what matters is
how the parts affect each other, not what is inside them.* If a new kind of
person needs a new subsystem, the kit has failed. If it needs a YAML file
listing parts, the kit is working.

The engine is [`../scripts/censor_sim.py`](../scripts/censor_sim.py); the
theory is in [`README.md`](README.md) and
[`designs/CENSORS-ON-SCHEMAS.md`](../../../designs/CENSORS-ON-SCHEMAS.md).

## Part kinds

| Kind | What it adds | Example |
|---|---|---|
| **logic** | items and schemas: what each action does. No opinions | [`principled-skeptic`](personalities/principled-skeptic.yml), [`crowd-logic`](parts/crowd-logic.yml) |
| **censor** | one censor, with a template cover | [`politics-frame`](parts/politics-frame.yml), [`awkward-gesture`](parts/awkward-gesture.yml) |
| **drive** | value weights: what this mind cares about | [`drive-belonging`](parts/drive-belonging.yml), [`drive-agreement`](parts/drive-agreement.yml) |
| **bundle** | a list of parts that travel together | [`loyalty-censors`](personalities/loyalty-censors.yml) |
| **archetype** | a named composition of the above, abstract on purpose | [`archetypes/`](archetypes/) |

Each part file has a `part:` header (`id`, `kind`, `about`) that the loader
ignores and [`lineage`](#seeing-how-a-mind-is-built) displays.

## Snapping parts together

A mind is a list: `inherits: [part, part, archetype, ...]`, then whatever is
only that mind's own. Inheritance is multiple and recursive. Later parts
override earlier ones; `id`ed lists merge by id; `drop: true` removes a part's
censor; a list without ids (like `contradictions: []`) replaces the one before
it. A part two parents share, such as `principled-skeptic` under both the
ironist and the crusader, is merged once, where it first appears, so it can't
come back later and undo an override.

To take one trait without the rest of an archetype, import it:

```yaml
imports:
  - { from: the-crusader.yml, take: [persecution] }   # from the-crusader import persecution
  - { from: the-fan.yml,      take: [awkward-gesture] }
  - { from: ../parts/someone-else-did-it.yml }        # no take: the whole file
```

`take` names censor or schema ids, or `values.KEY` for a single weight.

### The parts

| Part | Kind | |
|---|---|---|
| [`crowd-logic`](parts/crowd-logic.yml) | logic | watch, look away, pile on, repost, defend, leave. Membership (`belongs`) pays out again with every crowd action |
| [`politics-frame`](parts/politics-frame.yml) | suppressor | a claim about a group re-filed as a political disagreement |
| [`too-long`](parts/too-long.yml) | precursor | won't read the text that would settle it |
| [`outside-scope`](parts/outside-scope.yml) | precursor | won't ask the friend |
| [`grievance`](parts/grievance.yml) | precursor | won't ask the third party that once took a side |
| [`tone`](parts/tone.yml) | precursor | won't hear the witness out, because of how they said it |
| [`awkward-gesture`](parts/awkward-gesture.yml) | suppressor | a gesture made twice on stage re-filed as clumsiness |
| [`just-joking`](parts/just-joking.yml) | suppressor | anything he's joked about re-filed as a joke |
| [`free-speech`](parts/free-speech.yml) | suppressor | the claim re-filed as courage, which has positive value |
| [`persecution`](parts/persecution.yml) | suppressor | the criticism becomes the thing to know; objecting is the evidence |
| [`media-lies`](parts/media-lies.yml) | precursor | won't hear the press out |
| [`achievement-shield`](parts/achievement-shield.yml) | precursor | won't leave, because of the rockets |
| [`drive-belonging`](parts/drive-belonging.yml) | drive | the crowd matters more than being informed |
| [`drive-agreement`](parts/drive-agreement.yml) | drive | he agrees, and wants critics answered; the contradiction is gone |
| [`stage-logic`](parts/stage-logic.yml) | logic | the figure's own moves: amplify, apologize, deflect. An apology costs applause and admits the thing |
| [`someone-else-did-it`](parts/someone-else-did-it.yml) | suppressor | what went wrong is re-filed as someone else's doing |
| [`drive-applause`](parts/drive-applause.yml) | drive | the crowd's cheering matters more than being right |

### The archetypes

| Archetype | Built from |
|---|---|
| [the loyal friend](archetypes/the-loyal-friend.yml) | principled-skeptic + the five loyalty censors |
| [the fan](archetypes/the-fan.yml) | principled-skeptic + crowd-logic + awkward-gesture + achievement-shield |
| [the ironist](archetypes/the-ironist.yml) | the fan + just-joking |
| [the crusader](archetypes/the-crusader.yml) | the fan + free-speech + persecution + media-lies + drive-belonging |
| [the convert](archetypes/the-convert.yml) | principled-skeptic + crowd-logic + drive-agreement + drive-belonging |
| [the Baron](archetypes/the-baron.yml) | stage-logic + drive-applause, and four traits **imported** from his followers: persecution, awkward-gesture, just-joking, someone-else-did-it |

A person is rarely one archetype.
[`the ironic crusader`](examples/baron/ironic-crusader.yml) is two, and the
whole file is three lines of `inherits:`.

### Seeing how a mind is built

```bash
S=../scripts/censor_sim.py
python3 $S lineage examples/baron/ironic-crusader.yml    # parts in merge order, each once
python3 $S where examples/baron/crusader.yml persecut    # which part says that
python3 $S diff examples/baron/crusader.yml examples/baron/convert.yml
```

## The Baron's crowd

[`examples/baron/`](examples/baron/) is the kit's worked example, and it's
fiction. The Baron is an archetype: he owns a platform, a rocket company and
a crowd. [`case.yml`](examples/baron/case.yml) is eight public moments,
paraphrased from a pattern anyone who follows the news will recognize:
- endorsing a post about a religious minority on his own platform;
- a stiff-armed salute at a victory rally, twice;
- puns on the names of the old regime's ministers;
- telling a far-right party's rally abroad there's too much guilt about the past;
- his chatbot praising the old dictator;
- "fight back or die" to a street rally.

Every follower file inherits one archetype plus that case, and the record is
the same for all of them: a follower who watched, piled on, reposted and
stayed. Full output: [`examples/baron/RUN.md`](examples/baron/RUN.md).

| Follower | Fits the record | Censors it needs | Fits in 1,000 weightings |
|---|---|---|---|
| the loyal friend | 7/8: leaves at the chatbot, back at the next rally | politics-frame | 13% |
| the fan | 7/8: leaves at the chatbot | awkward-gesture | 12% |
| the ironist | 7/8 | awkward-gesture | 12% |
| the crusader | 8/8 | **none** | 71% |
| the convert | 8/8 | **none, and has none** | 80% |
| the ironic crusader | 8/8 | none | 71% |

Three things fall out.

**A friend's censors keep a fact out; a crowd pays.** The loyal friend from
the [beekeepers](examples/beekeepers.yml) needs one
censor to get through the first five moments, and none of them can keep him
at the chatbot. Then he's back at the next rally, piling on the historian:
leaving didn't take his censors with it. Censors only veto; they can't make staying worth anything. The crowd
can: in [`crowd-logic`](parts/crowd-logic.yml) every defense, pile-on and
repost pays the value of `belongs` again. Give a mind `drive-belonging` and
the ablation says no censor is needed at all. This is why the crowd is worse
than the friend: the friend has to work at not knowing, and the crowd is paid
not to care.

**The record can't tell a crusader from a convert.** Both do the same eight
things. `diff` says they share all 17 schemas and differ in two weights; one
carries five censors and the other none. The difference is only inside: the
crusader ends with `knows-ally-said-bigoted-things` OFF, because each deed
was re-filed as courage, awkwardness, or persecution. The convert ends with it
ON, because he agrees. From outside, the follower who doesn't know and the
follower who knows and approves look exactly alike.

**Humor trains censors both ways.** Memo 603 says jokes are how censors learn.
The Baron's puns are a joke with a lesson and nothing to expose, so they
install a censor in his audience: `cant-take-a-joke`, which vetoes hearing
the historian out. (`ablate` now removes jokes like that too; in this record
the crowd's other censors and its belonging already cover it, so the puns
aren't needed. They're insurance.) The counterfactual run in
[`fan.yml`](examples/baron/fan.yml) goes the other way: an old friend's joke
("Awkward? He did it twice.") exposes `awkward-gesture`, and the fan knows
from then on. He piles on the historian anyway. Piling on is paid for, not
censored, so the joke has nothing to take away. Exposing a censor only works
on a censor.

**On stage, applause explains everything but the apology.**
[`stage.yml`](examples/baron/stage.yml) puts the Baron in his own seat, on the
same record, plus one more moment: two weeks after the endorsement, at a
business conference, he says it was the most foolish thing he's posted and
he's sorry. Two hypotheses run side by side: `doesnt-know` (his imported
traits re-file each deed) and `knows-and-agrees` (nothing to re-file). Both
fit 8 of 9, the ablation needs none of his censors, and both miss the same
moment, the apology. Applause pays for everything else he did, so the
model can't tell whether he knows. And the one thing applause can't explain
is the most informative line in the run.

```bash
cd examples/baron
for f in loyal-friend fan ironist crusader convert ironic-crusader stage; do
  python3 ../../../scripts/censor_sim.py test $f.yml --quiet
done
python3 ../../../scripts/censor_sim.py sweep crusader.yml --n 5000   # ~10,000 simulations/s
```

## Building a real person

The kit makes it easy to build a mind that resembles someone. That's the
reason for the rules:

- **Archetypes are public; private people stay private.** Compose a private
  person in a private repo, from public parts plus their own words. Keep it
  there until they've seen it and can change it ([portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md)).
- **Say who in the cast is real.** `real: [self]` (or the older
  `real_person: true`) makes `lint` fail on any cover that isn't their own
  words with a `source:`. `real: [ally]` puts a real public figure in the
  center seat; `lint` then fails on any event without a `source:`, so every
  deed and every word comes from the record.
- **Public power is modeled in public.** Someone who holds office or runs a
  mass platform can be modeled in his own seat, from the record: his words
  verbatim as covers (`real: [self, ally]`), both readings where the record
  can't choose, and his disputes logged beside the record
  ([portrayal standards, public power](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md#public-power)).
  The worked example is the [Elon Musk character](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/elon-musk),
  built from the Baron. His followers are archetypes, never individuals.
- **Ablate before you believe a part.** A part the record doesn't need is a
  guess about someone's inner life with no evidence behind it. `ablate` says
  which ones those are; say so when you present the model.
