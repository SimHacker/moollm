# Layer 1: keys load from model YAML; expected keys present.

def test_session_list_keys_loaded():
    from lib.keys import SESSION_LIST_KEYS
    assert isinstance(SESSION_LIST_KEYS, list)
    assert len(SESSION_LIST_KEYS) >= 1
    assert "composer.composerData" in SESSION_LIST_KEYS


def test_composer_state_key():
    from lib.keys import COMPOSER_STATE_KEY
    assert isinstance(COMPOSER_STATE_KEY, str)
    assert "reactiveStorage" in COMPOSER_STATE_KEY


def test_bubble_prefix():
    from lib.keys import BUBBLE_PREFIX
    assert BUBBLE_PREFIX == "bubbleId"


def test_notable_global_keys():
    from lib.keys import NOTABLE_GLOBAL_KEYS
    assert isinstance(NOTABLE_GLOBAL_KEYS, list)
    assert len(NOTABLE_GLOBAL_KEYS) >= 1


def test_keys_loaded_from_yaml(model_dir):
    """Verify keys YAML files exist and are parseable."""
    import yaml
    for name in ["workspace-itemtable.yml", "global-itemtable.yml", "cursor-disk-kv.yml"]:
        path = model_dir / "keys" / name
        assert path.exists(), f"Missing: {path}"
        data = yaml.safe_load(path.read_text())
        assert isinstance(data, dict), f"Not a dict: {path}"
