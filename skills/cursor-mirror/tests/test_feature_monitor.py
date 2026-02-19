# Layer 2: validate feature flags against actual Cursor data.
# Detects: new flags, removed flags, changed values -- Cursor API evolution.

from pathlib import Path


def test_model_features_load():
    from lib.feature_monitor import load_model_features
    features = load_model_features()
    assert "feature_flags" in features
    assert "feature_config" in features
    assert "server_config" in features


def test_live_feature_flags(global_db: Path):
    from lib.feature_monitor import get_live_feature_flags
    flags = get_live_feature_flags()
    assert isinstance(flags, dict)
    assert len(flags) > 0, "Should have at least one feature flag"
    print(f"\nLive feature flags: {len(flags)} total")


def test_live_server_config(global_db: Path):
    from lib.feature_monitor import get_live_server_config
    config = get_live_server_config()
    assert isinstance(config, dict)
    assert len(config) > 0, "Should have server config"


def test_diff_features(global_db: Path):
    """Layer 2: detect Cursor feature drift since model was last updated."""
    from lib.feature_monitor import diff_features
    diff = diff_features()

    print(f"\nFeature drift report:")
    print(f"  New flags (not in model): {diff.new_flags[:10]}{'...' if len(diff.new_flags) > 10 else ''}")
    print(f"  Removed flags: {diff.removed_flags[:10]}")
    print(f"  Changed values: {dict(list(diff.changed_values.items())[:5])}")
    print(f"  New config keys: {diff.new_config_keys[:10]}")
    print(f"  Drift detected: {diff.drift_detected}")

    # Report drift but don't fail -- drift is expected and informative.
    # These tests exist to DETECT evolution, not prevent it.
