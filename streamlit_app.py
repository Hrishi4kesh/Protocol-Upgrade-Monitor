# streamlit_app.py

import os
import streamlit as st

from src.monitor import monitor_blockchain
# from src.sentiment import analyze_sentiment
from src.alert import generate_alert
from src.risk import compute_risk_score
from src.risk_outputs import (
    simulate_volatility,
    simulate_liquidity,
    simulate_execution_timing,
    simulate_rebalancing,
    simulate_mitigation
)
from src.user_input import get_user_inputs
from src.logger import logger
from ui.dashboard import (
    display_monitoring_settings,
    display_governance_timeline,
    display_execution_guidance
)

from src.sentiment import fetch_news_sentiment


# ---------------------------------------------
# Streamlit Page Setup
# ---------------------------------------------
st.set_page_config(layout="wide")
st.sidebar.title("🧭 Protocol Monitor Settings")

# ---------------------------------------------
# Sidebar Inputs
# ---------------------------------------------
network = st.sidebar.selectbox("Select Network", ["Ethereum"])
contract_address = st.sidebar.text_input("Protocol Contract Address", "0xc0Da02939E1441F497fd74F78cE7Decb17B66529")
from_block = st.sidebar.number_input("From Block", value=18000000)
to_block = st.sidebar.number_input("To Block", value=18010000)
risk_tolerance = st.sidebar.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
upgrade_type = st.sidebar.selectbox("Upgrade Type", ["Governance Proposal", "Parameter Change", "Implementation Upgrade"])
time_horizon = st.sidebar.selectbox("Time Horizon", ["Short-Term", "Long-Term"])
asset_pairs = st.sidebar.text_input("Asset Pairs Affected", "COMP/ETH, DAI/USDC")
run_monitor = st.sidebar.button("🔍 Run Monitor")

# ---------------------------------------------
# Main Execution Logic
# ---------------------------------------------
if run_monitor:
    try:
        # Collect user inputs into structured dict
        inputs = get_user_inputs(
            network,
            contract_address,
            from_block,
            to_block,
            risk_tolerance,
            upgrade_type,
            time_horizon,
            asset_pairs
        )

        col1, col2, col3 = st.columns([1, 2, 1])
        display_monitoring_settings(col1, inputs)

        with st.spinner("🔗 Monitoring Blockchain & Analyzing..."):
            # Monitor blockchain for governance events
            events = monitor_blockchain(
                contract_address=inputs["contract_address"],
                from_block=inputs["from_block"],
                to_block=inputs["to_block"],
                network=inputs["network"]
            )
            print("DEBUG EVENTS:", events)

            # Analyze sentiment (currently mocked)
            # sentiment_score, sentiment_label = analyze_sentiment()
            # st.success(f"🧠 Sentiment Score: {sentiment_score:.3f} ({sentiment_label})")
            
            sentiment_score, sentiment_label = fetch_news_sentiment()
            st.metric("Governance Sentiment", f"{sentiment_score:.2f}")

            # Simulate risk factors
            try:
                volatility = simulate_volatility()
                liquidity = simulate_liquidity()
                execution_timing = simulate_execution_timing(volatility, liquidity)
                rebalancing = simulate_rebalancing()
                mitigation = simulate_mitigation()
            except Exception as e:
                logger.warning("Simulation failed. Reason: %s", str(e))
                volatility = liquidity = execution_timing = rebalancing = mitigation = "Unavailable"
                st.warning("⚠️ Risk simulations could not be completed.")

        # Render dashboard sections
        display_governance_timeline(col2, events, sentiment_score, sentiment_label)
        display_execution_guidance(col3, volatility, liquidity, execution_timing, rebalancing, mitigation)

    except Exception as e:
        logger.exception("Error during monitoring run")
        st.error(f"🚨 An error occurred while monitoring: {e}")

