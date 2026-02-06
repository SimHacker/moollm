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

### Into `adversarial-committee` as a PLUGIN

The adversarial-committee skill should have a `plugins/` directory with reusable committee configurations. The Zero-Context Reader Test becomes one of the first plugins:

```yaml
# skills/adversarial-committee/plugins/zero-context-reader-test.yml

plugin:
  name: zero-context-reader-test
  description: "Test document clarity with readers who have zero prior context"
  source: "Anthropic doc-coauthoring skill"

committee:
  - name: "The Zero-Context Reader"
    context: none
    mode: isolated  # enforced — separate LLM call, no debate history
    question: "Does this document make sense on its own?"

  - name: "The Technical Expert"
    context: domain_knowledge_only
    mode: simulated  # speed-of-light, same call
    question: "Is this technically accurate?"

  - name: "The Executive"
    context: summary_only
    mode: simulated
    question: "Can I get the point in 30 seconds?"

  - name: "The Newcomer"
    context: none
    mode: isolated  # enforced — actually doesn't know jargon
    question: "What assumptions does this document make that I can't follow?"
```

Other committee plugins worth building: code-review-committee, design-review-committee, security-review-committee. Each is a YAML file in `plugins/` with a named cast of characters and their evaluation criteria. The adversarial-committee skill loads the plugin, the evaluator skill handles the isolation mode.

### Into `planning` (workflow stages)

The 3-stage structure (gather → refine → test) is a planning template. The shorthand response format ("1: yes, 2: see #channel, 3: no because backwards compat") is worth adopting as a general efficiency pattern.

### NOT a standalone skill

The document creation workflow is too generic to be a skill. It's a planning template + an adversarial-committee configuration + speed-of-light optimization. Three existing skills, composed.
