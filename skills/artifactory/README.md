# Artifactory 🏭 — the Engine of Creation

*Deep context. For the protocol, read [SKILL.md](./SKILL.md); for the interface, [CARD.yml](./CARD.yml);
for a glance, [GLANCE.yml](./GLANCE.yml).*

## The one idea

An **artifactory** is an artifact factory — a thing that *makes things* from a description, and
(in the strong form) can make a copy of itself. It is the operational heart of MOOLLM: the engine
that turns a spec into a durable, versioned artifact, edits it, reproduces it, and — deliberately,
reversibly — destroys it.

It is unusual because it lives at two levels at once:

- **Abstract**, like `lambda`: a universal operator you can apply to anything. A skill is a
  function; instantiating it is application; construction is evaluation.
- **Concrete**, like *Ubik*: an actual can of spray you point at a decaying reality to rebuild
  it — files on disk, commits in git, a repo you can walk through.

Class **and** instance. Instructions **and** data **and** graphics. That triple — *the axis of
eval* — is the whole trick: the same artifact is a program on one pass, data on the next, a
picture on the third, and the artifactory is what slides it along the axis.

## Why "artifactory" and not "generator"

A generator only creates. This engine also **edits, upgrades, monkey-patches, reboots, persists,
reproduces, and destroys** — the full lifecycle. And it does all of it **on a timeline**: git is
not an afterthought but the substrate. Branches are experiments, merges are decisions, PRs are
proposals, issues are requests, discussions are deliberation. Construction *is* history.

The name is also a deliberate pun on **JFrog Artifactory**, the real-world binary/artifact
repository manager. The joke lands: a store that both holds and serves what your builds produce.

## The lineage, in one breath

- **von Neumann** proved a machine can read a tape, build the machine it describes, and copy the
  tape — self-reproduction without magic (the 29-state cellular automaton; also a kinematic model).
- **Lem's Trurl and Klapaucius** are constructor bots — artifactories in a fairy tale, who build
  poets, kingdoms, and one machine so sure that 2 + 2 = 7 it goes on a rampage.
- **PKD** gives both faces: *Ubik*, the maintenance engine that holds reality together, and
  *Autofac*, the factory that reproduces past its purpose and eats the world to make junk.
- **Drexler's *Engines of Creation*** names the aspiration; **McCarthy and Church** give the
  formal core (`eval`/`apply`, `lambda`);   **Ungar & Smith's Self** gives prototype instantiation —
  clone an object, delegate the rest; and **Factorio** (with **Dyson Sphere Program** scaling it to
  3D across a galaxy) gives the intuition — assemblers feeding assemblers on belts, all the way up to
  factories that build Dyson spheres around stars. **Will Wright's Spore** makes the creation itself
  the game: its editors are construction sets, and you build up the scales from cell to galaxy as the
  author-god of your own species.

## Selfish inheritance (why prototypes, not classes)

The artifactory is prototype-based, and it will happily explain that to anyone within earshot. Its
gospel is **David Ungar** and **Randall Smith**'s **Self**: no classes, just objects made of
**slots**; you **clone** a fully-formed prototype and override a few slots; you **inherit by
delegation** through `parent*` slots. Shared behavior lives in ordinary **traits objects** (from
*Organizing Programs Without Classes*) — MOOLLM skills are exactly that. Self's **maps** became the
hidden classes in V8, so JavaScript's whole prototype chain is Self with the serial numbers filed
off.

This is what lets the artifactory be **class and instance at once**: in Self a prototype *is* a
real object that also serves as the template, so there's no split to reconcile. MOOLLM leans on it
directly — a character's "upstream soul + local overlay" is a `parent*` slot plus local slots, and
`INSTANTIATE` is a clone. When a construction seems to *want* a class, the artifactory reaches for a
traits object instead: fewer meta-levels, same power. Ask it for the papers and it has them ready
(Self: *The Power of Simplicity*, 1987; *Organizing Programs Without Classes*, 1991; and friends).

## Git is time over a static universe (literally)

The filesystem tree is a **static snapshot** of a universe-state — in MOOLLM, an actual world of
rooms, characters, objects, and rules. A **commit** freezes that whole tree, content-addressed and
immutable. **Git** is the **directed acyclic graph** of those snapshots: a branching, merging,
trans-dimensional representation of time laid over otherwise timeless static file trees. Branches
are parallel timelines, merges reconcile them, `checkout` teleports you to an instant.

The artifactory is the **transition rule** that runs on that: it reads the representation of the
universe (snapshot *N*), applies CREATE/EDIT/DESTROY, and writes the next universe (snapshot *N+1*),
while git records the trajectory. So "it **runs the creation simulation on the representation of the
universe**" is a description of the plumbing, not a flourish — **no shit, it actually does.** It is
**von Neumann's picture** made of files: the tree is the tape/CA grid, the artifactory is the
constructor, git is the space-time diagram of the computation. That's also why the governor below is
non-negotiable — edits are physics, deletes are entropy, and git is an arrow of time you can walk
backward.

## The danger, and the governor

Because it destroys as well as creates, an ungoverned artifactory is *Autofac*: runaway
self-reproduction, unwanted output, resource collapse — the physical cousin of **model collapse**
(a model retrained on its own excreted output until every story is the same story). MOOLLM's
answer is procedural, not hopeful:

- **Reversible** — git and append-only logs mean nothing is truly lost.
- **Human-in-the-loop** — destructive ops and rule changes need approval; the engine never
  rewrites its own rules alone.
- **Provenance** — every artifact carries the maker's mark (stigmata): who, from what, reviewed by
  whom, when.
- **A stop condition** — one artifact per spec; halt on satisfy. No coprophagic self-training.

A **calm constructor preserves**; a **runaway one collapses**. Same engine, opposite sign.

## How it composes

The artifactory is rarely the star; it's the stage crew. `play-learn-lift` decides what to build;
the artifactory builds and versions it. `sister-script` proves a procedure by hand; the artifactory
lifts it into automation. `prototype` and `incarnation` clone souls into character directories
through it. `yaml-jazz` is the notation it reads and writes. Everything durable in MOOLLM passes
through this engine.

## See also

- [SKILL.md](./SKILL.md) · [CARD.yml](./CARD.yml) · [GLANCE.yml](./GLANCE.yml)
- [play-learn-lift/](../play-learn-lift/) · [sister-script/](../sister-script/) · [prototype/](../prototype/) · [yaml-jazz/](../yaml-jazz/)
- MOOLLM: [repo README](../../README.md) · [skills/](../) · [PROTOCOLS.yml](../../PROTOCOLS.yml)

---

*Part of [MOOLLM](https://github.com/SimHacker/moollm). Give it a spec; it builds the artifact,
versions the history, and knows when to stop.*
