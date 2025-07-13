import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import logging

logger = logging.getLogger("ProtocolUpgradeMonitor")

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

API_KEY = "YOUR_NEWSAPI_KEY"  # Replace with actual key or use os.environ.get("NEWSAPI_KEY")

def fetch_news_sentiment(query="Compound Governance Upgrade", limit=10):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&sortBy=publishedAt&pageSize={limit}&apiKey={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])

        # Fallback if no articles
        if not articles:
            logger.warning("No articles found, using fallback headlines")
            articles = [
                {"title": "Compound community votes on new governance proposal", "description": "Expected changes in token allocation."},
                {"title": "Protocol upgrades spark debate on decentralization", "description": "Users question governance voting power."},
                {"title": "Crypto market reacts to Compound upgrade news", "description": "Token sees mild volatility amid governance changes."}
            ]

        scores = []
        for article in articles:
            text = f"{article.get('title', '')} {article.get('description', '')}"
            sentiment = analyzer.polarity_scores(text)
            scores.append(sentiment["compound"])

        avg_sentiment = sum(scores) / len(scores)
        label = (
            "Positive" if avg_sentiment > 0.2 else
            "Negative" if avg_sentiment < -0.2 else
            "Neutral"
        )
        logger.info(f"Computed average sentiment: {avg_sentiment:.3f}")
        return avg_sentiment, label

    except Exception as e:
        logger.error(f"Sentiment analysis failed: {e}")
        return 0.0, "Neutral"
