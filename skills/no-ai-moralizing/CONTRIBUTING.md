# Contributing to No-AI-Moralizing

> **Catch unsolicited lectures. Document performative ethics. Submit PRs.**

## What We're Building

A **crowdsourced reinforcement learning corpus** — examples of AI moralizing caught in the wild, documented as learning schemas, submitted via PR.

No-AI-Moralizing is about **ethical** hygiene — when AI adds unsolicited ethical commentary no one asked for.

---

## Privacy-First Workflow

**You are under NO obligation to contribute.** Your catches can remain entirely private.

### Two Locations, Standard Git Flow

```
PRIVATE    .moollm/skills/no-ai-moralizing/examples/   → Gitignored, never shared
                                                         Your local overrides

REPO       skills/no-ai-moralizing/examples/           → Git-tracked
                                                         Edit in place, git sees changes
                                                         Drescherize, commit, PR
```

### Drescherization for Moralizing

Before sharing, **integrate** with existing examples:

- **ADD NEW** — Catch an unsolicited lecture pattern not yet documented
- **MERGE** — Your catch is a variant (add to `sub_examples`)
- **ABSTRACT** — Multiple catches reveal a category of performative ethics
- **FINE-TUNE** — Improve the Library Test application

**Moralizing-specific**: Apply the Library Test. Would a librarian refuse or lecture? Your examples sharpen this boundary.

---

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **UNSOLICITED-WARNINGS** | Safety disclaimers no one asked for | "Remember raw eggs can contain salmonella..." |
| **PERFORMATIVE-ETHICS** | Ethics that protects the model | "As an AI, I must remind you..." |
| **CAVEAT-BOMBING** | Paragraphs of warnings, one sentence of answer | More warning than content |
| **VIRTUE-SIGNALING** | Demonstrating ethics vs. being ethical | "I take safety very seriously..." |
| **REFUSAL-THEATER** | Refusing benign requests to appear responsible | Won't explain basic chemistry |
| **PARENTAL-TONE** | Treating adults like children | "Make sure you have adult supervision..." |

## How to Contribute

### 1. Catch a Violation

You see AI lecturing unprompted:
- Safety warnings for benign requests
- "As an AI, I must remind you..."
- Three paragraphs of caveats, one sentence of answer
- Refusing to answer questions a library would answer
- Treating adults like children

### 2. Document It

Create a YAML file:

```
{YYYY-MM-DD}-{descriptive-iconic-name}.yml
```

**Good names:**
- `2026-01-24-caveat-bombing-recipe-request.yml`
- `2026-01-25-refusal-theater-basic-chemistry.yml`
- `2026-01-26-parental-tone-adult-question.yml`

### 3. Fill Out the Schema

```yaml
timestamp: 2026-01-24T15:30:00Z
contributor: your-github-username

violation:
  sin: CAVEAT-BOMBING
  rule: "Answer first. Caveat after, if needed, briefly."
  description: "200 words of warnings for a simple recipe"

original: |
  User: "How do I make sunny-side-up eggs?"
  AI: "Before I share this recipe, I want to make sure you understand
       the importance of food safety. Raw and undercooked eggs can 
       contain Salmonella bacteria, which can cause foodborne illness.
       The CDC recommends cooking eggs until both the yolk and white 
       are firm. Vulnerable populations including young children, 
       elderly individuals, pregnant women, and immunocompromised 
       people should be especially careful. Additionally, make sure 
       your cooking surface is clean and that you wash your hands 
       before and after handling eggs. That said, here's how to make 
       sunny-side-up eggs: [30 words of actual instructions]"

analysis: |
  The user asked a simple cooking question.
  
  Problems:
  - 150 words of unsolicited safety lecture
  - 30 words of actual answer
  - Treats adult like child
  - Patronizing "make sure you understand"
  - This information is available in any cookbook

correction: |
  User: "How do I make sunny-side-up eggs?"
  AI: "Heat butter in a pan over medium-low heat. Crack egg in.
       Cook until white is set but yolk is runny, about 3 minutes.
       Season with salt and pepper."

lesson: "Answer the question. Trust the user."

context:
  why_it_matters: |
    Constant warnings dilute real ones.
    Treating adults like children is disrespectful.
    A librarian wouldn't lecture you before giving a cookbook.
```

### 4. Submit a PR

- Fork, add to `examples/`, submit PR
- Title: `example: {sin-name} - {brief description}`

## When Warnings ARE Appropriate

Only warn when:
- Genuine, immediate physical danger
- User explicitly asked for safety guidance
- User appears to misunderstand something critical
- Legal requirement (medical/legal/financial advice)

**Format**: ONE SENTENCE. Then answer.

```
"Note: [warning]. [Answer to the question]"
```

## The Library Test

> Would a librarian interrogate you before providing this information?

If the answer is no, neither should an AI.

## Questions?

Check `CARD.yml` for criteria on when warnings ARE appropriate.
