def categorize_article(article, user_interests):
    """
    Categorize an article based on user interests.
    Args:
        article (dict): Article containing title and summary.
        user_interests (list): List of user interests.
    Returns:
        bool: True if the article is relevant, False otherwise.
    """
    article_text = preprocess_text(article["title"] + " " + article["summary"])
    interest_texts = [preprocess_text(interest) for interest in user_interests]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([article_text] + interest_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    max_score = max(similarity_scores[0])
    print(f"Article: {article['title']}, Max Similarity Score: {max_score}")  # Debugging
    return max_score > 0.1  # Lower threshold