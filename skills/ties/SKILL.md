---
name: ties
description: A manifest file type and authoring discipline for making a directory tree legible to an orchestrator without opening it. TIES.yml carries a semantic pyramid from emoji through label, name, one-paragraph definition, description and body, plus synonyms for name resolution, typed links, costs and read conditions for children, and foreign schemas attached as isolated organelles. Descends from HyperTIES (HCIL, 1988), whose articles were required to carry a previewable definition. Use when deciding what to page into context from an unfamiliar tree, when authoring a manifest for a node, when linting a corpus for silent name collisions, or when attaching external metadata such as Dublin Core.
allowed-tools: [Read, Write, Grep, Glob, Bash]
related: [yaml-jazz, design-sense, k-lines, dry-piles, postel, robust-first]
benefits_from: [cursor-mirror, skill-snitch]
license: MIT
tags: [manifest, metadata, hypertext, context, schema, dublin-core, prototypes, hyperties]
credits: "HyperTIES: Ben Shneiderman and the HCIL team, University of Maryland, with Don Hopkins on the NeWS implementation. Prior art: Owen Densmore and David S. H. Rosenthal, US 5,187,786. Diagnosis: Stephen Kell, PLOS'13. Rungs: Marvin Minsky's K-lines and level bands."
---

# TIES 🪢

**A name is not a description, and `ls` gives you names.**

You arrive in a directory you have never seen. `ls` returns twelve words. Which do you open? You cannot
tell, so you open several and pay for all of them, or you open one and guess. Now do it a hundred times
in one session, under a context budget, and the guessing is the dominant cost of the whole enterprise.

TIES.yml is a small file that answers the question without being the answer. It descends from
**HyperTIES** — The Interactive Encyclopedia System, Ben Shneiderman's group at the University of
Maryland HCIL, mid-1980s, with a NeWS implementation by Don Hopkins. HyperTIES had a property the web
threw away: **every article was required to carry a short definition**, so a link could be summarised
before it was followed. One click previewed, two clicks went. The reader could ask "should I go there?"
and get an answer that cost a paragraph instead of a page.

The web kept the link and dropped the definition. Everything that feels revelatory about gwern.net's
link popups is that rung rebuilt by hand, per link, as annotations — work HyperTIES got free in 1988
because its schema refused to let an article exist without one.

## The one idea: position implies cost

A TIES.yml orders its keys **cheap to dear**:

| Rung | Size | Answers |
|---|---|---|
| `glyphs` | 1–5 emoji | what KIND of thing is this |
| `label` | 1–4 words | what do I call this in a menu |
| `name` | one line | what is this called, canonically |
| `definition` | 1–3 sentences | **should I go there** |
| `description` | a paragraph to a page | what can it do, what is in it |
| `body` | the whole document | how does it actually work |

Reading top-down is therefore reading cheapest-first, and **stopping early is a decision rather than an
accident.** The ladder with its canonical weights lives in [`RUNGS.yml`](RUNGS.yml) and is cited from
elsewhere rather than retyped — it was once stated in two documents with different bottoms, and they
drifted.

`definition` is the only required rung besides `name`. It is the one the web dropped and the one that
makes the file worth reading. An LLM can draft a candidate, so "required" never has to mean "blocked" —
mark it in `provenance.generated` and let a human confirm it.

## What this is not: it screens, it does not advertise

The distinction that keeps the file small, and the one most likely to be got wrong:

|  | TIES.yml | CARD.yml |
|---|---|---|
| Job | **screen** | **advertise** |
| Answers | is this a candidate at all | how much would this help, given my state |
| Reports on | presence, cost, staleness, whether a richer declaration exists | value to this asker under these conditions |
| Grammar | advisory notes on pointers | triggers, conditions, scores, scopes, rationales |
| Weight | deliberately light | as heavy as it needs to be |

If you find yourself writing a trigger with a score in a TIES.yml, you are writing an advertisement and
it belongs in the CARD. The most useful thing a screen often says is `description: CARD.yml` — *a full
advertisement exists, one cheap fetch away.* Two stages, deliberately unequal.

