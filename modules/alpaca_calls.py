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


def retrieve_alpaca_dataframes(tickers):
    start = pd.Timestamp("2016-09-01", tz="America/New_York").isoformat()
    end = pd.Timestamp("2022-08-31", tz="America/New_York").isoformat()

    timeframe = "1Day"

    # Get current closing prices for FB and TWTR
    df_portfolio = alpaca.get_bars(
        tickers,
        timeframe,
        start = start,
        end = end
    ).df

    # Reorganize the DataFrame
    # Separate ticker data
    ticker1 = df_portfolio[df_portfolio['symbol']==tickers[0]].drop('symbol', axis=1)
    ticker2 = df_portfolio[df_portfolio['symbol']==tickers[1]].drop('symbol', axis=1)
    ticker3 = df_portfolio[df_portfolio['symbol']==tickers[2]].drop('symbol', axis=1)
    ticker4 = df_portfolio[df_portfolio['symbol']==tickers[3]].drop('symbol', axis=1)
    ticker5 = df_portfolio[df_portfolio['symbol']==tickers[4]].drop('symbol', axis=1)

    # Created new index to mitigate error: https://stackoverflow.com/questions/35084071/concat-dataframe-reindexing-only-valid-with-uniquely-valued-index-objects
    df_portfolio = df_portfolio.reset_index()

    # Concatenate the ticker DataFrames
    df_portfolio = pd.concat(
        [ticker1, ticker2, ticker3, ticker4, ticker5],
        axis=1, 
        keys=tickers)
    
    # Setting index to date for better index/date formatting
    df_portfolio.index = df_portfolio.index.date


    # Display sample data
    return df_portfolio

