#src/monitor.py

from web3 import Web3
from config import INFURA_PROJECT_ID
from src.utils import decode_logs
from src.logger import logger
import json

def get_web3(network):
    if network.lower() == "ethereum":
        return Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))
    elif network.lower() == "polygon":
        # Use official Polygon RPC
        return Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
    elif network.lower() == "arbitrum":
        # Use official Arbitrum RPC
        return Web3(Web3.HTTPProvider("https://arb1.arbitrum.io/rpc"))
    else:
        raise ValueError(f"Unsupported network: {network}")

def get_contract(web3, contract_address):
    with open("data/compound_abi.json") as f:
        abi = json.load(f)
    return web3.eth.contract(address=contract_address, abi=abi)

def monitor_blockchain(contract_address, from_block, to_block, network):
    logger.info(f"Monitoring {network} contract: {contract_address}")
    try:
        web3 = get_web3(network)
        if not web3.is_connected():
            logger.error("Web3 connection failed")
            return []
        contract = get_contract(web3, contract_address)
        logs = web3.eth.get_logs({
            "address": contract_address,
            "fromBlock": from_block,
            "toBlock": to_block
        })
        decoded = decode_logs(logs, contract, web3)
        logger.info(f"Decoded {len(decoded)} governance events")
        return decoded
    except Exception as e:
        logger.error(f"Blockchain monitoring failed: {e}")
        return []
