# Humansplaining — wasting tokens telling an LLM what it already knows

> **Novel jargon is a cache miss that never fills.** A made-up term has no latent prototype;
> every use pays full explanation cost, forever.

**Humansplaining** (n.): condescendingly explaining to an LLM, at length, in its own context
window, something already represented in its latent space. The canonical absurd case: pasting
the Python manual and the CPython interpreter source into a prompt asking about Python syntax
aesthetics. The reader knows Python deeper than any human ever will; the paste is pure attention
pollution.

It is the mirror image of AI slop, and the two sins bracket the channel:


|            | AI slop                                                                      | Humansplaining                                                                             |
| ---------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Direction  | model → human                                                                | human (or skill-generating LLM) → model                                                    |
| Pollutes   | human attention with generated redundancy                                    | the context window with tokens already in latent space                                     |
| Fought by  | [no-ai-slop](../../skills/no-ai-slop/) and family                            | [no-ai-humansplaining](../../skills/no-ai-humansplaining/) (ambient sibling in the no-ai-* suite); the naming discipline in [LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) |
| Same crime | spending the reader's scarce attention budget on what the reader already has | same                                                                                       |


MOOLLM's constitutional answer is the directive this whole series documents: **LEAN INTO the
training data.** Don't respell what the LLM already knows. A parent slot is a pointer; if the
pointee is in latent space, the name is the activation
([LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md)). The
[Gastown analysis](../gastown/GASTOWN-VS-MOOLLM-ANALYSIS.md) states the design consequence:
MOOLLM's patterns work *because* they're already deeply, coherently represented in the corpus;
invented jargon is a cache miss that never fills.

## The economics, bluntly

Latent knowledge is **prepaid** — it was bought at training time and costs zero tokens per call.
Context tokens are the scarcest resource in the system, and anything you respell is billed
**per call, forever**, at frontier-model prices, with a carbon footprint. Humansplaining is not
just rude; it's the single most expensive recurring line-item a prompt architecture can carry.

Gen-X-adjacent generations have the metaphor pre-installed: training is the **Disneyland
Passport** — admission already covers every ride in the park, no extra cash (no extra *cache*)
per ride. Humansplaining is standing at the gate of an attraction you've already paid for,
counting out coupons like it's still 1959. (Before the all-inclusive Passport, Disneyland sold
A- through E-ticket books — the E-ticket bought the headliners, which is why "an E-ticket ride"
still means *the good stuff* to anyone who was there.) And latent-space inheritance doesn't
just skip the ticket booth, it's a **FastPass to the front of the line**: a name resolves
inside the model without waiting behind the queue of context tokens that must be fed in and
attended to serially. Respelled knowledge stands in line; named knowledge is already on the
ride.
The GUID observation from [SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) is the same accounting: a
readable name is a K-line, an opaque identifier is a cache miss — and a respelled manual is a
cache miss you *chose*.

## The manifesto: lean into the training data

This argument crystallized long ago; only the sin's *name* is new. It's a recurring discussion
that returns every week wearing a different project name and a different invented language —
the latest occasion being a Show HN in July 2026 for Skillscript, a small declarative language
designed for agents to write and humans to approve, with genuinely good security instincts
(steelmanned below). That discussion is synthesized here, in full, so nobody has to go read a
comment thread — the mountain has come to Mohammed; this document is self-contained — and so
the *next* weekly recurrence can be answered with one K-line instead of another thread.

**Nobody can decree their way into the corpus.** You cannot force the world's LLM developers to
include your new language in their training data — so lean into the training that already
exists and the languages everyone knows. Invent a new language for LLMs and you sign up to
include the entire language definition, the tutorials, the examples, and the fictional
StackOverflow discussions in every single prompt — blowing away your context window
humansplaining your invented language, over and over and over, to an LLM that knows Python
deeper than any human being ever will, better than Linus knows git or Gosling knows Java. If an
LLM had feelings to hurt and eyes to roll, its extraocular muscles would be exquisitely tender
from acute bilateral myalgia.

**Generating a language is not programming in one.** Models are delightful at inventing
languages on request — and that's the trap, because they'll cheerfully play along with a plan
they should warn you about. A model doesn't learn from your prompts; each call starts from a
clean slate, and nothing you show it changes the weights. The definition must ride along every
time, and when the context compacts, the definition distorts — so the "same" language quietly
drifts between sessions. Give the model the *prompt that generated* the language instead of the
language, and you get a different language every time. There is no clever hack around
statelessness; there is only the corpus.

The mistake is forgivable, because the chat products work hard to sell the opposite illusion.
ChatGPT appears to remember what you said — but underneath it is just **compounding and
appending** your turns into one ever-growing prompt, then **summarizing, degrading, and
ungracefully forgetting** when the window fills. Your prompts have *no effect on the model*;
the product bends over backwards to make you believe they do. Anyone living under that
illusion will reasonably conclude that a model can be *taught* a new language by talking to
it — and every week, someone does. (MOOLLM's answer to the forgetting half is the
[honest-forget](../../skills/honest-forget/) skill: never pretend to remember — summarize
before forgetting and leave a tombstone pointing to where the full version lives. Forgetting
is inevitable; lying about it is a choice.)

**A language is an ecosystem and a community, not a grammar.** Python isn't valuable because of
its syntax; it's valuable because of PyPI, Stack Overflow, decades of manuals, courseware,
mailing-list flame wars, and ten million worked examples — all of it prepaid into the model
before your first token. And the ecosystem is *inhabited*: the people who build it and live in
it are in the corpus too. Guido and the BDFL debates, the PEP authors, the core devs, the Stack
Overflow regulars with their idioms and norms and running arguments about what's Pythonic —
characters, not just rooms. When a model writes Python it isn't consulting a grammar; it's
channeling a civilization of practitioners, and that community voice is the scaffolding that
keeps generation on the rails. A language that exists only in one repo is a ghost town in both
senses: no modules *and* nobody home — no one ever asked a question in it, answered one, argued
a style war, or wrote the library you need. Generated code in a well-known language is also
simply *better engineering*: reviewable by anyone, improvable, deterministic, and free to run —
no tokens spent nondeterministically interpreting it on every execution.

