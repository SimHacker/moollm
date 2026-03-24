#!/usr/bin/env python3
# Thin CLI: argparse + dispatch to lib.commands. Entry from skills/moo/moo.py.

import argparse
import os
import re
import sys

from . import config
from . import gh
from . import overlay
from . import urls
from .commands import focus as focus_cmds
from .commands import ls as ls_cmds
from .commands import read as read_cmds
from .commands import resolve as resolve_cmds
from .commands import repos as repos_cmds
from .commands import scan as scan_cmds
from .commands import sniff_cmd as sniff_cmds
from .commands import summarize_cmd as summarize_cmds
from .commands import write as write_cmds


def main():
    parser = argparse.ArgumentParser(
        description="moo — Moo VM CLI. GitHub branches as object storage.",
        epilog="Repos: moocroworld REPOS.yml. Cache: .moollm/skills/moo/cache/ (MOO_REPOS_FILE for REPOS path).",
    )
    parser.add_argument("--repo", default=os.environ.get("MOO_REPO"), help="repo (owner/name or alias)")
    parser.add_argument("--why", metavar="TEXT", help="Caller's reason for invoking (traceability; moo does not answer — use --help for command docs)")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("repos", help="List configured repos")

    resolve_p = sub.add_parser("resolve", help="Parse moorl (moo:// or moollm:// URL) to components (JSON)")
    resolve_p.add_argument("url", help="moorl (moo:// or moollm:// URL)")

    ls_p = sub.add_parser("ls", help="List branches (moos)")
    ls_p.add_argument("repo_pos", nargs="?", help="repo or alias")
    ls_p.add_argument("--type", dest="type_filter", help="Filter by ClassName prefix")
    ls_p.add_argument("--glance", action="store_true", help="Include GLANCE.yml summary")
    ls_p.add_argument("--all", action="store_true", help="Scan all configured repos")

    tree_p = sub.add_parser("tree", help="List files on a branch")
    tree_p.add_argument("repo_pos", nargs="?")
    tree_p.add_argument("branch")
    tree_p.add_argument("--recursive", "-r", action="store_true")

    read_p = sub.add_parser("read", help="Read a file or value; accepts repo/branch/path or a moorl")
    read_p.add_argument("targets", nargs="*", metavar="repo|url [branch] [path]",
                        help="Either one URL (moo:// or moollm://) or repo, branch, path")
    read_p.add_argument("--key", "-k", help="Extract YAML/JSON key (slash-separated path)")
    read_p.add_argument("-L", "--lines", metavar="START[-END]", help="Line range (1-based inclusive), e.g. 3 or 3-10")

    sniff_p = sub.add_parser("sniff", help="Extract smelly (structural) lines by file type; optional --depth, --max-lines, --max-chars")
    sniff_p.add_argument("targets", nargs="*", metavar="repo|url [branch] [path]",
                         help="Either one URL (moo:// or moollm://) or repo, branch, path")
    sniff_p.add_argument("--key", "-k", metavar="PATH", help="Extract sub-tree at slash path (e.g. payload/items); then skeleton (if dict/list) or smelly (if string)")
    sniff_p.add_argument("--depth", metavar="LEVEL", help="Max sniff depth: glance (1), structure (2), full (3); default structure")
    sniff_p.add_argument("--skeleton", action="store_true", help="Key-skeleton sniff: JSON/YAML only; keys + array lengths, no values (use with .json/.yml/.yaml)")
    sniff_p.add_argument("--skeleton-depth", type=int, metavar="N", dest="skeleton_depth", help="Max recursion depth for skeleton (default unlimited)")
    sniff_p.add_argument("--skeleton-format", choices=["text", "yaml", "json"], default="text", dest="skeleton_format", help="Skeleton output: text (compact lines), yaml, json")
    sniff_p.add_argument("--max-lines", type=int, metavar="N", help="Hard limit: emit at most N smelly lines")
    sniff_p.add_argument("--max-chars", type=int, metavar="N", help="Hard limit: emit at most N characters (from start of smelly output)")

    glance_p = sub.add_parser("glance", help="Read GLANCE.yml")
    glance_p.add_argument("repo_pos", nargs="?")
    glance_p.add_argument("branch")

    card_p = sub.add_parser("card", help="Read CARD.yml")
    card_p.add_argument("repo_pos", nargs="?")
    card_p.add_argument("branch")

    scan_p = sub.add_parser("scan", help="Scan moos, extract a key")
    scan_p.add_argument("repo_pos", nargs="?")
    scan_p.add_argument("--type", dest="type_filter", required=True)
    scan_p.add_argument("--key", "-k", required=True)
    scan_p.add_argument("--file", default="GLANCE.yml")
    scan_p.add_argument("--all", action="store_true", help="Scan all configured repos")

    write_p = sub.add_parser("write", help="Write a file to a branch")
    write_p.add_argument("repo_pos", nargs="?")
    write_p.add_argument("branch")
    write_p.add_argument("path")
    write_p.add_argument("content", nargs="?")
    write_p.add_argument("--file", dest="local_file")

    rm_p = sub.add_parser("rm", help="Delete a branch")
    rm_p.add_argument("repo_pos", nargs="?")
    rm_p.add_argument("branch")

    batch_glance_p = sub.add_parser("batch-glance", help="Batch glance: GLANCE.yml for each branch (optionally --type); use --all for all repos")
    batch_glance_p.add_argument("repo_pos", nargs="?", help="repo or alias")
    batch_glance_p.add_argument("--type", dest="type_filter", help="Branch name prefix (e.g. Issue)")
    batch_glance_p.add_argument("--all", action="store_true", help="All configured repos with default_type")

    summarize_p = sub.add_parser("summarize", help="LLM summary of a file (Gemini); caches under moo cache. Needs GEMINI_API_KEY and google-genai.")
    summarize_p.add_argument("targets", nargs="*", metavar="repo|url [branch] [path]",
                             help="Either one moorl or repo, branch, path")
    summarize_p.add_argument("--provider", default="gemini", help="LLM provider (default gemini)")
    summarize_p.add_argument("--model", metavar="NAME", help="Model name (e.g. gemini-2.0-flash)")
    summarize_p.add_argument("--no-cache", action="store_true", dest="no_cache", help="Skip cache, call LLM every time")

    focus_p = sub.add_parser("focus", help="Stare: fetch by attention-tree overlay (depth + at_depth + fragments)")
    focus_p.add_argument("overlay", nargs="?", help="Overlay YAML path (default: moocroworld ATTENTION-TREE.example.yml)")
    focus_p.add_argument("-o", "--output", choices=["text", "json"], default="text")
    focus_p.add_argument("-f", "--file", dest="overlay_file", help="Overlay file (same as positional)")

    args = parser.parse_args()
    why = getattr(args, "why", None)
    repos_config = config.load_repos()

    if args.command == "repos":
        repos_cmds.cmd_repos(repos_config, why=why)
        return

    if args.command == "focus":
        overlay_path = getattr(args, "overlay_file", None) or getattr(args, "overlay", None)
        if not overlay_path or not os.path.isfile(overlay_path):
            overlay_path = overlay.default_overlay_path()
        if not overlay_path or not overlay_path.exists():
            print("Overlay file not found. Pass path to overlay YAML or add skills/moocroworld/ATTENTION-TREE.example.yml.", file=sys.stderr)
            sys.exit(1)
        focus_cmds.cmd_focus(str(overlay_path), repos_config, output_json=(getattr(args, "output", "text") == "json"), why=why)
        return

    scan_all = getattr(args, "all", False)
    if scan_all:
        type_filter = getattr(args, "type_filter", None)
        show_glance = getattr(args, "glance", False)
        key = getattr(args, "key", None)
        file_name = getattr(args, "file", "GLANCE.yml")
        for alias, entry in repos_config.items():
            gh_repo = entry["github"]
            te = gh.get_token_env(entry)
            tf = type_filter or entry.get("default_type")
            if not tf:
                continue
            print(f"\n# {alias} ({gh_repo})")
            if args.command == "ls":
                ls_cmds.cmd_ls(gh_repo, tf, show_glance, token_env=te, why=why)
            elif args.command == "scan":
                scan_cmds.cmd_scan(gh_repo, tf, key, file_name, token_env=te, why=why)
            elif args.command == "batch-glance":
                focus_cmds.cmd_batch_glance(gh_repo, tf, token_env=te, repos_config=repos_config, why=why)
        return

    targets_default = getattr(args, "targets", []) or []
    repo_name = getattr(args, "repo_pos", None) or args.repo
    if not repo_name and args.command in ("read", "sniff", "summarize") and len(targets_default) == 3:
        repo_name = targets_default[0]
    read_url_only = args.command == "read" and len(targets_default) == 1 and urls.is_moo_url((targets_default or [None])[0])
    sniff_url_only = args.command == "sniff" and len(targets_default) == 1 and urls.is_moo_url((targets_default or [None])[0])
    summarize_url_only = args.command == "summarize" and len(targets_default) == 1 and urls.is_moo_url((targets_default or [None])[0])
    batch_glance_all = args.command == "batch-glance" and getattr(args, "all", False)
    no_repo_ok = args.command == "resolve" or read_url_only or sniff_url_only or summarize_url_only or batch_glance_all
    if not repo_name and not no_repo_ok:
        parser.error("repo required (positional, --repo, MOO_REPO, or --all)")
    if no_repo_ok:
        repo, repo_entry = None, None
    else:
        repo, repo_entry = config.resolve_repo(repo_name or "", repos_config)
        if not repo:
            parser.error(f"Unknown repo or alias: {repo_name}")
    te = gh.get_token_env(repo_entry) if repo_entry else None

    if args.command == "ls":
        tf = args.type_filter or (repo_entry.get("default_type") if repo_entry else None)
        ls_cmds.cmd_ls(repo, tf, args.glance, token_env=te, why=why)
    elif args.command == "tree":
        ls_cmds.cmd_tree(repo, args.branch, args.recursive, token_env=te, why=why)
    elif args.command == "resolve":
        resolve_cmds.cmd_resolve(args.url, repos_config, why=why)
        return
    elif args.command == "read":
        line_range = None
        if getattr(args, "lines", None):
            m = re.match(r"^(\d+)(?:-(\d+))?$", args.lines.strip())
            if m:
                line_range = (int(m.group(1)), int(m.group(2)) if m.group(2) else int(m.group(1)))
        targets = getattr(args, "targets", []) or []
        if len(targets) == 1 and urls.is_moo_url(targets[0]):
            u = urls.parse_moo_url(targets[0])
            if not u:
                print("Invalid moorl.", file=sys.stderr)
                sys.exit(1)
            rname = u["repo"] or args.repo or os.environ.get("MOO_REPO")
            if not rname:
                print("moorl (moo://) requires MOO_REPO or --repo.", file=sys.stderr)
                sys.exit(1)
            repo2, repo_entry2 = config.resolve_repo(rname, repos_config)
            if not repo2:
                print(f"Unknown repo: {rname}", file=sys.stderr)
                sys.exit(1)
            path_str, line_start, line_end = urls.parse_fragment(u.get("fragment", "") or "")
            key = path_str if path_str else args.key
            if line_start is not None and line_range is None:
                line_range = (line_start, line_end)
            read_cmds.cmd_read(repo2, u["branch"], u["path"] or "GLANCE.yml", key=key, line_range=line_range, token_env=gh.get_token_env(repo_entry2), why=why)
        elif len(targets) == 3:
            rname = targets[0] or args.repo
            if not rname:
                parser.error("repo required (positional, --repo, or MOO_REPO)")
            repo2, repo_entry2 = config.resolve_repo(rname, repos_config)
            if not repo2:
                parser.error(f"Unknown repo or alias: {rname}")
            read_cmds.cmd_read(repo2, targets[1], targets[2], key=args.key, line_range=line_range, token_env=gh.get_token_env(repo_entry2), why=why)
        else:
            parser.error("read requires either one moorl or three arguments: repo, branch, path")
        return
    elif args.command == "sniff":
        targets = getattr(args, "targets", []) or []
        key = getattr(args, "key", None)
        depth = getattr(args, "depth", None)
        max_lines = getattr(args, "max_lines", None)
        max_chars = getattr(args, "max_chars", None)
        skeleton = getattr(args, "skeleton", False)
        skeleton_depth = getattr(args, "skeleton_depth", None)
        skeleton_format = getattr(args, "skeleton_format", "text")
        if len(targets) == 1 and urls.is_moo_url(targets[0]):
            u = urls.parse_moo_url(targets[0])
            if not u:
                print("Invalid moorl.", file=sys.stderr)
                sys.exit(1)
            rname = u["repo"] or args.repo or os.environ.get("MOO_REPO")
            if not rname:
                print("moorl (moo://) requires MOO_REPO or --repo.", file=sys.stderr)
                sys.exit(1)
            repo2, repo_entry2 = config.resolve_repo(rname, repos_config)
            if not repo2:
                print(f"Unknown repo: {rname}", file=sys.stderr)
                sys.exit(1)
            path = u["path"] or "GLANCE.yml"
            sniff_cmds.cmd_sniff(repo2, u["branch"], path, key=key, depth=depth, max_lines=max_lines, max_chars=max_chars, skeleton=skeleton, skeleton_depth=skeleton_depth, skeleton_format=skeleton_format, token_env=gh.get_token_env(repo_entry2), why=why)
        elif len(targets) == 3:
            rname = targets[0] or args.repo
            if not rname:
                parser.error("repo required (positional, --repo, or MOO_REPO)")
            repo2, repo_entry2 = config.resolve_repo(rname, repos_config)
            if not repo2:
                parser.error(f"Unknown repo or alias: {rname}")
            sniff_cmds.cmd_sniff(repo2, targets[1], targets[2], key=key, depth=depth, max_lines=max_lines, max_chars=max_chars, skeleton=skeleton, skeleton_depth=skeleton_depth, skeleton_format=skeleton_format, token_env=gh.get_token_env(repo_entry2), why=why)
        else:
            parser.error("sniff requires either one moorl or three arguments: repo, branch, path")
        return
    elif args.command == "summarize":
        targets = getattr(args, "targets", []) or []
        provider = getattr(args, "provider", "gemini") or "gemini"
        model = getattr(args, "model", None)
        use_cache = not getattr(args, "no_cache", False)
        if len(targets) == 1 and urls.is_moo_url(targets[0]):
            u = urls.parse_moo_url(targets[0])
            if not u:
                print("Invalid moorl.", file=sys.stderr)
                sys.exit(1)
            rname = u["repo"] or args.repo or os.environ.get("MOO_REPO")
            if not rname:
                print("moorl (moo://) requires MOO_REPO or --repo.", file=sys.stderr)
                sys.exit(1)
            repo2, repo_entry2 = config.resolve_repo(rname, repos_config)
            if not repo2:
                print(f"Unknown repo: {rname}", file=sys.stderr)
                sys.exit(1)
            path = u["path"] or "GLANCE.yml"
            summarize_cmds.cmd_summarize(repo2, u["branch"], path, provider=provider, model=model, use_cache=use_cache, token_env=gh.get_token_env(repo_entry2), why=why)
        elif len(targets) == 3:
            rname = targets[0] or args.repo
            if not rname:
                parser.error("repo required (positional, --repo, or MOO_REPO)")
            repo2, repo_entry2 = config.resolve_repo(rname, repos_config)
            if not repo2:
                parser.error(f"Unknown repo or alias: {rname}")
            summarize_cmds.cmd_summarize(repo2, targets[1], targets[2], provider=provider, model=model, use_cache=use_cache, token_env=gh.get_token_env(repo_entry2), why=why)
        else:
            parser.error("summarize requires either one moorl or three arguments: repo, branch, path")
        return
    elif args.command == "glance":
        read_cmds.cmd_read(repo, args.branch, "GLANCE.yml", token_env=te, why=why)
    elif args.command == "card":
        read_cmds.cmd_read(repo, args.branch, "CARD.yml", token_env=te, why=why)
    elif args.command == "scan":
        tf = args.type_filter or (repo_entry.get("default_type") if repo_entry else None)
        scan_cmds.cmd_scan(repo, tf, args.key, args.file, token_env=te, why=why)
    elif args.command == "write":
        write_cmds.cmd_write(repo, args.branch, args.path, args.content, args.local_file, token_env=te, why=why)
    elif args.command == "rm":
        write_cmds.cmd_rm(repo, args.branch, token_env=te, why=why)
    elif args.command == "batch-glance":
        tf = getattr(args, "type_filter", None) or (repo_entry.get("default_type") if repo_entry else None)
        focus_cmds.cmd_batch_glance(repo, tf, token_env=te, repos_config=repos_config, why=why)
    else:
        parser.print_help()
