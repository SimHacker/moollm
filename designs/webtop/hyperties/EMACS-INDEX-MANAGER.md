# The Emacs index manager, reverse engineered

*Reading the surviving MockLisp sources for the HyperTIES authoring tool. The 1988 code implements a
stack of scoped, typed indexes with first-match-wins resolution, per-namespace completion, and a
duplicate-name lint — which is the resolution protocol this pack has been specifying, already built.*

↑ [hyperties pack](README.md) · Related: [LINK-RESOLUTION.md](LINK-RESOLUTION.md) ·
[ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md) · [`kernel/constitution-core.md` §14](../../../kernel/constitution-core.md)

## The sources

In `lloooomm-imports/ties/`, alongside the FORTH formatter and the NeWS PostScript:

| File | Lines | What it is |
|---|---|---|
| `ties.ml` | 305 | *"Emacs support for HyperTies"* — an interactive TIES session run from Emacs, separate from the terminal's server connection. Configured by `ties-directory "~don/n/ties/"` |
| `ht.ml` | 425 | *"HyperTIES Storyboard mode"* — storyboard editing as an Emacs major mode |
| `ties-2.ml` | 405 | *"Yet Another HyperTIES Implementation, This Time In Emacs (**YAHTITTIE**)"* |
| `yahtittie.ml` | 2634 | the developed YAHTITTIE — index manager, entry objects, field editing, storyboard mode, tilde buttons |
| `tiemacs.ps` | 273 | the NeWS side |
| `emacs/master-index` | 67 | **a real master index, dated 10 July 1988** |

Attribution, per [ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md): Don Hopkins wrote the MockLisp authoring
tool and the FORTH formatter; Bill Weiland wrote the C index manager used by the browser. This
document is about the MockLisp side — the *authoring* implementation, which is the one that had to
be interactive, and therefore the one that had to solve resolution in front of a human.

## The master index is the receipt for typed namespaces

The surviving 1988 index, abridged:

```
----- ARTICLES -----
"Master Index"                    ./index.st0
"!index"
"The Founders"                    ./founders.st0
"founders"
"Home Base"                       ./home.st0
"home"
"!home"
"!Control Panel"                  ./../global/control.st0
"controls"
"control panel"

----- PICTURES -----
"founders"                        ./obj/founders.pn0
"founders.big"                    ./obj/founders.big.pn0

----- TARGETS -----
"founder.curly"                   ./obj/founder.curly.tn0
"back-button"                     ./../global/back-button.tn0
```

Five things are visible in the artifact itself:

**Three namespaces, literally delimited.** `----- ARTICLES -----`, `----- PICTURES -----`,
`----- TARGETS -----`. Not a convention described in a document — section headers in a file.

**`founders` is a name in two namespaces at once and does not collide.** It is a synonym for the
article *The Founders* and it is the name of a picture. This is the claim about typed namespaces,
proven by the artifact rather than argued.

**Synonyms are unindented quoted lines with no path.** An entry is a quoted title plus a file; every
bare quoted string that follows is another name for the same entry. *The Founders* answers to
`founders`; *Home Base* answers to `home` and `!home`. The data format for
[self-naming text](ARTICLE-SCHEMA.md) is: put the other names on the next lines.

**`!` marks a name the system resolves rather than prose.** `!index`, `!home`, `!Control Panel` — a
reserved sub-namespace for browser-invoked entries, so a button can ask for `!home` without competing
with an author writing the word "home."

**Scope is relative paths.** `./../global/back-button.tn0`. Local names resolve in the local index;
shared furniture lives in a sibling `global/` index. Lexical scope, implemented as directories.

## A stack of indexes, searched innermost-first

`yahtittie.ml` keeps `master-indices` as an array used as a stack with `&master-indices` as the
pointer, and exposes `push-master-index`, `push-master-index-file`, `pop-master-index` (top, or by
name, splicing it out of the middle), and `with-top-master-index`. The resolver:

```lisp
(defun (search-master-indices $title $space ...
      (setq $title (canonicalize (arg 1 ...)))
      (setq $space (arg 2 ...))
      (setq $i (+ &master-indices 1))
      (while (> (-- $i) 0)
          (switch-to-buffer (array master-indices $i))
          (if (setq &entry (search-master-index $space $title))
              (setq $i 0) ; exit loop if found
          )
      )
      &entry
))
```

