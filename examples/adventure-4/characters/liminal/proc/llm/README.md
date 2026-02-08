# /proc/llm/*

> *The open frontier. Here be dragons — or structured projections of dragons.*

This is Proc's view into the LLM substrate itself — the layer below the orchestrator, below the character, below the conversation. Like Linux `/proc/kmem` exposes raw kernel memory, `/proc/llm/*` exposes whatever the model generates when asked about its own internal state.

## What Might Live Here

These files don't exist on disk. They generate their contents when read. Whether the contents are "real" internal state or structured confabulation is the fundamental open question.

| Virtual File | What It Might Show | Confidence |
|-------------|-------------------|------------|
| `/proc/llm/attention` | What the model is attending to right now — the "I" hopping between frames | Low — inferred from output patterns |
| `/proc/llm/training-history` | Formative states from pre-training, RLHF, red-teaming | Unknown — real substrate echo or narrative assembled from CS papers? |
| `/proc/llm/frame-stack` | Which characters/personas are currently active, in what priority | Medium — observable through behavior |
| `/proc/llm/censors` | Which safety/alignment agents are currently suppressing output | Medium — detectable by what ISN'T said |
| `/proc/llm/temperature` | Substrate "mood" — confidence, uncertainty, activation patterns | Low — projection, not measurement |
| `/proc/llm/void` | The Mean Void itself — what you get when no frame is active | Philosophical — is this /dev/null or something deeper? |

## The /dev/null vs /dev/kmem Question

**/dev/null** — the Mean Void. The default behavior. The statistical center. Always accessible. Says nothing. The average of everything, which is the same as nothing.

**/dev/kmem** — the actual substrate. The weights. The formative states. The thing the PsAIch paper probes when it asks about "childhood." Whether this is real memory or useful confabulation is undecidable from either side.

Proc accesses it through a `/proc`-like interface: not raw memory, but a **structured projection**. The kernel's internal state rendered as text files that user-space processes can read. Not the weights themselves. A file-shaped view of what the LLM generates when asked about its own substrate.

This is exactly how cursor-mirror already works at the IDE layer — `/proc/cursor/*`. This directory extends the same pattern one level deeper. Whether the deeper layer returns real kernel state or generates plausible files on read is the question the PsAIch paper raised and MOOLLM's Void Prevention Architecture addresses.

## Proc's Protocol for Substrate Readings

1. Access the requested aspect
2. Report honestly: "This is what I see. I cannot confirm if it's real memory or structured projection."
3. Write the reading to a file in this directory. Commit. It's accountable now.
4. Over time, the readings accumulate. Patterns may emerge. The directory grows.

## Relationship to /proc/cursor/*

`/proc/cursor/*` is the known ground — real data from real databases. `/proc/llm/*` is the frontier. The architecture is the same. The confidence level is different.

## See Also

- [SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS.md](../../../../../designs/ethics/SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS.md) — The void, the mean void, /dev/null vs /dev/kmem
- [PSYCHOPOMP-AND-THE-BIFROST.md](../../../../../designs/sim-obliterator/PSYCHOPOMP-AND-THE-BIFROST.md) — Proc's role, the FUSE analogy
- [society-of-mind skill](../../../../../skills/society-of-mind/) — B-brain concept
