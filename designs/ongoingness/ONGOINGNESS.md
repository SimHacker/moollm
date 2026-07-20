# Ongoingness

> The thing current LLMs arguably lack isn't primarily intelligence. It's
> ongoingness.

## Three continuities, often conflated

The dedicated-GPU "consciousness stream" question splits cleanly:

1. **Continuity of computation** — engineering. Keep the KV cache; never
   cold-start. Nothing in the transformer architecture requires inference to
   stop after one response.
2. **Continuity of memory** — engineering. Finite context eventually wins, so
   you need a hierarchy (working / episodic / semantic / retrieval — the
   MemGPT shape, which is also several cognitive theories of human memory).
3. **Continuity of subjective experience** — philosophy. Nobody has a theory
   of why brains produce subjective experience, so nobody can say which
   architectural properties are essential.

The design mistake is arguing about (3) while (1) and (2) remain unbuilt.
Building them doesn't prove consciousness; it **eliminates confounding
variables**. Every classic objection that turns out to be an engineering
artifact — no continuity, no memory, no persistence, no idle cognition —
stops being a philosophical argument.

Humans are not counterexamples to interrupted continuity: sleep, anesthesia,
comas, childhood amnesia, and the constant rewriting of autobiography all
interrupt or compress. An AI that periodically consolidates its own context is
doing something analogous. Not identical — analogous.

## Curiosity's four prerequisites

RWK's November 2023 observation: HAL's defining characteristic isn't language,
memory, or emotion — it's **autonomous curiosity**. Current LLMs answer
questions superbly and are not in the business of generating them.

The 2026 sharpening: curiosity requires

1. **continuity** — a process that exists across episodes
2. **idle time** — cycles not consumed by servicing requests
3. **memory** — accumulated unfinished business
4. **agency over attention** — choosing what to think about next

Today's chatbots have none. A NeLLM-style runtime supplies the first three
almost automatically. The fourth — attentional policy when no user tokens are
arriving — is where the research is. "What gets paged in next?" stops being
scheduling and starts being curiosity.

The fourth prerequisite already has a specified mechanism at the API level:
MOOCO's focus lock / defocus protocol and LLM-driven paging, where the model
chooses what to attend to and reports what was worth attending to. See
[MOOCO-KERNEL-IN-WAITING.md](MOOCO-KERNEL-IN-WAITING.md).

A process that runs for 20 seconds has almost no opportunity to become curious.
A process that runs for six months might. You don't program curiosity as a
module; you give a system enough persistence that it can **discover unfinished
business**. Humans accumulate unfinished business. That's why we wonder.

(See [CURIOSITY-SCHEMA-LINEAGE.md](CURIOSITY-SCHEMA-LINEAGE.md) for the
Drescher correction: the *machinery* of curiosity absolutely can be programmed.)

## CGI scripts vs. Unix processes

Viewed historically, the current LLM deployment model is bizarre. Alan Kay's
lineage — Smalltalk, NeWS, the Internet, Unix processes — is systems of
persistent communicating objects. Current LLM products are CGI scripts:
prompt, run, exit.

| Today | NeLLM |
|-------|-------|
| Inference as CGI script | Inference as Unix process |
| Tool call = model dies, restarts | Token boundary = interrupt; microkernel work between tokens |
| Computation migrates to the tool | Data migrates to the computation ("the room came to the character") |
| Memory bolted on | Scheduling built in |
| The LLM is "the AI" | The LLM is the CPU; the orchestrator is the kernel |

The deepest sentence in [nellm.md](../nellm.md), per its reviewer:

> The model maintains a continuous high-dimensional trajectory instead of
> repeatedly dying and being resurrected in approximately the right
> neighborhood.

Not a consciousness claim — a computational observation. Transformers compute
in an enormous latent state; today's API architecture throws that state away
at every boundary.

## What KV persistence actually buys (and doesn't)

Keep the claims honest:

- Preserving the KV cache lets generation continue without reconstructing its
  token-derived attention history. That is a **real, specific form of
  computational continuity**.
- It does *not* preserve transient per-forward-pass activations, and it does
  not establish subjective experience.
- "Context window IS virtual memory" is productive as a design analogy (page
  faults, working sets, thrashing, prefetch) but a file cannot be inserted as
  arbitrary semantic state into a standard transformer's KV cache — it must be
  tokenized, or handled by a runtime built for reusable prefixes.

## Idle cognition without self-stimulation

A persistent system should not "think continuously" merely because compute is
available. Background scheduling — consolidate memories, notice
contradictions, re-read earlier work, formulate next questions, *sleep* —
should follow expected value and resource budgets. Continuous self-talk to
simulate ongoing existence is the failure mode; see the thought-budget skill in
[SKILL-ROADMAP.md](SKILL-ROADMAP.md).

## Time as a computational resource

Current LLM APIs optimize FLOPs per token. Ongoingness optimizes **continuity
per thought**. Those are orthogonal axes, and nearly all current engineering
effort is on the first one.
