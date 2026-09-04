# Selfish link resolution — bringing back `~HyperTIES Links~`

The schema ([ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md)) says *what* a node declares. This is the protocol
for *how a name finds it*. The claim: MOOLLM already has every piece, and the missing part is one
markup form plus a build step.

## The markup — two versions, and the one to revive is the later one

There were **two link syntaxes**, and the distinction matters because the earlier one carries a
parser artifact that the later one removed.

| Version | Syntax | Why |
|---|---|---|
| FORTH prototype (Don Hopkins) | `.~ phrase~` | The dot directive is a FORTH word, and FORTH words are whitespace-delimited — so `.~` had to be its own token, which **required the space** after it. A parser constraint, visible in the authoring syntax. |
| Final C parser (mostly Bill Weiland) | `~phrase~` | No FORTH tokenizer, so no quirk. The delimiter is just the delimiter. |

Per Don, who wrote the FORTH formatter: the space in `.~ phrase~` existed *for simplicity's sake*,
because the FORTH word parser needed it. Weiland's C version supported `~phrase~` "without the
quirks of forth syntax."

**So the archive is written in the prototype dialect and the shipped system used the clean one.**
Everything quoted from `.st0` files below is FORTH-era, which is why the dots and spaces are there.
The form worth reviving is `~phrase~` — and it is what this document's title already says, which was
luckier than it was informed.

The general lesson is worth keeping, because it recurs: **an implementation's tokenizer leaked into
the syntax authors had to type, and the rewrite's main user-facing improvement was deleting that
leak.** Any markup this corpus proposes should be checked for the same failure — is this character
here for the reader, or for my parser?

### The prototype dialect, verbatim from 1988

The Space Telescope database, `ties/newdb/introduc/introduc.st0`:

```
.para
     Called the .~ Edwin P. Hubble Space Telescope~, the new observatory is
a NASA-wide and international .~ cooperative effort~.  Its name honors
Edwin P. Hubble (1889-1953), who discovered that the universe extends
far beyond the Milky Way galaxy.

.para
     The .~ Hubble Space Telescope~ will weigh about 25,000 pounds (11,300
kg) and will have a length of 43 feet (13.1 m) and a diameter of 14 feet
(4.26 m).  Its major components are an .~ optical telescope assembly~,
five .~ scientific instruments~, and a .~ support systems module~.
```

**That is the whole argument, and it is a paragraph of ordinary prose.** No URLs, no paths, no IDs.
"a NASA-wide and international *cooperative effort*" is a sentence a science writer would write
anyway; the only authoring act is deciding that the phrase already sitting there is a link. "Edwin P.
Hubble Space Telescope" and "Hubble Space Telescope" both resolve to the same article because one of
them is a declared synonym — the author writes whichever name the sentence wants and does not
reconcile them.

Corpus census, across 264 storyboard files in the local archive: **830 link references, 429
distinct.** A menu-style form also exists — bare `~name~` on its own line, used for the front page's
list of places to browse — but the inline prose form is 798 of the 830 uses. Links were overwhelmingly
things said in sentences, not lists of destinations.

That the standalone menu form is already the bare `~name~` is a hint that the dot was never wanted:
where FORTH did not need to tokenize a directive mid-paragraph, the syntax was clean even in the
prototype.

## Resolution was typed, and that is the part to steal

`ties.doc.txt` documents the index as **three namespaces**, not one:

```
** index
  3 namespaces of index entries
  storyboard names (.st0)
  image names (.in0)
  target names (.tn0)
```

So `~Founders~` in article position and `Founders` in image position were separate lookups that could
not collide. Resolution was scoped **by the type of thing being referenced**, and the type came from
the syntactic position of the reference.

MOOLLM already has this and calls it something else: plural typed containers
([`skills/file-system-object/SKILL.md`](../../../skills/file-system-object/SKILL.md)). `characters/`
declares a namespace of characters; `rooms/` declares a namespace of rooms. Weiland's three
namespaces generalize to *one namespace per plural container*, which means the type discipline is
already enforced by the directory structure. Nothing to build.

## The protocol

Four rules. Each maps onto machinery that exists.

**1. A node declares its names.** `title` plus `synonyms` in the node's marker file — `GLANCE.yml`
for the cheap case, `CARD.yml` when the node has behavior. This is the `.title` / `.synonyms` pair,
relocated:

```yaml
name: The Rubric Forge
synonyms: [rubric forge, the forge, criteria workshop, where weights get argued]
```

**2. A reference is a name in a scope.** `~rubric forge~` resolves by the walk MOOLLM's resolver
already performs for bare skill names: check the enclosing directory, then its parent, then outward
to the mounted repo roots, closest match winning. That is Self's parent-slot lookup and DOP's
delegation chain — the *selfish* part. A name is not a global identifier; it is a message sent into a
lexical scope, and scope decides what it means. Two rooms can both say `~the forge~` and mean
different forges, correctly, with no namespacing ceremony.

