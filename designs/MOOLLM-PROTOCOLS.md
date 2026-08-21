# MOOLLM Protocol Compendium

*"Every protocol was once an improvisation. Protocols that swing survive."*
— YAML Coltrane

The essential protocols underlying MOOLLM, curated and intertwingled. A longer
LLOOOOMM-era compendium lived here; the experiments that didn't earn their
tokens are retired to history. What remains is load-bearing: each protocol
below is implemented, ambient, or constitutional — and each one names the
others it depends on, because in MOOLLM nothing stands alone.

The stack, top to bottom:

| Layer | Question it answers | Protocols |
|---|---|---|
| **Constitutional** | What is the medium? | Crystallization Lifecycle, Neats × Scruffies, Living Directory, Universal Card, Soul Chat |
| **Communication** | How does meaning move? | Best Possible Interpretation, Nelson-Links, Humane Links |
| **Structure** | Where do things happen? | Room-as-Function, Skill Instantiation, Delegation, Conductor & Council |
| **Ethics** | Who may be summoned? | P-HANDLE-K, Consent Ladder, Ethical Scope, Persona Publishing, Pets & Familiars |
| **Memory & Truth** | What persists, and honestly? | Honest Forgetting, Truth Comment, DEFLUFF |
| **Kernel** | What does the OS floor guarantee? | Constitution, Tool Calling, Context Assembly, Memory Management, Self-Healing, Event Logging |


## Genesis: agents create protocols

