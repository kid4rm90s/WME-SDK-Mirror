# WME SDK Docs — Update Workflow Guide

## Overview

There are **7 scripts**, run in this order every time you update the SDK mirror:

```text
1. cleanup.py              <- wipe old .md output from scripts/ and ../source/
2. build-url-list.py       <- discover all page URLs from the live SPA
3. download-pages.py       <- download fresh HTML files
4. extract-to-md.py        <- convert HTML -> individual .md files
5. create-grouped-md-files.py  <- bundle .md files for LLM use
6. copy-to-source.py       <- sync fresh .md files to ../source/ for version control
7. update-skill.py         <- pull latest WME SDK skill from Claude Code
```

> All scripts must be run from the **`beta/latest/scripts/`** folder as your working directory.
> **Why not HTTrack?** The Waze SDK docs site is a Single-Page App (SPA) — all navigation is built by JavaScript at runtime, so traditional crawlers like HTTrack can only download `index.html` and nothing else. These scripts bypass that by reading TypeDoc's embedded `navigationData` JS bundle directly.

---

## Prerequisites

One-time setup — install Python dependencies once. On Windows, use the `py` launcher:

```powershell
py -m pip install requests beautifulsoup4 lxml
```

---

## Step 1 — `cleanup.py` (Reset old output)

**What it does:** Deletes all `.md` files and `-clean.html` files from:

- Local `scripts/` subfolders: `classes`, `documents`, `functions`, `interfaces`, `modules`, `types`, `variables`
- Version-controlled `../source/` subfolders (same list)

This ensures you're working with only fresh files and don't accidentally mix stale output with new.

**When to run it:** Every time before you re-process new HTML.

```powershell
py cleanup.py
```

---

## Step 2 — `build-url-list.py` (Discover all page URLs)

**What it does:** Fetches `assets/navigation.js` from the live site, decodes TypeDoc's
`window.navigationData` (a base64+zlib compressed JSON tree of the entire sidebar),
and walks every node to produce a complete list of all documentation page URLs.

**Output:**

- `url-list.txt` — one full URL per line (used by Step 3)
- `url-list-paths.txt` — relative paths only (useful for diffing against local mirror)

```powershell
py build-url-list.py
```

**Options:**

```powershell
py build-url-list.py --base-url https://www.waze.com/editor/sdk/  # default
py build-url-list.py --out my-urls.txt                            # custom output file
```

---

## Step 3 — `download-pages.py` (Download fresh HTML + TypeScript Definitions)

**What it does:** Reads `url-list.txt` and downloads each HTML page into the correct
local subfolder (`classes/`, `interfaces/`, `types/`, etc.) — exactly the structure
that `extract-to-md.py` expects.

**Also downloads the latest TypeScript definitions:**

- **Source:** `https://web-assets.waze.com/wme_sdk_docs/production/latest/wme-sdk-typings.tgz`
- **Extracts:** `wmeSDK_typedefs.d.ts` → `TypeDefs/` folder
- **Keeps in sync:** Type definitions are always refreshed with the HTML docs on every run

By default runs **incrementally** — skips files that already exist locally. Use
`--force` to re-download everything.

```powershell
py download-pages.py
```

**Options:**

```powershell
py download-pages.py --dry-run     # preview what would be saved, no files written
py download-pages.py --force       # re-download all files even if they exist
py download-pages.py --no-typedefs # skip the typings tarball download
py download-pages.py --delay 0.5   # seconds between requests (default: 0.3)
```

**TypeDefs notes:**

- `wmeSDK_typedefs.d.ts` — Extracted from the tarball above (kept up-to-date automatically)
- `geojson_typeddefs.d.ts` — Sourced separately, not updated by this script

---

## Step 4 — `extract-to-md.py` (HTML -> Markdown)

**What it does:** Reads every `.html` file in the root `latest/` folder and all
subfolders, parses the TypeDoc HTML structure using BeautifulSoup, and writes a
matching `.md` file next to each `.html` file.

It handles:

- Class/interface/type/function pages -> structured Markdown with TypeScript code blocks
- `modules.html` -> table of contents with `.md` links
- `documents/CHANGELOG.html` -> clean changelog Markdown
- Adds YAML frontmatter to every file (`title`, `source`, `created`, `tool`, `notes`)

```powershell
py extract-to-md.py
```

**Output:** One `.md` file per `.html` file, placed alongside the source HTML in each subfolder.

---

