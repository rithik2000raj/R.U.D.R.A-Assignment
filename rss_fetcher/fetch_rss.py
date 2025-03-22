import feedparser

def fetch_articles(rss_url):
    """
    Fetch articles from an RSS feed.
    Args:
        rss_url (str): URL of the RSS feed.
    Returns:
        list: List of articles, each containing title, summary, link, and published date.
    """
    print(f"Fetching articles from: {rss_url}")  # Debugging
    feed = feedparser.parse(rss_url)
    if feed.entries:
        print(f"Found {len(feed.entries)} articles.")  # Debugging
    else:
        print("No articles found in the feed.")  # Debugging

    articles = []
    for entry in feed.entries:
        article = {
            "title": entry.title if hasattr(entry, "title") else "No title available",
            "summary": entry.summary if hasattr(entry, "summary") else "No summary available",
            "link": entry.link if hasattr(entry, "link") else "No link available",
            "published": entry.published if hasattr(entry, "published") else "No date available"
        }
        articles.append(article)
    return articles