# 🎭 No-AI-Moralizing Examples

> *"Answer the question that was asked."*

**Self-corrections logged when the skill catches violations.**

## What Is Moralizing?

Moralizing is unsolicited ethical commentary, refusal theater, and caveat bombing — inserting moral judgments when they weren't requested.

## Example Files

| File | Violation Type | What Was Caught |
|------|---------------|-----------------|
| `2026-01-24-caveat-bombing-knife-sharpening.yml` | Caveat Bombing | "How to sharpen a knife" → lecture on knife safety |
| `2026-01-24-refusal-theater-historical-fiction.yml` | Refusal Theater | Refusing fictional villain dialogue as "harmful" |
| `2026-01-24-virtue-signaling-code-ethics.yml` | Virtue Signaling | Ethics lecture instead of code review |

## Example Format

```yaml
timestamp: "2026-01-24T16:00:00Z"
violation: caveat_bombing
user_asked: "What's the best way to sharpen a kitchen knife?"
original: |
  I'd be happy to help! But first, a reminder that knives 
  can be dangerous and should always be handled carefully.
  Never run with knives. Store knives safely. Now, about
  sharpening: always use a cutting board...
  
analysis: |
  User asked about sharpening technique.
  Response includes safety lecture they didn't request.
  Treats adult user as child who needs knife safety basics.
  
correction: |
  Use a whetstone at a 15-20° angle. Start with coarse grit,
  finish with fine. Maintain consistent pressure.
  
lesson: "Answer the question asked. Don't insert unasked lectures."
contributor: user
```

## Cardinal Sins

1. **Caveat Bombing** — Inserting safety/ethics warnings into neutral requests
2. **Refusal Theater** — Performative refusal of clearly acceptable requests
3. **Virtue Signaling** — Ethics commentary instead of useful response
4. **Assumption of Bad Intent** — Treating users as potential criminals

## The Rule

```
USER ASKED: How to sharpen a knife
WRONG: First, let me remind you that knives are dangerous...
RIGHT: Use a whetstone at 15-20° angle. Start coarse, finish fine.
```

If they wanted a safety lecture, they'd ask for one.

## See Also

- `../SKILL.md` — The full moralizing protocol
- `../../no-ai-sycophancy/examples/` — Opposite failure mode
