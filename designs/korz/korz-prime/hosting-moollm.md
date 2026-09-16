# Hosting Korz′ on MOOLLM — soups intertwingled with objects

*Part of the [Korz cauldron](../README.md). The
[design](README.md) specifies the semantics; this is the integration
story — how Korz′ runs on
[MOOLLM](https://github.com/SimHacker/moollm)'s way of reading a git
repository, with no new engine and no IDE.*

## The hosting move, one level up

David prototyped Korz **in Self** — an interpreter, debugger, and
partial IDE hosted on the Self language, VM, and environment. MOOLLM
**is** Self on the filesystem: directories as prototypes, slots as
files, `parents:` / `inherits:` as ordered delegation, clone as
`cp -r`, reflection as `ls`. So the hosting question isn't "can we
build a Korz VM beside MOOLLM?" — it's "can MOOLLM host the same
Korz-in-Self move one level up, with the filesystem as the substrate
instead of the Self heap?"

Yes — and the asymmetry from [korz-notes](../korz-notes.md) says it
should be *cheap*: Korz-in-Self took machinery; Self-in-Korz takes
only restraint (guard every slot on `rcvr` alone and you're writing
Self). MOOLLM's selfish object system is exactly that restraint —
**a one-dimensional Korz system**. The paper's spectrum runs from
procedural (zero dimensions) through single-receiver OO (one) to full
Korz (N). MOOLLM sits at dimension one: the receiver is the
directory path; lookup walks the parent list; first match wins. Add
guards on more dimensions and you've opened the sea without leaving
the repo.

So Korz soups and MOOLLM objects **intertwingle in place** — same
files, same
[yaml-jazz](https://github.com/SimHacker/moollm/tree/main/skills/yaml-jazz)
syntax, same big-endian naming (`2026-01-24-description.yml`), same
git history as the time dimension — dual-readable:

| Reading | What the filesystem is | Dispatch |
|---|---|---|
| **Self / MOOLLM** | Tree of prototypes | Send to path; walk `parents:`; first slot wins |
| **Korz** | Sea of slots | Send + implicit context; specificity lattice |

A `CHARACTER.yml` in the Self reading is prototype metadata and
shared state. In the Korz reading the *same directory* is a bundle of
guarded slots — and every file under it may carry more slots for other
selectors. Directory address supplies default coordinates
(`world: zork` because the file lives under `worlds/zork/`); moving
the file re-guards it. The tree isn't abolished; it's **one saved
view** among many the Korz dispatcher can cut through the sea
([addressing.md](addressing.md) follows that idea to the bottom).

## What is an interface in Korz?

In MOOLLM's
[Directory-as-IUnknown](https://github.com/SimHacker/moollm/blob/main/designs/DIRECTORY-AS-IUNKNOWN.md)
model, an interface is a **queryable facet** — drop `ROOM.yml`,
`CHARACTER.yml`, `SKILL.md` into a directory and QueryInterface finds
it. Inside-out COM: visible state, multiple interface files, shared
directory.

In Korz an interface is a **saved view** — a named cut through the
slot sea, not a container. The paper refused to reify layers in the
language and said the IDE would group slots as needed; an interface is
that grouping made durable. Here is one, declared for the
two-world troll of the [blend example](examples/troll-blend.md):

```yaml
# INTERFACE.yml — Korz facet declaration (same filename, extended semantics)
interface:
  id: gatekeeper
  query: {rcvr: troll*, selector: [BLOCK, DEMAND-TOLL, BRANDISH-AXE]}
  default_context: {world: null}   # bind at query time
  advertisement: |
    Prices an edge. Currency depends on which mind fronts.
```

QueryInterface in the hybrid: "does this directory implement
`gatekeeper`?" → read `INTERFACE.yml` (or infer from slot files) →
bind the declared default context → surface the matching slot group.
Not a vtable — a **subjective projection** with a contract. Multiple
interfaces on one directory share the same files the way COM
interfaces share state; in Korz they share the **sea** underneath.

## What are cards?

In MOOLLM the semantic image pyramid is fixed resolution: GLANCE.yml
→ CARD.yml → SKILL.md → README.md — precompiled views at increasing
depth, each a K-line activation packet. In Korz a **card** is the
same idea wearing guard algebra:

| MOOLLM | Korz |
|---|---|
| GLANCE | Minimal guard + one-line activation ("is this relevant?") |
| CARD | Saved view at medium resolution — methods/advertisements as guarded slots |
| SKILL | Full slot space for that facet — every selector, every guard stance |
| README | Human narrative layer; comments load-bearing in the soft tier |

A character's `CARD.yml` is already both readings at once: Self-side
rarity, methods, and combos_with *and* Korz-side advertisements that
dispatch when `{rcvr: troll*, ...}` matches. The card doesn't own the
character — it **advertises** which slots exist and how to invoke
them from a typical context. Add dimensions to the card's guard and
you've declared which subjective object you're looking at.

**A card is a bundle of Sims advertisements — guarded and scored.**
The advertisement shape is `action` (selector), `condition` (guard),
`score` (weight), `effect` (body). That is a Korz slot with one
addition Korz doesn't have: the **explicit score**. Korz derives
precedence structurally — unique most-specific wins, ties are errors;
The Sims declared it numerically — every object advertises scored
actions, every Sim re-weights the scores through its own needs and
personality, and dithers among the top few
([worked example](examples/sims-advertisements.md)). So MOOLLM cards
have been doing Korz dispatch all along, on roughly one dimension,
with an **auction instead of a lattice** — which is exactly the
[korz-notes](../korz-notes.md) ASK ("would he buy dispatch as an
auction?") already running in production. The score is where the two
resolution strategies meet: lattice specificity is a score the guard
structure computes; advertisement scoring is a lattice the designer
flattens by hand; the soft tier's relevance sampling interpolates
between them.

## Dropping interface files — accretion, state, pointers

How does dropping `ROOM.yml`, `CHARACTER.yml`, `HTML-RENDERER.yml`
into a directory actually work? **By accretion, with no
registration.** The directory is the object; the filename is the
interface ID; QueryInterface is a stat call — and **`ls` is more
powerful and reflective than QueryInterface ever was. `ls` is a
mirror.** QueryInterface only answers yes or no to an IID you must
already possess — COM never shipped enumeration, so you interrogate
IUnknown by guessing GUIDs you brought from somewhere else. `ls`
inverts the epistemics: the object volunteers its complete manifest,
unprompted, in human-readable names — and since names are K-lines,
each line of the listing is also an activation, which is why
yaml-jazz says the directory listing *is* the advertisement index,
the Sims-style "what's here?". COM's root interface confesses
ignorance (IUnknown: you must already know); the filesystem's root
operation confers knowledge (`ls`: now you know). The object shows
you itself — reflection without registration, introspection for the
price of a syscall. Drop the file in and the object grows a queryable
facet without touching anything that was already there
([Directory-as-IUnknown](https://github.com/SimHacker/moollm/blob/main/designs/DIRECTORY-AS-IUNKNOWN.md)
calls this design by accretion). In the Korz reading, dropping an
interface file **pours new slots into the sea** pre-guarded by the
directory's address coordinates: an `HTML-RENDERER.yml` under
`troll/` arrives already guarded `{rcvr: troll*}`; its own keys add
`{medium: html}`.

**Yes, they carry state as well as declarations** — that's the
inside-out-COM point. COM hid state behind interface methods; MOOLLM
inverts it: the directory is visible state, and the interface file is
both a contract *and* a place to keep the facet's own slots. A
`ROOM.yml` holds exits, contents, and mood (state) next to its
protocol hooks (declarations). COM even has the precedent for facet-
private state: **tear-off interfaces**, created on demand with their
own storage — dropping `HTML-RENDERER.yml` with a `theme:` block is a
tear-off that persists. In Korz terms the distinction dissolves
anyway: state is slots with data bodies, declarations are slots with
guard templates, and both float in the same sea.

**And yes, they point to other files** — pointers are just slots
whose bodies are addresses, and addresses come in two kinds: paths
into the repo and K-lines into latent space
([epistemics.md](epistemics.md): any slot, not just `parents:`, can
hold either). The path idiom is everywhere already: `prototype:` and
`parents:` (delegation), `script:` in CARD methods (behavior lives in
a sibling file), `see_also:` (associative edges). Shared state
between facets is the same move: `ROOM.yml` and `BUSINESS.yml` both
pointing at `inventory.yml` is COM aggregation with the sharing
visible in the open. One worked example, all three at once:

```yaml
# HTML-RENDERER.yml — dropped into troll/; the facet arrives by accretion
interface:
  id: html-renderer
  query: {medium: html}        # + {rcvr: troll*} free, from the address

state:                         # tear-off state, private to this facet
  theme: bridge-gothic
  last_rendered: 2026-08-20    # facet remembers; directory persists it

pointers:                      # slots whose bodies are addresses
  template: ../shared/character-page.tmpl.html
  heads_widget: ./heads-gauge.js   # renders the live fronting weights
  shares: ../CHARACTER.yml         # reads the same soul every facet reads
```

Query it, and the directory answers as an HTML renderer; delete the
file, and that facet of the object simply ceases — no deregistration,
no dangling vtable, and every other reading of the directory
untouched.

The Zork compiler ([case-zork.md](../case-zork.md)) is what turns a
SKILL-level slot space into strict-tier Korz — CARD and GLANCE
survive as the human/LLM-facing views; the compiled sea is what the
VM runs.

## The self-revealing soup

`ls`-is-a-mirror is the static claim; here is the dynamic one: the
slot soup is a **self-revealing interface** in the pie-menu sense
(gesture-space-self-revealing-ui).
A pie menu's display isn't separate from its expert gesture — the
novice's guided walk *is* the rehearsal for the expert's blind
stroke, same motion at different speeds. The soup works identically:
the novice runs `ls`, reads names, descends; the expert types the
full path unprompted. Browsing trains direct address, because the
reveal and the invocation are the same syntax. No mode switch, no
separate command language to graduate into — the menu *is* the
gesture.

And the reveal is **hierarchic both ways at once** — directories and
alphabetical sorting of shared prefixes — because hierarchy in the
soup is *revealed, not imposed*. Sorting adds nothing; it exposes
structure the big-endian names already carry: a flat `ls` of
prefix-clustered names reads as an outline, and `ls -R` is the same
outline played on directories. The two axes are one mechanism at two
temperatures: `/` is the hard separator (crystallized hierarchy —
somebody ran `mkdir`), `-` is the soft one (implicit hierarchy —
nobody had to). A path is a big-endian name whose separators got
promoted; a prefix cluster is a directory that hasn't been mkdir'd
yet; promotion and demotion are ordinary renames, and rename
re-guards, same rule as always. So the sea is flat and hierarchic
*simultaneously* — the hierarchy is just the cheapest saved view
there is, the one `sort` computes for free — which is the
interfaces-are-saved-views doctrine bottoming out in the collation
order of the filename alphabet.

## No IDE required — bootstrapping on bare files and git

Design constraint, stated flat: **this has to work with a normal
filesystem and a git repo, no IDE.** So what about Korz actually
*required* one? Audit the paper's IDE dependencies and almost all of
them turn out to be compensation for the heap — slots lived in an
opaque Self image, so you needed a tool to see them at all. Put the
sea in files and the image is born visible; the residue is semantic,
and the LLM covers it.

| The IDE did | The bare repo does |
|---|---|
| Group slots into objects/layers on demand | Directories, big-endian prefixes, `INTERFACE.yml`/`CARD.yml` — saved views that are *durable and versioned*, where the IDE's were ephemeral |
| Browse and navigate the sea | `ls` is reflection, `glob` is a subtree query, `grep <selector>` is "show every slot for this message"; filenames are K-lines; directory listings are advertisements |
| Answer "what does this code do in all contexts?" | The LLM cuts any subjective plane and narrates it in conversation — no window system required |
| Guard-writing support, ambiguity warnings | The strict compiler's refusal is the linter; `git diff` and PR review are the change protocol; crystallizations reviewed like pull requests |
| Debugging symmetric dispatch (no receiver to follow) | Dispatch traces as plain text committed beside the code; the provenance dimension; blend weights worn as visible state ([troll example](examples/troll-blend.md)); `git bisect` as the time-travel debugger |

The pattern: the Korz prototype inherited its IDE-dependence from its
host — it was built *on the Self environment*, where everything lives
in an image and outliners are how you see. MOOLLM made the opposite
bet and it's load-bearing here: `cat`, `ls`, `grep`, `glob`, and
`git` are the primitive IDE, the yaml-jazz comment channel carries
what tooltips and inspectors carried, and the LLM supplies the one
genuinely semantic service (cross-context comprehension) that Unix
tools can't. That service used to require building an environment;
now it requires a conversation.

So the bootstrap order inverts the paper's: **files first,
conversation second, IDE last** — and when the IDE eventually comes,
it's progressive enhancement generated *from* the same data (GLANCEs
and CARDs are precompiled views; an IDE is just a renderer for saved
views with faster refresh). Nothing in the semantics waits for it.

The open question this raises for David — how much of the prototype's
IDE was Korz needing an IDE, and how much was the Self image needing
a window? — is collected with the others in
[ask-david.md](../ask-david.md).

---

*The runnable proof of concept is planned in
[cauldron.md](cauldron.md); the evaluation ladder is running in
[experiments/korz-eval/](experiments/korz-eval/EXPERIMENT.md).*
