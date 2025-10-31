#!/usr/bin/env python3
"""
Fetch ORCID public record and save a JSON snapshot for the site to consume.

Usage:
  python scripts/fetch_orcid.py 0000-0002-9018-6480

This script calls the ORCID public API (v3) and writes the response to
`docs/assets/data/orcid-<id>.json`. It's safe to run in CI to refresh cached data.
"""
import sys
import json
from pathlib import Path
import urllib.request


def fetch_orcid(orcid_id: str) -> dict:
    url = f"https://pub.orcid.org/v3.0/{orcid_id}"
    req = urllib.request.Request(url, headers={
        'Accept': 'application/json',
        'User-Agent': 'mkdocs-orcid-fetcher/1.0 (+https://github.com)'
    })
    with urllib.request.urlopen(req) as resp:
        raw = resp.read()
        return json.loads(raw)


def save_snapshot(orcid_id: str, data: dict):
    out_dir = Path('docs/assets/data')
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f'orcid-{orcid_id}.json'
    with out_file.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('Saved ORCID snapshot to:', out_file)


def main():
    if len(sys.argv) < 2:
        print('Usage: fetch_orcid.py <orcid-id>')
        sys.exit(2)

    orcid_id = sys.argv[1]
    try:
        data = fetch_orcid(orcid_id)
        save_snapshot(orcid_id, data)
    except Exception as e:
        print('Failed to fetch ORCID:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