Walk the stack from the top down; first match wins; stop. Compare the MOOLLM constitution's §14
discovery rule — *"walk outward from the referring location… first match wins; closer definition
shadows farther one (lexical scope)"*. **Same algorithm.** The 1988 tool arrived at it because an
author needs a local name to mean the local thing, which is the same pressure that produces lexical
scope everywhere it appears.

Note the two-argument key: resolution takes `$title` *and* `$space`. There is no way to ask for a
name without saying what kind of thing it is. The per-index storage confirms it —
`search-master-index` reads `(get-from-dict (concat (current-buffer-name) ":" (arg 1)) (arg 2))`, so
the dictionary is keyed by *(index buffer, space)* and the name is looked up inside it. One namespace
per type per index, exactly.

## Plural containers, in 1988

The function that switches to a namespace takes the type name **singular** and constructs the plural
section header:

```lisp
(defun (narrow-to-sub-index $name
  (search-forward (concat "----- " $name "S -----\n"))
  ; if absent: create it at end of file, then narrow
  (insert-string "\n----- " $name "s -----\n")
  (case-region-upper)
  ...
  (narrow-region)
))
```

Callers pass `"article"`, `"picture"`, `"target"`; the code pluralizes and uppercases to find or
create `----- ARTICLES -----`. **The singular type name and the plural container name are the same
identifier under a pluralization rule**, and a missing container is created on demand rather than
being an error.

That is the [plural-container rule](../../../kernel/constitution-core.md) written into the
constitution this week — `farts/` holds `fart` instances, one namespace per plural container, and the
container appears when needed. It was in the receipt the whole time. Emacs `narrow-region` is doing
what a directory does: making a subtree the whole world for the duration of an operation.

## Resolution offered to the human as ranked completion

The tool did not resolve silently. It built completion lists, per namespace, in scope order:

```lisp
(defun (update-completion-list
  (if master-index-stack-changed
      (progn
          (make-completions "article")
          (make-completions "picture")
          (make-completions "target")
      )))

(defun (make-completions $mc-space $mc-i
  (temp-use-buffer (concat "*" $mc-space "-completions*")
      (setq $mc-i (+ &master-indices 1))
      (while (> (-- $mc-i) 0)              ; top of stack first
          (yank-buffer (concat (array master-indices $mc-i) ":" $mc-space))
          ...)))
```

Three completion buffers, one per namespace, rebuilt when the stack changes (guarded by a
`master-index-stack-changed` dirty flag), each assembled by walking the stack **from the top down** so
that nearer names come first. The author typing a link name gets the candidate set for that
namespace, ordered by scope proximity.

This is the ancestor of **human-in-the-loop method resolution as ranked results.** The resolver's
internal ordering is not hidden; it is rendered as a list the author picks from. Which is the Sims
move: an object's advertisements are scored, the scores are ranked, and the choice among the top
candidates is exposed rather than buried. Ambiguity stops being an error condition and becomes a
menu — the [pie menu of bindings](LINK-RESOLUTION.md) — and the ranking is the same computation the
automatic resolver would have done alone.

## The lint exists, and it is half of the one we need

`new-synonym` canonicalizes both names, then refuses to shadow within the current index:

```lisp
(if (! (setq $ns-index (search-master-index $ns-space $ns-title)))
    (message "Entry " $ns-space " " $ns-title " is not defined in " ...)
    (if (search-master-index $ns-space $ns-synonym)
        (message "Entry " $ns-space " " $ns-synonym " is already defined in " ...)
        ; else: insert the quoted synonym line, and put-in-dict
    ))
```

So the 1988 tool enforced: **you cannot claim a name twice in one namespace in one index**, checked
at authoring time, at the moment of claiming. That is the collision lint.

But `new-synonym` runs `with-top-master-index` — it checks *the top of the stack only*. Claiming a
name that shadows an entry in an enclosing index is permitted and unremarked. That is not obviously
wrong, because shadowing is the point of a scope chain. It does mean the failure mode is exactly the
one worth fearing: **a reference silently resolving to a plausible wrong node** because a nearer
index quietly captured the name.

The distinction to build on, then:

| Condition | Verdict |
|---|---|
| Same name claimed twice in one namespace in one scope | **Error.** Refuse the claim, as 1988 did |
| Name in a nearer scope shadows one in an enclosing scope | **Legal, but report it.** This is the missing half |
| Name resolves to different entries from different referring locations | **Warn.** Ambiguity that depends on where you stand |

