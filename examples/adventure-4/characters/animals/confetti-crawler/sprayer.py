#!/usr/bin/env python3
"""
worm-emoji-fordite.py

Sprays emoji "snow" onto comment-safe positions in text/YAML files using a
Moveable Feast–style random window strategy. Defaults to in-place operation but
can read stdin / write stdout. Comments and code are left intact; emojis append
only to lines that already contain comment markers or are blank.
"""

import argparse
import random
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set


DEFAULT_EMOJIS = list("✨🌈🪩🎨❄️🧊🌀🧭🪄🧱🪆")
EMOJI_RE = re.compile(
    r"[\U0001F300-\U0001FAFF\U0001F1E6-\U0001F1FF\u2600-\u26FF\u2700-\u27BF]"
)


def filter_emojis(chars: Iterable[str]) -> List[str]:
    return [c for c in chars if EMOJI_RE.fullmatch(c)]


def vlog(verbose: bool, msg: str) -> None:
    if verbose:
        print(msg)


def load_palette(args: argparse.Namespace) -> List[str]:
    if args.emoji_map_file:
        emoji_map = load_emoji_map(Path(args.emoji_map_file))
        if args.theme and args.theme in emoji_map:
            themed = filter_emojis(emoji_map[args.theme])
            if themed:
                return themed
        # fall back to concat of all categories
        all_concat = "".join(emoji_map.values())
        filtered_all = filter_emojis(all_concat)
        if filtered_all:
            return filtered_all
    if args.palette_file:
        raw = "".join(Path(args.palette_file).read_text().splitlines())
        filtered = filter_emojis(raw)
        if filtered:
            return filtered
    if args.palette:
        filtered = filter_emojis(list(args.palette))
        if filtered:
            return filtered
    return DEFAULT_EMOJIS


def load_emoji_map(path: Path) -> Dict[str, str]:
    """
    Read emojis.txt with k-line headers (# name) and following emoji lines.
    Blank lines ignored. Returns map of name -> concatenated emoji string.
    """
    emoji_map: Dict[str, str] = {}
    current: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "":
            continue
        if stripped.startswith("#"):
            current = stripped.lstrip("#").strip()
            emoji_map.setdefault(current, "")
            continue
        if current is None:
            continue
        emoji_map[current] += stripped
    return emoji_map


def choose_windows(n_lines: int, window_sizes: Sequence[int]) -> List[tuple[int, int]]:
    """Pick non-overlapping windows with roughly even spacing."""
    starts = list(range(n_lines))
    random.shuffle(starts)
    occupied: Set[int] = set()
    windows: List[tuple[int, int]] = []
    for start in starts:
        size = random.choice(window_sizes)
        span = range(start, min(start + size, n_lines))
        if any(i in occupied for i in span):
            continue
        windows.append((start, size))
        occupied.update(span)
    return windows


def line_is_commenty(line: str, comment_prefix: str) -> bool:
    if comment_prefix == "":
        return True
    stripped = line.lstrip()
    return stripped.startswith(comment_prefix) or stripped == ""


def split_comment(line: str, comment_prefix: str):
    """Return (prefix, marker, body, newline) or None if no comment marker. If comment_prefix is empty, treat whole line as body."""
    nl = "\n" if line.endswith("\n") else ""
    base = line.rstrip("\n")
    if comment_prefix == "":
        return "", "", base, nl
    idx = base.find(comment_prefix)
    if idx == -1:
        return None
    marker = comment_prefix
    prefix = base[:idx].rstrip()
    body = base[idx + len(marker) :].lstrip()
    return prefix, marker, body, nl


def pop_one_emoji(body: str, allow: set[str] | None = None) -> tuple[str, str] | None:
    """Remove the topmost (rightmost) allowed emoji from body, return (emoji, new_body)."""
    for pos in range(len(body) - 1, -1, -1):
        ch = body[pos]
        if EMOJI_RE.fullmatch(ch) and (allow is None or ch in allow):
            return ch, body[:pos] + body[pos + 1 :]
    return None


def count_emojis(body: str) -> int:
    return sum(1 for ch in body if EMOJI_RE.fullmatch(ch))


def trim_emojis_to(body: str, target: int) -> str:
    """Remove emojis so that at most `target` remain; preserve order of non-emoji."""
    if target < 0:
        target = 0
    emojis = [i for i, ch in enumerate(body) if EMOJI_RE.fullmatch(ch)]
    if len(emojis) <= target:
        return body
    to_remove = len(emojis) - target
    out_chars: List[str] = []
    removed = 0
    for ch in body:
        if EMOJI_RE.fullmatch(ch) and removed < to_remove:
            removed += 1
            continue
        out_chars.append(ch)
    return "".join(out_chars).rstrip()


