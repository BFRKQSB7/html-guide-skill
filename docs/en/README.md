# html-guide-skill

[**中文简体**](./../README.md) | **English**

Automatically turn any content (conversation answers, notes, code, project explanations, topics, URLs) into a **self-contained, interactive, printable, modern-looking** HTML guide document — tutorials, guides, explainer pages, manuals, learning paths; the page structure adapts to the content.

## What it does

Give Claude a topic, a note, or a line like "turn what I just explained into a nice HTML page", and it produces a **single `.html` file**:

- **Self-contained single file** — CSS / JS / icons all inlined, zero external CDN / fonts / images; double-click to open offline, prints cleanly to PDF
- **Web-verified** — facts, commands, versions and config are verified online first, with **clickable sources** at the page bottom (inline `[1]` jumps straight there)
- **Structure-adaptive** — auto-detects the document type: how-to tutorial / knowledge explainer / comparison / quick reference / code guide

Built-in capabilities (from the skeleton, nothing to hand-write):

| Capability | Description |
|---|---|
| Syntax highlighting | Code blocks colored like an editor (Python/Bash/JS/TS/JSON/SQL/HTML/CSS) |
| Light/dark toggle | ☀️/🌙 top-right, follows system by default; manual switch applies to this session only (not remembered); 0.3s color transition (respects reduced motion) |
| Print / PDF | 🖨️ top-right, `@media print` designed for export |
| Back to top | ↑ bottom-right, appears on scroll |
| Auto TOC | two-level table of contents + scroll-highlighted current position + `aria-current` |
| Citation jump | superscript `[n]` in text clickable to sources (JS scroll under `file://`, no security errors) |
| Section search | `Ctrl+K` opens section search — type to filter, keyboard navigation |
| Heading anchors | hover shows `¶` for deep-linking to subsections |
| Reading progress bar | thin top bar grows with scroll |
| Reading time estimate | hero read-time computed from body length |
| Decision quiz | picks give an instant conclusion (comparison pages) |
| Cheat-sheet search | sticky search box on reference tables, live filtering |
| Progressive disclosure | `<details>` for optional/advanced content without breaking the main flow |
| Code line numbers | optional `<pre class="linenos">`, copy excludes numbers |
| Terminal badge | `>_` rounded box marks command-line content |
| Chinese emphasis | `<span class="em">` standard Chinese emphasis |
| Score bar chart | horizontal bars + score table for comparison/review pages (pure CSS, no external libs) |
| Donut chart | shares/composition (vendor share, difficulty split) via conic-gradient + legend |
| Accessibility baseline | underlined links, `:focus-visible` rings, skip-link, `prefers-reduced-motion` |
| Warm paper light theme | soft non-glaring background |
| 9 visual themes | newspaper / magazine / minimal / Swiss International / book / brutalist / terminal / dark-tech… (designer lineage: swiss·Müller-Brockmann, book·Tschichold), auto light/dark inversion, one `data-style` attribute, live theme preview |
| Card layouts | `assets/card-template.html` ships 6 card layouts (data / opinion / headline / data-grid / poster / steps) × 9 styles, 1200×630 share cards for channels that can't take HTML; 2× hi-res export (`--force-device-scale-factor=2`, 2400×1260) |
| A4 pagination | `scripts/make_a4.py` splits a finished page into same-size **A4** images — tables/charts stay intact, breaks at sentence ends, author footer + page numbers, centered ending; `--scale` adjusts export resolution (1.5× recommended → 1191×1684) |
| Full-page long shot | long screenshot (Step 6.1): hides interactive widgets, **body centered + enlarged** to fill the page (`!important` to override theme rules), one screen shows it all |

## Installation

> The repo **root is the skill itself** (`SKILL.md` at the repo root), so the **Source code (zip)** on the Releases page IS the complete skill package — use it directly, no separate zip asset needed.

### From Releases

1. Open [Releases](https://github.com/BFRKQSB7/html-guide-skill/releases) and pick the latest version
2. Download **Source code (zip)** (GitHub generates it per version; its contents are that version's full skill files)
3. Extract → put the extracted folder into the skills directory (**the target folder must be named `html-guide`**, and `SKILL.md` directly inside):

| Platform | Location |
|----------|----------|
| Windows | `%USERPROFILE%\.claude\skills\html-guide` |
| macOS / Linux | `~/.claude/skills/html-guide` |

### Other install methods

- Copy the repo's `SKILL.md` + `references/` + `assets/` + `scripts/` + `evals/` straight into `~/.claude/skills/html-guide/`
- Or install from this repo inside Claude Code with `/plugin` or `/install-github-repo`

Restart Claude Code after installing — "把这段内容做成 HTML" will then trigger it.

Before first use, copy `user-config.example.md` to `user-config.md` and fill in your local proxy port
(for online verification; if unset it falls back to the system proxy / environment variables). `user-config.md` is machine-local and not committed.

## How it triggers

It activates automatically when you say any of the following:

- "Turn this content into a nice HTML tutorial / guide / explainer"
- "Organize XX into a web page"
- "Explain this project clearly and make it into a printable HTML document"
- English: "make an HTML guide", "render this as HTML", "create an interactive tutorial page"

## Directory structure

```
html-guide/
├── SKILL.md                    # main flow (receive → classify → verify online → write → self-check & deliver)
├── user-config.example.md      # personal config template (copy to user-config.md, fill proxy port)
├── references/
│   ├── design-system.md        # visual design system + anti-AI-flavor rules + component library
│   ├── structure-guide.md      # document type → page structure mapping
│   └── search-guide.md         # online search & proxy fallback (proxy port in user-config.md)
├── assets/
│   ├── skeleton.html           # reusable skeleton template (inlined CSS/JS, all interactions + 9 themes)
│   └── card-template.html      # share-card template (6 layouts × 9 styles, 1200×630)
├── scripts/
│   ├── check_html.py           # output self-check (self-contained/print/TOC/highlight/a11y…)
│   └── make_a4.py              # A4 pagination (long text → uniform A4 images, tables intact)
└── evals/                      # evaluation cases (skill-creator spec)
```

## Verification

Across 6 evaluation rounds (with skill-comparison baseline), 6 case types pass at 100% assertion rate; core interactions (syntax highlighting, TOC, citation jumps, light/dark, sticky search, decision quiz, theme transitions, Ctrl+K) are all verified by real headless-Chrome rendering. 9 themes × 6 card layouts × light/dark are each checked via headless render (background/accent/alignment/no-overflow), and the A4 pagination script is tested on real finished pages.

## License

MIT
