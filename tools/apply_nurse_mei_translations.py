#!/usr/bin/env python3
"""Apply a path→text translation map onto en.json and write a locale file.

Translation map JSON: list of {path, text} matching tools/nurse_mei_strings_en.json paths,
or a dict path→text.

Usage:
  python3 tools/apply_nurse_mei_translations.py id tools/translations/id.json
"""

from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path


def load_map(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return {str(k): str(v) for k, v in data.items()}
    if isinstance(data, list):
        out = {}
        for item in data:
            out[item["path"]] = item["text"]
        return out
    raise SystemExit("map must be list of {path,text} or dict")


def apply(en: dict, tmap: dict[str, str]) -> dict:
    loc = deepcopy(en)
    missing = []

    def need(path: str) -> str:
        if path not in tmap:
            missing.append(path)
            return None  # type: ignore
        return tmap[path]

    t = need("title")
    if t is not None:
        loc["title"] = t
    t = need("subtitle")
    if t is not None:
        loc["subtitle"] = t

    for n in loc["nodes"]:
        nid = n["id"]
        if "chapterTitle" in n:
            p = f"nodes[{nid}].chapterTitle"
            t = need(p)
            if t is not None:
                n["chapterTitle"] = t
        for li, _ in enumerate(n.get("lines") or []):
            p = f"nodes[{nid}].lines[{li}]"
            t = need(p)
            if t is not None:
                n["lines"][li] = t
        for ci, ch in enumerate(n.get("choices") or []):
            p = f"nodes[{nid}].choices[{ci}].label"
            t = need(p)
            if t is not None:
                ch["label"] = t
            if "me" in ch:
                p = f"nodes[{nid}].choices[{ci}].me"
                t = need(p)
                if t is not None:
                    ch["me"] = t
    if missing:
        print(f"WARNING: {len(missing)} paths missing from map (left as EN)")
        for p in missing[:20]:
            print(" ", p)
        if len(missing) > 20:
            print(f"  … +{len(missing)-20} more")
    return loc


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    lang = sys.argv[1]
    map_path = Path(sys.argv[2])
    root = Path(__file__).resolve().parents[1]
    en_path = root / "rp" / "nurse_mei" / "en.json"
    out_path = root / "rp" / "nurse_mei" / f"{lang}.json"
    en = json.loads(en_path.read_text(encoding="utf-8"))
    tmap = load_map(map_path)
    loc = apply(en, tmap)
    out_path.write_text(json.dumps(loc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
