# streamlit_app.py

import os
import streamlit as st

from src.monitor import monitor_blockchain
# from src.sentiment import analyze_sentiment
from src.alert import generate_alert
from src.risk import compute_risk_score
from src.risk_outputs import (
    execution_timing,
    rebalancing,
    mitigation
)

from src.user_input import get_user_inputs
from src.logger import logger
from ui.dashboard import (
    display_monitoring_settings,
    display_governance_timeline,
    display_execution_guidance
)
from src.volatility import forecast_volatility
from src.defi_llama import predict_liquidity_shift

from src.sentiment import fetch_news_sentiment

import matplotlib.pyplot as plt
import yfinance as yf


# ---------------------------------------------
# Streamlit Page Setup
# ---------------------------------------------
st.set_page_config(layout="wide")
st.sidebar.title("🧭 Protocol Monitor Settings")

# ---------------------------------------------
# Sidebar Inputs
# ---------------------------------------------
network = st.sidebar.selectbox("Select Network", ["Ethereum", "Polygon", "Arbitrum"])
contract_address = st.sidebar.text_input("Protocol Contract Address", "0xc0Da02939E1441F497fd74F78cE7Decb17B66529")
from_block = st.sidebar.number_input("From Block", value=18000000)
to_block = st.sidebar.number_input("To Block", value=18010000)
risk_tolerance = st.sidebar.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
upgrade_type = st.sidebar.selectbox("Upgrade Type", ["Governance Proposal", "Parameter Change", "Implementation Upgrade"])
time_horizon = st.sidebar.selectbox("Time Horizon", ["Short-Term", "Long-Term"])
asset_pairs = st.sidebar.text_input("Asset Pairs Affected", "COMP/ETH, DAI/USDC")
run_monitor = st.sidebar.button("🔍 Run Monitor")
risk_threshold = st.sidebar.slider("Volatility Tolerance", min_value=0, max_value=100, value=70)
liquidity_requirement = st.sidebar.slider("Liquidity Requirement", min_value=0, max_value=100, value=50)
token_symbol = st.sidebar.text_input("Token Symbol for Volatility", "COMP-USD", help="e.g. ETH-USD, BTC-USD")
protocol_slug = st.sidebar.text_input("Protocol Slug for Liquidity", "compound", help="e.g. aave, uniswap")
st.sidebar.markdown("""
---
📌 **Data Sources Used**
- Ethereum / Infura
- Compound Governance (ABI)
- NewsAPI + VADER
- DeFi Llama
- YFinance (GARCH)
""")


# ---------------------------------------------
# Main Execution Logic
# ---------------------------------------------
if run_monitor:
    try:
        inputs = get_user_inputs(
            network,
            contract_address,
            from_block,
            to_block,
            risk_tolerance,
            upgrade_type,
            time_horizon,
            asset_pairs,
            risk_threshold,
            liquidity_requirement
        )

        col1, col2, col3 = st.columns([1, 2, 1])
        display_monitoring_settings(col1, inputs)

        with st.spinner("🔗 Monitoring Blockchain & Analyzing..."):
            events = monitor_blockchain(
                contract_address=inputs["contract_address"],
                from_block=inputs["from_block"],
                to_block=inputs["to_block"],
                network=inputs["network"]
            )

            # Sentiment analysis (real)
            sentiment_score, sentiment_label = fetch_news_sentiment(
                query=f"{inputs['upgrade_type']} {inputs['contract_address']}"
            )

            # Risk score
            votes = events[0]['args']['votes'] if events else 0
            risk_score, risk_level = compute_risk_score(votes, sentiment_score, inputs["risk_threshold"])

            # Volatility (real)
            volatility = forecast_volatility(pair=token_symbol)
            if volatility == "Unavailable":
                volatility = "Data unavailable (check token symbol or API limits)"
                logger.warning("Volatility data unavailable for COMP-USD.")

            # Liquidity (real)
            liquidity = predict_liquidity_shift(protocol_slug=protocol_slug)
            if liquidity == "Unavailable":
                liquidity = "Data unavailable (check protocol slug or API limits)"
                logger.warning("Liquidity data unavailable for 'compound'.")

            # Execution timing, rebalancing, mitigation (data-driven)
            execution_timing_val = execution_timing(events, volatility)
            rebalancing_val = rebalancing(liquidity, inputs["asset_pairs"])
            mitigation_val = mitigation(volatility, sentiment_label)

            if not events:
                col2.warning("No governance events found in the selected block range.")
            else:
                display_governance_timeline(col2, events, sentiment_score, sentiment_label, inputs)

            display_execution_guidance(
                col3,
                volatility,
                liquidity,
                execution_timing_val,
                rebalancing_val,
                mitigation_val
            )

            st.success(f"Risk Score: {risk_score} ({risk_level})")

            if volatility.startswith("Data unavailable"):
                col3.warning(volatility)
            if liquidity.startswith("Data unavailable"):
                col3.warning(liquidity)

    except Exception as e:
        st.error(f"Error: {e}")

