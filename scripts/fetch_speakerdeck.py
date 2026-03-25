#!/usr/bin/env python3
"""
Fetch SpeakerDeck talks for yoshiori and write to src/content/talks.json.
Run locally:  python scripts/fetch_speakerdeck.py
Or via GitHub Actions on a schedule.
"""
import urllib.request
import xml.etree.ElementTree as ET
import json
import re
from pathlib import Path
from email.utils import parsedate_to_datetime

RSS_URL = "https://speakerdeck.com/yoshiori.rss"
OUT_PATH = Path(__file__).parent.parent / "src" / "content" / "talks.json"


def fetch_talks() -> list[dict]:
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as res:
        tree = ET.parse(res)

    root = tree.getroot()
    talks = []

    for item in root.findall(".//item"):
        title = item.findtext("title", "").strip()
        link  = item.findtext("link",  "").strip()
        date  = item.findtext("pubDate", "").strip()
        desc  = item.findtext("description", "")

        # Normalise date to ISO 8601
        try:
            iso_date = parsedate_to_datetime(date).isoformat()
        except Exception:
            iso_date = date

        # Extract first <img src="..."> from HTML description
        thumbnail = ""
        m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', desc)
        if m:
            thumbnail = m.group(1)

        if title and link:
            talks.append({
                "title":     title,
                "url":       link,
                "date":      iso_date,
                "thumbnail": thumbnail,
            })

    return talks


if __name__ == "__main__":
    talks = fetch_talks()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(talks, ensure_ascii=False, indent=2))
    print(f"✓ Fetched {len(talks)} talks → {OUT_PATH}")
