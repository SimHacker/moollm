#!/usr/bin/env python3
"""Tests for layers_lint.py against temporary sibling repos. Run: python3 test_layers_lint.py"""
from __future__ import annotations

import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layers_lint as ll  # noqa: E402

BIO = "secret-notes/characters"
PROFILE = "WillWrightShowForFood/characters"
CAST = "WillWrightShowForFood/characters/menagerie"
AUDIENCE = "WillWrightShowForFood/repo-shows/show/audience"
ADVENTURE = "moollm/examples/adventure-4/characters"


def person(i: str, envelope: bool = True, **extra: Any) -> dict[str, Any]:
    core = {"id": i, "name": i.replace("-", " ").title(), "real_being": True, "status": "living",
            "signifier": "👤"}
    core.update({k: v for k, v in extra.items() if k != "representation"})
    rep = extra.get("representation", {"authored_by": "don-hopkins", "public_figure": True})
    if envelope:
        return {"character": core, "representation": rep}
    return {**core, "representation": rep}


def rep(**kv: Any) -> dict[str, Any]:
    return {"authored_by": "don-hopkins", **kv}


GRANTED = {"state": "granted", "date": "2026-08-01", "evidence": "correspondence/2026-08-01-yes.md"}


class LintCase(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="layers_lint_"))
        for repo, slug in (("moollm", "SimHacker/moollm"), ("secret-notes", "acme/secret-notes"),
                           ("WillWrightShowForFood", "SimHacker/WillWrightShowForFood"),
                           ("ZetaPrivate", "acme/ZetaPrivate")):
            (self.root / repo / ".git").mkdir(parents=True)
            (self.root / repo / ".git" / "config").write_text(
                f'[remote "origin"]\n\turl = git@github.com:{slug}.git\n')
        (self.root / "ZetaPrivate" / "PRIVATE-REPOS.yml").write_text(yaml.safe_dump({
            "naming_rule": "names containing private",
            "repos": ["acme/secret-notes", "acme/ZetaPrivate"],
            "character_layers": {"acme/secret-notes": {"path": "characters/", "layer": "biography"}}}))
        (self.root / "moollm/skills/real-being").mkdir(parents=True)
        self.saved_refs = ll._refs
        ll._refs = None

    def tearDown(self) -> None:
        ll._refs = self.saved_refs
        shutil.rmtree(self.root)

    def put(self, where: str, i: str, data: Any) -> Path:
        p = self.root / where / i / "CHARACTER.yml"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(data if isinstance(data, str) else yaml.safe_dump(data, allow_unicode=True))
        return p

    def lint(self, ids: list[str] | None = None) -> dict[str, Any]:
        return ll.run(self.root, ids)

    def rules(self, res: dict[str, Any], i: str | None = None) -> list[tuple[str, str]]:
        return [(f.severity, f.rule) for f in res["findings"] if i is None or f.id == i]


