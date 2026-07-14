# The Dublin Core move — a strict executable core under the rich semantic overlay

> **The natural language IS the specification. The code IS the implementation.
> Both live side-by-side.** — [Adventure Compiler philosophy](../../skills/adventure/events/COMPILE_EXPRESSION.yml.tmpl)

[LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) admits a real failure mode: names are
not portable to non-LLM readers. A deterministic engine can't resolve "The Weird Sisters from
Macbeth"; a validator can't check "player trusts Einstein enough." The answer is not to abandon
names — it's to do what the metadata world did with **Dublin Core**: define a small, strict,
machine-readable and *machine-executable* core vocabulary, and let every richer layer be an
**overlay** on top of it. Non-LLM readers (engines, linters, other tools) consume the core.
LLMs and humans read everything — core, overlay, comments, and the latent space the names
point into.

The two layers have a contract:

- **Strip the overlay** and the world still runs — the core is sufficient for deterministic
  execution.
- **Strip the core** and the LLM can regenerate it from the overlay — the natural language is
  the specification, so compilation is recoverable.

That round trip is what makes the overlay refinement rather than decoration, and the core
compilation rather than transcription.

## Status: we are still playing and learning

Honesty about phase, per [play-learn-lift](../../skills/play-learn-lift/): we are **not** in
LIFT. Defining the strict core *first* would be the classic premature-abstraction mistake that
Oliver Steele's instance-first development (see the OpenLaszlo lineage in
[SELF-AND-MOOLLM](SELF-AND-MOOLLM.md)) exists to prevent. Instead we're eating our own dogfood
until the instance-first shape of the problem emerges — and it is emerging, in one application
space in particular.

## The leading instance: the adventure compiler

The [adventure skill](../../skills/adventure/ADVENTURE-COMPILER.md) is the furthest-along
example object-network application, and it demonstrates the whole stack end to end. The
pipeline ([PR vision doc](../pr/PR-ADVENTURE-COMPILER-VISION.md)):

```
AUTHOR (empathic YAML) → LINT (adventure.py) → LLM COMPILES → BROWSER RUNTIME (engine.js)
```

**The compiler is a linter, and the LLM is its back end.** `adventure.py` walks the world,
checks files against schemas, and emits typed events —
[LINTER.yml](../../examples/adventure-4/LINTER.yml) is a real run: 36 rooms, 37 objects,
8 errors, 36 warnings, and 9 `COMPILE_EXPRESSION` requests. A compile request is exactly the
warning "found an unimplemented natural language guard on exit *foo* in room *bar*":

```yaml
- type: COMPILE_EXPRESSION
  path: pub/gong.yml
  message: 'Expression needs compilation: RING-TWICE.score_if'
  source_expression: urgent situation OR point_of_order
  source_field: advertisements.RING-TWICE.score_if
  target_field_js: advertisements.RING-TWICE.score_if_js
```

The LLM reads the linter output and resolves the warnings — the loop it is best at, borrowed
straight from how it fixes compiler errors in ordinary code. Each event ships the full
`runtime_context`: the closure signature, the available function vocabulary, naming
conventions, and skill references. The event is a self-contained compilation brief.

**The door example, concretely.** An author writes intent on the exit, in English:

```yaml
exits:
  vault:
    guard: "can only lock and unlock if staff; anyone can go through if unlocked"
```

The linter flags the unimplemented guard; the LLM compiles it *in place*, next to its source:

```yaml
exits:
  vault:
    guard: "can only lock and unlock if staff; anyone can go through if unlocked"
    guard_js: "return verb === 'lock' || verb === 'unlock' ? subject?.hasTag('staff') : !object.state.locked"
```

The [runtime engine](../../skills/adventure/engine.js) wraps every body with one standard
signature — `(world, subject, verb, object) => { body }` — compiles it once with `compileJs`,
caches the closure, and evaluates it deterministically in the browser. No LLM in the loop at
play time. And because the English guard stays on the object beside its compiled form, **every
intentional constraint is individually inspectable** — the runtime's PSIBER inspector
([dist/README](../../skills/adventure/dist/README.md)) shows source YAML and live JSON
side-by-side, diffed, with a View Source button on every object via its `moollm://` path
identity.

The LLM's role is symmetric and total: it assisted in writing the engine, it writes the scripts
the engine executes, and it reads the linter's complaints about the gap between them. Human
intent enters once, in natural language, on the object it governs.

