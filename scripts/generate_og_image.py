#!/usr/bin/env python3
"""
Generate OG image (1200x630) for yoshiori.dev.
Run locally:  python scripts/generate_og_image.py
Requires:     pip install Pillow
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).parent.parent
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
    draw.text((80, 96), "ENGINEERING DIRECTOR · TOKYO", fill=ACCENT, font=font_small)

    # Name
    draw.text((80, 160), "YOSHIORI", fill=TEXT_COLOR, font=font_large)
    draw.text((80, 245), "SHOJI", fill=ACCENT, font=font_large)

    # Description
    draw.text((80, 370), "Software engineer with 20+ years of experience.", fill=MUTED, font=font_medium)
    draw.text((80, 410), "Speaker, author, and community organizer.", fill=MUTED, font=font_medium)

    # URL
    draw.text((80, 520), "yoshiori.dev", fill=MUTED, font=font_small)

    # Save
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, "PNG", optimize=True)
    print(f"✓ Generated OG image → {OUT_PATH}")


if __name__ == "__main__":
    generate()
