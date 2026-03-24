import pytest
from lib import storage


def test_extract_at_path_yaml_empty_path():
    content = "name: moo\ndescription: VM\n"
    val, structured = storage.extract_at_path(content, "x.yml", "")
    assert structured is True
    assert val.get("name") == "moo"


def test_extract_at_path_yaml_key_path():
    content = "payload:\n  camera_name: CAM1\n  count: 2\n"
    val, structured = storage.extract_at_path(content, "x.yml", "payload/camera_name")
    assert structured is True
    assert val == "CAM1"


def test_extract_at_path_json():
    content = '{"a": 1, "b": {"c": 2}}'
    val, structured = storage.extract_at_path(content, "x.json", "b/c")
    assert structured is True
    assert val == 2


def test_extract_at_path_list_index():
    content = "list:\n  - first\n  - second\n"
    val, structured = storage.extract_at_path(content, "x.yml", "list/1")
    assert structured is True
    assert val == "second"


def test_extract_at_path_non_structured():
    content = "plain text"
    val, structured = storage.extract_at_path(content, "x.txt", "")
    assert structured is False
    assert val == "plain text"


def test_extract_at_path_missing_key_raises():
    content = "a: 1\n"
    with pytest.raises(KeyError):
        storage.extract_at_path(content, "x.yml", "missing")
