# rtmdrr.github.io — Modern static site
Static site for your academic homepage. It renders publications from `data/publications.json`.

## Deploy on GitHub Pages
Push to the root of `rtmdrr/rtmdrr.github.io` on branch `main`. In Settings → Pages, choose `main` and `/ (root)`.

## Auto-updating publications
- Weekly + manual run via `.github/workflows/scholar.yml`.
- It runs `scholar_update.py` to scrape Google Scholar (ID `ZB0tZNEAAAAJ`) and overwrite `data/publications.json`.
- Note: Google Scholar has no official API; scraping can be throttled. Re-run manually if needed.

## Customize
- Edit `data/profile.json`, `data/talks.json`, `data/teaching.json`.
- Styles in `assets/styles.css`.

## Local preview
```bash
python -m http.server -d . 8080
```
