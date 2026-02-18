# MOOAM — MOO Access Management

**MOOAM** is a virtual, standardized, best-of-breed **IAM (Identity and Access Management)** adapted and extended for LLMs. We use the same terms and concepts as cloud IAM so that if you know IAM, you know where to reach.

**IAM alignment.** In IAM, a **principal** is who acts (user, service account, role). A **resource** is what they act on (bucket, file, VM, API). A **permission** is the right to perform an action (e.g. read, write, execute). A **grant** (or **policy** binding) assigns permission(s) to a principal on a resource. **Least privilege** means granting only the permissions needed. MOOAM uses these words in the same way and maps them to the LLM world.

**Mapping to LLMs.** Principals become **characters** (or skills acting as characters). Resources become: **tools** (invocable capabilities, e.g. read_file, run_terminal_cmd), **files** (filesystem paths), **paths**, **URLs**, **MCP resources** (resources exposed by MCP servers), **terminal**, **context** (ambient slot in the LLM). So when we say "grant permissions on a resource," we mean: grant this character permission to use these tools, or to read/write these files or paths or URLs, or to use the terminal, or to occupy ambient context. **All MOOLLM objects can participate** as principals or resources.

**See also:** [SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md) (metadata fields **allowed-tools**, **permissions**), [SKILLS-CONSTITUTION-AND-PLAN.md](./SKILLS-CONSTITUTION-AND-PLAN.md) (§3.4). This design may later become a **skill** (e.g. a MOOAM skill with a **mooam-manager**) that implements and audits the model.

**Terminology: advisory vs deterministic.** MOOAM declarations are used in two distinct ways. (1) **Advisory guidance** — for the LLM (what it should try to follow) and for **LLM-behavior snitching tools** (skill-snitch, mitm-snitch): compare declared vs observed tool use, flag mismatches; no claim to attribute "who" acted or to enforce policy. (2) **Deterministic tooling** — tools that support **standard metadata, formats, protocols, and resource types**: they **filter and assemble** context by machine-readable rules (K-line activation, diffusion net, skill related/dependency and conditional activation), wire **dependency import/output graphs** (parameterized importer and exporter arcs), and **assemble or disassemble** compound resources into big-endian named subdirs and YAML and other resource file trees (see §6). Only the latter is deterministic; the former is aspirational.

---

## 1. Model

### 1.1 Principals

Who is acting. In MOOAM we use **characters** as principals (when a skill runs, it acts as a character or group of characters, or as the moollm kernel itself). IAM would call this the principal identity. In practice the principal is **declared**, not observed: in one LLM call we cannot attribute tool use to a single principal (§5).

### 1.2 Resources

What is being acted upon. In IAM, resources are objects, buckets, instances, etc. In MOOAM we map resources to what LLMs and orchestrators actually touch:

| Resource type | Meaning | Examples |
|---------------|---------|----------|
| **tools** | Invocable capabilities | read_file, write_file, run_terminal_cmd, grep; MCP tools |
| **files** | Filesystem paths | Paths on disk the skill may read or write |
| **paths** | Path-like identifiers | File paths, directory paths |
| **URLs** | Network locations | HTTP(S) endpoints, GitHub URLs |
| **MCP resources** | Resources exposed by MCP servers | Tools and resources from an MCP server |
| **terminal** | Shell/command execution | Single resource: may use terminal or not |
| **context** | Ambient slot in the LLM | Always-on context (high trust) |

**Tools are resources.** Declaring **allowed-tools** is declaring which tool resources the skill may use. Permissions then say *what* the skill can do with them (read, write, execute, etc.).

### 1.3 Permissions

A **permission** is the right to perform an action on a resource — same as in IAM. A **grant** is: principal (character) has permission(s) on resource(s). Example: character has **read** and **write** on file resources; has **terminal** on the terminal resource; has **ambient** on context. **Least privilege:** grant only the permissions needed.

### 1.4 Reach inferred from permissions

We do not use a separate "reach" field. **Reach** is inferred from permissions: no file/terminal permissions → prompt-only; **read** and/or **write** → files; **terminal** → terminal. **Ambient** is a permission on the context resource, not a place.

---

## 2. Permission catalogue (canonical)

Skill metadata field: **permissions** (list of permission names). IAM uses the same word.

| Permission | Resource(s) | Meaning | Notes |
|------------|-------------|---------|-------|
| **read** | file, paths, URLs | May read (e.g. read_file, grep). | |
| **write** | file, paths | May write (e.g. write_file). | |
| **files** | file, paths | May read and write files. | Shorthand for read + write. Postel: accept; emit **read**, **write** if canonical. |
| **terminal** | terminal | May use the terminal (e.g. run_terminal_cmd). | Postel: accept **execute** as alias; emit **terminal**. |
| **youtube** | youtube | May watch/use YouTube. | |
| **ambient** | context | Lives in the LLM's head rent-free; always loaded. | **High trust.** Grant sparingly. |
| **code** | code | May read or edit code (codebase, snippets). | |
| **history** | history, session | May read session/chat history (e.g. cursor-mirror, transcripts). | |
| **wizard** | * | Superuser; full override when needed. | Postel: accept **admin** or **cow** as aliases; emit **wizard**. |

---

## 3. Virtual tool names (cross-orchestrator)

Tool names are not standardized across runtimes (Cursor, Claude, etc.). For **cross-LLM-orchestrator skills**, use a **standardized set of virtual tool names**: portable, declarative of intent. Each orchestrator maps virtual → real tool names. MOOLLM suggests a small **MOO canonical set** so skill-snitch and other tooling can understand declared intent regardless of runtime.

