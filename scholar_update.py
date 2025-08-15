#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and write data/publications.json.

Requires: scholarly
"""
import json, sys, time
from pathlib import Path

try:
    from scholarly import scholarly
except Exception as e:
    print("Failed to import scholarly. Ensure 'scholarly' is installed.", e)
    sys.exit(1)

USER_ID = "ZB0tZNEAAAAJ"  # Rotem Dror

def fetch_publications(user_id: str):
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["publications"])
    pubs = []
    for p in author.get("publications", []):
        try:
            filled = scholarly.fill(p)
        except Exception:
            time.sleep(1.0)
            try:
                filled = scholarly.fill(p)
            except Exception:
                continue
        bib = filled.get("bib", {})
        title = bib.get("title") or p.get("bib", {}).get("title")
        year = bib.get("pub_year")
        authors = bib.get("author")
        venue = bib.get("venue") or bib.get("journal") or bib.get("eprint") or ""
        url = (filled.get("eprint_url") or filled.get("pub_url") or filled.get("citedby_url") or "")
        if isinstance(authors, str):
            if " and " in authors:
                authors = [a.strip() for a in authors.split(" and ") if a.strip()]
            else:
                authors = [a.strip() for a in authors.split(",") if a.strip()]
        pubs.append({
            "title": title,
            "venue": venue,
            "year": int(year) if year and str(year).isdigit() else None,
            "authors": authors,
            "url": url,
        })
    seen, uniq = set(), []
    for p in pubs:
        key = (p.get("title") or "").strip().lower()
        if key and key not in seen:
            uniq.append(p); seen.add(key)
    uniq.sort(key=lambda x: (x.get("year") or 0, x.get("title") or ""), reverse=True)
    return uniq

def main():
    base = Path(__file__).resolve().parent
    data_dir = base / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    pubs = fetch_publications(USER_ID)
    with open(data_dir / "publications.json", "w", encoding="utf-8") as f:
        json.dump(pubs, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(pubs)} publications to data/publications.json")

if __name__ == "__main__":
    main()
