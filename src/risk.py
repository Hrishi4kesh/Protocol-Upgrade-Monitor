# src/risk.py
def compute_risk_score(votes, sentiment_score):
    vote_factor = min(votes / 1e24, 1)  # Normalize to 0–1
    sentiment_factor = abs(sentiment_score)  # 0 (neutral) to 1 (strong emotion)
    
    score = 100 * (0.6 * vote_factor + 0.4 * sentiment_factor)
    
    if score < 30:
        level = "Low"
    elif score < 70:
        level = "Medium"
    else:
        level = "High"

    return round(score, 2), level
