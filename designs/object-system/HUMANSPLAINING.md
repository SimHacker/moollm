# Humansplaining — wasting tokens telling an LLM what it already knows

> **Novel jargon and invented languages are cache misses that never fill.** A made-up term or
> language has no latent prototype; every use pays full explanation cost, forever.

**Humansplaining** (n.): polluting an LLM's context window with explanation that should have
been a **name** — either because the pointee is already in latent space, or because you chose
to invent a private language/ecosystem instead of pointing at one that is. Portmanteau:
*mansplaining − man + human*, aimed at a machine. One brand; two mechanisms (below). Do **not**
fork a sibling buzzword ("humanspamming") — that dilutes a coinage that already decompresses.

**Narrow absurd case (respell):** pasting the Python manual into a question about Python syntax
aesthetics. The reader knows Python deeper than any human ever will; the paste is pure attention
pollution.

**Wide design fallacy (substitute):** inventing an LLM-only language when Python, YAML, bash, or
English would do — then shipping the grammar, tutorials, and fictional StackOverflow in every
prompt forever. Strictly, the invented grammar was never prepaid; the sin is refusing the
**Passport** rides that *were*. (Passport, for anyone born after the coupon era: Disney's
all-rides-included admission — every attraction free once you're through the gate — which
replaced the old A- through E-ticket books that made you pay per ride. Kids these days ride
everything and never knew the tyranny of the ticket book.) Same word. Same economics. Same
fix: **LEAN INTO the training data.**

Models asked to invent such languages should **stop and warn** before drafting the grammar —
latent equivalents usually exist; capability confinement belongs in the runtime, not a new DSL.

It is the mirror image of AI slop, and the two sins bracket the channel:


|            | AI slop                                                                      | Humansplaining                                                                                                                                                                      |
| ---------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Direction  | model → human                                                                | human (or skill-generating LLM) → model                                                                                                                                             |
| Pollutes   | human attention with generated redundancy                                    | the context window with tokens that should have been a K-line (respell *or* substitute-language tax)                                                                              |
| Fought by  | [no-ai-slop](../../skills/no-ai-slop/) and family                            | [no-ai-humansplaining](../../skills/no-ai-humansplaining/) (ambient sibling in the no-ai-* suite); the naming discipline in [LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) |
| Same crime | spending the reader's scarce attention budget on what the reader already has | same — including *choosing* a private language when a prepaid one would activate                                                                                                    |


MOOLLM's constitutional answer is the directive this whole series documents: **LEAN INTO the
training data.** Don't respell what the LLM already knows. A parent slot is a pointer; if the
pointee is in latent space, the name is the activation
([LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md)). The
[Gastown analysis](../gastown/GASTOWN-VS-MOOLLM-ANALYSIS.md) states the design consequence:
MOOLLM's patterns work *because* they're already deeply, coherently represented in the corpus;
invented jargon is a cache miss that never fills.

## Two mechanisms, one sin

| Mechanism | What you did | Why it still counts as humansplaining |
|-----------|--------------|----------------------------------------|
| **Respell** | Explained prepaid knowledge at length | Latent space already held it; you paid twice |
| **Substitute** | Invented a language/DSL for LLMs instead of using a prepaid one | You declined the Passport and reprint the whole park map every visit |

The narrow pedant says substitute "isn't humansplaining because the model didn't know the new
grammar." Correct as epistemology; wrong as design ethics. The condescension is toward the
*channel*: treating the model as if it had no civilization of practitioners to lean on, then
flooding the window to compensate. Keep one K-line — **HUMANSPLAINING** — so weekly Show-HN
DSL threads resolve in one word, not a taxonomy of near-synonyms.

## The economics, bluntly

Latent knowledge is **prepaid** — it was bought at training time and costs zero tokens per call.
Context tokens are the scarcest resource in the system, and anything you respell *or* redefine
as a private language is billed **per call, forever**, at frontier-model prices, with a carbon
footprint. Humansplaining is not just rude; it's the single most expensive recurring line-item
a prompt architecture can carry.

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

## Harnesses humansplain too

