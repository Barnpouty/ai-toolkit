# AI Toolkit 2026 — storefront

A Flask landing page that sells two PDF guides:

- **AI Starter Kit 2026** — *50+ AI Tools Every Student & Young Professional Should Know in 2026* (20 pages)
- **Bonus guide** — *AI Toolkit for Students & Young Professionals* (30 pages)

Every purchase button sends the visitor to the external checkout at
`https://checkout.escalepay.com/1318780`. The site never handles payments or card data.

## Project structure

```text
ai-toolkit/
├── app.py              Flask app (routes, headers, caching). Vercel entry point: `app`
├── content.py          All product copy, taken from the two PDFs — edit text here
├── requirements.txt    Flask only
├── vercel.json         Sends every request to the Flask function
├── .env.example        Environment variables you can set
├── templates/
│   ├── base.html       <head>, SEO/Open Graph tags, nav, footer
│   ├── index.html      The landing page
│   ├── success.html    /thank-you — optional post-payment return page
│   ├── legal.html      /privacy and /terms (placeholders — replace before launch)
│   ├── 404.html
│   └── partials/       nav.html, footer.html
└── static/
    ├── css/style.css
    ├── js/main.js      ~150 lines, no libraries
    └── images/         Covers, 6 page previews, favicon, OG image (all generated from the PDFs)
```

## Routes

| Path | Purpose |
|---|---|
| `/` | Landing page |
| `/checkout` | Short link that 302-redirects to `CHECKOUT_URL` (handy for social bios) |
| `/thank-you` | Optional return page after payment (not indexed) |
| `/privacy`, `/terms` | Legal placeholders |
| `/robots.txt`, `/sitemap.xml` | SEO |

## Environment variables

| Name | Required | Default | Notes |
|---|---|---|---|
| `CHECKOUT_URL` | No | `https://checkout.escalepay.com/1318780` | Every CTA uses this |
| `SITE_URL` | Recommended | request host | Your public URL, no trailing slash. Used for canonical and Open Graph URLs |
| `CONTACT_EMAIL` | No | empty | When set, shown in the footer, FAQ and thank-you page |

`VERCEL_GIT_COMMIT_SHA` is set by Vercel automatically and is used to version static files,
so CSS/JS/images are cached for a year and refreshed on every deploy.

## 1. Install

Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Run locally

```bash
flask --app app run --debug
# or: python app.py
```

Open http://127.0.0.1:5000

## 3. Test locally

- Click every "Get the…" button: each should open `checkout.escalepay.com/1318780`.
- Visit `/checkout` — it should redirect to the same URL.
- In the "Organised by the work you're doing" section, use the mouse and the arrow keys to switch categories.
- Resize to 390px wide (or use device mode in DevTools): the menu button, the category tabs and the page previews should all work.
- Turn on "reduce motion" in your OS: entrance and reveal animations should stop.
- Quick automated check:

```bash
for p in / /checkout /thank-you /privacy /terms /robots.txt /sitemap.xml /missing; do
  curl -s -o /dev/null -w "$p %{http_code}\n" http://127.0.0.1:5000$p
done
# expected: 200, 302, 200, 200, 200, 200, 200, 404
```

## 4. Deploy to Vercel

**From GitHub (recommended)**

1. Push this folder to a GitHub repository. `.gitignore` already blocks `*.pdf`, so the paid guides are never committed.
2. In Vercel: **Add New → Project**, import the repository.
3. Framework preset: **Other** (the `vercel.json` handles the build). Leave build/output settings empty.
4. Deploy.

**From the command line**

```bash
npm i -g vercel
vercel          # preview deployment
vercel --prod   # production
```

## 5. Configure environment variables

Vercel → your project → **Settings → Environment Variables**. Add `SITE_URL` (e.g. `https://yourdomain.com`)
and, if you want, `CONTACT_EMAIL` or a different `CHECKOUT_URL`. Redeploy after changing them.

## 6. Verify production

- Open the production URL and check that the page, fonts and cover images load.
- Click a CTA and confirm you land on the EscalePay checkout.
- Visit `https://yourdomain.com/checkout` and `/robots.txt`.
- View source and confirm `<link rel="canonical">` and `og:url` use your domain (if not, set `SITE_URL`).
- Paste the URL into a link-preview tool (e.g. opengraph.xyz) to check the social card.
- Run Lighthouse in Chrome DevTools on mobile.

## Before you launch

- **Replace `/privacy` and `/terms`** with your real legal text (`templates/legal.html`).
- **Never put the PDFs in `static/`** — anything there is publicly downloadable. Deliver them through EscalePay.
- If EscalePay lets you set a return URL after payment, point it to `https://yourdomain.com/thank-you`.
- Add a contact email via `CONTACT_EMAIL` so buyers can reach you.

## Editing content

All copy lives in `content.py` and was taken from the PDFs. If you update a guide, update this file to match —
don't add claims the guides don't make.
