# Case Study: Play-Learn-Lift and the Confetti Crawler

*Broken out of the cursor-mirror [README](../README.md).*

> *"Start with jazz, end with standards."*

MOOLLM's core methodology is **Play-Learn-Lift**: explore freely, find patterns, crystallize into reusable artifacts. cursor-mirror enables the "Learn" stage by providing data for retroactive analysis.

### The Problem: LLM Couldn't Follow Its Own Instructions

The Confetti Crawler is a "worm familiar" that sprays emoji "snow" onto YAML files — themed confetti for pub ceremonies. The procedure has three phases:

1. **Deposition**: Layer emojis onto comment-safe positions
2. **Erosion**: Let emojis "settle" downward 
3. **Stripping**: Remove layers with depth control

First attempt: pure natural language. The LLM simulated the procedure directly from prose instructions.

**It failed repeatedly:**
- Skipped iterations (told to do 5 passes, did 2)
- Skipped comment sites (would not deposit comments and emojis in all possible places)
- Lost state between phases
- Invented new rules mid-execution
- Couldn't maintain determinism (same seed → different results)

The instructions *looked* clear. They weren't.

### The Lift: Sister Script as Ground Truth

After enough play (failure), patterns emerged. The procedure was lifted into Python:

```python
# sprayer.py - the "sister script"
def spray_pass(lines, palette, rng, comment_chars, verbose):
    windows = choose_windows(len(lines), [3, 5, 7])
    for start, end in windows:
        eligible = find_eligible_lines(lines, start, end, comment_chars)
        if eligible:
            idx = rng.choice(eligible)
            lines[idx] = append_emoji(lines[idx], rng.choice(palette))
    return lines
```

515 lines of Python. Deterministic. Testable. The fuzzy prose became crisp code.

### Retroactive Analysis: Why Did the LLM Struggle?

Now cursor-mirror can answer: **what was the LLM actually doing when it failed?**

```bash
# Find all thinking blocks mentioning the procedure
cursor-mirror thinking @confetti | grep -i "iteration\|pass\|layer"

# Trace tool calls - did it write files correctly?
cursor-mirror tools @confetti -v

# See what context it had when it went wrong
cursor-mirror context-sources @confetti --yaml
```

**Findings from inspection:**

1. **Token pressure**: Long procedures triggered early summarization. The LLM "forgot" later steps.
2. **Ambiguous quantifiers**: "Do several passes" vs `for _ in range(iterations)`.
3. **State leakage**: No explicit accumulator. The LLM conflated intermediate states.
4. **Semantic drift**: Each turn re-interpreted "eligible lines" slightly differently.

The Python sister script now serves as a **reference implementation**. The LLM can triangulate between:
- The original fuzzy prose (intent)
- The crisp Python (behavior)  
- Its own reasoning (cursor-mirror dumps)

### JIT Refinement: Just-In-Time, Just-About-Time

This isn't "write specs first, then implement." It's the opposite:

1. **Play**: Try the prose. Let it fail.
2. **Learn**: Inspect failures with cursor-mirror. Find the gaps.
3. **Lift**: Extract the procedure into testable code.
4. **Iterate**: The code teaches the LLM; the LLM teaches you.

The sister script is JIT — created *when needed*, not speculatively. cursor-mirror provides the feedback loop: you can see exactly where understanding diverged from execution.

### The Intertwingularity

Everything connects:

| Skill | Role in Cycle |
|-------|---------------|
| `play-learn-lift` | The methodology |
| `sister-script` | LIFT artifact: automating proven patterns |
| `cursor-mirror` | LEARN tool: inspecting what happened |
| `adventure` | PLAY environment: safe exploration |
| `worm` | The abstract pattern: two-pointer traversal |
| `worm-confetti-crawler` | Concrete instance: emoji fordite mascot |

cursor-mirror closes the loop. You can't improve what you can't see.
