import json
import os
import streamlit as st
from PIL import Image
from rss_fetcher.fetch_rss import fetch_articles
from nlp_categorizer.categorize_articles import categorize_article
from newsletter_generator.generate_newsletter import generate_newsletter

# Load user profiles
def load_user_profiles():
    """
    Load user profiles from JSON file.
    Returns:
        dict: User profiles and RSS feed configurations.
    """
    with open("user_profiles/user_profiles.json", "r") as file:
        return json.load(file)

# Streamlit App
def main():
    # Set page title and icon
    st.set_page_config(page_title="AI-Powered Newsletter Generator", page_icon="📰")

    # Add a header with a newspaper-themed image
    image_path = os.path.join(os.path.dirname(__file__), "assets", "newspaper_icon.png")
    st.image(image_path, width=100)
    st.title("AI-Powered Personalized Newsletter Generator")
    st.markdown("---")

    # Load user profiles and RSS feeds
    data = load_user_profiles()
    users = data["users"]
    rss_feeds = data["rss_feeds"]

    # Dropdown to select user
    user_names = [user["name"] for user in users]
    selected_user = st.selectbox("Select User", user_names)

    # Find the selected user's profile
    user = next((u for u in users if u["name"] == selected_user), None)

    if user:
        st.subheader(f"Generating Newsletter for {user['name']}...")

        # Fetch and filter articles
        articles = []
        for source in user["sources"]:
            rss_url = rss_feeds[source]
            fetched_articles = fetch_articles(rss_url)
            print(f"Fetched {len(fetched_articles)} articles from {source}.")  # Debugging
            articles.extend(fetched_articles)

        # Filter articles based on user interests
        filtered_articles = [
            article for article in articles
            if categorize_article(article, user["interests"])
        ]
        print(f"Filtered {len(filtered_articles)} relevant articles.")  # Debugging

        # Ensure at least 10 articles
        if len(filtered_articles) < 10:
            print("Adding additional articles to meet the minimum requirement.")  # Debugging
            additional_articles = [article for article in articles if article not in filtered_articles]
            filtered_articles.extend(additional_articles[:10 - len(filtered_articles)])

        # Generate and display newsletter
        newsletter = generate_newsletter(user, filtered_articles[:10])  # Limit to 10 articles
        st.markdown(newsletter)

        # Download button for the newsletter
        st.download_button(
            label="Download Newsletter",
            data=newsletter,
            file_name=f"{user['name']}_newsletter.md",
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()