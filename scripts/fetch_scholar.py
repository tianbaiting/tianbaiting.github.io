#!/usr/bin/env python3
"""
Fetch a Google Scholar profile page and save a JSON snapshot.

Usage:
  python3 scripts/fetch_scholar.py Wb4CcQ8AAAAJ

Outputs: docs/assets/data/scholar-<id>.json

Note: Google Scholar has no public API. This script scrapes the public profile page.
Use responsibly and consider running in CI with low frequency. If Google blocks
requests, consider manual snapshotting or using a third-party service.
"""
import sys
import json
from pathlib import Path
import time

import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
}


def fetch_profile(user_id: str, hl: str = 'en') -> dict:
    url = f'https://scholar.google.com/citations?user={user_id}&hl={hl}'
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    profile = {}
    # name
    name_div = soup.select_one('#gsc_prf_in')
    profile['name'] = name_div.text.strip() if name_div else ''

    # affiliation / metadata
    aff = soup.select_one('.gsc_prf_ila')
    profile['affiliation'] = aff.text.strip() if aff else ''

    # metrics table
    profile['metrics'] = {}
    try:
        rows = soup.select('.gsc_rsb_st table tr')
        for r in rows:
            cols = [c.get_text(strip=True) for c in r.find_all('td')]
            if len(cols) >= 2:
                key = cols[0]
                profile['metrics'][key] = {
                    'all': cols[1] if len(cols) > 1 else None,
                    'since2019': cols[2] if len(cols) > 2 else None
                }
    except Exception:
        pass

    # recent publications (first page, up to 8)
    pubs = []
    try:
        rows = soup.select('.gsc_a_tr')
        for r in rows[:8]:
            title_a = r.select_one('.gsc_a_t a')
            title = title_a.text.strip() if title_a else ''
            link = 'https://scholar.google.com' + title_a['href'] if title_a and title_a.has_attr('href') else ''
            year_td = r.select_one('.gsc_a_y')
            year = year_td.text.strip() if year_td else ''
            pubs.append({'title': title, 'link': link, 'year': year})
    except Exception:
        pass
    profile['publications'] = pubs

    # raw snapshot meta
    profile['_fetched_at'] = int(time.time())
    profile['_source_url'] = url

    return profile


def save_snapshot(user_id: str, data: dict):
    out_dir = Path('docs/assets/data')
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f'scholar-{user_id}.json'
    with out_file.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('Saved Google Scholar snapshot to:', out_file)


def main():
    if len(sys.argv) < 2:
        print('Usage: fetch_scholar.py <scholar_user_id>')
        sys.exit(2)
    user_id = sys.argv[1]
    try:
        data = fetch_profile(user_id)
        save_snapshot(user_id, data)
    except Exception as e:
        print('Failed to fetch scholar profile:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
