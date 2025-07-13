# src/risk.py
def compute_risk_score(votes, sentiment_score, risk_threshold=70):
    # Normalize votes and sentiment
    normalized_votes = min(votes / 1_000_000, 1.0)
    normalized_sentiment = (sentiment_score + 1) / 2
    score = int(100 * (0.7 * normalized_votes + 0.3 * (1 - normalized_sentiment)))
    # Compare to threshold
    if score < risk_threshold * 0.5:
        level = "Low"
    elif score < risk_threshold:
        level = "Medium"
    else:
        level = "High"
    return score, level
