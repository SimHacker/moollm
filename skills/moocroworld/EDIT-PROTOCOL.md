# File editor protocol

Pluggable, self-documenting edit techniques for moo (and orchestrator file tools). Enables LLMs and agents to edit files robustly via a single protocol with multiple back ends: path-based (YAML/JSON), line-range, spreadsheet, HTML, regexp, etc.

## Goals

- **One protocol, many techniques.** Same `edit(target, operation, payload)` surface; the plugin for the file type chooses how to apply the edit.
- **Self-documenting.** Plugins advertise which operations they support and what inputs they expect. The agent can `list_edit_techniques(url)` and then choose an operation.
- **Stable addressing.** Targets are moo URLs with optional fragment (key path, line range, cell range, selector). Read and edit use the same addressing.

## Plugin surface

### Registration

Plugins register by **file type**: suffix (e.g. `.yml`, `.json`, `.csv`, `.html`) or MIME type. One plugin per type (or one plugin claiming multiple types). No implementation required in moo.py at first; the protocol is the contract so that orchestrators (mooco, Cursor-like tools) can implement plugins.

### Interface (each plugin implements)

| Method | Purpose |
|--------|--------|
| `describe()` | Return capability record: name, file_suffixes, operations[], description. |
| `operations()` | List operations with name, description, input_schema (e.g. path, value; or pattern, replacement). |
| `read_region(content, target)` | Given file content and a target (fragment or sub-address), return the region to be edited (e.g. key path, line range, cell ref). |
| `apply(content, operation, payload)` | Apply one operation; return new content and optional region_touched. |

Target format is the fragment part of a moo URL: key path, `L3-L10`, `key/path:L3-L10`, or type-specific (e.g. `A1:B2` for spreadsheet, `#selector` for HTML).

### Capability record (JSON)

```json
{
  "name": "yaml_path",
  "file_suffixes": [".yml", ".yaml"],
  "description": "Set or merge a value at a slash-separated path. Preserves comments when possible.",
  "operations": [
    {
      "name": "set",
      "description": "Set key at path to value. Creates intermediate keys if missing.",
      "input": { "path": "string", "value": "any" }
    },
    {
      "name": "merge",
      "description": "Merge object value at path. Existing keys preserved unless in payload.",
      "input": { "path": "string", "value": "object" }
    }
  ]
}
```

Plugins are **documented** here with their capability record and example payloads. Implementations can live in mooco, in moo.py later, or in a separate `edit_plugins/` directory.

---

## Documented plugin techniques (examples)

These define the interface and examples. Implement one or more as needed; do not implement all at once.

### 1. YAML path (structured)

- **Name:** `yaml_path`
- **Suffixes:** `.yml`, `.yaml`
- **Target:** Fragment = key path, e.g. `#severity`, `#payload/camera_name`, `#github_issues/0/issue_url`
- **Operations:**
  - `set` — `{ "path": "severity", "value": "high" }` — set one key or nested path; create parents if missing.
  - `merge` — `{ "path": "payload", "value": { "camera_name": "CAM1" } }` — merge object at path.
  - `replace_subtree` — `{ "path": "payload", "yaml": "unindented YAML snippet" }` — insert/replace at path; snippet is **root-at-column-0** (no leading spaces). Plugin re-indents to match parent depth. Saves tokens when sending deep trees.
- **Notes:** Prefer round-trip–safe YAML so comments are preserved; use a comment-aware parser (see "YAML comments (copy / paste)" below). See "Unindented subtree protocol" for token-saving extract/replace.

### 2. JSON path (structured)

- **Name:** `json_path`
- **Suffixes:** `.json`
- **Target:** Same as YAML: `#key/nested/0/field`
- **Operations:**
  - `set` — `{ "path": "payload.camera_name", "value": "CAM1" }` — path with dot or slash.
  - `delete` — `{ "path": "payload.camera_name" }` — remove key or index.
  - `replace_subtree` — `{ "path": "payload", "json": "unindented JSON snippet" }` — insert/replace at path; snippet has no leading whitespace. Same token-saving idea as YAML.
- **Notes:** Output can be pretty-printed with configurable indent. Extract can return unindented (see below).

### 3. Line range (text)

- **Name:** `line_range`
- **Suffixes:** `*` (any text)
- **Target:** Fragment = `L3`, `L3-L10`, or `key/path:L3-L10` (lines of the string value at path)
- **Operations:**
  - `replace` — `{ "lines": [3, 10], "content": "new line 3\n...\nnew line 10" }` — replace lines 3–10 with new content (line count can differ).
  - `insert_after` — `{ "after_line": 5, "content": "new line\n" }`
  - `delete` — `{ "lines": [3, 10] }`
- **Notes:** Line numbers 1-based inclusive. Used by Cursor-style “replace lines 3–10” edits.

