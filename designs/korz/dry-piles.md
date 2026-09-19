# Dry piles

*A directory tree of [Korz](README.md) or MOOLLM objects arranged so that the filesystem
**is** the guard lattice: flat plural piles of same-typed objects, one canonical source per
fact, and every duplication declared, derived, and recomputable. The engineering discipline
underneath [yaml-jazz](../../skills/yaml-jazz/)'s "directories as advertisements."*

**Attribution:** Don Hopkins, Sept 2026 — including the name and the pumps.

## The name is not only a pun

A **dry pile** is a real object, and the most famous one has been running since 1840.

The Clarendon Dry Pile at Oxford — the Oxford Electric Bell — is a pair of Zamboni piles
(Giuseppe Zamboni, 1812: some two thousand pairs of foil-and-paper discs) driving a 4 mm metal
clapper between two bells at 2 Hz. It has rung on the order of **ten billion times** and holds the
Guinness record as the world's most durable battery, *"delivering ceaseless tintinnabulation."*

Three properties of that apparatus are the whole design, which is why the name was worth keeping:

| The pile | The repo |
|---|---|
| **Sealed in molten sulfur** — air tight, water proof | Derived content is sealed against hand-editing, per field |
| **Electrostatic: kilovolts, nanoamps** — enormous work, almost no charge transported | Enormous reading, almost no duplication transported |
| **Nobody knows what is inside**, because opening it would end the experiment | The anti-pattern. See the last section |

`verified: Clarendon Laboratory history archive and Oxford Electric Bell; "Set up in 1840" in
Robert Walker's hand, though a later note suggests construction ~15 years earlier. Composition
conjectural — outer coating sulphur is established, Zamboni-style innards are inference. Croft,
European Journal of Physics, 1984.`

## The shape

- **Flat plural directories of same-typed objects**, plus whatever metadata the directory itself
  needs. `lenses/` holds thirty-four lenses, not `lenses/perception/visual/fitts.md`.
- **One canonical home per fact.** Schemas factored so that the single-sourciest version is the
  one that exists; everything else derives.
- **Duplication is legal when declared.** Not forbidden — *declared, validatable, and
  recomputable*, preferably deterministically, and by inference where determinism is not
  available.
- **Directories carry guards.** Contents inherit declared overrides and computed constraint
  networks from where they sit.

## A directory is a guard, and `ls` is a gather

This is the load-bearing claim and it is why the idea belongs next to Korz rather than in a style
guide.

Putting a file at `skills/design-sense/lenses/fitts.md` already asserts everything a guard would
have to say:

```yaml
guards: {kind: skill, skill: design-sense, class: lens, id: fitts}
```

Nobody typed that. **The path is the guard expression**, pre-indexed by a B-tree somebody else
wrote and maintains, queryable by every tool on the machine without a schema. A directory listing
is a gather along whichever axis the tree was cut on, `find` is a gather along the others, and
`rg` is a gather along content. The filesystem is the cheapest dispatch engine available and it
ships with the computer.

Which immediately explains **why the pile is flat.** Any hierarchy you impose below the type level
is *one decomposition asserted as the dominant one* — precisely the error Korz exists to refuse.
`lenses/perception/` would make "perception" the privileged cut and silently demote every other
way of grouping lenses. Keep the pile flat and let `INDEX.yml` and `CARD.yml` be **gathers**: many
of them, cheap, none of them the tree, each one free to disagree. The dispatch table in
`lenses/CARD.yml` groups the same thirty-four files six different ways, and no file had to move.

> **Flat pile, many indexes. The pile is the sea; an index is a gather; the tree is a lie you only
> get to tell once.**

## The wet part, and the pumps

You cannot keep it totally dry, and pretending otherwise produces repos nobody can read.

The clearest case in this repository is the semantic image pyramid. `GLANCE.yml`, `CARD.yml`,
`SKILL.md` and `README.md` are **four denormalized resolutions of one object**, and that
redundancy is the entire point — it is what lets a reader answer "is this relevant?" without
loading a thousand lines. Normalizing it away would be correct and useless.

So the rule is not *no duplication*. It is:

