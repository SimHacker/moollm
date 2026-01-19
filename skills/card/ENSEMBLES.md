# Data Flow Ensembles

Cards can contain **coordinated ensembles** of generators, transformers, and consumers that automatically bind into data flow networks.

## Ensemble Card Structure

```yaml
# debate.card
card:
  name: "Structured Debate"
  type: ensemble
  
  components:
    generators:
      CREATE_SIDE:
        params: { name: required, position: required }
        outputs: [arguments, rebuttals]
        
      CREATE_TOPIC:
        params: { question: required }
        outputs: [topic_stream]
        
    transformers:
      CREATE_MODERATOR:
        inputs: [arguments, rebuttals]
        outputs: [moderated_stream]
        behavior: "interleave fairly, enforce time limits"
        
    consumers:
      CREATE_AUDIENCE:
        inputs: [moderated_stream]
        outputs: [reactions, scores]
        
      CREATE_TRANSCRIPT:
        inputs: [all_streams]
        outputs: [transcript.md]
        
  wiring: |
    Topic feeds into both Sides.
    Sides produce Arguments that flow to Moderator.
    Moderator routes to Audience.
    Transcript captures everything.
```

## Automatic Binding with POSTEL

Components **self-wire** based on compatible inputs/outputs:

```yaml
> CREATE_SIDE "Pro" position="AI is beneficial"
> CREATE_SIDE "Con" position="AI is dangerous"
> CREATE_MODERATOR

# LLM applies POSTEL to wire:
data_flow:
  pro.arguments → moderator.inputs
  con.arguments → moderator.inputs
  audience.reactions → moderator.feedback
```

## Factorio-Style Assembly

Build complex processing factories with queues:

```yaml
# research-factory.card
components:
  generators:
    SPAWN_CRAWLER: { outputs: [raw_documents] }
    SPAWN_READER: { outputs: [parsed_content] }
    
  transformers:
    SPAWN_SUMMARIZER: { inputs: [parsed_content], outputs: [summaries] }
    SPAWN_FACT_CHECKER: { inputs: [summaries], outputs: [verified_claims] }
    SPAWN_SYNTHESIZER: { inputs: [verified_claims], outputs: [synthesis] }
    
  consumers:
    SPAWN_NOTEBOOK: { inputs: [synthesis], outputs: [research_notebook.yml] }
    
  queues:
    raw_queue: { capacity: 100, overflow: drop_oldest }
    verified_queue: { capacity: 50, overflow: backpressure }
```

## Queue-Based Logistics

```yaml
data_flow:
  crawler → raw_queue → reader
  reader → parsed_queue → summarizer
  summarizer → summary_queue → fact_checker
  fact_checker.verified → verified_queue → synthesizer

queues:
  raw_queue:
    current: 47
    capacity: 100
    status: flowing
    
  verified_queue:
    current: 12
    status: backpressure  # Synthesizer is slow
```

## Ensemble Orchestration

The card tracks ensemble state:

```yaml
# debate-session-001.activation
ensemble:
  components:
    - id: pro-side
      status: producing
      output_rate: "3 arguments/round"
      
    - id: moderator
      status: routing
      queue_depth: 5
      
  flows:
    pro-side.arguments → moderator: 12 messages
    
  health: nominal
  bottleneck: none
```

## Natural Language Assembly

```
> PLAY debate.card
> "Set up a debate about AI safety with three sides: 
>  optimists, pessimists, and pragmatists. 
>  Add a moderator who enforces Robert's Rules.
>  10-minute rounds with 2-minute rebuttals."

# LLM interprets, creates components, wires data flow
```

**Factorio meets Dataflow meets Natural Language** — complex pipelines assembled from card components, wired by intent.

---

*See [SKILL.md](./SKILL.md) for core protocol.*
