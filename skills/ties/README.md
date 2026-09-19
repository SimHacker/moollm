# ties 🪢

**Reading order:** [GLANCE.yml](GLANCE.yml) → [CARD.yml](CARD.yml) → [SKILL.md](SKILL.md) → this file.
The schema is [TIES-SCHEMA.yml](TIES-SCHEMA.yml), the ladder is [RUNGS.yml](RUNGS.yml), and
[TIES.yml](TIES.yml) is this directory described by the file type it defines.

This is the *why* level. The protocol is in SKILL.md; what follows is where the ideas came from and
which of them are owed to whom.

## This is Ben Shneiderman's idea, and the debt is specific

Almost every load-bearing decision in this skill traces to one person and one lab: **Ben Shneiderman**
and the **Human-Computer Interaction Laboratory** at the University of Maryland, which he founded in
1983. Not as general influence — as four particular mechanisms, each of which this file type reuses.

### 1. Embedded menus, and the mandatory definition

**HyperTIES** — The Interactive Encyclopedia System — grew out of Shneiderman's work on *embedded
menus* (Koved and Shneiderman, CACM 1986): the radical proposal that a link should live **inside the
running prose**, highlighted in place, rather than in a separate list of destinations. The name is the
activation. That is now so ordinary it is invisible, and it was a research claim that had to be argued
and measured.

HyperTIES then added the part the web did not keep. **Every article was required to carry a short
definition**, and a single click showed it; a double click followed the link. The reader could ask
*should I go there* and get an answer costing a paragraph rather than a page.

The surviving archive census is in
[`../../designs/webtop/hyperties/ARTICLE-SCHEMA.md`](../../designs/webtop/hyperties/ARTICLE-SCHEMA.md),
and it is a receipt rather than a recollection. **The article has exactly four parts**, because the
formatter aliases the second spellings to the same FORTH word — `alias .description .definition`,
`alias .synonym .synonyms`, `alias .content .contents` in `fmt.f` — so counting the spellings
separately invents fields that never existed:

| Field | Uses | Spellings | What it was |
|---|---|---|---|
| `.title` | 254 | — | canonical name, one per article, the index's *principal* |
| `.definition` | **246** | `.definition` + `.description` | the mandatory abstract shown on single click |
| `.target` | 187 | — | arbitrarily-shaped live regions: embedded menus inside pictures |
| `.synonyms` | **136** | `.synonyms` + `.synonym` | every alias that resolves to this article |
| `.contents` | 118 | `.contents` + `.content` | the body |

264 storyboards, **246 carrying a definition, 136 declaring synonyms.** The schema was the working
discipline, not an aspiration, because the authoring tool refused to let an article exist without one.

### Resolution is one mechanism over three namespaces

