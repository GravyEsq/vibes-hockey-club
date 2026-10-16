# The Vibes Hockey Club

A phone-friendly hockey companion for friends following the Canadiens, Wild, Penguins, Senators and Kraken, with extra attention to Montreal.

## Course, roster guide and quick lookup

- **Reading course:** 18 original chapters. Read in order, resume your last chapter, bookmark pages and mark chapters read.
- **Quick lookup:** 321 short searchable pages about rules, teams, players, coaches, history, health, previous seasons and hockey terms.
- **English–Hebrew glossary:** 93 terms with English definitions and Hebrew names and explanations. Search either language, with or without Hebrew vowel marks.
- **Your Canadiens:** a dedicated roster guide with six players to learn first, all 26 players in the saved snapshot, individual roles and viewing cues, position filters, jersey-number search and a dated line-combination example.
- **Color theme:** choose System, Light or Dark in the header. Your choice is saved on this device; System follows the device’s appearance setting.

Current-season scores are hidden by default. They are excluded from Quick lookup. Historical outcomes are discussed openly. The edition is dated **15 October 2026**; report dates and official source links appear in the app. This is a saved research edition, not an automatically updating news or injury service.

## Privacy and offline use

The website is public and requires no account. Notebook entries, bookmarks, reading progress are stored only in the visitor's browser. They are not committed to this repository or sent to an application server. Data stored at a different website address does not transfer automatically; use the notebook export/import controls to move observations.

Use **Hockey library → Offline reading** to save chapters, roster guides and reference pages. Test offline access before relying on it. Browser storage depends on the device and browser.

## Hosting and source

GitHub Pages publishes the static files under `docs/` from `main`. No package installation or build step is needed. All asset links, the web manifest and service worker use relative paths to support project-site URLs.

`build_content.py` recreates `docs/data.json` from the original course text, `glossary-he.json`, `quick-rules.json` and official NHL JSON snapshots under `research/`. `docs/roster-guide.json` holds the original Canadiens player notes and their edition dates. Published narration and audio downloads have been removed.

This is an independent fan guide, not affiliated with the NHL or its clubs. Team marks belong to their owners and identify the teams. Statistics and reporting link to official NHL sources. Course prose and player watch points are original editorial guidance.
