# The Noisy Channel: Alan Kay, Claude Shannon, and nine layers of loss

**The artifact:**
[Alan Kay: Shannon Gave Us a Way of Dealing with Noisy Channels](https://www.youtube.com/watch?v=Cjntrqhn8pk)
(Don Hopkins, published 2026-08-28, 2:33).

**The occasion:** the Kristen Nygaard 100 Years Celebration Symposium, Aarhus
University, 2026-08-27. Kay was scheduled to speak on *How The First Simula
Catalyzed Early Thoughts About Objects* — his title slide, under portraits of
Nygaard and Dahl, is screen-shared through the whole incident.

**Kay was not in Aarhus.** He was at home in London, calling in over Zoom, and
that is the mechanism: the delay exists because he is remote, and the loop exists
because the far end of a link he could not see had a speaker and a microphone in
earshot of each other.

`verified: that Kay now lives in London is something he has explained publicly
himself, including on Quora — it is his own disclosure, not an inference.`

**What happened:** this was the AV setup and sound check before his talk — the
part of the schedule whose entire purpose is to find problems like this. Someone
in Aarhus left the live stream playing
out loud near an open Zoom microphone. So Kay's voice went out, came back
through the stream into the room, out of the room's speaker, into the room's
open mic, and back to Kay's own ears about 21 seconds later — over and over,
while he was saying this:

> "Shannon gave us a way of dealing with noisy channels."
>
> "I think about that almost every day. I realize what the fuck is going on and
> it's just so amazing."

`verified: transcript of Cjntrqhn8pk, verbatim`

**Shannon's noisy-channel coding theorem is the mathematics for precisely the
kind of channel that was garbling him as he praised it.** Not an irony. A
demonstration, delivered by the channel, unrequested, on the exact topic.

## Why this is a design document and not a video description

Because the recording is an unusually complete specimen of something this
repository deals with constantly and usually cannot see: **a signal passing
through a stack of lossy transformations, where each layer fails differently,
and where some of the failures are repairs, some are corruptions, and one is a
policy decision.**

Every argument here about transcription, dictation, patina and channel repair —
[`voicewashing/`](voicewashing/README.md),
[`voicewashing/DICTATE.md`](voicewashing/DICTATE.md), Article VI of
[`../skills/no-ai-parrot/CONSTITUTION.md`](../skills/no-ai-parrot/CONSTITUTION.md)
— is an argument about what a layer of this stack is allowed to do. Here is a
case where seven of them ran at once and left evidence.

## The stack, layer by layer

| # | Layer | Where | What it did to the signal |
|---|---|---|---|
| 1 | Kay speaking into his own microphone | his home | the source |
| 2 | Zoom, outbound | the wire | compression, packetization |
| 3 | The live stream | a CDN | encoding, and **segment buffering — most of the 21 seconds lives here** |
| 4 | The stream played out loud on a speaker | the Aarhus room | digital back to acoustic |
| 5 | The room's acoustics, into an open Zoom mic | the Aarhus room | reverberation, and **the loop closes here** |
| 6 | Zoom again, inbound, lap after lap | the wire | ~21 s per lap, artifacts compounding |
| 7 | Panopto's automatic captions, burned into the symposium recording | Aarhus | recognition under a **Danish** language prior |
| 8 | Don's screen recording | Don's desk | re-encode |
| 9 | YouTube's speech recognizer, on the re-encode | Google | recognition, plus **profanity censoring** |

Nine, counting properly, and the geography is the point rather than a detail:
**the loop passes through a room that Kay is not in.** He is the only
participant who cannot see why it is happening, and he is the only one hearing
it.

The point is not the number. The point is that **layers 7 and 9 are
categorically different from layers 2 through 6**, and the difference is the
whole subject.

**Layer 3 is where the 21 seconds actually comes from.** Not distance — an
HTTP live-streaming stack deliberately buffers several seconds of video so it
never runs dry, and the loop pays that toll on every lap. The delay is a queue,
which is worth knowing if you ever have to fix one.

## Three kinds of loss, and only one of them is noise

### Noise: the analog and network layers

Delay, dropout, compression artifact, acoustic re-entry. This is the classical
case, it is what Shannon's theorem addresses, and it is *content-free* — it
degrades the signal without opinions about what the signal should have been.
The fix is the one Kay himself supplied, and it is the correct engineering
answer: **"Just turn off the audio at your end on Zoom."** Break the loop.

### Hallucination-under-prior: Panopto hearing Danish

This is the layer that makes the recording valuable, and it is visible on screen
in the symposium player, timestamped, labelled with the disclaimer
*"Auto-generated captions may contain errors."*

The recognizer was running in a Danish context, at a Danish university. So:

| It heard | He said |
|---|---|
| "Sådan gaves A way of life with noisy channels" | "Shannon gave us a way of dealing with noisy channels" |
| "Og som. I kan se." | (English, unrecognizable at this point in the loop) |
| "So this is being we road to Mars and back in a streaming" | "So this is being rerouted to Mars and back" |
| "We just eat your hands" | (ditto) |
| "That it can I her? Can you hear my free?" | "Can you hear me?" |

`verified: read from the Panopto caption pane in the symposium recording,
timestamps 2:30:56–2:33:45`

**"Shannon gave us" became "Sådan gaves."** The recognizer did not fail to
hear; it heard confidently, in the wrong language, and produced fluent Danish
function words out of an English proper noun. And it did that to the name of the
man whose theorem describes what was happening to the audio.

This is not noise. **This is a prior overriding evidence** — the machine
supplying structure the signal did not contain, because its model said that
structure was likely. Which is the same mechanism as the simulator effect and
the same mechanism as apophenia, running in a transcription pipeline: see
[`../skills/no-ai-parrot/corpus/CANON.md`](../skills/no-ai-parrot/corpus/CANON.md)
on Wright's simulator effect, and
[`../skills/simulator-effect/`](../skills/simulator-effect/).

The practical consequence for anything in this repository that touches
transcripts: **a confident wrong transcription is worse than a gap**, because a
gap announces itself and a fluent mistranscription does not.

**There is a worked case of this, in another transcript in this repository, and
it cost real effort to fix.** In Will Wright's 1996 Stanford lecture, YouTube's
recognizer mangled the term *Braitenberg Machine* — a proper noun naming
exactly the mechanism Wright was claiming for The Sims' AI. Recovering it took
looking the term up and then **asking Wright himself** what he had said.

Note the shape of the repair, because it generalizes:

1. Someone **noticed** that a phrase was not a phrase.
2. They **researched** the candidate and found a term that made the sentence
   mean more, not less.
3. They **went to the source** — the speaker — rather than guessing.
4. They **linked the result** so the next reader inherits the work.

That is what channel repair costs when it is done honestly, and it is why the
cleanup pass in [`voicewashing/DICTATE.md`](voicewashing/DICTATE.md) is a
*human* pass. A recognizer cannot do step 3, and a proper noun it has never
heard is precisely where its prior does the most damage: the more specific and
load-bearing the term, the more likely it is to be smoothed into something
common and wrong. **The words most worth transcribing are the ones most likely
to be lost.** `align.py` in
[`voicewashing/`](voicewashing/TRANSCRIPTS.md) exists for exactly this reason —
it reports its own coverage and monotonicity so a bad alignment cannot pass
quietly.

### Policy: YouTube bleeping the enthusiasm

The third kind of loss is the one nobody models as loss at all. YouTube's
automatic transcript renders Kay's expletive as `[ __ ]`.

Consider what was removed. The word was not incidental — it was **the carrier of
the enthusiasm**, in a sentence about a man thinking daily, for decades, about
information theory and finding it amazing. A transcript that keeps the
proposition and drops the intensity has preserved the semantics and deleted the
person.

**This is Article VI violated by infrastructure.** Perfection is the enemy of
patina; the wear is the evidence; and here a pipeline sanded off the most human
feature of the utterance automatically, by default, with no one deciding to. The
constitution's rule against correcting anyone's typos — `[sic]` exists for this
— is the same rule, and the machine broke it at scale before any human got a
vote.

So the honest taxonomy, which is the reusable part of this document:

> **Noise degrades. Priors invent. Policy censors.**
> Only the first is what "channel repair" means, and only the first is what
> [`DICTATE.md`](voicewashing/DICTATE.md) authorizes a cleanup pass to touch.

## The accidental Lucier

Kay's setup reproduced **Alvin Lucier's *I Am Sitting in a Room* (1969)**, in
which Lucier recorded himself speaking, played the recording into the room,
re-recorded it, and repeated until the words dissolved and only the room's
resonances remained. The piece is *about* what a channel contributes when you
iterate a signal through it.

The difference is what remained, and where. Lucier's loop converged on the
**room** — standing waves, architecture made audible. Kay's loop ran through a
room *and* a network, so the residue is both: Aarhus reverberation plus delay,
codec and dropout, with two recognizers at the end arguing about what language
he was speaking.

**And Lucier was sitting in his room.** That is the title. Kay was in another
country, being slowly reprocessed by the acoustics of a lecture hall he had
never stood in, at a symposium he was attending by wire. The 1969 piece is a
man listening to a room he is in. The 2026 accident is a man listening to a room
he is not in, arriving late, on top of himself, in Danish.

**And this is the same family as video feedback and cellular automata**, which
is not a decorative connection — it is the methodology argued for in
[`voicewashing/README.md`](voicewashing/README.md) under "lather, rinse,
repeat," and it appears again in the adventure compiler acting as a linter for
the next iteration. Iterating a system against its own output is how the
character of the system becomes visible.

The other difference is **intent**, and that is exactly the distinction Don
draws about the simulator effect and procedural rhetoric:
these are double-edged tools, they operate whether or not anyone chose them, and
**it is better to be thoughtful and intentional about it.** Lucier chose the
loop. Kay was handed one. The loop did not care.

## Mars, briefly

Kay joked that his voice was "being rerouted to Mars and back." Since 21 seconds
is a number, it can be taken out for a walk.

Light does about 6.3 million km in 21 seconds. So he was getting roughly
**eight round trips to the Moon** — respectable, and nowhere near Mars, which
would have cost him **six minutes** at closest approach and about
**twenty-five** on an average day.

Mars would have been much funnier.

For the same arithmetic taken seriously, see
[`SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md`](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md).

## Why the occasion is not incidental

The venue makes this more than a funny clip.

Nygaard and Dahl built **Simula**. Simula catalyzed **Kay's** early thinking
about objects, which was the subject of the talk he was about to give. Kay's
thinking produced **Smalltalk**, which produced **Self** by way of Ungar and
Smith, which is the direct ancestor of the prototype-and-slots architecture this
repository runs on — see
[`object-system/SELF-AND-MOOLLM.md`](object-system/SELF-AND-MOOLLM.md) and
[`SELF-ISH-INFLUENCES.md`](SELF-ISH-INFLUENCES.md).

So: at the centenary of the man who co-invented objects, minutes before a talk
about how objects were invented, the founder of the next link in that chain met
a feedback loop and used it to praise the person whose mathematics explains
feedback loops. **The lineage and the accident are the same story.** Ole
Lehrmann Madsen — the Aarhus end of the Simula lineage — is in the Zoom
participant strip while it happens.

## The sound check worked

This is the part that makes it an engineering story rather than a blooper.

**The talk itself went off flawlessly.** The loop happened during the setup and
testing block, which exists precisely to shake out problems of this kind; it
found one; Kay diagnosed it correctly on the spot — *"just turn off the audio at
your end on Zoom"* — the fix was applied, and the channel behaved for the
duration of the actual talk.

Which is the whole content of the theorem he was praising, acted out. **Shannon
does not promise a channel without noise.** He proves that a noisy channel still
has a definite capacity, and that with the right arrangement you can transmit
across it reliably anyway. Nobody eliminated the physics here. Somebody broke
the loop, and then the talk got through clean.

So the correct reading of the recording is not that the technology failed. It is
that **the rehearsal did its job**, on camera, on the subject of rehearsals'
favorite failure mode, with the person best qualified in the world to name what
was happening naming it while it happened.

`verified: slide title, portraits and participant names read from the recording;
identify the two portraits explicitly before asserting they are Nygaard and
Dahl.`

## What to take from it

**For transcription work in this repository.** Three kinds of loss, distinguish
them, and only repair the first. Record the other two rather than fixing them
silently — the corrections ledger in
[`voicewashing/TRANSCRIPTS.md`](voicewashing/TRANSCRIPTS.md) is the right shape,
and the Danish case argues for one addition: **log the recognizer's language and
context**, because a prior is part of the provenance of a transcript.

**For the argument about machines and language.** This clip is a better
demonstration than most arguments, and it cuts in an inconvenient direction for
everyone. The recognizer produced *fluent, confident, grammatical Danish* out of
an English sentence — an answer-shaped string, in the sense discussed in
[`../skills/no-ai-parrot/corpus/ARGUMENTS.md`](../skills/no-ai-parrot/corpus/ARGUMENTS.md).
No path, no checking, no iteration; just a prior and a plausible output. It is
the clearest available specimen of the failure mode the critics name, produced
by a system nobody was defending, and it should be conceded cheerfully whenever
that failure mode comes up.

**And the reverse.** The same statistics, pointed the other way and steered by a
human hand, are MacKay's Dasher — the entry in `CANON.md` immediately adjacent
to Shannon's. Prediction measuring a human in 1951; prediction assisting a human
in the 2000s; prediction inventing Danish in 2026 when nobody was steering.
**The difference is never the mechanism. It is whether a person is in the loop,
and which loop.**

## See also

- [`voicewashing/README.md`](voicewashing/README.md) — patina, channel repair,
  and the proofreading boundary
- [`voicewashing/DICTATE.md`](voicewashing/DICTATE.md) — what a cleanup pass may
  and may not touch
- [`SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md`](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md)
  — latency and bandwidth arithmetic
- [`object-system/SELF-AND-MOOLLM.md`](object-system/SELF-AND-MOOLLM.md) — the
  Simula-to-Smalltalk-to-Self line this talk was about
- [`../skills/no-ai-parrot/corpus/CANON.md`](../skills/no-ai-parrot/corpus/CANON.md)
  — Shannon 1951, MacKay's Dasher, Kay on why the mediocre survives
- [`../skills/simulator-effect/`](../skills/simulator-effect/) — priors
  inventing structure, as a design tool rather than a bug
