
#src/alert.py

def generate_alert(event, sentiment_score, sentiment_label):
    args = event.get('args', {})
    if 'proposalId' not in args:
        return None
    return f"""
🚨 **Governance Alert**  
Proposal ID: `{args['proposalId']}`  
Votes: `{args.get('votes')}`  
Sentiment: `{sentiment_label}` ({sentiment_score:.2f})  
Support: `{args.get('support')}`  
"""
# This function generates an alert message based on the governance event details.