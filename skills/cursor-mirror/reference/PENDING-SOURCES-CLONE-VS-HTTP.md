# Pending sources: clone vs HTTP

Verdict for each pending source in IDEAS-TODO.yml: **clone and mount in Cursor** vs **peek via GitHub/web is enough**. Use this when deciding what to assimilate next and whether to clone.

---

## Summary

| # | Source | Verdict | Why |
|---|--------|---------|-----|
| 6 | Monish Gosar (context management) | **HTTP only** | Single blog post; no repo. Read on blog.gomonish.com. |
| 8 | Recovery guides (Dre Dyson, Cursor docs) | **HTTP only** | Blog + official docs; no code repo to clone. |
| 9 | somogyijanos/cursor-chat-export | **Assimilated** | SOMOGYIJANOS-CURSOR-CHAT-EXPORT.yml. |
| 10 | fankaidev gist | **Assimilated** | FANKAIDEV-CURSORDISKKV-EXPORT.yml. |
| 11 | Cursor Internals Skill (dav-ell/blink) | **Assimilated** | DAV-ELL-BLINK-CURSOR-SKILLS.yml. |
| 12a | CursorLens (HamedMP) | **Assimilated** | HAMEDMP-CURSORLENS.yml. |
| 12b | markelaugust74 Cursor-history-MCP | **Assimilated** | MARKELAUGUST74-CURSOR-HISTORY-MCP.yml. |
| 12c | SpecStory | **HTTP only** | Extension + docs at docs.specstory.com; no single repo to clone for “Cursor storage.” Use for product description and .specstory/history/ convention. |
| 13 | vltansky/cursor-chat-history-mcp | **Assimilated** | TypeScript MCP; harvested to VLTANSKY-CURSOR-CHAT-HISTORY-MCP.yml. Clone optional for deeper tool/schema mining. |
| 14 | ton-ai-core/unlimite-context | **Assimilated** | TON-AI-CORE-UNLIMITE-CONTEXT.yml. |

---

## Details

### 6. Monish Gosar — reverse-engineering Cursor context management
- **URL:** https://blog.gomonish.com/blog/reverse-engineering-cursor-context-management  
- **Content:** Behavioral (cursor locality, semantic retrieval, recency). No DB schema.  
- **Verdict:** HTTP only. Read the post; nothing to clone.

### 8. Recovery guides
- **URLs:** https://dredyson.com/... ; Cursor docs (shared transcripts, export).  
- **Content:** Paths, chat-history.json, state.vscdb-wal, recovery steps.  
- **Verdict:** HTTP only. Blogs and official docs.

### 9. somogyijanos/cursor-chat-export
- **Repo:** https://github.com/somogyijanos/cursor-chat-export  
- **Size:** 56 KB. **Archived.** Last push Aug 2024. Python, 237 stars.  
- **Layout:** README, chat.py (~9 KB), config.yml, requirements.txt, src/.  
- **Verdict:** HTTP enough. Use GitHub file view or raw for config.yml (paths) and chat.py (keys, discovery). Clone only to run and diff export output with cursor-mirror.

### 10. fankaidev gist
- **URL:** https://gist.github.com/fankaidev/5a8d5385cebd9d130cc60ec427df17f7  
- **Content:** One Python file; `SELECT value FROM cursorDiskKV`; global path `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb`; output md+JSON by timestamp.  
- **Verdict:** **Assimilated.** reference/assimilated/FANKAIDEV-CURSORDISKKV-EXPORT.yml.

### 11. Cursor Internals Skill (dav-ell/blink)
- **Skill page:** https://skills.rest/skill/cursor-internals-skill  
- **Repo:** https://github.com/dav-ell/blink (Dart app, “Manage cursor CLI agents from your phone”), size 926 KB.  
- **Skill install:** “Download https://github.com/dav-ell/blink/archive/main.zip#cursor-internals-skill” → extract to .claude/skills/. The path `.claude/skills/cursor-internals` was not present at repo root in API check; skill may be in the zip subpath or a separate bundle.  
- **Verdict:** **Worth cloning.** Clone blink, open `.cursor/` (mcp.json, rules) and search for cursor-internals or skill content. Mount in Cursor and assimilate Auth, API catalog, 40+ models, and DB schema from the skill docs. If the skill is only on skills.rest (no checked-in skill dir), still clone to inspect .cursor/rules and any Cursor-related docs.

### 12a. CursorLens (HamedMP)
- **Repo:** https://github.com/HamedMP/CursorLens  
- **Size:** 1605 KB. TypeScript, Next.js, PostgreSQL, Prisma. 379 stars. Last push Nov 2024.  
- **Content:** Proxy/dashboard for Cursor; log AI generations, usage, control models.  
- **Verdict:** Clone if you want their logging schema and how they intercept traffic. Otherwise README + homepage (cursorlens.com) is enough for “proxy analytics” assimilation.

### 12b. markelaugust74 — Cursor-history-MCP
- **Repo:** https://github.com/markelaugust74/Cursor-history-MCP (note: MCP in name, not “API”).  
- **Size:** 37 KB. Python, FastAPI, LanceDB, Ollama. RAG over vectorized chat history.  
- **Verdict:** HTTP enough. Small repo; browse for how they read history and embed. Clone only to run the MCP or reuse their ingestion.

### 12c. SpecStory
- **URL:** https://docs.specstory.com/integrations/cursor  
- **Content:** Cursor extension; auto-save to .specstory/history/; share link; AI rules from history.  
- **Verdict:** HTTP only. Docs and extension description; no single “Cursor storage” repo to clone.

### 14. ton-ai-core/unlimite-context
- **Verdict:** **Assimilated.** reference/assimilated/TON-AI-CORE-UNLIMITE-CONTEXT.yml.

---

## Recommendation

- **Clone and mount in Cursor:** **dav-ell/blink** (for Cursor Internals skill content and .cursor/rules). Optionally **HamedMP/CursorLens** if you want proxy/capture schema in code.  
- **HTTP / browse only:** Monish Gosar, Recovery guides, SpecStory, markelaugust74 Cursor-history-MCP.  
- **HTTP enough, clone optional:** somogyijanos/cursor-chat-export (run and compare exports if you want).  
- **Assimilated:** fankaidev gist, ton-ai-core/unlimite-context, somogyijanos/cursor-chat-export, dav-ell/blink, HamedMP/CursorLens, markelaugust74/Cursor-history-MCP.
