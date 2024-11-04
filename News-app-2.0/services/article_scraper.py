# services/article_scraper.py
import requests
from bs4 import BeautifulSoup


def scrape_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Modify the selector based on the structure of the articles you're scraping
            paragraphs = soup.find_all("p")  # Get all paragraph elements
            full_content = "\n".join(
                [para.get_text() for para in paragraphs]
            )  # Join all paragraph texts
            return full_content.strip()
        else:
            raise Exception(f"Failed to fetch article from {url}")
    except Exception as e:
        print(e)
        return ""
