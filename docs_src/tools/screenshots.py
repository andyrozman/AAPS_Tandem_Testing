#!/usr/bin/env python3
"""Helpers for capturing and preparing documentation screenshots.

Commands
--------
capture NAME        Take a screenshot from the phone over USB (adb) and save it as
                    docs_src/images/tandem/NAME.jpg (normalized).
demo on|off         Turn Android System UI demo mode on/off for a clean status bar
                    (fixed clock, full battery, no notification icons). Not all phones
                    support it (some Samsung builds ignore it).
normalize FILE...   Resize to 1080 px wide (if larger) and recompress as JPEG (quality 85).
                    PNG input is written next to it as .jpg.
redact FILE X Y W H Black out a rectangle (in pixels of the original image), e.g. a serial
                    number. Can be repeated with more X Y W H groups.

Requires: Pillow (pip install pillow). `capture` and `demo` also need adb on PATH and a phone
with USB debugging enabled.
"""

import argparse
import io
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install pillow")

IMAGES = Path(__file__).resolve().parent.parent / "images" / "tandem"
TARGET_WIDTH = 1080
JPEG_QUALITY = 85


def adb(*args: str, capture: bool = False) -> bytes:
    if not shutil.which("adb"):
        sys.exit("adb not found on PATH. Install Android platform-tools.")
    result = subprocess.run(["adb", *args], check=True, stdout=subprocess.PIPE if capture else None)
    return result.stdout if capture else b""


def normalize_image(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    if img.width > TARGET_WIDTH:
        height = round(img.height * TARGET_WIDTH / img.width)
        img = img.resize((TARGET_WIDTH, height), Image.LANCZOS)
    return img


def save_jpeg(img: Image.Image, path: Path) -> Path:
    path = path.with_suffix(".jpg")
    img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    print(f"wrote {path} ({img.width}x{img.height}, {path.stat().st_size // 1024} KB)")
    return path


def cmd_capture(args):
    png = adb("exec-out", "screencap", "-p", capture=True)
    img = normalize_image(Image.open(io.BytesIO(png)))
    IMAGES.mkdir(parents=True, exist_ok=True)
    save_jpeg(img, IMAGES / args.name)


def cmd_demo(args):
    def bcast(*extra):
        adb("shell", "am", "broadcast", "-a", "com.android.systemui.demo", *extra)

    if args.state == "on":
        adb("shell", "settings", "put", "global", "sysui_demo_allowed", "1")
        bcast("-e", "command", "enter")
        bcast("-e", "command", "clock", "-e", "hhmm", "1200")
        bcast("-e", "command", "battery", "-e", "level", "100", "-e", "plugged", "false")
        bcast("-e", "command", "network", "-e", "wifi", "show", "-e", "level", "4")
        bcast("-e", "command", "notifications", "-e", "visible", "false")
        print("demo mode on")
    else:
        bcast("-e", "command", "exit")
        print("demo mode off")


def cmd_normalize(args):
    for f in args.files:
        p = Path(f)
        save_jpeg(normalize_image(Image.open(p)), p)


def cmd_redact(args):
    p = Path(args.file)
    boxes = args.box
    if len(boxes) % 4:
        sys.exit("redact needs groups of four numbers: X Y W H")
    img = Image.open(p).convert("RGB")
    draw = ImageDraw.Draw(img)
    for i in range(0, len(boxes), 4):
        x, y, w, h = boxes[i:i + 4]
        draw.rectangle([x, y, x + w, y + h], fill="black")
    if p.suffix.lower() in (".jpg", ".jpeg"):
        save_jpeg(img, p)
    else:
        img.save(p)
        print(f"wrote {p}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("capture", help="capture from phone via adb")
    c.add_argument("name", help="file name without extension, e.g. v4_overview")
    c.set_defaults(func=cmd_capture)

    d = sub.add_parser("demo", help="toggle clean status bar")
    d.add_argument("state", choices=["on", "off"])
    d.set_defaults(func=cmd_demo)

    n = sub.add_parser("normalize", help="resize and recompress")
    n.add_argument("files", nargs="+")
    n.set_defaults(func=cmd_normalize)

    r = sub.add_parser("redact", help="black out rectangles")
    r.add_argument("file")
    r.add_argument("box", nargs="+", type=int, metavar="N")
    r.set_defaults(func=cmd_redact)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
