#!/usr/bin/env python3
"""Structural parity check: EN RP JSON vs a locale file.

Usage:
  python3 tools/validate_rp_locale.py rp/captured_princess_elara/en.json rp/captured_princess_elara/id.json
  python3 tools/validate_rp_locale.py rp/captured_princess_elara/en.json --all
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


LOCK_TOP = ("id", "start", "emoji", "video")
LOCK_NODE = ("id", "next", "speaker", "chapterStart", "videoUrl", "imageUrl")


def load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def node_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {n["id"]: n for n in data.get("nodes", [])}


def check_empty_strings(obj: Any, path: str, out: list[str]) -> None:
    if isinstance(obj, str):
        if obj.strip() == "":
            out.append(f"empty string at {path}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            check_empty_strings(v, f"{path}[{i}]", out)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            check_empty_strings(v, f"{path}.{k}", out)


def ascii_ratio(s: str) -> float:
    if not s:
        return 0.0
    ascii_letters = sum(1 for c in s if ("A" <= c <= "Z") or ("a" <= c <= "z"))
    return ascii_letters / max(len(s), 1)


def leftover_english_heuristic(
    en_s: str, loc_s: str, locale: str, path: str, out: list[str]
) -> None:
    """Flag likely untranslated lines for non-Latin-heavy locales."""
    if locale not in ("id", "ru", "hi"):
        return
    # Skip pure names / short tokens
    if len(loc_s) < 12:
        return
    # Identical to EN (except allowed proper nouns only lines) is suspicious
    if loc_s.strip() == en_s.strip() and re.search(r"[a-zA-Z]{4,}", loc_s):
        # Allow if mostly names
        stripped = re.sub(
            r"\b(Elara|Liora|Vance|Valdere|Mei)\b", "", loc_s, flags=re.I
        )
        if re.search(r"[A-Za-z]{5,}", stripped):
            out.append(f"possible untranslated (identical to EN) at {path}")
            return
    if locale in ("ru", "hi") and ascii_ratio(loc_s) > 0.55:
        out.append(
            f"high ASCII ratio ({ascii_ratio(loc_s):.2f}) at {path}: {loc_s[:60]!r}..."
        )


def validate(en: dict[str, Any], loc: dict[str, Any], locale_code: str) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []

    for k in LOCK_TOP:
        if k in en and en.get(k) != loc.get(k):
            errors.append(f"top-level locked field mismatch: {k}")

    en_nodes = node_map(en)
    loc_nodes = node_map(loc)

    en_ids = set(en_nodes)
    loc_ids = set(loc_nodes)
    if en_ids != loc_ids:
        missing = sorted(en_ids - loc_ids)
        extra = sorted(loc_ids - en_ids)
        if missing:
            errors.append(f"missing nodes ({len(missing)}): {missing[:10]}...")
        if extra:
            errors.append(f"extra nodes ({len(extra)}): {extra[:10]}...")

    for nid in sorted(en_ids & loc_ids):
        a, b = en_nodes[nid], loc_nodes[nid]
        for k in LOCK_NODE:
            if a.get(k) != b.get(k):
                errors.append(f"{nid}: locked field {k!r} differs")

        en_lines = a.get("lines") or []
        loc_lines = b.get("lines") or []
        if len(en_lines) != len(loc_lines):
            errors.append(
                f"{nid}: lines count {len(loc_lines)} != EN {len(en_lines)}"
            )
        else:
            for i, (el, ll) in enumerate(zip(en_lines, loc_lines)):
                if not isinstance(ll, str):
                    errors.append(f"{nid}.lines[{i}] not a string")
                    continue
                leftover_english_heuristic(
                    el, ll, locale_code, f"{nid}.lines[{i}]", warnings
                )
                # emphasis marker count
                if el.count("*") != ll.count("*"):
                    warnings.append(
                        f"{nid}.lines[{i}]: * count EN={el.count('*')} loc={ll.count('*')}"
                    )

        if ("chapterTitle" in a) != ("chapterTitle" in b):
            errors.append(f"{nid}: chapterTitle presence mismatch")
        elif "chapterTitle" in a and not b.get("chapterTitle"):
            errors.append(f"{nid}: empty chapterTitle")

        en_ch = a.get("choices") or []
        loc_ch = b.get("choices") or []
        if len(en_ch) != len(loc_ch):
            errors.append(
                f"{nid}: choices count {len(loc_ch)} != EN {len(en_ch)}"
            )
        else:
            for i, (ec, lc) in enumerate(zip(en_ch, loc_ch)):
                if ec.get("next") != lc.get("next"):
                    errors.append(f"{nid}.choices[{i}].next mismatch")
                if ec.get("set") != lc.get("set"):
                    errors.append(f"{nid}.choices[{i}].set mismatch")
                if ("me" in ec) != ("me" in lc):
                    errors.append(f"{nid}.choices[{i}].me presence mismatch")
                elif "me" in ec and not str(lc.get("me", "")).strip():
                    errors.append(f"{nid}.choices[{i}].me empty")
                if not str(lc.get("label", "")).strip() and "label" in ec:
                    errors.append(f"{nid}.choices[{i}].label empty")

    # required translated top fields present
    for field in ("title", "subtitle"):
        if not str(loc.get(field, "")).strip():
            errors.append(f"missing top-level {field}")

    check_empty_strings(loc.get("title"), "title", errors)
    check_empty_strings(loc.get("subtitle"), "subtitle", errors)

    # report warnings as non-fatal
    return errors, warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate RP locale vs EN")
    ap.add_argument("en_json", type=Path, help="Path to en.json")
    ap.add_argument(
        "locale_json",
        type=Path,
        nargs="?",
        help="Path to locale json (omit with --all)",
    )
    ap.add_argument(
        "--all",
        action="store_true",
        help="Validate all sibling *.json except en.json",
    )
    args = ap.parse_args()

    en_path: Path = args.en_json
    if not en_path.is_file():
        print(f"EN file not found: {en_path}", file=sys.stderr)
        return 2

    en = load(en_path)
    targets: list[Path] = []
    if args.all:
        targets = sorted(
            p
            for p in en_path.parent.glob("*.json")
            if p.name != en_path.name and p.name != "captured_princess_elara.json"
        )
        if not targets:
            print("No locale json files found next to EN")
            return 1
    elif args.locale_json:
        targets = [args.locale_json]
    else:
        print("Provide locale_json or --all", file=sys.stderr)
        return 2

    fatal = 0
    for t in targets:
        if not t.is_file():
            print(f"FAIL {t}: not found")
            fatal += 1
            continue
        loc = load(t)
        code = t.stem
        errors, warnings = validate(en, loc, code)
        if errors:
            print(f"FAIL {t} ({len(errors)} errors, {len(warnings)} warnings)")
            for e in errors[:40]:
                print(f"  ERROR: {e}")
            if len(errors) > 40:
                print(f"  ... +{len(errors) - 40} more errors")
            fatal += 1
        else:
            print(f"OK   {t} ({len(warnings)} warnings)")
        for w in warnings[:20]:
            print(f"  WARN: {w}")
        if len(warnings) > 20:
            print(f"  ... +{len(warnings) - 20} more warnings")

    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
