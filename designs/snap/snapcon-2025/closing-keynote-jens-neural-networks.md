# Snap!Con 2025 — Jens's Closing Keynote: Neural Networks in Snap! Itself

**Video:** [YouTube — U9W04TEMBUk](https://www.youtube.com/watch?v=U9W04TEMBUk) ·
Heidelberg, closing keynote, billed as *"What's new in Snap! 11 — Data — Extensions — Neural
Networks."*

Jens's own description: *"introducing deep machine learning capabilities to Snap as an alternative
way to create custom predicate blocks."* A predicate block. That is the frame: a neural net is a
thing that answers yes or no, so it belongs in the palette next to `is _ > _ ?`.

Companion: [karlstrom-intro-jens.md](karlstrom-intro-jens.md) (the same conference, the evening
before) · [../../revolutionary-chess/BRINGING-IT-HOME.md](../../revolutionary-chess/BRINGING-IT-HOME.md)
(what this talk is the existence proof for)

Every quote below is timestamped to the video. Lightly edited for clarity where speech repeats
itself; nothing is paraphrased inside quotation marks.

---

## What he built on stage

The perceptron is a **sprite**, named after Frank Rosenblatt. It responds to broadcasts — `setup`,
`predict`, `learn`. Forward feeding and backpropagation are two visible pipes of blocks. You add a
hidden layer by **duplicating the sprite**. Then he trains it live on microphone samples of his own
harmonica and his own recorder, and it tells them apart.

Implemented in Snap! itself, on Snap! 11's new prototypal object system. No JavaScript block doing
the real work offstage.

> These neural networks are all implemented in Snap! itself. There is no secret JavaScript block in
> there. It's all implemented using this new object-oriented system that we have in there, where we
> just have prototypical inheritance with actual objects with a new request block.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=3757s>

Live-built projects from the talk: Backpropagation ANN Sprite Layers · Instruments Recognition ·
Gesture Recognition (published under Jens's Snap! account).

## It is philosophy, not technology

> This is not about ones and zeros. This is not about how a processor works. This is not about how
> technology works. This has nothing to do with technology. This is all about philosophy. This is
> all about how we humans think about things.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=554s>

> The cool thing about Snap! that we've told you all along, and that's been a theme of this
> conference, is that if it takes one number, it takes one number in any dimension, or it takes any
> dimension of numbers.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=319s> — hyperblocks, which is why the matrix algebra
never has to be introduced as matrix algebra.

## The size of the thing

> This thing here is the current Nobel Prize of Physics. And I've seen more complicated code than
> that.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=2097s>

> This is a perceptron and this is a layer in a neural network. You've all written more complicated
> stuff than this, and the kids in your classes have written more complicated projects than this.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=1234s>

Asked from the floor whether the script on screen really was the whole perceptron:

> "Is that all there is to a perceptron?" — "Yes." — "So there's not any hidden magic?" — "Nope.
> This is why we wanted to have it out in the open. There's no — this is it."

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=4672s>

> It took us 18 months to break it down to just this. This is all there is.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=4731s> — the price of the return trip, paid in human
months, which is the whole reason nobody does it by accident.

## What teaching this is for

> If you're teaching merge sort and you think you're teaching algorithms, that's fine for teaching
> an algorithm, but you're not doing your job.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=4518s>

> Honestly, I think if you're not teaching backpropagation in college, you're killing computer
> science. This is the most relevant algorithm around.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=4502s>

> This thing is eating up our lunch. We want to teach algorithms. This might be the last algorithm
> we get to teach. We better teach it well.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=3739s>

> I would expect that just using these neural nets to be something that you could probably do in
> high school.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=4490s>

## Your own data, and one algorithm across domains

> It'd be way cooler if we could use our own data. So let me use my own data.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=2460s> — then the harmonica and the recorder.

> It's the same neural network, the same algorithm, that can distinguish one instrument from
> another, one drawing from another, a sea mine from a rock. It's the same thing, folks.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=3723s>

> To us it was more like a sensory experience. I duplicate the sprite to make another layer, rather
> than I increment an integer in an input field.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=5063s> — the architecture is manipulated as objects,
so adding depth is a gesture and not a hyperparameter.

And the hardware keeps arriving: Snap! 11 talks to Arduinos (Jan's Snap4Arduino port, the "S4A
bridge") and speaks websockets (Bernat).

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=3800s>

## No hype, and two hard limits stated out loud

> If any company, if any mogul is telling you that they're working on explainable AI, they are lying
> to you. They're working on some chatbot that is going to come up with some gibberish that is going
> to be an explanation, but it's not going to be what's actually going on. There is no way to explain
> what's going on as soon as you have one hidden layer.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=2272s>

> Think about 80%. This is a decision, friend or foe. Are you going to kill somebody with an 80%
> chance? Probably not. Are you going to take life and death decisions on an 80% chance? Probably
> not.

<https://www.youtube.com/watch?v=U9W04TEMBUk&t=1897s>

The sea-mine-from-a-rock example and the friend-or-foe example are the same algorithm, said in the
same talk, on purpose. Teaching the thing includes teaching what it costs to believe it.

## Why this belongs in MOOLLM's design notes

| Beat | Where it lands |
|---|---|
| Frontier algorithm compressed until a child can hold it, 18 months of human work | [BRINGING-IT-HOME.md](../../revolutionary-chess/BRINGING-IT-HOME.md) — the return trip, and why it is the half that never paid |
| A net as a society of sprites answering broadcasts; depth by duplication | Kay's "design the organisation of the parts, not a better part" — [masters/alan-kay.md](../../../skills/design-sense/masters/alan-kay.md) |
| Understanding arrives by use, as a sensory experience | [skills/constructionism](../../../skills/constructionism/) |
| "No secret JavaScript block" | [low-floor-no-ceiling](../../../skills/design-sense/methods/low-floor-no-ceiling.md); the ceiling is real only if the floor's material is the same material |
| "There is no way to explain what's going on as soon as you have one hidden layer" | Why MOOLLM keeps deliberation in inspectable artifacts on disk instead of asking a model to narrate itself |

↑ [Snap! index](../README.md) · [Jens's Karlstrom intro](karlstrom-intro-jens.md) ·
[Brian's Karlstrom address](karlstrom-address-brian.md)
