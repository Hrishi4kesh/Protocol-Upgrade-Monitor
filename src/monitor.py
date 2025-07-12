# src/monitor.py

from web3 import Web3
from config import INFURA_PROJECT_ID
from src.utils import load_contract, decode_logs
import json
import os


def monitor_blockchain():
    print("Monitoring Compound governance contract...")

    # Connect to Ethereum mainnet using Infura
    infura_url = f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"
    print(f"[DEBUG] Connecting to: {infura_url}")

    web3 = Web3(Web3.HTTPProvider(infura_url))

    if not web3.is_connected():
        raise ConnectionError("Failed to connect to Ethereum via Infura.")



    # Load ABI
    with open("data/compound_abi.json") as f:
        abi = json.load(f)

    # Setup contract
    contract_address = "0xc0Da02939E1441F497fd74F78cE7Decb17B66529"
    contract = web3.eth.contract(address=contract_address, abi=abi)

    # Define block range
    latest = web3.eth.block_number
    from_block = 18000000
    to_block = 18010000


    # Build event filter
    filter_params = {
        'fromBlock': from_block,
        'toBlock': to_block,
        'address': contract_address
    }

    print(f"Fetching logs from block {from_block} to {to_block}")
    logs = web3.eth.get_logs(filter_params)
    print(f"[DEBUG] Fetched {len(logs)} logs.")
    print("Sample log:", logs[0] if logs else "No logs.")

    decoded = decode_logs(logs, contract, web3)
    print(f"Decoded {len(decoded)} governance events")

    for d in decoded[:3]:  # print only first 3
        print(d)