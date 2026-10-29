#!/usr/bin/env python3
"""M12: retire `representation.consent_level`; fold `invitation.consent` into `representation.consent`.

The 1..5 number merged four facts. Each becomes its own key (skills/representation-ethics/
REPRESENTATION.yml), and the portrayal rule is computed from them:

    1  authored_by is the subject: nothing to write. authored_by naming someone else means
       the 1 was wrong; it is dropped and the invitation's state stands.
    2  consent.state: granted only with evidence on file; else the invitation's state when it
       has one; else unverified (an earlier record claimed consent, Don confirms).
    3  public_figure: true          4  public_figure: false
    5  status: deceased (added beside representation: when absent)

invitation.consent values map to consent.state (not_yet_asked -> not_asked, awaiting_reply ->
asked, ...); a value that is relationship context, not consent (warm_lead), becomes
state: unverified with the text kept verbatim in consent.note.

Skipped for hand edits: consent_level outside a representation: block, a level-5 layer whose
status says otherwise, level 1 with no authored_by, multi-line invitation.consent.

    python3 designs/object-system/tasks/migrations/m12_consent.py [--apply] [--diff] [--files PATH ...]
"""

from __future__ import annotations

import copy
import re
import sys
from pathlib import Path

from mlib import Result, Skip, block_end, header_lines, indent, is_content, private_character_repos, run, split_comment

LEVEL_KEYS = ("consent_level", "consent", "kind")
STATE = {
    "not_yet_asked": "not_asked", "not_addressed": "not_asked", "not_asked": "not_asked",
    "asked": "asked", "asked_no_reply_yet": "asked", "awaiting_reply": "asked",
    "pending_response": "asked", "outreach_sent_awaiting_reply": "asked", "collaborator_invited": "asked",
    "granted": "granted", "invitation_accepted": "granted",
    "declined": "declined", "revoked": "revoked",
}
LEVEL = {
    "self": 1, "self-sovereign": 1, "self_sovereign": 1, "1_self_sovereign": 1,
    "explicit": 2, "2_explicit": 2, "3_warm_contact": 3, "public_figure": 3,
    "private": 4, "memorial": 5, "deceased": 5, "5_deceased": 5, "5_deceased_legacy": 5,
}
EVIDENCE_KEYS = ("evidence", "accepted", "acceptance", "first_contact", "correspondence")
HEADER = re.compile(r"^# CONSENT LEVELS \(this character's level is in representation\.consent_level\):$")
NEW_HEADER = [
    "# PORTRAYAL RULE (computed from status, authored_by, consent, public_figure):",
    "#   memorial (deceased) · self-authored · consented (granted, with evidence) ·",
    "#   public figure (tradition/K-line) · private (fictional wrapper)",
]


def containers(data: dict) -> list[dict]:
    out = [data]
    if isinstance(data.get("character"), dict):
        out.append(data["character"])
    return out


def find(data: dict, key: str) -> tuple[dict | None, object]:
    for c in containers(data):
        if key in c:
            return c, c[key]
    return None, None


def level_of(rep: dict) -> tuple[int | None, str | None, str | None]:
    """(level, the key it was under, a consent state the old value implied)"""
    for k in LEVEL_KEYS:
        if k not in rep or isinstance(rep[k], dict):
            continue
        v = rep[k]
        if isinstance(v, int):
            return (v if 1 <= v <= 5 else None), k, None
        s = str(v).strip()
        if s in STATE:
            return None, k, STATE[s]
        if s.startswith("invited_"):
            return None, k, "asked"
        return LEVEL.get(s), k, None
    return None, None, None


def evidence_of(inv: dict) -> str | None:
    for k in EVIDENCE_KEYS:
        if isinstance(inv.get(k), str) and inv[k].strip():
            return inv[k].strip()
    return None