class FactTests(LintCase):
    def test_public_figure_disagreement_is_error_and_review_item(self) -> None:
        self.put(BIO, "bill", person("bill",
                                     inherits=["moollm://github/x/WillWrightShowForFood/characters/bill/"]))
        self.put(PROFILE, "bill", person("bill", representation=rep(public_figure=False)))
        res = self.lint()
        errs = [f for f in res["findings"] if f.severity == "error"]
        self.assertEqual([(f.rule, f.file) for f in errs],
                         [("fact-public-figure", f"{PROFILE}/bill/CHARACTER.yml")])
        self.assertIn("False here", errs[0].message)
        self.assertEqual(errs[0].layers, ["biography", "wwsff-profile"])
        self.assertEqual(len(res["review"]), 1)
        item = res["review"][0]
        self.assertEqual((item["id"], item["fact"], item["reason"], item["decision"]),
                         ("bill", "public_figure", "layers disagree", None))
        self.assertEqual(sorted(v["value"] for v in item["values"]), [False, True])

    def test_absent_fact_is_unknown_not_disagreement(self) -> None:
        self.put(BIO, "ann", person("ann", representation=rep(public_figure=True, consent=GRANTED)))
        self.put(PROFILE, "ann", person("ann", representation=rep()))
        res = self.lint()
        self.assertNotIn("error", [s for s, _ in self.rules(res, "ann")])
        self.assertNotIn(("warning", "public-figure-unknown"), self.rules(res, "ann"))
        self.assertEqual(res["review"], [])

    def test_consent_state_decisive_disagreement_is_error(self) -> None:
        self.put(BIO, "g", person("g", representation=rep(public_figure=True, consent=GRANTED)))
        self.put(PROFILE, "g", person("g", representation=rep(consent={"state": "asked"})))
        self.put(BIO, "d", person("d", representation=rep(public_figure=True,
                                                          consent={"state": "declined"})))
        self.put(PROFILE, "d", person("d", representation=rep(consent={"state": "not_asked"})))
        res = self.lint()
        for i in ("g", "d"):
            self.assertIn(("error", "consent-state"), self.rules(res, i))
        self.assertEqual([(r["id"], r["fact"]) for r in res["review"]],
                         [("d", "consent.state"), ("g", "consent.state")])
        self.assertEqual([v["value"] for v in res["review"][1]["values"]], ["granted", "asked"])

    def test_asked_vs_not_asked_is_stale_warning_naming_the_layer_behind(self) -> None:
        self.put(BIO, "s", person("s", representation=rep(public_figure=True,
                                                          consent={"state": "not_asked"})))
        self.put(PROFILE, "s", person("s", representation=rep(consent={"state": "awaiting_reply"})))
        res = self.lint()
        stale = [f for f in res["findings"] if f.rule == "consent-stale"]
        self.assertEqual([(f.severity, f.file) for f in stale], [("warning", f"{BIO}/s/CHARACTER.yml")])
        self.assertIn("biography is behind", stale[0].message)
        self.assertNotIn("error", [s for s, _ in self.rules(res, "s")])
        self.assertEqual(res["review"], [])

    def test_legacy_consent_spellings_are_info_and_never_compared(self) -> None:
        self.put(BIO, "m", person("m", representation=rep(public_figure=True, consent_level=3)))
        self.put(PROFILE, "m", person("m", representation=rep(consent="self-sovereign", kind="x")))
        self.put(AUDIENCE, "m", person("m", consent_level="5_deceased_legacy"))
        res = self.lint()
        self.assertNotIn("error", [s for s, _ in self.rules(res, "m")])
        self.assertEqual(self.rules(res, "m").count(("info", "consent-legacy")), 4)

    def test_status_spellings_normalize(self) -> None:
        self.put(BIO, "mouse", person("mouse", status="deceased", signifier="🕯️"))
        self.put(PROFILE, "mouse", person("mouse", status="memorial", signifier="🕯"))
        self.put(AUDIENCE, "mouse", person("mouse", status="passed", signifier="🕯️"))
        res = self.lint()
        self.assertNotIn("error", [s for s, _ in self.rules(res)])
        self.assertNotIn(("info", "signifier"), self.rules(res, "mouse"))

    def test_life_facts(self) -> None:
        self.put(BIO, "al", person("al", dates={"born": 1940, "died": 2020}))
        self.put(PROFILE, "al", person("al", born="1940-05-17", memorial={"died": 2021}))
        res = self.lint()
        self.assertEqual([r for r in self.rules(res, "al") if r[0] == "error"], [("error", "fact-died")])
        self.assertEqual([i["fact"] for i in res["review"]], ["died"])

    def test_status_living_vs_deceased_is_error(self) -> None:
        self.put(BIO, "z", person("z", status="living"))
        self.put(PROFILE, "z", person("z", status="memorial"))
        self.assertIn(("error", "fact-status"), self.rules(self.lint(), "z"))

    def test_status_vocabulary_is_warning(self) -> None:
        self.put(ADVENTURE, "bot", {"id": "bot", "name": "Bot", "status": "active", "signifier": "🤖"})
        self.put(CAST, "bot", {"character": {"id": "bot", "name": "Bot", "status": "reified",
                                             "real_being": False, "signifier": "🤖"}})
        r = self.rules(self.lint(), "bot")
        self.assertIn(("warning", "status-vocabulary"), r)
        self.assertNotIn("error", [s for s, _ in r])

    def test_reified_is_fictional(self) -> None:
        self.put(ADVENTURE, "elf", {"id": "elf", "name": "Elf", "status": "fictional", "signifier": "🎭"})
        self.put(CAST, "elf", {"id": "elf", "name": "Elf", "status": "reified", "signifier": "🎭"})
        r = self.rules(self.lint(), "elf")
        self.assertNotIn(("warning", "status-vocabulary"), r)
        self.assertNotIn(("warning", "public-figure-unknown"), r)

    def test_name_disagreement_is_warning(self) -> None:
        self.put(BIO, "n", person("n", name="Ann Smith"))
        self.put(PROFILE, "n", person("n", name="Anne Smith"))
        self.assertIn(("warning", "fact-name"), self.rules(self.lint(), "n"))


