# mcp-builder — Deep Probe + MOOLLM Integration Notes

> IMPORT as new MOOLLM-native skill for MCP server CONSTRUCTION. Note: mooco already orchestrates MCP servers, Cursor runs them natively, cursor-mirror sees all active MCP servers. What's missing is a skill for BUILDING new servers — the factory pattern and evaluation harness.

**Trust**: YELLOW (API calls to arbitrary MCP URLs, Anthropic API) | **Scripts**: 2 Python (connections.py, evaluation.py) | **License**: Apache 2.0

## What It Does

Build MCP servers: research → implement (TypeScript or Python) → review → evaluate. Factory pattern for connections (stdio/SSE/HTTP). Evaluation harness runs Claude as test subject against XML test cases, scores exact-match, generates markdown report.

## Code Review

| Script | Lines | Quality | Issues |
|--------|-------|---------|--------|
| connections.py | 138 | Excellent | Pure library. ABC + 3 implementations. Thorough type hints. No `__main__` (correct for library). Zero CWD dependency. |
| evaluation.py | 290 | Good | Rich argparse with argument groups and epilog examples. Async. XML parsing. Markdown report generation. Uses `ANTHROPIC_API_KEY` from env. |

**connections.py is the best-architected script in the Anthropic repo**: Clean strategy pattern. `MCPConnection` ABC with `_create_context()` hook. `MCPConnectionStdio`, `MCPConnectionSSE`, `MCPConnectionHTTP` concrete implementations. `create_connection()` factory. Async context managers with proper cleanup.

**evaluation.py is the most interesting**: The only Anthropic script that uses an LLM at runtime — but as the TEST SUBJECT, not the orchestrator. The script is deterministic infrastructure; Claude is the thing being tested. XML-tagged structured prompts (`<summary>`, `<feedback>`, `<response>`) for reliable extraction.

## MOOLLM-Native Version

**New skill**: `skills/mcp-builder/`

| Feature | Anthropic | MOOLLM-native |
|---------|-----------|---------------|
| Server templates | Reference docs | **prototype**: MCP servers inherit from parent templates |
| Testing | XML test cases with exact-match | **experiment**: Drescher schema (hypothesis → test → result) |
| Quality | Manual review | **rubric**: measurable criteria for server quality |
| Deployment | Manual | **github** skill handles deployment (delegation) |
| Evaluation | Sequential test cases | **speed-of-light**: simulate multiple scenarios in one call |
| Security | Manual review | **skill-snitch**: auto-scan generated server |
| Discovery | Manual invocation | **advertisement**: MCP-BUILD activates when building servers |

**connections.py**: Keep as-is. It's perfect. Wrap in MOOLLM CARD.yml.

**evaluation.py**: Integrate with `experiment` skill. The XML test case format maps naturally to Drescher schemas. The agent loop pattern is reusable for any tool-use evaluation.

**sveltekit-site-builder note**: The `web-artifacts-builder` counterpart would be SvelteKit-native, not React. Uses Svelte 5 runes, not React hooks. Tailwind stays. shadcn/ui → bits-ui or skeleton. This is a separate skill from mcp-builder.
