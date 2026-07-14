# Latent-Space Inheritance — multiple inheritance from named concepts in training data

**The claim:** in MOOLLM, an object's `parents:` list can mix **concrete files** and **names of
things the LLM already knows**. The mechanism does not distinguish. A path resolves by file
lookup; a name resolves by the LLM recognizing it. **The whole of the model's training is the
prototype store; the name is the activation; no essay needed.**

This is the discovery we've been dogfooding since cauldron, promoted from
[cauldron META-PLAN §1](../../skills/cauldron/META-PLAN.md) per the
[Opus review](../../skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.md), which called it "the
most novel thing in cauldron's docs and the thing least specific to cauldron… generalizes
MOOLLM's inheritance model to use the LLM as a universal resolver."

Siblings: [SELF-AND-MOOLLM.md](SELF-AND-MOOLLM.md) (the delegation mechanism) ·
[YOUTRACKDB-VS-MOOLLM.md](YOUTRACKDB-VS-MOOLLM.md) (contrast with engine-enforced classes) ·
[README.md](README.md).

## The canonical example

From the cauldron META-PLAN — one ordered parent list, three kinds of entries, one mechanism:

```yaml
parents:
  - ../../skills/cauldron                  # concrete path — follow the file
  - ../../skills/object                    # concrete path — follow the file
  - "Self prototypal inheritance model"    # latent-space K-line — LLM fills it in
  - "javascript"                           # latent-space K-line — LLM already knows
  - "The Weird Sisters from Macbeth"       # latent-space K-line — patron-as-prototype
  - "a taco — crisp shell, warm filling, salsa, fold in half"  # natural-language prototype
```

First-match-wins sweeps left to right. Formal discipline first, aesthetic influences after.
An ephemeral brew can declare `parents: ["the spirit of a PR-sized cauldron"]` and that's
enough — the one-line K-line activates every cauldron-adjacent pattern the model has.

## Why this works: K-lines are the linker

Minsky's K-lines ([skills/k-lines/](../../skills/k-lines/)) are strings you pull to reactivate a
constellation of knowledge. Saying **"Marvin Minsky"** instead of paraphrasing Minsky brings in
more, more accurately, at near-zero token cost. Latent-space inheritance is K-lines given the
**structural position of a parent slot**: not just "think about X" but "X is upstream of this
object — resolve missing slots through it."

So the inheritance system has two stores with one lookup rule:

| Store | Pointer | Resolver | Cost |
|-------|---------|----------|------|
| Filesystem | relative path | open the file | one read |
| Latent space | a name | the LLM's recognition | ~zero tokens |
| Latent space | a natural-language sketch | the LLM's interpretation | one line |

The filesystem is **the cache for prototypes we've bothered to reify**. Everything else stays in
latent space until there's a reason to write it down. Ungar's simplicity test passes: one
mechanism, an ordered parent list; no separate machinery for "formal" vs "inspirational" parents.

**Don't respell what the LLM already knows.** A parent slot is a pointer. If the pointee is in
the filesystem, follow it. If it's in latent space — also a pointer. The name is the activation.

## Multiple inheritance of abstract concepts

Class systems agonize over multiple inheritance (diamonds, MRO, mixin ordering). Latent-space
parents make multiple inheritance **the normal case and nearly free**, because the "conflict
resolution" is the LLM doing what it always does: blending constraints in context, with the
ordered list as priority.

Field-proven patterns, all currently in production in this repo:

- **Patron-as-prototype.** Cauldron inherits from "The Weird Sisters from Macbeth" — not
  decoration; it sets Phase-1 chaos-becoming-useful expectations that shape actual behavior
  ([cauldron CARD](../../skills/cauldron/CARD.yml)).
- **Character incarnation.** The bartender in adventure-4 declares `PRIMARY INHERITANCES
  (k-lines): Quark (DS9), James (Bar Karma), Guinan, Sam Malone` — a personality assembled by
  naming four traditions
  ([the-bartender/CHARACTER.yml](../../examples/adventure-4/characters/fictional/the-bartender/CHARACTER.yml)).
- **Real people, safely.** Pets and familiars inherit a named person's *expertise* by reference
  ("wrapping a raw pointer in a safe handle") without impersonating them — the ethics live in
  [incarnation](../../skills/incarnation/) and hero-story gating; see
  [SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS](../ethics/SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS.md):
  "K-lines as activation vectors that channel traditions rather than simulating persons."
