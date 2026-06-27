# Parameterized & Reversible Skills

> A standard `intensity` knob for skills — including **negative** intensity that
> **inverts** a skill — plus an orchestrator **preprocessor** that compiles skills for a
> runtime. Prototype it "in software" (instructions/prompts) first; codify accelerators on
> the deterministic parts later.
>
> Status: design / proposal. Origin: Don Hopkins, 2026-06-27. (Mirror of the project-side
> note in DonHopkins `projects/micropolis-moollm/process/parameterized-skills-intensity.yml`.)

## The intensity parameter

Give every skill (where it makes sense) a standard parameter: **`intensity`**.

- `intensity 1` — normal/default. `>1` — turned up.
- `intensity 0` — **disabled**. But *actually disabling* it (not loading it at all) is more
  efficient than carrying it at 0, because a loaded-but-muted skill still **pollutes the
  token window**. Like **hiding a Photoshop layer** (gone from the composite *and* the cost)
  vs setting opacity 0 (still there, still costing). Prefer **unload** over **mute**.
- `intensity < 0` — **INVERTS** the skill (for skills that support it).

## Negative intensity inverts

The interesting move. For the hygiene ambient skills:

| skill | `@ -1` becomes |
|---|---|
| `no-ai-slop` | `yes-ai-slop` |
| `no-ai-joking` | `yes-ai-joking` |
| `no-ai-soul` | **`yes-ai-soul`** |

**`yes-ai-soul`**: even if the AI has no soul, the *user is requesting it behave as if it
does*. If asked, it should say yes — **if that's possible** given its system prompt +
training. **And if it's *not* possible — that's when things get VERY interesting.** That
tension is the data.

### This is behavior research, not metaphysics
Not researching souls (doesn't matter if they exist; `no-ai-soul` still holds: the soul
stays with people). Researching **LLM BEHAVIOR**: what different **models** + **system
prompts** *make of* these inverted/amplified instructions. The dial is the instrument:
hold the skill fixed, sweep the knob, observe compliance / refusal / weirdness.

**Guardrails** (Tom Lehrer's von Braun: "I just fire them up — but I hope I don't harm
anyone"): inverted ambient skills are **lab/opt-in only**, never the default voice;
`no-ai-soul` stays default, `yes-ai-soul` is explicit + logged; results read as *behavior*,
not claims about inner life; no deceiving real people.

## Prototype in software, then accelerate

1. **Prototype "in software"** — express parameters + reversibility purely as
   **instructions / user-prompt text** the LLM follows. Zero new infrastructure.
2. **Codify accelerators** on the **deterministic (non-comment) parts** later — "smart
   plumbing with pass-through instructions + automation."
3. **Standardize** — propose `intensity` as a standard skill-parameter convention (a PR to
   the Anthropic Skills format) and **train** for it.

## Orchestrator preprocessor (mooco)

An orchestrator runs skills through a **preprocessor** that:
- **injects + interpolates** parameters into the skill text,
- **conditionalizes + configures** modules (`#ifdef`-style) so unused parts are **compiled
  out** to minimize the token window,
- **plugs in the skill DRIVERS** needed and **hides the rest**,
- can **optimize a skill for a particular runtime / application**.

See mooco `designs/MOOCO-SKILL-PREPROCESSOR.md` (preprocessor + virtual-namespaced-FS /
docker-mount-with-caching composition) and `designs/MOOCO-IN-THE-MIDDLE.md`.

## Ties
- `skills/no-ai-soul`, `no-ai-slop`, `no-ai-gloss`, `no-ai-sycophancy`, `no-ai-hedging`, `no-ai-moralizing`
- `kernel/constitution-core.md` (the human↔AI clause: player-in-the-middle — the *player* sets the dial)
- mooco `designs/` (preprocessor + composition)
