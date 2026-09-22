#!/usr/bin/env python3
"""Add a visible page-1 correction notice overlay to a prestored PDF.

Reads a YAML or JSON config (--config) and/or CLI flags. The founding-case config
lives at designs/prestoration/sources/notice.yml.

Usage:
  python3 pdf_add_correction_notice.py INPUT.pdf OUTPUT.pdf --config notice.yml

  python3 pdf_add_correction_notice.py INPUT.pdf OUTPUT.pdf \\
    --label "CORRECTED EDITION - September 2026" \\
    --body-file notice-body.txt \\
    --original-sha256 a5a91c1d... \\
    --change-list changes.txt

Config fields (all overridable on CLI):
  label                  Bold first line on page 1
  body                   Full notice prose (wrapped); alternative to template fields
  not_version_of_record  DOI, publisher id, or free text
  changes                What was updated on this edition
  standing               Wish / standing citation
  original_repo          Where the unaltered original is preserved
  original_file          Path to original (sha256 computed if original_sha256 omitted)
  original_sha256        Pin for the unaltered original
  attachment_ref         e.g. "Full change list attached"
  canonical_fix          Publisher/registry correction in progress
  change_list_file       Embedded attachment (path relative to config file)
  docinfo_note           PDF /Note metadata (auto-generated if omitted)
  layout.placement       top | bottom (default top)
  layout.margin          pt (default 72)
  layout.font_size       pt (default 7.5)
  layout.leading         pt (default 9.5)
  layout.wrap_width      chars (default 88)
  layout.y_top           pt baseline for first line when placement=top
  layout.y_base          pt baseline for last line when placement=bottom
"""

from __future__ import annotations

import argparse
import hashlib
import json
import textwrap
from pathlib import Path
from typing import Any

import pikepdf
from pikepdf import Dictionary, Name, Stream

DEFAULT_LAYOUT = {
    "placement": "top",
    "margin": 72.0,
    "font_size": 7.5,
    "leading": 9.5,
    "wrap_width": 88,
    "y_top": 748.0,
    "y_base": 108.0,
}


