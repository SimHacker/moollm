# MOOCO Orchestrator Protocol

**Status:** Design vision  
**Read first:** [MOOCO-MANIFESTO.md](MOOCO-MANIFESTO.md) — what MOOCO is (orchestrator, skills, MOOFS, k-lines, namespace)  
**Packages sketch:** [MOOCO-PACKAGES.md](MOOCO-PACKAGES.md)

---

# Introduction

MOOCO is not fundamentally a chatbot.

MOOCO is a protocol endpoint.

The orchestrator behaves similarly to a server.

The LLM behaves similarly to one or more browsers.

This analogy is intentional.

But it is not the destination.

It is a starting point.

---

# Why The Browser Metaphor Matters

Language models already understand browsers.

They understand:

- URLs
- tabs
- navigation
- history
- bookmarks
- forms
- GET
- POST
- cookies
- sessions

These concepts are deeply represented in training data.

Therefore they make excellent cognitive primitives.

The model does not need to learn them.

The model already knows them.

---

# Beyond The Historical Web

The historical web contains many accidents.

HTML, CSS, JavaScript, cookies, REST, and browsers evolved incrementally.

MOOCO is not constrained by those decisions.

Instead we ask:

What were browsers and servers trying to accomplish?

Then we generalize.

---

# LLM As Browser

The LLM acts as a browser.

Potentially many browsers.

Each active context becomes a tab.

```yaml
tabs:
  - architecture
  - cursor-mirror
  - adventure-system
```

Each tab may operate independently.

Each tab may maintain separate context.

Each tab may perform separate navigation.

Parallel cognition becomes a natural extension of tabbed browsing.

---

# The Orchestrator As Server

The orchestrator exposes resources.

```yaml
GET moollm://skills/cursor-mirror

GET moollm://rooms/control-room

GET moollm://docs/architecture
```

The LLM requests resources.

The orchestrator returns representations.

The representation might be:

- text
- markdown
- yaml
- code
- images
- embeddings
- conversations
- generated views

The protocol does not care.

---

# Natural Language As Executable Content

Traditional browsers download JavaScript.

MOOCO browsers download language.

A skill may contain:

```text
When debugging sessions:

1. Examine the timeline.
2. Inspect tool calls.
3. Trace active K-lines.
```

This is executable.

Not by a JavaScript VM.

By an LLM.

Natural language becomes the primary downloaded program format.

---

# Reversing JSON

Traditional systems assume:

```text
human
    ->
code
    ->
json
    ->
machine
```

LLM systems invert this relationship.

A compact natural language description often contains more useful information than a large JSON document.

The orchestrator should prefer transmitting meaning.

The LLM can generate structured representations when necessary.

Not the other way around.

---

# Generated Code

The LLM may still generate:

- JavaScript
- TypeScript
- Python
- Bash
- SQL

The orchestrator may execute these artifacts.

However:

the generated code is merely a temporary implementation, moving the other way.

The underlying intention remains natural language on the "llm virtual browser" side, JavaScript, Python, bash, etc on the "deterministic mooco orchestrator" side.

---

# Tool Calls As HTTP Methods

Tool calls resemble HTTP verbs.

```text
GET
POST
PUT
PATCH
DELETE
HEAD
OPTIONS
```

But generalized.

Examples:

```text
INVOKE
ACTIVATE
ENTER
LEAVE
HEAT
COOL
REFLECT
FOCUS
DEFOCUS
```

The protocol evolves naturally from web semantics.

---

# Partial Retrieval

Browsers do not always download entire resources.

Neither should LLMs.

Examples:

```text
HEAD skill

GET first 50 lines

GET summary

GET card

GET readme

GET implementation
```

Progressive retrieval should be a core capability.

---

# The LLM Also Provides Services

The relationship is not one-directional.

The browser/server model is asymmetric.

MOOCO can make it symmetric.

The orchestrator provides resources.

The LLM provides cognition.

The orchestrator may ask:

```text
Interpret this.

Summarize this.

Generate this.

Evaluate this.

Compare these.
```

The LLM becomes a service provider.

The orchestrator becomes a service provider.

Both become peers.

---

# Symmetric Cognition

Instead of:

```text
browser
    ->
server
```

we get:

```text
llm
    <->
orchestrator
```

Each side provides capabilities.

Each side maintains state.

Each side may initiate actions.

---

# Sandboxed Reality

Generated artifacts execute inside constrained environments.

Examples:

- containers
- sandboxes
- virtual machines
- git worktrees
- temporary branches

The orchestrator provides safety.

The LLM provides creativity.

Neither is trusted completely.

Both are useful.

---

# The Long-Term Vision

The web connected documents.

MOOCO connects cognition.

The web transported files.

MOOCO transports meaning.

The web linked pages.

MOOCO links concepts.

The web connected humans to information.

MOOCO connects intelligence to worlds.

Browsers and servers remain valuable metaphors.

But they are only the first approximation.

The real goal is a protocol for thought.