In practice those names are **virtual, aspirational, declarative** — the skill declares what it intends to use; the orchestrator binds to real tools. MOOLLM **recommends** that every tool call include a required **why** parameter (WHY-REQUIRED; see PROTOCOLS.yml and kernel/tool-calling-protocol.md).

### 3.1 MOO suggested virtual tool names (canonical set)

| Virtual name | Intent | Example real mappings |
|--------------|--------|------------------------|
| **file_read** | Read file(s) or path(s). | Cursor: `read_file`; Claude: (runtime-specific). |
| **file_write** | Write or overwrite file(s). | Cursor: `write_file`; Claude: (runtime-specific). |
| **file_search** | Search within files (e.g. grep, search). | Cursor: `grep`; Claude: (runtime-specific). |
| **terminal_run** | Run a command in terminal/shell. | Cursor: `run_terminal_cmd`; Claude: (runtime-specific). |

Orchestrators maintain a mapping (virtual → real) per runtime. Skills that target multiple orchestrators declare virtual names in **allowed-tools**; single-runtime skills may use real names. Postel: accept either; emit virtual when publishing cross-orchestrator, real when runtime-specific.

---

## 4. Skill metadata (grants)

Skill metadata declares the **grants** for that skill when it acts: which **resources** (tools) it may use and which **permissions** it has on them.

- **allowed-tools** — Which tool resources the skill may invoke (list of tool names).
- **permissions** — Which permissions the skill has (read, write, files, terminal, youtube, ambient, code, history, wizard).

Example: allowed-tools include read_file; permissions include read but not write → read-only file access. Terminal in allowed-tools and **terminal** in permissions → may use terminal.

Containment, snitch, and **mitm-snitch** (MOOCO-in-the-middle with local LLM) can use declarations to filter what is available and to monitor declared vs actual tool use (see §5).

**Postel (consumers):** Accept liberal input. **permissions:** accept list of strings (read, write, files, terminal, youtube, ambient, code, history, wizard; alias execute → terminal, admin or cow → wizard; files = read + write); or accept legacy **reach** / **tier** and map to permissions (e.g. tier 0 → []; tier 1 → [read, write] or [files]; tier 2 → [read, write, terminal]); omit = infer from allowed-tools. **Emit:** canonical form (list of tool names, list **permissions**; may expand files → read, write).

---

## 5. Who acted? We don't know. Declarations are advisory.

### 5.1 Principal attribution in one LLM call

In a single LLM call — especially in a multi-turn, multi-character speed-of-light simulation — there is **no way to know who acted** or **who called the tool**. The model emits tool calls; we cannot attribute them to a single principal. We can know **who was in context** at the time (which skills, which characters were activated or mentioned), but context is a soup: ghosts of past instructions and earlier turns are still present. So the "principal" in MOOAM is not something we observe or verify; it is a **declaration** that accompanies the skill or character. These declarations are **advisory** and **aspirational** — they guide tooling, they do not determine ground truth about who did what.

### 5.2 What declarations do: guide orchestrator and context assembly

MOOAM declarations (permissions, allowed-tools, grants) **guide** tools that operate on machine-readable context:

- **Orchestrator** — Which skills, tools, and commands are available to the LLM in this session? The orchestrator **deterministically filters** using declarations: load and expose only what the activated skills and their permissions allow.
- **Content assembly** — What gets included in the prompt or context window? **K-line activation**, **diffusion net**, and skill **related/dependency and conditional activation** networks use MOOAM metadata to decide what is pulled in. Declarations shape what the LLM "sees" as available.
- **Snitch and mitm-snitch** — Compare declared vs observed tool use; flag mismatches. Still advisory: we report "this skill declared X but the transcript shows Y," not "principal A violated policy."

So we don't pretend to enforce IAM in the cloud sense. We use declarations to **filter and assemble** context deterministically, and to **tell the LLM** which skills and tools and commands are available — by machine-readable rules, not by the LLM's ability to "obey."

### 5.3 Pretend Intelligence

The LLM cannot enforce these rules 100% of the time. It can *pretend to* — follow them as best it can, declare intent (e.g. why), let advisory containment and snitch checks run — without claiming perfect enforcement. Richard Stallman calls such systems **Pretend Intelligence (PI)** to counter hype that asks people to trust them with their lives and control; we acknowledge the same limit and still find the model useful when we don't overclaim. MOOAM is in that spirit: useful guidance, not a guarantee.

**Jazz standard** lists: **tools** (virtual tool names), **permissions**. Skills declare them; **mitm-snitch** can monitor and advise with a local LLM.

---

## 6. Resource deconstruction and reconstruction

**Resource deconstruction** is the convention and tooling for turning **compound resources** (e.g. Cursor state, orchestrator session state) into **big-endian named** subdirs, YAML, and other resource file trees — and back. **Deconstruct** = compound → tree; **reconstruct** = tree → compound. Deterministic tools **assemble** and **disassemble** these resources using **standard metadata, formats, protocols, and resource types**. Wiring is expressed as **dependency import/output graphs** with **parameterized importer and exporter arcs**: which inputs a resource needs, which outputs it produces, and how they connect. So compound state can be broken into a navigable, K-line-friendly file tree and reassembled from it; the same conventions support deterministic context assembly and filtering (§5.2). This design may be expanded in a separate doc (e.g. resource-deconstruction or MOOCO); the name **resource deconstruction** / **reconstruction** (and **unpacked resource format** for the tree form) anchors the idea here.

---

## 7. Future: MOOAM as skill and mooam-manager

This design lives in `designs/MOOAM.md` for now. It may later be turned into a **MOOAM skill** (a "skell") with a **mooam-manager** — a dedicated component that interprets grants, audits declared vs actual tool use, and **advises** on MOOAM policy (and, where tooling does deterministic filtering, restricts what is available).
