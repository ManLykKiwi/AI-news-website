# Kirish’s Brief — start here

A source-linked reading desk for AI, engineering and finance, with a dedicated ChatGPT documentation hub.

**Status: the website is built, but it is not published. Automatic updates start only after the GitHub setup below.** The starter edition was researched on 12 October 2026. It contains 11 explained stories, 9 foundation guides, 12 documentation introductions, a model map and a glossary.

## 1. Open it now

Open `kirish-brief-preview.html` in a normal web browser. It is a standalone snapshot: no installation, account or API key is needed. Some mobile file-preview apps do not execute JavaScript; use a browser on your laptop if you see a blank page.

For the multi-file version, open `site/index.html` while keeping the `assets` and `data` folders beside it. The single-file preview is more reliable for a quick look. The preview does not download new stories automatically; the deployed website does that through its workflow.

## 2. Publish with GitHub Pages

You need a GitHub account. GitHub Pages supports public repositories on GitHub Free; provider terms and limits still apply. [Official Pages guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

1. Create a **public repository** called `kirish-brief`, using **main** as its default branch. Review the files before making them public. Do not upload private documents or credentials.
2. Extract the ZIP. Upload the **contents of the `kirish-brief` folder into the repository root**, not the outer folder and not the ZIP itself. Include the hidden `.github` folder. The repository must contain `.github/workflows/publish.yml`, `scripts`, `content`, `site` and `tests` at the paths shown in the README.
3. In the repository, open **Settings → Pages → Build and deployment → Source**, and choose **GitHub Actions**. The supplied file is already the workflow; there is no need to add another template. Check **Settings → Actions → General** if Actions is disabled. This workflow needs permission to write its generated edition back to this repository. A protected branch or organisation policy may need an administrator to approve that permission.
4. Open **Actions → Update and publish the brief → Run workflow** on `main`. Wait for both build and deployment to finish. The first upload may have run before Pages was enabled; rerun it after changing the setting.
5. Open the website URL shown by the successful deployment or **Settings → Pages**. On the site, open **Sources & updates** and inspect each source and documentation check.

The first hosted run is important: **live feed fetching, paid API calls and deployment were not verified in the build environment**. Offline updater tests and browser interface checks passed. An inaccessible source should show a failure while previously available stories remain readable. A green deployment does not guarantee that every publisher feed succeeded.

GitHub’s guide to configuring the publishing source: [official instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## 3. How regular updates work

The supplied workflow attempts a refresh four times per day, at **00:17, 06:17, 12:17 and 18:17 UTC**. UK local time is one hour ahead during British Summer Time. It also runs after your pushes to `main` and can be run manually.

The job fetches selected publisher RSS/Atom feeds, checks dates, removes duplicate links, optionally generates short explanations, monitors selected documentation pages, rebuilds the website and publishes it. A feed is a publisher’s machine-readable list of updates.

Schedules are not an exact-time guarantee. GitHub says scheduled jobs can be delayed or dropped during heavy load, and public-repository schedules can be disabled after 60 days without repository activity. Check the Actions tab periodically. [Official scheduling details](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

### Default mode: source updates, no AI API calls

Leave `OPENAI_API_KEY` and `OPENAI_MODEL` unset. New items appear as **Source update** with publisher, title, date and original link. They do not pretend to be fully explained stories. The source-linked starter explainers remain available.

This mode does not incur OpenAI API usage. Your hosting and automation account remains subject to the provider’s own terms and limits.

### Optional mode: automatically explained updates

Enable this only after reviewing API billing. In the repository’s **Settings → Secrets and variables → Actions**:

- Add a repository **secret** called `OPENAI_API_KEY` containing your own OpenAI API key.
- Add a repository **variable** called `OPENAI_MODEL` containing the exact ID of a model available to your API project that supports the Responses API and structured text output. Check current model documentation rather than guessing a model name.

Run the workflow again. It will attempt up to **four digests per run** when the publisher supplies enough feed text. Additional stories remain headline-only. This limit also applies to manual and push-triggered runs; it is not a total spending cap.

Digests have four short parts: what happened, why it might matter, a technical distinction and a limitation. They are labelled **AI-generated · publisher feed text only**. They are not based on a guaranteed full-article review, are not independently verified, and can be wrong. Short feeds, invalid output or API errors fall back to source updates.

No API requests were made to build this package. API billing is separate from a ChatGPT subscription. [OpenAI billing explanation](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform). [Structured output documentation](https://developers.openai.com/api/docs/guides/structured-outputs).

**Never paste an API key into the website, a source file, a screenshot, a commit, or this chat.** Store it only as the repository secret. Remove the secret or variable to turn digest generation off. Review your provider’s usage dashboard and budget controls.

## 4. What happens to the documentation hub?

The hub separates ChatGPT product help, developer documentation, release notes and intended assistant behaviour. Each card explains why its official page is worth reading.

Six selected pages have a text-change watcher. The first successful check establishes a baseline; later checks can flag a text change. This does **not** prove a new feature was released, detect every dynamic-page change, or automatically rewrite the guide. Review a flagged original page before editing its introduction. A failed check retains the last successful baseline.

## 5. Make it yours

| Change | File |
|---|---|
| Stories, learning guides, docs introductions and model map | `content/editorial.json` |
| Publishers and topic keywords | `content/feeds.json` |
| Colours, spacing and typography | `site/assets/style.css` |
| Site shell and branding | `site/index.html` |
| Search, bookmarks, pages and article reader | `site/assets/app.js` |
| Update frequency and digest-attempt limit | `.github/workflows/publish.yml` |

After an editorial change, the next workflow rebuilds the edition. For a local rebuild, run `python scripts/update.py --build-only` from the project folder. To refresh the standalone preview, run `python scripts/build_preview.py`.

Do not rerun `seed_content.py` after making your own editorial changes: it restores the original starter content.

## 6. Common problems

**No workflow appears:** verify the path is exactly `.github/workflows/publish.yml` on the default branch, not `kirish-brief/.github/...` inside another folder.

**Git push is denied:** review repository Actions permissions and branch protection. The workflow preserves its feed cache by committing generated files; it needs an authorised write path. Do not broadly remove organisation safeguards just to publish this site.

**Site works, but new items have no explanation:** that is normal in default mode. Optional AI digests need both the secret and model variable, enough source text, a supported model and successful API access.

**One feed fails:** inspect its message under Sources & updates, check the publisher’s current official feed and update `content/feeds.json`. Do not bypass an access restriction. Other successful sources can still update.

**Documentation watcher fails:** some sites restrict automated access or render their content with JavaScript. The site still links to the official page; a failed watcher is not presented as a successful check.

**My bookmarks disappeared:** bookmarks live only in that browser/origin. They do not sync across devices. Private browsing, blocked storage, clearing browser data or moving from a local preview to a public URL can reset them. Use **How it’s built → Export reading list** to retain a copy.

**Another hosting provider:** the `site` folder can be served as a static website, but uploading that folder alone does not activate the GitHub updating workflow. Use the complete GitHub Pages setup for the included automatic-publishing route.

## 7. Plugins and tools

The website includes a **How it’s built** page. `TOOLS-AND-MAINTENANCE.md` gives the fuller explanation of the built-in research/code tools, GitHub/Vercel discovery, and how to connect a plugin in future.

This is an independent educational project. It is not affiliated with OpenAI and is not personalised financial or medical advice. The initial source mix is English-language and mostly US/European, with some international applications; it is not comprehensive global reporting.
