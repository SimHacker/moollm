---
name: file-system-object
description: "The grammar rules that make MOOLLM's file system object-oriented. Plural directory names declare element type; UPPERCASE marker files declare interface exports (COM-style, minus the UUIDs); directories are implementation classes exporting every interface whose marker file sits at their root."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [skill, prototype, card, schema, self, com-xpcom, yaml-jazz, room]
tags: [moollm, meta, grammar, object-oriented, com, self, filesystem, directories, markers]
credits:
  - "Smalltalk (Alan Kay et al., Xerox PARC, 1970s) — classes, messages, image-as-object"
  - "Self (Ungar & Smith, 1987) — prototype delegation; objects without classes"
  - "NeWS (James Gosling & David S. H. Rosenthal, Sun, 1986) — PostScript window system with prototype delegation in production"
  - "TNT: The NeWS Toolkit (Owen Densmore & David S. H. Rosenthal, Sun) — class hierarchy built on NeWS's prototype foundation; the patent and the conceptual ancestor"
  - "COM / XPCOM — multiple interfaces per class; QueryInterface"
  - "Ted Nelson — intertwingled systems; every node can link anywhere"
  - "MOOLLM — the actually-existing MOOLLM file system, already using this grammar before it was named"
---

# File System as Object — Directories, Interfaces, and the UPPERCASE Marker Grammar

> **"A directory named `<things>/` is saying: the things in here are of the type `<thing>`. A file named `FOO.md` at a directory's root is saying: this directory exports the FOO interface. The directory IS an implementation class; the UPPERCASE marker files ARE its interface declarations; no UUIDs needed because the filename IS the class name."**

This skill formalizes a grammar that **already exists throughout MOOLLM**. Every skill you've read — `skill`, `prototype`, `card`, `schema`, `adventure`, `room`, `character`, `incarnation` — uses these rules implicitly. The other meta-skills USE the grammar; this skill NAMES it so newcomers (human or LLM) can read MOOLLM directory trees fluently without pattern-matching each one from scratch.

---

## The Three Rules

### Rule 1: Plural-named directories declare element type

A directory named `<things>/` declares "the things in here are of type `<thing>`."

```
skills/          → each child is (presumably) a skill
biomes/          → each child is a biome
mechanisms/      → each child is a schema mechanism
recipes/         → each file is a recipe
gotchas/         → each file is a gotcha
runbooks/        → each file is a runbook
instances/       → each child is an instance
stacks/          → each child is a stack
protocols/       → each file is a protocol
rooms/           → each child is a room
characters/      → each child is a character
```

"Presumably" is doing real work here: the plural name is a **declaration of intent**. To confirm a specific child actually IS of that type, look for its **interface marker file** (see Rule 3). Auxiliary content (templates, indexes, READMEs) can also live in a plural container without being instances — their absence of a marker file is the tell.

### Rule 2: Singular-named directories are instances

A directory named `<thing>/` (singular, kebab-case or single word) is an **instance**. The directory name is the instance's identifier.

```
skills/skill/                    → instance named "skill" (a specific skill, happens to BE the meta-skill about skills)
skills/biome/                    → instance named "biome"
skills/gcs/                      → instance named "gcs"
mechanisms/json-schema/          → instance named "json-schema"
instances/leela-zion2-dev-0/     → instance named "leela-zion2-dev-0"
```

This reads as: `<plural-container>/<instance-id>/`.

### Rule 3: UPPERCASE marker files declare interface exports

A file named `FOO.md` or `FOO.yml` (UPPERCASE filename) at a directory's root declares that the directory **EXPORTS the FOO interface**.

```
skills/gcs/
├── SKILL.md         ← "I export the SKILL interface"
├── CARD.yml         ← "I export the CARD interface"
├── GLANCE.yml       ← "I export the GLANCE interface"
├── README.md        ← "I export the README interface (human landing)"
├── recipes/         ← plural: "I contain recipes"
├── gotchas/         ← plural: "I contain gotchas"
└── ...
```

The UPPERCASE convention visually distinguishes **interface declarations** from ordinary content. The presence of the file IS the declaration — no separate registry required.

**One directory exports many interfaces.** Just like a COM class implements many interfaces, a MOOLLM skill directory typically exports SKILL + CARD + GLANCE + README + sometimes CHARACTER + EXPORTS + PROTOTYPES — all simultaneously, via multiple marker files.

---

## The COM Analogy

This is Henry's framing, which anchors the whole grammar:

