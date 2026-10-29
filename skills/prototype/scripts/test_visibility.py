#!/usr/bin/env python3
"""Tests for visibility.py and private_leaks.py against fictional sibling repos in a temp dir."""
from __future__ import annotations

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import private_leaks  # noqa: E402
import visibility  # noqa: E402

PRIVATE_LIST = {
    "naming_rule": "any repo whose name contains 'private' (any case) is private",
    "repos": ["acme/secret-notes", "acme/vault", "acme/not-here"],
    "character_layers": {"acme/secret-notes": {"path": "characters/", "layer": "biography"},
                         "acme/vault": {"path": "", "layer": "private"}},
}


def checkout(root: Path, name: str, slug: str | None) -> Path:
    d = root / name
    (d / ".git").mkdir(parents=True)
    if slug:
        (d / ".git" / "config").write_text(f'[remote "origin"]\n\turl = git@github.com:{slug}.git\n')
    return d


class VisibilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="visibility_")).resolve()
        checkout(self.root, "moollm", "SimHacker/moollm")
        checkout(self.root, "secret-notes", "acme/secret-notes")
        checkout(self.root, "vault-local", "acme/vault")
        checkout(self.root, "ZetaPrivate", None)
        checkout(self.root, "notes-wiki", "acme/secret-notes.wiki")
        (self.root / "ZetaPrivate" / visibility.FILENAME).write_text(yaml.safe_dump(PRIVATE_LIST))
        self.v = visibility.Visibility(self.root)

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def test_listed_named_and_public(self) -> None:
        v = self.v
        self.assertTrue(v.is_private(self.root / "secret-notes"))
        self.assertTrue(v.is_private("vault-local"))
        self.assertTrue(v.is_private("ZetaPrivate"))
        self.assertTrue(v.is_private("notes-wiki"))
        self.assertTrue(v.is_private("acme/not-here"))
        self.assertTrue(v.is_private("someone/OtherPrivateThing"))
        self.assertFalse(v.is_private("moollm"))
        self.assertFalse(v.is_private("SimHacker/moollm"))
        self.assertEqual([d.name for d in v.public_checkouts()], ["moollm"])

    def test_private_names_and_character_layers(self) -> None:
        names = self.v.private_names()
        self.assertTrue({"acme/secret-notes", "acme/vault", "secret-notes", "vault-local",
                         "ZetaPrivate"} <= names)
        self.assertNotIn("moollm", names)
        self.assertEqual(self.v.character_layer("secret-notes"), ("characters/", "biography"))
        self.assertEqual(self.v.character_layer("vault-local"), ("", "private"))
        self.assertIsNone(self.v.character_layer("moollm"))

    def test_find(self) -> None:
        f = self.v.find
        self.assertEqual(f("inherits: moollm://github/acme/secret-notes/characters/x/"), ["acme/secret-notes"])
        self.assertEqual(f("see ../../../secret-notes/characters/x/"), ["secret-notes"])
        self.assertEqual(f("path ../ZetaPrivate"), ["ZetaPrivate"])
        self.assertEqual(f("drafts in ZetaPrivate/notes.md"), ["ZetaPrivate"])
        self.assertEqual(f("https://github.com/acme/vault/tree/main/x"), ["acme/vault"])
        self.assertEqual(f(f"{self.root}/vault-local/x"), ["vault-local"])
        for clean in ("news.ycombinator.com/threads?id=secret-notes", "user?id=secret-notes/",
                      "https://x.com/secret-notes/status/1", "medium.com/@secret-notes/post",
                      "skills/secret-notes/SKILL.md", "my-secret-notes/x", "acme/secret-notes-public"):
            self.assertEqual(f(clean), [], clean)

    def test_missing_or_broken_file_leaves_only_the_naming_rule(self) -> None:
        (self.root / "ZetaPrivate" / visibility.FILENAME).write_text("repos: [unclosed\n")
        v = visibility.Visibility(self.root)
        self.assertFalse(v.is_private("secret-notes"))
        self.assertTrue(v.is_private("ZetaPrivate"))
        self.assertEqual(v.find("../ZetaPrivate/x"), ["ZetaPrivate"])
        empty = visibility.Visibility(self.root / "nowhere")
        self.assertEqual((empty.private_names(), empty.find("anything/")), (set(), []))

    def test_remote_from_git(self) -> None:
        d = self.root / "cloned"
        d.mkdir()
        try:
            subprocess.run(["git", "init", "-q", str(d)], check=True)
            subprocess.run(["git", "-C", str(d), "remote", "add", "origin",
                            "https://github.com/acme/vault.git"], check=True)
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("git not available")
        self.assertEqual(visibility.remote_slug(d), "acme/vault")
        self.assertTrue(visibility.Visibility(self.root).is_private(d))


class LeakScanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="leaks_")).resolve()
        (self.root / "ZetaPrivate").mkdir()
        (self.root / "ZetaPrivate" / visibility.FILENAME).write_text(yaml.safe_dump(PRIVATE_LIST))
        pub = self.root / "public-repo"
        try:
            for d, url in ((pub, "https://github.com/acme/public-repo.git"),
                           (self.root / "secret-notes", "https://github.com/acme/secret-notes.git"),
                           (self.root / "ZetaPrivate", None)):
                d.mkdir(exist_ok=True)
                subprocess.run(["git", "init", "-q", str(d)], check=True)
                if url:
                    subprocess.run(["git", "-C", str(d), "remote", "add", "origin", url], check=True)
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("git not available")
        (pub / "a.md").write_text("ok\nsee ../secret-notes/characters/x/\nhn user?id=secret-notes\n"
                                  "moollm://github/acme/vault/x\n")
        (pub / "b.yml").write_text("clean: news.ycombinator.com/threads?id=secret-notes\n")
        (pub / "untracked.md").write_text("ZetaPrivate/plans\n")
        (self.root / "secret-notes" / "c.md").write_text("../secret-notes/ is fine here\n")
        subprocess.run(["git", "-C", str(pub), "add", "a.md", "b.yml"], check=True)
        subprocess.run(["git", "-C", str(self.root / "secret-notes"), "add", "c.md"], check=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def run_cli(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = private_leaks.main([*argv, "--root", str(self.root)])
        return code, out.getvalue()

    def test_hits_in_public_tracked_files_only(self) -> None:
        hits = private_leaks.scan(visibility.Visibility(self.root))
        self.assertEqual([(r, f, n, name) for r, f, n, name, _ in hits],
                         [("public-repo", "a.md", 2, "secret-notes"), ("public-repo", "a.md", 4, "acme/vault")])
        code, out = self.run_cli()
        self.assertEqual(code, 1)
        self.assertIn("public-repo/a.md:2: secret-notes:", out)

    def test_untracked_and_summary(self) -> None:
        code, out = self.run_cli("--untracked", "--summary")
        self.assertIn("hits: 3 in 2 files", out)
        self.assertIn("name ZetaPrivate", out)

    def test_clean_repo_exits_zero(self) -> None:
        (self.root / "public-repo" / "a.md").write_text("ok\n")
        code, out = self.run_cli("--repo", "public-repo")
        self.assertEqual(code, 0)
        self.assertIn("hits: 0", out)


if __name__ == "__main__":
    unittest.main()