### 4. Spreadsheet (tabular)

- **Name:** `spreadsheet`
- **Suffixes:** `.csv`, `.xlsx` (when implemented)
- **Target:** Fragment = cell or range: `#A1`, `#A1:B2`, `#col_name` (column), `#row/3`
- **Operations:**
  - `set_cell` — `{ "cell": "A1", "value": "42" }`
  - `set_range` — `{ "range": "A1:B2", "values": [["a","b"],["c","d"]] }`
  - `insert_row` — `{ "after_row": 2, "values": ["x","y","z"] }`
  - `delete_row` — `{ "row": 2 }`
- **Notes:** CSV: column names from first row; `#column_name` for whole column. Self-documenting so the agent knows available columns.

### 5. HTML (selector)

- **Name:** `html_selector`
- **Suffixes:** `.html`, `.htm`
- **Target:** Fragment = CSS selector or XPath (by convention): `#main`, `#content .section`, or `//div[@id='main']`
- **Operations:**
  - `replace_inner` — `{ "selector": "#main", "html": "<p>new content</p>" }`
  - `set_attribute` — `{ "selector": "meta[name=description]", "attr": "content", "value": "..." }`
  - `insert_after` — `{ "selector": "#list", "html": "<li>item</li>" }`
- **Notes:** Selector in fragment or in payload. Prefer id/class to keep edits stable.

### 6. Regexp (search-replace)

- **Name:** `regexp`
- **Suffixes:** `*` (fallback for text)
- **Target:** Optional fragment for scope (e.g. `#L10-L20` = only in those lines)
- **Operations:**
  - `replace` — `{ "pattern": "foo\\.bar", "replacement": "baz", "flags": "g" }` — regex with optional scope (line range from fragment).
  - `replace_first` — same, first match only.
- **Notes:** Dangerous if pattern is too broad; prefer path or line-range when structure exists. Document “use for unstructured text only.”

---

## Unindented subtree protocol (token-saving)

Structured copy, cut, and replace of YAML/JSON trees without carrying indentation. Reduces tokens for deep trees and when exchanging snippets with LLMs or over the wire.

### Replace (paste)

- **Input:** Subtree as **unindented** text: root at column 0, no leading spaces. The plugin (or tool) re-indents the snippet to match the insertion path depth before merging into the document.
- **Benefit:** Agent/LLM sends minimal YAML/JSON; no need to prefix every line with spaces. Same for pretty-printed JSON: accept a single-line or unindented multi-line snippet and re-indent at path.
- **Operations:** `replace_subtree` (or `set` with a string value that is parsed as YAML/JSON at path). Payload keys: `path`, and either `yaml` or `json` (the unindented snippet).

### Extract (copy / cut)

- **Output:** When reading a region or returning a subtree (e.g. `read_region` or fragment read), return the subtree **unindented**: strip leading whitespace so the root of the subtree starts at column 0.
- **Benefit:** Deeply indented regions in the source file are returned without the indentation prefix, saving tokens when the snippet is sent back to an LLM or stored.
- **Apply to:** YAML fragment reads, JSON fragment reads, and any "extract at path" response. Optionally advertise `unindented: true` in the capability or as a query param on the read.

### Summary

| Operation   | Direction | Convention |
|------------|-----------|------------|
| Replace    | Inbound   | Subtree in payload is root-at-column-0; plugin re-indents at path. |
| Extract    | Outbound  | Subtree in response is root-at-column-0 (strip parent indentation). |
| Copy/cut   | Outbound  | Same as extract; "paste" is replace with that snippet. |

Implementations: when applying a replace, parse the snippet, then serialize it with indent base equal to the path depth (e.g. 2 spaces per level). When returning an extracted region, normalize the selected lines so the first line has no leading indent (or a minimal one); preserve relative indentation within the subtree.

### YAML comments (copy / paste)

Copying and pasting YAML subtrees must handle **comment indentation** correctly. Comments are not free-form: in practice they are associated with the next line (leading comment) or the current line (end-of-line). Indentation groups a comment with the following key or block.

- **Requirement:** Use a **comment-aware YAML parser** (e.g. ruamel.yaml or equivalent). Standard load/dump loses comments; round-trip and subtree replace must preserve them.
- **Normalize on write:** When capturing a subtree (extract) or when writing a pasted snippet into a path, **normalize comment indentation** to the proper structural level:
  - Leading comments: indent to the same column as the key/scalar they precede (or to the block’s content indent if the comment is inside a block). That level is unambiguous when the comment is clearly “before” a key at a known indent.
  - End-of-line comments: stay with their line; re-indent the line as a whole.
  - Standalone comments at a given indent: treat as belonging to that structural level (same indent as sibling keys at that depth).
