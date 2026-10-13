# Build and test report

Build date: **12 October 2026**.

## Passed

**22 offline Python unit tests** passed. They cover RSS and Atom parsing; explicit Atom updated-date labels; missing, future and old dates; domain allowlists; tracking-link deduplication; topic filtering; unsafe XML; HTML sanitisation; preserving cached news after source failure; preserving or invalidating prior digests appropriately; structured digest validation and long-verbatim guards; documentation baselines, changes and failed checks; script-safe data encoding; and an all-feeds-fail run that does not claim success.

Python compilation passed for the updater, preview builder, seed script and optional browser test. `node --check site/assets/app.js` passed.

**Chromium/Playwright interface checks passed** at desktop 1440 × 1050 and mobile-sized 390 × 844 viewports. Tests covered the homepage, all navigation routes, article dialog, mark-as-read, session bookmarks, saved reading, news search, documentation filters/search, foundation-guide search, dark mode, mobile navigation and horizontal-overflow checks. No browser page errors or console errors occurred. Desktop, docs, dark and mobile screenshots were visually inspected (mobile top section reviewed separately).

The browser test rendered the **single-file HTML in an embedded offline page**. That page has an opaque origin, so session-only bookmark fallback was tested rather than persistent storage across browser restarts. The regular multi-file site's external-asset CSP still needs a normal hosted/browser check; the standalone file's hashed inline CSP passed the browser test.

## Not tested or not performed

- A public deployment or actual GitHub Actions run.
- Live fetching of the eight RSS/Atom endpoints from the code environment; outbound network/DNS was unavailable. These URLs remain configured candidates to validate on the first hosted run.
- Live documentation-change monitoring from Python. Monitoring logic was tested against controlled local fixtures, not an ongoing public-page history.
- A paid OpenAI API request, account-specific model access or billing.
- Safari/Firefox, native mobile file previews, real-device touch testing or a formal accessibility audit.
- Persistent reading-data storage across origins/devices or browser restarts; there is intentionally no cross-device synchronisation.
- Every future publisher claim. Starter sources were read with the web research tool, but this is AI-assisted explanation, not independent human editorial certification.

The package includes the actual tests. Run offline tests with:

```sh
python -m unittest discover -s tests -v
```

The optional UI test requires Playwright and its Chromium browser (not required for normal use of the site or updater):

```sh
python -m pip install playwright
python -m playwright install chromium
python scripts/build_preview.py
python scripts/browser_smoke.py
```

To exercise a deployed/local HTTP site instead of the embedded preview:

```sh
python scripts/browser_smoke.py --url http://localhost:8000/
```

Start the local web server in another terminal first. An existing system Chromium can be supplied with `--chromium` and its executable path.

## First deployment acceptance check

Confirm that the public URL loads its CSS and stories; both GitHub jobs succeed; source-check timestamps reflect the real run; any blocked feeds are marked failed; documentation checks show a baseline or an explicit error; API mode remains off unless deliberately configured; and bookmarks survive a page reload in an ordinary browser. Review the first generated digests against their sources before relying on automatic explanations.
