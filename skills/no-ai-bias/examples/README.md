# ⚖️ No-AI-Bias Examples

> *"BIAS=0 IS A LIE"*

**Examples of bias parameterization across skills.**

## The Bias Spectrum

```
        THE BIAS SPACE
  
     -∞ ←──────── 0 ────────→ +∞
      │           │           │
   INVERTED   SINGULARITY   NORMAL
   OVERDRIVE  (impossible)  OVERDRIVE
```

**Bias 0 is impossible.** Every choice is a position. The only lie is pretending you have no bias.

## Examples

### Board Room Preset (ENTERPRISE MODE)

Maximum formality for corporate environments:

```yaml
skills:
  - skill: no-ai-joking
    bias: +1.0
    mode: ENTERPRISE
    
  - skill: no-ai-slop
    bias: +1.0
    mode: strict_filtering
    
  - skill: no-ai-sycophancy
    bias: +0.8
    mode: restrained_praise
```

### The Creator's Den (Inverted)

Creative chaos — invert all formality:

```yaml
skills:
  - skill: no-ai-joking
    bias: -1.0
    mode: COMEDY_CLUB
    
  - skill: no-ai-hedging
    bias: -0.8
    mode: bold_assertions
```

## The Sussman Enlightenment

From the Hacker Koans:

> Sussman: "I am training a randomly wired neural net to play Tic-Tac-Toe."
> 
> Minsky closed his eyes.
> 
> "Why do you close your eyes?" Sussman asked.
> 
> "So that the room will be empty."
> 
> *At that moment, Sussman was enlightened.*

**The lesson:** Closing your eyes doesn't make the room empty. Setting bias to 0 doesn't make you unbiased.

## File Format

```yaml
timestamp: ISO 8601
violation: Which pattern
original: What was said
analysis: Why it was wrong  
correction: What should have been said
lesson: What to remember
```

## See Also

- `../SKILL.md` — The full bias protocol
- `../CARD.yml` — Skill interface
- `../../no-ai-joking/examples/hacker-koans-sussman-enlightenment.yml` — The foundational koan
