#!/usr/bin/env python3
"""Enforce the rules in NAMING_RULES.md. Exit 1 on any violation.

Usage:  python3 rp/validate_rp.py
CI:     run from the repo root on every push that touches rp/**
"""
import json
import os
import sys

RP = os.path.dirname(os.path.abspath(__file__))
IMG = (".webp", ".png", ".jpg", ".jpeg")
VID = (".mkv", ".mp4")
SLOTS = ("rp_cover", "bg_cover", "rp_trending")

errors = []
warnings = []


def err(rule, msg):
    errors.append(f"[{rule}] {msg}")


def warn(msg):
    warnings.append(f"[warn] {msg}")


manifest_path = os.path.join(RP, "rp_lists.json")
with open(manifest_path) as f:
    manifest = json.load(f)

if manifest.get("version") != 2:
    err("manifest", "rp_lists.json must declare \"version\": 2")

listed = {s["id"]: s for s in manifest.get("stories", [])}
on_disk = {
    d for d in os.listdir(RP)
    if os.path.isdir(os.path.join(RP, d)) and not d.startswith(".")
}

# A folder that exists but isn't listed is content that ships to nobody.
for d in sorted(on_disk - set(listed)):
    warn(f"{d}/ exists on disk but is not in rp_lists.json — unreachable content")

for sid in sorted(listed):
    s = listed[sid]
    folder = os.path.join(RP, sid)

    # R1 — one folder per story, named for the id.
    if sid not in on_disk:
        err("R1", f"{sid} is listed in rp_lists.json but has no folder")
        continue
    if "folder" in s:
        err("R1", f"{sid}: manifest must not carry a 'folder' field (folder == id)")

    # R2 — exactly one story file, named for the story, English only.
    story = s.get("story")
    if story != f"{sid}.json":
        err("R2", f"{sid}: story must be \"{sid}.json\", got {story!r}")
    elif not os.path.exists(os.path.join(folder, story)):
        err("R2", f"{sid}: {story} is missing from disk")
    for stale in ("en.json", "hi.json", "id.json", "pt.json", "ru.json"):
        if os.path.exists(os.path.join(folder, stale)):
            warn(f"{sid}/{stale} still present — legacy, remove once no consumer reads it")

    # R3/R4/R5 + R6 — slot naming, and a video slot must ship a still.
    for slot, img_key, vid_key, required in (
        ("rp_cover", "cover", "coverVideo", True),
        ("bg_cover", "bg", "bgVideo", True),
        ("rp_trending", "trending", "trendingVideo", False),
    ):
        img, vid = s.get(img_key), s.get(vid_key)

        if required and not img:
            err("R6", f"{sid}: {slot} still is mandatory, manifest has {img_key}=null")
        if vid and not img:
            err("R6", f"{sid}: has {vid} but no {slot} still")

        for name, exts, key in ((img, IMG, img_key), (vid, VID, vid_key)):
            if not name:
                continue
            if not name.startswith(slot + "."):
                err("R3/R4/R5", f"{sid}: {key}={name!r} must be named {slot}.<ext>")
            if not name.lower().endswith(exts):
                err("R8", f"{sid}: {key}={name!r} has an unexpected extension")
            if not os.path.exists(os.path.join(folder, name)):
                err("R8", f"{sid}: manifest points at {name}, which is not on disk")

    # A video file present on disk that the manifest never names is ambiguity.
    for slot in SLOTS:
        for e in VID + IMG:
            fn = slot + e
            if not os.path.exists(os.path.join(folder, fn)):
                continue
            if fn not in (s.get("cover"), s.get("coverVideo"), s.get("bg"),
                          s.get("bgVideo"), s.get("trending"), s.get("trendingVideo")):
                err("R8", f"{sid}: {fn} exists on disk but no manifest field names it")

    # R10 — no absolute URLs in story content.
    story_file = os.path.join(folder, f"{sid}.json")
    if os.path.exists(story_file):
        with open(story_file) as f:
            raw = f.read()
        if "linkit-links.github.io" in raw:
            n = raw.count("linkit-links.github.io")
            err("R10", f"{sid}: {n} absolute CDN URLs in {sid}.json — must be relative filenames")

        # Every media URL a chapter references must actually exist.
        nodes = json.loads(raw).get("nodes", [])
        missing = set()
        for node in nodes:
            for key in ("imageUrl", "videoUrl"):
                u = node.get(key)
                if not u:
                    continue
                # R10: these are filenames relative to the story folder.
                name = u.rsplit("/", 1)[-1]
                if not os.path.exists(os.path.join(folder, name)):
                    missing.add(name)
        for name in sorted(missing):
            err("content", f"{sid}: chapter references {name}, which is not on disk")

print(f"checked {len(listed)} stories in rp_lists.json")
for w in warnings:
    print(w)
for e in errors:
    print(e)
print()
if errors:
    print(f"FAIL — {len(errors)} violation(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"PASS — 0 violations, {len(warnings)} warning(s)")
