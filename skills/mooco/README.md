# MOOCO

MOOCO is a custom orchestrator designed to host MOOLLM skills with strong context control, safe tool boundaries, and structured event emission. This skill documents the design direction, not implementation details.

MOOCO is a separate, private repo for now. This skill uplifts the important ideas so the shared MOOLLM corpus remains the center of gravity.

## What MOOCO Is For

- Deterministic orchestration around LLM calls
- Explicit context assembly and paging
- Safe, scoped tool execution for sister scripts
- Structured event and trace emission
- Managed data flows between skills
- Streaming-first, SSE-native sessions with reconnection support
- Portability of skills across orchestrators and model providers

## What This Skill Contains

- Manifesto-level design goals
- Interfaces that skills can rely on
- Safe defaults and containment patterns
- A shared-core mindset: open source foundations with private extensions

## Relationship to MOOLLM

- MOOLLM stays the shared design source
- MOOCO is an implementation surface
- Skills should be portable across orchestrators
  and resilient to differences in context management

## Architecture Snapshot (Idea-Level)

- Shared conversation schema for messages, parts, and tools
- Async streaming engine with reconnection-friendly events
- Provider abstraction for model portability
- Tool execution loop with explicit turn limits
- Storage designed for time-series and embeddings
- MessagePart extensions can carry framing and consent metadata when needed

## Skill Portability Contract (Brief)

- Skills declare deterministic vs creative steps
- Skills declare sister-script APIs and parameter schemas
- Orchestrators decide sync vs async execution lanes
- Skills remain portable across models and runtimes

## Kilroy Dataflow (Idea-Level)

MOOCO should support Kilroy‑style dataflow networks where events are messages and tools are nodes. Deterministic transforms and small local models can run as focused nodes, and the same network can be rendered as visual programming.

In this model, a skill can declare how its sister scripts compose: as shell scripts, as calls to other skills’ sister scripts, as dataflow nodes, or as imported modules. Sister scripts are both self‑documenting CLI tools and composable modules.

This mirrors COM/OLE/IDispatch: type libraries enable tight, type‑safe bindings (like Visual Basic to COM), while late‑bound interfaces remain flexible but less efficient. MOOCO can support both styles for skills and sister scripts.

Example dataflow (YAML):

```yaml
dataflow:
  nodes:
    - id: ingest_probe
      type: sister_script
      skill: edgebox
      outputs: [probe_report]
    - id: normalize
      type: deterministic
      inputs: [probe_report]
      outputs: [normalized_state]
    - id: local_classifier
      type: local_model
      inputs: [normalized_state]
      outputs: [risk_flags]
    - id: llm_synthesis
      type: llm
      inputs: [normalized_state, risk_flags]
      outputs: [plan_summary]
  edges:
    - from: ingest_probe
      to: normalize
    - from: normalize
      to: local_classifier
    - from: normalize
      to: llm_synthesis
    - from: local_classifier
      to: llm_synthesis
```