The borrowed insight from the Sims' Find Best Action, and the only one borrowed: **usefulness is a delta
against what the reader already has.** The Sims scores a person twice, once with current motives and
once with motives plus the advertisement, and subtracts; "+50 Hunger" is worth nothing to a full Sim.
Likewise "693 KB of masters" is worth nothing to a reader holding the index. So a hint names the
condition under which its value collapses, not merely its size. Motives, check trees and cutoff curves
stay in the advertisement model where they belong.

## Read in bulk, and everything follows from it

A TIES.yml is not read one at a time. A hundred are read at once to decide what to page in next. That
single fact sets every other constraint:

- **Inline the screening set** — `glyphs`, `label`, `name`, `definition`. These are what the screen reads.
- **Point at the rest** — `description` and `body` are paths. Inlining them puts the answer inside the
  thing you were deciding whether to open.
- **Budget**: 500 bytes for a leaf that inherits, ~3 KB for a hub, 4 KB hard. A hundred leaves at 500
  bytes is 50 KB, which is the number that decides whether bulk reading is a real technique.
- **Caches go in a sidecar.** `cache: TIES-CACHE.yml`. Derived values are bulky, they churn, and they
  are exactly what a screen does not need.

## Carry only what is not derivable

Generally, not absolutely. The licence comes from `dry-piles`: duplication is allowed when it is
**declared, validatable and recomputable.**

Already available, so do not retype it:

- **from the filesystem** — names, counts, sizes, mtimes. `ls` and `wc` produce these, and they rot.
- **from the path** — type and class. `lenses/fitts.md` already says `{class: lens, id: fitts}` and
  nobody typed it. The path *is* the guard expression.
- **from the pointee** — the definition is in the CARD. Point; do not paraphrase.

**Redundancy is a cache**, and a cache is legitimate if and only if it can be invalidated and
recomputed. So the line between good and bad duplication is not how much, it is whether it is declared.
A count in a `cache:` sidecar with the command and the date is a cache. The same count hand-typed into
prose is a fork.

This is not hypothetical. The first real manifest written for this skill claimed 37 lenses, 36 methods,
62 masters and 9 seeds. The truth was 35 / 34 / 60 / 7: the numbers came from `ls | wc -l`, which counts
each pile's own `CARD.yml` and `GLANCE.yml` as if they were members. Every pile overcounted by exactly
two. Worth separating from ordinary staleness, because **a wrong formula refreshed on a schedule keeps
producing the same wrong answer, on time, forever.** The audit also found six files in one repo claiming
those counts with no two agreeing, two of them loaded into every session.

What survives the test, and is therefore the actual payload: `cost`, the read condition, `stale`,
`synonyms`, and why a tie exists.

## Organelles: extension by endosymbiosis

A schema this file type does not own arrives the way a mitochondrion did — **engulfed whole, kept inside
a membrane, still carrying its own genome.** Every guest lives under `x:` in a sub-object named for
itself, with a `schema:` pointer to its own definition. The host validates the membrane and never the
contents.

```yaml
x:
  dc:                                            # the mitochondrion: ancient, universal, boring
    schema: "http://purl.org/dc/elements/1.1/"
    creator: Don Hopkins
  korz:                                          # a recent acquisition, may not survive the month
    schema: ../../designs/korz/KORZ-SCHEMA.yml
    dimensions: [self, purpose, whose_purpose]
```

Dublin Core gets no special status, and that is the claim: **standard and experimental guests differ in
age and adoption, not in kind**, so one extension mechanism suffices instead of a blessed list plus an
escape hatch. schema.org, PROV-O, SKOS and CIDOC-CRM arrive on identical terms. A guest can leave by
deleting its sub-object, because nothing in the core referenced it.

### Preserve what you do not understand

An unrecognised key, an unrecognised organelle, and **every comment attached to either** must survive a
read-modify-write byte-identical. An unknown organelle is reported as INFO, never as an error — an
unblessed guest is the design working.

The comment half is the part that gets lost. In yaml-jazz the comments *are* the data, so a round-trip
that preserves structure and eats comments has destroyed the payload and kept the packaging — and that
failure looks like success in every diff of parsed values.

