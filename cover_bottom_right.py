#!/usr/bin/env python3
"""Draw a 110x60 black rectangle on the bottom-right of images and videos.

Usage:
    python cover_bottom_right.py <input>              # file: overwrite in place
    python cover_bottom_right.py <input> -o <output>  # file: write to a new path
    python cover_bottom_right.py <dir>                # media in that directory
    python cover_bottom_right.py <dir> -r             # recurse into subdirectories
    python cover_bottom_right.py . -r                 # whole repo
    python cover_bottom_right.py . -r --force         # re-cover even if already black
    python cover_bottom_right.py . -r -j 4            # parallel jobs (default: 4)

Images use Pillow (lossy WebP quality 85 by default). Videos use ffmpeg
and match the source bitrate so files stay near their original size.
Requires: pip install Pillow   and   ffmpeg on PATH
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow is required. Install it with: pip install Pillow")

RECT_W = 110
RECT_H = 60
IMAGE_EXTENSIONS = {".webp", ".png", ".jpg", ".jpeg"}
VIDEO_EXTENSIONS = {".mkv", ".mp4", ".webm", ".mov"}
MEDIA_EXTENSIONS = IMAGE_EXTENSIONS | VIDEO_EXTENSIONS
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".grok"}
BLACK_MAX = 8  # max channel value to treat a pixel as "already black"


def which_ffmpeg() -> str:
    path = shutil.which("ffmpeg")
    if not path:
        sys.exit("ffmpeg is required on PATH to cover videos.")
    return path


def source_video_bitrate(path: Path) -> int | None:
    """Return the source video bitrate in bps, or None if it cannot be probed."""
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return None
    try:
        data = json.loads(
            subprocess.check_output(
                [
                    ffprobe,
                    "-v",
                    "error",
                    "-show_entries",
                    "format=bit_rate",
                    "-show_entries",
                    "stream=codec_type,bit_rate",
                    "-of",
                    "json",
                    str(path),
                ]
            )
        )
    except (subprocess.CalledProcessError, json.JSONDecodeError, ValueError):
        return None

    fmt_br = int((data.get("format") or {}).get("bit_rate") or 0)
    audio_br = 0
    for stream in data.get("streams") or []:
        if stream.get("codec_type") == "audio" and stream.get("bit_rate"):
            audio_br += int(stream["bit_rate"])
    video_br = fmt_br - audio_br if fmt_br > audio_br else fmt_br
    return video_br if video_br >= 100_000 else None


def cover_image(src: Path, dest: Path, *, lossless: bool, webp_quality: int) -> None:
    with Image.open(src) as img:
        work = img.copy()
        draw = ImageDraw.Draw(work)
        left = max(0, work.width - RECT_W)
        top = max(0, work.height - RECT_H)
        fill = (
            0
            if work.mode in ("L", "1")
            else (0, 0, 0, 255)
            if work.mode in ("RGBA", "LA")
            else (0, 0, 0)
        )
        draw.rectangle([left, top, work.width, work.height], fill=fill)

        save_kwargs: dict = {}
        suffix = dest.suffix.lower()
        if suffix == ".webp":
            if lossless:
                save_kwargs = {"format": "WEBP", "lossless": True, "quality": 100, "method": 6}
            else:
                save_kwargs = {"format": "WEBP", "quality": webp_quality, "method": 6}
        elif suffix in {".jpg", ".jpeg"}:
            if work.mode in ("RGBA", "LA", "P"):
                work = work.convert("RGB")
            save_kwargs = {"format": "JPEG", "quality": 95}
        elif suffix == ".png":
            save_kwargs = {"format": "PNG"}

        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.resolve() == Path(src).resolve():
            tmp = dest.with_name(f".{dest.name}.tmp{dest.suffix}")
            work.save(tmp, **save_kwargs)
            tmp.replace(dest)
        else:
            work.save(dest, **save_kwargs)


def _video_cmd(
    ffmpeg: str,
    src: Path,
    tmp: Path,
    dest: Path,
    *,
    audio: str,
    bitrate: int | None,
    crf: int | None,
) -> list[str]:
    vf = (
        f"drawbox=x=iw-{RECT_W}:y=ih-{RECT_H}:w={RECT_W}:h={RECT_H}:color=black:t=fill"
    )
    cmd = [
        ffmpeg,
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(src),
        "-vf",
        vf,
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-pix_fmt",
        "yuv420p",
    ]
    if bitrate:
        cmd += ["-b:v", str(bitrate), "-maxrate", str(bitrate), "-bufsize", str(bitrate * 2)]
    else:
        cmd += ["-crf", str(crf if crf is not None else 23)]
    if audio == "copy":
        cmd += ["-c:a", "copy"]
    else:
        cmd += ["-c:a", "aac", "-b:a", "128k"]
    cmd += ["-map_metadata", "0"]
    if dest.suffix.lower() == ".mp4":
        cmd += ["-movflags", "+faststart"]
    cmd.append(str(tmp))
    return cmd


def cover_video(
    src: Path,
    dest: Path,
    ffmpeg: str,
    *,
    crf: int | None = None,
) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(f".{dest.name}.tmp{dest.suffix}")
    bitrate = None if crf is not None else source_video_bitrate(src)

    try:
        subprocess.run(
            _video_cmd(ffmpeg, src, tmp, dest, audio="copy", bitrate=bitrate, crf=crf),
            check=True,
        )
    except subprocess.CalledProcessError:
        if tmp.exists():
            tmp.unlink()
        subprocess.run(
            _video_cmd(ffmpeg, src, tmp, dest, audio="aac", bitrate=bitrate, crf=crf),
            check=True,
        )

    tmp.replace(dest)


def _region_is_black(img: Image.Image) -> bool:
    w, h = img.size
    if w < 1 or h < 1:
        return False
    left = max(0, w - RECT_W)
    top = max(0, h - RECT_H)
    region = img.convert("RGB").crop((left, top, w, h))
    extrema = region.getextrema()
    return all(mx <= BLACK_MAX for _mn, mx in extrema)


def already_covered_image(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            return _region_is_black(img)
    except Exception:
        return False


def already_covered_video(path: Path, ffmpeg: str) -> bool:
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        cmd = [
            ffmpeg,
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(path),
            "-frames:v",
            "1",
            str(tmp_path),
        ]
        subprocess.run(cmd, check=True)
        with Image.open(tmp_path) as img:
            return _region_is_black(img)
    except Exception:
        return False
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def gather_files(target: Path, recursive: bool) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() in MEDIA_EXTENSIONS else []

    if not target.is_dir():
        return []

    pattern = "**/*" if recursive else "*"
    files: list[Path] = []
    for p in target.glob(pattern):
        if not p.is_file() or p.suffix.lower() not in MEDIA_EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        files.append(p)
    return sorted(files)


def process_one(
    path: Path,
    dest: Path,
    force: bool,
    ffmpeg: str | None,
    *,
    lossless: bool,
    webp_quality: int,
    crf: int | None,
) -> tuple[str, Path]:
    suffix = path.suffix.lower()
    if suffix in IMAGE_EXTENSIONS:
        if not force and already_covered_image(path):
            return ("skip", path)
        cover_image(path, dest, lossless=lossless, webp_quality=webp_quality)
        return ("ok", dest)
    if suffix in VIDEO_EXTENSIONS:
        if ffmpeg is None:
            raise RuntimeError("ffmpeg is required for videos")
        if not force and already_covered_video(path, ffmpeg):
            return ("skip", path)
        cover_video(path, dest, ffmpeg, crf=crf)
        return ("ok", dest)
    raise RuntimeError(f"unsupported type: {suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Put a 110x60 black rectangle on the bottom-right of images and videos."
    )
    parser.add_argument("input", type=Path, help="Input file or directory.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output path for a single file (default: overwrite the input file).",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recurse into subdirectories when input is a directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Cover even if the bottom-right is already black.",
    )
    parser.add_argument(
        "-j",
        "--jobs",
        type=int,
        default=4,
        help="Parallel workers (default: 4).",
    )
    parser.add_argument(
        "--lossless",
        action="store_true",
        help="Save WebP lossless (much larger files).",
    )
    parser.add_argument(
        "--webp-quality",
        type=int,
        default=85,
        help="Lossy WebP quality 0-100 (default: 85).",
    )
    parser.add_argument(
        "--crf",
        type=int,
        default=None,
        help="Use this x264 CRF instead of matching the source bitrate.",
    )
    args = parser.parse_args()

    src = args.input
    if not src.exists():
        print(f"Not found: {src}", file=sys.stderr)
        return 1

    if src.is_dir() and args.output is not None:
        print("-o is only valid for a single input file", file=sys.stderr)
        return 1

    files = gather_files(src, args.recursive)
    if not files:
        print(f"No images or videos found: {src}", file=sys.stderr)
        return 1

    has_video = any(p.suffix.lower() in VIDEO_EXTENSIONS for p in files)
    ffmpeg = which_ffmpeg() if has_video else None

    jobs = max(1, args.jobs)
    failed = 0
    skipped = 0
    ok = 0

    def run(path: Path) -> tuple[str, Path] | tuple[str, Path, str]:
        dest = args.output if args.output is not None else path
        try:
            return process_one(
                path,
                dest,
                args.force,
                ffmpeg,
                lossless=args.lossless,
                webp_quality=args.webp_quality,
                crf=args.crf,
            )
        except Exception as exc:  # noqa: BLE001
            return ("fail", path, str(exc))

    if jobs == 1 or len(files) == 1:
        results = [run(p) for p in files]
    else:
        results = []
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            futs = {pool.submit(run, p): p for p in files}
            for fut in as_completed(futs):
                results.append(fut.result())

    # Stable print order by path
    results.sort(key=lambda r: str(r[1]))
    for item in results:
        status = item[0]
        path = item[1]
        if status == "ok":
            ok += 1
            print(f"OK      {path}  ({RECT_W}x{RECT_H} black rect, bottom-right)")
        elif status == "skip":
            skipped += 1
            print(f"SKIP    {path}  (already covered)")
        else:
            failed += 1
            err = item[2] if len(item) > 2 else "unknown error"
            print(f"FAILED  {path}: {err}", file=sys.stderr)

    print(f"\nDone. ok={ok} skip={skipped} fail={failed} total={len(files)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
