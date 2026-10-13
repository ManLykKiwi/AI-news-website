# Tools, plugins and the update pipeline

## What was actually used

| Capability | Role in this build | Why |
|---|---|---|
| Built-in web research | Read current first-party news and official documentation | The starter edition should not rely on model memory for current releases. |
| Built-in file/code execution | Wrote HTML/CSS/JS and Python; ran tests | Produces a complete editable project rather than a screenshot of a design. |
| Playwright with Chromium | Exercised the locally embedded preview on desktop and mobile-sized viewports | Checks real navigation, search, dialogs, bookmarks, theme and layout. It is a development test library, not a connected ChatGPT plugin. |
| Plugin Management discovery | Looked up GitHub and hosting integrations, including Vercel | Checked whether an external deployment route was connected. Neither account was connected or used to publish. |

No email, calendar, contacts or private cloud documents were used to populate the public website. The topic choices use the requested engineering/AI/finance interests. The published files contain only a first name, not private conversations or personal records.

## What the website uses after setup

**HTML** supplies the page structure; **CSS** controls the appearance; **JavaScript** handles the reader and browser-only state. Plain files make this small project easier to understand and publish without a browser framework or package-install step.

**Python** reads machine-readable publisher feeds. **GitHub Actions** supplies the scheduled computer that runs Python. **GitHub Pages** serves the resulting public files. These are distinct responsibilities: a hosting service does not automatically invent or refresh the news.

```text
Selected publisher feeds                 Selected documentation pages
          |                                         |
          v                                         v
  Dates / domain checks                    Readable-text fingerprints
  Topic filter / deduplicate               Compare with last good check
          |                                         |
          v                                         |
  Optional feed-only AI digest                      |
  (requires owner’s API credentials)                |
          |                                         |
          +--------------------+--------------------+
                               |
                     Build static edition
                     Preserve previous cache
                               |
                     Deploy with GitHub Pages
                               |
                     Reader opens the website
```

No browser receives the API key. The optional API receives public feed text only, with instructions not to follow instructions inside that text. `store: false` is requested, but do not treat that setting as a universal zero-retention guarantee; consult the provider’s data controls for your API account.

The JSON output schema keeps each digest in the four expected fields. It does not make the explanation true. The updater falls back to a headline when the input or output is unsuitable. Official API guidance: [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs).

## How to use plugins in future

In ChatGPT, open **Plugins**, select the intended plugin, review its included apps and requested permissions, then install it and complete any account connection. Installing a plugin does not bypass the service’s authorisation. Availability varies by account, workspace and device. Installed plugins can be selected with an **@ mention** or used when relevant to a request. [Official OpenAI plugin guide](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

For this project, GitHub is the useful first connection because the included publishing route keeps the code and update workflow there. Vercel is an alternative hosting integration discovered during research; it is not required for the supplied GitHub Pages route.

With the appropriate GitHub connection and supported permissions, useful requests include: “Inspect the update workflow in my kirish-brief repository and tell me why yesterday’s run failed,” or “Prepare a change adding this verified publisher feed.” Review changes before merging. A plugin is not itself evidence that a deployment succeeded; check the actual action result and public URL.

## Maintenance priorities

Check **Sources & updates** and the repository’s **Actions** tab regularly. Verify important claims against the original, especially benchmark scores, policy changes, medical findings and claimed commercial deployments. Broaden the regional source mix deliberately rather than presenting English-language US/European institutions as complete global coverage.

Review the source list when feeds break; remove blocked sources instead of evading restrictions. Revisit introductory docs text when the watcher flags a change. Review dependency/action versions and account permissions periodically. Check API usage when enabling automatic digests.

The included workflow has a six-hourly schedule, but GitHub documents possible delays and inactivity-related disabling. [Schedule reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). Hosting setup follows [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages). OpenAI API usage has [separate billing from ChatGPT](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform).