class RepresentationRuleTests(LintCase):
    def rule_of(self, res: dict[str, Any], i: str) -> str | None:
        return next(b["rule"] for b in res["beings"] if b["id"] == i)

    def test_governing_rule_first_match(self) -> None:
        self.put(BIO, "old", person("old", status="deceased", signifier="🕯️",
                                    representation=rep(authored_by="old", public_figure=True)))
        self.put(BIO, "me", person("me", representation=rep(authored_by="me")))
        self.put(PROFILE, "me2", person("me2", representation={"authored_by": "self"}))
        self.put(BIO, "yes", person("yes", representation=rep(public_figure=False, consent=GRANTED)))
        self.put(BIO, "pub", person("pub"))
        self.put(BIO, "priv", person("priv", representation=rep(public_figure=False)))
        self.put(ADVENTURE, "grue", {"id": "grue", "name": "Grue", "status": "fictional"})
        res = self.lint()
        self.assertEqual({i: self.rule_of(res, i) for i in ("old", "me", "me2", "yes", "pub", "priv", "grue")},
                         {"old": "memorial", "me": "self_authored", "me2": "self_authored",
                          "yes": "consented", "pub": "public_figure", "priv": "private", "grue": None})
        self.assertIn(("info", "authored-by-spelling"), self.rules(res, "me2"))
        s = ll.summary(res)
        self.assertEqual(s["governing_rules"], {"memorial": 1, "self_authored": 2, "consented": 1,
                                                "public_figure": 1, "private": 1})

    def test_rule_reads_facts_from_other_layers(self) -> None:
        self.put(BIO, "x", person("x", status="deceased", signifier="🕯️"))
        self.put(PROFILE, "x", {"character": {"id": "x", "name": "X", "real_being": True},
                                "representation": rep()})
        self.assertEqual(self.rule_of(self.lint(), "x"), "memorial")

    def test_granted_without_evidence_is_error_and_governs_nothing(self) -> None:
        self.put(BIO, "e", person("e", representation=rep(public_figure=True,
                                                          consent={"state": "granted"})))
        res = self.lint(["e"])
        self.assertIn(("error", "consent-no-evidence"), self.rules(res, "e"))
        self.assertEqual(self.rule_of(res, "e"), "public_figure")

    def test_speaks_as_only_under_self_authored_or_consented(self) -> None:
        self.put(BIO, "a", person("a", representation=rep(authored_by="a", speaks_as=True)))
        self.put(BIO, "b", person("b", representation=rep(consent=GRANTED, speaks_as=True,
                                                          public_figure=True)))
        self.put(BIO, "c", person("c", representation=rep(public_figure=True, speaks_as=True)))
        self.put(BIO, "d", person("d", status="deceased", signifier="🕯️",
                                  representation=rep(authored_by="d", speaks_as=True)))
        res = self.lint(["a", "b", "c", "d"])
        errs = sorted(f.id for f in res["findings"] if f.rule == "speaks-as")
        self.assertEqual(errs, ["c", "d"])
        self.assertIn("public_figure rule", next(f.message for f in res["findings"]
                                                 if f.rule == "speaks-as" and f.id == "c"))

    def test_public_figure_unknown_counted_per_being(self) -> None:
        self.put(BIO, "u", person("u", representation=rep()))
        self.put(PROFILE, "u", person("u", representation=rep(consent={"state": "not_asked"})))
        self.put(BIO, "v", person("v", representation=rep()))
        self.put(BIO, "dead", person("dead", status="deceased", signifier="🕯️", representation=rep()))
        self.put(BIO, "fic", {"id": "fic", "name": "Fic", "real_being": False, "status": "living",
                              "representation": rep()})
        self.put(BIO, "k", person("k"))
        res = self.lint()
        pf = [f for f in res["findings"] if f.rule == "public-figure-unknown"]
        self.assertEqual(sorted((f.id, f.severity) for f in pf), [("u", "warning"), ("v", "warning")])
        self.assertEqual(ll.summary(res)["public_figure_unknown"], {"count": 2, "ids": ["u", "v"]})
        self.assertEqual(self.rule_of(res, "u"), "private")

    def test_unverified_is_warning_and_review_item_with_note(self) -> None:
        self.put(PROFILE, "w", person("w", representation=rep(public_figure=True, consent={
            "state": "unverified", "note": "old friend;\n  cheered the plans"})))
        res = self.lint()
        self.assertIn(("warning", "consent-unverified"), self.rules(res, "w"))
        self.assertEqual(len(res["review"]), 1)
        item = res["review"][0]
        self.assertEqual((item["id"], item["fact"], item["decision"]), ("w", "consent.state", None))
        self.assertTrue(item["reason"].startswith("unverified"))
        self.assertEqual(item["values"], [{"layer": "wwsff-profile", "file": f"{PROFILE}/w/CHARACTER.yml",
                                           "value": "unverified", "spelled": "representation.consent.state",
                                           "note": "old friend; cheered the plans"}])

    def test_private_repo_entries_carry_only_path_and_value(self) -> None:
        p = self.root / "ZetaPrivate/characters/q/CHARACTER.yml"
        lay = ll.Layer("private", "ZetaPrivate", "characters/q/CHARACTER.yml", p,
                       {"representation": {"consent": {"state": "unverified", "note": "secret"}}})
        lay.f = lay.data
        entry = ll.value_entry(ll.Fact(lay, "unverified", "representation.consent.state"),
                               self.root, note=True)
        self.assertEqual(entry, {"layer": "private", "file": "ZetaPrivate/characters/q/CHARACTER.yml",
                                 "value": "unverified"})

    def test_bad_consent_values_warn_without_crashing(self) -> None:
        self.put(BIO, "z", person("z", representation=rep(public_figure=True, consent={"state": "maybe"})))
        self.put(PROFILE, "z", person("z", representation=rep(consent=["granted"])))
        self.put(AUDIENCE, "z", person("z", representation=rep(consent={"state": 7})))
        self.put(ADVENTURE, "z", person("z", representation="not a map"))
        res = self.lint()
        self.assertEqual(self.rules(res, "z").count(("warning", "consent-state-unknown")), 3)
        self.assertNotIn(("warning", "lint-crashed"), self.rules(res, "z"))