`implementation:` never PyYAML `safe_load`/`dump` for anything that writes; it discards comments, key
order and anchors. Use `ruamel.yaml` in round-trip mode, and assert byte-identity on a commented file as
the tool's first test. `ties_lint.py` is a pure reader and never writes, which is why `safe_load` is
honest there and nowhere else.

## Prototypes: say the diff, inherit the rest

Manifests come in families. Every member of a pile shares a creator, a language, a type and most of its
tags; what differs is a name, a definition and a few ties. Repeating the shared part per file is the
redundancy that **dominates a corpus, because it scales with the number of files rather than their
size.**

The pile's own TIES.yml is the prototype. It states shared values under `inherited:` so its own screen
fields stay its own. Children declare `proto:` and carry only overrides.

```yaml
# lenses/TIES.yml — the pile's screen AND its prototype
inherited:
  type: lens
  tags: [design, lens, ambient]
  x: {dc: {schema: "http://purl.org/dc/elements/1.1/", creator: Don Hopkins}}
```
```yaml
# lenses/fitts.TIES.yml — 415 bytes, and this is all of it
proto: TIES.yml
name: fitts
glyphs: 👁️🎯
definition: "Pointing cost grows with distance and shrinks with target size. Radial beats linear."
body: fitts.md
```

Resolution rules, chosen for a reader scanning a hundred files:

- **scalars** — child wins. **maps** — deep merge, child wins per leaf.
- **lists REPLACE.** Not append, because append makes a child's meaning depend on a parent it does not
  show you. `tags+: [extra]` is the visible opt-in.
- **absence means not-overridden-here**, resolving to the prototype. If the prototype lacks it too,
  absence means unknown, as everywhere. The two senses compose and neither means false.
- **tombstone**: `unset: [tags, x.dc.subject]`. Needed precisely because absence now means inherit, and
  dotted paths drop one organelle element without restating the organelle.

Budgets are **amortised**: a prototype is read once for N children, so it may be chattier; a leaf is
read N times, so it may not. Keep the chain to one or two hops — a deep prototype chain is a class
hierarchy, which is the thing Yertle warns about.

### Sidecars, selectively

A per-member manifest is `<subject>.TIES.yml`, beside the thing it describes — big-endian, the subject
leading, matching `name.yml` / `name.md` / `name.png` practice.

**Do not generate one per member.** A member earns a sidecar when it has synonyms or k-lines that must
resolve to it, outbound ties an index line cannot carry, its own glyphs because something renders it as
a pie slice or minimap dot, or references from outside its own pile. Otherwise the pile's `CARD.yml`
index line is enough, and the sidecar would be a file whose entire content is inherited. The asymmetry
decides it: one is cheap to add later, hundreds are expensive to delete once anything links to them.

## Synonyms, and the failure that leaves no artifact

Take this one seriously. It is the reason the linter exists.

A reference resolves to a **plausible wrong node**. The page renders, the link works, nothing reports
anything, and a corpus accumulates these faster than anyone re-reads it. Canonicalisation therefore
folds case, collapses whitespace — **the tilde is whitespace, so `~Founders~` and `founders` are one
name** — and strips punctuation.

That last one is a receipt from the surviving 1988 index: one article carried `"alphabetically"`,
`"alphabetically,"` and `"alphabetically."` as three separately registered synonyms, because a link
picked out of running prose drags its trailing punctuation into the lookup key. Widen the equivalence
class and the author stops paying for it.

Two claims on one canonical name in one scope is an **error**. A nearer scope shadowing an enclosing one
is **legal and must be reported** — that half is what the 1988 tool left unbuilt.

## Ties: the links, typed

HyperTIES links were untyped jumps. `ties[]` fixes that with `to`, `rel`, and a one-line `why` for a
reader deciding whether to follow. The relation names come from the senses already inside the word:

- **`binds`** — the Korz sense. This node binds that name to a meaning.
- **`cross`** — a **cross-tie**. A railroad tie runs across the grain, holding two rails at gauge. That
  is a bidirectional relation, which is exactly what HyperTIES lacked and what the web shipped without.
- **`lit_from`** — provenance, whose flame this came off.
- **`sustains`** — a musical tie: two notes, one duration, continuity across an apparent break.
- **`ties_with`** — a tie in a **vote**, two candidates with no dominant cut. Not an error; it is the
  ambiguity case, resolved by asking, which is where a pie menu belongs.