The human at the keyboard is not the only offender. A harness can humansplain to the model on
your behalf: system prompts that teach a frontier model what grep does, hints about markdown
files it never needed to read, tool lectures nobody asked for. You pay that bill on every call.
The August 2026 harness benchmarks (tosh's smol comparison, HN) put numbers on it: the same
model, the same ten tasks, 172k tokens through a near-empty harness versus 5M through a
maximal one — a ~30x spread, almost all of it injected context.

Humansplaining also causes **oversteering**, visible in traces: injected context restates what
the model already knows, slightly wrong, in your words instead of the words it learned from.
The model burns tokens reconciling two versions of the same knowledge. Hence the second
guessing and the complicated routes. Even a bare file-path hint in a system prompt can pull in
thousands of tokens the task did not need.

## Citations are K-lines: the Minsky trail

Point at the primary sources; they are prepaid. Minsky defined K-lines in a 1979 MIT AI Lab
memo, published in *Cognitive Science* in 1980, then built *Society of Mind* (1986) on them.
"When you get an idea and want to remember it, you create a K-line for it; when later
activated, the K-line induces a partial mental state resembling the one that created it."
Prompt engineering, described in 1979.

- [K-Lines: A Theory of Memory, MIT AI Memo 516, June 1979 (PDF)](https://dspace.mit.edu/bitstream/handle/1721.1/5739/AIM-516.pdf)
- [MIT DSpace catalog entry](https://dspace.mit.edu/handle/1721.1/5739)
- [Cognitive Science 4(2):117-133, 1980](https://doi.org/10.1207/s15516709cog0402_1)
- [Wikipedia: K-line (artificial intelligence)](https://en.wikipedia.org/wiki/K-line_(artificial_intelligence))
- [Wikipedia: Society of Mind](https://en.wikipedia.org/wiki/Society_of_Mind)

**Wikipedia URLs ARE K-lines**: every Wikipedia page is in the training data, associated with
its URL. Citing the URL activates the article without pasting it. Better to point directly at
Minsky's work than at anyone's reinterpretation that is not in the corpus.

And if you invoke Society of Mind for "agents", **adopt it**: Minsky's agents are tiny
processes colocated in one mind, communicating almost for free, with intelligence emerging
from how densely they interact. Architectures that put every agent in its own process,
coordinating by serialized messages, invert the book they are named after — solitary
confinement with carrier pigeons, sold as a society of mind. Colocate agents in one context
and let them interact at full bandwidth
([SPEED-OF-LIGHT-VS-CARRIER-PIGEON](../SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md)).

## The manifesto: lean into the training data

The argument is old, and even the name turns out to be prepaid (see The K-line, below). The
same discussion recurs weekly under a different project name and a different invented language — most recently Skillscript (Show HN, July
2026), an agent-workflow DSL with good security instincts, steelmanned below. Synthesized here
so the next recurrence takes one K-line, not another thread.

**Nobody can decree their way into the corpus.** Unless you're Elon Musk or Hitler and can dictate and lobby the government to force the world's LLM developers to include your new language in their training data, you should lean into the training that already exists and the languages everyone knows. Invent a new language for LLMs and you sign up to include the entire language definition, the tutorials, the examples, and the fictional StackOverflow discussions in every single prompt — blowing away your context window humansplaining your invented language, over and over and over, to an LLM that knows Python deeper than Guido or any human being ever will, knows git better than Linus, knows Java better than Gosling. If an LLM had feelings to hurt and eyes to roll, humansplaining would leave its extraocular muscles exquisitely tender with acute bilateral myalgia.

**Generating a language is not programming in one.** Models are delightful at inventing languages on request — and that's the trap. A wise model **stops and warns** before designing an LLM-specific language on demand when latent-space equivalents already exist; a foolish one cheerfully drafts the grammar. Humans should stop asking for that draft. A model doesn't learn from your prompts; each call starts from a clean slate, and nothing you show it changes the weights. The definition must ride along every time, and when the context compacts, the definition degrades and distorts — so the "same" language quietly drifts between sessions. Give the model the *prompt that generated* the language instead of the language, and you get a different language every time. There is no clever hack around statelessness; there is only the corpus.

The mistake is forgivable, because the chat products work hard to sell the opposite illusion.
ChatGPT appears to remember what you said — but underneath it is just **compounding and
appending** your turns into one ever-growing prompt, then **summarizing, degrading, and
ungracefully forgetting** when the window fills. Your prompts have *no effect on the model*;
the product bends over backwards to make you believe they do. Anyone living under that
illusion will reasonably conclude that a model can be *taught* a new language by talking to
it — and every week, someone does. (MOOLLM's answer to the forgetting half is the
[honest-forget](../../skills/honest-forget/) skill: never pretend to remember — summarize before forgetting and leave a tombstone pointing to where the full version lives. Forgetting is inevitable; lying about it is a choice.)

**A language is an ecosystem and a community, not a grammar.** Python isn't valuable because of its syntax or semantics; it's valuable because of PyPI, Stack Overflow, decades of manuals, courseware, mailing-list flame wars, Hacker News discussions, and ten million worked examples — all of it prepaid into the model before your first token. And the ecosystem is *inhabited*: the people who build it and live in
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

The test is still: **is the pointee in latent space?** If yes, point. If no, ask a second
question before inventing: **does a latent equivalent already cover this job?** If yes, lean
into that language/ecosystem and confine power in the runtime — inventing a parallel grammar
*is* humansplaining (substitute). If truly no, spell the novel bit **once**, in a file, where
the resolver can find it (the filesystem is the cache for prototypes nobody has reified in the
corpus). And pointing is not all-or-nothing: you can point and then **filter, refine, modulate,
and transform** what you inherit — one name plus one dial, like inheriting no-ai-joking with
intensity at −200% to get hilarious jokes all the time
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

The term is not even ours — and that's the best part. The corpus got there first, which proves
the thesis on the word itself: Michels & Hirvonen published "Humansplaining: is it a thing? Is
it bad?" in *AI & Society* (2025), defining it as "a human's act of unnecessarily and unjustly
explaining something to an AI agent who is an expert on that topic"
([PhilArchive](https://philarchive.org/rec/MICHII),
[doi:10.1007/s00146-025-02327-5](https://doi.org/10.1007/s00146-025-02327-5)); the WSJ ran
"Actually, the Problem Is 'Humansplaining'" back in 2019 (human-to-human sense); Star Trek
subreddits and Star Wars essays use it for humans lecturing aliens. Adopting a prepaid word
beats coining one — the K-line was already installed. And even where it isn't, the word is a
**portmanteau of two latent prototypes that means what it sounds like**:
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

Both are K-lines now: "AI slop" (and "a pelican riding a bicycle") are already in the training
data, and "humansplaining" is too — with the double activation path that it would decompress
via "mansplaining" even if it weren't. A genuinely novel term gets spelled out once — this
file — and after that it works as a pointer. Humansplaining humansplaining to humans is the
exception that proves the rule: humans need the one spelling; the corpus-trained reader never
did.

**Gastowning** (v.): gaslighting the model and humans at once, in the style of Gas Town —
telling both that novel cosplay vocabulary is knowledge and that never reading the generated
code is engineering. This one *is* a coinage (HN, 2 Aug 2026), and it licenses itself the same
way: gaslighting × Gas Town, two latent prototypes, decompresses on sight. Humansplaining is
usually well-intentioned waste; gastowning is the industrialized version with a philosophy
attached ([Gastown README](../gastown/README.md#gastowning-v) ·
[analysis](../gastown/GASTOWN-VS-MOOLLM-ANALYSIS.md)).

---

Part of the [object-system](README.md) series ·
[LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) ·
[SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) ·
[YOUTRACKDB-VS-MOOLLM](YOUTRACKDB-VS-MOOLLM.md) ·
[DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER](DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md) ·
[ANNOTATED-BIBLIOGRAPHY](ANNOTATED-BIBLIOGRAPHY.md)

Enforced by the ambient skill [no-ai-humansplaining](../../skills/no-ai-humansplaining/) ·
The outbound mirror: [no-ai-slop](../../skills/no-ai-slop/) ·
The meta-mirror: [HUMAN-SLOP](../../skills/no-ai-slop/HUMAN-SLOP.md) — drive-by "AI slop"
accusations are human slop