def load_config(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ImportError:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError(f"config must be a mapping: {path}")
    return data


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_sha256(cfg: dict[str, Any], config_dir: Path) -> str | None:
    if cfg.get("original_sha256"):
        return str(cfg["original_sha256"]).lower()
    rel = cfg.get("original_file")
    if not rel:
        return None
    original = (config_dir / rel).resolve()
    if not original.is_file():
        raise FileNotFoundError(f"original_file not found: {original}")
    return sha256_file(original)


def compose_body(cfg: dict[str, Any], sha256: str | None) -> str:
    if cfg.get("body"):
        return str(cfg["body"]).strip()

    parts: list[str] = []
    if cfg.get("not_version_of_record"):
        parts.append(f"Not the version of record ({cfg['not_version_of_record']}).")
    if cfg.get("changes"):
        parts.append(str(cfg["changes"]) + ".")
    if cfg.get("standing"):
        parts.append(f"Per {cfg['standing']}.")
    if cfg.get("original_repo") or sha256:
        repo = cfg.get("original_repo", "")
        hash_bit = f" (SHA-256 {sha256[:16]}...)" if sha256 else ""
        if repo:
            parts.append(f"Unaltered original: {repo}{hash_bit}.")
        elif sha256:
            parts.append(f"Unaltered original SHA-256: {sha256}.")
    if cfg.get("attachment_ref"):
        parts.append(str(cfg["attachment_ref"]) + ".")
    if cfg.get("canonical_fix"):
        parts.append(str(cfg["canonical_fix"]) + ".")
    if not parts:
        raise ValueError("config needs body or template fields (not_version_of_record, changes, ...)")
    return " ".join(parts)


def notice_lines(cfg: dict[str, Any], sha256: str | None) -> list[str]:
    label = str(cfg["label"]).strip()
    layout = {**DEFAULT_LAYOUT, **(cfg.get("layout") or {})}
    body = compose_body(cfg, sha256)
    wrapped = textwrap.wrap(body, width=int(layout["wrap_width"]))
    return [label, *wrapped]


def compose_docinfo_note(cfg: dict[str, Any], sha256: str | None) -> str:
    if cfg.get("docinfo_note"):
        return str(cfg["docinfo_note"]).strip()
    label = str(cfg.get("label", "Corrected edition")).strip()
    changes = cfg.get("changes") or "see page-1 notice"
    bits = [f"{label}: visible page-1 notice; {changes}."]
    if sha256:
        bits.append(f"Original preserved (SHA-256 {sha256}).")
    if cfg.get("change_list_file"):
        bits.append("Full change list attached.")
    return " ".join(bits)


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_overlay(lines: list[str], layout: dict[str, Any]) -> bytes:
    margin = float(layout["margin"])
    font_size = float(layout["font_size"])
    leading = float(layout["leading"])
    placement = layout["placement"]
    parts: list[str] = ["q"]

    if placement == "top":
        y_top = float(layout["y_top"])
        rule_y = y_top - len(lines) * leading - 4.0
        parts += [
            "0.25 w",
            "0 0 0 RG",
            f"{margin} {rule_y} m",
            f"{612 - margin} {rule_y} l",
            "S",
            "BT",
            f"{leading} TL",
        ]
        for i, line in enumerate(lines):
            font = "/HelvB" if i == 0 else "/HelvN"
            y = y_top - i * leading
            parts += [
                f"{font} {font_size} Tf",
                f"1 0 0 1 {margin} {y} Tm",
                f"({pdf_escape(line)}) Tj",
            ]
    elif placement == "bottom":
        y_base = float(layout["y_base"])
        parts += ["BT", f"{leading} TL"]
        y = y_base + (len(lines) - 1) * leading
        for i, line in enumerate(lines):
            font = "/HelvB" if i == 0 else "/HelvN"
            parts += [
                f"{font} {font_size} Tf",
                f"1 0 0 1 {margin} {y} Tm",
                f"({pdf_escape(line)}) Tj",
            ]
            y -= leading
    else:
        raise ValueError(f"unknown layout.placement: {placement}")

    parts += ["ET", "Q"]
    return "\n".join(parts).encode("latin-1", errors="replace")


def ensure_fonts(page: pikepdf.Page) -> None:
    resources = page.get("/Resources", Dictionary())
    fonts = resources.get("/Font", Dictionary())
    fonts["/HelvN"] = Dictionary(
        {
            "/Type": Name.Font,
            "/Subtype": Name.Type1,
            "/BaseFont": Name.Helvetica,
        }
    )
    fonts["/HelvB"] = Dictionary(
        {
            "/Type": Name.Font,
            "/Subtype": Name.Type1,
            "/BaseFont": Name("/Helvetica-Bold"),
        }
    )
    resources["/Font"] = fonts
    page["/Resources"] = resources


def append_overlay(page: pikepdf.Page, pdf: pikepdf.Pdf, overlay: bytes) -> None:
    stream = Stream(pdf, overlay)
    contents = page.Contents
    if isinstance(contents, pikepdf.Array):
        page.Contents = pikepdf.Array([*contents, stream])
    else:
        page.Contents = pikepdf.Array([contents, stream])


def attach_file(pdf: pikepdf.Pdf, path: Path, name: str | None = None) -> None:
    attachment_name = name or path.name
    pdf.attachments[attachment_name] = path.read_bytes()


def merge_config(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    out = {**base}
    for key, value in overrides.items():
        if value is None:
            continue
        if key == "layout" and isinstance(value, dict):
            out["layout"] = {**(out.get("layout") or {}), **value}
        else:
            out[key] = value
    return out


def add_notice(
    input_path: Path,
    output_path: Path,
    cfg: dict[str, Any],
    *,
    config_dir: Path,
    attach: bool,
) -> None:
    layout = {**DEFAULT_LAYOUT, **(cfg.get("layout") or {})}
    sha256 = resolve_sha256(cfg, config_dir)
    lines = notice_lines(cfg, sha256)
    overlay = build_overlay(lines, layout)
    note = compose_docinfo_note(cfg, sha256)

    with pikepdf.open(input_path) as pdf:
        page = pdf.pages[0]
        ensure_fonts(page)
        append_overlay(page, pdf, overlay)
        pdf.docinfo["/Note"] = note
        if attach and cfg.get("change_list_file"):
            cl_path = (config_dir / cfg["change_list_file"]).resolve()
            if not cl_path.is_file():
                raise FileNotFoundError(f"change_list_file not found: {cl_path}")
            attach_file(pdf, cl_path)
        pdf.save(output_path)


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--config", type=Path, help="YAML or JSON notice config")
    p.add_argument("--label", help="Bold first line (overrides config)")
    p.add_argument("--body", help="Notice prose (overrides config body and template fields)")
    p.add_argument("--body-file", type=Path, help="Notice prose from file")
    p.add_argument("--not-version-of-record")
    p.add_argument("--changes")
    p.add_argument("--standing")
    p.add_argument("--original-repo")
    p.add_argument("--original-file", type=Path, help="Compute sha256 from this file")
    p.add_argument("--original-sha256")
    p.add_argument("--attachment-ref")
    p.add_argument("--canonical-fix")
    p.add_argument("--change-list", type=Path, dest="change_list_file")
    p.add_argument("--docinfo-note")
    p.add_argument("--placement", choices=("top", "bottom"))
    p.add_argument("--no-attach", action="store_true")
    return p


def main() -> None:
    args = build_arg_parser().parse_args()
    config_dir = Path.cwd()
    cfg: dict[str, Any] = {}

    if args.config:
        config_dir = args.config.parent.resolve()
        cfg = load_config(args.config)

    overrides = {
        "label": args.label,
        "body": args.body,
        "not_version_of_record": args.not_version_of_record,
        "changes": args.changes,
        "standing": args.standing,
        "original_repo": args.original_repo,
        "original_file": str(args.original_file) if args.original_file else None,
        "original_sha256": args.original_sha256,
        "attachment_ref": args.attachment_ref,
        "canonical_fix": args.canonical_fix,
        "change_list_file": str(args.change_list_file) if args.change_list_file else None,
        "docinfo_note": args.docinfo_note,
    }
    if args.body_file:
        overrides["body"] = args.body_file.read_text(encoding="utf-8").strip()
    if args.placement:
        overrides["layout"] = {"placement": args.placement}

    cfg = merge_config(cfg, overrides)
    if not cfg.get("label"):
        raise SystemExit("error: --label or config.label is required")

    if args.original_file and not cfg.get("original_file"):
        cfg["original_file"] = str(args.original_file)

    add_notice(
        Path(args.input),
        Path(args.output),
        cfg,
        config_dir=config_dir,
        attach=not args.no_attach,
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