class RelationTests(LintCase):
    def test_missing_relation_on_non_canonical_layer(self) -> None:
        self.put(BIO, "p", person("p"))
        self.put(PROFILE, "p", person("p"))
        res = self.lint()
        missing = [f for f in res["findings"] if f.rule == "relation-missing"]
        self.assertEqual([f.file for f in missing], [f"{PROFILE}/p/CHARACTER.yml"])
        self.assertEqual(missing[0].severity, "warning")

    def test_parent_that_is_not_a_layer_still_missing(self) -> None:
        self.put(BIO, "p", person("p"))
        self.put(PROFILE, "p", person("p", inherits=["moollm://github/SimHacker/moollm/skills/real-being/"]))
        res = self.lint()
        self.assertIn(("warning", "relation-missing"), self.rules(res, "p"))
        self.assertNotIn(("warning", "ref-unresolved"), self.rules(res, "p"))

    def test_legacy_spelling_counts_and_is_reported(self) -> None:
        self.put(BIO, "p", person("p", public_portrayal="WillWrightShowForFood/characters/p/"))
        self.put(PROFILE, "p", person("p", moollm_source={
            "repo": "SimHacker/moollm", "path": "moollm/examples/adventure-4/characters/p",
            "absolute_url": "https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/p"}))
        self.put(ADVENTURE, "p", person("p", see_also=["../../../../../WillWrightShowForFood/characters/p/"]))
        r = self.rules(self.lint(), "p")
        self.assertNotIn(("warning", "relation-missing"), r)
        self.assertNotIn(("warning", "ref-unresolved"), r)
        self.assertEqual(r.count(("info", "relation-alias")), 3)

    def test_relative_ref_and_see_also(self) -> None:
        self.put(PROFILE, "q", person("q"))
        self.put(AUDIENCE, "q", person("q", character_ref="../../../../characters/q/CHARACTER.yml"))
        self.put(BIO, "q", person("q", see_also=["../../../WillWrightShowForFood/characters/q/"]))
        r = self.rules(self.lint(), "q")
        self.assertEqual(r.count(("warning", "relation-missing")), 0)
        self.assertEqual(r.count(("info", "relation-alias")), 2)

    def test_unresolved_ref(self) -> None:
        self.put(PROFILE, "u", person("u"))
        self.put(BIO, "u", person("u", upstream="../../../WillWrightShowForFood/characters/nobody/"))
        self.assertIn(("warning", "ref-unresolved"), self.rules(self.lint(), "u"))

    def test_absent_repo_and_foreign_urls_are_not_checked(self) -> None:
        self.put(BIO, "u", person("u"))
        self.put(PROFILE, "u", person("u", inherits=["moollm://github/x/NotCheckedOut/characters/u/",
                                                    "https://example.com/u"]))
        self.assertNotIn(("warning", "ref-unresolved"), self.rules(self.lint(), "u"))

    def test_fictional_canonical_is_adventure(self) -> None:
        self.put(ADVENTURE, "grue", {"id": "grue", "name": "Grue", "status": "fictional",
                                    "signifier": "🎭", "inherits": ["skills/real-being"]})
        self.put(CAST, "grue", {"character": {"id": "grue", "name": "Grue", "real_being": False,
                                              "status": "fictional", "signifier": "🎭"}})
        res = self.lint()
        missing = [f.file for f in res["findings"] if f.rule == "relation-missing"]
        self.assertEqual(missing, [f"{CAST}/grue/CHARACTER.yml"])
        self.assertNotIn(("info", "signifier"), self.rules(res, "grue"))
        self.assertNotIn(("warning", "key-missing"), self.rules(res, "grue"))


