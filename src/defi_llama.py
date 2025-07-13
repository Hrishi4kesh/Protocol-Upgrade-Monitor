# src/defi_llama.py

import requests
from src.logger import logger

LLAMA_TVL_URL = "https://api.llama.fi/protocol/{}"

def fetch_tvl(protocol_slug):
    """
    Fetch historical TVL for a protocol from DeFi Llama.
    Returns a list of (timestamp, tvl) tuples, or empty list on failure.
    """
    try:
        resp = requests.get(LLAMA_TVL_URL.format(protocol_slug))
        resp.raise_for_status()
        data = resp.json().get("tvl", [])
        return [(item["date"], item["totalLiquidityUSD"]) for item in data]
    except Exception as e:
        logger.error(f"Failed to fetch TVL data for '{protocol_slug}': {e}")

        return []

def predict_liquidity_shift(protocol_slug="compound"):
    """
    Simple liquidity shift predictor:
    Compares latest TVL vs 7-day ago TVL.
    Returns one of Increase/Stable/Decrease or 'Unavailable'.
    """
    tvl_data = fetch_tvl(protocol_slug)
    if len(tvl_data) < 8:
        return "Unavailable"

    _, latest = tvl_data[-1]
    _, week_ago = tvl_data[-8]
    if week_ago == 0:
        return "Unavailable"

    change_pct = (latest - week_ago) / week_ago * 100

    if change_pct > 5:
        return "Increase"
    elif change_pct < -5:
        return "Decrease"
    else:
        return "Stable"