def transform(path: Path, text: str, data, args) -> Result:
    if not isinstance(data, dict):
        return Result(None)
    _, rep = find(data, "representation")
    if not isinstance(rep, dict):
        if find(data, "consent_level")[0] is not None:
            raise Skip("consent_level outside a representation: block")
        return Result(None)
    level, lkey, implied = level_of(rep)
    _, inv = find(data, "invitation")
    inv = inv if isinstance(inv, dict) else {}
    inv_raw = inv.get("consent")
    if lkey is None and inv_raw is None:
        return Result(None)
    if inv_raw is not None and not isinstance(inv_raw, str):
        raise Skip("invitation.consent is not a string")
    ident = (find(data, "id")[1] or path.parent.name)
    notes: list[str] = []

    consent: dict | None = None
    inv_state = None
    if isinstance(inv_raw, str):
        raw = inv_raw.strip()
        if raw == "not_applicable":
            inv_state = None
        elif raw in STATE:
            inv_state = {"state": STATE[raw]}
        else:
            inv_state = {"state": "unverified", "note": raw}
            notes.append("invitation.consent was relationship context; state unverified, text kept in consent.note")
        if inv_state and inv_state["state"] == "asked" and evidence_of(inv):
            inv_state["evidence"] = evidence_of(inv)
        if inv_state and inv_state["state"] == "granted":
            ev = evidence_of(inv)
            if ev:
                inv_state["evidence"] = ev
            else:
                inv_state = {"state": "unverified", "note": f"invitation.consent said {raw}; no evidence on file"}
                notes.append("granted with no evidence: unverified")
    if implied:
        consent = {"state": implied}
        m = re.match(r"invited_(\d{4}-\d{2}-\d{2})", str(rep.get(lkey)))
        if m:
            consent["date"] = m.group(1)
    public = None
    add_status = False
    authored = rep.get("authored_by")

    if level == 1:
        if authored is None:
            if ident == "don-hopkins":
                authored = ident
            else:
                raise Skip("level 1 with no authored_by")
        if authored != ident:
            notes.append("level 1 but authored_by is someone else: dropped")
        consent = consent or inv_state
    elif level == 2:
        if inv_state:
            consent = inv_state
            if inv_state["state"] != "granted":
                notes.append(f"level 2 dropped: the file's own invitation says {inv_raw}")
        else:
            consent = {"state": "unverified"}
            notes.append("level 2 with no evidence: unverified")
    elif level in (3, 4):
        public = level == 3
        consent = consent or inv_state
    elif level == 5:
        sc, status = find(data, "status")
        if status is not None and str(status) not in ("deceased", "memorial", "passed"):
            raise Skip(f"level 5 but status: {status}")
        add_status = status is None
        consent = consent or inv_state
    else:
        consent = consent or inv_state
        if lkey and not implied:
            notes.append(f"{lkey}: {rep.get(lkey)!r} maps to no fact; dropped")

    expected = copy.deepcopy(data)
    erep = find(expected, "representation")[1]
    if lkey:
        erep.pop(lkey)
    if public is not None:
        erep["public_figure"] = public
    if consent:
        erep["consent"] = consent
    if level == 1 and rep.get("authored_by") is None:
        erep["authored_by"] = authored
    einv = find(expected, "invitation")[1]
    if isinstance(einv, dict) and "consent" in einv:
        einv.pop("consent")
    if add_status:
        rc = next(c for c in containers(expected) if "representation" in c)
        rc["status"] = "deceased"

    lines = text.split("\n")
    out = list(lines)
    hs = header_lines(lines, "representation")
    if len(hs) != 1:
        raise Skip("not exactly one representation: header")
    h = hs[0]
    end = block_end(lines, h)
    body = [i for i in range(h + 1, end) if is_content(lines[i])]
    if not body:
        raise Skip("representation: is a flow map or empty")
    child = indent(lines[body[0]])
    pad = " " * child
    new: list[str] = []
    if public is not None:
        new.append(f"{pad}public_figure: {'true' if public else 'false'}")
    if level == 1 and rep.get("authored_by") is None:
        new.append(f"{pad}authored_by: {authored}")
    if consent:
        new.append(f"{pad}consent:")
        for k in ("state", "date", "evidence", "note"):
            if k in consent:
                new.append(f"{pad}  {k}: {yaml_scalar(consent[k])}")
    placed = False
    if lkey:
        for i in body:
            if indent(lines[i]) == child and re.match(rf"^\s*{lkey}\s*:", lines[i]):
                _, comment = split_comment(lines[i].split(":", 1)[1])
                comment = comment.strip() if comment else ""
                if new and comment:
                    new[0] = f"{new[0]}  # {comment}"
                elif comment:
                    new = [f"{pad}# {comment}"]
                out[i] = "\n".join(new) if new else None
                placed = True
                break
        if not placed:
            raise Skip(f"{lkey} not found as a single line in representation:")
    elif new:
        last = body[-1]
        while last + 1 < end and lines[last + 1].strip() and indent(lines[last + 1]) > child:
            last += 1
        out[last] = out[last] + "\n" + "\n".join(new)
    if add_status:
        out[h] = " " * indent(lines[h]) + "status: deceased\n" + (out[h] or "")
    if inv_raw is not None:
        ih = header_lines(lines, "invitation")
        if len(ih) != 1:
            raise Skip("not exactly one invitation: header")
        iend = block_end(lines, ih[0])
        ib = [i for i in range(ih[0] + 1, iend) if is_content(lines[i])]
        ichild = indent(lines[ib[0]])
        hit = [i for i in ib if indent(lines[i]) == ichild and re.match(r"^\s*consent\s*:", lines[i])]
        if len(hit) != 1:
            raise Skip("invitation.consent not found as one line")
        i = hit[0]
        if i + 1 < iend and lines[i + 1].strip() and indent(lines[i + 1]) > ichild:
            raise Skip("multi-line invitation.consent")
        out[i] = None
    for i, line in enumerate(lines):
        if HEADER.match(line) and i + 3 < len(lines):
            out[i:i + 4] = NEW_HEADER + [None]
            break
    return Result("\n".join(x for x in out if x is not None), expected, notes)


def yaml_scalar(v) -> str:
    s = str(v)
    if re.match(r"^[\w./-]+$", s) and s.lower() not in ("true", "false", "null", "yes", "no", "on", "off"):
        return s if not re.match(r"^\d{4}-\d{2}-\d{2}$", s) else f'"{s}"'
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


if __name__ == "__main__":
    sys.exit(run("m12_consent", __doc__, ["WillWrightShowForFood", "MicropolisCore", "moollm", "RepoShow", *private_character_repos()],
                 lambda b, p: p.name == "CHARACTER.yml" or "audience" in p.parts,
                 re.compile(r"consent_level|^\s*consent\s*:|^\s*kind\s*:\s*self", re.M), transform))
