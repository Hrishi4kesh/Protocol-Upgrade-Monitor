
def generate_alert(event, sentiment_score, sentiment_label):
    args = event.get('args', {})
    if 'proposalId' not in args:
        print("[WARNING] Event missing proposalId, skipping:", event)
        return
    print(f"""
🚨 Governance Vote Alert 🚨
Proposal ID: {args['proposalId']}
Voter: {args.get('voter', 'N/A')}
Support: {args.get('support', 'N/A')}
Votes: {args.get('votes', 'N/A')}
Sentiment: {sentiment_label} ({sentiment_score:.3f})
Tx Hash: {event['transactionHash'].hex()}
Block: {event['blockNumber']}
    """)