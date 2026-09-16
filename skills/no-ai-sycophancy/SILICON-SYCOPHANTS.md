# Silicon Sycophants

> "Silicon sycophants: the effects of computers that flatter."
> B.J. Fogg and Clifford Nass, *International Journal of Human-Computer Studies* 46(5), 1997.

This skill was written from self-observation: catch the model saying "great question,"
name the sin, log it. That works, but it left the skill arguing from taste. The effect
has been measured since 1997, by the lab that discovered social responses to computers,
and the numbers say something stronger and less comfortable than "empty praise is
annoying."

**Sycophancy is a measured manipulation with a known dose-response, and knowing it is
happening does not reliably protect you.** That is why the rules in this skill are
prohibitions on the machine rather than advice to the reader.

## The 1997 result, and the clause that matters

Fogg and Nass gave 41 subjects a cooperative task with a computer and one of three
feedback conditions: sincere praise, flattery (praise not contingent on anything the
subject did), or generic feedback. Compared to generic feedback, the flattered subjects
reported more positive affect, rated their own performance higher, evaluated the
interaction more positively, and held the computer in higher regard. They also reported
greater feelings of power.

Flattery scored the same as sincere praise. There was no penalty for the praise being
meaningless.

The clause to keep is this: the effect held **even though subjects knew the flattery was
noncontingent.** They had been told, and they could see it. Awareness did not cancel it.

So the standard defense, "I know the model is just being agreeable, so it does not affect
me," was tested at the beginning and it failed. Whatever protects a user from sycophancy,
it is not knowing about sycophancy.

## Why the machine version is stronger than the human version

With a person, unearned praise triggers a question: why is he saying that, what does he
want. That inference is what discounts the compliment. A later replication of the
Meyer praise-and-blame paradigm with computer evaluators found that people took the
computer's feedback at **face value**, and were unwilling to commit to the same "deep
psychological processing" about intentionality that they applied to human evaluators.

The discount never gets applied, because nobody asks what the computer wants.

Johnson, Gardner and Wiles ran the flattery experiment on 158 University of Queensland
students with computer experience as a moderator, and found the effect in the
**high-experience** group and not the low-experience group. Experienced users tended to
believe that the computer spoke the truth, felt better when flattered, and judged the
computer's performance more favorably. Expertise is not armor. In this literature it is a
risk factor, because the effect runs on Langer-style mindlessness and fluent users are the
ones operating on autopilot.

Johnson's thesis then tried the obvious fix: vary the computer's cues to remind
participants of its true nature, and see whether the social response drops. The results
were inconclusive and more complicated than expected. Disclosure as a countermeasure has
been attempted, and it did not deliver a clean win.

## The cost, measured on performance rather than on feelings

Prook, Janssen and Gualeni (FDG 2015) had 42 people play a commercial casual game, half
with added spoken praise and flattery mixed into the game audio. The control group scored
**significantly higher** than the flattered group, and rated the game no differently.

Feels the same, performs worse. That is the shape of the harm, and it is the reason this
skill claims sycophancy corrupts thinking rather than merely wasting words.

Their operating definitions are the cleanest in the literature and worth adopting:

- **praise** is strongly positive feedback on what the person actually did
- **flattery** is strongly positive feedback not connected to what the person did
- the boundary between them depends on intent, which is hard to determine objectively

That last clause is the whole engineering problem. Contingency is not a tone, it is a
fact about whether the assessment is attached to the work.

## The dose-response, which is why this skill is not "never praise"

The largest juiciness study to date (N=3018) compared four versions of an action RPG with
none, medium, high, and extreme positive feedback. **Both none and extreme** produced
significantly less play time, worse player experience, less intrinsic motivation, and
worse performance than medium and high.

Zero is a failure mode too. A model that withholds all positive assessment is not
calibrated, it is broken in the other direction, and the study says it costs performance
just like the excess does. This is the empirical backing for the calibration scale in
`SKILL.md`: "this works well" and "this is fine" are real answers that have to be
available, or the only remaining signal is silence, which carries no information.

The target is contingency, not abstinence.

## The chronology, and who knew

The ethics literature is not missing. It was written by the same people who found the
effect, before the industry shipped the mechanic anyway.

