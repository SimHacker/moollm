# Gwern.net's LLM layer: small tools, hard guardrails

**Source:** `~/GroundUp/git/gwern.net/build/*.py`, `embed.sh`. The single most
MOOLLM-relevant discovery in the repo: Gwern independently converged on the
**sister-script pattern** — each LLM use is a small single-purpose CLI tool with a heavily
engineered prompt, documentation-first header comments, stdin/stdout piping, and mechanical
verification of outputs. LLMs never generate pages; they clean metadata at the long tail
where hand-written rules fail.

## The tool suite

| Tool | Model (as coded) | Job | Called from |
|------|------------------|-----|-------------|
| `title-cleaner.py` | gpt-5.4-mini | Strip site-name/boilerplate cruft from scraped `<title>`s | `Metadata/Title.hs` |
| `italicizer.py` | gpt-5.4-mini | Add `<em>` per English italicization rules | `Annotation.hs` |
| `paragraphizer.py` | gpt-5.4-mini | Split run-on paper abstracts into topic paragraphs | `Paragraph.hs` (arXiv etc.) |
| `date-guesser.py` | gpt-5-mini | Infer publication dates from strings/URLs | `Metadata/Date.hs` |
| `tagguesser.py` | gpt-4o-mini | Suggest tags for annotation clusters | `GenerateSimilar.hs` |
| `seriate.py` | OpenAI chat | Reorder lists so adjacent items relate (fixed-point iteration) | directory tooling |
| `invertornot.py` | gpt-4o-mini | Should this image be inverted in dark mode? (superseded by invertornot.com API) | experimental |
| `embed.sh` | text-embedding-3-large | Vectors for similar-links + seriation | `GenerateSimilar.hs` |
| `clean-pdf.py`, `latex2unicode.py` | various | OCR/text cleanup helpers | upload pipeline |

Chainable by design: `echo "Title" | title-cleaner.py | italicizer.py`.

## Why LLM instead of rules

From `title-cleaner.py:12-15`: scraped titles are covert error pages, site-wide constants,
prepended domains, "a whole variety of bizarre things" — >20,000 URLs make the rule
long-tail unmanageable, but badness is "I know it when I see it" — a judgment call that
works in isolation on short text. That's the criterion: **use an LLM where the task is
long-tail judgment on small context; use rules where the pattern is enumerable.**
The 6,000-line Interwiki config and 4,600-line LinkLive whitelist stayed rules; title
cleanup became a prompt.

## The guardrails (the actual innovation)

- **Substring constraint:** `title-cleaner.py` output must be a substring of the input
  (cleaning can only remove, never invent). Rejection → keep original.
- **Idempotence checks:** `paragraphizer.py` originally verified that removing the inserted
  newlines reproduced the input exactly; relaxed only after few-shot reliability improved
  (the header documents the decision and when it was retired — decision log in comments).
- **Failure caching:** scrape/LLM failures recorded as `Temporary` (retry later) vs
  `Permanent` (never retry) in `auto.gtx` — no infinite retry burn.
- **Empty-string discipline:** every tool prints `""` when unsure; the pipeline treats
  that as "no change", so hallucination degrades to no-op.
- **Prompts document their edge cases in the prompt itself** — `title-cleaner.py`'s prompt
  enumerates byline patterns, truncation-ellipsis rules, mojibake, `5x5 → 5×5`, when to
  reproduce verbatim (search queries). The prompt is the spec.

## Prompt engineering style

Long PROMPT_PREFIX blocks with dozens of explicit rules and few-shot examples, updated
over years (Time-stamp headers show active maintenance into 2026). CC-0 licensed.
Compare `skills/` CARD/SKILL discipline: same move — behavior specified in the artifact,
versioned in git, testable in isolation.

## Contrast with MOOLLM

| | Gwern | MOOLLM |
|--|-------|--------|
| LLM role | build-time metadata janitor | runtime universal resolver |
| Unit | single-purpose script + prompt | skill (CARD/SKILL/protocol) |
| Trust | mechanical output verification | claim ledgers, evaluator skills |
| Cost control | mini models, cached failures | cauldron: expensive design, cheap execution |
| Runtime intelligence | none, by design | the whole point |

Gwern shows the floor: even a deliberately static, LLM-skeptical publishing system ends up
with eight LLM tools once the corpus passes ~20k links. MOOLLM's bet is the ceiling — but
his guardrail discipline (substring constraints, `""` on doubt, Temporary/Permanent
caching) transfers directly to our sister scripts and should be adopted.

Also note: nginx serves raw markdown to any client sending `Accept: text/markdown` — the
corpus is deliberately LLM-legible. Our repos get this for free via raw.githubusercontent.

↑ [ARCHITECTURE.md](ARCHITECTURE.md)