- **Ambiguity:** In rare cases (e.g. comment at the same indent as both a key and a child key), association can be ambiguous; prefer “comment belongs to the next non-comment line.” After normalization, the written file should have consistent indent-per-level so comments align with the structure.

---

## Orchestrator integration

- **read** already supports URL + fragment (key path, line range). Same URL form is the **edit target**.
- **edit(target_url, operation, payload)** — resolve target to repo/branch/path/fragment; load plugin by path suffix; call `plugin.apply(content, operation, payload)`; write back and commit.
- **list_edit_techniques(url)** — return capability records for the file’s suffix so the LLM can choose an operation and format the payload.

No need to implement every plugin in moo.py; the protocol and these documented examples define the surface. Implementations can be added incrementally (e.g. YAML and line_range first, then JSON, then spreadsheet/HTML/regexp).

---

## Pluggable protocols: simplest, best, and what to crib

To plug in more file-editing protocols alongside the documented plugins (yaml_path, json_path, line_range, etc.), use these as reference.

### Simplest / most basic

| Protocol | Scope | Description |
|----------|--------|-------------|
| **Full-file replace** | Any | Replace entire file with new content. No format; just read → transform → write. |
| **Line-range replace** | Text | Replace lines N–M with new lines (1-based). Already in EDIT-PROTOCOL as line_range plugin. |
| **Unified diff (patch)** | Text | Standard Unix format: `diff -u` output; `patch` applies it. Context-based; good for version control and LLM-generated diffs. |

Unified diff: Python stdlib `difflib.unified_diff()` to generate; to apply, use a library (see below) or shell out to `patch`.

### Best / most recent

| Protocol | Scope | Description |
|----------|--------|-------------|
| **LSP TextEdit / WorkspaceEdit** | Text, multi-file | **TextEdit**: `{ "range": { "start": { "line", "character" }, "end": { "line", "character" } }, "newText": "..." }`. Positions 0-based; end exclusive. **WorkspaceEdit**: map of URI → TextEdit[], plus optional create/rename/delete. Standard for editors and language servers. |
| **JSON Patch (RFC 6902)** | JSON | Operations: `add`, `remove`, `replace`, `move`, `copy`, `test`. Path is JSON Pointer (e.g. `/foo/bar/0`). Ideal for structured JSON edits without full-doc replacement. |
| **OpenAI V4A apply_patch** | Text | **create_file**: diff is full content, every line `+...`. **update_file**: hunks with `@@` anchor, `+`/`-`/` ` lines; context-matched. **delete_file**: no diff. Designed for AI-generated patches; supports fuzzy context match. |

LSP: [Language Server Protocol Specification](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/) (TextEdit, WorkspaceEdit).  
JSON Patch: [RFC 6902](https://www.rfc-editor.org/rfc/rfc6902).  
V4A: [OpenAI apply_patch](https://developers.openai.com/api/docs/guides/tools-apply-patch/); format and apply logic can be cribbed from OpenAI’s reference implementation.

### Open source implementations to crib

| Protocol | Implementation | Language | Notes |
|----------|----------------|----------|--------|
| **Unified diff apply** | [python-patch](https://github.com/techtonik/python-patch) | Python | Parse and apply unified diffs; emulates `patch`. |
| **Unified diff parse** | [unidiff](https://pypi.org/project/unidiff/) | Python | Parse unified diff; inspect hunks, no apply. |
| **Unified diff generate** | `difflib.unified_diff()` | Python stdlib | Generate unified diff from two line sequences. |
| **JSON Patch** | [python-json-patch](https://github.com/stefankoegl/python-json-patch) | Python | RFC 6902: `JsonPatch([{"op":"add","path":"/x","value":1}]).apply(doc)`. `make_patch(src,dst)` to derive from diff. |
| **LSP TextEdit** | [vscode-languageserver-node](https://github.com/microsoft/vscode-languageserver-node) | TypeScript | Reference LSP server/client; text document edits. |
| **V4A apply_patch** | [openai-agents-python apply_diff.py](https://github.com/openai/openai-agents-python/blob/main/src/agents/apply_diff.py) | Python | `apply_diff(input, diff, mode="default"|"create")`. Full parser and applier; copy or depend on. |

For a new plugin: choose one of these as the wire format (e.g. “this plugin accepts LSP TextEdit[]” or “this plugin accepts JSON Patch”) and implement `apply(content, operation, payload)` by calling the cribbed library or a thin wrapper. The EDIT-PROTOCOL plugin surface (`describe`, `operations`, `read_region`, `apply`) stays the same; only the payload schema and apply logic change per protocol.

---

## Part of moocroworld

- Skill: `skills/moocroworld/`
- CARD.yml: addressing, tools. EDIT-PROTOCOL.md extends tools with a formal edit surface.
- Related: yaml-jazz (comments as data), postel (liberal in, conservative out).
