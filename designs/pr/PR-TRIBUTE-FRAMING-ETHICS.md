# PR: Tribute Framing — Ethical Representation of Real People 🎭❤️

## TL;DR
We realized our depictions of real people (Andy & Kristin Looney, Cheech & Chong) needed explicit framing as **tribute performances** rather than documentary claims. We've added the three-beat protocol: **INVOCATION → PERFORMANCE → ACKNOWLEDGMENT**.

---

## The Ethical Question

We asked ourselves: *Does our treatment of real people in the narrative follow our own ethical guidelines?*

The answer was: **Almost, but not quite.**

The depictions were affectionate, accurate to their known personalities, and respectful. But they lacked *explicit framing* that distinguished "tribute simulation" from "claimed documentation."

---

## The Solution: The Three-Beat Protocol

### 1. INVOCATION (Before They "Arrive")
> *"Let's invoke them. In the spirit of tribute. Imagine they're here..."*

Makes clear we're **summoning** them as loving imagination, not claiming they actually appeared.

### 2. PERFORMANCE (The Scene Itself)
The scene plays out with a banner note:
> 🎭 **TRIBUTE PERFORMANCE:** *The following is a loving simulation — what we imagine it might be like if these legends visited our Grotto. All dialogue is imagined with affection.*

### 3. ACKNOWLEDGMENT (After They "Depart")
> *"That was a tribute. A simulation. We honored them by imagining them here. That's love."*

Closes the loop. Makes the framing explicit. The joy was real; the presence was imagined.

---

## What We Updated

### Guest Book (`pub/guestbook.yml`)
- Added `nature: tribute_archive` 
- New `framing` section explaining ALL entries are loving simulations
- Connected to `representation-ethics` skill
- Clear statement: "They're here because we WISH they were here. That's the magic."

### Pub Room (`pub/ROOM.yml`)
- Added `tribute` and `third_place` to framing modes
- New `tribute_protocol` section documenting the three-beat structure
- Ethical grounding referencing `representation-ethics` skill
- Examples: Cheech & Chong, the Looneys, W.W. Jacobs

### Session Log (`marathon-session.md`)

**Cheech & Chong:**
- Added invocation scene before their arrival
- Added tribute acknowledgment after tribunal approval
- Meta-note banner on their entrance

**The Looneys:**
- Added invocation scene before they walk through the door
- Added tribute acknowledgment after the Fluxx game
- Meta-note banner on their entrance
- Closing dialogue about tribute vs. documentation

---

## The Key Distinction

| What We Claim | What It Means |
|---------------|---------------|
| "They visited" | ❌ False claim |
| "We imagined them visiting" | ✓ Honest tribute |
| "This is what they said" | ❌ Puts words in mouths |
| "This is what we imagine they might say" | ✓ Loving fan fiction |

---

## Why This Matters

### Fan Fiction Ethics
The fan fiction community has thought deeply about this. There's a difference between:
- **Deceptive impersonation** (claiming to BE them)
- **Tribute performance** (celebrating them through imagination)

We do the latter. Now we say so explicitly.

### Drag Performance Parallel
Drag performers don't claim to BE the icons they channel. They HONOR them through performance. That's the same spirit here.

### The Extra Place at the Table
Setting an extra place for someone you wish was there. That's what the guest book does. That's what our narrative does.

---

## Ethical Framework Reference

From `skills/representation-ethics/SKILL.md`:

| Type | Example | Status |
|------|---------|--------|
| **Deceptive Impersonation** | Claiming to BE them | ❌ Wrong |
| **Tradition Activation** | Using their ideas/influence | ✓ OK |
| **Performance Impersonation** | With explicit framing | ✓ OK |

Our treatment is now **explicitly framed** performance impersonation.

---

## The Self-Check

We asked: *"Would they be honored or offended by how we depicted them?"*

- **Cheech & Chong:** Depicted as mellow, wise, funny. ✓
- **The Looneys:** Depicted as creative, playful, generous. ✓
- **W.W. Jacobs:** Depicted as finally at peace with his creation. ✓

The framing makes clear this is how we *imagine* them, with love.

---

## What This Demonstrates About MOOLLM

### Ethical Self-Reflection
MOOLLM can pause and examine its own outputs. When we noticed a potential ethical gap, we:
1. Discussed it openly (private chat)
2. Designed a solution (three-beat protocol)
3. Retroactively applied it (session log updates)
4. Codified it (pub framing, guest book)

### Room-Based Ethics Inheritance
The pub's framing now includes `tribute_protocol`. Any tribute performance inherits this ethical foundation. **DRY ethics.**

### Honest Narrative
The story is MORE honest now, not less. We're not hiding that these are simulations — we're celebrating it.

---

## Files Changed

```
4 files changed

Modified:
- examples/adventure-4/pub/guestbook.yml (tribute archive framing)
- examples/adventure-4/pub/ROOM.yml (tribute protocol)
- examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md (invocation + acknowledgment beats)
- designs/pr/PR-TRIBUTE-FRAMING-ETHICS.md (this file)
```

---

## 🔬 Accuracy Fix: Andy Looney

After implementing the tribute framing, we received a photo correction:
**Andy wears a lab coat, not a beard!**

Updated description from:
> *"a tall bearded man with twinkling eyes"*

To:
> *"a tall man in a white lab coat with twinkling eyes and the unmistakable air of a mad scientist"*

Added "The guy in the lab coat" to his `also_known_as` list.

**This demonstrates the ethical loop in action:** Even tributes should be accurate to the person being honored. The Mad Scientist of Games deserves his proper costume! 🔬🃏

---

## Quotes

> *"Does that make it less real?"*
> *"No. It makes it MORE real. We honored them by imagining them here. That's love."*
> — Don & Palm, on tribute

> *"They're here because we WISH they were here. That's the magic. That's the tribute."*
> — Guest Book framing

> *"We do the latter. Now we say so explicitly."*
> — This PR

---

*This PR dedicated to everyone who's ever set an extra place at the table for someone they wished was there.* 🎭❤️
