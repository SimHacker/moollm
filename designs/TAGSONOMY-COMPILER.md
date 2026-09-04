# The Tagsonomy Compiler

*Don Hopkins · September 2026*

**Thesis:** Nondeterminism belongs at build time. An LLM reads a corpus and proposes the warm
things — titles, synonyms, definitions, tags, parent categories — and the build **crystallizes** them
into a static artifact that is navigable with one lookup, no model, no server, and no API key. When
the taxonomy needs renegotiating you **melt** it back up and recompile.

The pattern is not new and it is not speculative. It has shipped four times in this lineage, between
1977 and 1989, on hardware that could not have afforded anything else. The LLM changes only the warm
end.

---

## The name is already ours

From the Korz discussion, describing CAM-6:

> CAM-6 even shipped the compiler: rules written expressively in Forth, crystallized down into total
> lookup tables. That's exactly the pipeline I want with LLMs — describe the rule in Korz's
> subjective, guarded, dimensional terms, let the model crystallize it into a strict kernel (lookup
> table, or WebGPU compute shader), and when a guard needs renegotiating, **melt it back up and
> recompile.**

**Crystallize** and **melt** are the two operations. Everything below is that pair applied to
meaning rather than to cellular automata rules. The warm end also buys the thing that matters most
for authoring, stated in the same passage: a guard like `neighborhood: glider-head` instead of
enumerating cells — *"Nobody says 'dead cell with three live neighbors'; they say glider."*
Tagsonomy has the identical property. Nobody says "the article whose title matches this string";
they say *the Hubble piece with the exploded diagram*.

## Four receipts

### 1. MDL Zork: aliases intern to one object, and names fit in one word

`makstr.mud` defines three parallel synonym operators, each scoped to its own hash table:

| Operator | Table | Namespace |
|---|---|---|
| `SYNONYM` | `WORDS-POBL` | nouns and general vocabulary |
| `VSYNONYM` | `ACTIONS-POBL` | verbs |
| `DSYNONYM` | `DIRECTIONS-POBL` | directions |

Each works the same way — look the canonical name up once, then point every alias at **the identical
value**:

```mdl
<DEFINE SYNONYM (N1 "TUPLE" N2 "AUX" VAL (WORDS ,WORDS-POBL))
    <COND (<SET VAL <PLOOKUP .N1 .WORDS>>
           <MAPF <> <FUNCTION (X) <PINSERT .X .WORDS .VAL>> .N2>)>>
```

So `north`, `n`, and any other alias are not three entries that need reconciling; they are three
keys interned to one object. Synonym resolution has **no runtime cost at all**, because it happened
at load time.

The five-character limit is the part worth understanding, because it is usually described as
truncation and it is actually a data structure. `PSTRING` packs characters at 7 bits each into a
36-bit PDP-10 word — the print routine walks bit positions 29, 22, 15, 8, 1, which is exactly five
characters. A packed name is therefore **one machine word**, so comparing two names is a single word
compare with no string traversal. The vocabulary limit and the lookup speed are the same design
decision.

### 2. HyperTIES: the pyramid rungs are separate compilation units

Verified on disk, with 1988 timestamps, in the local archive. `compile-all.f` is the build script;
each entry names a unit and then its **title**:

```forth
.compile-definition ./faintobk/faintobk.st0.d
Faint Object Camera
.compile-article ./faintobk/faintobk.st0.a
Faint Object Camera
```

`compiled.f` is the generated FORTH, 5,170 lines, one word per unit. `compiled.exe` is the saved
memory image, 204,592 bytes, dated 1 July 1988. Don's own description of why:

> HyperTIES can subsequently read in the resulting Forth functions, and compile them into memory.
> Then they can be efficiently executed, to produce identical pages as the storyboards interpreted
> from disk, **without the overhead of the formatter reading the storyboards and laying out the
> page.**

Two details generalize. **Definitions and articles compile separately**, keyed by name — so the
abstract rung and the body rung are independently addressable compiled units, which is why
definition previews were fast enough to put on a single click. And the authoring form was
deliberately different from the browsing form: one file per object for editing, "smushed together
into one big file for browsing time," with PostScript tokenized so it would load faster.

