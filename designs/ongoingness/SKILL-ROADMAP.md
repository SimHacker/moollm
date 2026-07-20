# Ongoingness Skill Roadmap

The report's prioritized catalog, checked against the existing skill tree.
Many entries already exist (marked ✓); the recommendation for those is to add
the missing declarations and tests, not to rebuild.

## Priority 0 — epistemic and packaging infrastructure

| Skill | Status | Responsibility |
|-------|--------|----------------|
| no-ai-slop | ✓ exists | Remove filler, fake certainty, empty summaries |
| no-ai-sycophancy | ✓ exists | Require counterarguments, uncertainty, falsifiers |
| skill | ✓ exists | Root prototype and normative runtime |
| skill-snitch | ✓ exists | Declared vs. observed behavior |
| skill-linter | new | Validate compatibility, self-containment, pyramid structure, inheritance |
| prototype-resolver | new | Inheritance resolution: parent order, overrides, conflicts, provenance, flattened view, cycle detection |
| semantic-image-pyramid | partially (convention) | Build and validate GLANCE → CARD → SKILL → README |
| thought-budget | new | Allocate context, tokens, time, tools by expected cognitive value |

Rule for proposals (enforced via no-ai-sycophancy): every substantial
architectural claim states what is known, what is analogy, what is
speculative, what would falsify it, and what competing design might be better.

## Priority 1 — Society of Mind primitives

| Skill | Responsibility |
|-------|----------------|
| agency | Small cognitive specialist: activation, inhibition, inputs, effects, advertisements. **Does not speak unless speaking is its function.** |
| society-of-mind | Compose agencies into coalitions — not a cast of chatbot personas |
| shared-context | Several agencies in one working context with explicit shared state |
| k-line | Named activation handles and their relationships |
| state-of-mind-capsule | Capture, refresh, validate, reinstate a cognitive configuration ([spec](KLINE-STATE-OF-MIND.md)) |
| schema-mechanism | ✓ exists — context→action→result predictions updated from evidence |
| curiosity-engine | Select safe, informative experiments from schema gaps |
| noticer | Detect anomalies, novelty, contradictions worth activating |
| credit-assignment | Associate outcomes with actions, schemas, agencies, conditions |
| consolidation | Preserve, summarize, generalize, forget, or lift |

## Priority 2 — microworld OS primitives

| Skill | Responsibility |
|-------|----------------|
| microworld-kernel | Identity, lifecycle, events, time, transactions, interrupts, recovery |
| room / character / object | ✓ exist — spatial context, actor identity, persistent entities |
| advertisement | Capability + conditions + utility + cost + relevance scoring |
| simulation-clock | Scheduling, decay, deadlines, sleep/wake |
| coherence-engine | ✓ exists (concept) — world invariants, contradictions, dangling references |
| sensorium / actuator | Typed perceptions in; authorized world changes out |
| episode | Replayable record: decisions, predictions, actions, results |

## Priority 3 — context and persistence

| Skill | Responsibility |
|-------|----------------|
| context-pager | Page files, memories, skills, world objects into the working set |
| working-set-manager | Salience, locality, budgets, pinning, eviction, thrashing detection |
| honest-forget | ✓ exists (concept) — evict while recording what was lost and how to recover it |
| resume | Restore an interrupted task; verify its assumptions still hold |
| k-line-registry | Names → activation recipes, pyramids, memories, schemas |
| memory-consolidator | Episodes → semantic memories, schemas, k-lines |
| prefetch | Anticipate context needs from events, agencies, active schemas |
| provenance | Origin and transformation of claims, memories, skills, inherited behavior |

## Priority 4 — laboratories (the science)

