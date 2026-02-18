# Forum harvest: ideas, projects, people

Harvest from Cursor forum and related search for cursor-mirror applications, data representation, project links, and active contributors. Use for assimilation candidates and IDEAS-TODO.

---

## Ideas for cursor-mirror applications

- **Export to markdown/JSON** — Many users want one-click or scripted export of chat/composer to markdown (or JSON) for backup, version control, or feeding back as context. cursor-mirror already has export; align with community patterns (e.g. .specstory/history/ style, or timestamped files).
- **Path-based workspace association** — Metadata is tied to project **path**, not stored in project. Rename/move folder → history “lost” (still on disk under old workspace ID). cursor-mirror could: list orphaned workspaceStorage entries; suggest recovery (copy DB to new workspace id, or relink); document workspace.json → folder URI mapping.
- **Orphan / cleanup** — Users want to “clean unused” workspace metadata and export useful chat before deleting. cursor-mirror could: list workspaces with last-used or size; export selected to markdown; optionally prune or archive.
- **Recovery after rename/move** — Identify old workspace ID from workspace.json (folder URI), copy or symlink state into new workspace folder so Cursor sees history again. Document in a recovery guide.
- **Rich export** — Forum asks for PDF or “rich-ish text” export; currently export is markdown without colored diffs. cursor-mirror could add HTML or styled markdown (e.g. diff highlighting) for better readability.
- **localhost:8001/state** — Some guides mention Datasette at localhost:8001 to query state; likely a separate tool. cursor-mirror could document or integrate with a “serve state for query” workflow.
- **Docker/remote** — Metadata in containers at `~/.cursor-server` or `/home/user/.cursor-server`; cursor-mirror could document and support remote paths for CI/headless use.

---

## Data representation

- **ItemTable vs cursorDiskKV** — Forum and tools confirm migration: “Storage structure has changed… now it may be stored in cursorDiskKV.” Newer Cursor uses global `globalStorage/state.vscdb` with cursorDiskKV for bubbles/composerData; workspace ItemTable still used for session list (composer.composerData etc.). Keep both in KEY-CATALOG and BORG.
- **Workspace = path** — workspaceStorage folders are keyed by hash; each has workspace.json (folder URI). Association is path-based; no in-project storage. Data representation for “workspace” in cursor-mirror: folder URI, path, workspaceStorage id, list of state.vscdb paths (workspace + global).
- **Tabs vs composers** — Older posts say “chat history organized in tabs”; newer use “composer” and composerId. Unify terminology: composer = one conversation; bubbles = messages; composerData = metadata.

---

## Forum threads (additional)

