# src/monitor.py

from web3 import Web3
import logging
from config import ETHERSCAN_API_KEY

def monitor_blockchain():
    logging.info("Monitoring Ethereum Blockchain...")

    ETH_RPC = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"
    web3 = Web3(Web3.HTTPProvider(ETH_RPC))

    if web3.isConnected():
        print("Ethereum connected.")
        latest_block = web3.eth.block_number
        print(f"Latest Block: {latest_block}")
    else:
        print("Failed to connect to Ethereum node.")
