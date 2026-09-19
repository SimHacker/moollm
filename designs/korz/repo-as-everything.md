# Repo as everything, and the class system the filesystem never had

**People:** Stephen Kell · Rob Pike · Dan Ingalls · Alan Kay · Owen Densmore · David S. H. Rosenthal

Treating the filesystem as the universal object space is an old move with a known failure. This
document records the failure, the diagnosis, and the fact that the fix was patented in 1991 by two
people already in the WWSFF cast — then why `git` is the step that makes the whole argument work.

The source is Stephen Kell, *The operating system: should there be one?*, PLOS'13
([10.1145/2525528.2525534](https://doi.org/10.1145/2525528.2525534),
[gwern's copy](https://gwern.net/doc/cs/end-to-end-principle/2013-kell-4.pdf)). The title answers
Ingalls, whose Smalltalk design principle held that an operating system is a collection of things
that don't fit into a language, and that there shouldn't be one.

## Pike's anecdote, and Kell's correction

Pike's 2012 SPLASH keynote offers Plan 9's compositionality as a story:

> A system could import a TCP stack to a computer that didn't have TCP or even Ethernet, and over
> that network connect to a machine with a different CPU architecture, import its `/proc` tree, and
> run a local debugger to do breakpoint debugging of the remote process. This sort of operation was
> workaday on Plan 9, nothing special at all. **The ability to do such things fell out of the design.**

Pike credits the uniform interface — "all system data items implemented exactly the same interface, a
file system API defined by 14 methods." Kell's parenthetical is the whole essay in one shrug:

> (Given the few semantics which are guaranteed to be ascribed to a file, 14 seems a rather large
> number.)

And then the correction that matters: **the uniform interface is not sufficient and is not even the
main thing.** Network transparency of server access "is at least jointly responsible," and the
anecdote silently requires it — *import* a TCP stack, *import* its `/proc` tree. Kell names the three
properties actually being wished for, all three of which Smalltalk already had:

1. a **network-transparent object abstraction** — the unstated enabler of Pike's scenario
2. a **metasystem** — smuggled into the phrase "the same interface"
3. **late binding** — for the versioning problem that shows up the moment servers are separable

He then collapses the distinction everyone argues about: *"It now seems reasonable to declare 'file'
(in the Plan 9 sense) and 'object' (in the Smalltalk sense) as synonymous. Both are equally universal
and more-or-less deliberately semantics-free."*

## Kay's cells, and why the convergence is not a coincidence

Kell's evidence that this is one idea and not two analogies: Smalltalk objects, like Plan 9 files, are
naturally amenable to a distributed implementation (Schelvis and Bledoeg's distributed Smalltalk,
1988), and Kay recalls having "thought of objects being like biological cells and/or individual
computers on a network" from a very early stage.

`caveat:` Kell footnotes that quotation as *"Various sources on the web attribute this statement to
Kay"* — so the specific wording is web-attributed even in the paper that uses it. The underlying
framing is not in doubt and is Kay's own throughout the Smalltalk history writing; the exact sentence
wants a primary cite before anyone quotes it in anger.

The cell is the load-bearing part, not the network. A cell is a **membrane** with its own genome,
metabolising independently, addressed from outside by what it presents rather than what it contains.
That is a directory, and it is why the TIES extension model is
[endosymbiosis](../../skills/ties/TIES-SCHEMA.yml): a foreign schema arrives engulfed, keeps its own
genome, and the host never grows fields to accommodate it.

## What Plan 9 lacks: classes

This is the diagnosis worth keeping, because it is precisely the gap TIES.yml was written into:

> As the filesystem's use has expanded, its semantics have become less clear. What do the timestamps
> on a process represent? What about the size of a control file? [...] Can I use `cp` to take a
> snapshot of a process tree? It is hard to tell. [...] **Unlike in Smalltalk, semantic diversity is
> not accompanied with any meta-level descriptive facility analogous to classes.**

A fixed abstraction plus growing semantic diversity equals a namespace where you cannot tell what
anything means or whether the usual operations will work. Kell's framing of the residual difference:
Plan 9 applications must implement a 14-method protocol to reify their state as objects, whereas
Smalltalk objects are objects by default, and **classes give at minimum a semantic description.**

`ls` is the same problem at small scale. It returns names, and names are not descriptions. Everything
in [`../../skills/ties/TIES-SCHEMA.yml`](../../skills/ties/TIES-SCHEMA.yml) about beating `ls` is a
restatement of this paragraph, arrived at from the other end.

## Densmore and Rosenthal already built it, in-band, in 1991

**US 5,187,786** — *Method and apparatus for implementing a class hierarchy of objects in a
hierarchical file system.* Owen M. Densmore and David S. H. Rosenthal, Sun Microsystems. Filed
5 April 1991, granted 16 February 1993, **expired 2011**, so it is free to use and to read as a
design document. [Google Patents](https://patents.google.com/patent/US5187786A/en).

What it does, in its own terms:

| Smalltalk thing | Filesystem thing |
|---|---|
| class | a directory |
| method | a file in the class directory |
| instance | a directory of instance-variable files |
| instance variable initial values | files in the class directory |
| **the inheritance chain** | **a `path` file, whose contents relate to the parent's** |
| method lookup | invocation controlled through those path files |
| data abstraction | instance variables reached only via class methods |
| `Self` and `Super` | supported explicitly |

The clause that makes it interesting rather than merely clever is in the abstract: it **"does not
require the support of additional file attributes by the hierarchical file system."** No extended
attributes, no new inode fields, no kernel. Directories, files, and a path convention — and out of
that, inheritance with `Self` and `Super`. The path file *is* a dictionary stack, which is the shell's
`PATH` used as Smalltalk's method lookup, from two people who had just spent years inside PostScript
where the dictionary stack is the dispatch mechanism.

`dry-piles note:` [`dry-piles.md`](dry-piles.md) says the path is the guard expression and `ls` is a
gather along the axis the tree was cut on. The patent is that claim, nineteen years earlier, with
inheritance attached and a filed date.

## Why the in-band constraint is the whole reason git works

`git` **does not store extended attributes.** A tree entry carries a path, a blob hash, and a mode
that is effectively regular / executable / symlink / submodule. No xattrs, no owner, no ACLs, no
timestamps. Anyone who has tried to make a metadata scheme survive a clone has met this.

So a metasystem for a git repo has no choice but to be in-band: files and directories, or nothing.
That constraint sounds like a limitation and is actually the licence, because Densmore and Rosenthal
proved a **full class system with inheritance fits inside it.** A screening layer is a much smaller
ask than that.

And git supplies the property Kell says is jointly responsible and which a local filesystem does not
have. A repo is location-independent: `clone` is Plan 9's `import`, the same tree materialises from a
different machine, and the content hash makes identity independent of where the bytes live. Plan 9
needed 9P and a kernel; git gets network transparency from content addressing and an ordinary
transport.

Which is why the progression in the claim is a progression and not three names for one thing:

| Layer | What it adds that the previous one lacked |
|---|---|
| **filesystem** | uniform interface, hierarchy, position-implies-class (implicitly, per dry-piles) |
| **git repo** | history as an axis, content-addressed identity, distribution — Kell's network transparency |
| **github repo** | stable exterior URLs, an API, actions as compute, issues and PRs as deliberation |
| **TIES.yml** | the metasystem. The classes the filesystem never had, and the thing Plan 9 was missing |
| **mooco / MOOFS** | the per-process namespace and live synthetic files — Plan 9's `bind` and control files, restored on top of all of the above |

The last row is the one this repo is adding, and Kell's paper is the argument that it is the missing
row rather than a nice extra. Late binding — the third property — is
[k-lines](../../PROTOCOLS.yml) and `~name~` scope-walk resolution: symbolic references resolved at
read time against the nearest enclosing scope, which is late binding with the filesystem as the
environment and no symlinks to go stale.

## Membranes, thick and thin

Two thicknesses, both in use, and the distinction is Don's:

- **A directory is a thick membrane.** Its own walls, its own `TIES.yml`, its own prototype, its own
  organelles. Crossing it is a deliberate act.
- **A big-endian name prefix is a thin one.** `fitts.md`, `fitts.TIES.yml` share a membrane made of
  nothing but a common prefix in one directory — looser, cheaper, and enough to bind a subject to its
  sidecars without giving it walls.

Big-endian naming is what makes the thin membrane work: most significant first, so a directory listing
sorts into families and the prefix does the binding that a subdirectory would otherwise be spent on.
The sort order is the index.

## The live half: mooco mounts, and a control file that knows what it is

A checkout is dead, but mooco is not a checkout. Its design is Plan 9's structure with git underneath:
**multiple repos, possibly sparse subtree mounts, bound at arbitrary points in a virtual namespace,**
plus `/proc`-like magic-dictionary YAML files through which the orchestrator and the model actually
talk. Written up in [`../MOOFS-NAMESPACE.md`](../MOOFS-NAMESPACE.md) and
[`mooco/designs/MOOCO-REPOS.md`](https://github.com/SimHacker/mooco) — this section only records what
Kell's paper adds to a design that already exists.

Two things, and both are cases where Kell names a defect that this shape happens to answer.

**The mount table is the interposability property.** Kell's complaint about Unix is not about files, it
is about binding: *"user code cannot quite 'be a file', because only files may be opened by name"*, so
a program can be redirected only if its author had the foresight to accept a filename parameter. Plan 9
fixed this with per-process namespaces. MOOFS fixes it the same way, and `/proc/self/ns.yml` — where
**writing the file is the act of mounting** — makes the binding itself an ordinary object in the space
it binds. That is Kell's third property, late binding, not bolted on but made editable.

**A YAML control file is a Plan 9 control file that carries its own class.** This is the sharper point.
Kell's objection to control files is that they are semantically naked:

> What do the timestamps on a process represent? What about the size of a control file? [...] It becomes
> ill-defined whether "the usual things" one can do with files will work.

A Plan 9 control file is a byte stream with a convention in someone's head. A magic-dictionary YAML
file is **self-describing** — keys, structure, a schema pointer, and yaml-jazz comments carrying the
semantics for all three audiences. So the metasystem is not a separate registry bolted beside the
control files; it is *inside* them, which is the property Kell says distinguishes Smalltalk, arriving
by the cheapest possible route.

`and the reason it matters here:` the same file is edited by the model with read/write/ls and by a
human in an editor. No second mechanism, no API the human is locked out of, which is
**interfaces to agency** — symmetry of capability, asymmetry of throughput — enforced by the substrate
rather than by discipline.

One more convergence worth logging, because it explains why mooco is not making Smalltalk's mistake.
Kell observes that Smalltalk's answer to fragmentation is *"don't fragment; use Smalltalk for
everything"* — a modernist grand narrative in Noble and Biddle's sense — whereas Unix survives the
postmodern reality of mutually incoherent systems by being **oblivious** to them. Mounting other
people's repos as they are, and describing them from outside with manifests and organelles, is the
Unix answer rather than the Smalltalk one: no rewrite demanded, no single system claimed, the guest
keeps its genome.

## Where the argument stops

Honest limits, since the paper's own move is to deflate an over-claim:

- Kell's diagnosis is that unification **failed by fragmentation**, and a YAML manifest is another
  convention that could fragment exactly as the others did. What keeps it from being one more
  incompatible mechanism is the lint gate and the single rung ladder, not the idea.
- Plan 9's files are **live** and a plain checkout is not, which is why `cache:` sidecars carry a
  regenerating command and a date rather than a promise. mooco closes most of this gap with synthetic
  `/proc` files, so the honest residue is narrower: a **committed** `TIES.yml` describes a tree that
  can change under it, and no amount of mounting makes a recorded description self-updating.
- Smalltalk's advantage that nothing here recovers is **inclusiveness toward small objects.** Git's
  unit is a file, so the granularity floor is real, and the thin-membrane prefix trick is the
  concession to it rather than a solution.

## See also

- [`../MOOFS-NAMESPACE.md`](../MOOFS-NAMESPACE.md) — bind mounts, typed object mounts, `/proc`, and
  `/proc/self/ns.yml` where writing the file is the mounting
- [`../MOOFS-DESIGN.md`](../MOOFS-DESIGN.md) — the magic dictionary pattern
- [`dry-piles.md`](dry-piles.md) — the path as guard expression, `ls` as gather
- [`../../skills/ties/TIES-SCHEMA.yml`](../../skills/ties/TIES-SCHEMA.yml) — the metasystem, organelles, prototypes
- [`../../skills/ties/RUNGS.yml`](../../skills/ties/RUNGS.yml) — the rung ladder
- [`../../designs/webtop-gwern-inheritance/K-PYRAMID-ATTENTION-MAPS.md`](../../designs/webtop-gwern-inheritance/K-PYRAMID-ATTENTION-MAPS.md) — attention over the graph
- Owen Densmore and David Rosenthal in WWSFF — the cast this patent belongs to
