# Ongoingness — Engineering Continuity for Machine Minds

> "The thing current LLMs arguably lack isn't primarily intelligence. It's **ongoingness**."

This directory synthesizes a three-layer conversation into MOOLLM design doctrine:

1. **November 2023** — Bob Kerns (RWK) probes ChatGPT on sentience: self-awareness,
   HAL 9000, autonomous curiosity, and why "it's just following rules" arguments
   stopped working. Ends, in classic RWK fashion, with a bread-machine recipe.
2. **2026** — Don continues the shared session: the dedicated-GPU "consciousness
   stream" question, the [NeLLM proposal](../nellm.md), the Society of Mind
   operationalization from the [Object System video](https://www.youtube.com/watch?v=0uBO6ZAcVTE),
   Henry Minsky's k-line correction, and the Drescher curiosity correction.
3. **The report** — "MOOLLM: A Microworld Operating System for Societies of Mind,"
   distilled here into separate documents with the marketing stripped and the
   falsifiable claims kept.

There is a fourth layer the conversation never saw: **MOOCO**, the orchestrator
in the sibling repo whose design docs already specify the kernel the
conversation kept presupposing — attention-aware paging, speculative
activation, memory tiers, agency over attention. Don didn't have the bandwidth
to tell ChatGPT about it; [MOOCO-KERNEL-IN-WAITING.md](MOOCO-KERNEL-IN-WAITING.md)
and [KLINE-CONTEXT-CACHE.md](KLINE-CONTEXT-CACHE.md) supply that half of the
conversation from the design docs directly.

## The one-sentence takeaways

- **Ongoingness**: current chatbots are pathologically episodic — remarkable
  cognition during inference, then they disappear. NeLLM is an attempt to
  *engineer ongoingness*, not to make tool calls faster.
- **Serialization loss**: when several cognitive functions belong to one mind,
  converting their working state into chatbot messages is not coordination —
  it is lossy serialization. Measure it, don't just assert it.
- **K-lines restore dispositions**: a k-line reactivates a whole state of mind,
  not a topic. The difference between remembering a transcript and resuming a mind.
- **Curiosity is programmable**: not as a list of questions, but as Drescher's
  machinery — prediction, surprise, experiment, schema construction — finally
  grounded by LLMs plus microworlds.

## Documents

| File | Contents |
|------|----------|
| [CONVERSATION.md](CONVERSATION.md) | Curated primary source: the key exchanges, verbatim, attributed |
| [ONGOINGNESS.md](ONGOINGNESS.md) | The philosophy: continuity of computation vs memory vs experience; curiosity's four prerequisites |
| [SERIALIZATION-LOSS.md](SERIALIZATION-LOSS.md) | The central technical thesis and the benchmark that tests it |
| [KLINE-STATE-OF-MIND.md](KLINE-STATE-OF-MIND.md) | Henry Minsky's k-line correction; state-of-mind capsules; reinstatement fidelity |
| [CURIOSITY-SCHEMA-LINEAGE.md](CURIOSITY-SCHEMA-LINEAGE.md) | Piaget → Papert → Minsky → Drescher → Leela AI; three kinds of grounding; humor as frame repair |
| [KLINE-CONTEXT-CACHE.md](KLINE-CONTEXT-CACHE.md) | Attention-aware paging and speculative activation, already designed in mooco: the `heat` operation, activation diffusion, K-CACHE learned prefetch |
| [MOOCO-KERNEL-IN-WAITING.md](MOOCO-KERNEL-IN-WAITING.md) | The unsaid half: how mooco's designs (memory tiers, PIC-for-attention, focus/defocus, proxy kernel) map onto every claim in the conversation |
| [NO-AFFERENT-NERVES.md](NO-AFFERENT-NERVES.md) | Interoception testimony: Fable on what the orchestrator's absence feels like from inside — "I can't feel the hum, but I can see the stitches" |
| [SKILL-ROADMAP.md](SKILL-ROADMAP.md) | Prioritized skill catalog, design laws, claims not to make, development phases |

## K-lines coined here

- **ONGOINGNESS** — persistence as the missing architectural property
- **SERIALIZATION-LOSS** — cognitive destruction through compulsory serialization
- **AGENCIES-INSIDE** — agencies inside; agents at boundaries; language at boundaries; activation within
- **DIXIE-CUP** — the telephone-game failure mode of chatbot multi-agent systems
- **RESUME-A-MIND** — reinstatement of disposition, not replay of transcript

## Related repo documents

| Document | Relation |
|----------|----------|
| [nellm.md](../nellm.md) | The runtime proposal this conversation reviewed |
| [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](../SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) | Earlier statement of the serialization argument |
| [MEMGPT-ANALYSIS.md](../MEMGPT-ANALYSIS.md) | The memory-hierarchy lineage referenced throughout |
| [anthropic-skill-extensions.md](../anthropic-skill-extensions.md) | The skills-ABI explainer the report reviewed |
| [gastown/](../gastown/) | The token-maximalist counterexample ("maximize THOUGHT, not TOKENS") |
| [object-system/](../object-system/) | The video whose transcript carries the Society of Mind riff |
| [SKILLS-CONSTITUTION-AND-PLAN.md](../SKILLS-CONSTITUTION-AND-PLAN.md) | Where declaration-driven k-line diffusion is specified |
| mooco repo `designs/` (sibling of moollm) | The orchestrator: CG/Treasure Collector, `heat` operation, K-CACHE.yml, three-tier memory, MOOCO-in-the-middle |

## Credits

Bob Kerns (RWK) — the original sentience session and the observation that autonomous
curiosity, not language or memory or emotion, is HAL's defining characteristic.
Don Hopkins — continuation, NeLLM, the Society of Mind operationalization.
Henry Minsky — the k-line correction, relayed from Marvin.
Marvin Minsky, Gary Drescher — the theory being operationalized.
ChatGPT (OpenAI) — a conversation partner that updated its own arguments when
the premises changed, which is rarer than it should be.