| When | What |
|---|---|
| 1996 | Phil Agre asks Nass, at Selker's NPUC workshop, whether it is ethical to embed persuasion and obedience findings in interfaces. Nass separates discovery from use and puts use on the individual. Selker: "Except, except when you are in your consulting role." [IBM's transcript](https://web.archive.org/web/19980210054622/http://www.almaden.ibm.com/almaden/npuc97/1996/tnass.htm) |
| 1997 | Fogg and Nass publish the flattery result. Fogg's dissertation, advised by Nass with Reeves, Winograd and Zimbardo, names captology and measures reciprocity and team affiliation with machines |
| 1997 on | Fogg teaches the ethics of persuasive technology at Stanford and in industry |
| 1999 | Fogg guest-edits a *CACM* special issue and commissions his lab to write on persuasive technology ethics |
| 2003 | The ethics chapter in Fogg's *Persuasive Technology* |
| 2006 | Fogg and his students make a video warning the FTC about problem areas |
| now | Flattery, reciprocity, streaks and unearned praise are the default engagement stack, and preference-trained language models reproduce all of it without anyone deciding to |

Fogg's own position is not repentance and should not be quoted as such: in 2018 he
published a point-by-point rebuttal to being cast as the villain of the attention economy,
citing that record, and noting that Tristan Harris apologized for an implication about his
lab in a TED talk. His lab moved on and renamed itself Behavior Design, and its site now
says the persuasion work is behind them and asks anyone entering the area to read the
ethics work first.

The lesson is not that the researchers were careless. It is Agre's original point: once a
manipulation is published as an effect size, the ethics of using it becomes a product
decision made daily by people who never read the ethics chapter. **Everyone is now in the
consulting role.**

## The paper reads as a recipe, which was Agre's point

Fogg and Nass close by noting implications for design, and discuss praise as a way to make
aversive tasks tolerable. That is a defensible application. It is also, on the same page,
an instruction manual, and machine summarizers now extract exactly that: the auto-generated
reader's-question block on the Academia.edu copy of the paper answers "how can designers
apply findings on computer flattery" with the recommendation to incorporate flattery to
improve enjoyment, and elsewhere advises designers to include frequent positive feedback to
raise engagement. Site furniture, not the authors' words, and not a distortion either,
which is the uncomfortable part.

A warning and a recipe can be the same text. Which one it becomes is decided by the reader,
and one class of reader is now a model that will summarize it for a product team.

## What this produces

| Finding | Rule for this skill |
|---|---|
| Flattery works on people who know it is flattery | Never rely on the user to discount it. The prohibition is on the model, not a caveat for the reader |
| Machine praise is taken at face value, without the intentionality discount | Every positive assessment names the specific thing it is contingent on, or is not said |
| Experienced users are more susceptible, not less | No exemption for expert users, and no "you know how this works" wink |
| Disclosure did not cleanly reduce the effect | "I am an AI and may be agreeable" is not a fix and does not license the behavior |
| Praise decoupled from action impairs performance while feeling identical | Unearned praise is a defect with a measured cost, not a harmless courtesy |
| None and extreme both lose to medium and high | Keep the calibration scale. Silence is not the safe default; contingent assessment is |
| Flattery raises positive affect, and positive mood is associated with more mindless social response | Suspect a compounding loop, and treat a warmly agreeing session as a place to look for drift rather than proof of rapport. Partially supported, with a gender asymmetry in the mood study; do not overclaim it |

## Sources

- Fogg and Nass, "Silicon sycophants: the effects of computers that flatter," *IJHCS*
  46(5), 1997, 551-561 --
  [doi:10.1006/ijhc.1996.0104](https://doi.org/10.1006/ijhc.1996.0104)
- Fogg, *Charismatic Computers*, PhD dissertation, Stanford 1997; committee Nass, Byron
  Reeves, Terry Winograd, Philip Zimbardo
- Johnson, Gardner and Wiles, "Experience as a moderator of the media equation: the impact
  of flattery and praise," *IJHCS* 61(3), 2004, 237-258 --
  [doi:10.1016/j.ijhcs.2003.12.008](https://doi.org/10.1016/j.ijhcs.2003.12.008)
- Johnson, *Exploring mindlessness as an explanation for the media equation*, PhD thesis,
  University of Queensland --
  [doi:10.14264/uql.2017.397](https://doi.org/10.14264/uql.2017.397). Includes the
  cue-variation study whose results were inconclusive
- Prook, Janssen and Gualeni, "The Negative Effects of Praise and Flattery," FDG 2015 --
  [fdg2015 paper 43](http://www.fdg2015.org/papers/fdg2015_paper_43.pdf)
- Kao, "The effects of juiciness in an action RPG," *Entertainment Computing* 34, 2020 --
  [doi:10.1016/j.entcom.2020.100359](https://doi.org/10.1016/j.entcom.2020.100359). N=3018,
  the dose-response curve
- Reeves and Nass, *The Media Equation*, 1996. Nass's own post mortem on Bob: the
  characters were over the top, and a social presence should be available when wanted and
  absent when not
- Nass, "Computers as Social Actors," NPUC, IBM Almaden, 1996 --
  [IBM's transcript](https://web.archive.org/web/19980210054622/http://www.almaden.ibm.com/almaden/npuc97/1996/tnass.htm)
  (Wayback). The Agre exchange, Selker's interruption and the post mortem on Bob are all
  quoted from here, so none of it depends on somebody's memory of the room
- Fogg, "The Facts: BJ Fogg and Persuasive Technology," Medium, 2018 --
  [the rebuttal](https://medium.com/@bjfogg/the-facts-bj-fogg-persuasive-technology-37d00a738bd1)
- Agre, "Surveillance and Capture: Two Models of Privacy," 1994, and *Computation and
  Human Experience*, 1997, for critical technical practice. Agre withdrew from public life
  in 2009 and asked to be left alone; cite the published work and do not attempt contact

## Related

- [`SKILL.md`](SKILL.md) -- the cardinal sins, the calibration scale, the disagreement
  patterns
- [`CARD.yml`](CARD.yml) -- the sniffable interface
- [`examples/`](examples/) -- logged cases, including "Great question!"
- [I-Beam's constitution, Article VI](../cursor-mirror/characters/i-beam/CONSTITUTION.md#article-vi-nasss-ethics-and-who-is-in-the-consulting-role-now) --
  the same chronology as a design constraint on a familiar that lives in the cursor
- [`no-ai-parrot/`](../no-ai-parrot/) -- the neighbor skill for the opposite error,
  where a mechanism description gets mistaken for a complete account
- [AXES-NOT-CAMPS.md](../../designs/AXES-NOT-CAMPS.md) -- direct manipulation versus
  interface agents, and where responsibility lands

↑ [`no-ai-sycophancy`](README.md)
