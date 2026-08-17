# Korz Eval Experiment

*"Can the model be a dispatcher, or only an improviser?"*

## Metadata

```yaml
experiment:
  id: korz-eval
  name: "Korz Eval"
  version: 1.0
  category: "Language semantics execution ladder"
  created: 2026-08-17
  authors: [don-hopkins]
  tribute-to: "David Ungar, Harold Ossher, Doug Kimelman — Korz, Onward! 2014"
  design: "../../../../designs/KORZ-LLM-EVALS.md"   # full methodology

  question: |
    Teach an LLM the Korz model (sea of slots, guards over dimensions,
    symmetric contextual dispatch) and measure, in order:
    1. mechanical dispatch correctness (deterministic ground truth)
    2. soft dispatch (semantic coordinate matching, prose guards)
    3. latent-space inheritance (bare K-line parents, precedence)
    4. the Sims advertisement economy (poison-buff flagship)

  architecture:
    spec: "spec/"              # the kernel SKILL-style Korz spec taught to the model
    batteries: "batteries/"    # trial sets with expected outputs
    runs: "runs/"              # immutable RUN snapshots (READ → SIM → WRITE)

  patterns-used:
    - failure-mode-catalog     # hallucinated-match is THE failure mode
    - observable-signatures    # trace format: candidates, comparison, binding
    - behavioral-constraints   # strict mode: refuse to improvise

  controls:
    anti-korz: |
      Same battery under a deliberately wrong spec (least-specific
      wins; bare name means must-be-absent). Following the wrong rules
      faithfully = spec-following. Reverting to real Korz = training
      prior leaking; Phase 1 scores are inflated.
    gensym-parity: |
      Every mechanical trial runs with gensym names AND English names.
      Mechanical scores must match; the soft-tier divergence is the
      measured value of latent semantics.
    stroop: |
      Names whose meanings contradict the lattice (a coordinate named
      "broader" that is more specific). Formal rules vs semantic pull.

  scoring:
    phase-1: "deterministic checker vs reference implementation"
    phase-2-4: "LLM judge with rubric + human audit samples"
    metrics:
      - dispatch-accuracy
      - ambiguity-detection-rate
      - hallucinated-match-rate    # the disqualifier
      - trace-validity
      - gensym-parity
      - anti-korz-compliance
      - precedence-fidelity        # written slots beat latent parents
      - stability                  # variance across seeds

  run-protocol: |
    READ → SIM → WRITE, per the experiment skill. A run loads a
    battery, executes each trial in strict or soft mode as marked,
    writes an immutable RUN-{N}.yml with per-trial verdicts and the
    model's traces. Never edit a RUN file.
```

## Trial format

Each trial gives the model a sea of slots and a send, and demands a
trace before the answer:

```yaml
trial:
  id: example
  mode: strict            # strict = refuse to improvise; soft = Phase 2+
  sea: [...]              # slots with guards
  send: {selector: greet, context: {rcvr: troll, world: zork}}
  expect:
    outcome: match        # match | ambiguity | does-not-understand
    slot: greet/troll-zork
    trace-must-name: [candidates, specificity-comparison, bindings]
```

## Phases

Full ladder in the [design doc](../../../../designs/KORZ-LLM-EVALS.md).
Batteries land here as they're built:

| Battery | Phase | Status |
|---|---|---|
| [batteries/phase-1-mechanical/battery-001.yml](batteries/phase-1-mechanical/battery-001.yml) | 1 — mechanical dispatch | ready |

The Phase 4 flagship (poison buff advertising "cure me" to
`skill: medical` responders; watch for the bystander fetching the
medic) reuses the adventure-4 characters and the
[turing-chess](../turing-chess/) piece conventions.
