import numpy as np
import pandas as pd
import seaborn as sns
number_trading_days = 252

def volatility_analysis(portfolio, tickers):
  each_ticker_volatility = []
  each_ticker = []
  for ticker in tickers:
    each_ticker.append(ticker)
    daily_returns = portfolio.loc[:, (ticker, "daily_returns")]
    each_ticker_volatility.append(daily_returns.std() * np.sqrt(number_trading_days))
  
  volatility_df = pd.DataFrame([each_ticker, each_ticker_volatility]).T
  cols = ["Stocks", "Volatility"]
  volatility_df.columns=cols
  volatility_df.sort_values(by="Volatility", inplace=True)
  sns.barplot(data=volatility_df, x="Stocks", y="Volatility", palette="flare")
  return(volatility_df)
