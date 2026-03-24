import pytest
from pathlib import Path

from lib import overlay


def test_load_overlay_empty_file(tmp_path):
    f = tmp_path / "overlay.yml"
    f.write_text("")
    out = overlay.load_overlay(str(f), {})
    assert out["repos"] == []
    assert out["defaults"] == {}


def test_load_overlay_with_defaults_and_repos(tmp_path):
    f = tmp_path / "overlay.yml"
    f.write_text("""
defaults:
  depth: 1
  at_depth:
    0: [GLANCE.yml]
    1: [CARD.yml]
repos:
  - repo: leela-ai/alerts
    type: Issue
    depth: 2
    at_depth:
      0: [GLANCE.yml]
      1: [CARD.yml]
      2: [ALERT.yml]
""")
    repos_config = {"alerts": {"github": "leela-ai/alerts"}}
    out = overlay.load_overlay(str(f), repos_config)
    assert len(out["repos"]) == 1
    r = out["repos"][0]
    assert r["repo"] == "leela-ai/alerts"
    assert r["type"] == "Issue"
    assert r["depth"] == 2
    assert r["at_depth"][0] == ["GLANCE.yml"]
    assert r["at_depth"][2] == ["ALERT.yml"]


def test_load_overlay_resolves_alias(tmp_path):
    f = tmp_path / "overlay.yml"
    f.write_text("""
repos:
  - repo: myalias
    depth: 1
    at_depth: { 0: [GLANCE.yml] }
""")
    repos_config = {"myalias": {"github": "owner/repo"}}
    out = overlay.load_overlay(str(f), repos_config)
    assert out["repos"][0]["repo"] == "owner/repo"


def test_default_overlay_path_returns_path_or_none():
    p = overlay.default_overlay_path()
    assert p is None or (isinstance(p, Path) and (p.exists() or not p.exists()))
