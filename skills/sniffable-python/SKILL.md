# Sniffable Python — depth levels and abstractions

How to mark and sniff Python (and other files) at multiple depths. Moo and other tools use this convention.

---

## 1. Sniff depth levels (three, extensible)

Three standard **depth levels** for structural sniffing. Higher depth includes all lower levels.

| Level | Name       | Numeric | Python: what is included |
|-------|------------|---------|---------------------------|
| 1     | **glance** | 1       | Section comments: `# ---`, `# SECTION`, `# UPPERCASE_LABEL`, `# Title Case` (single-line). Module-level outline only. |
| 2     | **structure** | 2    | Glance + `class`, `def`, `async def`, `@decorator`. The skeleton of the file. |
| 3     | **full**   | 3       | Structure + any other line the sniffer classifies as "smelly" (structural). Everything the sniffer emits. |

- **glance** — Smallest useful outline (sections only). Good for indexes and "what's in this file?"
- **structure** — Default for "show me the shape": classes and functions, plus sections.
- **full** — No filtering; all smelly lines. Use when you want every structural line.

Other levels or names are allowed: tools should accept numeric depth (1, 2, 3, …) or canonical names (glance, structure, full) and may support file-type-specific semantics.

---

## 2. Marking Python (optional override)

By default, the sniffer assigns depth by **line kind** (section = 1, class/def/decorator = 2, rest = 3). Authors can override with a comment on the **previous line**:

- `# SNIFF: 1` or `# SNIFF: glance` — next line is treated as depth 1 (glance).
- `# SNIFF: 2` or `# SNIFF: structure` — next line is depth 2.
- `# SNIFF: 3` or `# SNIFF: full` — next line is depth 3.

Alternative form:

- `# depth: glance` / `# depth: structure` / `# depth: full`

Only the line **immediately following** the comment is overridden. Use to promote a line into a shallower depth (e.g. a key function into glance) or to demote (e.g. treat a decorator as full-only).

---

## 3. Other file types

Depth semantics can differ by type:

- **YAML**: e.g. glance = top-level keys, structure = keys + list markers, full = all key/list lines.
- **Markdown**: glance = H1–H2, structure = H1–H4, full = all headers.
- **TS/JS**: glance = export lines, structure = export + function/class/interface, full = all smelly.

Moo (and this skill) define the Python mapping explicitly; other types may be added with their own depth tables. The same numeric/name convention (1/2/3, glance/structure/full) is reused where it fits.

---

## 4. Abstractions beyond depth

Beyond structural depth, files can have **abstractions** that are not just "which lines to show":

- **description** — One-line description (e.g. from docstring or a tag). Could be first docstring line or `# description: ...`.
- **glance** — Short human or generated summary (e.g. GLANCE.yml content, or a cached one-liner).
- **LLM summary** — A model-generated summary of the file, cached locally (e.g. under `.moollm/skills/moo/cache/` or similar). Keyed by (repo, branch, path, abstract_type). Moo can call an LLM (e.g. Gemini) to produce and cache this.

These are **not** depth levels; they are separate axes. A tool might offer:

- `moo sniff --depth glance` — structural outline only.
- `moo summarize` or `moo abstract --kind summary` — LLM summary, with caching and optional `--provider gemini`.

Design leaves room for more abstraction kinds and providers without overloading the depth semantics.

---

## 5. Moo integration

- **Sniff**: `moo sniff ... --depth glance|structure|full` (or `--depth 1|2|3`). Emits only lines at or above the requested depth. Default: structure (2).
- **Summarize**: `moo summarize ... [--provider gemini] [--model MODEL]` — calls LLM, caches under moo cache, prints summary. Requires API key (e.g. GEMINI_API_KEY) and optional `google-genai` (or REST).

Part of MOOLLM. See repo README and skills/README.
