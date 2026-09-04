# Nenex: the engine that needs our shell

**Source:** [gwern.net/nenex](https://gwern.net/nenex) — *"Nenex: A Neural Personal Wiki Idea"*,
created 2023-09-13, modified 2023-12-31. His own metadata: `status: in progress`,
`confidence: possible`, `importance: 6`.

It is a **proposal**, not a shipped system. That matters, because the two halves are split cleanly:
gwern has specified an engine and explicitly deferred the interface; Don has been building the
interface for thirty-five years and has been hand-rolling the engine. Neither has the other's half.

## What Nenex is

The 2024 LessWrong prescription — *"systems which can think for the user instead"*, and *"you need
to rethink the entire system and rewrite it from the ground up... better to start with a clean sheet
(and an empty cap table)"* — cashed out as an architecture.

**The wiki is not files. It is a log of edits.**

> A more natural approach would be to draw inspiration from DL scaling paradigms in treating
> 'everything as a sequence prediction task': in this LLM-centric wiki paradigm (**Nenex**), the
> wiki would not be file/node-centric but *edit*-centric.

**The model is trained continuously on that log, locally, to imitate you.**
Not retrieval, not a bigger context window — **dynamic evaluation**, the RNN-era trick of running an
SGD step on each input as it arrives:

> as soon as it is used, it is infused into the model's weights, and the more surprising or novel
> the unpredicted text is, the larger the update.

**The paradigm slogan**, which is the line to remember:

> Where Emacs is "everything is a buffer or Lisp function", and vi is "everything is a keystroke",
> for a neural assistant, **"everything is user imitation"**.

The model is an imitation-learning agent (Decision Transformer lineage) with a DAgger correction
loop: when it guesses wrong, your next keystrokes are the correction, and the fix sticks immediately
in the weights rather than scrolling out of a context window. He proposes binding this to a
`should-have-been` function — edit any wrong output into the right one, and that edit is the lesson.

The motivation is stated better than any of us have stated it, under a Phaedrus epigraph about
writing being unable to answer when questioned:

> What I want is to *animate my dead corpus so it can learn & think & write*.

> (Our goal here is not 'superintelligence', but 'superknowledge'.)

## The pieces that land directly on our work

### The log should be S-expressions — which is Winer's outline

> This would work particularly well with a Lisp approach, as Lisp systems like Emacs can easily
> serialize all executed user actions to textual S-expressions, and then call the LLM to generate a
> new S-expression, and interpret *that* to achieve anything that the user could do. [footnote:] One
> could use other text formats like JSON, but there wouldn't be much point, and one risks
> reinventing Lisp badly.

Don, describing Frontier in 2019: *"a scripting language whose syntax (for both code and data) was
an outline. Kind of like Lisp with open/close triangles instead of parens!"*

Gwern arrives at Winer's answer from the opposite direction, thirty years later, for a different
reason. The action log wants to be a homoiconic tree; **YAML jazz is that tree with comments
promoted to semantic data**, which is strictly better for this purpose because the log then carries
the *why* alongside the *what*, and both train. See [`../winer/`](../winer/).

### Constraint propagation over prose

The "Outdated Pages" feature: after any edit, walk the embedding graph outward and ask the model
whether each neighboring passage is now false.

> you have a bunch of pages documenting some software tool and you fire up the editor and write
> 'version 1.0 can now handle JSON' and then all the passages which mention 'JSON' get inspected by
> the model which says 'well obviously this page which says "the tool does not handle JSON" is now
> out of date, let's ask the user for an edit'

> The user can't read the whole site every time he updates something or a week passes... but the
> model can!

This is **Temkin's constraint model applied to meaning instead of layout.** Declare's `[ ]` / `{ }`
constraints keep the interface true when a value changes; Nenex keeps the *corpus* true when a fact
changes. Same dataflow shape, same "declare the relationship and let it re-satisfy," different
substrate — one deterministic, one probabilistic with a human in the approval loop. Worth putting in
front of both of them. See the Temkin study.

### Daemons — we already have the parliament

> **Commentary/critique** [footnote: Maggie Appleton suggests the term 'daemons', although they'd be
> more like a parliament or Greek chorus, perhaps]: prompts can elicit different persona in the
> model to make writing suggestions... A user could package up a set of prompts into a single
> command, like `M-x criticize-paragraph`.

MOOLLM has this built and populated: `adversarial-committee`, `debate`, `evaluator`, the character
and incarnation system, the ambient hygiene skills that run as standing constraints. Gwern's
parliament is a prompt bundle; ours is a cast with rooms, cards, and consent rules.

### Warm-starting is programming by example

> a Nenex's LLM would come pretrained on a public 'demo corpus', a log which ran through
> demonstrations of all standard functionality. Users could contribute back additional
> demonstrations to 'patch' problems.

That is MOOLLM skills — inheritable prototypes you instantiate, taught by example, published as
portable artifacts. A skill *is* a demo-corpus fragment with a card on the front.

### Advisor models

> There is no reason that our local model cannot learn to call, when uncertain, out to a large
> model for assistance... The more you do this, the more you 'distill' the relevant knowledge from
> the advisors into the local model.

Small personal model that knows *you*, calling frontier models that know *everything*, and
distilling down. Clean division of labor, and it maps onto the room/skill dispatch model directly.

### The concrete numbers

Gwern.net at 2023-10-13: ~32.4M Unicode characters of Markdown essays, ~77.4M characters including
the YAML/HTML annotation database. Estimated finetuning cost on the whole thing: ~$160 in 2023
dollars, about $1.10/month amortized over the twelve years it took to write.

That is the entire economic argument for personalization, and it is a rounding error.

## Where it stops — and that is our half

Gwern spends the essay on the engine and gives the interface one sentence, flagged as provisional:

> The suggested text completion is presented to the user through some sort of GUI or TUI interface,
> like grayed-out text or listed in a side pane. (**A side pane for all the LLM 'commentary', akin
> to how streaming websites implement chat in a pane next to or below the streamed video, would be
> the obvious first stab at a GUI.**)

A side pane. A Twitch chat. That is the honest placeholder of someone who knows it is not his
problem.

Everything a Nenex needs at the surface is what this directory has been about for thirty-five years:

| Nenex needs | The webtop has |
|---|---|
| Approve/reject a stream of proposed actions, fast, without leaving flow | Pie menus — the batch-approval gesture is a flick, not a dialog |
| Present a parliament of critics without drowning the page | Windows, tabs, and rooms; each daemon gets a frame, not a sidebar queue |
| Show a proposed edit *in context* before committing | Definition previews and popup-as-window, from [HyperTIES](../hyperties/) forward |
| Navigate a corpus the model has restructured | Semantic zoom, the `link-icon → title → abstract → section` ladder, one rung further to a glyph |
| Make the log inspectable rather than a black box | View records: addressable, diffable, citable ([`VIEW-STATE-ANCESTORS.md`](../../pie-stack-views/VIEW-STATE-ANCESTORS.md)) |
| Let the user *see where it keeps its brain* — his own epigraph | Naked objects, live editing, the HyperLook flip-into-edit-mode move |

He quotes Arthur Weasley — *"Never trust anything that can think for itself if you can't see where it
keeps its brain"* — and then proposes a system whose brain is a continuously mutating local weight
matrix. The only way to honor that epigraph is a **shell that makes the log and the model's
proposals visible, navigable, and reversible.** That is a UI problem, and it is unsolved in the
essay.

## The real divergence: inward vs outward

Not a disagreement, a difference in purpose, and naming it keeps both honest.

**Nenex logs to train.** The log is private, local, and exists so a model can become you. Privacy is
handled by the model never leaving the machine. There is no other reader.

**The webtop logs to share.** A view record exists so *another person* can see what you saw, cite
it, and reply with a counter-view. Attribution, transclusion, and credit are the point.

Same substrate — an append-only log of actions over a corpus — pointed in opposite directions. One
compresses a person into weights; the other publishes attention between people. A system that did
both would let you write with a model that has read everything you ever wrote, and then hand a
colleague not just the essay but the *path you took through it*, with the model's rejected
suggestions still visible as the road not taken.

## Endosymbiosis

The stated ambition: make this good enough that gwern could run his own site on it — by
[engulfment without digestion](../../object-system/ENDOSYMBIOSIS.md). Nenex keeps its membrane: its
own log format, its own local model, its own metabolism. It gains a shell that gives it windows,
pies, rooms, semantic zoom, and a publication surface. Neither organism is rewritten as the other.

What each side actually supplies:

- **From Nenex:** the edit-log substrate, dynamic evaluation, imitation learning, corpus-wide
  consistency sweeps, advisor distillation.
- **From the webtop:** the interaction shell, the approval gestures, the pyramid rendering, the
  view-as-citation model, the publication and provenance layer.
- **From MOOLLM:** the skills-as-demo-corpus, the daemon parliament with consent rules, rooms as
  activation contexts, YAML jazz as the homoiconic log format he says he wants and then declines to
  specify.

## Honest reading

- It is a 2023 proposal at `confidence: possible`, unbuilt as of the document. Do not describe it as
  a system that exists.
- Dynamic evaluation at interactive latency on a personal corpus is the load-bearing bet, and it is
  a real bet. His own performance section is a set of plausible mitigations, not measurements.
- The security argument — a model imitating you won't follow injected instructions because *you*
  wouldn't — is elegant and not obviously sufficient. It deserves adversarial attention, not
  agreement.
- He is right that nobody has built this, and right about why: the paradigm cannot be retrofitted.

↑ [gwern](README.md) · [webtop hub](../README.md) · [what to inherit](../../webtop-gwern-inheritance/GWERN-WHAT-TO-INHERIT.md)
