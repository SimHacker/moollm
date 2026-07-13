# moollm-speech — native SpeechAnalyzer bridge (planned)

Swift CLI target for macOS/iOS 26+ that exposes Apple STT to Python/Node adventure runtimes
via **JSON lines on stdout** — tight integration without embedding Swift in every host.

## Why compile

`SpeechAnalyzer` / `SpeechTranscriber` are **Swift-only**. No stable `say`-style shell for STT.
Python `ctypes` cannot reach it. Options:

1. **This CLI** (recommended) — one binary, spawn from `stt_dispatch.py`
2. **SwiftPM library** linked from iOS safari app
3. **Legacy** `SFSpeechRecognizer` — still valid for custom vocabulary only

## Planned interface

```bash
moollm-speech listen --locale en-US --timestamps
# stdout (newline-delimited JSON):
# {"type":"partial","text":"take me","confidence":0.91}
# {"type":"final","text":"take me to the canal","start":1.2,"end":2.8,"confidence":0.94}
```

## Minimal Swift shape (WWDC 2025 pattern)

```swift
let transcriber = SpeechTranscriber(
    locale: locale,
    transcriptionOptions: [],
    reportingOptions: [],
    attributeOptions: [.audioTimeRange]
)
let analyzer = SpeechAnalyzer(modules: [transcriber])
// Task { for try await r in transcriber.results { emitJSON(r) } }
// analyzer.analyzeSequence(from: micBufferSequence)
// await analyzer.finalizeAndFinishThroughEndOfInput()
```

Download models on first use:

```swift
if let req = try await AssetInventory.assetInstallationRequest(supporting: [transcriber]) {
    try await req.downloadAndInstall()
}
```

## VoyStick

**Not** in SpeechTranscriber output. Run parallel:

- `AVAudioEngine` input tap → pitch (vDSP / aubio) → JSON `{"voystick":{"x":0.3,"y":0.7}}`
- Or pipe same mic to `voystick_probe.py` on Mac for dev calibration

## Wire-up

When built, set `MOOLLM_SPEECH_CLI=/path/to/moollm-speech` and extend `stt_dispatch.py` to spawn it.

Spec: [../platforms/apple-speech-analyzer.yml](../platforms/apple-speech-analyzer.yml)
