# Protocol Upgrade Monitor

A high-performance blockchain protocol upgrade monitoring system that tracks governance activity, predicts volatility and liquidity shifts, and provides execution guidance to DeFi users.

---

## 🚀 Overview

This system monitors smart contract upgrades on major networks like Ethereum, Polygon, and Arbitrum. It connects to blockchain APIs, news sentiment feeds, and simulates market effects of governance proposals to generate actionable insights.

It includes:

- A user-friendly Streamlit dashboard  
- Real-time governance monitoring via Web3  
- Sentiment analysis using News API + VADER  
- Simulated risk metrics: volatility, liquidity, execution timing  
- Execution guidance with rebalancing & mitigation suggestions  

---

## 🧱 Features

| UI Panel       | Functionality |
|----------------|----------------|
| **Left Panel** | Input contract address, block range, risk preferences |
| **Center Panel** | View governance proposal events, voter data, sentiment & risk score |
| **Right Panel** | Get trading guidance: volatility, liquidity, timing, rebalancing advice |

---

## ⚙️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Protocol-Upgrade-Monitor.git
cd Protocol-Upgrade-Monitor
```
2. **Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your API keys**

Update config.py or set environment variables:

```bash
INFURA_PROJECT_ID = "your_infura_project_id"
NEWSAPI_KEY = "your_newsapi_key"
```

5. **Run the app**

```bash
streamlit run streamlit_app.py
```
## 🔍 Technologies Used
- Python 3.10+

- Streamlit – for UI dashboard

- Web3.py – Ethereum/POS blockchain interaction

- NewsAPI + NLTK (VADER) – Sentiment analysis

- Simulated GARCH & Liquidity Forecasting – Mocked backend logic

- YFinance / DeFi Analytics APIs (optional expansion)

## 🧠 Architecture
```bash
📁 Protocol-Upgrade-Monitor/
│
├── streamlit_app.py             # Main app entry
├── config.py                    # API keys and network config
├── requirements.txt             # Dependencies
│
├── src/
│   ├── monitor.py               # Blockchain event monitor
│   ├── sentiment.py             # News-based sentiment engine
│   ├── risk.py                  # Risk score computation
│   ├── risk_outputs.py          # Simulated liquidity/volatility/etc.
│   ├── alert.py                 # Alerts and notifications (optional)
│   ├── logger.py                # Logging setup
│   └── utils.py                 # Helper functions
│
├── ui/
│   └── dashboard.py             # Streamlit UI layout (3 panels)
│
├── data/
│   └── compound_abi.json        # Sample ABI used to decode contract logs
```
## 📈 Sample Output
- ✅ Governance Event: Proposal ID, Voter, Vote Weight, Sentiment

- 📊 Risk Score: Computed from sentiment + votes

- ⏱️ Execution Timing: Based on simulated volatility & liquidity

- 🛡️ Guidance: Rebalancing and mitigation suggestions

## 📌 Notes
- If NewsAPI returns no articles, the system falls back to default simulated news to ensure sentiment analysis continues.

- Governance event logs can also be simulated for testing.

👨‍💻 Author
Hrishikesh Bhatt