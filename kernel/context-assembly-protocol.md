# Context Assembly Protocol
## Building Prompts from Files

---

## 1. Overview

The LLM's "memory" is its prompt context. This protocol defines how
the orchestrator assembles that context from files, manifests, and
dynamic state — fitting everything into the token budget.

---

## 2. The Working Set Manifest

### Schema

```yaml
# working-set.yml
protocol: CONTEXT-ASSEMBLY/0.1
budget:
  max_tokens: 28000
  reserved_for_response: 4000
  effective: 24000

files:
  - path: ".agent/constitution.md"
    priority: 1.0          # Highest (always included)
    role: "system"
    truncate_strategy: "never"
    
  - path: "current_task.md"
    priority: 0.95
    role: "developer"
    truncate_strategy: "end"
    
  - path: "src/main.ts"
    priority: 0.8
    role: "context"
    truncate_strategy: "middle"
    max_lines: 500
    
  - path: "tool/terminal/log-latest.txt"
    priority: 0.3
    role: "context"
    truncate_strategy: "start"  # Keep recent

metadata:
  last_updated: "2025-12-30T12:30:00Z"
  assembled_by: "model" | "orchestrator" | "user"
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `path` | string | File path relative to session |
| `priority` | float | 0.0-1.0, higher = more important |
| `role` | enum | How to inject: system/developer/user/context |
| `truncate_strategy` | enum | How to cut: never/start/middle/end |
| `max_lines` | int? | Hard limit on lines |

---

## 3. Assembly Algorithm

```python
def assemble_context(working_set, budget):
    """
    Assemble context from working set manifest.
    
    1. Sort files by priority (descending)
    2. For each file, attempt to include
    3. Apply truncation if over budget
    4. Return assembled context + report
    """
    
    # Sort by priority
    files = sorted(working_set.files, key=lambda f: -f.priority)
    
    context = []
    used_tokens = 0
    included = []
    excluded = []
    
    for file in files:
        content = read_file(file.path)
        tokens = count_tokens(content)
        
        if used_tokens + tokens <= budget.effective:
            # Include fully
            context.append(format_for_role(content, file))
            used_tokens += tokens
            included.append(file.path)
            
        elif file.truncate_strategy != "never":
            # Try truncated
            remaining = budget.effective - used_tokens
            truncated = truncate(content, remaining, file.truncate_strategy)
            if truncated:
                context.append(format_for_role(truncated, file))
                used_tokens += count_tokens(truncated)
                included.append(f"{file.path} (truncated)")
            else:
                excluded.append(file.path)
        else:
            excluded.append(file.path)
    
    return AssemblyResult(
        context=context,
        used_tokens=used_tokens,
        included=included,
        excluded=excluded
    )
```

---

## 4. Truncation Strategies

### `never`
File must be included fully or not at all. Use for critical docs like constitution.

### `start`
Keep the end, cut the beginning. Good for logs where recent matters.

```
Original:  [AAAAABBBBBCCCCC]
Truncated: [...BBBBBCCCCC]
```

### `middle`
Keep start and end, cut middle. Good for code files.

```
Original:  [AAAAABBBBBCCCCC]
Truncated: [AAAAA...CCCCC]
```

### `end`
Keep the beginning, cut the end. Good for documents read top-down.

```
Original:  [AAAAABBBBBCCCCC]
Truncated: [AAAAABBBBB...]
```

---

## 5. Role Formatting

Files are injected based on their role:

### `system`
```
<system>
[Constitution content here]
</system>
```

### `developer`
```
<developer>
[Developer instructions/context]
</developer>
```

### `user`
```
<user>
[User message or file content]
</user>
```

### `context`
```
<context path="src/main.ts">
[File content]
</context>
```

---

## 6. Dynamic Context Updates

### Model-Initiated Updates

The model can update `working-set.yml`:

```yaml
# Add file to working set
action: add_to_working_set
path: "newly_discovered.md"
priority: 0.7
why: "Found relevant documentation"

# Remove file from working set
action: remove_from_working_set
path: "no_longer_needed.md"
why: "Task complete, don't need this"

# Adjust priority
action: adjust_priority
path: "important_file.md"
priority: 0.9
why: "This is more relevant than initially thought"
```

### Orchestrator-Initiated Updates

The orchestrator may automatically:
- Add recent tool outputs
- Remove old tool outputs
- Bump files referenced recently
- Demote files not used in N turns

---

## 7. The Boot Header

Every context starts with a minimal boot header:

```
Root: .agent/
Constitution: .agent/constitution.md (v0.1, checksum: abc123)
Session: .agent/sessions/2025-12-30T12-30-00Z/
Output sink: output.md (append-only)
Working set: working-set.yml
Cache hints: hot.yml, cold.yml
Tool contract: All calls require `why`
```

This lets the model orient without reading everything.

---

## 8. Context Budget Guidelines

| Component | Typical Allocation |
|-----------|-------------------|
| System (constitution) | 2000-4000 tokens |
| Developer (task, plan) | 1000-2000 tokens |
| Context (files, artifacts) | 15000-20000 tokens |
| Conversation history | 2000-5000 tokens |
| Reserved for response | 3000-4000 tokens |

**Total budget varies by model.** Adjust `working-set.yml` accordingly.

---

## 9. Reporting

After assembly, the orchestrator reports:

```yaml
assembly_report:
  budget:
    max: 28000
    used: 23456
    remaining: 4544
    
  included:
    - path: ".agent/constitution.md"
      tokens: 2100
      truncated: false
      
    - path: "current_task.md"
      tokens: 500
      truncated: false
      
    - path: "src/main.ts"
      tokens: 8000
      truncated: true
      original_tokens: 15000
      
  excluded:
    - path: "large_log.txt"
      reason: "Over budget, priority too low"
      
  warnings:
    - "3 files excluded due to budget"
    - "1 file truncated significantly"
```

---

## 10. Best Practices

1. **Keep constitution small** — It's always included
2. **Use priorities wisely** — 1.0 for critical, 0.3 for nice-to-have
3. **Truncate logs aggressively** — Use `start` strategy
4. **Update working set actively** — Model should manage its attention
5. **Trust the report** — Don't assume everything was included

---

## 11. Dovetails With

- **Constitution** (§4): Memory policy
- **Memory Management Protocol**: Hot/cold influences priority
- **Tool Calling Protocol**: Tool outputs enter working set
- **Event Logging**: Track what was included when
- **Bouncy Castle Protocol**: Navigation through context

---

*Context is the LLM's reality.*
*What's not in context doesn't exist.*
*Assemble wisely.*