**3. Type comes from position, not from the author.** A reference inside a room's `exits:` resolves
in the rooms namespace. One in `npcs:` resolves in characters. One in running prose resolves in the
document namespace and falls outward. The author writes the phrase they meant; the container supplies
the type.

**4. Ambiguity is a choice, not an error.** When a name resolves to several nodes in scope, present
them — a pie menu at the point of reference, since it is a small ordered set at a known position. The
deeper answer is PSIBER's definition editor
([`pie-stack-views/PERIPHERAL-VIEWS.md`](../../pie-stack-views/PERIPHERAL-VIEWS.md)): *"editable
references to every definition of the name on the dictionary stack."* One name, every binding, in
scope order, all openable. HyperTIES and PSIBER independently arrived at the same answer, in the same
lab, in the same two years.

## Resolution as ranked results: the Sims advertisement model

Rule 4 generalizes past links. **Method resolution should be a ranked candidate list with a human in
the loop** — search-engine results rather than a silent dispatch — and the corpus already has the
scoring model for it: Sims object advertisements. An object broadcasts what it offers, the advert is
*scored* against the actor's state, and the actor picks among the top few. The scores are the ranking
function, and they are inspectable, which is why Sims behavior was debuggable at all.

Applied here, a name or a method call produces candidates ranked by the same factors resolution
already uses — scope proximity first, then namespace match, then declared specificity, then recency
or usage. The ranking is not new work: **it is the ordering the automatic resolver would have used
anyway, rendered instead of hidden.** Automatic dispatch is the special case where the top candidate
wins by enough margin to skip the menu.

This is not speculative. The 1988 authoring tool did exactly this, building three completion
buffers — one per namespace — by walking the index stack from the top down so nearer names ranked
first, and handing the author the list ([EMACS-INDEX-MANAGER.md](EMACS-INDEX-MANAGER.md)). What is
new is showing *why* each candidate ranked where it did, which the Sims model supplies and a
completion list did not.

The payoff is that ambiguity becomes a feature with an interface instead of an error with a
stacktrace, and the human's pick is training data: a chosen candidate is a disambiguation you can
record as a synonym, which turns the menu into a one-time cost per phrase.

### Each candidate needs a title *and* a description

A ranked list of bare names is not enough to choose from, and the interfaces that solved this
already know the answer: **title on the item, description in a companion pane.** Search results put
a snippet under each hit. The browser's smart URL bar dropdown puts the page title on one line and
the URL, or the matched text, on the next. HyperTIES itself had the mechanism — the `.definition`
field, [compiled as a separate object](EMACS-INDEX-MANAGER.md) precisely so a summary could be shown
without loading the article.

For pie menus this is a real constraint rather than a detail, because a pie item is a short label at
a fixed angle and has no room for a snippet. The resolution is the one HyperTIES and NeWS both used:
**the pie carries the titles, and a description window carries the detail for whatever is currently
under the cursor.** Tracking a pie item pre-selects it, and pre-selection populates the description
pane — so browsing the menu is browsing the summaries, and the commitment only happens on release.
That is the definition-preview interaction (single click summarizes, double click follows) relocated
into the menu, and it means the candidate list can be *understood* before it is chosen.

Two consequences worth building for. The description pane is a [peripheral
view](../../pie-stack-views/PERIPHERAL-VIEWS.md) and should be addressable like any other, so a
disambiguation menu's descriptions can themselves be cited. And the summary shown there is a
[rung selector](../../../skills/adventure/SKILL.md) choice — `SUPERBRIEF` for a crowded pie,
`BRIEF` for a short one — which makes the pane's content a view parameter rather than a hardcoded
field.

## The build step is the whole trick

Name resolution at read time needs an index. Weiland wrote one in C; `ties.doc.txt` then describes
what HyperTIES did with it, and this is the part worth quoting at length because it is the
adventure-compiler move stated plainly in 1988:

> The storyboard interpreter is capable of compiling storyboards into Forth programs that call low
> level formatting commands to describe pages to the NeWS server. … HyperTIES can subsequently read
> in the resulting Forth functions, and compile them into memory. Then they can be efficiently
> executed, to produce identical pages as the storyboards interpreted from disk, **without the
> overhead of the formatter reading the storyboards and laying out the page.** … The memory image of
> the HyperTIES Forth system, loaded with all the compiled storyboards of a database, can be saved
> out to disk.

Authoring is interpreted and slow; browsing is compiled and fast; the compiled form is a saved image.
Don's email to Weiland describes the same split in the data: a **"broken apart" form for authoring
time** — one file per object, named by object name — which "can be smushed together into one big file
for browsing time," with a filter that tokenizes the PostScript "so it will be smaller and load
faster."

Applied here: **an LLM proposes synonyms at build time; the build emits a static name → path index;
run time is a lookup with no model in the loop.** The general pattern, its three other historical
receipts, and the honest problem of restructuring a compiled taxonomy are in
[TAGSONOMY-COMPILER.md](../../TAGSONOMY-COMPILER.md). Nondeterminism is paid once, by the author, at
compile time. The published corpus browses with no server and no API key — which is the requirement
that makes this publishable as an artifact rather than a service.

