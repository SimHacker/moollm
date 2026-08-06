# P-Pyramid — an anchored attention mask over a graph

> *"Given these constraints, if one 'looks down' from the viewpoint of a given agent P, one
> will see other agents arranged roughly in a hierarchical Pyramid... I emphasize that the
> network as a whole need not be pyramidal; the P-pyramid we speak of is an illusion of an
> agent's perspective."*
> — Marvin Minsky, K-Lines: A Theory of Memory (MIT AI Memo 516, 1979)

Minsky's term, adopted whole. The graph is not a hierarchy; the **view from P** is. Every
outliner, every tree-style tab bar, every expanded skill pyramid, every context window is a
P-pyramid: a hierarchical illusion projected from one agent's vantage over a structure that
is really a tangled graph.

Primary sources:

- [K-Lines: A Theory of Memory, MIT AI Memo 516, June 1979 (PDF)](https://dspace.mit.edu/bitstream/handle/1721.1/5739/AIM-516.pdf)
  — full OCR text cached at [skills/k-lines/sources/aim-516-k-lines-1979-ocr.txt](../skills/k-lines/sources/aim-516-k-lines-1979-ocr.txt)
- [Cognitive Science 4(2):117-133, 1980](https://doi.org/10.1207/s15516709cog0402_1)

## Definition

A **P-pyramid** is an anchored attention mask over a graph:

- **Anchored** — at P, the agent whose perspective projects the hierarchy. Move the anchor,
  get a different pyramid over the same graph.
- **Attention mask** — a weight on every node in view: **0** closed (a collapsed outline
  item; a tab; fog of war), **1** fully open, **0..1** partial — rendered smaller,
  summarized shallower. In PSIBER Space Deck terms the weight is the pretty-plotter point
  size; in MOO-Map terms it selects the mip level (GLANCE at 0.2, CARD at 0.5, SKILL at
  0.8, source at 1.0).

The mask is a **remembered view**: it does not modify the graph, it records how P last
looked at it. And that is precisely what a K-line stores. The memo's two-step mechanism:

> *"K-NODE ASSIGNMENT: A new agent — call it the K-node AK — is created and somehow linked
> with GK. K-LINE ATTACHMENT: Each K-node has a K-line — a wire having potential
> connections to every Agent in the P-pyramid. The act of 'memorizing' causes this K-line
> to make an 'excitatory' attachment to every currently active P-agent."*

**A K-line IS a stored attention mask**: which nodes to activate and how much. Activate the
K-node later and P "re-enacts" the partial state — the memo says P will *virtually
hallucinate* the event. Saving a view mints a K-line; speaking the name reopens the
pyramid:

> *"I once solved a similar problem. If I can get into that old state, I could probably
> handle this one the same way."*

## The level-band principle: how much to reactivate

The memo's self-declared most important idea. A perfect hallucination would be harmful —
*"complete resetting of the P-net would erase all the work done in processing the recent
data. It might even fool one into seeing the present problem as already solved."* So the
K-line attaches only to an **intermediate band of levels**:

- **Lower band-limit** — don't reach far down, *"for this would impose false perceptions
  and conceal the real details of the present problem."*
- **Upper band-limit** — don't reach up near P itself, *"for that would make us hallucinate
  the present problem as already solved, and impose too strongly the details of the old
  solution."*

This is context-loading policy, stated in 1979. Restoring a saved view should reload the
**middle of the pyramid** — the structural understanding — leaving the top free for the
current goal and the bottom free for the current facts. Don't paste yesterday's raw
source (too low: false perceptions, concealed details). Don't paste only yesterday's
conclusion (too high: the problem hallucinated as solved). The MOO-Map reading discipline
(GLANCE before CARD before SKILL) is level-band etiquette.

And the **fringes attach weakly** (Note 9): weak connections at the band's edges behave
exactly like frame **default assignments** — present unless the current situation
overrides them, because *"weakly activated agents will be less persistent in
cross-exclusion competition."* Fractional attention weights are not an interface gimmick;
they are the difference between a memory and a hallucination.

Note 5 adds the steering wheel: the active band is selected not locally but by **another
agency sending a facilitation signal** — a coarse enhancement of a chosen level band that
can bias the computation up or down, instructing the K-P pair to *"try a more general
method"* or *"pay more attention to the input."* The zoom control on the attention mask is
itself an agent.

## Cross-exclusion: radio buttons, 1979

> *"Most agents are grouped in small 'cross-exclusion' arrangements. Each sends inhibiting
> connections to the others in its group, so that it is hard for more than one to be
> 'active' at a time. This... makes it particularly easy to re-set the state of a system;
> one need only force to 'on' one agent in each cross-exclusion group."*

A cross-exclusion group is a **radio button group**; forcing one member on is clicking it.
A stack of tabbed overlapping windows is a cross-exclusion group whose "active" member is
the front window; the pie-menu gesture that brings any tab's window to the front is the
force-to-on that resets the group. (UI rendering:
[MicropolisCore p-pyramid-attention-overlay](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md).)

Three consequences the memo derives:

- **Persistence for free.** Networks of cross-exclusion groups have *"a kind of built-in
  'short-term memory'"*: force a partial state even for a moment and it tends to persist.
  A window stack remembers its ordering without a memory subsystem.
- **Dispositions.** The persistent pattern across many groups reads, from outside, as a
  *disposition* — a distinctive style of behavior. *"Each P-pyramid may have a repertory
  of such dispositions, defined by pre-activating different subsets of agents."* A
  workspace preset is a disposition: pre-activate a subset of windows and the whole system
  sees Necker-cube-style differently — same graph, different way of seeing.
- **Conflict means zoom out.** In the Minsky-Papert version, two competing members active
  at once make their **whole group drop out**, defaulting control to the next level up:
  *"if a single viewpoint produces two conflicting suggestions... it is often better not
  to seek a compromise, but to seek another, less ambiguous viewpoint."* Contradiction at
  one level of the pyramid is a signal to raise attention to the parent, not to average
  the children.

## K-recursion: pyramids made of pyramids

> *"When forming a new K-node... it will suffice to attach the new K-line AK to just the
> currently-active K-nodes. In effect... new memories are composed mainly of ingredients
> from earlier memories."*

New masks are defined over old masks, not over raw nodes — fewer connections, more
meaningful structure. This is why a skill can cite skills instead of restating them, and
why a K-line vocabulary compounds: every named view becomes a component of the next one.
The K-nodes grow into a **K-pyramid lying against the P-pyramid**, information flowing
down where perception flows up, computation spiraling between them. Memory is a second
pyramid learning to operate the first.

The memo's crossbar answer belongs here too: K-lines don't need point-to-point wiring to
everything. Sparse random-subset coding over a shared bundle (Mooers' zatocoding 1956,
Willshaw's associative nets 1969) suffices — hashing and Bloom filters, proposed as
neuroanatomy. And most pairs of agents *"have no real need to talk to one another"* — the
Society answer to the crossbar problem is the same locality argument against carrier-pigeon
agent architectures
([SPEED-OF-LIGHT-VS-CARRIER-PIGEON](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md)).

## Loops

The graph has cycles — Minsky links to Papert links to Minsky. The P-pyramid handles them
because it is keyed by **path, not node** (the overlay-tree move from
[HALLS-AND-ROOMS](../skills/mind-mirror/HALLS-AND-ROOMS.md#addendum-the-overlay-the-colors-and-the-form)):
one node can appear at several places in the pyramid, at different scales, without
contradiction.

Better: the pyramid can **follow a loop deliberately**, assigning a fresh attention weight
at every lap — recurse down the cycle, shrinking each step, and stop after a few laps. The
truncated spiral *is* the notation for recursion: a human sees the shape and reads "this
repeats"; an LLM reading the serialized pyramid sees the same three shrinking laps and
binds the cycle without walking it forever. Attention decay as a base case.

## Relations to what already exists here

| Concept | Relation |
|---------|----------|
| [MOO-Maps / Semantic Image Pyramid](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) | Object-side resolution ladder (GLANCE→CARD→SKILL→README). The P-pyramid is the **agent-side selection over it**: which object, at which mip level, right now, for P. |
| [K-lines](../skills/k-lines/) | A K-line stores the mask (which nodes, how much: strong in the band, weak at the fringes); a P-pyramid is the mask deployed. Save view = mint K-line; speak name = reopen pyramid. |
| [HALLS-AND-ROOMS overlay](../skills/mind-mirror/HALLS-AND-ROOMS.md) | The lighting rig and the overlay tree of opened views are P-pyramids in fog-of-war costume. Light intensity = attention weight; the facilitation signal is a stage-lighting cue. |
| [moocroworld attention-tree](../skills/moocroworld/ATTENTION-TREE.md) | The operational YAML serialization: depth, fragments, expansion state. Add `agent:` and per-node `attention: 0.0-1.0` and it is a P-pyramid file. |
| Strassmann butterfly diagrams ([mind-mirror](../skills/mind-mirror/HALLS-AND-ROOMS.md)) | A butterfly is a minimal local P-pyramid: P at the head, one level of inbound links on the left wing, outbound on the right. Growing a wing is raising that node's weight. |
| [Society of Mind](https://en.wikipedia.org/wiki/Society_of_Mind) | The memo's own frame: agents in a lattice, inputs from below and the side, outputs upward. P at the tip is not the boss of the network; P is where this particular look-down happens to stand. |
| Context window | The context IS a P-pyramid over the repo: a curated, weighted, hierarchical selection from a graph that is not hierarchical. Context assembly = pyramid construction. Compaction = global attention decay — and the level-band principle says what compaction should keep: the middle. |

## The philosophical point

The network as a whole need not be pyramidal. Neither the filesystem, nor the skill graph,
nor the web, nor a mind is really a tree — but every act of attention makes one. Hierarchy
is not a property of the world; it is the shape of looking. MOOLLM's whole reading
discipline (never load a lower level without the level above) is pyramid construction
etiquette: build the view top-down from P, spend weight where it earns context, let the
rest stay dark and cheap.

And because the pyramid is an overlay — versionable, sharable, nameable — curation becomes
a first-class artifact. A tutorial is a guided sequence of P-pyramids. A code review is two
agents diffing their pyramids over the same graph. A handoff is passing your pyramid to the
next agent so they can get into that old state and handle this one the same way.

## Practical UI counterpart

The interface rendering of all this — tab stacks as cross-exclusion groups, pie-up to
force a window on, fish-eye scale as fractional weight, workspace presets as dispositions
— is specified in MicropolisCore:
[p-pyramid-attention-overlay](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md)
and [PIE-TAB-WINDOWS](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/notes/PIE-TAB-WINDOWS.md).

---

Part of the designs series · [SPEED-OF-LIGHT-VS-CARRIER-PIGEON](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) ·
[MOOPMAP](MOOPMAP.md) · [object-system/SELF-AND-MOOLLM](object-system/SELF-AND-MOOLLM.md) ·
[object-system/HUMANSPLAINING](object-system/HUMANSPLAINING.md)
