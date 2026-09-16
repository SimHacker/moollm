# Dancing with Symmetry — Korz at Lang.NEXT 2014

Primary source bundle for Don Hopkins's planned async follow-up (Aug 2026).
David Ungar distills **Korz** — subjective, multi-dimensional context-oriented programming —
from the 2013 SPLASH-i talk into a Lang.NEXT 2014 episode.

**Same conference** as the Stroustrup × Hewitt × Ungar panel — two 2014 treasures, one async revisit project.

---

## Video

| Mirror | URL |
|--------|-----|
| **Microsoft Learn** (Lang.NEXT 2014) | https://learn.microsoft.com/en-us/shows/lang-next-2014/dancing-symmetry-to-harness-power-of-complexity-subjective-programming-in-context |
| **Lang.NEXT 2014 show hub** | https://learn.microsoft.com/en-us/shows/lang-next-2014/ |

**Episode title:** *Dancing with Symmetry to Harness the Power of Complexity: Subjective Programming in Context*  
**Speaker:** Dave Ungar

---

## What the talk covers (from episode description)

At any instant when you are programming, some details rise to the foreground and others recede
into the background context. The manner in which the programming language supports context
profoundly affects the ease of evolution and reuse.

Korz amplifies object-oriented programming by explicitly supporting **multi-dimensional context**,
using it for **dispatch** and **program organization**:

- Dispatch rules reduce to familiar delegation in the one-dimensional case
- All dimensions treated **equally and symmetrically**
- Programmers evolve the system by **adding dimensions**
- Many awkward OO situations become direct expression instead of ad hoc mechanisms
- **Progressive disclosure** — environments hide dimensions; developer-specific views smooth the learning curve

In this distillation: paradigm introduction, context-based dispatch details, glimpse of early prototype.

---

## Papers (repo copies)

| Paper | Link |
|-------|------|
| **Korz** (Onward! 2014) | [`korz-2014-onward.pdf`](https://dl.acm.org/doi/10.1145/2661136.2661147) · [Bret Victor refs](https://worrydream.com/refs/Ungar_2014_-_Korz_Simple,_Symmetric,_Subjective,_Context-Oriented_Programming.pdf) · [ACM](https://dl.acm.org/doi/10.1145/2661136.2661147) |
| **Foundation** (FOOL 2014) | `fool2014-korz-foundation.pdf` |
| **Deep dive + MOOLLM mapping** | [`korz-paper-deep-dive-moollm-mapping.md`](korz-paper-deep-dive-moollm-mapping.md) |

Lineage: **Us** (Smith & Ungar, TAPOS '96) → Korz → MOOLLM context-activated inheritance.

---

## 2026 ideas worth connecting (Don's listening agenda)

David pointed Don at Korz in **Oct 2025** — *"the natural extension of Self to multidimensional
(context | subjectivity)"* — and asked *"Is there anything like that today? Why not??"*
([`2025-10-26-korz-email-hn-rollup.md`](2025-10-26-korz-email-hn-rollup.md)).

| 2014 talk thread | 2026 repo thread |
|------------------|------------------|
| Multi-dimensional context dispatch | [`korz/design.md`](../korz-prime/README.md) — strict VM tier + soft LLM tier |
| Progressive disclosure / Stage Magic | MOOLLM GLANCE → CARD → SKILL pyramid |
| Symmetric dimensions | Korz eval battery · [`korz/korz-notes.md`](../korz-notes.md) |
| Early prototype glimpse | Two-minded Troll, Wumpus cartridge, Revolutionary Chess reparenting (`chat-guide.md` §5) |
| Subjectivity | Cross-Platform Troll = Korz subjective object in adventure-4 |

**Will Wright framing:** [*revisit those weird old ideas*](https://youtu.be/ofA6YWVTURU?t=3657) — Korz looked exotic in 2014; LLM dispatch + yaml-jazz rooms make it worth another listen.

---

## Planned follow-up (async)

Same shape as the Stroustrup/Hewitt panel follow-up:

1. Don re-listens; writes timestamped notes and questions
2. David answers **whatever he chooses**, on his schedule
3. Don drafts article — 2014 talk + 2026 MOOLLM/Korz′ mapping + David's replies
4. Optional: co-respondents from IBM Korz team (Ossher, Kimelman, Adams) if they want to chime in

**Article scaffold:** [`2026-08-korz-dancing-with-symmetry-article-scaffold.md`](2026-08-korz-dancing-with-symmetry-article-scaffold.md)

Format: TicketPR / written Q&A — no new video required.

↑ [Korz index](../README.md)