## What each layer costs

| Layer | Who does it | When | Determinism |
|---|---|---|---|
| Write `~the phrase you meant~` | author, while writing prose | authoring | n/a |
| Propose synonym candidates | LLM | build | nondeterministic, human-confirmed |
| Emit name → path index | build script | build | deterministic |
| Resolve a reference | index lookup + scope walk | read | deterministic, offline |
| Disambiguate | reader, via pie menu | read | reader's choice, recorded as a view |

The last row is the join with the view layer: which binding a reader picked is itself testimony
([`pie-stack-views/VIEW-STATE-ANCESTORS.md`](../../pie-stack-views/VIEW-STATE-ANCESTORS.md)).

## Honest costs

**Synonym collision across a large corpus is the real risk, and it fails silently.** The more
aliases each node declares, the more often two nodes claim one phrase. Scope limits the blast radius
but does not eliminate it, and the failure mode is the bad one: a reference resolves to a *plausible
wrong* node, so the page looks fine and nothing reports anything. Collisions are detectable at build
time — the index knows every phrase claimed in every scope — so this is a lint rather than a mystery.
**It has to be built as a lint from the start**, because a silent wrong resolution leaves no artifact
to notice later, and a corpus accumulates them faster than anyone re-reads it.

The spec, with the 1988 tool's behavior as the baseline (see
[EMACS-INDEX-MANAGER.md](EMACS-INDEX-MANAGER.md), where `new-synonym` already refused duplicates
within one namespace at claim time):

| Condition | Verdict | Why |
|---|---|---|
| One name claimed twice in one namespace in one scope | **Error**, refuse the claim | Unresolvable in principle; YAHTITTIE enforced this in 1988 |
| Nearer scope shadows an enclosing one | **Legal, but reported** | Shadowing is the point of a scope chain, but silent capture is the failure being described. This is the half the 1988 tool left unbuilt — it checked the top index only |
| Name resolves differently depending on referring location | **Warn** | Position-dependent meaning is legitimate and worth knowing about |
| Alias fails the distinctness filter | **Reject at generation** | See below |

"Same name" is defined by the canonicalizer, and the 1988 one is wider than string equality: case
folded, and `[ \n\t<>~]+` collapsed to a single space, so **the tilde is stripped as whitespace** and
`~Founders~`, `Founders`, and `founders` are one name. The lint must use that equivalence class or it
will pass collisions the resolver then hits.

**Widen it to punctuation, on the archive's evidence.** The 1988 canonicalizer did *not* normalize
`,` or `.`, and the cost is visible in the surviving NeWS documentation index, where one article
carries three hand-registered synonyms — `"alphabetically"`, `"alphabetically,"`,
`"alphabetically."` — because a link picked out of running prose drags its trailing punctuation into
the lookup key. The author paid for the gap by claiming the variants manually
([EMACS-INDEX-MANAGER.md](EMACS-INDEX-MANAGER.md)). Strip trailing and internal punctuation in
canonicalization so the phrase `~the forge~,` at the end of a clause resolves without ceremony — and
then apply the same widened class in the lint, since anything the resolver merges the lint must also
merge.

**Generated synonyms drift toward the generic.** "the forge" is a good alias; "the thing where you
do the work" is mean-regression, and it will collide with everything. Candidate lists need a
distinctness filter for the same reason the [glyph benchmark](../GLYPH-BENCHMARK.md) does.

**Tildes are not free.** `~` appears in prose (URLs, home directories, approximations) and in
Markdown's strikethrough as `~~`. A real implementation needs an escape and should accept the
alternatives Postel-style — `[[name]]` is the wiki idiom and costs nothing to also parse.

**A name-addressed corpus is hard to link *into* from outside.** The web can point at a URL; it
cannot point at "whatever `~the forge~` means in that scope." Names are the interior addressing
scheme; stable URLs remain the exterior one, and both have to exist. That is the same
inside/outside split gwern's stable-URL discipline enforces, and it is not optional.

---

## Sources

- `archive/HyperTIES/news-paper/hyperties.st0` — the `~name~` markup in use
- `archive/HyperTIES/ties.doc.txt` — the four-part field list, the three index namespaces, the FORTH
  compilation section quoted above
- `archive/HyperTIES/to.bill.txt` — Don to `weiland@bensun`: the index manager's ownership, and the
  broken-apart/smushed-together authoring-vs-browsing split
- `ties/yahtittie.ml`, `ties/ht.ml`, `ties/ties.ml`, `ties/ties-2.ml`, and `ties/emacs/master-index`
  (10 July 1988) — the MockLisp authoring tool and a surviving index, read in
  [EMACS-INDEX-MANAGER.md](EMACS-INDEX-MANAGER.md)
- All three are **unversioned**, in the LLOOOOMM import tree. See [ARTICLE-SCHEMA.md § Local
  archive](ARTICLE-SCHEMA.md#local-archive).

↑ [hyperties pack](README.md) · [ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md) · [TEAM.md](TEAM.md)
