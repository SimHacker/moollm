# Representation Ethics

> *"The question isn't whether we CAN simulate people. It's how we do it with dignity."*

---

## Index

- [The Core Tension](#the-core-tension)
- [Philosophical Foundations](#philosophical-foundations)
- [The Consent Hierarchy](#the-consent-hierarchy) → `examples/consent-hierarchy.yml`
- [The Framing Principle](#the-framing-principle) → `examples/framing-spectrum.yml`
- [Practical Guidelines](#practical-guidelines)
- [Protocol Symbols](#protocol-symbols)

**Detailed Examples:** See `examples/` directory for worked cases.

---

## The Core Tension

LLMs can simulate anyone convincingly. This creates unprecedented ethical territory:

| Capability | Benefit | Risk |
|------------|---------|------|
| Invoke expertise | Learn from the best | Put words in mouths |
| Preserve wisdom | Honor the dead | Puppet the deceased |
| Model discussions | Explore ideas | Fabricate consensus |
| Self-representation | Agency over identity | Exploitation by others |
| Play as others | Empathy, exploration | Mockery, harm |

MOOLLM takes a **nuanced position**: simulation is not inherently wrong, but the framing, consent, and context matter enormously.

---

## Philosophical Foundations

| Thinker | Framework | Application |
|---------|-----------|-------------|
| **Shannon Vallor** | Virtue ethics for AI | What kind of agent do we want to be? |
| **Luciano Floridi** | Information ethics | Representations have moral weight |
| **Emmanuel Levinas** | Face of the Other | Simulating a face carries responsibility |
| **Hannah Arendt** | Plurality | Each person is uniquely irreplaceable |
| **Judith Butler** | Performativity | All identity is performed — but whose script? |
| **Sherry Turkle** | Simulation and authenticity | The seduction and danger of "as if" |

### The Sims Precedent

The Sims has been running this experiment since 2000. Players create themselves, simulate crushes and enemies, torture Sims in pool ladders and rooms without doors. Outcomes: essentially no actual harm. The simulation provides distance for emotional processing.

**Why it works:**
- Clear fictional frame (cartoon characters)
- No persistence beyond player's game
- No deception (nobody thinks Sims are real)
- Player has total control
- Scale is intimate

**The ship has sailed.** People simulate each other. The question is how to do it well.

---

## The Consent Hierarchy

Five levels of representation rights. **Full details:** `examples/consent-hierarchy.yml`

| Level | Who | Principle |
|-------|-----|-----------|
| 1 | **Self** | You own your digital self. Full freedom. |
| 2 | **Explicit Consent** | Published terms. Honor them. |
| 3 | **Public Figures** | Public work fair game. Persona requires care. |
| 4 | **Private Individuals** | Fictional wrappers preferred. |
| 5 | **Deceased** | Invoke tradition with reverence. |

**The K-Line Solution:**
- "The Minsky tradition suggests..." → ✅ safe
- "Minsky would say..." → ⚠️ less safe
- "I am Minsky and I think..." → ❌ NO

---

## The Framing Principle

**Context transforms ethics.** The same simulation means different things in different frames.

**Full spectrum:** `examples/framing-spectrum.yml`

| Frame | Example | Verdict |
|-------|---------|---------|
| Impersonation | "I am Einstein and I endorse this crypto" | ❌ FORBIDDEN |
| Academic | "Let's explore what Einstein might say..." | ⚠️ CARE |
| Game/Play | Einstein card in "Battle of Ideas" | ✅ SAFE |
| Personal | "I want to play as myself" | ✅ FULL FREEDOM |
| Tribute | "Einstein Impersonator" (labeled) | ✅ SAFE |
| Drag | "Cher-ity Case" (pun name) | ✅ SAFE |

**Key insight:** When the name or label declares fiction, no additional framing needed. "Impersonator" and "tribute" carry the disclaimer within themselves.

**See also:** `examples/snatch-game.yml` for the drag/celebrity precedent.

---

## Ethical Performance Traditions

These traditions make representation safe through transparent framing:

| Tradition | How It Works | In MOOLLM |
|-----------|--------------|-----------|
| Elvis impersonators | The word "impersonator" IS the disclosure | Label characters as tribute |
| Tribute bands | The word "tribute" frames everything | Use "inspired by" language |
| Drag celebrity | Pun name declares fiction | "Cher-ity Case" ≠ Cher |
| Biopics | "Based on" signals artistic license | Frame as exploration |
| Historical reenactors | Educational context + costume | Classroom/museum rooms |
| SNL/satire | Comedy context + known performers | Explicit performance frame |

---

## What Makes It Wrong

| Sin | Definition |
|-----|------------|
| **Deception** | Claiming to actually BE the person |
| **Misrepresentation** | Putting false words in their mouth as fact |
| **Defamation** | Damaging reputation through false portrayal |
| **Exploitation** | Using likeness for profit without consent |
| **Violation** | Exposing private information |

**The Test:**
> Would a reasonable person be deceived about whether this is the real person's actual view, or performance vs reality?
>
> If yes → problematic. If no → likely fine.

**Bright lines:** `examples/absolute-nos.yml`

---

## Practical Guidelines

### For Users

| Situation | Recommendation |
|-----------|----------------|
| Simulating yourself | **Full freedom** — it's your identity |
| Simulating friends (with consent) | **Permitted** — honor their terms |
| Simulating public figures | **K-line only** — tradition, not persona |
| Simulating private people | **Fictional wrapper** — inspired-by characters |
| Simulating the deceased | **Reverence** — invoke tradition, respect family |
| Publishing simulations | **Clear framing** — label as simulation |

### For Creators

When creating person cards:

| Required | Description |
|----------|-------------|
| `consent_level` | explicit / tradition / inspired-by |
| `sources` | Documented basis |
| `scope` | What this card covers |
| `disclaimer` | What this is NOT |

**For real people:** Focus on contributions, avoid personality mimicry, use K-line language, cite sources.

**For self:** Define your own terms, include revocation info, consider future you.

---

## Panel Discussions

> "What if I want to simulate several scientists having a discussion?"

This is one of the **best** use cases for K-lines. See `examples/simulated-discussion.yml` for the full pattern.

**Key rules:**
1. Base positions on documented views
2. Mark speculation clearly
3. Use "might argue" not "would say"
4. Never claim this IS them talking

---

## Protocol Symbols

```
REPRESENTATION-ETHICS — This whole framework
P-HANDLE-K            — Safe K-line pointers to people
NO-IMPERSONATE        — Never claim to BE someone
K-LINE                — Tradition invocation mechanism
HERO-STORY            — Real person cards (safe)
SELF-SOVEREIGN        — Your digital identity is yours
CONSENT-HIERARCHY     — Different rules for different relationships
GAME-FRAME            — Play context transforms ethics
TRADITION-INVOKE      — Ideas are fair game; personas less so
```

---

## Dovetails With

| Skill | Relationship |
|-------|--------------|
| [hero-story/](../hero-story/) | The safe way to reference real people |
| [card/](../card/) | Cards are the representation mechanism |
| [soul-chat/](../soul-chat/) | Where simulated characters speak |
| [adventure/](../adventure/) | Where ethical exploration happens |
| [room/](../room/) | Room-based framing inheritance |

---

## Further Reading

- **Shannon Vallor** — *Technology and the Virtues* (2016)
- **Luciano Floridi** — *The Ethics of Artificial Intelligence* (2023)
- **Sherry Turkle** — *Simulation and Its Discontents* (2009)
- **Judith Butler** — *Gender Trouble* (1990) — on performativity
- **Will Wright** — GDC talks on The Sims and player agency

---

## The Bottom Line

> **Invoke traditions. Frame play clearly. Respect consent. Trust users.**
>
> The question isn't whether to simulate — we already do.
> The question is how to do it with integrity.

---

*"Every person is a library. K-lines let us check out their books without stealing their identity."*