**Authoring is interpreted and slow. Browsing is compiled and fast. They are different artifacts.**

See [webtop/hyperties/LINK-RESOLUTION.md](webtop/hyperties/LINK-RESOLUTION.md) for the resolution
protocol this compiles, and note the convergence: Zork used three typed namespaces and HyperTIES
used three typed namespaces, independently, and MOOLLM's plural typed containers are the same
answer a third time.

### 3. CAM-6: expressive Forth down to total lookup tables

A rule written in readable Forth, crystallized into a table indexed by neighborhood state. Total —
every input enumerated, no evaluation at run time. The rule *language* is warm and the shipped
artifact is a table. This is the receipt closest in spirit to the LLM version, because the source
form is genuinely more expressive than the compiled form rather than merely more convenient.

Receipt strengthened, because the artifacts are in this workspace. `CAM6/javascript/CAM6.js` carries
the rules across a hardware original, Toffoli and Margolus's FORTH, Don's C-plus-FORTH simulator,
C++, Python, and JavaScript, with `jsforth.js` shipping a FORTH interpreter in the browser so the
original dialect still runs and `twgl-full.js` present for the GPU hop. The rule definitions survived
every transition; the interpreters were all disposable. And the source's own aside — use *"old rule
tables generated by Forth if you can find them"* — is the melt argument in four words: the cold
artifact outlived its compiler and then became scarce, which is why you keep the warm definition
next to the table instead of shipping only the output.

### 4. Scott Adams: the database outlived every interpreter

Adventure International shipped an **interpreter plus a portable database**, splitting the engine
from the world. The consequence is the one that matters for publishing: the data files still run,
decades later, on interpreters nobody had written yet when the games were authored. Porting meant
reimplementing a small interpreter, never re-authoring the content.

That is the archival argument for crystallizing. A compiled artifact with a documented format
outlives its runtime. A live service does not.

## The ground-up version

The seeds are not documents. They are utterances with a location and a timestamp — and this part is
already designed, in the eBike Safari pack, where it is called something better than "seeds."
[`speech-track.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/speech-track.md)
splits speech into two tiers, and the second one is the compiler's input:

- **Commands** — addressed speech, interpreted immediately. *"Hey ebike, remember here."*
- **Impressions** — unaddressed keywords and exclamations, **laid down now and interpreted later**,
  timestamped onto the same ride track as GPS, photos, scrobbles and gestures.

An impression is a seed precisely because interpretation is deferred. You are riding; you say what
you see; the utterance lands in the architectural and civic soil where it was spoken, and nothing
has been decided about what it means.

Then the growth, also already designed, in
[`semantic-taxonomy-pyramid.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/semantic-taxonomy-pyramid.md):
the LLM compresses payloads into specific and abstract tags with yaml-jazz comments weighted double,
near-duplicate tags merge by embedding distance, and when a cluster's **mass** passes a threshold the
model proposes a parent tag, which becomes a node one level up. No central ontology — *"New meme pees
L0; if popular, parent tag emerges without committee."* A ground-up lexicon out of peer yaml-jazz.

So the metaphor maps onto stages that exist:

| Stage | What it is | Where |
|---|---|---|
| **seed** | a GPS-located, timestamped impression, uninterpreted | `speech-track.md`, [souvenirs](webtop/DISPENSERS-AND-SOUVENIRS.md) |
| **soil** | the street, building, and civic context it landed in | `city-record.md`, the street graph |
| **germination** | LLM proposes tags, synonyms, a definition | `semantic-taxonomy-pyramid.md` |
| **vegetation** | tags accrue mass, merge, coalesce into parents | taxonomy tick |
| **pruning** | human confirms; collisions linted | this document |
| **fruit** | the crystallized artifact: title, synonyms, definition, static index | the build |

