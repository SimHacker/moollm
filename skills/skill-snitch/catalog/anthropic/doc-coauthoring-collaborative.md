# doc-coauthoring — Deep Probe + MOOLLM Integration Notes

> NOT importing as separate skill. The Reader Testing pattern integrates into `adversarial-committee`. The workflow integrates into `planning`.

**Trust**: GREEN | **Scripts**: 0 | **License**: Apache 2.0 (no LICENSE.txt in skill dir)

## What It Does

3-stage collaborative document creation: Context Gathering (info dump + clarifying questions) → Refinement & Structure (section-by-section brainstorm/curate/draft) → Reader Testing (fresh Claude sub-agents verify clarity).

## Key Pattern: Zero-Context Reader Test

The most valuable idea: spawn a fresh Claude instance with ZERO prior context, give it only the document, and ask "does this make sense?" If the reader can't understand it without the conversation history, the document isn't self-sufficient.

This is the `adversarial-committee` with a specific configuration:

```yaml
committee:
  - name: "The Zero-Context Reader"
    context: none
    question: "Does this document make sense on its own?"
    
  - name: "The Technical Expert" 
    context: domain_knowledge
    question: "Is this technically accurate?"
    
  - name: "The Executive"
    context: time_pressure
    question: "Can I get the point in 30 seconds?"
    
  - name: "The Newcomer"
    context: no_jargon
    question: "What assumptions does this make?"
```

### How to implement with MOOLLM

Use **speed-of-light** to simulate all four readers in ONE call. No sub-agents needed — the LLM simulates multiple perspectives simultaneously. This is faster, cheaper, and the perspectives can interact (The Expert: "this is wrong" / The Executive: "I don't care, is the conclusion right?").

## Where This Goes

### Into `adversarial-committee` (named pattern)

Document "The Zero-Context Reader Test" as a named committee configuration in the adversarial-committee skill. It's a specific, reusable pattern.

### Into `planning` (workflow stages)

The 3-stage structure (gather → refine → test) is a planning template. The shorthand response format ("1: yes, 2: see #channel, 3: no because backwards compat") is worth adopting as a general efficiency pattern.

### NOT a standalone skill

The document creation workflow is too generic to be a skill. It's a planning template + an adversarial-committee configuration + speed-of-light optimization. Three existing skills, composed.