| COM concept | File-system-object equivalent |
|---|---|
| Implementation class (C++ / IDL class) | Directory — the `<thing>/` singular name |
| Interface declaration (IDL `interface IFoo`) | UPPERCASE marker file — `FOO.md` or `FOO.yml` |
| Interface UUID (`IID_IFoo = {01234567-89ab-...}`) | **Not needed** — the filename IS the identifier |
| Multiple interfaces per class | Multiple UPPERCASE marker files per directory |
| `QueryInterface(IID_IFoo, &ptr)` | `cat <dir>/FOO.md` (or "does this dir export FOO?" = `test -e <dir>/FOO.md`) |
| Class factory (`CoCreateInstance`) | Prototype instantiation (see `skill-instantiation-protocol.md`, `delegation-object-protocol.md`) |
| Aggregation (one class delegating to another) | DOP prototype chain via `inherits:` or `PROTOTYPES.yml` |
| TypeLib registry | `schemapedia/registry.yml` (for schema mechanisms); `skills/biome/biomes/registry.yml` (for biomes) |

COM's big wins were: (a) multiple interfaces per implementation, (b) language-neutral contracts, (c) strong versioning via UUIDs. MOOLLM keeps (a) and (b), swaps (c) for **readable UPPERCASE names** because we want humans and LLMs to read the tree, not a binary-stamped registry.

COM's big losses were: opaque UUIDs, fiddly registration, reliance on a global registry, Windows-centric tooling. MOOLLM avoids all four by putting the declarations in the filesystem itself.

---

## Why UPPERCASE

The UPPERCASE-filename convention (`SKILL.md`, `CARD.yml`, `MECHANISM.yml`, `ALERT.yml`, `PROTOTYPES.yml`) does several things at once:

1. **Visual grep.** In any `ls` output, UPPERCASE files leap out. Structural signposts pop; ordinary content recedes.
2. **Class-vs-content distinction.** Lowercase filenames (`camera-configs.json`, `my-recipe.md`) are content; UPPERCASE is meta — "I am telling you what this directory IS."
3. **Namespace cleanliness.** `foo.md` (lowercase) is a note about foo; `FOO.md` (uppercase) is a declaration that this directory implements FOO. They don't collide, and their roles are clear at a glance.
4. **Future-proof tooling.** A validator script can simply glob for `[A-Z]*.{md,yml}` at a directory root to find all exported interfaces. No manifest file, no parsing.
5. **Big-endian naming.** The UPPERCASE prefix groups structural files together alphabetically at the top of `ls` output.

