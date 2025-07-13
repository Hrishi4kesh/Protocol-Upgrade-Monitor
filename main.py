#main.py

from src.monitor import monitor_blockchain
from src.sentiment import analyze_sentiment
from src.alert import generate_alert  # ✅ NEW: Import alert generator
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

contract_address, from_block, to_block, risk = get_user_config()
events = monitor_blockchain(contract_address, from_block, to_block)


def run_monitor():
    print("📡 Monitoring blockchain for governance votes...\n")
    
    events = monitor_blockchain()  # ✅ Expect this to return the decoded events list
    
    sentiment_score, sentiment_label = analyze_sentiment()
    print(f"\n🧠 Sentiment Analysis Score: {sentiment_score:.3f} ({sentiment_label})\n")
    for event in events:
        # ✅ Extract key details
        votes = int(event['args']['votes'])
        proposal_id = event['args']['proposalId']
        voter = event['args']['voter']
        tx_hash = event['transactionHash'].hex()
        block = event['blockNumber']

        # ✅ Compute risk score
        risk_score, risk_level = compute_risk_score(votes, sentiment_score)

        # ✅ Print governance vote + risk report
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
        generate_alert(event, sentiment_score, sentiment_label)


if __name__ == "__main__":
    run_monitor()
