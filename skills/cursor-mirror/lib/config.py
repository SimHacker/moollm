# Configuration loading. Built-in defaults, then skill/user/project YAML overrides.

from pathlib import Path
from typing import Any

import yaml


def load_config() -> dict[str, Any]:
    """Load config from multiple sources (later overrides earlier)."""
    config: dict[str, Any] = {
        "limits": {"default": 50, "tail": 20, "stream": 100},
        "resolution": {"min_hash_prefix": 4, "match_hash_prefixes": True},
        "export": {"trailing_newline": True},
        "debug": {"enabled": False},
    }

    config_paths = [
        Path(__file__).resolve().parent.parent / "scripts" / "cursor_mirror_config.yml",
        Path.home() / ".config/cursor-mirror/config.yml",
        Path.home() / ".cursor-mirror.yml",
        Path.cwd() / ".moollm/cursor-mirror.yml",
    ]

    for cfg_path in config_paths:
        if cfg_path.exists():
            try:
                file_config = yaml.safe_load(cfg_path.read_text()) or {}
                for k, v in file_config.items():
                    if isinstance(v, dict) and k in config:
                        config[k].update(v)
                    else:
                        config[k] = v
            except Exception:
                pass

    return config


CONFIG = load_config()
