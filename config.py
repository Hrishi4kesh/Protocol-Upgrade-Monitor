# config.py

import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
POLYGONSCAN_API_KEY = os.getenv("POLYGONSCAN_API_KEY")
ARBISCAN_API_KEY = os.getenv("ARBISCAN_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
API_KEY = os.getenv("NEWS_API_KEY")


COINGECKO_URL = "https://api.coingecko.com/api/v3"
DEFI_LLAMA_URL = "https://api.llama.fi"
