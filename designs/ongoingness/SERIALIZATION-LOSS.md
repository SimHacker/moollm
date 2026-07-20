# Serialization Loss — The Central Technical Thesis

> When several cognitive functions belong to one mind, repeatedly converting
> their working state into chatbot messages is not coordination. It is lossy
> serialization.

## The problem

Most current "multi-agent" systems are distributed chatbot RPC:

```
internal state → natural-language message → API boundary
              → another model invocation → reconstructed internal state
```

Formally: S₀ →serialize→ T₀ →reconstruct→ Ŝ₁ →serialize→ T₁ →reconstruct→ Ŝ₂ …
with no reason to expect Ŝₙ₊₁ = Sₙ.

The token message omits weak activations, rejected alternatives, unresolved
tensions, implicit assumptions, degrees of confidence, unverbalized analogies,
active constraints, and the trajectory that made a thought salient. The
receiving model fills those gaps **plausibly, not faithfully**. Then the next
agent summarizes the reconstruction, and the process repeats — a cognitive
telephone game where each participant confidently invents what the last
transmission destroyed.

The vivid versions, in escalating order:

- prisoners in solitary confinement exchanging notes written in lipstick on
  wet napkins, delivered by carrier pigeon, instead of everyone in one room
- a Dixie cup on a wet string during a hurricane, with a second model paid to
  hallucinate the original state back into existence
- neurons in the visual cortex writing emails to neurons in the motor cortex

The objection is not token cost (though the cost is real — money, latency,
energy). It is **cognitive destruction through compulsory serialization**.
Maximize THOUGHT, not TOKENS.

## The rule

**Agencies inside; agents at boundaries. Language at boundaries; activation
within.**

- An **agent** is an accountable actor with a genuine boundary: another
  machine, model, user, organization, permission domain, or failure domain.
- An **agency** (Minsky's sense) is a cognitive specialist participating in a
  shared computation: critic, noticer, planner, suppressor, schema builder,
  contradiction detector, joke recognizer. Agencies are *smaller than people*
  and often nonverbal. A critic need not write a memo; it may simply inhibit.
- A **coalition** is a temporary working assembly of agencies.

Tokens are the right interface when crossing a real boundary: humans, audit
trails, trust/permission domains, genuinely independent systems, heterogeneous
models, independent verification. Separate agents remain right when
independence *is the point*: adversarial review, fault isolation, privilege
separation. The sin is serializing cognition merely because the framework only
knows how to call chatbots.

Current frameworks are synchronous distributed systems (speak, wait, respond —
latency explodes). Co-located agencies are a shared-memory multiprocessor: the
attention mechanism itself determines what information flows where, with no
decision overhead about *whether* to communicate.

## The honest qualification

"Telepathy" is a metaphor. Several roles in one prompt still communicate
through token representations and attention over shared context; they do not
exchange arbitrary hidden-state objects, and intermediate activations vanish
after each forward pass. But they share the same token history, KV cache,
working context, world description, and one uninterrupted generation
trajectory — materially better than independent API agents. The stronger form
(reinstating or exchanging latent states directly) requires modified runtimes;
see the Priority-5 experimental skills in [SKILL-ROADMAP.md](SKILL-ROADMAP.md).

## The benchmark: build it first

The thesis must be tested, not repeated. One model, one task family, several
continuation conditions:

| Condition | Description |
|-----------|-------------|
| A | Uninterrupted continuation — one context, one trajectory |
| B | Same-context agencies — named specialists in one context |
| C | Full-transcript handoff — new invocation gets complete history |
| D | Summary handoff — new invocation gets a conventional summary |
| E | Structured state capsule — goals, schemas, hypotheses, constraints, next action |
| F | K-line reconstruction — compact name resolves to capsule + files + memories |
| G | Prefix/KV restoration — where the local runtime permits |

Measure: task success, forgotten constraints, contradictions, invented
assumptions, recovery of unresolved hypotheses, prediction of the intended
next action, tokens, latency, external calls, energy, human correction
required, variance across runs.

Include adversarial cases where a summary *sounds* complete while omitting a
weak but decisive constraint — that is exactly where summaries fail silently.

This single laboratory (`serialization-loss-lab`) determines whether "preserve
thought rather than maximize token exchange" is a measurable engineering
result or a persuasive metaphor. Build the benchmark first. Then build the
skills that beat it.

## See also

- [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](../SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) — the earlier repo statement of this argument
- [gastown/](../gastown/) — the token-maximalist counterexample analyzed at length
- [KLINE-STATE-OF-MIND.md](KLINE-STATE-OF-MIND.md) — what a faithful state handoff would even mean
