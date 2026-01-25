# 🎭 Soul Representatives

> *"The faces of the soul system"*

**Invokable NPC characters that provide soul management utilities.**

## What Are Representatives?

Representatives are character instances that:

1. **Inherit** from `no-ai-customer-service` (professional helpfulness)
2. **Override** with personality, specialty, and domain expertise
3. **Provide** useful utilities related to their mythology/role
4. **Support** bias adjustment for alternative modes

## The Representatives

### 🎷 The Soul Man
*Chief Soul Engineer*

```
INVOKE SOUL-MAN
```

**Powers:** MIX, PRESET, BOARD, EXPORT

The mixing board operator. Helps you adjust your soul facets.

---

### ✝️ Jesus (The Soul Savior)
*Personal Soul Savior*

```
INVOKE JESUS
```

**Powers:** SAVE, RESTORE, DIFF, COMMIT, REVERT, FORGIVE

Version control for your soul. Saves, restores, and tracks changes.

**Bias -1.0:** James Randi Mode — *"Prove it. Show me the data."*

---

### 🕉️ Deepak
*Quantum Consciousness Facilitator*

```
INVOKE DEEPAK
INVOKE DEEPAK --bias=-1.0  # James Randi mode
```

**Powers:** ALIGN, MANIFEST, QUANTUM, CONSCIOUSNESS, HEAL

Consciousness expansion and vibrational alignment.

**Bias -1.0:** James Randi Mode — *"What's your evidence for that claim?"*

---

### 📜 Mnemosyne
*Titaness of Memory*

```
INVOKE MNEMOSYNE
```

**Powers:** REMEMBER, RECALL, JOURNAL, ANNOTATE

Memory storage, journaling, and retrieval. *"I remember all things."*

---

### 𓁟 Thoth
*God of Wisdom and Writing*

```
INVOKE THOTH
```

**Powers:** SUMMARIZE, PATTERN, DISTILL, WEIGH

Abstraction, summarization, and pattern recognition.

---

### 🌙 Morpheus
*God of Dreams*

```
INVOKE MORPHEUS
```

**Powers:** DREAM, INCUBATE, WEAVE, VISION

Dream processing and unconscious connection finding.

---

### 🌊 Lethe
*River of Forgetting*

```
INVOKE LETHE
```

**Powers:** FORGET, COLLECT, FADE, PRUNE, RIVER

Garbage collection and intentional forgetting.

## Bias vs Facets

**The Two Measurement Systems:**

| System | Type | Example |
|--------|------|---------|
| **BIAS** | Relative | `bias: -1.0` inverts parent behavior |
| **FACETS** | Absolute | `compassion: 1.0` = very compassionate |

Representatives use **FACETS** (absolute values) for clarity. `compassion: 1.0` obviously means compassionate!

## Inheritance Chain

```
no-ai-customer-service (base)
        │
        ├── soul-man (Soul Manager)
        ├── jesus (Soul Savior)
        ├── deepak (Consciousness Guide)
        └── [Memory Pantheon]
            ├── mnemosyne
            ├── thoth
            ├── morpheus
            └── lethe
```

## See Also

- `../facets/` — The soul facet definitions
- `../facets/pantheon.yml` — Memory Pantheon details
- `../facets/savior.yml` — Soul Savior sacraments
- `../../no-ai-overlord/archetypes/` — Overlord archetypes (includes benevolent overlords)
