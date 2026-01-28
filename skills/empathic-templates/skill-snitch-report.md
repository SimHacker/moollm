# Skill Snitch Report: empathic-templates

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** TEMPLATES THAT UNDERSTAND

---

## Executive Summary

**Smart templates with semantic understanding.**

Not just string substitution — intelligent content generation that understands context and creates appropriate, coherent output.

---

## The Core Insight

| Old Way | Empathic Way |
|---------|--------------|
| `description: '{{description}}'` | `description: '{{describe_based_on_context}}'` |
| Dumb passthrough | Semantic generation |
| User provides everything | LLM infers what's appropriate |

---

## Template Syntax

### Basic (string substitution)
```
{{variable}}
{{#if condition}}...{{/if}}
{{#each items}}...{{/each}}
{{> partial_name}}
```

### Empathic (semantic understanding)
```
{{describe_X}}
{{summarize_Y}}
{{generate_Z}}
{{appropriate_W}}
{{format_V}}
{{infer_traits_from_context}}
```

---

## Methods

| Method | Purpose |
|--------|---------|
| **INSTANTIATE** | Create instance from template with context |
| **PARSE** | Analyze template structure |
| **PREVIEW** | Show what instantiation would produce |
| **VALIDATE** | Check if context satisfies template |

---

## Front-Matter Pattern

First 50 lines let LLM sniff:
- Template name and purpose
- Required variables with types
- Optional variables with defaults
- Example context

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Dumb passthrough** | `{{description}}` | `{{describe_based_on_context}}` |
| **No context** | No semantic hints | Provide tone, setting, constraints |
| **Over-specification** | 50 required variables | Few required, many inferrable |

---

## Relationship to Inheritance

| Concept | Role |
|---------|------|
| **Templates** | Prototypes (define shape) |
| **Instances** | Created by instantiation |
| **Inheritance** | Self-style delegation |
| **Empathy** | LLM adds semantic value |

---

## Security Assessment

### Concerns

1. **Arbitrary generation** — LLM produces content
2. **File writes** — Instantiation creates files
3. **Context injection** — Malicious context

### Mitigations

- Templates are visible
- Output paths constrained
- Context validated before use

**Risk Level:** LOW — bounded generation

---

## Why "Empathic"?

Traditional templates are **mechanical**: substitute X for Y.

Empathic templates are **understanding**: generate what's appropriate given context.

The template says `{{describe_atmosphere}}`. The LLM:
1. Reads the context (room type, time, mood)
2. Generates appropriate atmosphere
3. Maintains coherence with surroundings

The template doesn't specify HOW. It trusts the LLM's comprehension.

---

## Advertisements

| Condition | Score |
|-----------|-------|
| Template instantiation | 95 |
| Character creation | 90 |
| Room generation | 90 |
| Smart (not dumb) generation | 85 |

---

## Verdict

**TEMPLATES THAT THINK. APPROVE.**

The insight: LLMs can understand context. Use that understanding.

Don't ask for `{{description}}`. Ask for `{{describe_based_on_context}}`.

The difference is semantic understanding vs mechanical substitution.
