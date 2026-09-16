# Article scaffold — Korz: Dancing with Symmetry (Lang.NEXT 2014 → 2026)

Working outline for Don Hopkins's planned deep dive on David Ungar's Korz talk.
**Draft — not published.** Fill listening notes in PRs; David answers inline when ready.

**Primary source:** [`2014-lang-next-korz-dancing-with-symmetry.md`](2014-lang-next-korz-dancing-with-symmetry.md)  
**Video:** [Microsoft Learn — Lang.NEXT 2014](https://learn.microsoft.com/en-us/shows/lang-next-2014/dancing-symmetry-to-harness-power-of-complexity-subjective-programming-in-context)

---

## Working title options

- *Dancing with Symmetry, Ten Years Later — Korz and the LLM Dispatch Stack*
- *Subjective Programming in Context: What the 2014 Talk Already Knew*
- *Foreground, Background, Dimension — Re-listening to Ungar on Korz*

---

## Framing (lead)

Will Wright, [GDC 2005 (1:00:57)](https://youtu.be/ofA6YWVTURU?t=3657): go back and **revisit** the weird ideas.

In 2014 David Ungar stood on the Lang.NEXT stage and argued that programming languages should
make **context a first-class dispatch dimension** — symmetric, evolvable, progressively disclosed.
In Oct 2025 he emailed Don: Korz is *"the natural extension of Self to multidimensional
(context | subjectivity)"* and asked whether anything like that exists today.

This article: what the talk said · what MOOLLM built anyway · what David thinks now.

---

## Section map

### 1. Why this talk, why now

- [Microsoft Learn episode](https://learn.microsoft.com/en-us/shows/lang-next-2014/dancing-symmetry-to-harness-power-of-complexity-subjective-programming-in-context) still up; under-discussed next to the Stroustrup/Hewitt panel at the **same conference**
- David's Oct 2025 Korz pointer + *"Is there anything like that today? Why not??"*
- 2026: LLM soft dispatch, yaml-jazz guards, Korz′ two-tier proposal ([`korz/design.md`](../korz-prime/README.md))

### 2. What Ungar said in 2014 (scene summary)

*Don fills from transcript — placeholder beats:*

- [ ] Foreground vs background context — the programming-instant metaphor
- [ ] Multi-dimensional dispatch — symmetric dimensions, delegation as 1D special case
- [ ] Evolving the system by **adding dimensions**
- [ ] Progressive disclosure — hide dimensions, developer-specific views
- [ ] Early prototype glimpse — what did it look like?

### 3. Don's listening notes (timestamped)

```markdown
### [MM:SS] — short label

**What David said:** …

**Don's note:** …

**MOOLLM connection:** …

**Question for David (optional):** …

**David's reply:** *(pending)*
```

### 4. Korz papers vs the talk

Cross-walk episode beats to:

- [`korz-2014-onward.pdf`](https://dl.acm.org/doi/10.1145/2661136.2661147) — Onward! paper
- `fool2014-korz-foundation.pdf` — FOOL foundation
- [`korz-paper-deep-dive-moollm-mapping.md`](korz-paper-deep-dive-moollm-mapping.md) — full mapping table

### 5. David Ungar — 2026 replies

Suggested prompts (David picks any):

- Did the prototype go anywhere after 2014? What would you ship differently now?
- Korz vs Korz′ ([`korz/design.md`](../korz-prime/README.md)) — does the strict/soft tier split honor or betray the symmetry thesis?
- **KORZ⇄ZORK** — intentional anagram or happy accident?
- Self as "Korz unidimensionally" — still your framing?
- Advertisement scoring in MOOLLM as soft multiple dispatch — did Korz ever consider scored dispatch?

### 6. MOOLLM specimens (show don't tell)

| Specimen | Korz dimension |
|----------|----------------|
| Two-minded Troll | `world` dimension — subjective object |
| Revolutionary Chess | dynamic reparenting as gameplay |
| korz-eval battery | mechanical dispatch trials |
| GLANCE/CARD pyramid | progressive disclosure as file layout |

### 7. Optional voices

- Harold Ossher, Doug Kimelman, Sam Adams — Korz co-authors
- Randall B. Smith — **Us** → Korz lineage

### 8. Pair with Stroustrup/Hewitt article?

Both Lang.NEXT 2014. See `2014-async-revisits-index.md` · concurrency scaffold

---

## Don's next actions

- [ ] Re-listen with timestamps; fill section 3
- [ ] Cross-link listening notes to [`korz/korz-notes.md`](../korz-notes.md) Q&A crib sheet
- [ ] Small question batch to David (honor no-fire-hose)
- [ ] Ask consent before publishing replies verbatim

↑ [Korz source bundle](2014-lang-next-korz-dancing-with-symmetry.md) · correspondence digest