> **Every duplicated fact has exactly one upstream, a declared derivation, and a pump that can
> regenerate it. Hand-edit the source; never the copy.**

The [amsterdank rules](https://github.com/SimHacker/amsterdank) already state the strict version
of this for field data — `PLACE.yml` is canonical, `data/*.csv` is derived, never hand-edit a
derived file, regenerate it — and add the constraint that makes pumps survivable:
**generators propose and never overwrite hand-written comments.** The fieldwork is in the
comments. A pump that clobbers them is a pump that eats the thing it was built to serve.

That constraint is the sulfur. The seal is not on the file, it is **per field**: derived fields are
machine territory, authored fields and their comments are not, and the boundary is recorded rather
than remembered.

### Two kinds of pump, two kinds of seal

Don's definition allows inference as well as determinism, which is right, and they need different
guarantees because only one of them can be re-run as a check:

| Pump | Verification | Seal |
|---|---|---|
| **Deterministic** — script, template, schema projection | Re-run it and diff. A difference is a bug | Output may be overwritten freely. Check in for speed, or not at all |
| **Inference** — an LLM filling a rung nobody wrote | Re-running gives a *different* answer, so diffing proves nothing | Must be marked as inferred, dated, and reviewed once by a human; then it is authored content with a provenance note |

The failure mode to design against is an inference pump whose output is indistinguishable from
canonical source. That is how a repo quietly becomes its own hallucination. `needs-check:` markers
exist for exactly this, and an inferred field without one is a leak.

## Constraint networks over the tree

Because the path carries guards, a directory can carry **defaults its contents inherit** — which
is prototype inheritance with the filesystem as the delegation chain, and is the same cascade CSS
runs and the same ambient propagation Korz runs on dimensions.

The useful part is that inheritance plus overrides gives you a **checkable** relation rather than a
convention:

> **A child's override must be narrower than the parent's constraint.** Widening it is an error,
> because the parent's guard is a promise the pile makes to anything gathering over it.

That single lint catches the class of bug where one file in a pile quietly stops satisfying the
thing the directory's index claims about all of them — which is otherwise found by a reader, later,
in public.

## The anti-pattern, which the metaphor also supplies

Nobody knows what is inside the Oxford pile. Opening it would end the experiment, so it has run
for 185 years as a **sealed box whose mechanism is conjecture** — the composition in every account
is inference from Zamboni's other work, not observation.

That is a charming property in a Victorian curiosity and a fatal one in a repository. A seal so
tight that the derivation cannot be inspected is the [anti-prosthetic
shape](../PROSTHETICS.md): a thing that works, that nobody can audit, that you therefore have to
trust. The discipline is the opposite of the museum piece — **seal the derived content against
editing, and leave the derivation open to reading.** Airtight against hands, transparent to eyes.

## Already dry piles in this repo

`skills/` (150 same-typed objects, flat) · `lenses/`, `methods/`, `masters/` under design-sense ·
`characters/<id>/` with `sources/<date-slug>/` piles beneath · `places/<id>/PLACE.yml` in
amsterdank. In each case the pile is flat, the indexes are several, and the type is the directory
name in the plural.

## The test

1. **Can you add an object without editing a taxonomy?** If a new lens requires choosing a
   subdirectory, the tree is asserting a dominant cut.
2. **Point at any duplicated fact and name its upstream.** If the answer is "both of them are
   maintained," it is not a pile, it is two lies waiting.
3. **Delete every derived file and rebuild.** What does not come back was never derived, and is
   now canonical whether you meant it or not.
4. **Grep for inferred content.** If you cannot distinguish what a machine guessed from what a
   person established, the pile has no seal.

**See also:** [README.md](README.md) — dimensions, guards, and why no decomposition is dominant ·
[../../skills/yaml-jazz/](../../skills/yaml-jazz/) — directories as advertisements, filenames as
K-lines · [korz-prime/README.md](korz-prime/README.md) — crystallize what has stabilized,
deoptimize what has not, which is the same traffic a pump runs ·
[../PROSTHETICS.md](../PROSTHETICS.md) — why the derivation stays readable
