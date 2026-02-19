# Layer 1: universal model YAML files are valid and consistent.
# This validates the model itself, not just that Python can read it.

from pathlib import Path

import yaml


def test_all_model_yaml_valid(model_dir: Path):
    """Every .yml in the model dir should parse without error."""
    for yml_file in model_dir.rglob("*.yml"):
        data = yaml.safe_load(yml_file.read_text())
        assert data is not None or yml_file.stat().st_size == 0, \
            f"Failed to parse: {yml_file}"


def test_glance_lists_all_chunks(model_dir: Path):
    """GLANCE.yml should reference all top-level .yml files in model/."""
    glance = yaml.safe_load((model_dir / "GLANCE.yml").read_text())
    top_level_ymls = {f.stem for f in model_dir.glob("*.yml") if f.name != "GLANCE.yml"}

    # GLANCE values reference filenames; keys may use underscores (YAML-safe).
    # Collect all referenced filenames from GLANCE values.
    referenced_stems: set[str] = set()
    for v in glance.values():
        if isinstance(v, str) and v.endswith(".yml"):
            referenced_stems.add(v.removesuffix(".yml"))
    # Also accept keys that match stems when hyphens are replaced with underscores
    glance_keys_normalized = {k.replace("_", "-") for k in glance.keys()} - {"description"}
    all_covered = referenced_stems | glance_keys_normalized

    missing = top_level_ymls - all_covered
    assert not missing, f"GLANCE.yml missing entries for: {missing}"


def test_sql_files_are_valid_sql(model_dir: Path):
    """SQL files should contain SELECT statements (basic sanity)."""
    sql_dir = model_dir / "sql"
    if not sql_dir.exists():
        return
    for sql_file in sql_dir.glob("*.sql"):
        text = sql_file.read_text().upper()
        assert "SELECT" in text, f"No SELECT in {sql_file.name}"


def test_paths_yml_has_all_platforms(model_dir: Path):
    paths = yaml.safe_load((model_dir / "paths.yml").read_text())
    for platform in ["darwin", "win32", "linux"]:
        assert platform in paths, f"Missing platform: {platform}"
        assert "base" in paths[platform]
        assert "global_db" in paths[platform]
        assert "workspace_storage" in paths[platform]


def test_keys_yml_session_list_priority(model_dir: Path):
    ws_keys = yaml.safe_load((model_dir / "keys" / "workspace-itemtable.yml").read_text())
    priority = ws_keys.get("session_list_priority", {}).get("keys", [])
    assert len(priority) >= 1, "Should have at least one session list key"
    assert "composer.composerData" in priority


def test_bubble_entity_has_type_field(model_dir: Path):
    bubble = yaml.safe_load((model_dir / "entities" / "bubble.yml").read_text())
    assert "type" in bubble or "type_values" in bubble or \
        any("type" in str(v) for v in bubble.values()), \
        "bubble.yml should document the type field (1=user, 2=assistant)"


def test_no_unicode_in_model_yaml(model_dir: Path):
    """Model YAML should be ASCII-safe (no em-dashes, ellipses, smart quotes)."""
    bad_chars = {
        '\u2014': 'em-dash',
        '\u2013': 'en-dash',
        '\u2026': 'ellipsis',
        '\u2018': 'left-single-quote',
        '\u2019': 'right-single-quote',
        '\u201c': 'left-double-quote',
        '\u201d': 'right-double-quote',
    }
    violations = []
    for yml_file in model_dir.rglob("*.yml"):
        text = yml_file.read_text()
        for char, name in bad_chars.items():
            if char in text:
                violations.append(f"{yml_file.name}: contains {name}")
    assert not violations, f"Unicode violations:\n" + "\n".join(violations)
