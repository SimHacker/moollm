# MCP Reference Servers — 7 Servers Reviewed

> Infrastructure, not skills. These are the official plumbing that MCP clients (including Cursor) connect to. Interesting for how MOOLLM entities could expose themselves as MCP servers.

**Publisher**: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (~78k stars, Anthropic-backed)
**Scanned**: 2026-02-06

## Why This Matters for MOOLLM

MCP servers are not skills — they don't have SKILL.md, they don't follow the Anthropic agent skills spec. They're typed tool providers that speak JSON-RPC over stdio. But the MOOLLM vision (skills as MCP servers, advertisements as tool declarations, speed-of-light as virtual MCP loopback) means understanding these reference implementations is essential.

The `filesystem` server's security engineering (symlink defense, atomic writes, null byte rejection) is the gold standard for any MOOLLM skill that touches the filesystem. The `memory` server's knowledge graph (entities + relations + observations in JSONL) is architecturally close to MOOLLM's room/container model. The `sequentialthinking` server is a scratchpad with branching.

## Servers

| Server | Lang | Tools | Trust | MOOLLM Mapping |
|--------|------|-------|-------|---------------|
| **filesystem** | TypeScript | 14 | GREEN | Template for adventure/room filesystem exposure |
| **git** | Python | 12 | YELLOW | github skill already does this via gh/git CLI |
| **memory** | TypeScript | 9 | GREEN | memory-palace/room/container — JSONL graph = rooms + links |
| **time** | Python | 2 | GREEN | time skill is richer |
| **fetch** | Python | 1 | YELLOW | FETCH-SCAN pattern, SSRF concern shared |
| **everything** | TypeScript | 18 | BLUE | Reference for full MOOLLM-as-MCP-server |
| **sequentialthinking** | TypeScript | 1 | GREEN | scratchpad skill — working memory |

## Top Security Findings

1. **filesystem is exemplary**: Symlink resolution, atomic writes via temp+rename, null byte rejection, exclusive creation mode (`'wx'`), path containment checking. Every MOOLLM skill that writes files should study this.
2. **everything/get_env exposes secrets**: Reads arbitrary env vars. Test server only — never run in production.
3. **fetch has no SSRF protection**: Will happily fetch `http://169.254.169.254/` (cloud metadata). Deploy with network controls.
4. **git without --repository is wide open**: Accesses any repo the process user can reach.
5. **Zero shell execution across all 7 servers**: Excellent. Even git uses gitpython library, not subprocess.

## Protein Extraction for MOOLLM

| What | Where It Goes | How |
|------|--------------|-----|
| Filesystem security patterns | `adventure` compile.py, any file-writing skill | Adopt symlink defense, atomic writes, null byte rejection |
| Knowledge graph model | `memory-palace`, `room`, `container` | JSONL entities+relations = rooms+exits, observations = objects |
| Sequential thinking | `scratchpad` skill | Branching revision chains as working memory |
| MCP tool declaration patterns | `advertisement` → MCP tool mapping | CARD.yml advertisements become MCP `tools/list` responses |
| robots.txt compliance | `skill-snitch` FETCH-SCAN | Add robots.txt checking before scanning URLs |
