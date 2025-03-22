import feedparser

def fetch_articles(rss_url):
    """
    Fetch articles from an RSS feed.
    Args:
        rss_url (str): URL of the RSS feed.
    Returns:
        list: List of articles, each containing title, summary, link, and published date.
    """
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries:
        article = {
            "title": entry.title,
            "summary": entry.summary,
            "link": entry.link,
            "published": entry.published
        }
        articles.append(article)
    return articles