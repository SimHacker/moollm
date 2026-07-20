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

## Two kinds of k-lines: abstract and snapshot

Henry's correction does not abolish the simple reading; it splits k-lines
into two tools with different lifecycles:

- **Abstract k-lines** — LOVE, IUNKNOWN, SECURITY. Concepts with no
  particular trajectory attached; the training data *is* the surrounding
  mental state. Pure activation handles into latent space: the name is the
  whole payload, resolution is dictionary lookup against the resident
  overlay, and what comes back is whatever the model's priors plus the skill
  graph associate. Cheap, timeless, shared across every session.
- **Snapshot k-lines** — minted at a moment, naming a particular mental
  state that existed once: trajectory, stakes, hypotheses, unfinished
  business. These need a schema (the capsule below) and an **address**.

**Minting.** When a state is worth keeping, write the capsule to a file and
bind a fresh k-line to it — a gensym (`K-7F3A`) at minimum, better a
descriptive big-endian name carrying a timestamp and a unique suffix:

```
VAULT-HEIST-PLANNING-2026-07-20T1842Z-7F3A
```

Big-endian so related snapshots sort and group; timestamped because a
snapshot k-line, unlike an abstract one, refers to a *moment*.

**Addressing.** The binding is a pointer that drills down like a URL:
through the directory tree, into a file, into the file's structure via
`#fragment` or path. Such pointers are a well-established "thing" — URL
fragments, JSON Pointer, XPath, `file:line:col`, `repo@commit:path#L10` —
and moo already speaks `moollm://` URLs, so snapshot k-lines ride the same
scheme:

```
moollm://SimHacker/moollm/main/.moollm/snapshots/VAULT-HEIST-PLANNING-2026-07-20T1842Z-7F3A.yml#hypotheses
```

Commit the snapshot and git's content addressing makes the moment immutable
for free.

The resolution paths differ accordingly: an abstract k-line resolves through
the overlay to skills and advertisements; a snapshot k-line resolves through
its address to a capsule, whose procedural layer then takes over — refresh
hooks, invalidators, resumption instructions.

## A string you pull

> In a delightful sense a k-line is a "string" you "pull", in both senses of
> a "string" of characters and a "string" of threads. — Don

The character-string is the address; the thread-string is what it is tied
to. Pull the name and the whole coalition unspools out of storage — capsule,
working set, agencies, unfinished business — the way one loose thread brings
the whole sweater. Ariadne's thread, `git pull`, and Minsky's original
image all in one word.

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

## Storage substrate already specified

MOOCO makes k-lines schema, not convention: `k_line_activate` is a first-class
message part, `k_line_fired` an SSE event with source and strength,
`mooco-mirror k-lines @1` queries any past session's activation history, and
K-CACHE.yml persists learned associations to git. The capsule described above
has a place to live. See
[MOOCO-KERNEL-IN-WAITING.md](MOOCO-KERNEL-IN-WAITING.md).

## Representation research

Compare, for the same state of mind: prose summary, structured YAML capsule,
agency/schema graph, episodic fragments, full token prefix, KV/prefix
snapshot, learned control vector, hybrids. The likely answer is not one
representation but a **pyramid selected by budget and runtime capability** —
the same Semantic Image Pyramid logic MOOLLM already applies to skills.
