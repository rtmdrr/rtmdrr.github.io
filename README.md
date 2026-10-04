# rtmdrr.github.io

Personal academic website of Rotem Dror. Plain HTML/CSS/JS, no build step.

## Files

| File | What it is |
| --- | --- |
| `index.html` | Home: bio, links, call for students, recent publications |
| `research.html` | Research vision and topics |
| `publications.html` | Full publication list (rendered from `data/publications.json`) |
| `students.html` | Students and alumni (edit the lists directly) |
| `data/publications.json` | Publication data, refreshed weekly from Google Scholar |
| `data/publications_extra.json` | Optional: papers missing from Scholar, merged in by title |
| `scripts/update_publications.py` | The updater |
| `.github/workflows/update-publications.yml` | Runs the updater every Monday |
| `assets/photo.jpg` | Optional: add a portrait and it appears on the home page |

## Deploying

1. Replace the contents of the `rtmdrr.github.io` repository with these files
   (keep `.nojekyll` and the `.github` folder; delete the old `cv.html`, `talks.html`, `teaching.html`).
2. In the repository: **Settings > Actions > General > Workflow permissions**, choose
   **Read and write permissions** so the workflow can commit the updated list.
3. Go to the **Actions** tab, open "Update publications from Google Scholar" and click
   **Run workflow** once to pull the current Scholar list.

## Automatic publication updates

The workflow tries Google Scholar with the free `scholarly` package. Google sometimes
blocks requests from GitHub's servers; when that happens nothing is overwritten and
the site keeps the last good list.

For a reliable update, create a free account at serpapi.com and add the API key as a
repository secret named `SERPAPI_KEY` (Settings > Secrets and variables > Actions).
The script uses it automatically. One run per week stays well inside the free tier.

## Previewing locally

The publication list is loaded with `fetch`, which browsers block for `file://` pages.
Run `python3 -m http.server` in this folder and open http://localhost:8000.
