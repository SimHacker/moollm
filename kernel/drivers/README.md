# MOOLLM Drivers
## Orchestrator-Specific Adaptations

*"Same OS, different hardware."*

---

## What is a Driver?

A driver adapts the MOOLLM constitution to a specific orchestrator's
capabilities and constraints. Just like OS drivers adapt to different
hardware, MOOLLM drivers adapt to different LLM orchestrators.

---

## Available Drivers

| Driver | Orchestrator | Tier | Key Features |
|--------|-------------|------|--------------|
| `cursor.yml` | Cursor IDE | 4 | File tools, search, terminal |
| `claude-code.yml` | Claude Code | 5 | MCP, custom tools possible |
| `chatgpt.yml` | ChatGPT Web | 3 | Python, browser, apps |
| `custom.yml` | Custom orchestrator | 6 | Full kernel control |
| `generic.yml` | Fallback | 1 | Minimal assumptions |

---

## Driver Structure

Each driver defines:

```yaml
driver:
  name: "orchestrator-name"
  tier: 4
  # NO VERSIONS — the driver IS the current adapter
  
capabilities:
  file_read: true
  file_write: true
  file_search: true
  terminal: true
  custom_tools: false
  why_parameter: false  # Can we add 'why' to tools?
  
paths:
  session_root: ".agent/sessions/"
  output_sink: "output.md"
  event_log: "session-log.md"
  # ... driver-specific paths
  
tools:
  # Map abstract operations to concrete tools
  read_file: "read_file"
  write_file: "write"  # or "search_replace"
  list_dir: "list_dir"
  search: "codebase_search"
  # ...
  
adaptations:
  # How to handle features the driver doesn't support
  why_parameter:
    supported: false
    fallback: "document_intent_in_response"
    
  append_only:
    supported: false  # Can't enforce at tool level
    fallback: "convention_only"
    
  event_logging:
    supported: "partial"
    fallback: "session_log_markdown"
```

---

## Driver Loading

The constitution core loads a driver at session start:

1. Detect orchestrator from environment/tools
2. Load appropriate driver YAML
3. Merge driver config with core
4. Adapt behavior accordingly

---

## Capability Graceful Degradation

When a feature isn't available, drivers specify fallbacks:

| Feature | Full Support | Fallback |
|---------|-------------|----------|
| `why` parameter | Include in tool call | Document in response |
| Append-only | Enforced by orchestrator | Convention only |
| Event logging | `session-log.md` (YAML blocks) | Markdown narrative |
| Vector search | `search.vector` | Grep/manual scan |
| Sandboxed exec | Isolated container | Trust-based |

---

## Creating a New Driver

1. Copy `generic.yml` as starting point
2. Document orchestrator capabilities
3. Map abstract tools to concrete ones
4. Define fallbacks for unsupported features
5. Test with real orchestrator

---

---

## 🗺️ Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [kernel/](../) |
| ⬆️⬆️ Root | [Project Root](../../) |

---

## See Also

- [constitution-core.md](../constitution-core.md) — Universal principles
- [constitution-template.md](../constitution-template.md) — Full template
- [PROTOCOLS.yml](../../PROTOCOLS.yml) — Protocol symbols
