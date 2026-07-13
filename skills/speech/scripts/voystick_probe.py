#!/usr/bin/env python3
"""
MOOLLM VoyStick probe — stream pitch (Y) from microphone for pie-wedge calibration.
Optional deps: sounddevice, aubio, numpy. Degrades with install instructions.
"""
from __future__ import annotations

import argparse
import json
import sys
import time


def main() -> int:
    p = argparse.ArgumentParser(description="Stream pitch Hz as JSON lines (VoyStick Y axis probe)")
    p.add_argument("--seconds", type=float, default=10.0)
    p.add_argument("--device", type=int, default=None)
    args = p.parse_args()

    try:
        import numpy as np
        import sounddevice as sd
        import aubio
    except ImportError as e:
        print(
            json.dumps(
                {
                    "error": "missing_deps",
                    "need": ["sounddevice", "aubio", "numpy"],
                    "install": "pip install sounddevice aubio numpy",
                    "detail": str(e),
                }
            ),
            file=sys.stderr,
        )
        return 2

    sr = 44100
    hop = 512
    pitch_o = aubio.pitch("yin", hop, hop, sr)
    pitch_o.set_tolerance(0.8)

    def callback(indata, _frames, _time, _status):
        samples = indata[:, 0].astype(np.float32)
        hz = float(pitch_o(samples)[0])
        y = min(1.0, max(0.0, (hz - 80.0) / 400.0)) if hz > 0 else 0.0
        print(json.dumps({"t": time.time(), "pitch_hz": hz, "y": y, "x": None}), flush=True)

    with sd.InputStream(
        channels=1,
        samplerate=sr,
        blocksize=hop,
        device=args.device,
        callback=callback,
    ):
        time.sleep(args.seconds)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
