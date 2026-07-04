# Profile setup guide

This document explains every external dependency the profile README relies on,
what you must enable, and how to customize each piece. Work through the
checklist once; afterwards the profile maintains itself.

## 1. Widget stack (and why these, in 2026)

| Widget | Project | Endpoint | Notes |
|---|---|---|---|
| General stats, Top languages, Repo pins | [stats-organization/github-stats-extended](https://github.com/stats-organization/github-stats-extended) | `github-stats-extended.vercel.app` | Actively maintained successor of `anuraghazra/github-readme-stats`, which is no longer updated. URL-compatible: only the domain differs. |
| Streak | [DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) | `streak-stats.demolab.com` | Still the standard streak widget; maintained. |
| Activity graph | [ashutosh00710/github-readme-activity-graph](https://github.com/ashutosh00710/github-readme-activity-graph) | `github-readme-activity-graph.vercel.app` | 31-day contribution line chart. |
| Contribution snake | [Platane/snk](https://github.com/Platane/snk) (`@v3`) | generated in-repo | Rendered by a GitHub Actions workflow, not an external service. |
| Badges | [shields.io](https://shields.io) + [simpleicons.org](https://simpleicons.org) | `img.shields.io` | No setup needed. |

All of the hosted widgets are **read-only image services**: they only see your
public GitHub data, require no token from you, and can be removed by deleting
an `<img>`/`<picture>` block from the README.

**Visitor counter:** deliberately omitted. Hit counters are widely considered
dated on engineering profiles and the numbers are trivially inflated. A
commented-out `komarev.com/ghpvc` badge is left in the README if you ever want
one — it is the only maintained option worth considering.

## 2. One-time checklist

1. **Merge this branch** so `README.md` and `.github/workflows/generate-snake.yml`
   land on `main` of `oligiochi/oligiochi`.
2. **Enable GitHub Actions** (usually already on): repository *Settings →
   Actions → General* → "Allow all actions and reusable workflows".
3. **Check workflow write permission**: same page, *Workflow permissions*.
   The workflow declares `permissions: contents: write` itself, which works
   with the default settings; if your account has "Read repository contents
   permission" forced org-wide, switch it to "Read and write permissions".
4. **Run the snake once manually**: *Actions* tab → "Generate contribution
   snake" → *Run workflow*. This creates the `output` branch that the README
   images point to. Until this first run the snake section shows a broken
   image. Afterwards the daily cron keeps it fresh — no PAT, no secrets.
5. **Fill in the placeholders** marked `CUSTOMIZE:` in `README.md`:
   - your display name in the header (optional),
   - your LinkedIn handle in the Connect section,
   - the four repository names under Featured Projects (cards render an error
     image until the repo exists and is public),
   - trim the Backend / Databases / OS badge rows to what you actually use.
6. **Private contributions (optional)**: the hosted widgets only count public
   activity. If you want private contributions included, self-host
   `github-stats-extended` on your own free Vercel account with a PAT — see
   its README ("Deploy on your own"). The PAT needs no scopes beyond `repo`
   read if you include private repos. This is entirely optional; do not put a
   PAT anywhere in this repository.

## 3. Color palette

Everything uses GitHub's own accent colors so the profile blends into the
site chrome instead of fighting it:

| Role | Dark theme | Light theme |
|---|---|---|
| Accent (titles, icons, lines, snake-adjacent) | `#58A6FF` | `#0969DA` |
| Primary text | `#C9D1D9` | `#24292F` |
| Muted text (labels, dates) | `#8B949E` | `#57606A` |
| Background | `#0D1117` (or transparent) | `#FFFFFF` (or transparent) |
| Badge background | `#24292e` on both themes | |

Dark/light switching is done with `<picture>` + `prefers-color-scheme`, which
GitHub supports natively in READMEs. The stats cards use a fully transparent
background (`bg_color=00000000`); the streak and activity graph get explicit
backgrounds because those services handle transparency less reliably.

If you change the accent, change it in **every** widget URL (both the dark
`<source>` and light `<img>` variants) and optionally pass `color_snake` to
the snake workflow — the palette table above is the single source of truth.

## 4. Maintenance notes

- **No abandoned actions**: the workflow uses `Platane/snk@v3` and
  `crazy-max/ghaction-github-pages@v4`, both maintained. Avoid the old
  `svg-only` forks and `gautamkrishnar/blog-post-workflow`-era hit counters.
- If a hosted widget ever goes down, the profile degrades gracefully: GitHub
  shows the alt text, nothing else breaks.
- The snake workflow also re-runs on every push to `main`, so editing the
  README refreshes the animation as a side effect.