**When NOT to use uppercase.** Normal content, per-instance data (`state.yml`, `history.md`), templates (`RUN.yml.tmpl` — the `.tmpl` is the tell that it's a template, not a declaration), ordinary documentation (`troubleshooting.md`).

---

## Serialization — YAML Preferred, JSON Welcome, Comments Encouraged

Interface marker files come in three flavors, each picked on purpose:

| Extension | Use when | Why |
|---|---|---|
| `.yml` | The interface is **data-shaped** (fields, structure, lists). Default choice. | Comments are first-class and **encouraged** (see [`yaml-jazz`](../yaml-jazz/)). The same file can carry structure, semantic hints, lineage notes, and authorial voice simultaneously. |
| `.md` | The interface is **narrative** (explains, teaches, guides). | Markdown supports prose + structure + code blocks. `SKILL.md`, `README.md` are the canonical narrative interfaces. |
| `.json` | **A downstream tool needs it** (jq pipelines, ajv validators, frontend code reading an API) and no human is expected to author it by hand. | Universal tool support. Smaller parser footprint. But: no comments → strips human intent. |

**The rule: YAML is preferred, JSON is welcome, comments are encouraged.**

### When to prefer which

- **Authoring by hand?** → YAML. Every time.
- **Tool reads it, humans rarely?** → JSON is fine.
- **Both?** → YAML is canonical; emit JSON on a hook if needed.
- **Narrative / teaching / guiding?** → Markdown.

### Why YAML over JSON for MOOLLM interface declarations

YAML gives us three-audiences support (humans, LLMs, machines — see the `yaml-jazz` skill):

```yaml
# CARD.yml — this is a comment — it carries semantic information for
# humans AND LLMs, even though machines technically ignore it.
card:
  id: example
  tagline: "The tagline is the elevator pitch."
  # ↑ Next audience note: rule-of-thumb is one sentence, present tense.
```

Strip the comments and you have the same data. Keep them and you have **intent** alongside the data — why the fields are there, what alternatives we considered, which examples are load-bearing. That's the yaml-jazz difference, and it's why every UPPERCASE marker file in MOOLLM defaults to YAML.

### Canonical patterns observed in MOOLLM

| Pattern | Example | Notes |
|---|---|---|
| Data-shaped interface | `CARD.yml`, `GLANCE.yml`, `MECHANISM.yml`, `ALERT.yml`, `CHARACTER.yml`, `PROTOTYPES.yml`, `EXPORTS.yml` | YAML. Comments throughout. |
| Narrative interface | `SKILL.md`, `README.md`, `CHANGELOG.md` | Markdown with YAML frontmatter. |
| Generated-for-tool interface | rare in MOOLLM proper; common in build outputs | `.json` next to `.yml` canonical, regenerated on change. |
| Template interfaces | `CARD.yml.tmpl`, `SKILL.md.tmpl` | `.tmpl` suffix signals placeholder content; not a real declaration. |

If you're introducing a new UPPERCASE interface type and you have to choose: `FOO.yml` is the default. Reach for `.md` if the content is prose-heavy; reach for `.json` only when a tool demands it.

### The yaml-jazz skill is a hard dependency

This skill inherits conceptually from [`yaml-jazz`](../yaml-jazz/): "Semantic YAML — comments as data; three audiences." The two skills together give MOOLLM its **authoring grammar**:

- `file-system-object` says: directories are classes, UPPERCASE files are interfaces.
- `yaml-jazz` says: inside those interface files, comments are first-class semantic carriers.

Together they turn an `ls` + `cat` session into a legitimate class browsing experience.

---

## Nesting — Sub-skills and Categorization

Following the grammar, a directory can nest further plurals inside itself:

```
skills/biome/                  ← singular (instance of skill type)
├── SKILL.md                   ← exports SKILL interface
├── CARD.yml                   ← exports CARD interface
├── biomes/                    ← plural: "this skill contains biomes"
│   ├── registry.yml           ← (not UPPERCASE — data, not interface)
│   ├── gateways.yml           ← (not UPPERCASE — data, not interface)
│   ├── convention.yml         ← (not UPPERCASE — data, not interface)
│   └── families.yml           ← (not UPPERCASE — data, not interface)
└── templates/
    └── BIOME/                 ← the template IS named UPPERCASE because it's a TYPE template
        ├── SKILL.md.tmpl
        ├── CARD.yml.tmpl
        └── ...
```

A skill can also contain sub-skills:

```
skills/parent-skill/
├── SKILL.md
├── CARD.yml
└── skills/                    ← plural: sub-skills live here
    └── child-skill/
        ├── SKILL.md
        └── CARD.yml
```

And so on recursively. The grammar holds at any depth.

### Skills as categories

When a skill contains a `skills/` subdirectory, the parent skill plays two roles at once:

1. **It's still a skill itself** (via its own `SKILL.md` / `CARD.yml`).
2. **It's also a CATEGORY** for the sub-skills — the parent directory name is the category name; its child skills belong to that category by virtue of their path.

```
skills/gardening/                    ← the gardening skill AND the gardening category
├── SKILL.md                         ← the parent skill's full protocol
├── CARD.yml
└── skills/                          ← sub-skills (i.e., members of the gardening category)
    ├── composting/
    │   ├── SKILL.md
    │   └── CARD.yml
    ├── pruning/
    │   ├── SKILL.md
    │   └── CARD.yml
    └── seed-starting/
        └── SKILL.md
```

No separate "category" concept is needed — **the parent skill IS the category**. A sub-skill participates in the category simply by living under `skills/<parent>/skills/<child>/`. Cross-category sub-skills (a skill that belongs to two categories) are handled by DOP inheritance, not by duplicating directories: `child-skill` lives in one canonical path, and other categories reference it via `inherits:` chains.

**When to nest vs flatten.** Put a skill under a parent when:

- It's only meaningful inside the parent's context (e.g., `biome`'s `biomes/` stubs — each stub is only a reference biome for this mother skill).
- It's a sub-concern of the parent that isn't reused elsewhere yet.

Pull it up to a top-level skill (lift it) when:

- It becomes reusable across unrelated contexts.
- Other skills start wanting to inherit from it.
- Its audience broadens beyond users of the parent skill.

This is the same PLAY-LEARN-LIFT arc applied to skill hierarchy: sub-skills start nested (low-cost), get promoted when they earn independence.

---

## Empathic Templates — `FOOBAR.yml.template` Files

A **plural container directory** `foobars/` often ships with a companion file `FOOBAR.yml.template`. This is an **empathic template** — a template that anticipates what the author of a new instance needs and carries that guidance inline.

### Shape

```
foobars/                            ← plural container
├── README.md                       ← explains what foobars are and how to add one
├── FOOBAR.yml.template             ← empathic template (UPPERCASE because it declares the FOOBAR type)
├── foobar-alice/                   ← instance: created by copying the template
│   ├── FOOBAR.yml                  ← filled-in marker file
│   └── README.md
└── foobar-bob/
    └── FOOBAR.yml
```

### What makes a template "empathic"

An empathic template does three things an ordinary template doesn't:

1. **Explains itself inline.** Comments alongside every section say what the section is for, what typical values look like, what trade-offs to consider, and when to leave it blank.
2. **Ships with sensible defaults.** Fields carry default values that work for the most common case. The author can **omit defaults they don't need to override**, not just copy-and-edit.
3. **Separates meta-commentary from payload.** Blocks of explanation are clearly marked (`# [INSTANTIATE: strip this section]` or a `# --- meta ---` banner) so the author knows what to delete when finishing the instance.

### Instantiation protocol

To create a new instance `foobar-<id>`:

1. **Copy** `FOOBAR.yml.template` → `foobars/foobar-<id>/FOOBAR.yml`.
2. **Fill in** required fields (values marked `# REQUIRED` or similar).
3. **Override defaults only where you differ** — you can delete default-valued keys entirely; the template documents them so the instance file can stay minimal.
4. **Strip the meta-commentary** blocks. The instance is production documentation, not the template.
5. **Keep the YAML comments that add authorial voice** (per `yaml-jazz`). Comments explaining "why THIS instance is set up this way" are valuable and should stay. Comments of the form "← replace with your value" are meta-commentary and should go.

### Worked example

**Template file** `foobars/FOOBAR.yml.template`:

```yaml
# FOOBAR.yml.template — empathic template for foobar instances
# Copy this to foobars/<your-foobar-id>/FOOBAR.yml, fill in REQUIRED
# fields, override defaults if you need to, delete this banner.
# See foobars/README.md for the full instantiation recipe.

foobar:
  id: my-foobar                      # REQUIRED — kebab-case; must be unique within foobars/
  name: "My Foobar"                  # REQUIRED — human-readable title

  # OPTIONAL — defaults listed here; OMIT if you're fine with the default.
  flavor: standard                   # default: standard (options: standard, spicy, plain)
  region: auto                       # default: auto (detects from ambient context)
  enabled: true                      # default: true

  # REQUIRED — this one has no reasonable default; every foobar differs.
  owner: null                        # e.g. "team-web"; pick an owner
```

**Filled instance** `foobars/foobar-alice/FOOBAR.yml` — written minimally, keeping only fields that differ from defaults or are required:

```yaml
# FOOBAR.yml — alice's foobar
# Spicy flavor for the summer festival use-case; otherwise default.

foobar:
  id: alice
  name: "Alice's Festival Foobar"
  flavor: spicy
  owner: team-festivals
```

Notice what the instance **left out**: `region`, `enabled`, and the template banner. Those use defaults and get inherited implicitly at read time.

### Defaults resolution

A reader (human or LLM) merges the template's defaults with the instance's overrides:

```
effective foobar = defaults_from(FOOBAR.yml.template)
                   ∪ fields_from(FOOBAR.yml)        # instance wins on conflict
```

This is Self-style prototype delegation applied to templates: the template is the prototype, the instance inherits from it. It composes naturally with DOP — the prototype chain for a foobar instance is `instance → FOOBAR.yml.template → biome/skill/whatever contains foobars/`.

### Why templates are declared UPPERCASE

`FOOBAR.yml.template` is UPPERCASE-prefixed because it declares the **type** of the things that go in `foobars/`. Same grammar as `BIOME/` (the directory-scaffold template in `skills/biome/templates/`) — the UPPERCASE names say "this is a type-level artifact, not a content file."

Two flavors of template in common use:

| Template shape | Example | When to use |
|---|---|---|
| Single-file template | `FOOBAR.yml.template` or `FOOBAR.md.template` | Instance is a single file, or a directory with one marker file plus trivial extras |
| Directory scaffold | `templates/FOOBAR/` containing `FOOBAR.yml.tmpl`, `README.md.tmpl`, etc. | Instance is a multi-file directory with several interfaces (e.g., a full skill with SKILL + CARD + GLANCE + README) |

Both are valid. Use single-file when the instance is essentially one YAML document; use directory-scaffold when the instance exports multiple interfaces.

### Templates as proto-skills

An empathic template is often the **larval form of a skill**. If the template starts getting used across unrelated contexts — different parent skills, different repos, different domains — **lift it** to a standalone skill:

```
Before:                                              After:
moollm/skills/biome/biomes/FOOBAR.yml.template  →    moollm/skills/foobar/
                                                     ├── SKILL.md
                                                     ├── CARD.yml
                                                     ├── GLANCE.yml
                                                     └── templates/
                                                         └── FOOBAR.yml.template
```

The consumers that used the template in place switch to `inherits: [foobar]` and use the lifted skill's template directory. Same PLAY-LEARN-LIFT arc that governs skill promotion — applied here to templates. A template that stays nested is one that hasn't yet earned the move.

### Enumeration skip rules

Smart enumeration of a plural directory `foobars/` should **skip** metadata and template files — they're not instances. Per the grammar:

| Filename pattern | Treat as |
|---|---|
| `README.md`, `INDEX.md`, `INDEX.yml`, `ROOM.yml` at container root | metadata (skip in enumeration) |
| `*.yml.template`, `*.md.template` | empathic template (skip) |
| `*.yml.tmpl`, `*.md.tmpl` | scaffolding template (skip) |
| `*.yml.prototype`, `*.md.prototype` | prototype (skip) |
| Any other entry with the expected UPPERCASE marker at its root | instance |
| Any other entry **without** the expected marker | auxiliary (skip or warn) |

A smart `queryInterface(dir, FOOBAR)` returns null for any of the skipped entries — they declare *how to make* foobars, not *a foobar*.

---

---

## The Branch-as-Object Connection

Git branches are directories-with-history. The grammar extends:

```
Branch ALERT_42 in leela-ai/leela-alerts:
├── ALERT.yml                  ← "this branch exports the ALERT interface"
├── README.md                  ← "I have a human landing page"
└── attachments/
    └── screenshot.png
```

The branch's root directory implements the `ALERT` interface, declared by `ALERT.yml`. The branch NAME (`ALERT_42`) encodes both the interface name (`ALERT`) and the instance id (`42`). Full protocol at [`central/skills/github/protocols/branch-as-object.md`](../../../central/skills/github/protocols/branch-as-object.md).

This is the same grammar operating in git-branch space instead of filesystem space. The rules don't change; only the storage backend does.

---

## Examples from the MOOLLM and Leela Ecosystems

### Example 1: A MOOLLM skill

```
moollm/skills/adventure/
├── SKILL.md                   ← exports SKILL
├── CARD.yml                   ← exports CARD
├── GLANCE.yml                 ← exports GLANCE
├── README.md                  ← exports README
├── examples/                  ← plural: contains adventure examples
│   └── adventure-4/           ← singular: an adventure instance
│       ├── ADVENTURE.yml      ← exports ADVENTURE (this IS an adventure)
│       ├── characters/        ← plural: contains characters
│       ├── pub/               ← singular: a room named "pub"
│       └── sessions/          ← plural: contains session instances
└── templates/                 ← plural: contains templates
```

Everything parseable by the grammar.

### Example 2: A schemapedia mechanism plugin

```
moollm/skills/schema/schemas/mechanisms/json-schema/
├── MECHANISM.yml              ← "I export the MECHANISM interface — I am a registered schema mechanism"
└── README.md                  ← "I have a human landing page"
```

Two interfaces, two marker files. That's the entire class.

### Example 3: A Leela biome

```
central/skills/gcs/
├── SKILL.md                   ← exports SKILL
├── CARD.yml                   ← exports CARD (declares biome: true + inherits: [biome])
├── GLANCE.yml                 ← exports GLANCE
├── README.md                  ← exports README
├── recipes/                   ← plural: contains recipes
├── instances/                 ← plural: contains instances
│   └── leela-zion2-dev-0/     ← singular: a project-instance
│       └── ...                ← (content TBD as the instance grows)
├── gotchas/                   ← plural: contains gotchas (each a .md file)
│   ├── README.md              ← index
│   ├── boot-disk-family-mismatch.md
│   ├── blackwell-open-driver.md
│   └── ...
└── ...
```

### Example 4: A character in an adventure

```
moollm/skills/adventure/examples/adventure-4/characters/bartender/
├── CHARACTER.yml              ← "I export the CHARACTER interface — I am a character"
├── README.md
└── memory/                    ← plural: contains memories
```

---

## Practical Reading Protocol

When you encounter an unfamiliar MOOLLM or biome directory:

1. **`ls`** — look for:
   - Plural-named subdirectories (they're typed containers)
   - UPPERCASE marker files (they declare what this directory IS)
2. **Collect the exports.** `ls <dir>/[A-Z]*` gives you the interface list.
3. **For each export, read the marker file** at the appropriate resolution:
   - `GLANCE.yml` first if present (relevance check)
   - Then `CARD.yml` if you need the sniffable interface
   - Then `SKILL.md` / `MECHANISM.yml` / etc. for the full protocol
4. **For each plural subdirectory, descend** — each of its children is a typed instance (probably with its own marker files).
5. **For each singular subdirectory without a marker file**, it's auxiliary — not an instance, just organized content.

This is fast. It works at any depth. It scales from a 4-file skill to a 100+ directory tree.

---

## Practical Authoring Protocol

When creating a new directory:

1. **Decide: container or instance?**
   - Container of type T → name the directory `<T-plural>/`
   - Instance of type T → name the directory singularly (id-form), add `T.<ext>` marker file at its root
2. **Decide: which interfaces does this instance export?**
   - For each interface you want to export, create a UPPERCASE marker file:
     - `SKILL.md` for a skill
     - `CARD.yml` for a card
     - `GLANCE.yml` for a glance
     - `README.md` for human landing
     - Your own `FOO.md` / `FOO.yml` for a new interface you're introducing
3. **Do not register.** There's no registry to update. The marker file IS the registration. (Unless you're in a skill like `schema` or `biome` that maintains a cross-cutting registry — then yes, update that registry to point at your new instance, same as any member.)
4. **Inherit if appropriate.** In `CARD.yml` and/or `GLANCE.yml` and/or `SKILL.md` frontmatter, declare `inherits: [parent-skill]` to participate in DOP delegation.

---

## Interaction with Other MOOLLM Concepts

| Concept | How it uses this grammar |
|---|---|
| **[skill](../skill/)** (meta-skill) | SKILL.md + CARD.yml + GLANCE.yml + README.md as UPPERCASE interface exports; `skills/` as plural container |
| **[card](../card/)** | CARD.yml is the canonical UPPERCASE marker for the card interface |
| **[prototype](../prototype/)** — Self-style inheritance | PROTOTYPES.yml is an UPPERCASE marker for the delegation chain; `inherits:` in CARD.yml is the declarative equivalent |
| **[schema](../schema/)** (schemapedia) | `mechanisms/<id>/MECHANISM.yml` uses exactly this grammar — MECHANISM.yml at root declares the mechanism interface |
| **[self](../schema/schemas/mechanisms/self/)** mechanism | Self-style prototypes and message reception applied to directories |
| **[room](../room/)** | rooms ARE directories; characters / items / scripts are contents; ROOM.yml or ROOM.md (if one exists) marks the directory as a room |
| **[adventure](../adventure/)** | Hierarchical nesting: adventures contain sessions, sessions contain rooms, rooms contain characters, characters contain memory. Every level uses the grammar. |
| **[yaml-jazz](../yaml-jazz/)** | UPPERCASE YAML marker files are all YAML Jazz — structured YAML where comments + structure both carry meaning |
| **DOP** ([delegation-object-protocol.md](../skill/delegation-object-protocol.md)) | PROTOTYPES.yml is the ordered prototype stack declaration; first-match-wins resolution walks the directory tree guided by this grammar |
| **Branch-as-object** (leela-ai/leela-alerts `Issue_<id>` pattern) | Same grammar, git-branch storage backend. The branch root directory implements an interface declared by an UPPERCASE marker file. |

---

## Edge Cases & FAQs

### Q: What if a directory has no UPPERCASE marker files?

Then it exports no interfaces under this grammar. It's "just a directory" — maybe organizational (a subfolder of recipes, an index), maybe auxiliary (a `tmp/` scratch dir, a `snapshots/` archive). Parse accordingly.

### Q: What about `README.md`? It's UPPERCASE.

`README.md` declares that this directory exports the README interface — i.e., "I have a human-readable landing page." This is the lightest possible interface; nearly every MOOLLM directory exports it.

### Q: What if the marker is in a subdirectory instead of the root?

Then the **subdirectory** is the exporter, not the parent. Marker files apply to their enclosing directory only. `skills/gcs/gotchas/README.md` declares that `gcs/gotchas/` has a README, not that `gcs/` has a README.

### Q: What if I see `.foo/` instead of `foo/`?

Dotfiles / dotdirs are hidden by convention (tools often skip them by default). Treat them as biome-specific configuration, not as interface exports. `.github/` workflows is a good example.

### Q: Is `Dockerfile` or `Makefile` an interface marker?

By our grammar, yes — they're ALLCAPS / CamelCase marker files declaring that the directory exports a build interface. This existed long before MOOLLM; we're codifying a pre-existing convention. Same applies to `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`.

### Q: What's the difference between `skills/` and `biomes/`?

At the filesystem-object-grammar level, nothing — both are plural containers declaring element type. The difference is semantic (skills are any MOOLLM skill; biomes are platform-descriptor skills that additionally inherit from the `biome` mother skill). The grammar is agnostic to domain; the `inherits:` chain carries the type refinement.

### Q: Can one file export multiple interfaces?

Convention: no. One file → one declared interface. If you want to export two, create two files. (Internally, a marker file may reference or include another, but each file's root existence is one declaration.)

### Q: What about file-as-object, not just directory-as-object?

For content files (recipes, gotchas, runbooks, protocols), the plural parent dir declares the type; the file itself is the instance. Interface marker is implicit (the filename + parent-dir-type). This is the lighter form of the grammar — directories get rich multi-interface treatment, content files get one-type-per-plural-container treatment.

---

## Why This Matters

Without an explicit grammar:

- Newcomers read MOOLLM directory trees as undifferentiated file piles.
- LLMs navigate by keyword matching instead of type-aware traversal.
- Authors reinvent conventions per skill; inconsistencies accumulate.
- Cross-references break when directories restructure.

With the grammar:

- A 5-second `ls` reveals what every directory IS and CONTAINS.
- Interfaces are discoverable without registries, IDE plugins, or documentation scavenger hunts.
- Authors add new interfaces by dropping a marker file; consumers discover by globbing.
- Refactors are local — move a directory, and its interface exports move with it.

The grammar is the file-system analog of COM's big insight ("multiple interfaces per class is the right abstraction") — plus a human-readable naming scheme instead of UUIDs, plus the `ls` tool as a free type-checker.

---

## Historical Lineage — Where This Came From

This grammar did not appear from nowhere. The ideas it combines have been circling since the 1970s; MOOLLM is stapling them onto filesystems and LLM-legible contexts specifically. Oldest first:

**Smalltalk** (Xerox PARC, 1970s). Alan Kay et al. Classes and instances, message passing as the primitive mechanism, the image-as-object idea (your entire state is an object you can dump and reload). The spirit of "every thing is a kind of thing" lives here. MOOLLM's "directories are classes" reads as a Smalltalk image with the filesystem as the serialization.

**Self** (Ungar & Smith, 1987). The prototype revolution — you don't need classes, just objects that delegate to parent objects. The delegation chain IS the type. MOOLLM's `inherits:` and `PROTOTYPES.yml` come directly from Self. Schemapedia's `self` mechanism profile has the full retrospective; the `prototype` skill is the MOOLLM-internal transmission of Self's ideas.

**NeWS — Network extensible Window System** (James Gosling & David S. H. Rosenthal, Sun, 1986). PostScript-based window system. Lightweight prototype delegation proved in production system software, years before Self became widely known. NeWS dictionaries were Self-style objects before Self had a user base. The fact that you could build a full window system this way was the proof that prototype-based OO wasn't just a research curiosity.

**TNT — The NeWS Toolkit** (Owen Densmore & David S. H. Rosenthal, Sun, late 1980s). A class hierarchy *on top of* NeWS's prototype foundation — widgets, UI components, message dispatch — organized by convention-naming that made class identity and inheritance legible as a tree. The patent Densmore and Rosenthal filed around this work is the direct conceptual ancestor of "treat the file system as an OO class hierarchy." MOOLLM's UPPERCASE-marker-file grammar is the filesystem-scoped reading of ideas TNT proved out at the widget level.

**COM** (Microsoft, mid-1990s). Multiple interfaces per implementation class — the single idea MOOLLM borrows most directly in the "UPPERCASE marker file = exported interface" rule. `QueryInterface(IID_IFoo, &ptr)` maps to `test -e <dir>/FOO.md`. The UUIDs were COM's great mistake (opaque, registry-bound, Windows-centric); MOOLLM swaps them for UPPERCASE filenames.

**XPCOM** (Mozilla). Cross-platform COM; the "how to COM right" / "how COM went wrong" retrospective. Schemapedia's `com-xpcom` mechanism has the fuller history.

**Ted Nelson — intertwingularity** (Project Xanadu, 1960s+). Explicit cross-reference is the primary mode. Filesystems work when cross-references are first-class navigation targets, not annotations on the side. MOOLLM's relentless cross-linking inherits this ethos.

**MOOLLM DOP** ([`../skill/delegation-object-protocol.md`](../skill/delegation-object-protocol.md)). Formalized Self-style delegation for LLM-read-able filesystems. `PROTOTYPES.yml` is an interface export under the grammar this skill names; DOP is the resolution algorithm that uses the grammar.

**MOOLLM branch-as-object** (`leela-ai/leela-alerts` Issue_<n> / ALERT_<n> branches). Extends the grammar from filesystems to git branches — the branch's root directory declares its implemented interface via an UPPERCASE marker file. See [`central/skills/github/protocols/branch-as-object.md`](../../../central/skills/github/protocols/branch-as-object.md).

What MOOLLM adds to this long conversation:

- LLM-legibility (the grammar is `ls`-readable and grep-friendly; no parser needed)
- Semantic Image Pyramid (GLANCE → CARD → SKILL → README as a multi-resolution reading order)
- YAML comments as first-class semantic data (yaml-jazz)
- Hierarchical nesting (`<plural>/<singular>/<plural>/<singular>/...`) natural and unbounded
- Branch-as-object extension (git history as part of the object's timeline)

---

## See Also

- [`skill/SKILL.md`](../skill/SKILL.md) — MOOLLM meta-skill; uses this grammar to define what a skill IS
- [`skill/delegation-object-protocol.md`](../skill/delegation-object-protocol.md) — DOP; PROTOTYPES.yml is an interface export under this grammar
- [`skill/skill-instantiation-protocol.md`](../skill/skill-instantiation-protocol.md) — how a skill prototype creates instances; the instance path follows this grammar
- [`prototype/SKILL.md`](../prototype/SKILL.md) — Self-style prototypes; directories play the role of objects
- [`card/SKILL.md`](../card/SKILL.md) — the CARD.yml interface
- [`schema/`](../schema/) — schemapedia; every mechanism profile follows this grammar
- [`schema/schemas/mechanisms/com-xpcom/`](../schema/schemas/mechanisms/com-xpcom/) — COM / XPCOM background
- [`schema/schemas/mechanisms/self/`](../schema/schemas/mechanisms/self/) — Self-style prototype mechanism profile
- [`yaml-jazz/`](../yaml-jazz/) — semantic YAML; the serialization style UPPERCASE marker files use
- `central/skills/github/protocols/branch-as-object.md` (if reading from the Leela central repo) — the grammar extended to git branches

### External historical references (if you want the full story)

- **Smalltalk:** *"Smalltalk-80: The Language and its Implementation"* — Goldberg & Robson, 1983. The original vision.
- **Self:** *"Self: The Power of Simplicity"* — Ungar & Smith, 1987 (OOPSLA paper). <https://bibliography.selflanguage.org/>
- **NeWS:** *"The NeWS Book"* — Gosling, Rosenthal & Arden, 1989. <https://en.wikipedia.org/wiki/NeWS>
- **TNT:** Densmore, O. & Rosenthal, D.S.H. *"A user-interface toolkit in object-oriented PostScript."* Computing Systems 3(1), Winter 1990. The paper that laid out the class hierarchy on PostScript NeWS dictionaries; widely cited as the patent-adjacent ancestor of "treat the filesystem as a class hierarchy."
- **COM:** *"Inside COM"* — Dale Rogerson, Microsoft Press, 1997. Or Don Box's *"Essential COM"*, 1998 — both are where "multiple interfaces per class" got popular.
- **Intertwingularity:** Ted Nelson, *"Computer Lib / Dream Machines,"* 1974.

---

*Directories are classes. UPPERCASE files are interfaces. Plurals declare type. YAML is preferred, comments encouraged. The filesystem is the registry.*
