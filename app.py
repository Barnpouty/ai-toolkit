"""
AI Toolkit — storefront for the AI Starter Kit 2026 and its bonus guide.

Runs locally with `flask --app app run` and on Vercel as a Python serverless
function (see vercel.json). The module-level `app` object is the entry point.
"""

import os
from datetime import date

from flask import Flask, Response, redirect, render_template, request, url_for

import content

DEFAULT_CHECKOUT_URL = "https://checkout.escalepay.com/1318780"


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")

    app.config.update(
        CHECKOUT_URL=os.environ.get("CHECKOUT_URL", DEFAULT_CHECKOUT_URL),
        # Public origin used for canonical/OG URLs, e.g. https://aitoolkit.example.com
        SITE_URL=os.environ.get("SITE_URL", "").rstrip("/"),
        # Optional. When empty, the footer shows no contact address.
        CONTACT_EMAIL=os.environ.get("CONTACT_EMAIL", ""),
        # Changes on every Vercel deploy, so static URLs can be cached forever.
        ASSET_VERSION=(os.environ.get("VERCEL_GIT_COMMIT_SHA") or "dev")[:8],
    )

    def site_url() -> str:
        return app.config["SITE_URL"] or request.url_root.rstrip("/")

    @app.context_processor
    def inject_globals():
        return {
            "checkout_url": app.config["CHECKOUT_URL"],
            "contact_email": app.config["CONTACT_EMAIL"],
            "site_url": site_url(),
            "product": content.PRODUCT,
            "year": date.today().year,
            "asset": lambda path: url_for("static", filename=path, v=app.config["ASSET_VERSION"]),
        }

    @app.get("/")
    def index():
        return render_template(
            "index.html",
            categories=content.CATEGORIES,
            workflows=content.WORKFLOWS,
            quick_starts=content.QUICK_STARTS,
            bonus_rule=content.BONUS_RULE,
            when_free=content.WHEN_FREE,
            when_paid=content.WHEN_PAID,
            decision_guide=content.DECISION_GUIDE,
            decision_guide_total=content.DECISION_GUIDE_TOTAL,
            stacks=content.STACKS,
            bonus_chapters=content.BONUS_CHAPTERS,
            rules=content.RULES,
            closing_quote=content.CLOSING_QUOTE,
            previews=content.PREVIEWS,
            faq=content.FAQ,
        )

    @app.get("/checkout")
    def checkout():
        """Short shareable link (/checkout) that forwards to the external checkout."""
        return redirect(app.config["CHECKOUT_URL"], code=302)

    @app.get("/thank-you")
    def thank_you():
        """Optional return page — only used if EscalePay is set to redirect here after payment."""
        return render_template("success.html")

    @app.get("/privacy")
    def privacy():
        return render_template("legal.html", page="privacy")

    @app.get("/terms")
    def terms():
        return render_template("legal.html", page="terms")

    @app.get("/robots.txt")
    def robots():
        body = f"User-agent: *\nAllow: /\nDisallow: /thank-you\n\nSitemap: {site_url()}/sitemap.xml\n"
        return Response(body, mimetype="text/plain")

    @app.get("/sitemap.xml")
    def sitemap():
        base = site_url()
        urls = "".join(f"<url><loc>{base}{p}</loc></url>" for p in ("/", "/privacy", "/terms"))
        xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
        return Response(xml, mimetype="application/xml")

    @app.get("/favicon.ico")
    def favicon():
        return redirect(url_for("static", filename="images/favicon.svg"), code=301)

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html"), 404

    @app.after_request
    def headers(response: Response) -> Response:
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")

        if request.path.startswith("/static/"):
            if request.args.get("v") and app.config["ASSET_VERSION"] != "dev":
                # Versioned URL: safe to cache in browsers and on Vercel's CDN for a year.
                response.headers["Cache-Control"] = "public, max-age=31536000, s-maxage=31536000, immutable"
            else:
                response.headers["Cache-Control"] = "public, max-age=3600"
        elif response.mimetype == "text/html" and response.status_code == 200:
            # Let Vercel's CDN hold rendered pages briefly; every deploy invalidates it.
            response.headers["Cache-Control"] = "public, max-age=0, s-maxage=3600, stale-while-revalidate=86400"
        return response

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))
