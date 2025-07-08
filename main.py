# main.py

from src.monitor import monitor_blockchain
from src.sentiment import analyze_sentiment
from src.volatility import predict_volatility
from src.liquidity import forecast_liquidity
from src.governance import fetch_proposals

def run_monitor():
    monitor_blockchain()
    analyze_sentiment()
    predict_volatility()
    forecast_liquidity()
    fetch_proposals()

if __name__ == "__main__":
    run_monitor()
