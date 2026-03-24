import pytest
from lib import config


def test_resolve_repo_by_alias():
    repos = {
        "alerts": {"github": "leela-ai/leela-alerts", "description": "Alerts"},
        "central": {"github": "leela-ai/central"},
    }
    gh, entry = config.resolve_repo("alerts", repos)
    assert gh == "leela-ai/leela-alerts"
    assert entry == repos["alerts"]


def test_resolve_repo_by_github_name():
    repos = {"alerts": {"github": "leela-ai/leela-alerts"}}
    gh, entry = config.resolve_repo("leela-ai/leela-alerts", repos)
    assert gh == "leela-ai/leela-alerts"
    assert entry is None


def test_resolve_repo_owner_slash_name():
    gh, _ = config.resolve_repo("leela-ai/central", {})
    assert gh == "leela-ai/central"


def test_resolve_repo_empty():
    assert config.resolve_repo("", {"a": {"github": "x"}}) == (None, None)
    assert config.resolve_repo(None, {}) == (None, None)


def test_resolve_repo_unknown():
    gh, entry = config.resolve_repo("unknown", {"alerts": {"github": "leela-ai/alerts"}})
    assert gh is None
    assert entry is None