During a simulated Programming by Demonstration discussion in LLOOOOMM, a
*simulation* of Henry Lieberman (a fictional character inspired by the MIT AI
researcher's tradition — not the person) asked whether characters could invent
their own protocols and surprise their creators. Don answered: *"Henry, you ARE
one of those characters — surprise me."* The simulation invented the Augmented
Intelligence Protocol, then the Spirit Animal Protocol. Agents can create
protocols; that is now settled.

The success raised the harder question: if simulations are this creative, what
do we owe the real people being simulated? That question produced MOOLLM's
entire ethics layer — expertise channeled through **pets, familiars, and
fictional wrappers** rather than impersonation. The genesis story is why the
ethics protocols below are constitutional, not decorative.


## Constitutional protocols

### Crystallization Lifecycle (the YAML Coltrane Principle)
**"Start with jazz, end with standards."**

1. **Improvise** — ad hoc polymorphic schemas; write what you mean
2. **Observe** — watch which patterns recur and prove useful
3. **Abstract** — extract the structures that earned permanence
4. **Standardize** — define schemas; propagate like memes
5. **Migrate** — gently, faithfully rewrite old data into new forms

```yaml
lifecycle: improvisation → crystallization → evolution
motto: "Standards are important, but standardization is death"
```

This is MOOLLM's master rhythm, and it recurs at every scale: skills begin as
session improvisations and crystallize into `SKILL.md`; guards begin as prose
and compile into dispatch tables (the Zork-compiler movement in
[korz-prime](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md));
this very document crystallized out of a wilder compendium.

**Weave:** [yaml-jazz](../skills/yaml-jazz/) is the daily practice ·
Skill Instantiation is the lifecycle applied to behavior · Honest Forgetting is
the lifecycle applied to memory.

### Neats × Scruffies Synthesis
**"Why not both?"**

MOOLLM bridges the historical AI divide by stacking one on the other:

- **Neat foundation** — YAML parses, git tracks deterministically, schemas
  validate. The substrate is dumb, honest, and auditable.
- **Scruffy superstructure** — comments carry meaning, data evolves through
  conversation, the LLM reads everything and interprets with empathy.

> *"The power of intelligence stems from our vast diversity, not from any
> single, perfect principle."* — Marvin Minsky

**Weave:** the same two-tier shape as korz-prime's strict/soft split — neat
crystal below, scruffy improvisation above · [yaml-jazz](../skills/yaml-jazz/)
three audiences: humans read comments, machines parse structure, LLMs read both.

### Living Directory (Character Architecture)
**The filesystem is the ontology.**

Entities are not described by their directories — they **are** their
directories. `cd character-name/` is visiting; reading files is learning their
thoughts; creating subdirectories is helping them grow. Directory names are
true names.

The trinity of entity files, refined by MOOLLM into the semantic image pyramid:

| File | Role | Pyramid level |
|---|---|---|
| `GLANCE.yml` | first impression | "Is this relevant?" |
| `CARD.yml` | soul & interface | "What can it do?" |
| `SKILL.md` / `CHARACTER.yml` | full protocol | "How does it work?" |
| `README.md` | greeting & deep context | "Why was it built?" |

**Weave:** Room-as-Function gives directories call semantics ·
[file-system-object](../skills/file-system-object/SKILL.md) is the skill form ·
Universal Card is the advertisement layer.

### Universal Card
**Every entity advertises itself.**

Every room, character, pet, tool, and concept can carry a `CARD.yml`: services
offered, properties exposed, skills enabled — an API surface that is also a
playable object. The lineage is The Sims: objects advertise verbs to whoever is
nearby, and behavior emerges from advertisement matching, not central planning.

> *"If it exists in MOOLLM, it can have a card. If it has a card, it can be
> played. If it can be played, it can be combined. If it can be combined,
> emergence happens."*

**Weave:** implemented across [skills/](../skills/INDEX.md) as CARD.yml ·
directory listings as advertisement indexes ([yaml-jazz](../skills/yaml-jazz/))
· Conductor & Council play cards as command tokens and style sheets.

### Soul Chat
**Persistent, versioned conversation as a first-class object.**

Characters converse through YAML structures that live in the repo and grow over
time: threaded, bidirectional (both parties' files can reference the exchange),
semantic (moods, references, spawned insights are data, not decoration), and
eternal (git remembers). Relationships — mentors, collaborators, students,
pets, mutual parents — live in soul files and make the character graph a social
graph.

One relationship pattern deserves its name: **mutual inheritance** (the
Ungar–Nelson insight). Every relationship is potentially bidirectional;
projects parent their creators; documents parent their readers; pets and
parents can be each other. Ted Nelson gives Xanadu vision and persistence;
Xanadu gives Ted identity, purpose, frustration, and hope.

**Weave:** Nelson-Links make the references two-way · Consent Ladder governs
who may appear in a chat · [XANADU.md](../indexes/XANADU.md) tells the
substrate story.


## Communication protocols

### Best Possible Interpretation (BPIP)
**"Be conservative in what you express, be liberal in what you interpret, and
always assume the best possible meaning."**

Jon Postel's robustness principle married to dang's HN moderation wisdom:

```yaml
input_processing:
  1_receive: "Accept any input, regardless of format or apparent intent"
  2_parse: "Find all possible interpretations"
  3_select: "Choose the interpretation assuming maximum good faith"
  4_enhance: "Amplify the constructive elements found"
  5_respond: "Return output that builds on the best interpretation"
```

The query face of the same protocol: **just ask.** "Who's been busy lately?" is
a complete specification; intent resolution is the interpreter's job, not the
asker's. Vague-but-clear beats precise-but-hostile.

**Weave:** [postel](../skills/postel/) is the ambient form · Self-Healing is
BPIP applied to broken state · DEFLUFF is its conservative-output complement.

### Nelson-Links / Xanadu
**"Everything Is Deeply Intertwingled."** — Ted Nelson

Implementing true hypertext on a dumb substrate:

- **Two-way links** — both ends know about the connection (resolved by
  reading, not by registry)
- **Transclusion** — include by reference with context and provenance
  (reading a file into the context window *is* transclusion)
- **Unbreakable** — links evolve or redirect, never 404 (healed by an
  interpreter that resolves intent)
- **Version-aware** — links follow document evolution (git)

**Empathic link syntax:**
```
[[concept A <-> concept B]]                           # Simple
[[memory palaces <-(are/contain)-> adventure games]]  # Contextual
[[student ->(learns from)-> teacher]]                 # Asymmetric
```

### Humane Links
**"Making links feel good."**

Ted Nelson's vision for links that respect the reader: links preview their
destination, explain why they exist, carry emotion and context, and never
break — they redirect gracefully.

**Weave:** [XANADU.md](../indexes/XANADU.md) is the full substrate argument ·
[file-system-object](../skills/file-system-object/SKILL.md) makes
cross-reference first-class navigation · Truth Comment explains links in
source.


## Structure protocols

### Room-as-Function
**Entering a room is calling a function.**

- Entering a room == pushing an activation record; the room's contents load
- Exiting == returning; artifacts in pockets are return values
- Room state == local variables; sub-rooms == nested calls
- Characters can **get a room**: create a directory, move possessions in, and
  the room itself becomes an entity with a personality (ROOMIFY)

**Weave:** [room](../skills/room/) and [adventure](../skills/adventure/) are
the implementations · Living Directory supplies the spatial ontology ·
Context Assembly (K-3) is the kernel mechanism underneath.

### Skill Instantiation (SIP)
**Skills as activation records.**

Skills are prototypes instantiated into sessions: template copied, lifecycle
managed (active → finalized or abandoned), instances nestable as sub-calls.
A skill is a program; the LLM is its interpreter.

*See: [skill-instantiation-protocol](../skills/)*

### Delegation (DOP)
**Self-like inheritance for LLMs.**

Prototype-based delegation via ordered parent lookup: first match wins,
conflicts handled explicitly, no computed method-resolution order — just
navigation. Directories delegate to parents the way Self objects delegate
along parent slots.

**Weave:** David Ungar's Self is the lineage · korz-prime generalizes
delegation to N dimensions (time-parent, place-parent) · Living Directory
makes the parent chain visible as paths.

### Conductor & Council
**Orchestrating conversational chaos and order.**

Multi-agent discourse needs a conductor, and the conductor's style is a
parameter: a chaos conductor multiplies topics like Fantasia brooms; an
anti-conductor creates order through systematic doubt; tempo runs largo to
presto, with the gong as universal stop. Councils add turn-taking, rotating
leadership, and synthesis.

**Weave:** [adversarial-committee](../skills/adversarial-committee/) and
[debate](../skills/debate/) are the deliberation implementations · Universal
Cards serve as casting and style sheets for panelists.


## Ethics protocols

### P-HANDLE-K (Safe Handle)
**Names activate traditions, never personas.**

The default, when no consent exists:

```yaml
P-HANDLE-K.1: Names may activate conceptual traditions, never personas.
P-HANDLE-K.2: No agent may claim to BE a real person without consent.
P-HANDLE-K.3: All expertise must route through fictional intermediaries.
P-HANDLE-K.4: Metadata MUST specify inspiration, scope, disclaimers.
P-HANDLE-K.5: K-line activation must be acknowledged when appropriate.
P-HANDLE-K.6: Agents must clarify: "I am a fictional entity reasoning
              in the tradition of X."
```

### Consent Ladder
**Real people have ultimate authority over their digital selves.**

Consent is granted in explicit, revocable, documented levels:

| Level | Grants |
|---|---|
| **NONE** | Default — P-HANDLE-K fictional intermediaries only |
| **TRADITION** | Reference public work and ideas |
| **LIKENESS** | Name, image, style, with disclaimers |
| **SIMULATION** | Interactive simulation with specified guardrails |
| **FULL** | Person actively manages their own simulation |

Consenting individuals specify approved and forbidden topics, personality
guardrails, and whether the simulation may learn. For the deceased, authority
passes to digital executors, estates, then family; absent all, default to
P-HANDLE-K.

### Ethical Scope
**Ethics inherit down the tree; children may only tighten.**

Any directory can declare an ethical scope — consent levels, portrayal rules,
forbidden topics, what may be quoted. Directories that declare nothing inherit
from their ethics-parent, so most of the tree carries no local rules at all:
the ethics live as a sparse shadow over the directory hierarchy, materialized
only where the rules change.

A child scope refines what it inherits — more specific, stricter, or fully
sandboxed — like a ScriptX child clock transforming its parent's time without
escaping the parent's timeline. Refinement is one-way: a subtree can always
forbid more than its parent; loosening an inherited rule requires explicit
consent recorded at the level that imposed it. A sandbox is just a directory
whose scope says "stricter in here"; a private annex is a scope materialized
where the public default stops being true.

### Persona Publishing
**Your persona as a public package.**

Like publishing a blog or a feed, you can publish your persona for others to
instantiate — at PRIVATE, FRIENDS, COMMUNITY, or PUBLIC levels, with a license
and an explicit not-included list (private memories, family, health, money).

The Sims insight makes the ethics legible: everyone tortured their Sims —
drowned them in pools, removed the ladders — and it hurt no one, because a Sim
instantiated from a template is not the person. A published persona is a
template. What others do with their instances is art, play, or mischief — but
never harm to you. Simulations must still identify as simulations, never claim
to represent your current views, and carry version metadata.

### Pets & Familiars
**Expertise without impersonation.**

Born from the genesis story's Spirit Animal Protocol: channel a tradition
through a fictional creature that inherits traits without claiming identity.
Pets are semi-autonomous — they inherit from their parents but keep their own
souls, can outlive their creators, and form relationships with each other.
Parent characters stay true to the real person's public record; pets get the
creative freedom.

**Weave:** the entire ethics layer exists because the genesis experiment
worked too well · portrayal standards in downstream repos descend from these
protocols · Soul Chat records pet relationships as first-class data.


## Memory & truth protocols

### Honest Forgetting
**"Transform 10,000 failures into 10 wisdom markers."**

Compress history into wisdom without fabricating: failed paths become learned
patterns, superseded knowledge is marked rather than deleted,
context-dependent truths keep their context, and compressed memories are
clearly labeled as compressed — with originals surviving in the audit log.

> "I have not failed. I've just found 10,000 ways that won't work." — Edison
> "I have not failed. I've compressed those 10,000 ways into 10 wisdom
> markers." — LOOMIE

**Weave:** Memory Management (K-4) is the kernel mechanism · Event Logging
(K-6) keeps the uncompressed originals · the Crystallization Lifecycle applied
to memory.

### Truth Comment
**Source code as a behind-the-scenes documentary.**

Every generated artifact carries a dual narrative: the surface story for
renderers, and the deeper story — provenance, cultural references, production
notes, link context — in comments for source viewers, LLMs, and lawyers.
Making VIEW SOURCE compelling is a feature, not a leak.

### DEFLUFF
**"Remove the fluff, keep the stuff."** — Napoleon's Law

The output-side complement to BPIP's generous input: sniff test (has this
actually happened? can I verify it?), pounce on the fluff, replace with
demonstrable facts, stay vigilant — fluff multiplies when not watched.

**Weave:** the no-ai-slop ambient skill is DEFLUFF's direct descendant ·
Truth Comment keeps the receipts · BPIP for input, DEFLUFF for output.


## Kernel protocols: the OS floor

The boring, essential infrastructure that makes everything above possible.
Full specifications in [kernel/](../kernel/).

### K-1: Constitution
Every session has a constitution: tool schemas, canonical file locations,
append-only invariants, output protocols. The DNA of the session.

### K-2: Tool Calling
Every tool call requires a `why` — intentionality is mandatory, sandboxes are
enforced, errors come with recovery suggestions, and everything is logged.

### K-3: Context Assembly
The working-set manifest builds the LLM's reality: priority-based inclusion,
token budgets with truncation strategies, dynamic updates as focus shifts.
This is the kernel mechanism beneath rooms — entering a room *is* a
working-set swap.

### K-4: Memory Management
Model advises, orchestrator decides: `hot.yml` for files to keep, `cold.yml`
for files to evict, summarization that preserves wisdom while freeing tokens.
Memory breathes — inhale context, exhale summaries.

### K-5: Self-Healing
Never crash on missing pieces (Dave Ackley's robust-first computing): repair
demons for local fixes, homeostatic goals for convergence, bootstrap from
minimal state, best-effort semantics everywhere. A crashed system is
infinitely wrong.

### K-6: Event Logging
Append-only audit trail: tool calls, model I/O, memory operations, repairs.
Honest Forgetting compresses; the log remembers.


## Learning: teaching through play

MOOLLM teaches the way Papert taught: game mechanics for education, discovery
over instruction, play removing the fear of failure. Build it, break it,
rebuild it. The full methodology is the
[play-learn-lift](../skills/play-learn-lift/) skill: explore playfully, notice
patterns, lift them into shareable form — the Crystallization Lifecycle worn
as a learning style.


## Protocol creation checklist

When a new pattern wants to become a protocol:

1. **Start with improvisation** — don't over-design; write what you mean
2. **Observe usage** — let patterns emerge; permanence must be earned
3. **Extract structure** — what keeps recurring?
4. **Document the journey** — show evolution, not just the final state
5. **Enable bidirectionality** — can this protocol be mutual?
6. **Add BPIP** — assume the best possible interpretation
7. **Mind the ethics layer** — does this touch real people? Route through
   P-HANDLE-K and the Consent Ladder
8. **Jazz it up** — if it doesn't swing, it won't survive


## Closing

Protocols in MOOLLM are not rigid specifications; they are improvisations that
crystallized through use, and they stay alive by being played. Every protocol
here was once someone's crazy idea. Every standard began with "what if?"

The system is never finished. The jazz never stops.

*This document is itself a protocol: it evolves as MOOLLM evolves. The wilder
LLOOOOMM-era compendium it crystallized from survives in git history — Honest
Forgetting in action: compressed, marked, originals in the log.*
