# main.py

from src.monitor import monitor_blockchain
from src.sentiment import analyze_sentiment
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()


def run_monitor():
    monitor_blockchain()

    sentiment_score, sentiment_label = analyze_sentiment()
    print(f"\n🧠 Sentiment Analysis Score: {sentiment_score:.3f} ({sentiment_label})")



if __name__ == "__main__":
    run_monitor()