## The diff is the review: Knuth's literate programming, realized

That two-line guard/guard_js pair **shows up as a reviewable diff in a PR** — the compiled
code lands in the trampoline net like every other change. And it's an unusually easy review,
because of **colocation**: the generated code sits directly under the natural-language
definition that specified it, on the object that owns it, in the room where that object lives,
among the other objects and characters it interlocks and dovetails with. A reviewer — human or
LLM — has the spec and the implementation in the same glance and the whole activation context
one directory listing away. Syncing code with intent stops being archaeology; it's a two-line
comparison.

The English is the durable half. When the adventure compiler's runtime model, API, or naming
conventions change, the compiled `_js`/`_py` fields are **invalidated and regenerated** against
the new contract — build artifacts refreshed from source, where the source is the sentence.
The intent survives every engine migration untouched.

And because the substrate is YAML jazz, the intent channel has unlimited bandwidth: an
end-of-line comment when a phrase is enough; block comments of any depth when the author's
reasoning needs paragraphs; and, accumulating in place, the **history of the collaboration
itself** — edits, transformations, LLM-assisted generations, and the back-and-forth dialog
where humans and LLMs asked and answered questions, discussed the design, and resolved the
ambiguities. This is **Knuth's literate programming, realized**: the program as an explanation
addressed to human beings, with executable code interleaved. Knuth needed WEB to tangle code
one way and weave documentation the other; here the weave is the English and the comments, the
tangle is the compiled expression, and they never separate — same file, same object, same
line of sight. The compiler even reads the *documentation* (that's what the natural-language
guard is) and complains when the code drifts from it, which is the literate-programming dream
Knuth couldn't mechanize in 1984: prose that the toolchain holds the code accountable to.

## The Dublin Core that has already precipitated

The strict core isn't designed yet — but pieces of it have *precipitated* from play, which is
exactly how instance-first says fields should be discovered:

| Emerged convention | Where it lives |
|---|---|
| Closure signature `(world, subject, verb, object)`, parallel-safe, `world` never null | [engine.js](../../skills/adventure/engine.js) `compileJs` |
| Subjective runtime vocabulary: `i_have`, `i_am`, `i_say`, `emit`, `go`, `flag`, buffs, effective values | `runtime_context.available_functions` in every compile event |
| Dual-runtime rule: every expression compiles to both `_js` and `_py` | [COMPILE_EXPRESSION handler](../../skills/adventure/events/COMPILE_EXPRESSION.yml.tmpl) |
| Flat collections + ID references, never object pointers — serialization is trivial | [dist/README](../../skills/adventure/dist/README.md) object-modeling rules |
| Path identity: every object IS its path; `moollm://` names it globally, with git refs | [dist/README](../../skills/adventure/dist/README.md) namespace |
| Typed linter events as the compilation interface | [events/INDEX.yml](../../skills/adventure/events/INDEX.yml), [LINTER.yml](../../examples/adventure-4/LINTER.yml) |

When enough compiled worlds exist, LIFT means writing these down as the strict schema — a
handful of required, validated, executable fields (the Dublin Core), with everything else
(comments, empathic expressions, latent-space parent names, theme variants) formally defined
as overlay. The linter then enforces the core mechanically and hands the overlay to the LLM,
which is the division of labor the pipeline already practices informally.

## Lineage: the (good) Scott Adams

The application space is no accident. The adventure compiler descends from a conversation with
**Scott Adams of Adventureland** (1978, the first commercial text adventure — the good Scott
Adams) on Hacker News in November 2021, continued on Facebook, documented in the
[letter to Scott Adams](../email/letter-to-scott-adams.md) and the
[PR vision doc](../pr/PR-ADVENTURE-COMPILER-VISION.md): adventure games as Memory Palaces
(the Method of Loci, computerized), pie menus as room navigation, code as buildings — and the
shared ambition of publishing both men's papers, articles, and biographies as *explorable
adventures* rather than linear archives. Rooms of ideas; characters you can question; objects
you can examine. The strict core is what lets those archives run deterministically in anyone's
browser; the overlay is what keeps them alive to the LLM and legible to the reader.

---

Part of the [object-system](README.md) series ·
[LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) ·
[SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) ·
[HUMANSPLAINING](HUMANSPLAINING.md) ·
[ANNOTATED-BIBLIOGRAPHY](ANNOTATED-BIBLIOGRAPHY.md)
