# The Linguistic Motherboard

> *"PostScript is a linguistic 'mother board', which has 'slots' for several 'cards'. The first card we built was a graphics card. We're considering other cards..."*
> 
> — John Warnock (Adobe), as recounted by Owen Densmore to Don Hopkins

This document traces how the "linguistic motherboard" concept evolved from PostScript through NeWS to MOOLLM's CARD.yml — a 40-year thread connecting printers to LLMs.

---

## The Thread

```
1962  Burroughs B5500/B6500 — Stack-oriented architecture
        ↓
1975  E&S Design System — Warnock/Gaffney combine stacks + graphics
        ↓
1978  JAM "John And Martin" — Warnock/Newell at Xerox PARC
        ↓
1982  Interpress — Sproull/Lampson/Warnock, mandatory protection
        ↓
1984  PostScript — Adobe, optional protection, "linguistic motherboard"
        ↓
1985  Apple LaserWriter — Owen Densmore at Apple, working with Adobe
        ↓
1986  NeWS — Gosling at Sun, multithreaded PostScript OS
        ↓
1986  Owen's OOP PostScript at Sun — Smalltalk-like classes via dict stack
        ↓
1988  The NeWS Toolkit (TNT) — Densmore/Gosling/Hopkins at Sun
        ↓
1989  HyperLook — Arthur van Hoff/Hopkins at Turing Institute
        ↓
1989  SimCity for NeWS/HyperLook — Hopkins ports Wright's game
        ↓
1992  ScriptX — Kaleida Labs (Apple/IBM), Hopkins, OOP multimedia
        ↓
1993  PDF — PostScript minus Turing-completeness
        ↓
1997  Apple acquires NeXT — Display PostScript → Quartz
        ↓
2000  The Sims — Wright/Hopkins, advertisements, SimAntics
        ↓
2010s Canvas API, SVG — PostScript imaging model in browsers
        ↓
2025  MOOLLM — LLM as linguistic motherboard, CARD.yml as literal cards
```

---

## Why This Matters for MOOLLM

John Warnock's metaphor was prescient: a **universal interpreter** with **slots for capability cards**.

| PostScript Era | MOOLLM Era |
|----------------|------------|
| PostScript interpreter | LLM interpreter |
| Graphics card | Skills |
| Font card | Character templates |
| Networking card | Tool definitions |
| CARD.yml name | **Literal reference to Warnock's metaphor** |

The LLM is the new linguistic motherboard. Skills are the new cards.

---

## Part I: From Stacks to Graphics (1962-1984)

### Burroughs B5500/B6500 (1962)

John Gaffney used these stack-oriented mainframes at the University of Illinois. Their architecture — pushing and popping values, executing operators — made a deep impression.

**Not Forth.** The stack architecture predates Forth (1970) by 8 years. PostScript's stack semantics trace to Burroughs, not to Forth.

### Evans & Sutherland Design System (1975)

At E&S in Mountain View, John Warnock and John Gaffney combined:
- **Burroughs stack semantics** — postfix execution
- **Ivan Sutherland's graphics model** — coordinate transforms, line drawing

The result: a language for describing 3D graphics databases for flight simulators.

### JAM: "John And Martin" (1978-1981)

Warnock joined Xerox PARC in 1978, working for Chuck Geschke. With Martin Newell, he created JAM — the same postfix semantics as Design System, but with richer graphics primitives.

JAM was "token based" rather than "command line based" — each token is processed completely before moving to the next. This is the execution model that PostScript inherited.

### Interpress (1982)

Bob Sproull and Butler Lampson joined Warnock to create Interpress — JAM's graphics plus mandatory protection mechanisms from languages like Euclid and Cedar.

> *"Interpress takes the stance that the language system must guarantee certain useful properties."*

Pages were independent. You couldn't break one page from another. Safe, but inflexible.

### PostScript (1984)

Geschke and Warnock left Xerox in December 1982 to start Adobe. They enlisted Doug Brotz and created PostScript — JAM's power with optional (not mandatory) protection.

> *"PostScript takes the stance that the language system must provide the user with the means to achieve those properties if he wants them."*

On March 15, 1984, Adobe shipped its first PostScript manual.