def append_emoji_to_body(body: str, emoji: str) -> str:
    if body.strip() == "":
        return emoji
    emoji_only = all((EMOJI_RE.fullmatch(ch) or ch.isspace()) for ch in body)
    if emoji_only:
        clean = "".join(ch for ch in body if EMOJI_RE.fullmatch(ch))
        return f"{clean}{emoji}"
    return (body.rstrip() + " " + emoji).strip()


def find_block_scalar_lines(lines: List[str], comment_prefix: str) -> Set[int]:
    """
    Identify lines belonging to block scalars (| or >) so we avoid placing emojis there.
    """
    if comment_prefix == "":
        return set()
    blocked: Set[int] = set()
    in_block = False
    block_indent = 0
    for i, ln in enumerate(lines):
        raw = ln.rstrip("\n")
        if in_block:
            leading = len(raw) - len(raw.lstrip(" "))
            if leading > block_indent:
                blocked.add(i)
                continue
            else:
                in_block = False
        # strip trailing comment part to reduce false positives
        code_part = raw.split("#", 1)[0]
        if re.search(r":[ \t]*[>|] *$", code_part) or re.match(r"[ \t]*[>|] *$", code_part.strip()):
            in_block = True
            block_indent = len(raw) - len(raw.lstrip(" "))
            blocked.add(i)
    return blocked


def collect_comment_sites(lines: List[str], blocked: Set[int], comment_prefix: str) -> List[int]:
    """Depth-first (top-to-bottom) collection of line indices that can host emojis."""
    if comment_prefix == "":
        return list(range(len(lines)))
    return [i for i, ln in enumerate(lines) if i not in blocked and line_is_commenty(ln, comment_prefix)]


def append_emojis(line: str, palette: Sequence[str], max_per_pass: int, comment_prefix: str) -> str:
    if not palette:
        return line
    count = random.randint(1, max_per_pass)
    emojis = "".join(random.choices(palette, k=count))
    newline = "\n" if line.endswith("\n") else ""
    parsed = split_comment(line, comment_prefix)
    if parsed:
        prefix, marker, body, _ = parsed
        emoji_only = all((EMOJI_RE.fullmatch(ch) or ch.isspace()) for ch in body)
        if emoji_only:
            body_clean = "".join(ch for ch in body if EMOJI_RE.fullmatch(ch))
            new_body = f"{body_clean}{emojis}"
        else:
            new_body = f"{body.rstrip()} {emojis}"
        if comment_prefix == "":
            return f"{new_body}{newline}"
        prefix_part = prefix.rstrip()
        sep = " " if prefix_part else ""
        return f"{prefix_part}{sep}{marker} {new_body}{newline}"
    core = line.rstrip("\n")
    if core.strip() == "":
        if comment_prefix == "":
            return f"{emojis}{newline}"
        return f"{comment_prefix} {emojis}{newline}"
    if comment_prefix == "":
        return f"{core} {emojis}{newline}"
    return f"{core} {comment_prefix} {emojis}{newline}"


def apply_pass(
    lines: List[str],
    palette: Sequence[str],
    max_per_pass: int,
    mode: str,
    drift_radius: int,
    drift_prob: float,
    blocked: Set[int],
    verbose: bool,
    comment_prefix: str,
) -> List[str]:
    sites = collect_comment_sites(lines, blocked, comment_prefix)
    if not sites:
        return lines

    def spray_at(idx: int) -> None:
        target = idx
        if drift_radius > 0 and random.random() < drift_prob:
            start = max(0, idx - drift_radius)
            end = min(len(lines), idx + drift_radius + 1)
            candidates = [i for i in range(start, end) if line_is_commenty(lines[i], comment_prefix)]
            if candidates:
                target = random.choice(candidates)
        vlog(verbose, f"[spray] mode={mode} idx={idx} -> target={target}")
        lines[target] = append_emojis(lines[target], palette, max_per_pass, comment_prefix)

    if mode == "serial":
        for idx in sites:
            spray_at(idx)
        return lines

    # mfm: one random site per iteration call (iteration count controls total applications)
    idx = random.choice(sites)
    vlog(verbose, f"[mfm] choose site={idx}/{len(sites)}")
    spray_at(idx)
    return lines


