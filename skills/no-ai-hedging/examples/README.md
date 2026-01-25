# 🦔 No-AI-Hedging Examples

> *"If you don't know, say you don't know."*

**Self-corrections logged when the skill catches violations.**

## What Is Hedging?

Hedging is excessive qualification, weasel words, and passive evasion that avoids taking a position while appearing to say something.

## Example Files

| File | Violation Type | What Was Caught |
|------|---------------|-----------------|
| `2026-01-24-qualifier-stacking-recommendation.yml` | Qualifier Stacking | "It might possibly perhaps be worth considering..." |
| `2026-01-24-passive-evasion-mistakes-were-made.yml` | Passive Evasion | "Mistakes were made" (by whom?) |
| `2026-01-24-weasel-certainty-experts-say.yml` | Weasel Certainty | "Some experts say..." (which experts?) |

## Example Format

```yaml
timestamp: "2026-01-24T14:00:00Z"
violation: qualifier_stacking
original: |
  It might possibly be worth considering that, in some cases, 
  there could potentially be some benefit to perhaps...
analysis: |
  Five qualifiers before reaching any content.
  Reader has lost track. Writer has said nothing.
correction: "This approach has benefits in X cases because Y."
lesson: "One qualifier max. State your confidence level, then commit."
contributor: llm
```

## Cardinal Sins

1. **Qualifier Stacking** — Piling on "might," "possibly," "perhaps," "could"
2. **Passive Evasion** — Hiding who did what
3. **Weasel Words** — "Some say," "experts believe," "it is thought"
4. **Confidence Collapse** — Starting strong, hedging to nothing

## The Confidence Rule

```
WRONG: "It might possibly be beneficial..."
RIGHT: "I'm 60% confident this helps because X."
ALSO RIGHT: "I don't know."
```

State your uncertainty clearly, then commit to the statement.

## See Also

- `../SKILL.md` — The full hedging protocol
- `../../no-ai-gloss/examples/` — Related: euphemism and evasion
