#!/usr/bin/env python3
"""quora_harvest.py — drive your own logged-in Chrome to archive Quora threads.

Why CDP attach instead of a fresh headless browser: Quora requires a session for
most content, and the session you are entitled to is the one already in your
browser. Attaching reuses it without exporting cookies to disk, and every request
comes from the browser you were reading in anyway.

Setup (once per session), quit Chrome first, then:

    /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome \\
        --remote-debugging-port=9222

Then:

    pip install playwright && playwright install    # once, ever
    python3 quora_harvest.py urls path/to/urls.txt --out ../../../harvest
    python3 quora_harvest.py profile Alan-Kay-11 --out ../../../harvest --limit 50

Each answer lands as one Markdown file plus one JSON sidecar. Already-harvested
URLs are skipped, so interrupting and rerunning resumes.

The expansion and extraction logic lives in quora-extract.js, injected into each
page. This file is the driver: navigation, pacing, and files on disk.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXTRACTOR = HERE / "quora-extract.js"

ANSWER_HREF = re.compile(r"^https://www\.quora\.com/[^/]+/answer/[^/?#]+")


def slugify(url: str) -> str:
    """One stable filename per answer URL: question slug + author slug."""
    tail = url.split("quora.com/", 1)[-1]
    tail = tail.split("?", 1)[0].split("#", 1)[0].strip("/")
    parts = [p for p in tail.split("/") if p and p != "answer"]
    slug = "--".join(parts)
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", slug).strip("-")
    return slug[:180] or "quora-page"


def attach(playwright, port: int):
    browser = playwright.chromium.connect_over_cdp(f"http://localhost:{port}")
    if not browser.contexts:
        raise SystemExit(
            f"Attached to Chrome on :{port} but it has no browsing context. "
            "Open a tab and try again."
        )
    return browser, browser.contexts[0]


def harvest_one(context, url: str, out_dir: Path, settle_ms: int) -> dict:
    page = context.new_page()
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_timeout(settle_ms)
        page.add_script_tag(path=str(EXTRACTOR))
        record = page.evaluate("() => window.__quoraHarvest()")
        markdown = page.evaluate("(rec) => window.__quoraToMarkdown(rec)", record)
    finally:
        page.close()

    stem = slugify(url)
    (out_dir / f"{stem}.md").write_text(markdown, encoding="utf-8")
    (out_dir / f"{stem}.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return record


def collect_profile_answers(context, profile: str, limit: int, settle_ms: int) -> list[str]:
    """Scroll a profile's answers tab, collecting answer URLs as they mount."""
    page = context.new_page()
    urls: list[str] = []
    seen: set[str] = set()
    try:
        page.goto(
            f"https://www.quora.com/profile/{profile}/answers",
            wait_until="domcontentloaded",
            timeout=60_000,
        )
        page.wait_for_timeout(settle_ms)
        stalls = 0
        while len(urls) < limit and stalls < 6:
            found = page.eval_on_selector_all(
                'a[href*="/answer/"]', "els => els.map(e => e.href)"
            )
            before = len(urls)
            for href in found:
                clean = href.split("?", 1)[0]
                if ANSWER_HREF.match(clean) and clean not in seen:
                    seen.add(clean)
                    urls.append(clean)
                    if len(urls) >= limit:
                        break
            stalls = stalls + 1 if len(urls) == before else 0
            page.mouse.wheel(0, 4000)
            page.wait_for_timeout(settle_ms)
    finally:
        page.close()
    return urls[:limit]


def run(args) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Needs Playwright: pip install playwright && playwright install", file=sys.stderr)
        return 2

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser, context = attach(playwright, args.port)

        if args.mode == "profile":
            urls = collect_profile_answers(context, args.target, args.limit, args.settle)
            index = out_dir / f"{args.target}-answer-urls.txt"
            index.write_text("\n".join(urls) + "\n", encoding="utf-8")
            print(f"{len(urls)} answer URLs -> {index}")
        else:
            source = Path(args.target).expanduser()
            urls = [
                line.strip()
                for line in source.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.startswith("#")
            ][: args.limit]

        done = failed = skipped = 0
        for i, url in enumerate(urls, 1):
            target = out_dir / f"{slugify(url)}.md"
            if target.exists() and not args.force:
                skipped += 1
                continue
            print(f"[{i}/{len(urls)}] {url}")
            try:
                record = harvest_one(context, url, out_dir, args.settle)
                rounds = record.get("expansion", {}).get("rounds")
                clicks = len(record.get("expansion", {}).get("clicked", []))
                print(
                    f"    {len(record.get('comments', []))} comments · "
                    f"{clicks} folds opened in {rounds} rounds -> {target.name}"
                )
                done += 1
            except Exception as err:
                # Keep going: a walled garden will hand you an occasional wall.
                print(f"    FAILED: {err}", file=sys.stderr)
                failed += 1
            if i < len(urls):
                time.sleep(args.delay)

        browser.close()
        print(f"\n{done} harvested, {skipped} already present, {failed} failed -> {out_dir}")
    return 1 if failed and not done else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("mode", choices=["urls", "profile"])
    parser.add_argument("target", help="path to a URL list, or a profile slug like Alan-Kay-11")
    parser.add_argument("--out", default="./harvest", help="output directory")
    parser.add_argument("--port", type=int, default=9222, help="Chrome remote debugging port")
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--delay", type=float, default=3.0, help="seconds between pages")
    parser.add_argument("--settle", type=int, default=1200, help="ms to wait after navigation")
    parser.add_argument("--force", action="store_true", help="re-harvest pages already on disk")
    return run(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
