#main.py

from src.monitor import monitor_blockchain
from src.sentiment import fetch_news_sentiment
from src.alert import generate_alert
from src.risk import compute_risk_score
from src.user_input import get_user_inputs
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

def get_user_config():
    # Example static config, replace with dynamic input as needed
    return get_user_inputs(
        "Ethereum",
        "0xc0Da02939E1441F497fd74F78cE7Decb17B66529",
        18000000,
        18010000,
        "Medium",
        "Governance Proposal",
        "Short-Term",
        "COMP/ETH, DAI/USDC",
        70,
        50
    )

def run_monitor():
    print("📡 Monitoring blockchain for governance votes...\n")
    config = get_user_config()
    events = monitor_blockchain(
        config["contract_address"],
        config["from_block"],
        config["to_block"],
        config["network"]
    )
    sentiment_score, sentiment_label = fetch_news_sentiment()
    print(f"\n🧠 Sentiment Analysis Score: {sentiment_score:.3f} ({sentiment_label})\n")
    for event in events:
        votes = int(event['args']['votes'])
        proposal_id = event['args']['proposalId']
        voter = event['args']['voter']
        tx_hash = event['transactionHash'].hex()
        block = event['blockNumber']
        risk_score, risk_level = compute_risk_score(votes, sentiment_score)
        print(f"""
🚨 Governance Vote Detected 🚨
Proposal ID: {proposal_id}
Voter: {voter}
Votes: {votes}
Sentiment: {sentiment_label} ({sentiment_score:.2f})
Risk Score: {risk_score} ({risk_level})
Tx Hash: {tx_hash}
Block: {block}
""")
    if not events:
        print("✅ No governance events found.")
        return
    for event in events:
        print(generate_alert(event, sentiment_score, sentiment_label))

if __name__ == "__main__":
    run_monitor()