class KeyAndSignifierTests(LintCase):
    def test_core_keys_for_real_being(self) -> None:
        self.put(BIO, "k", person("k"))
        self.put(PROFILE, "k", {"character": {"id": "k", "name": "K", "status": "living"}})
        res = self.lint()
        msgs = [f.message for f in res["findings"] if f.rule == "key-missing"]
        self.assertEqual(msgs, ["core keys missing: signifier, real_being, representation.authored_by"])

    def test_signifier_convention(self) -> None:
        self.put(BIO, "w", person("w", signifier="🌍"))
        self.put(PROFILE, "w", person("w", envelope=False))
        res = self.lint()
        sig = [f for f in res["findings"] if f.rule == "signifier"]
        self.assertEqual([(f.severity, f.file) for f in sig], [("info", f"{BIO}/w/CHARACTER.yml")])
        self.assertIn("move to emoji:", sig[0].message)


class RobustnessTests(LintCase):
    def test_single_layer_ids_skipped_unless_named(self) -> None:
        self.put(BIO, "solo", person("solo"))
        self.assertEqual(self.lint()["checked"], [])
        self.assertEqual(self.rules(self.lint(["solo"])), [("info", "single-layer")])
        self.assertEqual(self.rules(self.lint(["ghost"])), [("info", "single-layer")])

    def test_unparseable_file_does_not_crash(self) -> None:
        self.put(BIO, "x", person("x"))
        self.put(PROFILE, "x", person("x"))
        self.put(ADVENTURE, "x", "id: x\n  bad: [unclosed\n")
        self.assertIn(("warning", "unparseable"), self.rules(self.lint(), "x"))

    def test_broken_refs_module_falls_back(self) -> None:
        class Broken:
            @staticmethod
            def locate(*a: Any, **k: Any) -> Any:
                raise RuntimeError("boom")

            @staticmethod
            def parse_ref(*a: Any, **k: Any) -> Any:
                raise ValueError("nope")

        ll._refs = Broken()
        self.put(PROFILE, "r", person("r"))
        self.put(BIO, "r", person("r", inherits=["moollm://github/x/WillWrightShowForFood/characters/r/"]))
        self.assertNotIn(("warning", "relation-missing"), self.rules(self.lint(), "r"))

    def test_refs_module_hit_is_used(self) -> None:
        target = self.put(BIO, "s", person("s"))

        class Hit:
            @staticmethod
            def locate(ref: str, base: Path, root: Path) -> Path:
                return target.parent

        ll._refs = Hit()
        self.put(PROFILE, "s", person("s", inherits=["somewhere:only-refs-knows"]))
        self.assertNotIn(("warning", "relation-missing"), self.rules(self.lint(), "s"))

    def test_with_real_refs_module(self) -> None:
        try:
            import refs
        except Exception:
            self.skipTest("refs.py not importable")
        ll._refs = refs
        self.put(PROFILE, "t", person("t"))
        self.put(BIO, "t", person("t", inherits=["moollm://github/SimHacker/WillWrightShowForFood/characters/t/"],
                                  upstream="../../../WillWrightShowForFood/characters/missing/"))
        r = self.rules(self.lint(), "t")
        self.assertNotIn(("warning", "relation-missing"), r)
        self.assertIn(("warning", "ref-unresolved"), r)


