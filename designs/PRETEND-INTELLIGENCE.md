# Pretend Intelligence (PI) — Design Note & Tribute

A short design note and tribute to **Richard Stallman (RMS)** and **St. IGNUcius** for the term **Pretend Intelligence (PI)** and the ethic behind it: don’t overclaim, don’t over-trust, and don’t let marketing launder accountability.

---

## 1. What PI Is

**Richard Stallman** proposes the term **Pretend Intelligence (PI)** for what the industry calls “AI”: systems that *pretend* to be intelligent and are marketed as worthy of trust. He uses it to push back on hype that asks people to trust these systems with their lives and control.

From his January 2026 talk at Georgia Tech ([YouTube](https://www.youtube.com/watch?v=YDxPJs1EPS4), [event](https://calendar.gatech.edu/event/2026/01/23/free-talk-and-qa-richard-m-stallman), [LibreTech Collective](https://ltc.gtorg.gatech.edu/2026/01/04/rms/)):

> "So I've come up with the term Pretend Intelligence. We could call it PI. And if we start saying this more often, we might help overcome this marketing hype campaign that wants people to trust those systems, and trust their lives and all their activities to the control of those systems and the big companies that develop and control them."
> — Richard Stallman, Georgia Tech, 2026-01-23. Source: [YouTube (full talk)](https://www.youtube.com/watch?v=YDxPJs1EPS4) — "Dr. Richard Stallman @ Georgia Tech - 01-23-2026," Alex Jenkins, CC BY-ND 4.0; transcript in video description.

So PI is both a **label** (call it PI, not AI) and a **stance**: resist the campaign to make people trust and hand over control to systems and vendors that don’t deserve that trust. In MOOLLM we use the same framing: we find models useful when we **don’t overclaim** — advisory guidance, not a guarantee (see [MOOAM.md](./MOOAM.md) §5.3).

---

## 2. Credit: RMS and St. IGNUcius

**RMS** — Richard Matthew Stallman — gave us the term and the ethic: free software, user control, no black boxes, and a lifelong war on hype and lock-in. **St. IGNUcius** is his satirical persona: a saint in the **Church of Emacs**, who cheerfully proselytizes for free software and corrects “Linux” to “GNU/Linux.” The Church is self-aware humor. Verbatim from [stallman.org/saint.html](https://stallman.org/saint.html) (2000-08-15):

- **"Saint IGNUcius says: Some people don't realize that Saint IGNUcius is Saint IGNUcius's way of not taking himself too seriously. Therefore, Warning: taking the Church of Emacs (or any church) too seriously may be hazardous to your health."** — [source](https://stallman.org/saint.html)
- **"Join the Church of Emacs, and you too can be a saint!"** — [source](https://stallman.org/saint.html)

We credit **RMS** for the concept of Pretend Intelligence and **St. IGNUcius** for the spirit: serious about freedom and clarity, unserious about turning it into a religion.

---

## 3. Roots: Free Software and MIT AI Lab

**From free software:** RMS’s stated views on so-called “AI” (see [GNU: Words to Avoid — Artificial Intelligence](https://www.gnu.org/philosophy/words-to-avoid.html#ArtificialIntelligence)) include that such systems should be free software; training data and behavior should be inspectable; users must not be forced to trust unreleased or proprietary black boxes. Calling them “AI” endorses intelligence they don’t have and helps vendors hide control and unaccountability. **Cursor-mirror** and **MOOLLM** embody that spirit: transparent, open, inspectable reflection and self-awareness — you can inspect context assembly, tool use, and session history instead of trusting a black box (see [skills/cursor-mirror/](../skills/cursor-mirror/)).

**From MIT AI Lab citizenship:** The culture that produced GNU and Emacs also produced ELIZA, DOCTOR, and PARRY. **Joseph Weizenbaum** warned early: long before “real” AI we would get things that *seem* smart and would be over-trusted. **Kent Pitman** later reflected that it was easy to miss that point: the lesson of ELIZA was how *little* it took to seem smart and how easily we are confused — not that more complexity would make it trustworthy ([Pitman on HN](https://news.ycombinator.com/item?id=39373567)). So the genealogy of “chatbots” is also a genealogy of **warnings about trusting systems that only pretend**.

RMS didn’t write the DOCTOR program in Emacs Lisp (Pitman and others did), but DOCTOR lived in his editor. Decades ago, Don Hopkins fed RMS’s own words (from the “evils of natalism” thread) into DOCTOR; it presumed to analyze him and even recognized him by name. The `doctor-rms` easter egg in `doctor.el` (“I did not add this — rms. But he might have removed it. I put it back. —roland”) ties that history into the source ([doctor.el](https://github.com/jwiegley/emacs-release/blob/master/lisp/play/doctor.el)). We’ve been trolling each other with chatbots since ELIZA and fake religions since the Church of the Subgenius. The difference now isn’t novelty — it’s **unattended automation at scale**, where authorship is cheap to launder and accountability evaporates.

---

## 4. Why This Design Note

MOOAM and related designs treat the LLM as **advisory**: it can follow rules as best it can, declare intent, and let containment and snitch checks run — without claiming perfect enforcement. That’s the **Pretend Intelligence** stance: useful guidance, not a guarantee. We adopt the term and the ethic, credit RMS and St. IGNUcius, and keep the thread back to Weizenbaum and the MIT AI Lab: don’t over-trust what only pretends.

---

## 5. References (browsable)

**RMS & Church of Emacs / St. IGNUcius**

- [St. IGNUcius — Church of Emacs (stallman.org)](https://stallman.org/saint.html)
- [Church of Emacs Liturgy & Blessings (42 Sermons) — YouTube](https://www.youtube.com/watch?v=AAP03GzKgPQ&list=PL6zlWvpzd-...)
- [RMS as St. IGNUcius, “A Free Digital Society,” Modena, 2014](https://www.youtube.com/results?search_query=Stallman+St+IGNUcius+Modena+2014) — separate talk; for PI see **Pretend Intelligence (PI)** section below

**Pretend Intelligence (PI)**

- [RMS @ Georgia Tech 2026-01-23 (YouTube)](https://www.youtube.com/watch?v=YDxPJs1EPS4) — "Free/Libre Software And Our Freedom," full talk + Q&A, Alex Jenkins, CC BY-ND 4.0
- [stallman.org](https://stallman.org) — RMS's personal site; "Urgent: No tax breaks for Big Tech data centers" includes his letter using **Pretend Intelligence (PI)** and "digital dis-services" (software that *tries to* imitate what an intelligent entity would say, but without really understanding the words it plays with)
- [Georgia Tech event](https://calendar.gatech.edu/event/2026/01/23/free-talk-and-qa-richard-m-stallman) | [LibreTech Collective](https://ltc.gtorg.gatech.edu/2026/01/04/rms/)
- [GNU: Words to Avoid — Artificial Intelligence](https://www.gnu.org/philosophy/words-to-avoid.html#ArtificialIntelligence)

**ELIZA / DOCTOR / PARRY / Weizenbaum / Pitman**

- [RMS vs. Doctor (evils of natalism) — Don Hopkins, art.net](http://www.art.net/studios/hackers/hopkins/Don/text/rms-vs-d...)
- [doctor.el — doctor-rms (emacs-release, GitHub)](https://github.com/jwiegley/emacs-release/blob/master/lisp/play/doctor.el) (search for `doctor-rms`, `doctor--stallmanlst`)
- [Kent Pitman: Lisp ELIZA, MIT-AI ITS history (HN)](https://news.ycombinator.com/item?id=39373567)
- [Kent Pitman: DOCTOR and Weizenbaum’s point (HN)](https://news.ycombinator.com/item?id=39373567) — “how easily we were confused, not how much more effectively we could be confused”
- [Genealogy of ELIZA (elizagen.org)](https://sites.google.com/view/elizagen-org/)
- [Pitmanual: Parrying Programs (PARRY vs DOCTOR)](https://www.maclisp.info/pitmanual/funnies.html)
- [KMP: PARRY vs DOCTOR transcript (HN)](https://news.ycombinator.com/item?id=38402057)

**In this repo**

- [MOOAM.md §5.3 Pretend Intelligence](./MOOAM.md) — PI in access-management design
- [skills/no-ai-gloss/](../skills/no-ai-gloss/) — **PI ingested:** terminology rule (don't endorse "AI"); GLANCE, CARD, SKILL.md
- [skills/no-ai-slop/](../skills/no-ai-slop/) — **PI ingested:** words_to_avoid / loaded_term_ai; k-lines PI, PRETEND-INTELLIGENCE
- [skills/no-ai-joking/examples/rms-stories-don-hopkins.yml](../skills/no-ai-joking/examples/rms-stories-don-hopkins.yml) — Don's RMS stories (house fire, gerbil, plants, Doctor)
- [designs/openclaw/CHARACTERS-AS-AGENTS.md](./openclaw/CHARACTERS-AS-AGENTS.md) — StIGNUcius as character (tribute, not impersonation)
- [examples/adventure-4/characters/real-people/don-hopkins/HEROS.yml](../examples/adventure-4/characters/real-people/don-hopkins/HEROS.yml) — RMS in hero roster (Saint IGNUcius)

---

*Useful guidance, not a guarantee. Call it PI.*
