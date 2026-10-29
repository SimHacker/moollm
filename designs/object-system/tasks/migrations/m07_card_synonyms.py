#!/usr/bin/env python3
"""M7: top-level synonyms in skills/*/CARD.yml, one row per run so each commit is one row.

  --row one_liner       one_liner: -> tagline:            (only where tagline: is absent)
  --row related_skills  related_skills: -> related:       (renamed, or its items appended to a
                                                           block-list related:, duplicates dropped)
  --row inherits_from   inherits_from: -> inherits:       (only where inherits: is absent)
  --row activates       activates: -> k_lines.activates   (k_lines map, the shape 43 of 45 cards
                                                           use) or appended to a k_lines list
  --row allowed_tools   report only: allowed_tools stays (a foreign spelling, SCHEMA "foreign
                                                           keys keep theirs"); lists the cards

Text edits at the top level only; comments on the moved lines move with them.

    python3 designs/object-system/tasks/migrations/m07_card_synonyms.py --row ROW [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys

import yaml

from mlib import Result, Skip, block_end, indent, is_content, run, skill_card, split_comment

ROWS = ("one_liner", "related_skills", "inherits_from", "activates", "allowed_tools")


def top(lines: list[str], key: str) -> int | None:
    hits = [i for i, ln in enumerate(lines) if re.match(rf"^{re.escape(key)}\s*:(\s|$)", ln)]
    if len(hits) > 1:
        raise Skip(f"{key}: appears twice at the top level")
    return hits[0] if hits else None


def rename_top(lines: list[str], old: str, new: str) -> list[str]:
    i = top(lines, old)
    out = list(lines)
    out[i] = re.sub(rf"^{re.escape(old)}(\s*):", rf"{new}\1:", lines[i], count=1)
    return out


def block_items(lines: list[str], i: int) -> tuple[int, list[str], int]:
    """(item indent, item lines including their continuation lines, block end) of a block list."""
    end = block_end(lines, i)
    body = lines[i + 1:end]
    content = [ln for ln in body if is_content(ln)]
    if not content or not content[0].lstrip().startswith("- "):
        raise Skip("not a block list")
    return indent(content[0]), body, end


def item_value(line: str):
    v, _ = split_comment(line.lstrip()[2:])
    try:
        return yaml.safe_load(v)
    except yaml.YAMLError:
        return object()


def one_liner(lines, data):
    if "tagline" in data:
        raise Skip("tagline already present (keep both, or drop one_liner by hand)")
    exp = {("tagline" if k == "one_liner" else k): v for k, v in data.items()}
    return rename_top(lines, "one_liner", "tagline"), exp


def inherits_from(lines, data):
    if "inherits" in data:
        raise Skip("inherits already present")
    exp = {("inherits" if k == "inherits_from" else k): v for k, v in data.items()}
    return rename_top(lines, "inherits_from", "inherits"), exp


def related_skills(lines, data):
    rs = data["related_skills"]
    if "related" not in data:
        exp = {("related" if k == "related_skills" else k): v for k, v in data.items()}
        return rename_top(lines, "related_skills", "related"), exp
    rel = data["related"]
    if not isinstance(rel, list) or not isinstance(rs, list):
        raise Skip("related or related_skills is not a list")
    exp = copy.deepcopy(data)
    del exp["related_skills"]
    exp["related"] = rel + [x for x in rs if x not in rel]
    r = top(lines, "related")
    s = top(lines, "related_skills")
    if re.match(r"^related\s*:\s*\[", lines[r]):
        raise Skip("related: is a flow list")
    ind, _, r_end = block_items(lines, r)
    if re.match(r"^related_skills\s*:\s*\[.*\]\s*(#.*)?$", lines[s]):
        val, comment = split_comment(lines[s].split(":", 1)[1])
        new_items = [" " * ind + "- " + yaml.safe_dump(x, default_flow_style=True, width=1000).strip().removesuffix("...").strip()
                     for x in rs if x not in rel]
        if comment:
            new_items = [" " * ind + "# " + comment] + new_items
        s_lines = (s, s + 1)
    else:
        s_ind, body, s_end = block_items(lines, s)
        if any(not ln.lstrip().startswith(("- ", "#")) for ln in body if ln.strip() and indent(ln) == s_ind):
            raise Skip("related_skills items are not simple list items")
        if any(is_content(ln) and indent(ln) > s_ind for ln in body):
            raise Skip("related_skills items span several lines")
        new_items = []
        for ln in body:
            if ln.strip() and is_content(ln) and item_value(ln) in rel:
                continue
            new_items.append(" " * ind + ln.lstrip() if ln.strip() else ln)
        while new_items and not new_items[-1].strip():
            new_items.pop()
        hc = split_comment(lines[s].split(":", 1)[1])[1]
        if hc:
            new_items = [" " * ind + "# " + hc] + new_items
        s_lines = (s, s_end)
    out = list(lines)
    a, b = s_lines
    if a > r:
        del out[a:b]
        if a < len(out) and a > 0 and not out[a - 1].strip() and not out[a].strip():
            del out[a]
        out[r_end:r_end] = new_items
    else:
        out[r_end:r_end] = new_items
        del out[a:b]
        if a < len(out) and a > 0 and not out[a - 1].strip() and not out[a].strip():
            del out[a]
    return out, exp


def activates(lines, data):
    act = data["activates"]
    exp = copy.deepcopy(data)
    del exp["activates"]
    a = top(lines, "activates")
    a_end = block_end(lines, a)
    while a_end > a + 1 and not lines[a_end - 1].strip():
        a_end -= 1
    seg = lines[a:a_end]
    kl = data.get("k_lines", "<absent>")
    k = top(lines, "k_lines")
    out = list(lines)
    if kl == "<absent>" or (kl is None and k is not None and re.match(r"^k_lines\s*:\s*(#.*)?$", lines[k])
                            and k + 1 == a):
        exp["k_lines"] = {"activates": act}
        moved = ["  " + ln if ln.strip() else ln for ln in seg]
        if kl == "<absent>":
            out[a:a_end] = ["k_lines:"] + moved
        else:
            out[a:a_end] = moved
        return out, exp
    if isinstance(kl, dict):
        if "activates" in kl:
            raise Skip("k_lines.activates already present")
        exp["k_lines"] = {**kl, "activates": act}
        k_end = block_end(lines, k)
        child = next(indent(ln) for ln in lines[k + 1:k_end] if is_content(ln))
        moved = [" " * child + ln if ln.strip() else ln for ln in seg]
        if a > k:
            del out[a:a_end]
            out[k_end:k_end] = moved
        else:
            out[k_end:k_end] = moved
            del out[a:a_end]
        return out, exp
    if isinstance(kl, list) and isinstance(act, list):
        exp["k_lines"] = kl + [x for x in act if x not in kl]
        raise Skip("k_lines is a list: append by hand (1 card)")
    raise Skip(f"k_lines has shape {type(kl).__name__}")


def allowed_tools(lines, data):
    return None, None


FN = {"one_liner": one_liner, "related_skills": related_skills, "inherits_from": inherits_from,
      "activates": activates, "allowed_tools": allowed_tools}


def transform(path, text, data, args):
    if not isinstance(data, dict) or args.row not in data:
        return Result(None)
    if args.row == "allowed_tools":
        has_tools = "tools" in data
        return Result(None, notes=[f"allowed_tools present (left as is){'; tools: also present' if has_tools else ''}"])
    lines, exp = FN[args.row](text.split("\n"), data)
    notes = []
    if args.row == "related_skills" and any(isinstance(x, dict) for x in data["related_skills"]):
        notes.append("related_skills items are maps {id: why}; related: entries elsewhere use {ref, relation}")
    if args.row == "activates" and "k_lines" in data and data["k_lines"] is None:
        notes.append("empty k_lines: followed by column-0 activates:; check whether the next "
                     "top-level keys were meant under k_lines too")
    if args.row == "inherits_from" and data["inherits_from"] is None:
        notes.append("inherits_from: null becomes inherits: null (could be dropped)")
    return Result("\n".join(lines), exp, notes)


def add_args(ap):
    ap.add_argument("--row", choices=ROWS, required=True)


if __name__ == "__main__":
    sys.exit(run("m07_card_synonyms", __doc__, ["moollm"], skill_card, None, transform, add_args))
