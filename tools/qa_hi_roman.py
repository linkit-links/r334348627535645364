#!/usr/bin/env python3
"""QA for Correct Roman Hindi RP files."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DEV = re.compile(r"[\u0900-\u097F]")
TU = re.compile(r"\b(tu|tera|teri|tujhe|tujh)\b", re.I)
BAD = re.compile(r"\b(vorn|haimar|adhyay)\b", re.I)


def main() -> int:
    paths = sys.argv[1:] or [str(p) for p in Path("rp").rglob("hi.json")]
    fatal = 0
    for raw in paths:
        p = Path(raw)
        text = p.read_text(encoding="utf-8")
        n_dev = len(DEV.findall(text))
        tu = TU.findall(text)
        bad = BAD.findall(text)
        print(f"{p}: dev={n_dev} tu-forms={len(tu)} ban={bad}")
        if n_dev:
            fatal += 1
        if bad:
            fatal += 1
    return 1 if fatal else 0


if __name__ == "__main__":
    raise SystemExit(main())