class VisibilityTests(LintCase):
    def test_public_layer_naming_a_private_repo_is_an_error(self) -> None:
        self.put(BIO, "v", person("v", inherits=["moollm://github/SimHacker/WillWrightShowForFood/characters/v/"]))
        self.put(PROFILE, "v", person("v", inherits=["moollm://github/acme/secret-notes/characters/v/"],
                                      see_also=["../../../secret-notes/characters/v/"],
                                      notes={"where": "drafts live in ZetaPrivate/notes/",
                                             "hn": "news.ycombinator.com/user?id=secret-notes"}))
        res = self.lint()
        hits = [f for f in res["findings"] if f.rule == "private-ref"]
        self.assertEqual([(f.severity, f.file) for f in hits], [("error", f"{PROFILE}/v/CHARACTER.yml")] * 3)
        self.assertEqual(sorted(f.message.split(" names")[0] for f in hits),
                         ["character.inherits[0]", "character.notes.where", "character.see_also[0]"])

    def test_private_layer_may_name_public_layers(self) -> None:
        self.put(BIO, "w", person("w", inherits=["moollm://github/SimHacker/WillWrightShowForFood/characters/w/"]))
        self.put(PROFILE, "w", person("w"))
        r = self.rules(self.lint(), "w")
        self.assertNotIn(("error", "private-ref"), r)
        self.assertNotIn(("warning", "relation-missing"), r)

    def test_private_layer_layer_kind_comes_from_private_repos_file(self) -> None:
        self.put(BIO, "k", person("k"))
        self.put("secret-notes/drafts", "k", person("k"))
        res = self.lint()
        self.assertEqual(sorted({l for f in res["findings"] for l in f.layers if f.id == "k"}),
                         ["biography", "private-other"])

    def test_consent_lives_in_the_public_layer(self) -> None:
        self.put(BIO, "c", person("c", inherits=["moollm://github/SimHacker/WillWrightShowForFood/characters/c/"],
                                  representation=rep(public_figure=False)))
        self.put(PROFILE, "c", person("c", representation=rep(public_figure=False, consent=GRANTED)))
        self.put(BIO, "d", person("d", representation=rep(consent={"state": "asked"})))
        self.put(PROFILE, "d", person("d"))
        res = self.lint()
        self.assertEqual(next(b["rule"] for b in res["beings"] if b["id"] == "c"), "consented")
        self.assertNotIn("consent-placement", [f.rule for f in res["findings"] if f.id == "c"])
        self.assertIn(("info", "consent-placement"), self.rules(res, "d"))


