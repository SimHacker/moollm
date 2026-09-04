# Temkin: constraints that stay true, and a canvas you share with an agent

David Temkin is the only person in this hub **actively shipping runnable code** on the same problem.
Everyone else here is a lineage, a proposal, or an archive. Declare and Mesa run in a browser today.

Public surfaces:

| Thing | Where | State |
|---|---|---|
| **Mesa** | [davidtemkin.com/about-mesa/](https://davidtemkin.com/about-mesa/) | Essay, videos, **live demo**, no account. Agent half is account-only, shared selectively |
| **Declare** | [github.com/davidtemkin/declarelang](https://github.com/davidtemkin/declarelang) · [live](https://davidtemkin.github.io/declarelang/) | Public repo, live docs/calendar/desktop/inspector apps |
| **OpenLaszlo 5.0** | [github.com/davidtemkin/openlaszlo-5.0](https://github.com/davidtemkin/openlaszlo-5.0) · [Explorer](https://davidtemkin.github.io/openlaszlo-5.0/) | Public, compiles in browser, byte-for-byte vs 4.9 |
| **In Formation** | print magazine, founded 1998, relaunched 2025 | *"Because every day computers are making people easier to use"* |
| **Manic Episode** | *"A 3D glasses game written for the Macintosh in 1991; ported to the web in 2025"* | Playable; Mac source and web source both public |

Founder of **Laszlo Systems** (2000–2009); later co-founded **Cola**; product leadership at Google,
Brave, and AOL; engineering at Apple. The 1991 Mac game was rewritten to JS with Claude Code —
roughly 15K lines of 68000 assembly in three or four days, which is the same trick as OpenLaszlo 5.0
and worth noting as method, not anecdote.

Rooms and correspondence:
[`characters/david-temkin/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/david-temkin)
· show seed [`repo-shows/openlaszlo/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/repo-shows/openlaszlo)
· pre-call agenda [`TEMKIN-CALL-2026-08-05.md`](../../webtop-gwern-inheritance/TEMKIN-CALL-2026-08-05.md)

---

## Mesa is the semantic pyramid, rendered as space

Mesa's own description, which is the pyramid claim in different words:

> Files appear as themselves — thumbnails, previews, contents — **at whatever level of detail the
> current zoom affords.** You navigate by zooming. Position carries meaning: what's next to what,
> what's grouped with what, what you've put first.

And the sentence that matters most:

> You don't open a file in a new tab, or in a separate application. It opens where it lives, at the
> spot you found it. A PDF renders inline, page by page. A text file can be edited on the spot. A
> video plays in place. An audio file shows its waveform. Click outside and the canvas comes back.
> **Mesa keeps you oriented by erasing the line between the icon you see and the actual opened
> file — they're the same thing.**

That is the `link-icon → title → abstract → section` ladder stated as a spatial invariant instead of
a rendering pipeline. The glyph and the document are **one object at two zoom levels**, not a preview
of a thing plus the thing. Gwern's popup still distinguishes the link from its target; Mesa refuses
to. This is the difference our notes flag as **CSS-collapse zoom versus literal continuous zoom**.

The pitch, from his announcement (2 June 2026):

> The future of computing can't possibly be "everything is a chat window," can it? ... I spent the
> last four months building an alternative — a spatial canvas you share with your AI... Alongside
> you is an AI agent that sees the same canvas, uses it as its context, and can make changes just
> like you can. **The visual mode and the conversational mode share one surface, instead of fighting
> for one.**

Compare Nenex, which proposes the opposite interface and admits it is a placeholder: *"A side pane
for all the LLM 'commentary', akin to how streaming websites implement chat in a pane next to or
below the streamed video, would be the obvious first stab at a GUI."* Nenex has the engine and a
Twitch chat. Mesa has the surface. See [`../gwern/NENEX.md`](../gwern/NENEX.md).

Mesa also renders offscreen in a worker and hands frames to main — the same architecture as
Micropolis under Wasm — and crosses that boundary with JSON datasets rather than shared reactivity.

---

## Declare: "SQL for interfaces"

Heir to OpenLaszlo LZX, deliberately **not a port**. LZX gave you declarative reactive apps
compiling to Flash *or* Ajax in 2002. Declare asks what that language becomes when the compiler's
reviewer is an LLM.

**Two delimiters.**

- `[ … ]` is the **view tree** — components, attributes, children.
- `{ … }` is **TypeScript**, where values are **constraints: standing relationships the runtime keeps
  true**, not one-shot expressions.

**No VDOM.** Stated flatly in the language docs: *"No re-render, no VDOM diff, no dependency arrays,
no hooks."* Assignment notifies, like Svelte 5 `$state`; derived relationships stay true, like
`$derived`; the compiler extracts dependencies statically.

**Push, not pull.** David's own framing, 3 August 2026:

> Spreadsheet mental model: a cell changes → dependents update → their dependents, recursively.

The dependency tree is compiler-derived, and the compiler **sees into functions** to track which
cells affect a constraint expression. Like Brad Myers' Garnet in that expressions are parsed — but
*"no pull code."* And: *"This is pretty much like OpenLaszlo, no surprise, but comes with type
checking."*

**Unanalyzable constraints are compile errors,** not silent fallbacks — the `DECLARE7001` residue.
The language refuses to accept a relationship it cannot verify it can maintain.

**No CSS, no DOM in the language.** Style is attributes. All UI objects, keyboard navigation, and
layout are Declare classes; no platform layout engines. Children come from **datapath replication**
(`:rows[]`) rather than a `{#each}` block. One tree, **two back ends: DOM or canvas** (WebGL next).

**Instance-first.** Instances may declare their own members; the compiler synthesizes an anonymous
subclass; you promote to a named `class` once you instantiate it twice. Oliver Steele's **Instance
Substitution Principle** is the test, and David's answer when asked directly was *"Yup! (Or so I
hope)"* — David's own assessment of his own language, appropriately hedged. Oliver himself has not
weighed in, so the honest statement is that Declare's author believes it satisfies the ISP and its
namer has not been asked.

**Sized for a context window.** The whole language spec is roughly 10K tokens, single file. This is a
design constraint, not marketing: when writing code is free, the language's job shifts from helping
you write to **reviewing what was written**. Language-as-reviewer.

**The Inspector** (`⌥⌘D`): click any value, see the expression that produced it and its live inputs,
edit the Declare source in place. That is HyperLook's flip-into-edit-mode, thirty years later, on
the web — and it belongs in the webtop as a first-class gesture, not a devtool.

**Verification is a six-rung ladder** in `tools/verify`: structure → resolution → typecheck →
headless boot → real input → visual baselines.

**Demos that matter here.** The **Calendar**: four views with **continuous zoom**, drag and edit,
`State` and `Spring` as first-class reactive slots — **484 lines, 54 KB gzipped, zero lines written
by hand.** The **Desktop**: a full window manager running inside a Declare app.

---

## DOMIsland: endosymbiosis with a type signature

The most important thing in this directory, and it was built in response to a direct ask.

Don, 13 August 2026, recalling OpenLaszlo practice:

> Remember when somebody imported the Flash swf file that some mapping service used in their client
> into openlaszlo and wrote an openlaszlo wrapper so we could put slippery maps into openlaszlo
> apps? ... the important thing was that it was easy to plug another flash component into openlaszlo
> and wrap it up so it acts in a Laszlo friendly way, with constraints and data replication and
> instance first programming and all that other delicious stuff.
>
> There should be documentation and a "skill" or an "sdk" or at least set of interfaces and
> practices and patterns for wrapping existing html/css and web components and widgets written in
> other frameworks... **More like PlugOver and PlugOn instead of PlugIn.**

David, 20 August 2026 — *"Your wish is my command!"*:

> A Declare app (the host app) can embed HTML content as an "island". The Declare app declares the
> embedded content as an instance (of type `DOMIsland`), which can have instance specific
> attributes. The instance will receive attribute changes from the host in the form of a function
> call, and can push attribute changes to the host, too, from the embedded HTML. **These attributes
> on the embedded instance act like bidirectional constraints from the POV of the Declare app.**

Read that against [`ENDOSYMBIOSIS.md`](../../object-system/ENDOSYMBIOSIS.md). Engulfment without
digestion: the foreign organism — a slippy map, an HTML5 video element, a WebRTC recorder, someone
else's React widget — keeps its own membrane and metabolism, and the host talks across the boundary
through a **declared, typed, bidirectional constraint interface**. Not rewritten. Not a plugin
conforming to a host API. Engulfed, and made to participate in the constraint graph.

**PlugOver, not PlugIn.** DOMIsland supersedes the "limited connectivity" caveat from the 3 August
thread. Two archetypes to knock off first, both named by Don: HTML video in all its modes (play,
record, screencast, WebRTC) and the slippy map eBike Safari runs on. The skill/SDK of wrapping
patterns Don asked for is **still open** — that is a concrete deliverable someone could write.

---

## The constraint that reframes the shell question

Before treating Declare as the webtop's shell language, his own scoping, 3 August 2026:

> **Declare is best for self-contained things with coarse-grained connections to the outside world.
> It's not a good added layer or framework to be used with combo-plate JS/CSS/HTML.**

So Declare is not a veneer over an existing HTML corpus. Consequences, taken seriously:

- A Declare webtop is **a Declare application** that transcludes markdown through a JSON bridge —
  not Declare sprinkled onto gwern-style static HTML.
- Bridges that do **not** exist: Svelte or React as a reactive data source. JSON datasets only.
- **In-app window management: yes, today** — the Desktop demo is the proof.
- **Native OS overlay window management: beyond current design.** It needs an Electron bridge
  projecting external "cells" into Declare, and **the compiler must be taught about external
  cells**. Z-order against native windows is the hard part; a full-desktop overlay is easier than
  interleaving. His summary: *"meant for web apps today."*
- Practical read, recorded in [`MOOLLM-WEBTOP-VISION.md`](../../webtop-gwern-inheritance/MOOLLM-WEBTOP-VISION.md):
  **design for the overlay, ship browser-first.**

The honest open question is therefore not "is Declare the shell" but **which of three**: a Declare
application that owns the whole webtop, a Declare island inside a Svelte shell, or a parallel
implementation built to be compared against the Svelte one.

---

## SimFaux: the demo that wants an LLM

Don's old extensible content app, proposed as the Declare showcase (20 August 2026):

> It had a notion of a set of **weighted decaying keywords** (and a widget to display a word cloud
> of them scaled to their weight), and they would both **trigger content to play, and get emitted by
> content** (so the trigger and emit keywords could be different, resulting in interesting
> producer/consumer call/response flows). And that is the kind of stuff llms just love to gobble! So
> the "what do I do next" loop could be quite clever!

Decaying weighted keywords as both activation condition and emitted effect is the
advertisement/attraction model — the shape of The Sims' object advertisements and MOOLLM's
`score_when` triggers. Constraint propagation over a soup of decaying salience, with an LLM as
arbiter of what plays next. Drop-in content and widgets that play together with no integration work
is precisely what a constraint language is for.

Port plan and the LZX → OL 5.0 → Declare organelle framing:
[`apps/simfaux/declare/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/simfaux/declare)
· [`apps/simfaux/ORGANELLES.yml`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/simfaux/ORGANELLES.yml)

---

## Why he is in this hub

| Problem in the hub | Declare / Mesa answer |
|---|---|
| Rendering the pyramid | Mesa: one object, any zoom, opened in place. Calendar: continuous zoom across four views |
| A shell language for the webtop | Declare Desktop — in-app WM, DOM or canvas, no HTML/CSS |
| Absorbing foreign widgets without rewriting them | DOMIsland — PlugOver, bidirectional constraints |
| Keeping a corpus true as facts change | Push constraints — the deterministic sibling of Nenex's outdated-pages sweep |
| Human and agent on one surface | Mesa's shared canvas, versus Nenex's side pane |
| A language an LLM can hold entirely | ~10K-token spec; unverifiable constraints rejected at compile time |
| Editing the thing you are looking at | The Inspector — HyperLook's edit mode, on the web |
| Showing a reader where the keyboard will take them | OpenLaszlo's animated chevrons between tab stops — the flow half of [hyperties/FOCUS-FLOW.md](../hyperties/FOCUS-FLOW.md), whose reveal half is Shneiderman's |

The unification worth putting in front of both David and gwern: **Declare re-satisfies layout
constraints when a value changes; Nenex re-satisfies a corpus when a fact changes.** Same dataflow
shape, one deterministic and one probabilistic with a human approving. Neither has said it to the
other.

Don's one-liner from the pre-call agenda:

> Gwern built the best popup hypertext reader; OpenLaszlo built the webtop; NeWS built pie menu
> window managers; I want the same publishing virtues inside a classic WIMP shell — and I'm asking
> if Declare is how we chrome it.

---

## Open, and known gaps in our own record

- **No post-call transcript exists.** The 5 August agenda's hoped outcomes are all still unchecked,
  and the scheduled date drifts across our files (3 Aug thread says Wednesday 6 PM, the agenda says
  5 Aug 18:00, `CHARACTER.yml` says 6 Aug 18:00). Either the call notes were never written or they
  live in RepoShowPrivate. **Resolve before the show.**
- Which of the three shell options above.
- Can a MOOLLM room be a Declare instance, with `CARD.yml` advertisements as constraints?
- Does the view record ([`VIEW-STATE-ANCESTORS.md`](../../pie-stack-views/VIEW-STATE-ANCESTORS.md)) map onto
  Mesa's camera plus selection, so a Mesa vantage becomes citable?
- The JSON bridge schema for "open this markdown path in a window" is still unspecified.
- Declare data binding for a 100K-item corpus sidebar without instantiating every view.
- Oliver Steele on whether Declare satisfies his own Instance Substitution Principle — never asked.
  David has certified it for himself; the ISP's author has not commented. A question for the
  OpenLaszlo reunion, with both of them in the room.
- **Publicity:** Mesa he announced himself and is safe to link. The invitation draft records "your
  call on how public Declare is when we record." **Ask before pointing anyone at Declare.**

↑ [webtop hub](../README.md) · [gwern](../gwern/) · [winer](../winer/) · [hyperties](../hyperties/)