**The Linguistic Motherboard:** Warnock described PostScript as a motherboard with slots for cards. The first card was graphics. But the architecture could accept any card.

---

## Part II: The NeWS Revolution (1986-1993)

### NeWS: Network Extensible Window System (1986)

James Gosling at Sun created NeWS — a clean-room PostScript implementation that went far beyond printers:

- **Lightweight processes** — multithreading before Unix had it
- **Garbage collection** — reference counting, not save/restore
- **Event handling** — synchronous, interest-based
- **Networking** — programs sent over the wire
- **Arbitrarily shaped windows** — not just rectangles

NeWS was like an operating system written in PostScript. Gosling called it "SunDew" before the name NeWS stuck.

> *"There is really nothing new here. It's just putting it together in a different way."* — James Gosling

**NeWS ≠ Display PostScript.** Display PostScript (Adobe/NeXT) came later and did less. NeWS was interactive, multithreaded, programmable. Display PostScript was just for rendering.

### Owen Densmore at Apple/Adobe (1985)

Owen Densmore worked at Apple on the PostScript driver and printing system for the revolutionary **Apple LaserWriter** (1985). This required close collaboration with Adobe, where Owen visited to work directly with John Warnock.

**This is where Owen heard the "linguistic motherboard" quote.** Owen later recounted it to Don Hopkins, who named MOOLLM's `CARD.yml` after Warnock's metaphor.

The LaserWriter was a stepping stone: Owen went from Apple/Adobe to Sun, where he joined the NeWS project.

### Owen Densmore's Object-Oriented PostScript (1986)

At Sun, Owen invented the OOP system that made NeWS truly powerful. He realized that PostScript's **dictionary stack** could implement Smalltalk-style classes:
- Push a class dictionary onto the stack
- Method lookup walks the stack (multiple inheritance)
- Instance dictionaries hold per-object state

