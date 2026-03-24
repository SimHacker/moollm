import pytest
from lib import util


def test_yaml_load_json_fallback():
    # Without PyYAML, yaml_load falls back to json for JSON-like input.
    out = util.yaml_load('{"a": 1}')
    assert out == {"a": 1}


def test_yaml_dump():
    out = util.yaml_dump({"a": 1, "b": 2})
    assert "a" in out and "1" in out


def test_apply_line_range():
    text = "line1\nline2\nline3\nline4\nline5"
    assert util.apply_line_range(text, 1, 1) == "line1"
    assert util.apply_line_range(text, 1, 3) == "line1\nline2\nline3"
    assert util.apply_line_range(text, 2, 4) == "line2\nline3\nline4"


def test_apply_line_range_empty():
    assert util.apply_line_range("", 1, 1) == ""


def test_apply_line_range_clamping():
    text = "a\nb\nc"
    assert util.apply_line_range(text, 1, 10) == "a\nb\nc"
    assert util.apply_line_range(text, 0, 2) == "a\nb"