| Thread | Topic | Use |
|--------|--------|-----|
| [Guide: 5 steps exporting chats & prompts](https://forum.cursor.com/t/guide-5-steps-exporting-chats-prompts-from-cursor/2825) | Datasette, ItemTable query, parse JSON | Classic query; 22k views; Han, sheikheddy |
| [Where is all metadata stored?](https://forum.cursor.com/t/where-are-all-the-metadata-chat-composer-history-indexed-cached-data-workplace-settings-etc-stored/42699) | Path-based association, orphan cleanup, .vscode-style storage request | Design rationale; user “tree” |
| [Small script to export chat history](https://forum.cursor.com/t/small-script-to-export-chat-history/35361) | cursorDiskKV-based export (fankaidev gist) | Migration to cursorDiskKV |
| [Built extension: save chat and composer history](https://forum.cursor.com/t/built-a-cursor-extension-to-save-and-share-chat-and-composer-history/35314) | SpecStory extension | Extension approach |
| [Save chat & composer to markdown file](https://forum.cursor.com/t/save-chat-composer-to-markdown-file/54247) | cursor-chat-export-to-markdown, batch files | Multi-platform export |
| [Export as rich-ish text](https://forum.cursor.com/t/export-cursorai-conversation-as-rich-ish-text/37986) | Rich export, formatting | Feature idea |
| [SOLVED: Renamed folder, history gone](https://forum.cursor.com/t/solved-i-renamed-3-project-folder-names-and-my-composer-and-chat-history-is-gone/48163) | Recovery: workspace id, copy DB | Recovery procedure |
| [Where are cursor chats stored?](https://forum.cursor.com/t/where-are-cursor-chats-stored/77295) | Storage locations | Onboarding |
| [Can I get full Composer history?](https://forum.cursor.com/t/can-i-get-full-composer-history/20587) | Export full history; points to somogyijanos repo, chat storage location | 1.1k views; open source code + prompts |

---

## Other references

- **cursordocs.com** — [How to Export Cursor Chat History (2025)](https://cursordocs.com/tutorial/02-cursor-chat-history-export): guide; tools mentioned (cursor-chat-export, unlimite-context, SpecStory).

---

## Projects to look at

| Project | Author | What | GitHub / link |
|---------|--------|------|----------------|
| **cursor-chat-export** | somogyijanos | Python CLI; discover workspaces, export to Markdown; ItemTable/cursorDiskKV | https://github.com/somogyijanos/cursor-chat-export |
| **cursor-db-mcp** | jbdamask | MCP server; cursor:// resources; query_table | https://github.com/jbdamask/cursor-db-mcp (assimilated) |
| **cursor-rpc** | everestmz | Go + protos; API/auth from state.vscdb | https://github.com/everestmz/cursor-rpc (assimilated) |
| **cursor-chat-export (gist)** | fankaidev | Python; cursorDiskKV; globalStorage paths; export to md+JSON | https://gist.github.com/fankaidev/5a8d5385cebd9d130cc60ec427df17f7 |
| **Cursor chat export script** | legel | “Export chat history in .md from SQL”; context feed-back | https://gist.github.com/legel/ebd0bbc012bf019a1db5212b825e7d16 |
| **SpecStory** | Han (forum) | Cursor extension; auto-save chat/composer to .specstory/history/; share link | https://docs.specstory.com/integrations/cursor ; marketplace |
| **CursorLens** | HamedMP | Proxy; logs AI interactions, analytics; Next.js, PostgreSQL, Prisma | https://github.com/HamedMP/CursorLens |
| **Cursor-history-MCP / Cursor-history-API** | markelaugust74 | Vectorize chat history; LanceDB, Ollama; RAG API | https://github.com/markelaugust74/Cursor-history-API (or Cursor-history-MCP) |
| **Cursor Internals Skill** | dav-ell | Reverse-engineered docs: Auth, API, DB schema, 40+ models; installable skill | https://skills.rest/skill/cursor-internals-skill ; https://github.com/dav-ell/blink (skill in .claude/skills/cursor-internals) |
| **cursor-history** | S2thend | Node CLI; list/show/export; tool types, thinking | https://github.com/S2thend/cursor-history (assimilated) |
| **cursor-chat-history-mcp** | vltansky | TypeScript MCP; git-link commits to chats; search, analytics; 100% local SQLite | https://github.com/vltansky/cursor-chat-history-mcp (assimilated) |
| **unlimite-context** | ton-ai-core | TypeScript; auto-detect state.vscdb (all OS); export to cursor-composers/ | https://github.com/ton-ai-core/unlimite-context |

---

## People and GitHub accounts to check

| Forum / source | GitHub / note |
|----------------|----------------|
| **Han** | SpecStory; Cursor extension; forum guide. Check SpecStory org or Han’s profile for other Cursor work. |
| **somogyijanos** | https://github.com/somogyijanos — cursor-chat-export |
| **fankaidev** | https://github.com/fankaidev — gist for cursorDiskKV export |
| **jbdamask** | https://github.com/jbdamask — cursor-db-mcp (assimilated) |
| **everestmz** | https://github.com/everestmz — cursor-rpc (assimilated) |
| **S2thend** | https://github.com/S2thend — cursor-history (assimilated) |
| **HamedMP** | https://github.com/HamedMP — CursorLens |
| **markelaugust74** | https://github.com/markelaugust74 — Cursor-history-MCP / API, vectorization |
| **dav-ell** | https://github.com/dav-ell — Blink repo, Cursor Internals skill (Auth, API, schema) |
| **legel** | https://gist.github.com/legel — export script |
| **vltansky** | https://github.com/vltansky — cursor-chat-history-mcp (assimilated) |
| **ton-ai-core** | https://github.com/ton-ai-core — unlimite-context |
| **tree** (forum) | Forum user; raised path-based metadata and orphan cleanup; no GitHub identified |
| **sheikheddy** | Forum; contributed to export guide (Sheikh Abdur Raheem Ali) |

---

## Assimilation candidates

- **somogyijanos/cursor-chat-export** — Python, config.yml paths, workspace discovery; compare with S2thend (Node) and BORG keys.
- **fankaidev gist** — cursorDiskKV-focused; globalStorage; good for “migration from ItemTable” note.
- **Cursor Internals Skill (dav-ell/blink)** — Auth, API catalog, DB schema in one skill; potential Stage 1 source for API/schema.
- **SpecStory** — Extension approach; .specstory/history/; share link; AI rules from history; document as alternative to CLI.
- **CursorLens (HamedMP)** — Proxy/analytics; different angle (observe traffic vs read DB).
- **markelaugust74 Cursor-history-API** — Vectorization, RAG; data representation for “chat as vectors.”

Add any of these to IDEAS-TODO.yml `sources_ordered` when ready to assimilate. EXTERNAL-SOURCES.md updated with a "More forum and projects" section pointing here.

**Clone vs HTTP:** For each pending source, see **reference/PENDING-SOURCES-CLONE-VS-HTTP.md** — which are worth cloning and mounting in Cursor vs peeking via GitHub/web only.
