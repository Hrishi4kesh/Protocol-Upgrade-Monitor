# src/volatility.py

import yfinance as yf
import numpy as np
from arch import arch_model
from src.logger import logger

def get_price_series(pair="COMP-USD", period="30d", interval="1h"):
    """Fetch historical price data using yfinance."""
    try:
        df = yf.download(pair, period=period, interval=interval, progress=False)
        if df.empty:
            raise ValueError("Price data not available.")
        return df["Close"].dropna()
    except Exception as e:
        logger.error(f"Failed to fetch price data for {pair}: {e}")
        return None

def forecast_volatility(pair="COMP-USD"):
    """Forecast volatility using GARCH(1,1)"""
    prices = get_price_series(pair)
    if prices is None or len(prices) < 20:
        return "Unavailable"

    returns = 100 * prices.pct_change().dropna()  # Convert to percentage returns

    # GARCH(1,1)
    model = arch_model(returns, vol='Garch', p=1, q=1)
    res = model.fit(disp="off")
    
    forecast = res.forecast(horizon=1)
    next_vol = forecast.variance.values[-1][0]
    volatility = np.sqrt(next_vol)

    # Qualitative label
    if volatility < 1:
        return "Low"
    elif volatility < 3:
        return "Moderate"
    else:
        return "High"