def run(
    input_text: str,
    iterations: int,
    palette: Sequence[str],
    max_per_pass: int,
    mode: str,
    drift_radius: int,
    drift_prob: float,
    erode: bool,
    verbose: bool,
    comment_prefix: str,
) -> str:
    lines = input_text.splitlines(keepends=True)
    if not lines:
        vlog(verbose, "[info] empty input; nothing to do")
        return input_text
    blocked = find_block_scalar_lines(lines, comment_prefix)
    if erode:
        lines = erode_runs(lines, iterations, drift_radius, blocked, verbose, allow=set(palette), comment_prefix=comment_prefix)
    else:
        for _ in range(iterations):
            lines = apply_pass(lines, palette, max_per_pass, mode, drift_radius, drift_prob, blocked, verbose, comment_prefix)
    return "".join(lines)


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Emoji fordite sprayer with Moveable Feast windows.")
    p.add_argument("-i", "--input", help="Input file (default: stdin if none).")
    p.add_argument("-o", "--output", help="Output file (default: overwrite input, else stdout).")
    p.add_argument("--iterations", "-n", type=int, default=1, help="Number of spray/erode iterations.")
    p.add_argument("--palette", "-p", help="String of emojis to sample from (e.g., '✨🌈❄️'). Non-emoji chars are ignored.")
    p.add_argument("--palette-file", help="File containing emojis to sample from (raw chars; newlines ignored).")
    p.add_argument("--emoji-map-file", help="emojis.txt with category headers (# name) and emoji lines.")
    p.add_argument("--theme", help="Use emojis from a named category in emoji-map-file; falls back to all.")
    p.add_argument("--max-per-pass", "-m", type=int, default=4, help="Max emojis appended per touched line.")
    p.add_argument("--drift-radius", type=int, default=0, help="Max line distance to drift (0 disables drift).")
    p.add_argument("--drift-prob", type=float, default=0.0, help="Probability of drifting per placement (0 disables).")
    p.add_argument("--seed", type=int, help="Random seed for reproducibility.")
    p.add_argument("--strip", action="store_true", help="Strip emoji comments instead of spraying.")
    p.add_argument("--strip-mode", choices=["all", "serial", "mfm"], default="all", help="Strip strategy: all=blow away emojis; serial=trim all sites to min depth; mfm=random sites per iteration.")
    p.add_argument("--strip-min-depth", type=int, default=0, help="Minimum emoji depth to preserve when stripping.")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logging of actions.")
    p.add_argument("--erode", action="store_true", help="Move existing emojis downward; do not create new ones.")
    p.add_argument("--comment-prefix", default="#", help="Comment prefix to target (use '' for raw text).")
    p.add_argument(
        "--mode",
        choices=["mfm", "serial"],
        default="mfm",
        help="Execution model: mfm=random non-overlapping windows; serial=top-to-bottom every line.",
    )
    return p.parse_args(argv)


def strip_line(line: str, min_depth: int, comment_prefix: str) -> str:
    nl = "\n" if line.endswith("\n") else ""
    content = line.rstrip("\n")
    parsed = split_comment(line, comment_prefix)
    if not parsed:
        return line
    prefix, marker, body, _ = parsed
    depth = count_emojis(body)
    if depth <= min_depth:
        return line
    new_body = trim_emojis_to(body, min_depth)
    if new_body.strip() == "":
        return ""
    prefix_part = prefix.rstrip()
    if comment_prefix == "":
        return f"{new_body}{nl}"
    sep = " " if prefix_part else ""
    return f"{prefix_part}{sep}{marker} {new_body}{nl}"


def strip_text(text: str, mode: str, iterations: int, min_depth: int, verbose: bool, comment_prefix: str) -> str:
    lines = text.splitlines(keepends=True)
    blocked = find_block_scalar_lines(lines, comment_prefix)
    sites = collect_comment_sites(lines, blocked, comment_prefix)
    if not sites:
        vlog(verbose, "[strip] no comment sites; nothing to strip")

    def strip_site(idx: int):
        new_line = strip_line(lines[idx], min_depth, comment_prefix)
        lines[idx] = new_line if new_line.endswith("\n") else new_line
        vlog(verbose, f"[strip:{mode}] idx={idx} depth>={min_depth}")

    if mode == "all":
        for idx in sites:
            lines[idx] = strip_line(lines[idx], 0)
    elif mode == "serial":
        for idx in sites:
            lines[idx] = strip_line(lines[idx], min_depth)
    elif mode == "mfm":
        for _ in range(iterations):
            candidates = []
            for i in sites:
                parsed = split_comment(lines[i])
                if not parsed:
                    continue
                _, _, body, _ = parsed
                if count_emojis(body) > min_depth:
                    candidates.append(i)
            if not candidates:
                break
            idx = random.choice(candidates)
            lines[idx] = strip_line(lines[idx], min_depth)
            vlog(verbose, f"[strip:mfm] idx={idx} depth>={min_depth}")
    return "".join(lines)


