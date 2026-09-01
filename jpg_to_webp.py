#!/usr/bin/env python3
"""Convert .jpg/.jpeg images to lossless .webp.

Usage:
    python jpg_to_webp.py <input>              # single file or directory
    python jpg_to_webp.py <input> -o <outdir>  # write results to outdir
    python jpg_to_webp.py <dir> -r             # recurse into subdirectories
    python jpg_to_webp.py <input> --keep       # keep originals (default)
    python jpg_to_webp.py <input> --delete     # delete originals after success

Requires Pillow:  pip install Pillow
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required. Install it with: pip install Pillow")

JPG_EXTENSIONS = {".jpg", ".jpeg", ".jpe", ".jfif"}


def convert_file(src: Path, out_dir: Path | None, delete_original: bool) -> bool:
    """Convert a single JPEG file to lossless WebP. Returns True on success."""
    dest_dir = out_dir if out_dir is not None else src.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / (src.stem + ".webp")

    try:
        with Image.open(src) as img:
            # Preserve mode; lossless WebP supports RGB/RGBA.
            if img.mode not in ("RGB", "RGBA", "L"):
                img = img.convert("RGBA")
            img.save(dest, "WEBP", lossless=True, quality=100, method=6)
    except Exception as exc:  # noqa: BLE001 - report and continue
        print(f"FAILED  {src}: {exc}", file=sys.stderr)
        return False

    print(f"OK      {src} -> {dest}")

    if delete_original:
        try:
            src.unlink()
        except OSError as exc:
            print(f"WARN    could not delete {src}: {exc}", file=sys.stderr)

    return True


def gather_files(target: Path, recursive: bool) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() in JPG_EXTENSIONS else []

    if target.is_dir():
        pattern = "**/*" if recursive else "*"
        return sorted(
            p for p in target.glob(pattern)
            if p.is_file() and p.suffix.lower() in JPG_EXTENSIONS
        )

    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert .jpg/.jpeg images to lossless .webp."
    )
    parser.add_argument("input", type=Path, help="Input file or directory.")
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output directory (default: alongside each source file).",
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true",
        help="Recurse into subdirectories when input is a directory.",
    )
    parser.add_argument(
        "--delete", action="store_true",
        help="Delete original JPEGs after successful conversion.",
    )
    args = parser.parse_args()

    if not args.input.exists():
        sys.exit(f"Input path does not exist: {args.input}")

    files = gather_files(args.input, args.recursive)
    if not files:
        sys.exit("No .jpg/.jpeg files found to convert.")

    ok = sum(convert_file(f, args.output, args.delete) for f in files)
    failed = len(files) - ok
    print(f"\nDone. {ok} converted, {failed} failed, {len(files)} total.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