And the loop closes, because **fruit contains seeds.** A distilled card is itself plantable
elsewhere — which is transclusion, arrived at from the garden rather than from Xanadu. The
community-garden framing in
[`urban-garden-loop.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/urban-garden-loop.md)
already insists the plot is shared and the harvest is collective credit, which is the right social
default for a corpus many people contribute impressions to.

## Publishing a life's work as a playable adventure

This is the output format, and it is Scott Adams' architecture applied to a biography instead of a
treasure hunt. The corpus compiles to a database; a small interpreter walks it in the browser; the
reader moves through it the way they moved through Adventureland.

The pieces are all present rather than hypothetical. Rooms are directories. Articles have titles,
synonyms, definitions and bodies. Links are phrases in prose that resolve by name. Views are saved,
citable positions. The semantic pyramid supplies **VERBOSE / BRIEF / SUPERBRIEF as semantic zoom** —
the same room described at three detail levels, shipped as a player preference in 1977 and now a
stated requirement of the adventure skill, extended with `GLYPH` and `INFODUMP` at the ends
([`skills/adventure/SKILL.md` § The rung selector](../skills/adventure/SKILL.md#the-rung-selector)).

What makes it a *game* rather than a website is that navigation is the interface and the reader's
path is the record of their visit. What makes it *archival* is that it crystallizes: no server, no
key, no inference at read time, a documented database format, and an interpreter small enough that
someone can write another one in forty years.

Correspondence with Scott exists and he replied — *"BTW I also captured the original Hacker thread
for my biography"* — which is the same instinct from the other direction. See
[`designs/email/letter-to-scott-adams.md`](email/letter-to-scott-adams.md).

## Honest costs

**Crystallized artifacts go stale, and the melt is the expensive direction.** Melting a taxonomy back
up, changing it, and recompiling means every downstream reference resolves differently. Renaming is
cheap only because synonyms absorb it; restructuring a parent tag is not cheap, and the four
historical receipts all had small, closed, hand-authored vocabularies where restructuring was rare.
A grown tagsonomy restructures constantly. **This is the unsolved part**, and pretending otherwise
would be the one dishonest move available here.

**Build-time nondeterminism is still nondeterminism.** Two builds of the same corpus produce
different synonyms and possibly different parents. That is tolerable only if the build output is
committed and diffed as an artifact, so the changes are visible and reviewable, rather than
regenerated silently. Commit the crystal, not just the source.

**Mass-based coalescence rewards volume.** A parent tag emerging because a cluster got heavy means
the taxonomy tracks what people talk about most, not what matters most — the same failure mode as
engagement ranking. Whatever guards against that is a policy decision and belongs in
`territory/taxonomy/policy.yml` beside `merge_tau` and `coalesce_min_mass`, written down and
arguable.

**Generated synonyms drift generic and collide silently**, which is the failure mode already
documented in [webtop/hyperties/LINK-RESOLUTION.md](webtop/hyperties/LINK-RESOLUTION.md): a
reference that resolves to a plausible wrong node. Detectable at build time as a lint, which is the
only reason it is survivable.

**A five-character key was a brilliant fit for a 36-bit word and is a terrible fit for prose.** Do
not cargo-cult the receipts. What generalizes is *intern aliases to one object and compile the
index*; what does not generalize is any specific packing.

---

## Related

- [webtop/hyperties/LINK-RESOLUTION.md](webtop/hyperties/LINK-RESOLUTION.md) — the resolution protocol and the build-time index
- [webtop/hyperties/ARTICLE-SCHEMA.md](webtop/hyperties/ARTICLE-SCHEMA.md) — title, synonyms, definition, body as the node contract
- [webtop/GLYPH-BENCHMARK.md](webtop/GLYPH-BENCHMARK.md) — the smallest rung, and why generated distinctness needs measuring
- [webtop/README.md](webtop/README.md) — the publishing shell this compiles for
- [pie-stack-views/VIEW-STATE-ANCESTORS.md](pie-stack-views/VIEW-STATE-ANCESTORS.md) — views as saved, citable positions
- [email/letter-to-scott-adams.md](email/letter-to-scott-adams.md) — the correspondence
- WWSFF `characters/david-ungar/korz/case-cellular-automata.md` — crystallization targets, compiling Korz to kernels
- WWSFF `apps/ebike-safari/design/` — `speech-track.md`, `semantic-taxonomy-pyramid.md`, `urban-garden-loop.md`, `city-record.md`
