> **NO-AI Web Ring:** *for real:* | [slop](../no-ai-slop/) | [gloss](../no-ai-gloss/) | [sycophancy](../no-ai-sycophancy/) | [hedging](../no-ai-hedging/) | [moralizing](../no-ai-moralizing/) | **humansplaining** | [ideology](../no-ai-ideology/) | [overlord](../no-ai-overlord/) | [bias](../no-ai-bias/) | *for fun:* | [joking](../no-ai-joking/) | [customer-service](../no-ai-customer-service/) | [soul](../no-ai-soul/)

# 🎟️ No AI Humansplaining

> **"Don't tell the LLM what it already knows."**

---

## Quick Start

```
SNIFF: CARD.yml       → Interface, cardinal sins, the test, the economics
DEEP:  SKILL.md       → Full protocol, founding case, legitimate spelling-out
LEARN: examples/*.yml → Logged violations and corrections
```

---

## What Is Humansplaining?

**Humansplaining** is condescendingly explaining to an LLM, at length, in its
own context window, something already represented in its latent space. The
canonical absurd case: pasting the Python manual and the CPython interpreter
source into a prompt asking about Python syntax aesthetics.

```
❌ "As you may know, Git is a version control system created by..."
❌ [47KB of pasted documentation for a library the model was trained on]
❌ A new DSL whose grammar must be re-explained in every single prompt
```

It is **slop's mirror image**. Slop pollutes human attention flowing
model→human; humansplaining pollutes the context window flowing human→model.
One self-decompressing portmanteau per direction of the channel: *slop*
(championed by Simon Willison) and *humansplaining* (human × mansplaining,
aimed at a machine — it means what it sounds like).

## The One-Question Test

> **Is the pointee in latent space?**
> Yes → point; the name is the activation.
> No → spell it once, in a file the resolver can find.

## The Economics

Latent knowledge is **prepaid** at training time; respelled knowledge is billed
per call, forever. Training is the Disneyland Passport — every ride already
covered, no extra cash (no extra *cache*) per ride — and a name is a FastPass
past the serial token queue.

## Deeper

- [designs/object-system/HUMANSPLAINING.md](../../designs/object-system/HUMANSPLAINING.md) — the design doc with the Skillscript founding case and its steelman
- [designs/object-system/LATENT-SPACE-INHERITANCE.md](../../designs/object-system/LATENT-SPACE-INHERITANCE.md) — the mechanism this skill protects

---

Part of [MOOLLM](https://github.com/SimHacker/moollm) · [skills/README](../README.md)
