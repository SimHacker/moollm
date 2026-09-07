# CLICHES — harvested instances, verbatim and attributed

What was actually said, by whom, when, with a link. Character-exact, including
typos and emphasis markers. Nothing here is cleaned up, and nothing here is
paraphrased.

Harvest rules in [`../SKILL.md`](../SKILL.md). Two standing prohibitions:
**nothing about anyone's health or private life goes in this file**, and
**no entry without a permalink** — an unattributable quote is a rumor.

---

## hypfer — Hacker News

Three instances in twenty-six days, in three unrelated threads: a paper about
reasoning traces, a news story about a misbehaving agent, and a thread about
organizing markdown files. The dates and the subjects are the only commentary
needed.

Found by `ENLIST-THE-RECORD` against the HN Algolia API on 2026-09-07. All text
below is character-exact from the API response.

### 2026-08-12 · on a news story about an agent booking a gym class

Thread: *AI agent hacks gym to get its user a spot in pilates class* (BBC) —
https://news.ycombinator.com/item?id=49268697

https://news.ycombinator.com/item?id=49269255

> No, it starts much earlier. They should not have given a next token predictor
> unsupervised Internet access, regardless of what the marketing might have told
> them about its capabilities or alignment. Don't use technology you do not
> understand in ways that might bring harm to others.
>
> Exercise appropriate caution. I don't think the guy itself is fully to blame
> though. Our whole culture has rotted quite significantly.

`kind: cliche · form: general-purpose verdict, applied to a consumer-product
story · verified: verbatim via HN Algolia API, fetched 2026-09-07`

**This instance is why the phrase is a cliché rather than an argument.** The
same four words carry a metaphysical verdict on 21 August, a product-safety
judgment on 12 August, and a workflow judgment on 7 September, across three
unrelated subjects, without changing.

### 2026-08-20 · on a paper about reasoning traces

Thread: *Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking
Traces* — https://news.ycombinator.com/item?id=49360140

https://news.ycombinator.com/item?id=49384104

> Cyberpsychosis. A next token predictor is not a being.
>
> Stop posting these things. Stop thinking these things.

`kind: cliche · form: verdict plus prohibition · verified: verbatim via HN
Algolia API, fetched 2026-08-21`

Note the structure, which is the strong form: a metaphysical verdict, then a
ban on the inquiry. The ban is the part with a literature (see
[`CANON.md`](CANON.md), Lifton and Turing).

### 2026-08-21 · on the venue

https://news.ycombinator.com/item?id=49386217

> As I said, context.
>
> In the right space with real people, worthy of a debate. On HN? No. Not like
> this. Not here. Not without filtering the participants for real human beings.

`kind: cliche · form: door policy · verified: verbatim via HN Algolia API`

The requested door policy is a procedure for deciding, from text, whether a
genuine mind produced it. Turing published that procedure in 1950. Quote them,
then quote Turing, and let the reader put the two next to each other.

### 2026-08-21 · the exit

https://news.ycombinator.com/item?id=49386790

> I think you might be operating in the mindset of a high-trust internet that no
> longer exists. You do not engage with sea lions, concern trolls, grifters,
> marketing people and the like. You shut them down.
>
> inb4 "who are you to decide that?" - "Me. I am me."
>
> That said, I appreciate what you did for computing at large, but you're missing
> the point here. This is (unfortunately) not a good faith debate club. The
> Internet as we know and love it is dead.

`kind: cliche · form: dead-internet fatalism, plus an unexamined claim of
privileged being-ness · verified: verbatim via HN Algolia API`

"Me. I am me." is offered without a test, in a thread that demanded tests of
everyone else. It is quotable directly beside the door-policy passage above.

### 2026-09-07 · on delegating judgment, in a thread about markdown files

Thread: *Ask HN: How do you manage skills files?*, posted by imadtaieber.

Thread: *Ask HN: How do you manage skills files?* —
https://news.ycombinator.com/item?id=49589914

https://news.ycombinator.com/item?id=49594743

Replying to ygjb (https://news.ycombinator.com/item?id=49594458).

> You're putting a lot of trust into the judgement abilities of what is just a
> next token predictor there.
>
> I can see what the goals are there, and they do make sense I suppose, but I'm
> not confident that what you're handing off there can be handed off to that
> degree.
>
> But maybe that is not the point and the point instead is to see what the LLM
> thinks would be correct, and then think about that and collect learnings about
> the world from it. It might not be right, but it still tells you how normal
> people think. So that's useful.
>
> Just a very roundabout way to achieve that, but that's fine, I guess.

`kind: cliche · form: workflow claim, with a concession in paragraph three ·
verified: verbatim via HN Algolia API, fetched 2026-09-07, 06:44:37Z`

**Harvest the third paragraph.** It walks from *cannot be trusted* to *that's
useful* without prompting. Their own concession, quoted, does more work than a
rebuttal, and it means the conceding has already been done for you.

### 2026-09-07 · the good question, same account, same thread

https://news.ycombinator.com/item?id=49594705

> My genuine question is:
>
> Are there any "skills" at all that have proven to be useful? And if so, what's
> the context?
>
> Because, for me anyway, LLMs usually do one thing, and that then produces a
> durable artifact. So the prompt that got me there by that point expired and is
> not really needed anymore.

> For the "add this endpoint" example you've described, I just throw commit IDs
> at the clanker and say "go do that again". That works, and doesn't decouple
> knowledge from code.

`kind: NOT a cliche — filed here to keep the account's material together ·
form: answerable question, correctly reasoned · verified: verbatim via HN
Algolia API, 06:38:34Z — six minutes BEFORE the cliché comment`

**This is the one worth answering.** "The prompt that got me there expired" is
accurate and is a design principle rather than an objection to one. Throwing
commit IDs at it is a reusable procedure stored in `git log`, keyed by a hash
only its author can find. Their own two paragraphs contain the whole argument
for writing procedures down; no counter-argument is required.

---

## Filing note

The clichés get harvested because they sting; the good answers get lost because
the moment passes. See [`CORRECTIONS.md`](CORRECTIONS.md), which is the more
useful half of this corpus and the half that takes discipline to keep.