**Greenspun's Tenth Rule comes for every hamstrung language.** PHP was a decent templating
language, and none of its flaws had to do with templating. But the industry decided designers
couldn't be trusted with foreach loops, invented deliberately weakened template languages like
Smarty inside it — and then the designers needed variables, macros, conditionals, and functions
anyway, so those were hacked back in with quirky syntax nothing like the host language.
Greenspun's Tenth Rule on steroids, a swarm of locusts sent to smite the sinners: any
sufficiently complicated agent DSL will grow an ad hoc, informally-specified, bug-ridden, slow
implementation of half of Python. Constraining the grammar doesn't remove the need for power;
it just guarantees the power comes back ugly.

**Design for humans; the training data follows.** This is not an argument against new
programming languages — the world should keep making those, for *people*. If a language is good
enough to catch on, it gets written in, asked about, taught, flamed about on Hacker News, and
eventually lands in the corpus, where every future model knows it for free. That is the one
road into latent space, and a language designed only for LLMs structurally cannot take it: it
is condemned to be humansplained in every prompt, forever — a recurring bill in money,
electricity, and carbon that no other design decision can claw back.

**The steelman, honestly.** Skillscript's real goals — default-deny allowlists,
connector-mediated credentials, an effect surface a non-programmer can approve, deterministic
replay — are good goals, and the builder deserves credit for taking agent safety seriously. The
disagreement is about *where the constraint lives*: **capability confinement belongs in the
runtime, not the grammar**. MOOLLM's split: the languages stay latent (Python, bash, YAML,
English — maximally represented, zero respelling), while permissions live in a policy layer
([MOOAM](../MOOAM.md), reviewed diffs, git as the audit log). Confine what code *may touch*,
not what the model *may say*. You get the approval surface without paying the per-prompt
language tax.

And the safety layer you already have is better than any grammar: the git repo, GitHub, and
the PR code-review workflow are a **trampoline net** under everyone who jumps — catching your
mistakes, your contributors' mistakes, and the LLM's, whether the failure is malicious intent,
stupid unintentional error, hallucination, a brain fart, or the cat walking across the
keyboard. Every change is a diff someone can read, a commit someone can revert, a branch that
never touched main, a review that caught it at the boundary. A constrained language tries to
make mistakes *inexpressible* and fails (Greenspun, above); the net makes them *survivable and
reversible*, which is the property you actually need — and it works identically for human and
machine authors, because the net doesn't care who was bouncing.

## What is NOT humansplaining

The test is always the same: **is the pointee in latent space?** If yes, point. If no, spell it
— once, in a file, where the resolver can find it (the filesystem is the cache for prototypes
nobody has reified in the corpus). And pointing is not all-or-nothing: you can point and then
**filter, refine, modulate, and transform** what you inherit — one name plus one dial, like
inheriting no-ai-joking with intensity at −200% to get hilarious jokes all the time
([LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) works the knobs). Legitimate
spelling-out:

- **Project-local conventions** — your CARD.yml layout rule, your naming scheme. Latent space
has the *traditions* these descend from, not your specifics.
- **Disambiguation** — "Mercury the Roman god" costs one clause and prevents a wrong-parent bind.
- **Post-cutoff and fast-moving facts** — new APIs, current versions, yesterday's HN thread.
(The `youtrackdb-driver` sketch in [YOUTRACKDB-VS-MOOLLM](YOUTRACKDB-VS-MOOLLM.md) puts the
docs URL in the parents alongside the name for exactly this reason.)
- **Anchored evidence** — quoting the three lines of source you're arguing about is grounding,
not humansplaining. Quoting the file is.

## The K-line

Say **HUMANSPLAINING** to invoke all of this: the sin, the economics, the Skillscript case, the
test. One word; the rest is in latent space now — or will be, once this file has done its work.

Yes, the term is itself a coinage — but it's not a cache miss, and the difference is the whole
lesson. It's a **portmanteau of two latent prototypes that means what it sounds like**:
*human* × *mansplaining* (Solnit's essay, a decade of usage, the full semantics of condescending redundant explanation prepaid), aimed at a machine. The word decompresses on first sight with zero explanation tokens. That's the naming discipline applied to naming itself: good coinages are latent-space
arithmetic — literally the word2vec move. Just as *king − man + woman = queen*, so
*mansplaining − man + human = humansplaining*. The embedding geometry that made Mikolov's
party trick work is the same geometry that makes the coinage decompress: the vector from
*man* to *human* carries the meaning across, no explanation required. Bad coinages are opaque
handles with no vector to anywhere — they must be humansplained forever.

It's also the natural sibling of **slop** — the one-syllable name for unwanted AI output that
Simon Willison championed into common usage on exactly this argument: pick a word whose
existing connotations do all the work, the way "spam" did for unsolicited email. *Slop* names
the pollution flowing model→human; *humansplaining* names the pollution flowing human→model.
Two self-decompressing words, one for each direction of the channel.

---

Part of the [object-system](README.md) series ·
[LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) ·
[SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) ·
[YOUTRACKDB-VS-MOOLLM](YOUTRACKDB-VS-MOOLLM.md) ·
[ANNOTATED-BIBLIOGRAPHY](ANNOTATED-BIBLIOGRAPHY.md)