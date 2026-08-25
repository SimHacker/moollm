# MCP vs Skills + CLI Pipes

> Composition economics: when the model is the only union vs when the kernel is.

**Related:** [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](./SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) (multi-agent simulation, carrier pigeon metaphor) · [sister-script](../skills/sister-script/SKILL.md) (doc → CLI) · [speed-of-light](../skills/speed-of-light/GLANCE.yml) · [2026 MCP roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) · [HN discussion](https://news.ycombinator.com/item?id=49399591)

---

## Thesis

MCP composes at the speed of **governance**. Skills + Unix pipes compose at the speed of **light**.

Every MCP hop forces data through the LLM token bus. There is no `|`. The model must ingest arguments, emit JSON, read results, re-reason. Skills amortize instructions once; **data moves off-bus** through stdin/stdout.

MCP is not replacing APIs — it stacks meters:

```
SaaS API bill  +  model token bill  +  (often) MCP host/marketplace bill
```

Per-token vendors need not conspire. MCP makes the LLM the **only** composition layer. That maximizes billable surface by architecture.

---

## Two composition layers

| Layer | Mechanism | Marginal cost | Example |
|-------|-----------|---------------|---------|
| **Process** | stdin/stdout, pipes, exit codes | ~free (electricity) | `gh pr list \| jq \| rg lazy` |
| **Token bus** | tool call → JSON → model → tool call | tokens + latency | MCP `list_prs` then MCP `get_issue` |

```bash
# Skill + CLI: one orchestration decision, zero intermediate tokens
cursor_mirror.py grep 'lazy-cave' | tail -20 | jq -r '.text'
```

```
# MCP: minimum two bus crossings for the same work
model → tools/call(list) → JSON → model → tools/call(filter) → JSON → model
```

**Skills compose in bash.** MCP composes in context — unless code mode smuggles a script into a vendor sandbox (see below).

---

## What MCP is good for

Not composition. **Constraints:**

| Constraint | MCP | skill + CLI |
|------------|-----|-------------|
| No shell (cloud agent, locked VDI, browser harness) | yes | no |
| Corp policy: approved plugins, no arbitrary code | yes | no |
| Non-dev marketplace install ("Add Slack") | yes | awkward |
| OAuth/SSO across many SaaS, vendor-maintained | yes | roll your own |
| Per-tool ACL without handing over bash | yes | containerize hard |
| You have shell, `gh`, skills | **no** | **yes** |

**Decision rule:** MCP is middleware for environments that **cannot** run middleware-free.

---

## "Vendor ships MCP, not CLI" — wrong

Major vendors ship **both**:

| Vendor | CLI | MCP |
|--------|-----|-----|
| GitHub | `gh` | yes |
| Google | `gcloud`, `gsutil` | yes |
| AWS | `aws` | yes |
| Cloudflare | `wrangler` | yes (+ Code Mode) |

MCP is a **second front door** (harness, marketplace, ACL), not a CLI gap-filler. For developers with shell: skill wrapping `gh` wins.

---

## Code mode (2026)

Not MCP spec. A **harness pattern**: model writes script → vendor sandbox executes → many calls inside → one result to model.

Cloudflare: [`search()` + `execute()`](https://blog.cloudflare.com/code-mode-mcp/) in a Workers isolate (~1k tokens vs millions of tool schemas). Anthropic, Goose, others converging.

| Question | Answer |
|----------|--------|
| Pattern portable? | Yes — architectural, not CF-only |
| Where code runs? | **Vendor sandbox** (garden wall) |
| Which MCP servers? | Can be **multi-vendor** behind a gateway (e.g. MCP Portals) |
| vs bash on your machine? | Different thing — still cheaper locally |

Code mode is MCP admitting pipes win, then selling the pipe factory inside a leased isolate:

```
bash:      model → script → gh | jq | curl

code mode: model → execute() → [Vendor isolate] → MCP → MCP → API → back
```

---

## 2026 roadmap vs composition

[MCP roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) priority areas:

- **Progressive discovery** — less idle schema tax; still not pipes
- **Tasks / webhooks** — long loops without polling model every tick
- **HTTP unification** — deployability, not pipeability
- **Agent identity / DPoP** — who calls, not how cheap

HN thread ([49399591](https://news.ycombinator.com/item?id=49399591)) has fragments (lubujackson on wrong layer for batch, cjg007 on 44 tools ≈ 8k tokens, skinfaxi/wilj on code mode) but **no single coherent synthesis** of bus economics + pipes + stacked billing + CLI already exists.

---

## MOOLLM stack

```yaml
skill:      protocol + when-to-use + invoke line
cli:        sister-script child — proven procedure automated
pipe:       composition layer (speed of light for data)
mcp:        optional transport when shell/auth/marketplace blocked
llm:        orchestrator — decides WHAT to run, not carrier for every byte
```

**Hybrid (recommended):**

```yaml
# SKILL.md
invoke: python3 skills/cursor-mirror/scripts/cursor_mirror.py grep "$QUERY" | tail -50
# Remote only when needed:
# invoke: mcp://vendor/execute  # one fat tool, pipeline inside sandbox
```

Anti-pattern: N sequential MCP micro-tools for work one pipeline does.

Anti-pattern: using MCP for in-context simulation — see [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](./SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md).

---

## Head-play and lazy caves

[examples/lazy-cave/](../examples/lazy-cave/) — adventure rooms on disk when persisted; **head-play** holds graph in session (Amsterdam canal tours). Python `lazy_cave.py` is a reference engine for CI, not the canonical form. Composition limit for in-head play: ~15–25 rooms with perfect graph; ring topology easier than dense skew mesh.

Disk-backed MCP playtests can fail for mundane reasons (temp dir full) — head-play sidesteps that entirely.

---

## Summary

| | MCP | Skills + CLI |
|---|-----|--------------|
| Composes via | model context | kernel pipes |
| Cost model | stacked meters | instructions once, data free |
| Best for | no-shell, auth, marketplace | developers with shell |
| Code mode | vendor sandbox + MCP inside | your machine + bash |

> MCP composes at the speed of governance. Pipes compose at the speed of light. Use MCP when bash is banned — not when `gh` is already installed.

---

## K-lines

- CARRIER-PIGEON — see [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](./SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md)
- SPEED-OF-LIGHT — in-context simulation; orthogonal to pipe composition
- SISTER-SCRIPT — doc → CLI automation
- TOKEN-BUS — model as only union between tools (this doc's name for the anti-pattern)