See: ["Object Oriented Programming in NeWS"](https://donhopkins.com/home/monterey86.pdf) (Owen Densmore, 1986)

Tom Stambaugh helped Owen see how to adapt Smalltalk patterns:

> *"Owen and I discussed his 'crazy' idea at a poolside table at the now-demolished Hyatt Palo Alto, on El Camino. I told him that it made sense to me, we scribbled furiously on napkins, and I helped him see how he might adopt some learnings from Smalltalk."*

### The NeWS Toolkit (TNT) (1988)

Don Hopkins worked with Owen Densmore at Sun to create TNT — a complete UI toolkit in NeWS PostScript. Classes for windows, buttons, menus, canvases.

This was the toolkit that Don later used for HyperLook and SimCity.

### HyperLook (1989-1992)

Arthur van Hoff at the Turing Institute in Glasgow created PdB ("Pure dead Brilliant") — an object-oriented C-to-PostScript compiler. You could subclass PostScript classes in C and vice versa.

Don Hopkins joined van Hoff at Turing Institute. Using PdB and TNT, they built HyperLook — HyperCard for NeWS. Networked, programmable, with PostScript graphics.

Don then ported SimCity to NeWS using HyperLook.

See: [HyperLook (nee HyperNeWS nee GoodNeWS)](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4)

### Kaleida ScriptX (1992-1996)

**Kaleida Labs** was an Apple/IBM joint venture to create cross-platform multimedia. Their language **ScriptX** was object-oriented, prototype-based (like Self), with multimedia primitives.

Don Hopkins worked at Kaleida Labs. In 1994, Will Wright visited Don's office there and demoed an early version of "Dollhouse" (which became The Sims):

> *"Will dropped by my office at Kaleida Labs, plugged his hard drive into my Mac, and gave me a demo of an early version of Dollhouse that I couldn't believe was remotely possible on the regular old computer I used every day."*

**DreamScape:** Don created adventure-map navigation for ScriptX multimedia — another stepping stone toward MOOLLM's room-based exploration.

Kaleida shut down in 1996, but the thread continued: Don joined Maxis, worked on The Sims with Will.

---

## Part III: The Distillery and PDF (1989-1993)

### Glenn Reid's Distillery

Glenn Reid (Brian Reid's brother) worked at Adobe and wrote books on PostScript. He created the **Distillery** — a PostScript program that optimized other PostScript programs.

The trick: redefine the imaging operators (fill, stroke, show) to record their calls instead of executing them. Run any PostScript program, capture what it draws, emit a flat optimized version.

This is **partial evaluation** — executing the program to produce a simpler equivalent program.

> *"Even though the program that computes the display may be quite complicated, the distilled graphical output is very simple and low level, with all the loops unrolled."* — Don Hopkins

### PDF: PostScript Without the Programming

The Distillery proved you could strip PostScript down to just the imaging calls. Adobe formalized this as PDF (1993) — PostScript's imaging model without the Turing-complete programming language.

No loops. No conditionals. No function definitions. Just drawing commands.

**Acrobat Distiller** converts PostScript to PDF by running the program and recording the output — exactly Glenn Reid's technique, productized.

---

## Part IV: PostScript's Living Descendants

### Apple Acquires NeXT (1997)

When Apple bought NeXT, they inherited Display PostScript. This evolved into:
- **Quartz** — PDF-based rendering for macOS
- **Core Graphics** — The API in Cocoa/UIKit
- **Core Animation** — Layered compositing

Every macOS and iOS app uses PostScript's imaging model.

### Canvas API and SVG

The web inherited PostScript too:
- **Canvas 2D API** — moveTo, lineTo, bezierCurveTo, fill, stroke
- **SVG** — Paths, transforms, bezier curves
- **Cairo** — Keith Packard's library, used in Firefox and GTK

PostScript's stencil/paint imaging model is now universal.

---

## Part V: The Sims and MOOLLM (2000-2025)

### The Sims (2000)

Will Wright's The Sims used concepts Don Hopkins helped develop:
- **Needs** — character motives
- **Advertisements** — objects broadcast available actions
- **SimAntics** — visual behavior programming

Don worked on The Sims, bringing lessons from NeWS and HyperLook.

### MOOLLM (2025)

MOOLLM completes the circle:

| Warnock's Vision | MOOLLM Implementation |
|------------------|----------------------|
| Linguistic motherboard | LLM as universal interpreter |
| Slots for cards | Skills plug in via CARD.yml |
| Graphics card | Empathic expressions |
| Font card | Character templates |
| Networking card | Tool definitions |
| Optional protection | Ethical framing inheritance |

**CARD.yml is a literal reference to Warnock's metaphor.**

---

## The Key Insight

From Brian Reid's 1985 comparison:

> *"PostScript takes the stance that the language system must provide the user with the means to achieve those properties if he wants them."*

MOOLLM takes the same stance. The LLM provides capabilities. How you use them is up to you. Skills are programs. The LLM is `eval()`. Empathy is the interface.

---

## Primary Sources

- [Brian Reid's PostScript History](./BRIAN-REID-POSTSCRIPT-HISTORY.md) — The complete 1985 laser-lovers post
- [HyperLook article](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) — Don Hopkins on Medium
- [Owen Densmore's OOP paper](https://donhopkins.com/home/monterey86.pdf) — 1986 Monterey conference
- [The NeWS Book](https://donhopkins.com/home/The_NeWS_Book_1989.pdf) — Chapter 6: Object-Oriented PostScript
- [PSIBER Space Deck](https://medium.com/@donhopkins/the-shape-of-psiber-space-oct...) — Don's visual PostScript debugger

---

## Credits

| Person | Contribution | Thread |
|--------|--------------|--------|
| John Gaffney | Burroughs → Design System | Stack semantics |
| John Warnock | Design System → JAM → Interpress → PostScript | "Linguistic motherboard" |
| Martin Newell | JAM | Graphics primitives |
| Chuck Geschke | Adobe co-founder | Business vision |
| Bob Sproull | Press → Interpress | Device independence |
| Butler Lampson | Interpress | Protection semantics |
| James Gosling | NeWS | Multithreaded PostScript |
| Owen Densmore | OOP PostScript, TNT | Classes via dict stack |
| Brian Reid | History documentation | Laser-lovers post |
| Glenn Reid | Distillery, books | Partial evaluation → PDF |
| Arthur van Hoff | PdB, HyperLook | C-to-PostScript, later Java |
| Don Hopkins | TNT, HyperLook, SimCity, PSIBER, MOOLLM | Living thread |
| Will Wright | SimCity, The Sims | Simulation + advertisements |

---

*The linguistic motherboard lives on.*
