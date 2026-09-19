# The HyperTIES article schema

**An article had a title, a synonym list, a definition, and a body.** Four parts, required by the
markup, in 1988 — and exactly four, because three of the six directives people count are second
spellings aliased to the same field (see below). That schema is the semantic pyramid with an
addressing layer bolted to the front, and it is the single most important thing in this pack.

The schema itself is settled by the storyboard source below. **Authorship of the code that
implemented it is a separate question, and the division of labor was real.** Don wrote the page
formatter (`fmt.c`, `fmt.cps`, `fmt.ps`), the FORTH storyboard compiler, and the Emacs MockLisp
authoring editor. Name resolution lived elsewhere — in the **index manager, which was Bill Weiland's
C code**. The archive holds the receipt, an email from Don to `weiland@bensun`:

> Would it be much trouble to make .h files for the index manager so that I can include them in
> fmt.c? I'm not sure how to deal with including the .c files.

Don is asking the index manager's author for headers so his formatter can call into it. That is the
division of labor, in one sentence: **Weiland owned resolution, Don owned formatting and
compilation.**

And HyperTIES was not one program. It was a bundle of ideas reimplemented across platforms — the PC,
SunView, NeWS, and likely others after Don left — so attributing any mechanism to a single person
misdescribes how it was built. Ben Shneiderman can give the details. See [TEAM.md](TEAM.md), which
needs Weiland added.

## The receipt

From `doc/demos/hyperties.st0`, the first article of the demo database, verbatim:

```
.title
The HyperTIES hypermedia browser

.synonyms
NeWS HyperTIES
HyperTIES
TIES

.definition
NeWS HyperTIES is a hypermedia browser for the NeWS window system, 
under development at the Human Computer Interaction Lab, at the
University of Maryland.

.contents
NeWS HyperTIES is a hypermedia browser for the NeWS window system, 
under development at the Human Computer Interaction Lab, at the
University of Maryland. You're looking at it!
.lines 2

Here are some links to interesting parts of the database to browse. 
.lines 2

=> .~ The Space Telescope in Orbit~ .nl
=> .~ Miscellaneous~ .nl
=> .~ PopupTarget~ .nl
```

Note the article is self-describing: its own definition and the opening of its body are nearly the
same sentence, and the body then says *"You're looking at it!"*

The `.~ name~` form here is the **FORTH prototype dialect** — the dot is a FORTH word and FORTH words
are whitespace-delimited, so the space after `.~` was required by the tokenizer. Weiland's final C
parser accepted the clean `~name~` instead. The archive is prototype-era throughout; see
[LINK-RESOLUTION.md](LINK-RESOLUTION.md) for which form to revive and why.

## Three of the directives are two spellings of one field

**Read the formatter's alias table before counting anything.** From `fmt.f` (and identically in
`foremat.c`), the whole of it:

```forth
alias .left      .line
alias .buttonl   .buttonline
alias .synonym   .synonyms
alias .description .definition
alias .content   .contents
```

So `.description` **is** `.definition` — the same slot, under a second spelling, dispatching to the
same FORTH word. There is no separate longer-prose field, and `ties-doc.txt`, the authoritative
internal spec, documents only `.definition`: *"Starts with the line `.definition`."* The archive
agrees by the strongest available test — **no article anywhere carries both**, because they cannot;
they are one field. Same for `.synonym`/`.synonyms` and `.content`/`.contents`. The index manager
makes the equivalence explicit in its parse, accepting both in one command string:

```c
FindCommand ("synonyms synonym ", &start, &args, &next, storyboard);
```

Which is why the opening sentence of this document is exactly right and the census table below it
used to disagree with it: **four parts, not six.**

## Directive census

Counted across `archive/` and `ties/` in `Leela/git/lloooomm-imports`, 264 `.st0` files, editor
backups (`.st0~`, `.BAK`) excluded because they double-count. Alias pairs summed, since the parser
sums them:

