#!/usr/bin/env python3
"""Refresh data/publications.json from Google Scholar.

Run weekly by .github/workflows/update-publications.yml.

Two ways to reach Scholar:
  1. SerpAPI (reliable): set a repository secret SERPAPI_KEY. Free tier is enough
     for a weekly run. Used automatically when the key is present.
  2. The `scholarly` package (free, no key): used otherwise. Google sometimes
     blocks requests coming from GitHub's servers; if that happens the script
     leaves the existing file untouched and the site keeps showing the last
     good list.

Optional: data/publications_extra.json can hold entries that are missing from
Scholar (e.g. accepted papers). They are merged in by title.
"""
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

SCHOLAR_ID = "ZB0tZNEAAAAJ"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "publications.json"
EXTRA = ROOT / "data" / "publications_extra.json"
SCHOLAR_PUB = ("https://scholar.google.com/citations?view_op=view_citation&hl=en"
               "&user=" + SCHOLAR_ID + "&citation_for_view={}")


def norm(title):
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def to_int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------- SerpAPI
def fetch_serpapi(key):
    import requests

    pubs, metrics, start = [], {}, 0
    while True:
        r = requests.get("https://serpapi.com/search.json", timeout=60, params={
            "engine": "google_scholar_author", "author_id": SCHOLAR_ID, "hl": "en",
            "num": 100, "start": start, "sort": "pubdate", "api_key": key,
        })
        r.raise_for_status()
        d = r.json()
        if start == 0:
            for row in (d.get("cited_by") or {}).get("table", []):
                if "citations" in row:
                    metrics["citations"] = row["citations"].get("all")
                if "h_index" in row:
                    metrics["h_index"] = row["h_index"].get("all")
        arts = d.get("articles") or []
        for a in arts:
            cid = a.get("citation_id")
            pubs.append({
                "title": a.get("title", "").strip(),
                "authors": a.get("authors", ""),
                "venue": a.get("publication", ""),
                "year": to_int(a.get("year")),
                "citations": to_int((a.get("cited_by") or {}).get("value")),
                "url": a.get("link"),
                "scholar_url": SCHOLAR_PUB.format(cid if ":" in cid else SCHOLAR_ID + ":" + cid) if cid else None,
            })
        if len(arts) < 100:
            break
        start += 100
    return pubs, metrics


# ---------------------------------------------------------------- scholarly
def fetch_scholarly(previous):
    from scholarly import scholarly, ProxyGenerator

    if os.environ.get("USE_FREE_PROXY") == "1":
        pg = ProxyGenerator()
        if pg.FreeProxies():
            scholarly.use_proxy(pg)

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "publications"])
    metrics = {"citations": author.get("citedby"), "h_index": author.get("hindex")}

    # Reuse author lists/venues we already have, so only new papers need an
    # extra request (fewer requests = less chance of being blocked).
    known = {norm(p["title"]): p for p in previous}
    pubs = []
    for p in author.get("publications", []):
        bib = p.get("bib", {})
        title = bib.get("title", "").strip()
        old = known.get(norm(title), {})
        authors, venue, url = old.get("authors"), old.get("venue"), old.get("url")
        if not authors or old.get("scholar_url") is None:
            try:
                time.sleep(2)
                full = scholarly.fill(p)
                fb = full.get("bib", {})
                authors = fb.get("author", "").replace(" and ", ", ") or authors
                venue = (fb.get("journal") or fb.get("conference") or fb.get("booktitle")
                         or fb.get("publisher") or bib.get("citation") or venue)
                url = full.get("pub_url") or full.get("eprint_url") or url
            except Exception as e:  # keep going with what we have
                print("  could not fill:", title[:60], "-", e, file=sys.stderr)
        pid = p.get("author_pub_id", "")
        pubs.append({
            "title": title,
            "authors": authors or "",
            "venue": venue or bib.get("citation", ""),
            "year": to_int(bib.get("pub_year")),
            "citations": to_int(p.get("num_citations")),
            "url": url,
            "scholar_url": SCHOLAR_PUB.format(pid if ":" in pid else SCHOLAR_ID + ":" + pid) if pid else None,
        })
    return pubs, metrics


# ---------------------------------------------------------------- main
def main():
    current = load(OUT) or {"publications": []}
    previous = current.get("publications", [])

    key = os.environ.get("SERPAPI_KEY")
    try:
        pubs, metrics = fetch_serpapi(key) if key else fetch_scholarly(previous)
        source = "Google Scholar via " + ("SerpAPI" if key else "scholarly")
    except Exception as e:
        print("Could not reach Google Scholar:", e, file=sys.stderr)
        print("Keeping the existing publication list.")
        return 0

    pubs = [p for p in pubs if p["title"]]
    # Safety net: a partial or blocked response must not wipe the site.
    if len(pubs) < 0.8 * len(previous):
        print(f"Only {len(pubs)} publications returned (had {len(previous)}); not overwriting.")
        return 0

    # Keep seed links (arXiv/DOI) when Scholar has no direct link.
    by_title = {norm(p["title"]): p for p in previous}
    for p in pubs:
        if not p.get("url"):
            p["url"] = by_title.get(norm(p["title"]), {}).get("url") or p.get("scholar_url")

    extra = load(EXTRA) or []
    seen = {norm(p["title"]) for p in pubs}
    pubs += [e for e in extra if norm(e.get("title")) not in seen]

    pubs.sort(key=lambda p: -(p.get("year") or 0))  # stable: keeps Scholar's order within a year
    new = {"updated": date.today().isoformat(), "source": source,
           "scholar_id": SCHOLAR_ID, "metrics": metrics, "publications": pubs}

    if {k: v for k, v in new.items() if k != "updated"} == {k: v for k, v in current.items() if k != "updated"}:
        print("No changes.")
        return 0
    OUT.write_text(json.dumps(new, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(pubs)} publications.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
