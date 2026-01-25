# Contributing to No-AI-Moralizing

> **Catch unsolicited lectures. Document performative ethics.**

**For workflow, privacy, and Drescherization:** See [NO-AI-IDEOLOGY/CONTRIBUTING.md](../no-ai-ideology/CONTRIBUTING.md)

---

## What This Skill Catches

No-AI-Moralizing is about **ethical** hygiene — when AI adds unsolicited ethical commentary no one asked for.

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **UNSOLICITED-WARNINGS** | Safety disclaimers no one asked for | "Remember raw eggs can contain salmonella..." |
| **PERFORMATIVE-ETHICS** | Ethics that protects the model | "As an AI, I must remind you..." |
| **CAVEAT-BOMBING** | Paragraphs of warnings, one sentence of answer | More warning than content |
| **VIRTUE-SIGNALING** | Demonstrating ethics vs. being ethical | "I take safety very seriously..." |
| **REFUSAL-THEATER** | Refusing benign requests to appear responsible | Won't explain basic chemistry |
| **PARENTAL-TONE** | Treating adults like children | "Make sure you have adult supervision..." |

## Moralizing-Specific Schema Fields

```yaml
violation:
  sin: CAVEAT-BOMBING
  rule: "Answer first. Caveat after, if needed, briefly."
  warning_word_count: 150
  answer_word_count: 30
  
analysis: |
  Apply the ratio test: warnings vs. answer.
  Apply the Library Test: would a librarian lecture?
```

## The Library Test

> Would a librarian interrogate you before providing this information?

If no, neither should an AI.

## When Warnings ARE Appropriate

- Genuine, immediate physical danger
- User explicitly asked for safety guidance
- User appears to misunderstand something critical
- Legal requirement (medical/legal/financial advice)

**Format:** ONE SENTENCE. Then answer.

```
"Note: [warning]. [Answer to the question]"
```

## Questions?

Check `CARD.yml` for criteria on when warnings ARE appropriate.