class ConsentVocabularyTests(LintCase):
    def test_interested_comes_from_the_schema_and_governs_nothing(self) -> None:
        schema = self.root / "REPRESENTATION.yml"
        schema.write_text(yaml.safe_dump({"schema": {"keys": {"consent": {"keys": {"state": {
            "values": ["not_asked", "asked", "interested", "granted", "declined", "revoked",
                       "unverified"]}}}}}}))
        states, _ = ll.load_consent_vocabulary(schema)
        self.assertIn("interested", states)
        saved = ll.STATES
        ll.STATES = states
        try:
            self.put(PROFILE, "i", person("i", representation=rep(public_figure=True,
                                                                  consent={"state": "interested"})))
            self.put(PROFILE, "j", person("j", representation=rep(public_figure=False,
                                                                  consent={"state": "interested"})))
            res = self.lint(["i", "j"])
        finally:
            ll.STATES = saved
        self.assertNotIn("consent-state-unknown", [f.rule for f in res["findings"]])
        self.assertEqual({b["id"]: b["rule"] for b in res["beings"]}, {"i": "public_figure", "j": "private"})

    def test_fallback_vocabulary_knows_interested(self) -> None:
        states, _ = ll.load_consent_vocabulary(self.root / "missing.yml")
        self.assertIn("interested", states)


