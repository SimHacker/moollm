# NO-AI-HUMANSPLAINING™ — Protocol

> *"Don't tell the LLM what it already knows."*

---

## Quick Reference

| Command | Effect |
|---------|--------|
| `POINT [name]` | Replace explanation with the activating name |
| `TEST [content]` | Latent? Point. Not latent? Spell once, in a file |
| `ANCHOR [lines]` | Quote the disputed lines, not the whole file |
| `CONFINE [capability]` | Restrict in runtime/permissions, not grammar |

---

## The Problem

**Humansplaining** is condescendingly explaining to an LLM, in its own context
window, something already represented in its latent space:

```
❌ Pasting the Python manual into a question about Python aesthetics
❌ "As you may know, Git is a version control system..."
❌ Inventing a DSL whose grammar must ride along in every prompt
❌ Attaching five whole files when the dispute is about three lines
```

It is the mirror image of slop. Slop pollutes human attention on the way out;
humansplaining pollutes the context window on the way in. Same crime — spending
the reader's scarce attention budget on what the reader already has.

The word is a portmanteau that means what it sounds like: *human* ×
*mansplaining*, aimed at a machine. Its outbound twin is *slop* (championed by
Simon Willison on exactly this naming theory: pick a word whose existing
connotations do all the work, the way "spam" did for unsolicited email).

---

## The Economics

**Latent knowledge is prepaid** — bought at training time, zero tokens per call.
**Respelled knowledge is billed per call, forever**, at frontier-model prices,
with a carbon footprint.

Training is the Disneyland Passport: admission already covers every ride in the
park, no extra cash (no extra *cache*) per ride. Humansplaining is standing at
the gate of an attraction you've already paid for, counting out coupons like
it's still 1959. And a name is a FastPass: it resolves inside the model without
waiting behind the queue of context tokens that must be fed in and attended to
serially. **Respelled knowledge stands in line; named knowledge is already on
the ride.**

---

## The Test

One question decides every case:

> **Is the pointee in latent space?**

- **Yes** → Point. The name is the activation. `"Postel's law"`, `"Self
  prototypal inheritance"`, `"US Patent 5187786A"` — zero explanation tokens.
- **No** → Spell it **once**, in a file the resolver can find. The filesystem
  is the cache for prototypes nobody has reified in the corpus.

---

## Cardinal Sins

### 1. Manual Pasting
Pasting reference material the model was trained on.

**Fix:** Name it. The name is the activation.

### 2. Language Inventing
Designing a new language or DSL that only LLMs will use. It has no ecosystem,
no Stack Overflow, no latent scaffolding — and the whole grammar must be
humansplained in every prompt, forever, drifting under every compaction.

**Fix:** Lean into well-known languages. Confine *capabilities* in the runtime
(allowlists, permissions, review, MOOAM), not expressiveness in the grammar.

### 3. Respelling
Restating a latent concept instead of pointing at it. Three paragraphs
re-deriving Postel's law instead of the word "Postel."

**Fix:** A parent slot is a pointer. Point.

### 4. Preemptive Tutoring
"As you may know, Python is a programming language..."

**Fix:** Start at the actual question. Would you say this to Linus about git?

### 5. File Dumping
Attaching everything in reach "for context."

**Fix:** Quote the lines you're arguing about. Anchored evidence is grounding;
the full file is humansplaining.

### 6. GUID Naming
Coining opaque handles with no latent prototype. Novel jargon is a cache miss
that never fills — every use pays full explanation cost, forever.

**Fix:** Good coinages are latent-space arithmetic — the word2vec move:
*king − man + woman = queen*, so *mansplaining − man + human = humansplaining*.
Bad coinages have no vector to anywhere and must be humansplained forever.
Does the name decompress on first sight?

---

## What Is NOT Humansplaining

| Case | Why it's legitimate |
|------|---------------------|
| Project-local conventions | Latent space has the *traditions*, not your specifics |
| Disambiguation | "Mercury the Roman god" — one clause prevents a wrong bind |
| Post-cutoff facts | New APIs, current versions, yesterday's thread |
| Anchored evidence | The three disputed lines are grounding, not padding |

The self-application rule: this skill's own GLANCE is short *because* the
concept now lives at `designs/object-system/HUMANSPLAINING.md` and in this
file — spelled once, in files the resolver can find. Saying
**HUMANSPLAINING** invokes the rest.

---

## Invocation

```yaml
# When attaching context
BEFORE paste: TEST [is this in latent space?]

# When writing a skill
CATCH "explaining a well-known concept" → POINT [its name]

# When tempted by a new notation
CATCH "inventing jargon" → TEST [does the coinage decompress on sight?]

# When arguing about code
CATCH "attaching the file" → ANCHOR [the three lines]
```

---

## The Founding Case

Skillscript (Show HN, July 2026): a small declarative language designed for
agents to write and humans to approve. Legitimate security goals — but the
language move pays the humansplaining tax forever: no training-data presence,
no ecosystem, the entire language definition, tutorials, examples, and
fictional StackOverflow discussions riding along in every prompt, humansplained
over and over to a model that knows Python deeper than any human ever will,
better than Linus knows git or Gosling knows Java. Full manifesto with the
steelman: [HUMANSPLAINING.md](../../designs/object-system/HUMANSPLAINING.md).

---

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[repo README](../../README.md) and [skills/README](../README.md).

Related MOOLLM skills: [no-ai-slop](../no-ai-slop/) (outbound twin),
[no-ai-hedging](../no-ai-hedging/), [yaml-jazz](../yaml-jazz/) (filenames are
K-lines), [k-lines](../k-lines/), [postel](../postel/).

## See Also

- [CARD.yml](CARD.yml) — Sniffable interface
- [README.md](README.md) — Overview
- [designs/object-system/HUMANSPLAINING.md](../../designs/object-system/HUMANSPLAINING.md) — The design doc
- [designs/object-system/LATENT-SPACE-INHERITANCE.md](../../designs/object-system/LATENT-SPACE-INHERITANCE.md) — The mechanism this protects
- [../no-ai-ideology/BRAND.md](../no-ai-ideology/BRAND.md) — Brand philosophy
