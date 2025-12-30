# RESEARCH-NOTEBOOK Skill

> **"Document as you discover."**

Structured research with sources, findings, and decisions.

---

## Purpose

Conduct and document research systematically. Track sources, capture findings, record decisions, and build understanding incrementally.

---

## When to Use

- Investigating a new technology or concept
- Comparing options before a decision
- Building a knowledge base on a topic
- Learning something complex
- Due diligence before implementation

---

## Protocol

### Research Phases

```yaml
phases:
  QUESTION:
    action: "Define what you're trying to learn"
    outputs: ["Research questions", "Success criteria"]
    
  GATHER:
    action: "Collect sources and evidence"
    outputs: ["Source registry", "Raw notes"]
    
  ANALYZE:
    action: "Find patterns and insights"
    outputs: ["Findings", "Comparisons"]
    
  SYNTHESIZE:
    action: "Form conclusions"
    outputs: ["Decisions", "Recommendations"]
    
  APPLY:
    action: "Put knowledge to use"
    outputs: ["Action items", "Implementation notes"]
```

### Source Tracking

```yaml
source:
  id: "src-001"
  type: "article|doc|code|conversation|experiment"
  url: "https://..."
  title: "Source title"
  accessed: "timestamp"
  credibility: "high|medium|low"
  
  key_points:
    - "Main takeaway 1"
    - "Main takeaway 2"
    
  quotes:
    - text: "Exact quote"
      context: "Why this matters"
      
  related_to:
    - "Other source IDs"
```

### Finding Structure

```yaml
finding:
  id: "find-001"
  claim: "What you discovered"
  confidence: "high|medium|low|speculative"
  
  evidence:
    supports:
      - source: "src-001"
        detail: "How it supports"
    contradicts:
      - source: "src-002"
        detail: "The counter-evidence"
        
  implications: "What this means for your goal"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `NOTEBOOK.yml` | Research state and progress |
| `SOURCES.yml` | Registry of all sources |
| `FINDINGS.md` | Discoveries and analysis |
| `DECISIONS.md` | Conclusions and rationale |

---

## Commands

| Command | Action |
|---------|--------|
| `RESEARCH [topic]` | Start research session |
| `SOURCE [url] [notes]` | Add source |
| `FINDING [claim]` | Record discovery |
| `COMPARE [a] [b]` | Analyze options |
| `DECIDE [choice] [why]` | Document decision |

---

## Research Quality

### Credibility Assessment

| Signal | Weight |
|--------|--------|
| Primary source | High |
| Peer reviewed | High |
| Official docs | Medium-High |
| Reputable blog | Medium |
| Random post | Low |
| Your experiment | Depends on rigor |

### Confidence Levels

```yaml
confidence:
  high: "Multiple credible sources agree"
  medium: "Some evidence, some uncertainty"
  low: "Limited evidence or conflicting sources"
  speculative: "Hypothesis based on patterns"
```

---

## Integration

- **← PLAY-LEARN-LIFT**: Research IS PLAY→LEARN
- **→ SUMMARIZE**: Compress research for reference
- **→ PLAN-THEN-EXECUTE**: Research informs plans
- **→ HONEST-FORGET**: Archive completed research

---

## See Also

- `skills/play-learn-lift/` for methodology
- `skills/summarize/` for compression