- **Tool metaphors.** Factorio for dataflow, Fluxx for rule mutation, Mario World cannons for
  flick navigation — chosen precisely because they are *massively represented in training data*
  ([GASTOWN-VS-MOOLLM-ANALYSIS](../gastown/GASTOWN-VS-MOOLLM-ANALYSIS.md): "we lean into
  knowledge already well-represented in the LLM's training data"; its inverse is the Gas Town
  failure mode — invented jargon like "bead" and "polecat" with no training-data support).
- **Double inheritance through one name.** "Bester" in
  [PSYCHOPOMP-AND-THE-BIFROST](../sim-obliterator/PSYCHOPOMP-AND-THE-BIFROST.md) inherits both
  Alfred Bester the author and the B5 character named after him — one token, two lineages, and
  the LLM holds both.

## Inheriting whole systems by name

The parent list isn't limited to characters and aesthetics. It resolves **languages, object
systems, protocols, interfaces, APIs, function signatures, calling conventions** — anything with
deep training-data presence. Say "Smalltalk-80" and you inherit message sends and metaclasses.
Say "NeWS TNT" and you inherit dict-stack delegation with ordered `/Parents` multiple
inheritance. Say **"US Patent 5187786A"** and you inherit Densmore and Rosenthal's
filesystem-as-class-hierarchy, `SEND` via shell and all. The reflective tower bootstraps by
*describing itself in terms the LLM already knows* — we aren't inventing these capabilities and
defining them from scratch; we're addressing them where they already live.

This is what makes the Self core a practical machine language for other object systems: hybrids,
adaptors, bridges, emulators, and CLI/programmatic drivers get built by pointing at the target
system's name rather than reimplementing it. Worked through concretely against a real database in
[YOUTRACKDB-VS-MOOLLM.md §10](YOUTRACKDB-VS-MOOLLM.md#10-inheriting-from-youtrackdb--the-machine-language-move).

## The naming discipline this imposes

If names are pointers into latent space, then **naming is API design**:

1. **Prefer names with deep, multifaceted training-data coherence.** "Filesystem", "YAML",
   "Smalltalk inheritance", "Sims advertisements" — each name drags in a whole correct behavior
   model. (From the Gastown analysis: MOOLLM's patterns work *because* they're in training data
   deeply and coherently.)
2. **Novel jargon is a cache miss that never fills.** A made-up term has no latent prototype;
   every use pays full explanation cost, forever.
3. **Filenames are K-lines.** The directory listing is the advertisement index (yaml-jazz);
   a well-named file is a pullable string.
4. **Sketches work when no name exists.** "A taco — crisp shell, warm filling, fold in half" is
   a valid prototype. The LLM interprets loose-but-sufficient specifications (Postel: accept
   liberally).

## Failure modes, honestly

- **Drift.** Latent prototypes vary across models and versions; "javascript" resolves slightly
  differently in every model generation. Mitigation: reify into the filesystem cache when the
  resolution starts to matter (that's what LIFT is for — play, learn, lift).
- **Hallucinated slots.** The LLM may confabulate detail the named concept doesn't pin down.
  Mitigation: ordered parents put concrete files first; grep-anchored claims (cauldron ANCHOR);
  no-ai-slop's claim ledger.
- **Ambiguous names.** "Mercury" is a planet, element, god, and record label. Mitigation: qualify
  the K-line ("Mercury the Roman messenger god") — one clause, still cheaper than an essay.
- **Not portable to non-LLM readers.** A human can follow a path; a name asks the human to know
  the reference too. That's a feature in practice (the docs read like culture, not boilerplate)
  but it's a real cost for outsiders.

## Why this is the load-bearing concept

Every distinctive MOOLLM behavior reduces to this move:

- **Skills** are prototypes whose most important parents are latent ("Postel's law", "Jon Postel"
  himself, "RFC 761").
- **Characters** are constellations of named traditions, not simulations of people.
- **Rooms** inherit genre physics by naming it ("a cozy pub", "a NOC war room").
- **The cheapest correct behavior is a name away.** MOOLLM's efficiency isn't compression; it's
  addressing — pointing at knowledge instead of restating it.

Class-based systems (see [YOUTRACKDB-VS-MOOLLM](YOUTRACKDB-VS-MOOLLM.md)) must declare every
parent inside the schema before use, and the engine can only resolve declared subsumption.
MOOLLM's resolver already contains most of human culture, indexed by name. Inheritance from
"things well known in the training data, by name" is the feature no database engine can copy —
and we've been thriving on it, not as a theory but as the daily working method of every skill,
character, and brew in this repo.