Both halves are computable at build time, because the index knows every phrase claimed in every
scope. This is a lint, not a mystery — but only if it is written as a lint from the start, since a
silent wrong resolution produces a page that looks fine.

## The equivalence class, from `canonicalize`

The lint's notion of "same name" is defined by the canonicalizer, which is worth reading exactly:

```lisp
(defun (canonicalize $c-string &c-fold
        (setq &c-fold (< (nargs) 2))
        ...
        (if &c-fold (case-region-lower))
        (error-occurred (re-replace-string "[ \n\t<>~]+" " "))
        ...
```

Case is folded by default, and the character class `[ \n\t<>~]+` collapses to a single space. So
**tildes and angle brackets are treated as whitespace** — which means `~Founders~` canonicalizes to
`founders`, and the markup that makes a phrase a link is erased by the same pass that normalizes
spacing. The link syntax and the name are not two things that need mapping between them; strip the
punctuation and the name is what is left. Self-naming text, mechanically.

Two names collide if they are equal after case folding, markup stripping, and whitespace collapse.
That is the equivalence class a synonym lint must use, and it is wider than string equality —
`~Founders~`, `Founders`, and `founders` are one name, which is the intent.

## The second database: NeWS documenting itself

`lloooomm-imports/ties/newsdoc/` is a far larger HyperTIES database than the `emacs/` one above — a
268-line master index over **108 operator articles** in `o/`, plus the sibling `global/` scope (84
files) that the smaller index's `./../global/` paths implied but did not contain.

What it documents is the joke: `acceptconnection`, `awaitevent`, `expressinterest`,
`redistributeevent`, `canvastotop`, `setrasteropcode`, `forkunix`. **It is the NeWS PostScript
operator reference, published as HyperTIES** — and HyperTIES ran *on* NeWS. The window system's
manual, delivered as hypertext by an application of the window system.

