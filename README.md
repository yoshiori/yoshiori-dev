# yoshiori.dev

Personal resume site built with [Astro](https://astro.build) and deployed on [Cloudflare Pages](https://pages.cloudflare.com).

## Stack

- **Framework**: Astro (static build)
- **Styling**: Tailwind CSS + custom CSS
- **Hosting**: Cloudflare Pages
- **Domain**: yoshiori.dev (managed by Cloudflare)

## Development

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # outputs to dist/
```

## SpeakerDeck sync

Talks are stored in `src/content/talks.json` and synced weekly via GitHub Actions.

To fetch manually:
```bash
python scripts/fetch_speakerdeck.py
```

The workflow (`.github/workflows/fetch-speakerdeck.yml`) runs every Sunday and opens a commit if new talks are found. Cloudflare Pages detects the push and redeploys automatically.

## Cloudflare Pages settings

| Setting | Value |
|---|---|
| Framework preset | Astro |
| Build command | `npm run build` |
| Output directory | `dist` |
