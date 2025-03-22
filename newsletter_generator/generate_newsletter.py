def generate_newsletter(user, articles):
    """
    Generate a personalized newsletter in Markdown format.
    Args:
        user (dict): User profile containing name and interests.
        articles (list): List of relevant articles.
    Returns:
        str: Newsletter in Markdown format.
    """
    newsletter = f"# Personalized Newsletter for {user['name']}\n\n"
    newsletter += "## Top Trending Articles\n"

    for article in articles:
        newsletter += f"1. **{article['title']}**\n"
        newsletter += f"   Summary: {article['summary']}\n"
        newsletter += f"   [Read more]({article['link']})\n\n"

    return newsletter