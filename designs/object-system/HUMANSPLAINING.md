# Humansplaining — wasting tokens telling an LLM what it already knows

**Humansplaining** (n.): condescendingly explaining to an LLM, at length, in its own context
window, something already represented in its latent space. The canonical absurd case: pasting
the Python manual and the CPython interpreter source into a prompt asking about Python syntax
aesthetics. The reader knows Python deeper than any human ever will; the paste is pure attention
pollution.

It is the mirror image of AI slop, and the two sins bracket the channel:

| | AI slop | Humansplaining |
|---|---|---|
| Direction | model → human | human (or skill-generating LLM) → model |
| Pollutes | human attention with generated redundancy | the context window with tokens already in latent space |
| Fought by | [no-ai-slop](../../skills/no-ai-slop/) and family | this doc; the naming discipline in [LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) |
| Same crime | spending the reader's scarce attention budget on what the reader already has | same |

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
The GUID observation from [SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) is the same accounting: a
readable name is a K-line, an opaque identifier is a cache miss — and a respelled manual is a
cache miss you *chose*.

## Case study: inventing languages for LLMs (Skillscript, HN, July 2026)

[Show HN: Skillscript](https://github.com/sshwarts/skillscript) — a small declarative language
designed for agents to write and humans to approve. The security goals are legitimate (see
below). But the language-design move triggers the humansplaining tax, and the HN thread
captured the argument in the wild:

> "Unless you're Hitler and can force all LLM developers to include your new language in their
> training data, it's always much better to lean into the existing training and well known
> languages. … Inventing a new language means now you have to include the entire language
> definition, tutorials, examples, and fictional StackOverflow discussions in every prompt,
> blowing away your context window with mansplaining your invented language over and over and
> over again to an LLM who knows Python deeper than any human being ever will, better than
> Linus knows git, or Gosling knows Java." — Don Hopkins, in the thread

(The coinage sharpened afterward: not mansplaining — **humansplaining**.)

The supporting points from the same thread, kept because they generalize:

- **No ecosystem.** A language that exists only in your repo has no PyPI, no Stack Overflow, no
  ten thousand worked examples — none of the latent scaffolding that makes LLM codegen reliable.
- **Models don't learn from your prompts.** Each call starts cold. The language definition must
  ride along every time, and when the context compacts, the definition distorts — so the "same"
  language drifts between sessions. You can't wish your way out of statelessness.
- **Greenspun's Tenth Rule, LLM edition.** The PHP/Smarty parable: hamstring a capable language
  to protect users from power, then watch the users hack the power back in as an ad hoc,
  informally-specified, bug-ridden dialect. Any sufficiently complicated agent DSL contains a
  slow implementation of half of Python.
- **Design for humans; the training data follows.** New languages for *people* are fine — if
  they're good, they get written about, discussed, taught, and eventually land in the corpus.
  A language designed *only for LLMs* can never take that path; it is structurally condemned to
  be humansplained forever.

**The steelman, honestly.** Skillscript's real goals — default-deny allowlists,
connector-mediated credentials, an effect surface a non-programmer can approve, deterministic
replay — are good goals. The critique is not "sandboxing is bad"; it's that **capability
confinement belongs in the runtime, not the grammar**. MOOLLM's split: the languages stay
latent (Python, bash, YAML, English — maximally represented, zero respelling), while permissions
live in a policy layer ([MOOAM](../MOOAM.md), reviewed diffs, git as the audit log). Confine
what code *may touch*, not what the model *may say*. You get the approval surface without
paying the per-prompt language tax.

## What is NOT humansplaining

The test is always the same: **is the pointee in latent space?** If yes, point. If no, spell it
— once, in a file, where the resolver can find it (the filesystem is the cache for prototypes
nobody has reified in the corpus). Legitimate spelling-out:

- **Project-local conventions** — your CARD.yml layout rule, your naming scheme. Latent space
  has the *traditions* these descend from, not your specifics.
- **Disambiguation** — "Mercury the Roman god" costs one clause and prevents a wrong-parent bind.
- **Post-cutoff and fast-moving facts** — new APIs, current versions, yesterday's HN thread.
  (YouTrackDB's own docs URL belongs in a driver skill's parents *before* the name, for exactly
  this reason — [YOUTRACKDB-VS-MOOLLM §10](YOUTRACKDB-VS-MOOLLM.md).)
- **Anchored evidence** — quoting the three lines of source you're arguing about is grounding,
  not humansplaining. Quoting the file is.

## The K-line

Say **HUMANSPLAINING** to invoke all of this: the sin, the economics, the Skillscript case, the
test. One word; the rest is in latent space now — or will be, once this file has done its work.

---

Part of the [object-system](README.md) series ·
[LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) ·
[SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) ·
[YOUTRACKDB-VS-MOOLLM](YOUTRACKDB-VS-MOOLLM.md) ·
[ANNOTATED-BIBLIOGRAPHY](ANNOTATED-BIBLIOGRAPHY.md)
