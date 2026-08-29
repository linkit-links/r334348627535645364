#!/usr/bin/env python3
"""Apply a Sasha translation overlay onto en.json and write a locale file."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "rp" / "sasha_secret_agent" / "en.json"
OUT_DIR = ROOT / "rp" / "sasha_secret_agent"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def apply(en: dict, overlay: dict) -> dict:
    out = copy.deepcopy(en)
    if "title" not in overlay or "subtitle" not in overlay:
        raise SystemExit("overlay missing title/subtitle")
    out["title"] = overlay["title"]
    out["subtitle"] = overlay["subtitle"]
    nodes_t = overlay.get("nodes") or {}
    en_ids = [n["id"] for n in en["nodes"]]
    if set(nodes_t) != set(en_ids):
        missing = sorted(set(en_ids) - set(nodes_t))
        extra = sorted(set(nodes_t) - set(en_ids))
        raise SystemExit(f"node set mismatch missing={missing[:8]} extra={extra[:8]}")
    for n in out["nodes"]:
        nid = n["id"]
        t = nodes_t[nid]
        if "chapterTitle" in n:
            if not t.get("chapterTitle"):
                raise SystemExit(f"{nid}: missing chapterTitle")
            n["chapterTitle"] = t["chapterTitle"]
        elif t.get("chapterTitle"):
            raise SystemExit(f"{nid}: unexpected chapterTitle")
        if "lines" in n:
            if "lines" not in t or len(t["lines"]) != len(n["lines"]):
                raise SystemExit(
                    f"{nid}: lines {len(t.get('lines') or [])} != EN {len(n['lines'])}"
                )
            for i, s in enumerate(t["lines"]):
                if not isinstance(s, str) or not s.strip():
                    raise SystemExit(f"{nid}.lines[{i}] empty")
            n["lines"] = t["lines"]
        if n.get("choices"):
            tc = t.get("choices") or []
            if len(tc) != len(n["choices"]):
                raise SystemExit(f"{nid}: choices {len(tc)} != EN {len(n['choices'])}")
            for i, c in enumerate(n["choices"]):
                lab = tc[i].get("label")
                if not isinstance(lab, str) or not lab.strip():
                    raise SystemExit(f"{nid}.choices[{i}].label empty")
                c["label"] = lab
                if "me" in c:
                    me = tc[i].get("me")
                    if not isinstance(me, str) or not me.strip():
                        raise SystemExit(f"{nid}.choices[{i}].me empty")
                    c["me"] = me
                elif "me" in tc[i]:
                    raise SystemExit(f"{nid}.choices[{i}] unexpected me")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("overlay", type=Path)
    ap.add_argument("locale")
    args = ap.parse_args()
    en = load(EN_PATH)
    overlay = load(args.overlay)
    out = apply(en, overlay)
    dest = OUT_DIR / f"{args.locale}.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