## Step 5 — `copy-to-source.py` (Sync to Version Control)

**What it does:** Copies all freshly generated `.md` files from `scripts/` subfolders into the corresponding `../source/` subfolders for version control.

**Why needed:** The pipeline regenerates files in `scripts/` (temporary working directory), but `source/` is the version-controlled archive. This script ensures git tracks the latest documentation with current `created:` dates.

```powershell
py copy-to-source.py
```

**Output:** All `.md` files from `scripts/{classes,documents,functions,interfaces,modules,types,variables}/` copied to `../source/` with preserved metadata (timestamps, content).

---

## Step 6 — `create-grouped-md-files.py` (Bundle for LLM)

**What it does:** Takes all the individual `.md` files from Step 4 and assembles them into the `docs/` folder.

| Output file       | Source                                                       |
| ----------------- | ------------------------------------------------------------ |
| `classes.md`      | All `.md` files from `classes/`                              |
| `modules.md`      | All `.md` files from `modules/`                              |
| `types.md`        | All `.md` files from `types/`                                |
| `interfaces.md`   | All `.md` files from `interfaces/`                           |
| `variables.md`    | All `.md` files from `variables/`                            |
| `functions.md`    | All `.md` files from `functions/`                            |
| `changelog.md`    | Copied from `documents/CHANGELOG.md`                         |
| `*.md` (typedefs) | Wraps each `.d.ts` from `TypeDefs/` in a markdown code block |
| Guide `.md` files | Copied from `guides/`                                        |
| External docs     | Copied from `externalDocs/`                                  |
| `index.md`        | Master index with TOC, SDK version, and source guide         |

```powershell
py create-grouped-md-files.py
```

---

## Step 7 — `update-skill.py` (Sync WME SDK Skill with Fallback Chain)

**What it does:** Pulls the latest WME SDK skill from your Claude Code skills directory
(`~/.claude/skills/wme-sdk/SKILL.md`) and saves a copy to the local `skills/` folder.

**Also injects a fallback chain** for documentation discovery:

- **Primary:** Local docs at `../../docs/` (works if repo is cloned, offline-friendly)
- **Fallback:** GitHub Pages at `https://kid4rm90s.github.io/WME-SDK-Mirror/docs/` (works anywhere with internet)

This keeps your skill versioned alongside the SDK documentation it references. The skill will reference
local docs first, but gracefully fall back to GitHub Pages if the repo isn't cloned.

**Output:**

- `skills/SKILL.md` — Copy of your WME SDK skill with fallback chain injected

The script compares content before writing — if the skill hasn't changed, it skips the write
and reports `[OK]`.

```powershell
py update-skill.py
```

**Options:**

```powershell
py update-skill.py --skill-path C:\custom\path\to\SKILL.md  # custom skill location
```

**Fallback Chain Details:**

When the skill runs:

- **With repo cloned:** Uses local `../../docs/` paths (no internet needed)
- **Without repo cloned:** References `https://kid4rm90s.github.io/WME-SDK-Mirror/docs/` (works online)

This approach ensures the skill always has access to documentation, whether you're working with
a local clone or using it standalone.

> **Note:** If the skill is not found at the default location (`~/.claude/skills/wme-sdk/SKILL.md`),
> the script reports an error. Verify the skill exists or use `--skill-path` to specify a custom location.

---

## Full Run (Copy-Paste)

```powershell
cd production/latest/scripts
py cleanup.py; py build-url-list.py; py download-pages.py --force; py extract-to-md.py; py copy-to-source.py; py create-grouped-md-files.py; py update-skill.py
```

**Note:** The `--force` flag tells `download-pages.py` to re-download all files even if they already exist locally, ensuring a completely fresh snapshot.

---

## What Gets Updated

After the run, you'll have:

**Documentation (in `docs/`):**

- `index.md` — start here; has the TOC and source guide
- `classes.md`, `interfaces.md`, `types.md`, `functions.md`, `variables.md`, `modules.md`
- `changelog.md`
- `*.md` typedef files (wrapping the `.d.ts` sources)
- Guide files (`how-to-get-started-with-the-wmeSDK.md`, `migration-guide.md`, etc.)

**Skill (in `skills/`):**

- `SKILL.md` — Your WME SDK skill, ready to use with Claude Code

Load the documentation files into your LLM context (docs, Claude, etc.) for complete,
up-to-date SDK reference. The skill is automatically available in your `~/.claude/skills/`
when you develop WME scripts.
