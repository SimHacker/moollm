# K-Lines Restore States of Mind, Not Topics

## Henry's correction

The diluted textbook reading of a k-line:

```
ETHICS → retrieve documents about ethics
```

What Marvin actually meant, per Henry Minsky: a k-line reactivates **the entire
state of mind you had — what you were thinking — when you coined it**.

```
ETHICS → reinstate the constellation of agencies, goals, frames,
         expectations, relationships, active questions, and modes
         of thought associated with that activation
```

Not a symbol. **A checkpoint for a mode of mind.** Closer to a
content-addressed continuation than a keyword. It does not contain a complete
copy of the former mental state; it records enough activation connections to
fall back into approximately the same cognitive configuration.

That is the difference between **remembering a transcript** and **resuming a
mind**.

## MOOLLM's current implementation, honestly placed

[nellm.md](../nellm.md) makes k-lines explicit activation requests resolved
against a preloaded graph — `dictionary["ETHICS"]`, O(1), grep-simple, no
embeddings, because the transformer already did the semantic search when it
emitted the token. That is correct and cheap, and it is the **symbolic and
contextual layer** of a larger reinstatement mechanism, not the whole thing.

## The state-of-mind capsule

What a practical capsule preserves:

- active goals and priorities
- salient objects, people, concepts, relationships
- active agencies and inhibited alternatives
- current hypotheses and confidence
- schema predictions awaiting results
- unresolved contradictions and questions
- working-set files and memory references
- current strategy and intended next action
- urgency/novelty/threat signals
- provenance: why this state was considered useful

Layered, not a verbose status report:

| Layer | Contents |
|-------|----------|
| Symbolic | names, goals, active schemas, world bindings, constraints, working-set refs |
| Episodic | minimal trace of how the state arose |
| Procedural | reconstruction, refresh, validation, resumption instructions |
| Context | which GLANCE/CARD/SKILL/objects to page in |
| Latent (experimental) | reusable prefix/KV state, control vectors, recurrent state |

## Reinstatement is not replay

The world may have changed while the state slept. A k-line must distinguish:

- **invariants** — purpose, method, unresolved problem, relevant agencies
- **volatile bindings** — current files, people, world state, permissions, evidence
- **refresh hooks** — what must be re-read or recomputed
- **invalidators** — conditions under which the old state should *not* resume

An activation recipe plus a checkpoint, not a frozen brain image.

## Fidelity test

Stronger than "the model mentions the same topic." After restoration, the
system must recover:

1. What was the active goal?
2. Why had it become important?
3. Which alternatives had been rejected, and why?
4. What remained uncertain?
5. Which schema prediction was awaiting evidence?
6. What action was intended next?
7. Which constraints must not be violated?
8. What changed in the world while the process was inactive?
9. Should the old plan still resume?
10. Which agencies should become active now?

Compare against an uninterrupted reference continuation (condition A in
[SERIALIZATION-LOSS.md](SERIALIZATION-LOSS.md)). A successful k-line restores
**disposition** — what the system notices, expects, avoids, and is prepared to
do — not prose.

## Activation protocols instead of agent chatter

Most internal transitions should not become essays. Compact, auditable
operations:

```
ACTIVATE contradiction-check
INHIBIT premature-consensus
RAISE-SALIENCE unresolved-grounding
PIN schema:door-affordance
REQUEST evidence:world-state
```

An agency does not speak unless speaking is its function.

## Representation research

Compare, for the same state of mind: prose summary, structured YAML capsule,
agency/schema graph, episodic fragments, full token prefix, KV/prefix
snapshot, learned control vector, hybrids. The likely answer is not one
representation but a **pyramid selected by budget and runtime capability** —
the same Semantic Image Pyramid logic MOOLLM already applies to skills.