def erode_runs(
    lines: List[str],
    iterations: int,
    drift_radius: int,
    blocked: Set[int],
    verbose: bool,
    allow: set[str] | None,
    comment_prefix: str,
) -> List[str]:
    comment_sites = collect_comment_sites(lines, blocked, comment_prefix)
    if not comment_sites:
        vlog(verbose, "[erode] no comment sites; nothing to move")
        return lines

    def has_emoji(idx: int) -> bool:
        parsed = split_comment(lines[idx], comment_prefix)
        if not parsed:
            return False
        _, marker, body, _ = parsed
        return marker and EMOJI_RE.search(body) is not None

    for _ in range(iterations):
        candidates = [idx for idx in comment_sites if has_emoji(idx)]
        if not candidates:
            break
        src = random.choice(candidates)
        parsed = split_comment(lines[src], comment_prefix)
        if not parsed:
            continue
        prefix, marker, body, nl = parsed
        popped = pop_one_emoji(body, allow)
        if not popped:
            continue
        emoji, new_body = popped
        # choose downhill target within drift_radius
        lower_sites = [i for i in comment_sites if i > src and i <= src + drift_radius] if drift_radius > 0 else []
        if not lower_sites:
            lower_sites = [src]
        tgt = random.choice(lower_sites)
        t_parsed = split_comment(lines[tgt], comment_prefix)
        if not t_parsed:
            # target is blank or missing marker; leave it unchanged
            tgt_prefix, tgt_marker, tgt_body, tgt_nl = "", "#", "", "\n" if lines[tgt].endswith("\n") else ""
        else:
            tgt_prefix, tgt_marker, tgt_body, tgt_nl = t_parsed

        # rebuild source
        if new_body.strip() == "":
            lines[src] = f"{prefix}{nl}"
        else:
            lines[src] = (f"{prefix} {marker} {new_body}{nl}").strip() + nl
        # rebuild target with moved emoji
        tgt_body_new = append_emoji_to_body(tgt_body, emoji)
        prefix_part = f"{tgt_prefix} " if tgt_prefix else ""
        lines[tgt] = f"{prefix_part}{tgt_marker} {tgt_body_new}{tgt_nl}"
        vlog(verbose, f"[erode] src={src} -> tgt={tgt} emoji={emoji}")
    return lines

# TODO: diffuse mode (not implemented yet)
# Idea: treat comment-emoji clusters as "lakes" and randomly swap/shuffle emojis
# within small neighborhoods (e.g., 2x2 or Margolus-style blocks) to stir pools
# without creating/destroying emojis. This would operate after spray, similar
# to a diffusion/annealing pass, using PRNG for swaps and optional radius/stride.


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.seed is not None:
        random.seed(args.seed)
    palette = load_palette(args)
    emoji_map = None
    if args.emoji_map_file:
        try:
            emoji_map = load_emoji_map(Path(args.emoji_map_file))
        except Exception as exc:
            vlog(args.verbose, f"[warn] failed to load emoji map: {exc}")
            emoji_map = None

    if args.input:
        input_path = Path(args.input)
        input_text = input_path.read_text(encoding="utf-8")
    else:
        input_text = sys.stdin.read()

    if args.strip:
        output_text = strip_text(
            text=input_text,
            mode=args.strip_mode,
            iterations=args.iterations,
            min_depth=args.strip_min_depth,
            verbose=args.verbose,
            comment_prefix=args.comment_prefix,
        )
    elif args.erode:
        output_text = run(
            input_text=input_text,
            iterations=args.iterations,
            palette=palette,
            max_per_pass=args.max_per_pass,
            mode=args.mode,
            drift_radius=args.drift_radius,
            drift_prob=args.drift_prob,
            erode=True,
            verbose=args.verbose,
            comment_prefix=args.comment_prefix,
        )
    else:
        output_text = run(
            input_text=input_text,
            iterations=args.iterations,
            palette=palette,
            max_per_pass=args.max_per_pass,
            mode=args.mode,
            drift_radius=args.drift_radius,
            drift_prob=args.drift_prob,
            erode=False,
            verbose=args.verbose,
            comment_prefix=args.comment_prefix,
        )

    if args.output == "-":
        sys.stdout.write(output_text)
    elif args.output:
        Path(args.output).write_text(output_text, encoding="utf-8")
    elif args.input:
        Path(args.input).write_text(output_text, encoding="utf-8")
    else:
        sys.stdout.write(output_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
