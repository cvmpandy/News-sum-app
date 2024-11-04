# app.py
from flask import Flask, render_template, request
from services.news_api import fetch_news
from services.article_scraper import scrape_article_content
from services.summarizer import summarize_text
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    summaries = []
    page = int(request.args.get("page", 1))
    category = None

    if request.method == "POST":
        category = request.form.get("category")
        # limit = int(request.form.get("article_limit", 10))
        articles = fetch_news(category)  # Fetch articles with URLs
        valid_articles=[]
        # Summarize each article's full content
        for article in articles:
            full_content = scrape_article_content(article["url"])  # Get full content

            if full_content:  # If content is not None or empty

                valid_articles.append(article) 

                full_content = full_content[:2000]
                summary = summarize_text(full_content)  # Summarize the full content
                # summary = full_content  # Summarize the full content
                summaries.append({"title": article["title"], "summary": summary})
        
        articles = valid_articles
        # Store summaries in a session or local variable if needed for persistent pagination
        app.config["summaries"] = summaries

    else:
        # Use stored summaries if the user is paginating
        summaries = app.config.get("summaries", [])

    # Calculate pagination variables
    per_page = 5
    total_pages = math.ceil(len(summaries) / per_page)
    paginated_summaries = summaries[(page - 1) * per_page : page * per_page]

    return render_template(
        "index.html",
        summaries=paginated_summaries,
        category=category,
        page=page,
        total_pages=total_pages,
    )


if __name__ == "__main__":
    app.run(debug=True)
