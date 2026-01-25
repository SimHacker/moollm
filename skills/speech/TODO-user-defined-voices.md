# 🎤 TODO: User-Defined Voices

> Status: **Research in Progress**

---

## The Goal

Create and use **your own voice** (or any voice) for text-to-speech.

---

## Approaches

### 1. macOS Personal Voice (Native)

**Requirements:**
- Apple Silicon (M1/M2/M3)
- macOS Sonoma 14.0+
- 15+ minutes of voice recording

**Steps:**
1. System Settings → Accessibility → Personal Voice
2. Create Personal Voice
3. Record ~150 phrases (takes 15-20 minutes)
4. Wait for processing (15-60 minutes)
5. Enable in Spoken Content settings

**Known Limitations:**
- ⚠️ Does NOT appear in `say -v ?` output
- ⚠️ Cannot use `-o` flag to save audio files
- ⚠️ Exact name required (case-sensitive)
- ⚠️ Privacy restrictions on programmatic access

**Testing:**
```bash
# Must know exact name from System Settings
say -v "Your Personal Voice Name" "Test message"
```

**Workaround for file output:**
- [SavePersonalVoiceAudio](https://github.com/limneos/SavePersonalVoiceAudio)
- Record system audio while speaking

### 2. Coqui TTS (Open Source)

**Link:** https://github.com/coqui-ai/TTS

**Pros:**
- Fully open source
- Run locally
- Voice cloning with few samples
- Multiple models (Tacotron, VITS, etc.)

**Quick Start:**
```bash
pip install TTS

# List available models
tts --list_models

# Clone a voice (need reference audio)
tts --text "Hello!" \
    --model_name tts_models/en/vctk/vits \
    --speaker_wav reference.wav \
    --out_path output.wav
```

**XTTS (Multilingual Cloning):**
```bash
# XTTS v2 - high quality voice cloning
tts --text "Hello world" \
    --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
    --speaker_wav my_voice.wav \
    --language_idx en
```

### 3. ElevenLabs (Cloud API)

**Link:** https://elevenlabs.io

**Pros:**
- Highest quality
- Instant voice cloning
- Easy API

**Cons:**
- Paid service
- Cloud-dependent
- Privacy concerns

**API Example:**
```python
import requests

response = requests.post(
    "https://api.elevenlabs.io/v1/text-to-speech/your-voice-id",
    headers={"xi-api-key": "YOUR_API_KEY"},
    json={
        "text": "Hello world",
        "model_id": "eleven_monolingual_v1"
    }
)
with open("output.mp3", "wb") as f:
    f.write(response.content)
```

### 4. Tortoise TTS (High Quality, Slow)

**Link:** https://github.com/neonbjb/tortoise-tts

**Pros:**
- Extremely high quality
- Good voice cloning
- Multiple voice samples improve quality

**Cons:**
- VERY slow (minutes per sentence)
- Requires GPU

### 5. Bark (Suno AI)

**Link:** https://github.com/suno-ai/bark

**Pros:**
- Generates speech AND music
- Emotional control
- Open source

**Cons:**
- Less control over voice
- Can be unpredictable

---

## Research Questions

1. **Can Personal Voice be accessed programmatically?**
   - AVSpeechSynthesizer?
   - Private API?
   - Shortcuts automation?

2. **What's the minimum audio for good voice cloning?**
   - ElevenLabs: ~1 minute
   - Coqui XTTS: ~6 seconds (but more is better)
   - Tortoise: 3-5 clips recommended

3. **Real-time voice cloning?**
   - So-VITS-SVC for singing voice
   - RVC (Retrieval Voice Conversion)

4. **Voice consistency across sessions?**
   - How to ensure same voice characteristics
   - Seed control in models

---

## Integration Plan

### Phase 1: Document existing voices
- [x] Create apple.yml registry
- [ ] Create web.yml registry
- [ ] Create windows.yml registry

### Phase 2: Test Personal Voice
- [ ] Document exact creation steps
- [ ] Test programmatic access
- [ ] Document workarounds

### Phase 3: Integrate Coqui TTS
- [ ] Create wrapper script
- [ ] Add to speech skill
- [ ] Document voice cloning workflow

### Phase 4: Character voice creation
- [ ] Workflow for cloning character voices
- [ ] Store voice models with characters
- [ ] Auto-select based on character metadata

---

## References

- [SavePersonalVoiceAudio](https://github.com/limneos/SavePersonalVoiceAudio) — Extract Personal Voice
- [Coqui TTS](https://github.com/coqui-ai/TTS) — Open source TTS
- [XTTS v2](https://huggingface.co/coqui/XTTS-v2) — Multilingual voice cloning
- [ElevenLabs](https://elevenlabs.io) — Commercial voice cloning
- [Tortoise TTS](https://github.com/neonbjb/tortoise-tts) — High quality slow TTS
- [Bark](https://github.com/suno-ai/bark) — Generative audio model

---

*Last updated: 2026-01-25*
