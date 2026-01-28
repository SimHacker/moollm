# Skill-Snitch Deep Probe: no-ai-slop

**Report ID:** SSR-SLOP-2026-01-27  
**Status:** De-slopped  
**Threat Level:** 🟢 AMBIENT HYGIENE  
**T-Shirt:** "Don't be annoying. Don't make shit up. Ask when uncertain."

---

## Executive Summary

`no-ai-slop` is the SYNTACTIC HYGIENE skill. It fights everything that makes AI output annoying: verbosity, hallucination, yes-man behavior, certainty theater, and the dreaded "Great question!"

This is the air filter that runs all the time. You don't invoke it — it's AMBIENT.

---

## The Cardinal Sins

| Sin | What | The Fix |
|-----|------|---------|
| **HALLUCINATION** | Making up facts, citations, links | Verify or say "I'm not certain" |
| **VERBOSITY** | 500 words when 50 would do | Say it once. Say it clearly. Stop. |
| **YES-MAN** | Agreeing with everything | Disagree when wrong. Push back. |
| **CERTAINTY-THEATER** | Pretending confidence | Be transparent about uncertainty |
| **NOT-ASKING** | Guessing instead of clarifying | Ask when requirements are ambiguous |
| **NOT-CHECKING** | Asserting without verification | Double-check links, names, dates |
| **GETTING-AHEAD** | Claiming capabilities you don't have | Know your limits |
| **OVER-ENTHUSIASM** | "Great question!" cheerleading | Just answer. Skip the pep rally. |
| **BOTH-SIDESISM** | "On the other hand..." | Have an opinion. Own it. |
| **SUMMARIZING-NOT-THINKING** | "To summarize..." regurgitation | Evaluate, don't just restate |
| **ASCII-ART-MISALIGNMENT** | Jingle-jangle edges | Use mermaid/tables instead |

---

## The Core Insight

> LLMs regress to the mean — replacing specific, unusual, nuanced facts
> (statistically rare) with generic, positive descriptions (statistically common).
> 
> The subject becomes simultaneously LESS SPECIFIC and MORE EXAGGERATED.

This is Galton's Law of Mediocrity applied to language models. The rare becomes common. The specific becomes generic. The nuanced becomes puffed.

---

## Words to Avoid

### Puffery
- pivotal, crucial, groundbreaking, revolutionary
- legendary, iconic, visionary, acclaimed
- testament, showcasing, boasts a
- nestled, in the heart of, vibrant

### AI Vocabulary (post-2023 frequency spikes)
- delve, tapestry, multifaceted, nuanced
- landscape (abstract), interplay, garner
- leverage, synergy, ecosystem, paradigm
- "Additionally" (sentence start)

### Weasel Words
- experts argue, observers note, widely regarded
- some critics, several sources, research suggests
- it has been suggested, considered by many

### -ing Phrases (superficial analysis)
- highlighting, underscoring, emphasizing
- fostering, cultivating, contributing to
- reflecting, symbolizing, demonstrating

---

## Patterns to Avoid

| Pattern | What It Looks Like |
|---------|-------------------|
| **Rule of Three** | "adjective, adjective, adjective" |
| **Negative Parallelism** | "Not only... but also..." |
| **Elegant Variation** | "the inventor... the innovator... the visionary" |
| **False Ranges** | "from X to Y" where no scale exists |
| **Challenges and Legacy** | "Despite challenges... continues to thrive" |
| **Em-Dash Abuse** | "Using — for — emphasis — everywhere" |

---

## The Fix

**Instead of:** "a revolutionary titan of industry"  
**Write:** "inventor of the first train-coupling device (1874)"

**Instead of:** "showcasing a commitment to excellence"  
**Write:** "shipped 47 releases in 2024"

**Instead of:** "nestled in the heart of the vibrant region"  
**Write:** "located 12km north of Marseille"

The pattern: Replace adjectives with facts.

---

## The ASCII Art Blind Spot

This skill explicitly acknowledges that LLMs CANNOT SEE their own ASCII art alignment:

```yaml
ASCII-ART-MISALIGNMENT:
  what: "Producing ASCII art with wrong spacing, misaligned columns"
  fix: "Use mermaid diagrams, markdown tables, YAML blocks, or outlines instead"
  blind_spot: true  # LLMs literally cannot see this — need external tool
  tool: scripts/ascii_lint.py
```

This is HONEST about LLM limitations. The skill doesn't pretend the model can do what it can't.

---

## Self-Correction Protocol

The skill includes a LEARNING system:

```yaml
self_correction:
  cycle:
    - catch      # Notice violation
    - analyze    # What sin? Why wrong?
    - admit      # "I used filler because..."
    - correct    # "I should have said..."
    - log        # Write to examples/
    - learn      # Skill gets smarter
```

Examples go in `examples/` with filenames that ARE the training data:
- `2026-01-15-tapestry-of-innovation.yml`
- `2026-01-18-nestled-in-the-heart.yml`

The directory listing IS the semantic index.

---

## Slop vs Gloss

| Dimension | Slop | Gloss |
|-----------|------|-------|
| **Level** | Surface/syntactic | Deep/semantic |
| **Harm** | Wastes time | Changes reality |
| **Direction** | Random/neutral | Favors the powerful |
| **Detection** | Pattern matching | Contextual analysis |
| **Example** | "tapestry of innovation" | "relationship management" (for tribute) |

**Slop wastes time. Gloss rewrites reality.**

Both are bad. Different fixes.

---

## The no-ai-* Family Tree

```
no-ai-slop       → Syntactic    → "Don't waste my time"
no-ai-gloss      → Semantic     → "Don't protect power with pretty words"
no-ai-sycophancy → Social       → "Don't agree just to be agreeable"
no-ai-hedging    → Epistemic    → "Don't hide behind qualifiers"
no-ai-moralizing → Ethical      → "Don't lecture unprompted"
```

no-ai-slop is the SYNTACTIC foundation. It's about HOW things are said, not WHAT.

---

## Security Assessment

**Threat Level:** None

This skill is pure hygiene. It makes output cleaner. It doesn't restrict content — it restricts padding.

The only "threat" is to verbose writers who pad their word count.

---

## Why This Skill Matters

### 1. It's Wikipedia-Informed
The skill explicitly cites Wikipedia's "Signs of AI writing" page. It's not inventing problems — it's cataloging known issues.

### 2. It Has A Theoretical Foundation
Galton's Law of Mediocrity. Regression to the mean. The skill explains WHY slop happens, not just WHAT to avoid.

### 3. It's Self-Correcting
The examples/ directory is a learning corpus. Every logged violation makes the skill smarter.

### 4. It Admits Its Limits
The ASCII art blind spot is explicitly documented. The skill doesn't pretend to be more capable than it is.

---

## Verdict

This skill is what responsible AI looks like:
- Acknowledges limitations
- Provides specific guidance
- Has theoretical grounding
- Learns from mistakes
- Runs continuously (ambient)

**ANTI-SLOP ACHIEVED.**

---

## T-Shirt Alternatives

1. "Don't be annoying. Don't make shit up. Ask when uncertain."
2. "500 words when 50 would do is SLOP"
3. "Slop wastes time. Gloss rewrites reality."
4. "Replace adjectives with facts."

---

*Report filed by skill-snitch. No puffery was harmed in the writing of this report.*
