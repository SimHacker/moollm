# I5: Feature flag monitor.
# Compare current Cursor feature flags/config against universal model.
# Detects: new flags, removed flags, changed values -- Cursor API drift.
# Driven by reference/universal/model/features.yml

from pathlib import Path
from typing import Any
from dataclasses import dataclass, field

import yaml

from .db import get_item_table_value
from .debug_util import debug

_MODEL_DIR = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model"


def _load_yaml(name: str) -> dict[str, Any]:
    path = _MODEL_DIR / name
    if path.exists():
        return yaml.safe_load(path.read_text()) or {}
    return {}


@dataclass
class FeatureDiff:
    """Diff between model and live Cursor feature state."""
    new_flags: list[str] = field(default_factory=list)
    removed_flags: list[str] = field(default_factory=list)
    changed_values: dict[str, dict[str, Any]] = field(default_factory=dict)
    new_config_keys: list[str] = field(default_factory=list)
    removed_config_keys: list[str] = field(default_factory=list)

    @property
    def drift_detected(self) -> bool:
        return bool(self.new_flags or self.removed_flags or self.changed_values
                     or self.new_config_keys or self.removed_config_keys)

    def summary(self) -> dict[str, Any]:
        return {
            "drift_detected": self.drift_detected,
            "new_flags": self.new_flags,
            "removed_flags": self.removed_flags,
            "changed_values": self.changed_values,
            "new_config_keys": self.new_config_keys,
            "removed_config_keys": self.removed_config_keys,
        }


def load_model_features() -> dict[str, Any]:
    """Load documented features from features.yml."""
    return _load_yaml("features.yml")


def get_live_feature_flags() -> dict[str, bool]:
    """Read current feature flags from Cursor's DB."""
    raw = get_item_table_value("cursorai/featureStatusCache")
    if not isinstance(raw, dict):
        return {}
    return {k: bool(v) for k, v in raw.items() if isinstance(v, (bool, int))}


def get_live_feature_config() -> dict[str, Any]:
    """Read current feature config from Cursor's DB."""
    return get_item_table_value("cursorai/featureConfigCache") or {}


def get_live_server_config() -> dict[str, Any]:
    """Read current server config from Cursor's DB."""
    return get_item_table_value("cursorai/serverConfig") or {}


def diff_features() -> FeatureDiff:
    """Compare live Cursor state against documented model."""
    model = load_model_features()
    result = FeatureDiff()

    # Feature flags
    model_enabled = set(model.get("feature_flags", {}).get("enabled", []))
    model_disabled = set(model.get("feature_flags", {}).get("disabled", []))
    model_all_flags = model_enabled | model_disabled

    live_flags = get_live_feature_flags()
    live_all_flags = set(live_flags.keys())

    result.new_flags = sorted(live_all_flags - model_all_flags)
    result.removed_flags = sorted(model_all_flags - live_all_flags)

    for flag in model_all_flags & live_all_flags:
        model_val = flag in model_enabled
        live_val = live_flags.get(flag, False)
        if model_val != live_val:
            result.changed_values[flag] = {"model": model_val, "live": live_val}

    # Feature config (compare top-level keys)
    model_config = model.get("feature_config", {})
    model_config_flat = set()
    for section in model_config.values():
        if isinstance(section, dict) and section != {"location": model_config.get("location")}:
            model_config_flat.update(section.keys())

    live_config = get_live_feature_config()
    live_config_flat = set()
    if isinstance(live_config, dict):
        for v in live_config.values():
            if isinstance(v, dict):
                live_config_flat.update(v.keys())
            else:
                live_config_flat.add(str(v))

    # Server config keys
    model_server = model.get("server_config", {})
    model_server_flat = set()
    for section_key, section in model_server.items():
        if isinstance(section, dict) and section_key != "location":
            model_server_flat.update(section.keys())

    live_server = get_live_server_config()
    live_server_flat = set()
    if isinstance(live_server, dict):
        for v in live_server.values():
            if isinstance(v, dict):
                live_server_flat.update(v.keys())

    all_model_keys = model_config_flat | model_server_flat
    all_live_keys = live_config_flat | live_server_flat

    result.new_config_keys = sorted(all_live_keys - all_model_keys)
    result.removed_config_keys = sorted(all_model_keys - all_live_keys)

    if result.drift_detected:
        debug("feature drift detected: %d new flags, %d removed, %d changed",
              len(result.new_flags), len(result.removed_flags), len(result.changed_values))

    return result
