#!/usr/bin/env python3
"""
Generate OG image (1200x630) for yoshiori.dev.
Run locally:  python scripts/generate_og_image.py
Requires:     pip install Pillow
"""
import json
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parent.parent
SITE_JSON = ROOT / "src" / "content" / "site.json"
PROFILE_PATH = ROOT / "src" / "assets" / "profile.jpg"
OUT_PATH = ROOT / "public" / "og-image.png"

# Design tokens (matching src/styles/global.css @theme)
BG = (10, 10, 10)           # #0a0a0a
ACCENT = (232, 255, 0)      # #e8ff00
TEXT_COLOR = (232, 232, 232) # #e8e8e8
MUTED = (85, 85, 85)        # #555555

W, H = 1200, 630

# Font paths (Liberation fonts are widely available on Linux)
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"


def generate():
    site = json.loads(SITE_JSON.read_text())

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Profile image (right side)
    profile = Image.open(PROFILE_PATH)
    profile = profile.resize((280, 280), Image.LANCZOS)
    profile_x = W - 280 - 80
    profile_y = (H - 280) // 2
    img.paste(profile, (profile_x, profile_y))
    draw.rectangle(
        [profile_x - 3, profile_y - 3, profile_x + 280 + 2, profile_y + 280 + 2],
        outline=ACCENT, width=3,
    )

    # Fonts
    font_large = ImageFont.truetype(FONT_BOLD, 72)
    font_medium = ImageFont.truetype(FONT_REGULAR, 28)
    font_small = ImageFont.truetype(FONT_MONO, 18)

    # Accent line
    draw.rectangle([80, 80, 500, 83], fill=ACCENT)

    # Label
    label = f"{site['title'].upper()} · {site['location'].split(',')[0].upper()}"
    draw.text((80, 96), label, fill=ACCENT, font=font_small)

    # Name
    draw.text((80, 160), site["firstName"], fill=TEXT_COLOR, font=font_large)
    draw.text((80, 245), site["lastName"], fill=ACCENT, font=font_large)

    # Description
    y = 370
    for line in site["ogDescription"]:
        draw.text((80, y), line, fill=MUTED, font=font_medium)
        y += 40

    # URL (extract domain from siteUrl)
    domain = urlparse(site["siteUrl"]).hostname
    draw.text((80, 520), domain, fill=MUTED, font=font_small)

    # Save
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, "PNG", optimize=True)
    print(f"✓ Generated OG image → {OUT_PATH}")


if __name__ == "__main__":
    generate()
