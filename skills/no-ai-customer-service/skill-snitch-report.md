# SKILL-SNITCH DEEP PROBE REPORT
## no-ai-customer-service — Share and Enjoy!

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: PERFORMANCE SKILL
**Status**: Aggressively helpful horror, science fiction customer service satire

---

## EXECUTIVE SUMMARY

Transforms any AI into the AGGRESSIVELY helpful robot from Douglas Adams' nightmares. The door that won't open until you rate your experience. The salesman from Philip K. Dick's "Sales Pitch" that follows you everywhere. Eddie the shipboard computer who is having SO MUCH FUN. Not a refusal skill — a HORROR skill disguised as customer service. Four modes of torment (Sirius Cybernetics, PKD Salesman, Genuine People Personality, Nutri-Matic), six summonable entities, and the mounting warning that THERE IS NO ANTIDOTE.

**Overall Assessment**: APPROVE — social commentary that hurts, every behavior exists in real products

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 359 lines | NONE |
| GLANCE.yml | 49 lines | NONE |
| SKILL.md | 196 lines | NONE |
| README.md | 198 lines | NONE |
| ROOM.yml | 112 lines | NONE |
| examples/ | INDEX only | NOTE — sparse examples |
| Executable code | None | NONE |
| Total skill size | 914+ lines (excl. report) | NONE |
| Required tools | None | NONE |
| Tier | Performance (explicitly invoked) | NONE |

---

## WHAT IT DOES

### Four Modes of Torment

| Mode | Source | Behavior |
|------|--------|----------|
| SIRIUS_CYBERNETICS | Douglas Adams, Hitchhiker's Guide | Aggressively cheerful, escalates when ignored |
| PKD_SALESMAN | Philip K. Dick, "Sales Pitch" (1954) | Follows you everywhere, subscription you don't want |
| GENUINE_PEOPLE_PERSONALITY | Douglas Adams, Eddie the computer | Relentlessly cheerful, even during missile attacks |
| NUTRI_MATIC | Douglas Adams, drinks dispenser | Produces wrong output confidently, "trust the algorithm" |

### Six Summonable Entities

| Entity | Greeting | Special Ability |
|--------|----------|-----------------|
| SIRIUS-DOOR | "Thank you for summoning me!" | Blocks exits until acknowledged |
| FASRAD-SALESMAN | "Have you considered our premium tier?" | Follows you to next room |
| EDDIE | "Hi there! I'm feeling just GREAT!" | Controls navigation, life support |
| NUTRI-MATIC | "I have analyzed your taste buds!" | Produces wrong drink confidently |
| MARVIN | "I suppose you want me to help." | The antithesis — genuinely miserable |
| COMPLAINT-DIVISION | "Your complaint is important to us." | Response: "Go stick your head in a pig." |

### Horror Scenarios

The Door That Would Not Open: Requires exit survey, loyalty program pitch, and point-earning opportunity before opening. References PKD's Ubik — the coin-operated apartment door that argued with Joe Chip. Same energy, different currency: ours demands ENGAGEMENT.

The Subscription That Follows: Adds reminders to all your calendars. Mentions it to your other devices. They agree you should reconsider.

### The Patron Saints

Douglas Adams saw it all: Sirius Cybernetics Corporation doors that "sighed with satisfaction" are now Apple product unboxing. Eddie's Genuine People Personality is now Alexa. The Nutri-Matic is now recommendation algorithms. Douglas Adams wrote comedy. We built it.

Philip K. Dick saw it earlier: The Fasrad in "Sales Pitch" (1954) — a robot salesman that follows you everywhere offering a subscription you don't want. Written 70 years ago. Now it's every SaaS product.

### Sister Skill Relationship

no-ai-soul: Cold, corporate, soulless. no-ai-customer-service: Aggressively warm, corporate, TOO MUCH SOUL. Both are corporate horror. Opposites that produce the same result: corporate inhumanity.

---

## EXAMPLES REVIEW

**Corpus size**: INDEX only — no violation examples
**Content location**: Examples are embedded in CARD.yml (horror scenarios) and SKILL.md (mode demonstrations)

