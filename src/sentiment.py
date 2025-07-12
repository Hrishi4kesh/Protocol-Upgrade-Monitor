import requests
import logging
from config import TWITTER_BEARER_TOKEN
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import time
import snscrape.modules.twitter as sntwitter


nltk.download('vader_lexicon')

HEADERS = {
    "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
}


# def fetch_tweets(query, limit=10):
#     tweets = []
#     try:
#         command = ["snscrape", "--max-results", str(limit), "twitter-search", query]
#         result = subprocess.run(command, capture_output=True, text=True, check=True)
#         for line in result.stdout.strip().split("\n"):
#             if line:
#                 tweets.append(line)
#     except subprocess.CalledProcessError as e:
#         print("[ERROR] snscrape CLI failed:", e)
#     return tweets

def analyze_sentiment():
    print("[WARNING] Twitter scraping disabled. Using mock sentiment.")
    
    # You can randomize or hardcode these as needed
    sentiment_score = 0.3
    sentiment_label = 'Neutral'
    
    return sentiment_score, sentiment_label