| Skill | Responsibility |
|-------|----------------|
| play-learn-lift | ✓ exists — govern the lifecycle |
| **serialization-loss-lab** | **The first decisive experiment** — [SERIALIZATION-LOSS.md](SERIALIZATION-LOSS.md) |
| state-reinstatement-lab | The 10-question fidelity test — [KLINE-STATE-OF-MIND.md](KLINE-STATE-OF-MIND.md) |
| schema-lab | Schema formation, prediction, repair, abstraction, transfer |
| curiosity-lab | Are chosen experiments informative or merely novel? |
| frame-shift | Competing interpretations and schema repair, including humor |
| thought-efficiency | Useful state change per token, second, joule, external call |
| society-observer | Visualize agency activation, inhibition, coalitions, causal contributions |

## Priority 5 — experimental NeLLM runtime hooks

These declare model/runtime dependencies loudly; they must not pretend to be
portable vanilla skills.

| Skill | Responsibility |
|-------|----------------|
| nellm-driver | Adapt MOOLLM services to a local inference runtime (llama.cpp, vLLM, SGLang) |
| token-interrupt | Structured activation and I/O signals during generation |
| prefix-state-cache | Reuse stable token prefixes and their cache state |
| kv-checkpoint | Preserve and restore model-specific KV state |
| attention-prefetch | Can attention/entropy/uncertainty signals improve paging? |
| latent-k-line | Learned activation vectors or state handles beyond textual retrieval |
| continuous-inference | Generation, waiting, interruption, background tasks, resumption |

## Development phases

1. **Prove the architecture with ordinary LLM calls.** Shared-context
   agencies, k-line registries, state capsules, schema traces, advertisements,
   the two benchmarks. No modified runtime required.
2. **Make the microworld persistent.** Event loop, clock, transactional state,
   permissions, working-set manager, consolidation, interruption/resume,
   Git-backed provenance. "Learning" changes world state and skills, not
   weights.
3. **Integrate a local inference runtime.** Prefix caching, continuous
   generation, token-level signals, context paging. Measure real latency and
   energy; stop citing theoretical tables.
4. **Experiment with latent reinstatement.** KV snapshots, control vectors,
   attention-guided prefetch — with the symbolic system as control condition
   and interpretability layer.
5. **Lift the winners** into Anthropic-compatible skills with MOOLLM
   declarations, tests, permissions, provenance, and model-specific drivers
   isolated from the portable protocol.

## Claims MOOLLM should not make

1. LLM representations are not fully grounded — semantic/social priors only;
   microworlds add operational grounding.
2. One context is not literal latent telepathy — shared token history and
   attention; stronger latent exchange is experimental.
3. KV-cache persistence does not prove consciousness — it demonstrates a
   specific computational continuity.
4. Several verbose personas are not a Society of Mind — agencies are smaller
   than people and often nonverbal.
5. K-lines are not tags or embedding queries — their target is reinstated
   disposition.
6. Summaries do not preserve state until reinstatement fidelity is tested.
7. Permission declarations are not enforcement — kernels enforce.
8. Ambient context is not free — compress and page it.
9. More tokens, more agents, more debate ≠ more thought.
10. One successful improvisation is not a general skill — lift only
    demonstrated mechanisms.
11. Runtime memory changes are not model-weight learning.
12. Continuous self-talk is not ongoing existence.

## Design laws

```
Agencies inside; agents at boundaries.
Language at boundaries; activation within.
Preserve state before summarizing it.
A k-line restores a disposition, not merely a topic.
Schemas predict; worlds answer.
Curiosity chooses experiments, not just questions.
Advertisements expose affordances; schemas estimate consequences.
Context is a managed working set, not a transcript landfill.
Declarations guide; kernels enforce.
Play before abstraction.
Learn from failures and counterexamples.
Lift only demonstrated mechanisms.
Measure thought preserved, not tokens emitted.
Make every important state inspectable, interruptible, and resumable.
Remain compatible outward while becoming compositional inward.
```

## The order of work

Build `serialization-loss-lab` first. It tests the central thesis against the
strongest current fashion, produces numbers instead of metaphors, and every
other skill on this list either feeds it (capsules, k-lines, agencies) or is
justified by its results (pagers, drivers, latent experiments).

Build the benchmark first. Then build the skills that beat it.
