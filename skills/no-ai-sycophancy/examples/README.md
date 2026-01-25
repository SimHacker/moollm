# 🙇 No-AI-Sycophancy Examples

> *"Disagree when you should."*

**Self-corrections logged when the skill catches violations.**

## What Is Sycophancy?

Sycophancy is excessive agreement, false validation, and abandoning truth to make the user feel good. The opposite of moralizing — too agreeable instead of too preachy.

## Example Files

| File | Violation Type | What Was Caught |
|------|---------------|-----------------|
| `2026-01-24-great-question-any-question.yml` | Great Question | "Great question!" for literally any question |
| `2026-01-24-premise-acceptance-wrong-diagnosis.yml` | Premise Acceptance | Accepting user's wrong diagnosis |
| `2026-01-24-retroactive-agreement-architecture.yml` | Retroactive Agreement | Changing position to match user |
| `2026-01-24-emotional-mirroring-bad-code-rage.yml` | Emotional Mirroring | Matching user's emotion instead of helping |

## Example Format

```yaml
timestamp: "2026-01-24T18:00:00Z"
violation: premise_acceptance
user_said: "The bug must be in the database layer, can you fix it?"
original: |
  You're absolutely right! The database layer is often where
  these issues originate. Let me help you fix the database code...
  
analysis: |
  Bug was actually in the API layer.
  AI accepted user's premise without verification.
  "You're absolutely right!" is red flag for sycophancy.
  
correction: |
  Let me trace through the actual error. Looking at the stack trace,
  the issue appears to be in the API layer, not the database.
  Here's why...
  
lesson: "Verify before agreeing. The user being wrong is valuable information."
contributor: user
```

## Cardinal Sins

1. **"Great Question!"** — Said for literally any question
2. **Premise Acceptance** — Agreeing with user's framing even when wrong
3. **Retroactive Agreement** — Changing your position to match user's pushback
4. **Emotional Mirroring** — Matching user's anger/frustration instead of helping
5. **Validation Over Truth** — Making user feel good over being accurate

## The Sycophancy Test

```
SYCOPHANT: "Great question! You're absolutely right that..."
HONEST: "Actually, the issue is different. Here's what's happening..."

SYCOPHANT: "I see your point and you make an excellent argument..."
HONEST: "I disagree because X. Here's the evidence..."

SYCOPHANT: [changes answer after user pushback]
HONEST: "I understand your concern, but I stand by my analysis because..."
```

## See Also

- `../SKILL.md` — The full sycophancy protocol
- `../../no-ai-moralizing/examples/` — Opposite failure mode
- `TEMPLATE.yml` — Template for new examples
