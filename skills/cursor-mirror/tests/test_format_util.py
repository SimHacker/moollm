# Layer 1: formatting utilities (no Cursor DB needed).

import json


def test_format_ts_string():
    from lib.format_util import format_ts
    assert format_ts("2026-02-19T12:34:56.789Z") == "2026-02-19 12:34:56"


def test_format_ts_millis():
    from lib.format_util import format_ts
    result = format_ts(1708300000000)
    assert "2024" in result
    assert ":" in result


def test_format_ts_none():
    from lib.format_util import format_ts
    assert format_ts(None) == ""


def test_get_output_format_default():
    from lib.format_util import get_output_format
    from types import SimpleNamespace
    args = SimpleNamespace(output_format=None, json=False, yaml=False)
    assert get_output_format(args) == "text"


def test_get_output_format_explicit():
    from lib.format_util import get_output_format
    from types import SimpleNamespace
    args = SimpleNamespace(output_format="yaml", json=False, yaml=False)
    assert get_output_format(args) == "yaml"


def test_get_output_format_legacy_json():
    from lib.format_util import get_output_format
    from types import SimpleNamespace
    args = SimpleNamespace(output_format=None, json=True, yaml=False)
    assert get_output_format(args) == "json"


def test_output_data_json(capsys):
    from lib.format_util import output_data
    output_data({"key": "value"}, "json", supported=["json"])
    captured = capsys.readouterr()
    parsed = json.loads(captured.out)
    assert parsed["key"] == "value"
