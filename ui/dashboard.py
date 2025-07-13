# ui/dashboard.py

import streamlit as st
from src.risk import compute_risk_score

def display_monitoring_settings(col, inputs):
    with col:
        st.subheader("🔗 Network Monitoring")
        st.write(f"Network: {inputs['network']}")
        st.write(f"Contract: `{inputs['contract_address']}`")
        st.write(f"Block Range: {inputs['from_block']} - {inputs['to_block']}")
        st.write(f"Risk Tolerance: {inputs['risk_tolerance']}")
        st.write(f"Upgrade Type: {inputs['upgrade_type']}")
        st.write(f"Time Horizon: {inputs['time_horizon']}")
        st.write(f"Affected Pairs: {inputs['asset_pairs']}")


def display_governance_timeline(col, events, sentiment_score, sentiment_label):
    with col:
        st.subheader("📜 Governance Timeline")
        for event in events[:10]:
            votes = int(event['args']['votes'])
            proposal_id = event['args']['proposalId']
            voter = event['args']['voter']
            tx_hash = event['transactionHash'].hex()
            block = event['blockNumber']
            support = event['args']['support']

            risk_score, risk_level = compute_risk_score(votes, sentiment_score)
            risk_color = "🟢" if risk_level == "Low" else "🟠" if risk_level == "Medium" else "🔴"

            st.markdown(f"""
**🚨 Proposal ID:** `{proposal_id}`  
Voter: `{voter}`  
Support: `{support}`  
Votes: `{votes}`  
Sentiment: `{sentiment_label}` ({sentiment_score:.2f})  
📊 **Risk Score:** `{risk_score}` ({risk_color} {risk_level})  
Block: `{block}`  
TxHash: `{tx_hash}`  
---""")


def display_execution_guidance(col, volatility, liquidity, execution_timing, rebalancing, mitigation):
    with col:
        st.subheader("📈 Execution Guidance")
        st.write("💡 Based on sentiment and vote weight:")
        st.write("→ Avoid major trades until vote resolution")
        st.write("→ Consider hedging if volatility rises")
        st.write("→ Monitor proposal status daily")
        st.write(f"📉 **Volatility Impact**: {volatility}")
        st.write(f"💧 **Liquidity Shift Prediction**: {liquidity}")
        st.write(f"⏱️ **Execution Timing**: {execution_timing}")
        st.write(f"📊 **Rebalancing Advice**: {rebalancing}")
        st.write(f"🛡️ **Risk Mitigation**: {mitigation}")