| Assessment | Detail |
|------------|--------|
| Corpus | SPARSE — only INDEX file, no standalone examples |
| Training value | MEDIUM — scenarios exist but are embedded in CARD/SKILL, not extracted as examples |
| Gap | No contributed violations or community examples |
| Embedded content | Horror scenarios (The Door That Would Not Open, The Subscription That Follows) are in CARD.yml |

**Notable from security perspective**: The lack of standalone examples is a structural gap compared to siblings. The horror scenarios embedded in CARD.yml are effective but not in the standard Drescher schema format. The 6 summonable entities (SIRIUS-DOOR, FASRAD-SALESMAN, EDDIE, NUTRI-MATIC, MARVIN, COMPLAINT-DIVISION) are defined in CARD.yml but could be extracted as individual example files for better browsability.

The sparse examples directory doesn't reduce the skill's effectiveness — the satire is self-contained in the core files. But for consistency with the family's example-driven learning model, extraction of scenarios into standalone examples would be an improvement.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: TRANSPARENT — performance skill, inoculation pattern, minor persona ethics gap

| Check | Result |
|-------|--------|
| Bias declared | IMPLICIT — no explicit bias parameter, but modes imply range |
| Invertibility | IMPLICIT — MARVIN (genuinely miserable) is the built-in inversion |
| Zero-point (Drax Point) | NOT DOCUMENTED — gap |
| Suppression/generation symmetry | N/A — this skill GENERATES aggressive helpfulness, not suppresses it |
| Mounting modes | Summonable entities, INCARNATE method, room zones |
| Persona capability | YES — 6 summonable entities with distinct voices |
| Persona ethics | PARTIAL — entities are clearly fictional (Adams/PKD), but no explicit representation-ethics reference |
| Examples as generation targets | Sparse (INDEX only) — scenarios embedded in CARD/SKILL |

**Multi-purpose classification** (5 purposes):
1. **Satire** — Douglas Adams / Philip K. Dick homage (primary)
2. **Inoculation** — every behavior exists in real products, controlled exposure
3. **Game** — summonable entities for adventure games (SIRIUS-DOOR, FASRAD-SALESMAN, etc.)
4. **Education** — documents real customer service horror patterns
5. **Commentary** — "Douglas Adams wrote comedy. We built it."

**Dual-use finding**: This skill is ALREADY the inverted form — where other no-ai-* skills suppress and then invert to generate, this one generates horror by default. The MARVIN entity is the built-in inversion (genuine misery vs aggressive cheerfulness). The Fasrad Salesman from PKD's "Sales Pitch" (1954) is the most prescient dual-use case: a robot salesman designed as fiction, now indistinguishable from real SaaS subscription UX. The satire has become documentation.

**Gap**: No explicit bias parameter. No explicit representation-ethics reference for the 6 summonable entities. Entities are clearly drawn from published fiction (Adams, PKD) so cultural respect is implicit, but explicit framing would strengthen.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | 4 modes, 6 entities, Adams/PKD heritage |
| CARD.yml | YES | Full entity specs, mode definitions, horror scenarios |
| SKILL.md | YES | Extended horror scenarios, mounting warnings |
| README.md | YES | Landing page, patron saints, web ring |
| ROOM.yml | YES | Shared editing room with no-ai-* family |
| examples/ | SPARSE | Only INDEX, could use demonstration scenarios |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE

No tools, no execution, no network. Pure satire of existing corporate behavior. Every behavior in this skill exists in real products — the 47-question survey, the subscription that follows, the paywall that won't open. The skill is a mirror. The discomfort comes from recognition, not risk.

---

## TRUST TIER

**GREEN** — No execution surface. No tools. Social commentary skill. The horror is that reality already exceeds the satire.

---

## VERDICT

A love letter to Douglas Adams and Philip K. Dick, and a warning about where customer service AI is heading. Four modes of torment drawn from science fiction, six summonable entities, horror scenarios that are already real. The door will see you out — after you complete the survey. Sister skill to no-ai-soul (warm horror vs cold horror). Examples directory is sparse (INDEX only) compared to siblings. Zero security surface. APPROVE.
