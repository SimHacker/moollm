# Pretend Intelligence (PI) — Richard Stallman's term

An essay on **Richard Stallman (RMS)** and his term **Pretend Intelligence (PI)**: what he means by it, and the ethic he attaches to it. The term is his. This file records that account so it can be set beside other ideologies and stay in the argument. Its role is seed and fertilizer for ongoing discussion.

---

## 1. What he means

**Richard Stallman** proposes the term **Pretend Intelligence (PI)** for what the industry calls “AI”: systems that *pretend* to be intelligent and are marketed as worthy of trust. He uses it to push back on hype that asks people to trust these systems with their lives and control.

From his January 2026 talk at Georgia Tech ([YouTube](https://www.youtube.com/watch?v=YDxPJs1EPS4), [event](https://calendar.gatech.edu/event/2026/01/23/free-talk-and-qa-richard-m-stallman), [LibreTech Collective](https://ltc.gtorg.gatech.edu/2026/01/04/rms/)):

> "So I've come up with the term Pretend Intelligence. We could call it PI. And if we start saying this more often, we might help overcome this marketing hype campaign that wants people to trust those systems, and trust their lives and all their activities to the control of those systems and the big companies that develop and control them."
> — Richard Stallman, Georgia Tech, 2026-01-23. Source: [YouTube (full talk)](https://www.youtube.com/watch?v=YDxPJs1EPS4) — "Dr. Richard Stallman @ Georgia Tech - 01-23-2026," Alex Jenkins, CC BY-ND 4.0; transcript in video description.

For him, PI is both a **label** and a **stance**. The label puts “pretend” where the industry puts “artificial,” so the name itself says the systems are pretending. The stance resists a campaign to make people trust those systems, and the companies behind them, with their lives and their control.

That is his proposal, in his words. The comparisons below are for argument. They leave the term his.

---

## 2. The person and the saint

**RMS** — Richard Matthew Stallman — is the author of the term and of the ethic he ties to it: free software, user control, no black boxes, and a lifelong argument against hype and lock-in. **St. IGNUcius** is his satirical persona: a saint in the **Church of Emacs**, who cheerfully proselytizes for free software and corrects “Linux” to “GNU/Linux.” The Church is self-aware humor. Verbatim from [stallman.org/saint.html](https://stallman.org/saint.html) (2000-08-15):

- **"Saint IGNUcius says: Some people don't realize that Saint IGNUcius is Saint IGNUcius's way of not taking himself too seriously. Therefore, Warning: taking the Church of Emacs (or any church) too seriously may be hazardous to your health."** — [source](https://stallman.org/saint.html)
- **"Join the Church of Emacs, and you too can be a saint!"** — [source](https://stallman.org/saint.html)

The comic spirit is his too. He is serious about freedom and clarity, and unserious about turning that seriousness into a religion. Taking the saint as a metaphysics would miss the warning he printed on the saint page.

---

## 3. Where the term comes from

**From free software.** RMS’s stated views on so-called “AI” (see [GNU: Words to Avoid — Artificial Intelligence](https://www.gnu.org/philosophy/words-to-avoid.html#ArtificialIntelligence)) include that such systems should be free software; training data and behavior should be inspectable; users must not be forced to trust unreleased or proprietary black boxes. On his account, calling them “AI” endorses intelligence they don’t have and helps vendors hide control and unaccountability. [Cursor-mirror](../skills/cursor-mirror/) is one concrete place to hold that demand up against a tool that exposes its context assembly, tool use, and session history. Agreement is a question for the discussion, and his conditions are stated here as his.

**From the MIT AI Lab.** The culture that produced GNU and Emacs also produced ELIZA, DOCTOR, and PARRY. **Joseph Weizenbaum** warned early: long before “real” AI we would get things that *seem* smart and would be over-trusted. **Kent Pitman** later reflected that it was easy to miss that point: the lesson of ELIZA was how *little* it took to seem smart and how easily we are confused — not that more complexity would make it trustworthy ([Pitman on HN](https://news.ycombinator.com/item?id=39373567)). Read that way, the genealogy of “chatbots” is also a genealogy of warnings about trusting an appearance.

DOCTOR came to Emacs from the Lisp DOCTOR tradition (Bernie Cosell's BBN Lisp version, Kent Pitman's MacLisp DOCTOR on ITS), and the first known `doctor.el` (Emacs 17.61, 1986) says "Copyright (C) 1985 Sidney Markowitz and Richard M. Stallman" ([4.3BSD copy](https://github.com/larsbrinkhoff/emacs-history/blob/sources/www.tuhs.org/UnixArchive/4BSD/Distributions/4.3BSD/emacs/lisp/doctor.el)). So DOCTOR lived in his editor under his own name. It is programmed to recognize its creator and does not understand him. The words `rms` and `stallman` are entries in the script; `doctor-rms` answers from a list of lines about Stallman. Decades ago, Don Hopkins fed RMS’s own words (from the “evils of natalism” thread) into DOCTOR, and it presumed to analyze him because the name was on that list. The recognition was, then was not, then was again. On `doctor-rms` in [doctor.el](https://github.com/emacs-mirror/emacs/blob/master/lisp/play/doctor.el) the notes read “I did not add this -- rms” and “But he might have removed it. I put it back. --roland”: RMS disclaiming the addition, the feature gone, Roland restoring it. We’ve been trolling each other with chatbots since ELIZA and fake religions since the Church of the Subgenius. The difference now is **unattended automation at scale**, where authorship is cheap to launder and accountability evaporates.

---

## 4. Beside other ideologies

The term stays his. These are accounts worth setting next to it.

**McCarthy’s name.** John McCarthy wrote “artificial intelligence” into the proposal for the Dartmouth Summer Research Project, dated 31 August 1955. The workshop met in the summer of 1956, which is the date usually given for the birth of the field. The proposal’s conjecture is that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it. The word covers that work. Defenders of the name, Ted Selker among them, add that the field coined it, that it is a broad name for work toward intelligent systems, and that people outside a field do not get to mandate what the field calls its work. McCarthy is reported to have preferred it to “machine intelligence” because “machine intelligence” sounded less interesting. His conjecture already says *simulate*.

**Weizenbaum’s warning.** Seeming intelligent is cheap, and people trust the appearance. That objection is older than the current marketing campaign, and Pitman’s retelling of it is linked above. It sits close to Stallman’s stance about trust, and it says something different about the machinery: the danger he named was the audience.

**Use without understanding.** Emacs does not understand the buffer. A great deal of its usefulness comes from Lisp, a programming language from this same field, and the Lisp in Emacs does not understand anything either. Its DOCTOR program is programmed to recognize its creator, RMS, and does not understand him. That recognition was, then was not, then was again. Stallman maintains Emacs anyway. He has not treated that old symbol-processing as a reason to abandon the tool. Affection for Emacs is affection for a tool in that condition. Usefulness and understanding come apart. Current systems that generate code and process information are open to the same test. Those abilities can be real. His diatribe can still be interesting as an argument about marketing, trust, and control, which is a different question from whether the tool can do the work.

This file is here so that comparison can keep going. His words stay available, and so do the objections.

---

## 5. References (browsable)

**RMS & Church of Emacs / St. IGNUcius**

- [St. IGNUcius — Church of Emacs (stallman.org)](https://stallman.org/saint.html)
- [Church of Emacs Liturgy & Blessings (42 Sermons) — YouTube](https://www.youtube.com/watch?v=AAP03GzKgPQ&list=PL6zlWvpzd-...)
- [RMS as St. IGNUcius, “A Free Digital Society,” Modena, 2014](https://www.youtube.com/results?search_query=Stallman+St+IGNUcius+Modena+2014) — separate talk; for PI see **What he means** above

**Pretend Intelligence (PI)**

- [RMS @ Georgia Tech 2026-01-23 (YouTube)](https://www.youtube.com/watch?v=YDxPJs1EPS4) — "Free/Libre Software And Our Freedom," full talk + Q&A, Alex Jenkins, CC BY-ND 4.0
- [stallman.org](https://stallman.org) — RMS's personal site; "Urgent: No tax breaks for Big Tech data centers" includes his letter using **Pretend Intelligence (PI)** and "digital dis-services" (software that *tries to* imitate what an intelligent entity would say, but without really understanding the words it plays with)
- [Georgia Tech event](https://calendar.gatech.edu/event/2026/01/23/free-talk-and-qa-richard-m-stallman) | [LibreTech Collective](https://ltc.gtorg.gatech.edu/2026/01/04/rms/)
- [GNU: Words to Avoid — Artificial Intelligence](https://www.gnu.org/philosophy/words-to-avoid.html#ArtificialIntelligence)

**ELIZA / DOCTOR / PARRY / Weizenbaum / Pitman**

- [RMS vs. Doctor (evils of natalism) — Don Hopkins](https://donhopkins.com/home/catalog/text/rms-vs-doctor.html)
- [doctor.el — doctor-rms (emacs-release, GitHub)](https://github.com/jwiegley/emacs-release/blob/master/lisp/play/doctor.el) (search for `doctor-rms`, `doctor--stallmanlst`)
- [Kent Pitman: Lisp ELIZA, MIT-AI ITS history (HN)](https://news.ycombinator.com/item?id=39373567)
- [Kent Pitman: DOCTOR and Weizenbaum’s point (HN)](https://news.ycombinator.com/item?id=39373567) — “how easily we were confused, not how much more effectively we could be confused”
- [Genealogy of ELIZA (elizagen.org)](https://sites.google.com/view/elizagen-org/)
- [Pitmanual: Parrying Programs (PARRY vs DOCTOR)](https://www.maclisp.info/pitmanual/funnies.html)
- [KMP: PARRY vs DOCTOR transcript (HN)](https://news.ycombinator.com/item?id=38402057)

**Discussion elsewhere in this repo**

These cite the term or tell stories around him. They are part of the discussion. They are not this essay granting his ethic to MOOLLM.

- [MOOAM.md §5.3 Pretend Intelligence](./MOOAM.md) — cites the term while discussing advisory limits
- [skills/no-ai-gloss/](../skills/no-ai-gloss/) — a skill note with its own terminology preference, pointing here
- [skills/no-ai-slop/](../skills/no-ai-slop/) — a skill note that lists the term among loaded words, pointing here
- [skills/no-ai-joking/examples/rms-stories-don-hopkins.yml](../skills/no-ai-joking/examples/rms-stories-don-hopkins.yml) — Don's RMS stories (house fire, gerbil, plants, Doctor)
- [designs/eval/CHURCH-OF-EMACS.md](./eval/CHURCH-OF-EMACS.md) — St. IGNUcius; reads this essay as a late sermon
- [designs/eval/CHURCHES.md](./eval/CHURCHES.md) — index of rites
- [examples/adventure-4/characters/real-people/don-hopkins/HEROS.yml](../examples/adventure-4/characters/real-people/don-hopkins/HEROS.yml) — RMS in hero roster (Saint IGNUcius)

---

*His term. Written down here to be compared, and to keep the argument going.*
