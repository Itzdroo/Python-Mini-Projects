import requests
from bs4 import BeautifulSoup

def scrape_google_news(query="AI machine learning"):
    """
    Scrapes the latest news headlines from Google News related to a given query.

    Parameters:
        query (str): The topic you want to search for (e.g., "LLM NLP", "artificial intelligence")

    Returns:
        list of dicts: Each dict contains 'title', 'link', and 'source' of a news item
    """

    # Set headers to avoid being blocked by Google
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Format search URL for Google News (news-specific with site:news.google.com)
    search_url = f"https://www.google.com/search?q={query}+site:news.google.com&tbm=nws"

    # Send the GET request
    response = requests.get(search_url, headers=headers)

    # Parse the response with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    # Google News cards have this class 'dbsr'
    for item in soup.select("div.dbsr"):
        try:
            # Extract title, link, and source
            title = item.select_one("div.JheGif.nDgy9d").text
            link = item.a["href"]
            source = item.select_one("div.XTjFC.WF4CUc").text

            results.append({
                "title": title,
                "link": link,
                "source": source
            })
        except Exception as e:
            # Skip malformed entries
            print(f"Skipping an item due to error: {e}")
            continue

    return results

# =============================
# Example usage
# =============================
if __name__ == "__main__":
    # Customize your search topic here
    topic = "LLM NLP artificial intelligence"
    news_data = scrape_google_news(topic)

    # Print results in a clean format
    print(f"\n📰 Top News on: {topic}\n{'='*50}")
    for i, item in enumerate(news_data, 1):
        print(f"{i}. {item['title']} ({item['source']})")
        print(f"   {item['link']}\n")