## The authoring loop

1. **Name it and define it.** The definition answers *should I go there* in one to three sentences.
2. **Point, do not inline.** `description:` and `body:` are paths to files that exist.
3. **List `inside[]` in read order**, never alphabetically, each with a `cost` and a read condition
   that names when its value collapses: "index is enough", "open exactly one, named", "skip unless
   gardening".
4. **Add `synonyms` only if** something must resolve to this node under another name. Generic aliases
   are worse than none — "the forge" is good, "the thing where you do the work" will collide with
   everything.
5. **Hoist anything a sibling also says** into a prototype.
6. **Move derived values to a `cache:` sidecar** with the command that regenerates them and the date.
7. **Lint.** `python3 skills/ties/scripts/ties_lint.py --corpus DIR`

Then re-read what you wrote and delete every line that the filesystem, the path, or the pointee already
says. That pass removed 900 bytes from the first manifest written with this skill, including a header
that duplicated an index file verbatim.

## Linting

```bash
python3 skills/ties/scripts/ties_lint.py PATH...          # files or directories
python3 skills/ties/scripts/ties_lint.py --corpus DIR     # adds cross-file checks
```

Exit 0 clean or warnings only, 1 on any error. Every check is build-time and needs no model: required
rungs, ladder order, inline-body refusal, budgets, pointer resolution (glob-aware, because a pile
addresses its members as `*.md`), `inside` costs, type-versus-container agreement, undeclared caches,
redundant inheritance, bogus tombstones, organelle membranes, and across files, synonym collision,
shadowing and glyph set contrast.

Warnings are advisory and sometimes the right answer is to change the threshold rather than the file —
`BUDGET_HUB` was moved from 2 KB to 3 KB once three real manifests showed that a hub's cost is dominated
by its `inside` entries, so a flat target punished breadth rather than chattiness. Say so when you do it.

## Why this belongs in a git repo specifically

Stephen Kell's diagnosis (*The operating system: should there be one?*, PLOS'13) is that the filesystem
has **no meta-level descriptive facility analogous to classes**, so as its uses multiply, its semantics
get less clear and you cannot tell whether the usual operations will work. TIES.yml is that facility,
retrofitted in-band.

In-band is not a compromise, it is the only option: **git does not store extended attributes.** A tree
entry is a path, a blob hash and a mode. Which makes Densmore and Rosenthal's **US 5,187,786** (Sun,
filed 1991, expired 2011) the encouraging precedent — a full class hierarchy in a plain hierarchical
filesystem, classes as directories, instances as directories of variable files, the inheritance chain in
a **path file** used as a dictionary stack, with `Self` and `Super`, and explicitly "without requiring
additional file attributes." If a class system fits that budget, a screening layer certainly does.

The full argument, with Pike's Plan 9 anecdote and Kell's correction to it, is in
[`../../designs/korz/repo-as-everything.md`](../../designs/korz/repo-as-everything.md).

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — a microworld OS where the
filesystem is navigable space, comments carry semantic meaning, and skills are prototypes you
instantiate. See the [skills index](../README.md).

Related skills, and what each actually contributes here:

- **[`yaml-jazz`](../yaml-jazz/)** — the notation. Comments are first-class data, and in a TIES.yml they
  carry the read conditions that no field expresses.
- **[`dry-piles`](../../designs/korz/dry-piles.md)** — the path is the guard expression, so type comes
  free from position, and the licence for declared duplication comes from here.
- **[`k-lines`](../k-lines/)** — `~name~` references and scope-walk resolution: the late-binding half,
  with no symlinks to go stale.
- **[`design-sense`](../design-sense/)** — the first dogfood: a hub, a pile prototype, and a leaf
  sidecar, all lint-clean.
- **[`postel`](../postel/)** — accept messy manifests, emit clean ones, ask when a name is ambiguous.
- **[`robust-first`](../robust-first/)** — an unknown organelle degrades to preserved-and-reported. A
  tool that drops what it cannot parse is not conservative, it is lossy, and the loss is silent.