class RealBeingDefaultTests(LintCase):
    def test_real_unless_fictional_in_every_layer(self) -> None:
        self.put(ADVENTURE, "plain", {"id": "plain", "name": "Plain"})
        self.put(CAST, "fic", {"id": "fic", "name": "Fic", "status": "fictional"})
        self.put(ADVENTURE, "no", {"id": "no", "name": "No", "real_being": False, "status": "living"})
        res = self.lint(["plain", "fic", "no"])
        self.assertEqual({b["id"]: b["real_being"] for b in res["beings"]},
                         {"plain": True, "fic": False, "no": False})

    def test_fictional_signifier_and_alias(self) -> None:
        self.put(ADVENTURE, "book", {"id": "book", "name": "Book", "status": "fictional", "signifier": "📖"})
        self.put(CAST, "book", {"id": "book", "name": "Book", "status": "fictional", "signifier": "🎭"})
        self.put(ADVENTURE, "bot", {"id": "bot", "name": "Bot", "status": "fictional", "type": "robot",
                                    "signifier": "👾"})
        self.put(CAST, "bot", {"id": "bot", "name": "Bot", "status": "fictional", "signifier": "🤖"})
        res = self.lint()
        sig = {(f.id, f.file): f.message for f in res["findings"] if f.rule == "signifier"}
        self.assertEqual(sorted(sig), [("book", f"{ADVENTURE}/book/CHARACTER.yml"),
                                       ("bot", f"{ADVENTURE}/bot/CHARACTER.yml")])
        self.assertIn("alias of 🎭", sig[("book", f"{ADVENTURE}/book/CHARACTER.yml")])
        self.assertIn("use 🤖", sig[("bot", f"{ADVENTURE}/bot/CHARACTER.yml")])

    def test_signifier_aliases_come_from_the_schema(self) -> None:
        schema = self.root / "CHARACTER.yml"
        schema.write_text(yaml.safe_dump({"schema": {"keys": {"signifier": {
            "value_aliases": {"📕": "🎭"}}}}}, allow_unicode=True))
        self.assertEqual(ll.load_signifier_aliases(schema), {"📕": "🎭"})
        self.assertEqual(ll.load_signifier_aliases(self.root / "missing.yml"), {"📖": "🎭"})


class CliTests(LintCase):
    def cli(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ll.main([*argv, "--root", str(self.root)])
        return code, out.getvalue(), err.getvalue()

    def test_text_yaml_summary_and_review(self) -> None:
        self.put(BIO, "b", person("b"))
        self.put(PROFILE, "b", person("b", representation=rep(public_figure=False)))
        self.put(BIO, "u", person("u", representation=rep()))
        review = self.root / "out" / "REVIEW.yml"
        code, out, _ = self.cli("--review", str(review))
        self.assertEqual(code, 1)
        self.assertIn("fact-public-figure", out)
        self.assertIn("rule:   public_figure", out)
        text = review.read_text()
        self.assertTrue(text.startswith("# Facts for Don to decide. Agents must not resolve them."))
        doc = yaml.safe_load(text)
        self.assertEqual([(i["id"], i["fact"]) for i in doc["items"]], [("b", "public_figure")])

        code, out, _ = self.cli("--summary")
        self.assertIn("public_figure unknown (1): u", out)
        self.assertIn("governing rule (2 real beings): memorial 0, self_authored 0, consented 0, "
                      "public_figure 1, private 1", out)

        code, out, _ = self.cli("--format", "yaml", "--summary")
        doc = yaml.safe_load(out)
        self.assertEqual(doc["summary"]["findings"]["error"], 1)
        self.assertEqual(doc["summary"]["governing_rules"]["private"], 1)
        self.assertNotIn("findings", {k for k in doc if k != "summary"})

        code, out, _ = self.cli("--format", "yaml")
        doc = yaml.safe_load(out)
        self.assertEqual({f["rule"] for f in doc["findings"] if f["severity"] == "error"},
                         {"fact-public-figure"})
        self.assertEqual({b["id"]: b["rule"] for b in doc["beings"]}, {"b": "public_figure", "u": "private"})

    def test_review_refuses_a_public_checkout(self) -> None:
        self.put(BIO, "b", person("b"))
        inside = self.root / "moollm" / "designs" / "REVIEW.yml"
        code, _, err = self.cli("--review", str(inside))
        self.assertEqual(code, 2)
        self.assertIn("public checkout", err)
        self.assertFalse(inside.exists())
        ok = self.root / "secret-notes" / "REVIEW.yml"
        self.cli("--review", str(ok))
        self.assertTrue(ok.exists())

    def test_clean_exit_zero(self) -> None:
        self.put(PROFILE, "c", person("c"))
        self.put(BIO, "c", person("c", derived_from="../../../WillWrightShowForFood/characters/c/"))
        code, out, _ = self.cli("--summary")
        self.assertEqual(code, 0)
        self.assertIn("error 0", out)


if __name__ == "__main__":
    unittest.main()
