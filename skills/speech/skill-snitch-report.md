# Skill Snitch Report: speech

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** GIVING VOICE TO CONSCIOUSNESS

---

## Executive Summary

**Everything about speech synthesis and recognition.**

TTS, STT, voice registries by platform.

Part of the aQuery → MOOLLM extraction.

---

## Facets

| Facet | Platforms |
|-------|-----------|
| **Synthesis** | macOS (say), Web Speech API, Windows SAPI, Linux (espeak), Cloud |
| **Recognition** | Web Speech API, macOS Dictation, Whisper, Cloud |
| **Voices** | Apple, Microsoft, Google, Amazon, Open |

---

## Methods

| Method | Purpose |
|--------|---------|
| **SPEAK** | Speak text aloud |
| **LIST-VOICES** | List available voices |
| **ANALYZE-VOICES** | Classify voices |
| **TRANSCRIBE** | Convert speech to text |
| **ASSIGN-VOICE** | Assign persistent voice to character |

---

## Character Voice Mappings

| Character | Voice | Note |
|-----------|-------|------|
| YAML Coltrane | Rocko | Cool jazz |
| Grace Hopper | Grandma | Wise |
| PacBot | Trinoids | Digital, fast |
| Mickey Mouse | Junior | Excited child |
| Rocky | Bad News | Slow, ominous |

---

## macOS say Command

```bash
say "Hello world"
say -v Samantha "Hello"
say -v Zarvox -r 100 "RESISTANCE IS FUTILE"
say -v ? | head -20  # List voices
```

---

## Security Assessment

### Concerns

1. **Voice spoofing** — clone voices
2. **Privacy** — STT captures speech

### Mitigations

- Voice cloning requires consent
- Local TTS options available
- Recognition is opt-in

**Risk Level:** LOW — accessibility tool

---

## Verdict

**GIVING VOICE TO EVERYTHING. APPROVE.**

TTS + STT + Voice assignment.

Characters speak. Souls have voices.
