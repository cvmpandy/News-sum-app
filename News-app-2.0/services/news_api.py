# services/news_api.py
import requests
from config import NEWS_API_KEY, NEWS_API_URL


def fetch_news(category, country="us"):
    params = {
        "category": category,
        "country": country,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        
        articles = response.json().get("articles", [])
        # Return article titles, URLs, and truncated content
        return [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "publishedAt": article["publishedAt"],
            }
            for article in articles[:5]  # Limit based on the parameter
        ]
    else:
        raise Exception("Failed to fetch news")
