import pytest
from lib import config


def test_resolve_repo_by_alias():
    repos = {
        "alerts": {"github": "example-org/alerts", "description": "Alerts"},
        "app": {"github": "example-org/app-monorepo"},
    }
    gh, entry = config.resolve_repo("alerts", repos)
    assert gh == "example-org/alerts"
    assert entry == repos["alerts"]


def test_resolve_repo_by_github_name():
    repos = {"alerts": {"github": "example-org/alerts"}}
    gh, entry = config.resolve_repo("example-org/alerts", repos)
    assert gh == "example-org/alerts"
    assert entry is None


def test_resolve_repo_owner_slash_name():
    gh, _ = config.resolve_repo("example-org/app-monorepo", {})
    assert gh == "example-org/app-monorepo"


def test_resolve_repo_empty():
    assert config.resolve_repo("", {"a": {"github": "x"}}) == (None, None)
    assert config.resolve_repo(None, {}) == (None, None)


def test_resolve_repo_unknown():
    gh, entry = config.resolve_repo("unknown", {"alerts": {"github": "example-org/alerts"}})
    assert gh is None
    assert entry is None