| Field | Uses | Spellings | Role |
|---|---|---|---|
| `.title` | **254** | — | canonical article name; one per article, and the index's principal |
| `.definition` | **246** | `.definition` 190 + `.description` 56 | the mandatory abstract shown on single click |
| `.target` | **187** | — | arbitrarily-shaped graphical regions; embedded menus inside pictures |
| `.synonyms` | **136** | `.synonyms` 107 + `.synonym` 29 | alternate names resolving to this article |
| `.contents` | **118** | `.contents` 108 + `.content` 10 | the body |
| `.picture` | **38** | — | an image, itself a resolvable name |

264 storyboards, 254 with a title, **246 carrying a definition, 136 declaring synonyms.** The schema
was the working grain of the system, not an aspiration. Reproduce with:

```bash
cd Leela/git/lloooomm-imports
find archive ties -name '*.st0' -print0 | xargs -0 rg --no-filename '^\.definition\b' -o | wc -l
```

`provenance:` counted 19 Sep 2026 from the archive on disk. Earlier revisions of this table gave
261/197/112/62/186 and listed `.description` as a separate "longer prose" field — the field was an
alias, and the totals came from a file set that included backups.

## The index manager resolves three namespaces, not one

Weiland's index manager does not index documents. It indexes **documents, pictures, and targets**,
in parallel, and that is the entire structure (`master-index.h`):

```c
typedef struct master_index
    {
    struct index *documents, *pictures, *targets;
    }
    MASTER_INDEX;
```

So a name resolves to a storyboard, *or* to a picture, *or* to a target — a target being an
arbitrarily-shaped live region inside a picture, which is to say **an embedded menu with pop-up
shapes, an applet addressed by name.** One resolution mechanism, three kinds of destination. The
generated master index is one file with `----- PICTURES -----` and `----- TARGETS -----` section
markers (`make-index.c`), so the three namespaces are visible in the artifact.

Each index distinguishes canonical names from aliases in its own counters (`index.h`):

```c
typedef struct index
    {
    long n_entries;
    long n_principals;
    struct tree *root;
    }
    INDEX;
```

**`n_principals` is titles; `n_entries` is titles plus synonyms.** Aliasing is not a layer on top of
the index — it is in the index's shape, which is what makes resolution by synonym cost the same as
resolution by title.

And the master index is itself an article, reachable by a synonym (`make-index.c`):

```c
fputs (".title\nMaster Index\n\n.synonyms\n!index\n\n.content\n\n", master_index);
```

A generated article, named `!index`, in the same namespace it describes. The index is in the
encyclopedia.

## Why synonyms are the load-bearing part

The 1991 paper drops a phrase almost in passing, while explaining why graphical links are harder to
author than textual ones:

> the author must laboriously link targets to their references (**they are not "self-naming", as in
> the text case**)

Text links are *self-naming*. The synonym list is the mechanism that makes that true. You write the
sentence you meant to write — "the telescope's faint object spectrograph", "TIES", "the Interactive
Encyclopedia System" — and the system resolves the phrase against article titles **and their
synonyms**. The author is not marking up links. The author is writing prose, and the prose links
itself.

That inverts the web's model completely:

| | HyperTIES | The web |
|---|---|---|
| To link | write the phrase | write the phrase, then find and paste a URL |
| Address | a name, with declared aliases | a location, with no aliases |
| Renaming a thing | add a synonym; old references keep working | every inbound link breaks |
| Two names for one thing | first-class, declared | two pages, or a redirect you must remember to create |
| Author burden | declare your aliases once, per article | resolve every reference, every time, forever |

Borretti's complaint that 80% of his wiki links were structural busywork and the rest were duty-links
is a symptom of the second column. When linking costs a lookup, you either skip it or you do it
mechanically. When the phrase resolves itself, you link by writing.

## It is the pyramid, and it was mandatory

Line up the schema against the ladder gwern describes and against what MOOLLM already has:

