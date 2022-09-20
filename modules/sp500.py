import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import pandas as pd

# Load .env environment variables
load_dotenv()

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Verify that Alpaca key and secret were correctly loaded
print(f"Alpaca Key type: {type(alpaca_api_key)}")
print(f"Alpaca Secret Key type: {type(alpaca_secret_key)}")

# Create the Alpaca API object
alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")


def retrieve_sp500_data(ticker):
    start = pd.Timestamp("2016-09-01", tz="America/New_York").isoformat()
    end = pd.Timestamp("2022-08-31", tz="America/New_York").isoformat()
    
    timeframe = "1Day"

    # Get current closing prices for FB and TWTR
    sp500_df = alpaca.get_bars(
        ticker,
        timeframe,
        start = start,
        end = end).df

      
    # Setting index to date for better index/date formatting
    sp500_df.index = sp500_df.index.date

    # Calculate "daily_returns" for S&P 500
    sp500_df["daily_returns"] = sp500_df["close"].pct_change()

    
    # Return the S&P 500 dataframe

    return sp500_df

    



