import pytest
from lib import urls


def test_is_moo_url():
    assert urls.is_moo_url("moo://Issue_0/ALERT.yml") is True
    assert urls.is_moo_url("moollm://leela-ai/leela-alerts/main/GLANCE.yml") is True
    assert urls.is_moo_url("https://example.com") is False
    assert urls.is_moo_url("") is False
    assert urls.is_moo_url(None) is False


def test_parse_moo_url_moo_scheme():
    p = urls.parse_moo_url("moo://Issue_0/ALERT.yml")
    assert p is not None
    assert p["scheme"] == "moo"
    assert p["repo"] is None
    assert p["branch"] == "Issue_0"
    assert p["path"] == "ALERT.yml"
    assert p["fragment"] == ""
    assert p["query"] == ""


def test_parse_moo_url_moollm_scheme():
    # urlparse: netloc=leela-ai, path=/leela-alerts/main/skills/moo/GLANCE.yml → repo=netloc, branch=first segment, path=rest
    p = urls.parse_moo_url("moollm://leela-ai/leela-alerts/main/skills/moo/GLANCE.yml")
    assert p is not None
    assert p["scheme"] == "moollm"
    assert p["repo"] == "leela-ai"
    assert p["branch"] == "leela-alerts"
    assert p["path"] == "main/skills/moo/GLANCE.yml"


def test_parse_moo_url_invalid():
    assert urls.parse_moo_url("http://x/y") is None
    assert urls.parse_moo_url("moo://") is None


def test_parse_fragment_empty():
    assert urls.parse_fragment("") == ("", None, None)
    assert urls.parse_fragment(None) == ("", None, None)


def test_parse_fragment_line_only():
    assert urls.parse_fragment("L3") == ("", 3, 3)
    assert urls.parse_fragment("L3-L10") == ("", 3, 10)


def test_parse_fragment_key_path():
    assert urls.parse_fragment("severity") == ("severity", None, None)
    assert urls.parse_fragment("payload/camera_name") == ("payload/camera_name", None, None)


def test_parse_fragment_key_and_lines():
    assert urls.parse_fragment("payload:L3") == ("payload", 3, 3)
    assert urls.parse_fragment("payload:L3-L10") == ("payload", 3, 10)