| Pyramid rung | HyperTIES, 1988 | MOOLLM |
|---|---|---|
| glyph / icon | `.target` — a shaped region that pops out | emoji or SVG, pie-slice sized |
| title | `.title` | `name` |
| **abstract** | **`.definition` — required** | `GLANCE.yml`, `description` |
| longer summary | `.description` | `CARD.yml` |
| full text | `.contents` | body, `README.md` |
| addressing / aliases | **`.synonyms`** | K-line names, latent-space aliases |

The rung the web dropped is the abstract, and the reason gwern's popups feel like a revelation is
that he reconstructed it by hand, per link, as annotations. HyperTIES got it for free because the
schema refused to let an article exist without one.

**And the rung nobody has rebuilt at all is synonyms.** No modern system in this hub has it. Not
gwern.net, not Roam, not Obsidian, not Notion, not Cartesian. Wikipedia has redirects, which is the
same idea implemented as a workaround. This is the gap with the clearest specification and the least
competition.

## What this means for the webtop

1. **Adopt the four-part schema as the node contract.** Title, synonyms, description, body. A node
   without a description is invalid — and since the LLM can generate one, invalid never has to mean
   blocked. The author writes the rung they care about; the schema guarantees the rung exists.

2. **Resolve links by name, not by path.** Write the phrase; let the resolver match titles and
   synonyms across the corpus. Paths remain, for the machine, underneath. The protocol — the `~name~`
   markup, scope-walking resolution, type-from-position, and the build-time index — is
   [LINK-RESOLUTION.md](LINK-RESOLUTION.md).

3. **Generate synonym candidates, let the human confirm.** This is the single best fit for LLM
   assistance in the whole design: proposing the aliases under which a thing might be mentioned is
   exactly what a language model is good at, and confirming a list is cheap. Nenex's
   imitation-learning loop applied to something narrow and verifiable.

4. **Synonyms make renaming survivable,** which is what a corpus meant to outlive its author needs.
   Add the old name as a synonym and nothing breaks. This is linkrot defense pointed inward.

5. **Ambiguity gets a pie menu.** When a phrase resolves to more than one article, that is not an
   error — it is a small set of choices at a known position. Same gesture as "same window, other
   window, new window."

## Local archive

Primary sources are on disk, outside version control, in the LLOOOOMM import tree:

| What | Where |
|---|---|
| Storyboard source (`.st0`) | `Leela/git/lloooomm-imports/ties/doc/demos/hyperties.st0`, `archive/HyperTIES/news-paper/hyperties.st0` |
| Markup language spec (scan) | `lloooomm-imports/ties/scans/HyperTIESMarkupLanguage.pdf` |
| Database format (scans) | `HyperTIESDatabase.pdf`, `NewHyperTIESDatabaseFormat.pdf` |
| Emacs authoring tool (scan) | `EmacsAuthoringToolsForHyperTIES.pdf` |
| UI design, research directions, notebook | `UIDesignForHyperTIES.pdf`, `ResearchDirectionsForHyperTIES.pdf`, `HyperTIESNotebook.pdf` |
| The 1991 paper | `LookBackAtHyperTIES.html`, `HyperMediaHyperTIESArticle.pdf` |
| Database index | `HyperTIESDatabases.xml` |
| Format + FORTH compiler + index namespaces | `archive/HyperTIES/ties.doc.txt` — the authoritative internal spec |
| Don → Weiland on the index manager | `archive/HyperTIES/to.bill.txt` |
| Code | [donhopkins.com/home/ties/doc/ties/](https://donhopkins.com/home/ties/doc/ties/) |

**Caution for anyone extending this:** the `lloooomm` trees also contain *synthetic* character
material about Ted Nelson and Xanadu — worm poetry, concerts, chess automata. That is generated
fiction from the LLOOOOMM experiments, not primary source. Do not cite it as history.

↑ [hyperties](README.md) · [HN archive](HN-ARCHIVE.md) · [team](TEAM.md) · [webtop hub](../README.md)