Two index articles sit over the same 108 operators — `alphabetically.st0` (*"NeWS Operators,
Alphabetically"*) and `type.st0` (*"NeWS Operators, by Type"*). One corpus, two compiled orderings,
each an article in its own right. Viewspecs, shipped as build products.

### The build script, and the definition/article split

`compile-all` is the actual build, 558 lines of two directives per node:

```
.compile-controls global/control.st0.c
!Control Panel

.compile-definition ./o/random.st0.d
random
.compile-article ./o/random.st0.a
random
```

**The definition and the article are separate compilation units** with separate output extensions —
`.d` and `.a` — each named by the title on the following line. So the one-line summary shown on a
single click was not extracted from the article at read time; it was *compiled as its own object*.
The [semantic pyramid's rungs are build artifacts](../../TAGSONOMY-COMPILER.md), which is the
claim this corpus keeps making, and here it is as a Makefile-shaped list from 1988. A third
directive, `.compile-controls`, handles the control panel out of `global/`.

### The compiler output, including its crash

`compiled.f` is the FORTH the compiler emitted, and it is worth being precise that the surviving
artifact is a **failure** — it stops mid-target with:

```
Bombing to Forth!
Segmentation violation
```

What it got through shows the emitted form:

```forth
c~ ControlsPileID~
.ULP .ZP .SP .SL
16 c~ Times-Bold~ .UF
71 10 c~ FIRST~ .PS
15 46 67 10 c~ !OptionFirst~ c~ first-button~ .PT
```

Dot-prefixed FORTH words matching the storyboard field markup, coordinates pushed as bare numbers,
and `c~ string~` — **the tilde as string delimiter**, the same character that marks a link in prose
and that `canonicalize` treats as whitespace. Note what survives compilation: `.PT` receives
`!OptionFirst` and `first-button` as *names*, not addresses. The compiled image still defers to the
index at load time, which is why the bang-namespace exists — `!OptionFirst` is a browser command, not
an author's phrase.

### The index edit history, and a canonicalizer gap visible as manual labor

`master-index.old` differs from `master-index` by exactly one line — `+ "!index"` — so index edits
were incremental single-synonym additions, consistent with `new-synonym` being the interface.

The more useful finding is in the synonyms themselves:

```
"NeWS Operators, Alphabetically"    ./alphabetically.st0
"alphabetically"
"alphabetically,"
"alphabetically."
```

The author registered the **comma- and period-suffixed forms as separate synonyms.** Because
`canonicalize` collapses `[ \n\t<>~]+` but does *not* touch `,` or `.`, a link picked out of running
prose dragged its trailing punctuation into the lookup key, and the workaround was to claim the
punctuated variants by hand. Three index entries for one article, to survive a comma.

That is a specification bug diagnosed by its own maintenance burden, and it is the most actionable
thing in the archive: **normalize trailing and internal punctuation in the canonicalizer, or authors
will do it by hand, forever.** It also widens the collision equivalence class, which the lint has to
match ([LINK-RESOLUTION.md](LINK-RESOLUTION.md)).

## What to reimagine

A note-to-self survives at the top of `ties-2.ml` and `yahtittie.ml`, and it is longer than a single
line:

```
; Notes:
; * Make synonyms use the abbrev mechinism
;   use-abbrev-table define-local-abbrev abbrev-mode abbrev-expansion
; * Edit definitions, etc, with edit-in-transient-window
; * Show temporary messages with typeout-text
; * Use define-hooked-local-abbrev to make .commands prompt for
;   arguments, with completion over known names, in storyboard mode.
;   Look at /usr/unimacs/lib/emacs/maclib/cmacs.ml
```

Synonyms as Emacs abbrevs — expansion at typing time, so writing the phrase *is* creating the link.
Worth taking seriously now, because it is the interaction the whole self-naming argument implies: the
author does not mark up a link, they write the words, and the tool recognizes a claimed name as they
type it.

The fourth note is the more ambitious one and it was also not built: **`define-hooked-local-abbrev`
to make `.commands` prompt for their arguments, with completion over known names.** An abbrev with a
hook — type the directive, and it interviews you for its parameters against the live index. That is
structured entry with type-aware completion driven by type-ahead, sketched in 1988, and it is the
same interaction as [TREE-NAVIGATION.md](../TREE-NAVIGATION.md)'s type-ahead-as-resolution and
[LINK-RESOLUTION.md](LINK-RESOLUTION.md)'s ranked candidates.

### Correction: the abbrev mechanism *was* built — as a dictionary, not as an input method

An earlier version of this document said the abbrev note was never implemented. That is wrong, and
the truth is better. `yahtittie.ml` references abbrevs twenty-five times, and there is a line that
settles what for:

```
    ; The dictionary mappings are stored in the dictionary buffer's
    ; local abbrev table, of the same name as the buffer.
    (use-abbrev-table $md-buffer)
    (setq abbrev-mode 0) ; We don't want abbrevs in the buffer to be expanded
```

**Expansion is deliberately turned off.** The abbrev table is used purely as a hash table, with the
typing behavior — the thing that makes an abbrev table an abbrev table — disabled on purpose. So the
two uses are distinct and only one shipped:

| Use of abbrevs | `abbrev-mode` | Status |
|---|---|---|
| **Input method** — recognize a claimed name as you type it | on | Available for free; never used for synonyms |
| **Data structure** — key→value store | **off** | Used, and the index manager runs on it |

Precision on the first row, per Don: **there was nothing to build.** Abbrev expansion was already a
built-in part of Emacs, sitting right there with `abbrev-mode` a `setq` away. It simply was not
needed for synonyms, so it was never turned on for them. That is a different and more interesting
fact than "unimplemented" — the interaction the self-naming argument implies was *one line of
configuration away in 1988* and went unused because nothing at the time required it. The idea in the
note-to-self was not a wish for a missing feature; it was a wish for a *use* of a present one.

Don's account of why, which the code corroborates: MockLisp had no associative structures at all, and
**the per-buffer abbrev table was the only one available**, so he repurposed it — and had to switch off the very behavior it was named for in order to use it as storage. Arrays did exist —
`array`, `array-size`, `setq-array`, `grow-array`, `nullarray` are used throughout for the index
stack and the entry tables — so the precise gap was *dictionaries*, not indexed storage.

### The dictionary ADT, and why it needed two representations

The full CRUD layer is in `yahtittie.ml`, and it is worth reading as a design rather than a hack:

| Operation | Implementation |
|---|---|
| `make-dict` | Create a buffer named `owner:space`; `use-abbrev-table` with the same name; `abbrev-mode 0` |
| `put-in-dict` | Insert the key as **a line of text in the buffer**, *and* `define-local-abbrev key value` |
| `get-from-dict` | `abbrev-expansion key` |
| `remove-from-dict` | Walk the buffer's lines; `define-local-abbrev key 0` and `erase-region` |

The dual representation is the interesting part, and it is not redundancy. **The buffer text holds the
key set; the abbrev table holds the key→value map.** An abbrev table cannot be enumerated, so the
buffer's lines supply iteration order and searchability — with a leading newline inserted as a
delimiter, annotated in the source as *"delimiter to make searches easy."* One dictionary, two
projections: the text is walkable, greppable, and **savable to a file**, and the table is the lookup.

That is why Don's description — *"the buffer then would hold a text representation of the
dictionary, i.e. could be stored in a file or info node"* — is literally what the code does. It is
**a persistent dictionary in a language with no dictionaries**, and persistence comes free because
the authoritative key set was already text in a buffer.

Values were stored as text and coerced on read: `(concat &ff-index)` to store a number,
`(+ (abbrev-expansion ...))` to get one back. The store was string→string, with coercion at both ends
— which is exactly what makes the text representation authoritative rather than a cache of it.

Case-insensitivity came free from the borrowed mechanism rather than being implemented. `put-in-dict`
lowercases its key with `case-string-lower` and `get-from-dict` does not, which would be a bug except
that Emacs abbrev lookup is itself case-insensitive. So one of the
[canonicalizer's](LINK-RESOLUTION.md) equivalence rules was inherited from the data structure it was
squatting in — worth knowing, because a reimplementation has to make that rule explicit instead of
receiving it as a gift.

### Buffers as objects, and dictionary names as scoped types

The naming convention is the payoff. Dictionary buffers are named `owner:space` — the source's own
example is `master-index<2>:articles`, and elsewhere `<buffer>:fields` and `"storyboard"`. So a
dictionary's *name* encodes two things at once:

- `master-index<2>` — **which scope frame**, by position in the index stack
- `articles` — **which type namespace**, of the three

Which means the typed, scoped resolution this pack documents was not layered over the storage. It
*was* the storage: the buffer name is the fully qualified path of a namespace, and a name lookup is a
walk over buffer names. And a buffer could carry more than one dictionary for different facets of the
same object — `<buffer>` for its slots, `<buffer>:fields` for its field index.

Don's summary is the right one: *"buffers were FANCY!!! And we used them as objects."* A buffer had a
name, local variables, a local abbrev table, and persistence to a file — which is identity, slots, an
associative store, and durability. That is an object, assembled out of a text editor's incidental
features by someone who needed objects and did not have them.

**And it is MOOLLM's own architecture, thirty-eight years early.** MOOLLM makes the filesystem the
dictionary because its language — text read by an LLM — has no native associative structures either;
directories are the objects, their names are qualified paths, containment is the scope chain, and
everything persists because it was always already text. The 1988 code reached the same design from
the same pressure. That is a stronger endorsement of the pattern than any argument for it, and it is
worth recording that the constraint produced the architecture rather than the other way around.

The rest of the reimagining list, in the order the 1988 code suggests it:

- **The completion lists become the ranked-advertisement UI.** Three buffers rebuilt on a dirty flag
  is a cache invalidation strategy; the modern version scores candidates and shows why each ranked
  where it did.
- **The dirty flag becomes the incremental build.** `master-index-stack-changed` is exactly the
  signal a [tagsonomy compiler](../../TAGSONOMY-COMPILER.md) needs to recrystallize a scope.
- **Buffers-as-dictionaries becomes files-as-state.** `make-dict`, `put-in-dict`, `get-from-dict`,
  `remove-from-dict` build hash tables out of Emacs buffers because that was the only data structure
  available. MOOLLM has the same instinct for the same reason, one substrate up.
- **`entry-class` and its hooks become CARD dispatch.** Entries carry a class and three
  method hooks — `entry-instantiation-hook`, `entry-author-hook`, `entry-find-field-hook` — installed
  by the major mode of the entry's file. Type-driven method lookup, with the type inferred from the
  file. That is `CARD.yml` advertisements with the file extension as the type declaration.
- **`relativize-file-name` becomes the portability discipline.** The tool rewrote absolute paths to
  relative ones when defining entries, which is why the 1988 index still resolves.

## Status

Reverse engineered from source, `2026-09-04`. Claims here are traceable to the files named above;
`yahtittie.ml` line numbers are from the copy in `lloooomm-imports/ties/`. The three-namespace design
was documented in `ties.doc.txt`; this document adds the *implementation* — the stack, the
first-match-wins walk, the pluralizing sub-index switch, per-namespace completion, and the
within-scope duplicate check.

Open question for Ben Shneiderman, per the standing list in
[ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md): how many platform implementations of the index manager
existed, and which of them enforced the duplicate-name check.