Weiland's index manager indexes **documents, pictures and targets** in parallel — `struct index
*documents, *pictures, *targets` is the whole of `MASTER_INDEX` — so a name in prose resolves to a
storyboard, a picture, or a target, where a target is an arbitrarily-shaped live region inside a
picture: **an embedded menu with pop-up shapes, an applet addressed by name.** One namespace
mechanism, three kinds of destination, and the prose does not have to know which it got.

Aliasing is in the index's shape rather than layered on top of it — `n_principals` counts titles,
`n_entries` counts titles plus synonyms — which is why resolving a synonym costs exactly what
resolving a title costs. And the master index is itself a generated article carrying the synonym
`!index`, so the index lives inside the encyclopedia it indexes.

Don Hopkins built the NeWS implementation, the pie menus, and the Emacs-based authoring tools —
see [`TEAM.md`](../../designs/webtop/hyperties/TEAM.md). The synonym mechanism is why a link in prose
could be any alias and still resolve, and the reason `synonyms:` is in this schema at all.

### 2. Treemaps: the same lab, the same tree, and a weight on every node

In 1990, one floor of the same building, Shneiderman got annoyed at a full disk. In his own words from
the [HCIL treemap history](http://www.cs.umd.edu/hcil/treemap-history/):

> During 1990, in response to the common problem of a filled hard disk, I became obsessed with the idea
> of producing a compact visualization of directory tree structures. Since the 80 Megabyte hard disk in
> the HCIL was shared by 14 users it was difficult to determine how and where space was used.

And the diagnosis, from HCIL TR 91-03, which is **exactly the complaint this skill exists to answer**:

> Most operating systems display the contents of one node at a time with names of the files and
> subdirectories or icons to represent them. [...] even elegant tree-like layouts of the hierarchical
> structures [...] soon overwhelm the available display space and **users cannot grasp the entire
> picture.**

That is `ls`, described in 1991. One node at a time, names only, no way to see the whole. The treemap
answer required one thing of the data: *"Treemaps require that a weight be assigned to each node."*

So the `cost:` field on every `inside[]` entry is a treemap weight. Same lab, same directory tree, same
question — **what is big here, and where should I not go** — with the scarce resource changed from
screen space and disk blocks to context tokens. The recursive slice-and-dice algorithm took Shneiderman
a few days and six lines; naming it took longer. (HCIL TR 91-03, March 1991; Johnson and Shneiderman,
IEEE Visualization, October 1991; ACM TOG 11(1):92–99, January 1992.)

### 3. The mantra is the rung ladder

> **Overview first, zoom and filter, then details on demand.**
>
> — Shneiderman, ["The Eyes Have It: A Task by Data Type Taxonomy for Information
> Visualizations"](https://ieeexplore.ieee.org/document/545307), 1996

One sentence that designed a field, and [RUNGS.yml](RUNGS.yml) is that sentence applied to a
filesystem. `glyphs` and `label` are the overview. `definition` plus the per-child costs are zoom and
filter. `description` and `body` are details on demand — *on demand* being the load-bearing half, since
the whole point is that you did not pay for them while deciding.

Nothing here improves on the mantra. The contribution is only that a directory can now answer it.

### 4. Measure the interface

The rule Shneiderman's lab actually enforced was empirical: **don't argue about interfaces you could
measure.** The CHI'88 pie menu paper exists because HCIL tested menus rather than theorising about them
— Callahan, Hopkins, Weiser and Shneiderman, which is to say Don measured pie menus with Ben.

That is why this skill's numbers are measurements rather than opinions, and why one of them changed
within an hour of being written. `BUDGET_HUB` was set to 2 KB by guess. Three real manifests later — a
415-byte inheriting leaf, a 1397-byte pile prototype, a 2755-byte nine-child skill root with nothing
redundant left in it — it was clear the guess punished *breadth* rather than chattiness, because a
hub's bytes are mostly `inside` entries at roughly 100 each. It is 3 KB now, on evidence.

See [`../design-sense/masters/ben-shneiderman.md`](../design-sense/masters/ben-shneiderman.md) for the
votes and vetoes in loadable form.

## What the web dropped

The web kept embedded links and threw away the definition. Forty years on, the most admired feature of
[gwern.net](https://gwern.net) is link popups that preview a destination before you commit to it —
which is HyperTIES' single-click summarise, **rebuilt by hand, per link, as annotations.** Gwern's
engineering is excellent and the labour is enormous, and it is labour HyperTIES did not have to spend,
because a schema that requires a definition gets one for every article for free.

This skill's wager is that the requirement is cheap again now for a different reason: an LLM can draft
the definition, so *required* never has to mean *blocked*. Mark it in `provenance.generated`, let a human
confirm it, and the rung exists.

## Why a filesystem needs this at all

Stephen Kell, [*The operating system: should there be one?*](https://doi.org/10.1145/2525528.2525534)
(PLOS'13), diagnoses the general case. Unix and Plan 9 unified everything around the file, and as the
abstraction absorbed more uses its semantics got vaguer — what does the size of a control file mean?
Can `cp` snapshot a process tree? His conclusion:

> Unlike in Smalltalk, semantic diversity is not accompanied with any meta-level descriptive facility
> analogous to classes.

TIES.yml is that facility, retrofitted, in-band. And in-band is not a compromise: **git does not store
extended attributes**, so a tree entry is a path, a blob hash and a mode, and any metadata scheme that
must survive a clone has no other option.

Which makes **US 5,187,786** the encouraging precedent — Owen Densmore and David S. H. Rosenthal, Sun,
filed 1991, expired 2011. A full object class hierarchy in a plain hierarchical filesystem: classes as
directories, methods as files, instances as directories of variable files, the inheritance chain held in
a **path file** used as a dictionary stack, with `Self` and `Super`, and explicitly *"without requiring
additional file attributes."* If a class system fits that budget, a screening layer certainly does.
Both authors are in the WWSFF cast, and both came out of the NeWS/PostScript world where the dictionary
stack *is* the dispatch mechanism.

The full argument, including Pike's Plan 9 anecdote and Kell's correction to it, is
[`../../designs/korz/repo-as-everything.md`](../../designs/korz/repo-as-everything.md).

## Decisions, and what forced each one

Recorded because the evidence is more useful than the conclusion.

**It screens, it does not advertise.** The first draft made TIES.yml a scoring engine — the Sims'
Find Best Action over a corpus. That was an overreach: advertisements are declared in `CARD.yml` with
their own grammar of triggers, conditions and scores. A screen reports presence, cost, staleness, and
*whether a richer declaration exists at all.* The one idea kept from the Sims is that usefulness is a
delta against what the reader already has, which is why a hint names the condition under which its value
collapses instead of just its size.

**Carry only what is not derivable.** The first real manifest claimed 37 lenses, 36 methods, 62 masters
and 9 seeds. The truth was 35 / 34 / 60 / 7 — the numbers were `ls | wc -l`, counting each pile's own
`CARD.yml` and `GLANCE.yml` as members, so every pile overcounted by exactly two. A **wrong formula
refreshed on schedule keeps producing the same wrong answer, on time, forever**, which is why that is a
different failure from ordinary staleness. The same audit found six files in one repo claiming those
counts with no two agreeing, two of them loaded into every session. Hence: redundancy is a cache, legal
only when declared and recomputable; undeclared duplication is a fork.

**Organelles, not core growth.** Foreign schemas arrive by endosymbiosis — engulfed whole under `x:`,
keeping their own genome, with the host validating the membrane and never the contents. Dublin Core gets
no special status, which is the claim: standard and experimental guests differ in age and adoption, not
in kind. Alan Kay's recollection of thinking of objects as "biological cells and/or individual computers
on a network" is the framing, and the cell is the load-bearing half, not the network.

**Prototypes, because redundancy scales with file count.** Siblings sharing a creator, a language and a
type is the duplication that actually dominates a corpus. `inherited:` in the pile, `proto:` in the
child, and lists replace rather than append — because append makes a child's meaning depend on a parent
it does not show you, and a reader scanning a hundred files cannot hold the chain.

**Sidecars selectively.** A member earns `<subject>.TIES.yml` when it has synonyms that must resolve,
ties an index line cannot carry, its own glyphs, or references from outside its pile. Generating one per
member produces files whose entire content is `proto:` plus a name already on disk as the filename.

**Glyph contrast is per pile, not per type.** The rule first demanded that all skills share a leading
emoji, which is wrong: a skill is addressed by name and rendered alone, so its first glyph is its most
identifying byte, and 150 of them cannot be distinguished after a shared prefix. A pile of 35 lenses is
the opposite — read as a set, in one menu, where a shared lead means *same kind of thing.*

## What is not built

- **Nothing writes.** `ties_lint.py` is a pure reader. The comment-preservation requirement is therefore
  currently guaranteed by the absence of writers rather than by tooling: `ruamel.yaml` is not installed
  here, and the first tool that wants to write must add it and assert byte-identical round-trip on a
  commented file as its own first test.
- **No `keywords` field, and the placement question is open.** Whether free-text retrieval terms belong
  in the screen, and whether `tags:` is doing classification and search badly at once, is recorded
  unresolved in `TIES-SCHEMA.yml` → `placement_experiments`. Nothing was deleted to settle it.
- **Activation hints have no home.** A structural waypoint has no CARD and never will, so either the
  screen grows a light activation field or waypoints stay unactivatable. Waiting for a case where it
  bites.
- **Shadowing is reported, not resolved.** A nearer scope shadowing an enclosing one is legal and gets a
  warning. The 1988 tool refused duplicate claims within a namespace and checked only the top index; the
  shadowing half is what it left unbuilt, and so is this.
- **`cross` ties are not yet bidirectional in practice.** The relation means a cross-tie — a railroad
  tie holding two rails at gauge, across the grain — but nothing generates the backlink. That is the
  limitation HyperTIES had and the web shipped with.

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[repo README](https://github.com/SimHacker/moollm/blob/main/README.md) and
[skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md).
Kin skills: [yaml-jazz](../yaml-jazz/) (the notation, where comments are data),
[design-sense](../design-sense/) (first dogfood, and the masters shelf),
[k-lines](../k-lines/) (`~name~` resolution and scope walking),
[postel](../postel/) (accept messy, emit clean, ask when ambiguous),
[robust-first](../robust-first/) (an unknown organelle degrades to preserved-and-reported).
