#!/usr/bin/env python3
"""
saz_concordancer.py: Query the saz.lu concordancer API for real-life Luxembourgish sentence examples.
Usage:
    python3 saz_concordancer.py <query> [--limit 5] [--strict] [--with-translation]
"""

import sys
import argparse
import requests
import json

SOURCES = [
    {"id": 1, "name": "lod.lu"},
    {"id": 2, "name": "lb.wikipedia.org"},
    {"id": 3, "name": "exercice.lu"},
    {"id": 4, "name": "rtl.lu"},
    {"id": 5, "name": "stemm.lu"},
    {"id": 6, "name": "gouvernement.lu"},
    {"id": 7, "name": "100komma7.lu"},
    {"id": 8, "name": "eldo.lu"},
    {"id": 9, "name": "chd.lu"}
]

def search_concordancer(query, strict=False, with_translation=True, limit=10):
    url = "https://www.saz.lu/api/searchSentences"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Content-Type": "application/json",
        "Origin": "https://saz.lu",
        "Referer": "https://saz.lu/"
    }
    payload = {
        "text": query,
        "strictMode": strict,
        "sources": SOURCES,
        "withTranslation": with_translation
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return data.get("sentences", [])
        else:
            print(f"Error: HTTP {response.status_code} - {response.text[:200]}", file=sys.stderr)
            return []
    except Exception as e:
        print(f"Connection error: {e}", file=sys.stderr)
        return []

def main():
    parser = argparse.ArgumentParser(description="Query saz.lu concordancer for Luxembourgish sentence examples.")
    parser.add_argument("query", help="Word or phrase to search for")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of sentences to display (default: 5)")
    parser.add_argument("--strict", action="store_true", help="Use strict exact-match search")
    parser.add_argument("--no-translation", action="store_true", help="Do not request translations")
    args = parser.parse_args()

    sentences = search_concordancer(args.query, strict=args.strict, with_translation=not args.no_translation, limit=args.limit)
    
    if not sentences:
        print(f"No sentences found for '{args.query}'.")
        return

    print(f"Found {len(sentences)} sentence(s) for '{args.query}' (showing up to {args.limit}):\n" + "=" * 70)
    for idx, s in enumerate(sentences[:args.limit], 1):
        lb = s.get("textLb", "").replace("<em>", "").replace("</em>", "")
        source = s.get("source", {}).get("name", "Unknown") if isinstance(s.get("source"), dict) else s.get("sourceName", "")
        print(f"{idx}. {lb}")
        if source:
            print(f"   [Source: {source}]")
        fr = s.get("textFr")
        en = s.get("textEn")
        de = s.get("textDe")
        if fr:
            print(f"   FR: {fr}")
        if en:
            print(f"   EN: {en}")
        if de:
            print(f"   DE: {de}")
        print("-" * 70)

if __name__ == "__main__":
    main()
