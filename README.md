# Kirish’s Brief

A lightweight, source-linked AI / engineering / finance reading desk. Start with **[START-HERE.md](START-HERE.md)** for publishing instructions.

## Included

- Eleven explained news stories researched on 12 October 2026.
- Nine foundation guides, a five-part model map, fifteen glossary terms and a small timeline.
- Twelve ChatGPT/OpenAI documentation introductions across product, developer, release and behaviour tracks.
- Topic filters, search, native-dialog reading room, local bookmarks/progress, JSON export and dark mode.
- Eight configurable RSS/Atom sources and six documentation text-change watchers.
- A standard-library Python updater, optional Responses API digests and a six-hourly GitHub Pages workflow.
- Offline failure-handling/security tests, optional browser smoke test and single-file preview builder.

**Built, not deployed.** No account connection, public hosting, scheduled run or paid API request was made while creating the package. See `TEST-REPORT.md` for exactly what was tested.

## Project layout

```text
kirish-brief/
  .github/workflows/publish.yml  # scheduled refresh + Pages deployment
  content/editorial.json        # editable explained stories and learning material
  content/feeds.json            # publisher feeds, domains and keywords
  scripts/update.py            # fetch, validate, merge, optional digest, build
  scripts/build_preview.py      # self-contained HTML with hashed CSP
  scripts/seed_content.py       # reset starter content; do not rerun after editing
  scripts/browser_smoke.py      # optional Playwright browser checks
  site/index.html
  site/assets/app.js
  site/assets/style.css
  site/assets/favicon.svg
  site/data/brief.js            # generated public data
  site/data/brief.json          # generated public data
  tests/test_updater.py
  kirish-brief-preview.html     # standalone snapshot
  START-HERE.md
  TOOLS-AND-MAINTENANCE.md
  TEST-REPORT.md
```

`content/feed-cache.json` and `content/update-status.json` are created by a live updater run. They are not fake seeded results.

## Local use

Python 3.12 or newer is the workflow target. No third-party Python packages are needed for the updater or its unit tests.

```sh
python -m unittest discover -s tests -v
python scripts/update.py --build-only
python scripts/build_preview.py
python -m http.server 8000 --directory site
```

Open `http://localhost:8000` in your browser. Stop the local server with Ctrl+C. `--build-only` makes no network/API requests. Running `python scripts/update.py` without that flag contacts configured publishers and, only when both API variables are set, the API.

## Data and behaviour

Imported text is escaped in the browser. Source URLs use a server-side HTTPS allowlist, redirects are checked, fetch sizes are bounded, and unsafe XML is rejected. The updater excludes future, missing-date and stale items, distinguishes an Atom update date from publication, deduplicates links and retains cached stories on individual source failures. Imported feed history is retained for 120 days, up to 240 items; starter explainers remain separately available.

Without credentials, only headlines/links/dates are imported. Raw feed descriptions are transient and are not committed. Optional digests use bounded structured output with a verbatim-copy guard. That guard is not a complete copyright or accuracy guarantee. The source publisher retains its rights; follow the original for its full account. Do not remove attribution or turn feed access into unrestricted republication of full articles.

Selected-source news coverage is not an exhaustive view of the field. First-party announcements are labelled by publisher and may be promotional. No market prices or market-data API are included. Model cards link to current official information rather than presenting an unsupported universal leaderboard.

## Operational limitations

- RSS endpoints and documentation access must be validated on the first hosted run.
- GitHub scheduled delivery is best-effort, not a real-time service.
- Optional API digests need separate billing and a model supported by the owner’s API account.
- Documentation text changes require interpretation; guide prose is not automatically rewritten.
- Bookmarks are browser-local, with no account or cross-device sync.
- The front end is a small client-rendered site, not a server-rendered publishing platform; rich per-article search-engine previews are not implemented.
- The offline HTML preview is a snapshot. Only the deployed scheduled workflow fetches updates.

The code contains no analytics, remote fonts, advertising, or private contact information. A hosting provider can still retain access logs. See the site’s How it’s built page for privacy and methodology.
