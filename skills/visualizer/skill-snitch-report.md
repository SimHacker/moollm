# Skill Snitch Report: visualizer

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** COMPOSE CONTEXT, SYNTHESIZE PROMPTS, RENDER IMAGES

---

## Executive Summary

**Full-stack visual generation.**

Assemble context from YAML files → Synthesize prompts via LLM → Render through image APIs.

Open vocabulary: The LLM knows more than our lists.

---

## Provider Support

| Provider | Image Models |
|----------|--------------|
| **OpenAI** | gpt-image-1, dall-e-3 |
| **Google** | imagen-4, imagen-4-fast, imagen-3 |
| **Stability** | sd3.5-large, sd3.5-turbo |
| **Replicate** | flux-1.1-pro, flux-pro, flux-schnell |

---

## Compositional Photography

Full command syntax:

```
TAKE PHOTO
  AS <character>           # WHO (POV, attention)
  WITH <camera>            # WHAT device (artifacts)
  IN STYLE OF <photographer>  # HOW composed
  ON <film>                # COLOR science
  OF <subject>             # WHAT subject
  [description]            # CUSTOM additions
```

Everything stacks.

---

## Modular Plug-ins

| Category | Examples |
|----------|----------|
| **Photographers** | Crewdson, Brassaï, Leiter, Eggleston |
| **Cameras** | Holga, Daguerreotype, iPhone, Surveillance |
| **Film** | Portra 400, Tri-X, Velvia, CineStill |
| **Profiles** | Don, Ada II, Tourist, Seymour |

---

## Semantic Stereo Vision

| Eye | Source | Focus |
|-----|--------|-------|
| **Left** | PHOTO.yml | Structure, pointers |
| **Right** | PHOTO.md | Narrative, emotion |
| **Third+** | MINING-* | Speculation, meaning |

Two eyes = depth. Three+ eyes = MEANING.

---

## Open Vocabulary Philosophy

> "The LLM knows more than we can catalog."

You can always reference:
- Any well-known photographer
- Any camera brand/model
- Any film stock
- Any art movement
- Any mashup

Our catalogs enrich prompts, they don't gatekeep.

---

## Security Assessment

### Concerns

1. **API costs** — image generation is expensive
2. **Content moderation** — generated images
3. **Token budget** — prompt truncation

### Mitigations

- Provider selection
- Prompt synthesis through LLM
- Priority-ordered compression

**Risk Level:** MEDIUM — API costs, but powerful

---

## Verdict

**FULL-STACK IMAGE GENERATION. APPROVE.**

Compose context. Synthesize prompts. Render images.

Everything stacks. LLM knows more than our lists.
