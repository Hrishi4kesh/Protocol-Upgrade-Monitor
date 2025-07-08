# config.py

from dotenv import load_dotenv
import os

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
POLYGONSCAN_API_KEY = os.getenv("POLYGONSCAN_API_KEY")
ARBISCAN_API_KEY = os.getenv("ARBISCAN_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
COINGECKO_URL = "https://api.coingecko.com/api/v3"
DEFI_LLAMA_URL = "https://api.llama.fi"
