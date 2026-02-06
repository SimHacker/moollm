# MCP Reference Servers — 7 Servers Deep Probed

> Infrastructure, not skills. The official plumbing that MCP clients connect to. Every line of code reviewed.

**Publisher**: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (~78k stars, Anthropic-backed)
**Scanned**: 2026-02-06 by skill-snitch Deep Probe v2.0

## Why This Matters for MOOLLM

MCP servers are typed tool providers speaking JSON-RPC over stdio. They're not skills — but the MOOLLM vision (skills as MCP servers, advertisements as tool declarations, speed-of-light as virtual MCP loopback) means understanding these is essential. The `filesystem` server's security engineering is what every file-writing MOOLLM skill should aspire to.

## Servers

| Server | Lang | LOC | Tools | Trust | One-liner |
|--------|------|-----|-------|-------|-----------|
| **filesystem** | TypeScript | 1,400 | 14 | GREEN | Gold standard security: symlink defense, atomic writes, null byte rejection, path containment |
| **git** | Python | 500 | 12 | YELLOW | Git ops via gitpython. Flag injection defense. Open to any repo without `--repository` |
| **memory** | TypeScript | 430 | 9 | GREEN | JSONL knowledge graph: entities + relations + observations. Single dep. |
| **time** | Python | 230 | 2 | GREEN | Pure computation. Zero side effects. IANA timezone lookup. |
| **fetch** | Python | 330 | 1 | YELLOW | Arbitrary URL fetch → Markdown. robots.txt compliance. SSRF unprotected. |
| **everything** | TypeScript | 800+ | 18 | BLUE | Test harness for ALL MCP features. `get_env` exposes secrets. Never production. |
| **sequentialthinking** | TypeScript | 225 | 1 | GREEN | Append-only thought chain with branching. Zero side effects. Safest server. |

## Security Deep Dive

### filesystem — The Gold Standard

14 file operations sandboxed to configurable allowed directories. Five layers of defense:

1. **Path containment**: Every path resolved to absolute, checked against allowed directories
2. **Symlink resolution**: Both requested path AND `fs.realpath()` result validated — can't escape via symlink
3. **Null byte rejection**: Explicit `\x00` check prevents null byte path traversal
4. **Atomic writes**: Temp file + `rename()` prevents TOCTOU races where a symlink appears between check and write
5. **Exclusive creation**: `'wx'` flag on new files prevents writing through pre-existing symlinks

Every MOOLLM skill that touches the filesystem should study this implementation.

### git — Flag Injection Defense

Rejects targets starting with `-` in `git_diff` and `git_checkout` to prevent flag injection (`git checkout --upload-pack=evil`). Uses `--` separator before file arguments in `git_add`. Good but not comprehensive — no allowlist of valid ref characters.

### fetch — SSRF Exposure

Will happily fetch `http://169.254.169.254/latest/meta-data/` (AWS metadata), `http://localhost:8080/admin`, or any internal service URL. The robots.txt compliance is good (uses protego library), but cloud deployments MUST add network-level SSRF protection. This concern applies to skill-snitch FETCH-SCAN too.

### everything — get_env Reads Secrets

The `get_env` tool reads and returns arbitrary environment variables. API keys, database passwords, service tokens — anything in the process environment. Test-only. Would be RED in production.

## Cross-Cutting Findings

| Finding | Detail |
|---------|--------|
| **Zero shell execution** | No server uses exec/spawn/subprocess. Even git uses gitpython library. |
| **Dependency hygiene** | Simplest servers have 1-3 deps. No suspicious packages. |
| **Pydantic everywhere (Python)** | All Python servers use Pydantic models for input validation. |
| **Zod everywhere (TypeScript)** | All TypeScript servers use Zod schemas. |
| **No credentials stored** | No server stores or caches credentials. API keys stay in env vars. |

## Protein Extraction for MOOLLM

| What | Where It Goes | Priority |
|------|--------------|----------|
| Filesystem security patterns (5-layer defense) | Any file-writing skill: adventure compile.py, groceries scripts | HIGH |
| Knowledge graph model (entities + relations + observations) | memory-palace, room, container skills | HIGH |
| Sequential thinking with branching | scratchpad skill upgrade | MEDIUM |
| MCP tool ↔ CARD.yml advertisement mapping | future MCP bridge | HIGH |
| robots.txt compliance (protego) | skill-snitch FETCH-SCAN | MEDIUM |
| SSRF protection | skill-snitch FETCH-SCAN, any URL-fetching skill | HIGH |
| Flag injection defense pattern | github skill, any skill that shells out | MEDIUM |
| Pydantic/Zod validation patterns | sister-script convention (typed inputs/outputs) | LOW |
