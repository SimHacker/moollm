"""Transcription I/O — Whisper JSON with word/segment timestamps."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any


def extract_audio_wav(video_path: Path, out_wav: Path) -> None:
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_path),
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
        str(out_wav),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def transcribe_whisper(
    audio_path: Path,
    model: str = "base",
    language: str | None = None,
) -> dict[str, Any]:
    """Run openai-whisper CLI; return parsed JSON with segments + words."""
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        cmd = [
            "whisper",
            str(audio_path),
            "--model",
            model,
            "--output_format",
            "json",
            "--word_timestamps",
            "True",
            "--output_dir",
            str(out_dir),
            "--verbose",
            "False",
        ]
        if language:
            cmd.extend(["--language", language])
        subprocess.run(cmd, check=True, capture_output=True)
        json_files = list(out_dir.glob("*.json"))
        if not json_files:
            raise SystemExit(f"Whisper produced no JSON for {audio_path}")
        return json.loads(json_files[0].read_text(encoding="utf-8"))


def transcribe_video(
    video_path: Path,
    model: str = "base",
    language: str | None = None,
    cache_dir: Path | None = None,
) -> dict[str, Any]:
    """Extract audio if needed, transcribe, optionally cache JSON."""
    if cache_dir:
        cache_dir.mkdir(parents=True, exist_ok=True)
        cached = cache_dir / f"{video_path.stem}.whisper.json"
        if cached.is_file():
            return json.loads(cached.read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio.wav"
        extract_audio_wav(video_path, wav)
        result = transcribe_whisper(wav, model=model, language=language)

    if cache_dir:
        cached.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def load_whisper_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def segments_from_whisper(whisper_doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize whisper segments to {start_s, end_s, text, words[]}."""
    out: list[dict[str, Any]] = []
    for seg in whisper_doc.get("segments", []):
        words = []
        for w in seg.get("words") or []:
            words.append(
                {
                    "text": (w.get("word") or "").strip(),
                    "start_s": round(float(w.get("start", 0)), 3),
                    "end_s": round(float(w.get("end", 0)), 3),
                }
            )
        out.append(
            {
                "start_s": round(float(seg.get("start", 0)), 3),
                "end_s": round(float(seg.get("end", 0)), 3),
                "text": (seg.get("text") or "").strip(),
                "words": words,
            }
        )
    return out
