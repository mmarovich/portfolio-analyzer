
import quantstats as qs
import seaborn as sns
import pandas as pd

def sharpe_ratio(portfolio, tickers):
  sharpe_ratio_list = []
  ticker_list = []
  
  for ticker in tickers:
    ticker_list.append(ticker)
    ticker_daily_returns = portfolio.loc[:, (ticker, "daily_returns")]
    sharpe_ratio_list.append(qs.stats.sharpe(ticker_daily_returns))
  
  # Needed to call .T method to transpose data properly
  sharpe_ratio_df = pd.DataFrame([ticker_list, sharpe_ratio_list]).T
  cols = ["Stocks", "Sharpe Ratio"]
  sharpe_ratio_df.columns = cols
  sharpe_ratio_df.sort_values(by="Sharpe Ratio", inplace=True)
  sharpe_ratio_barchart = sns.barplot(data = sharpe_ratio_df, x="Stocks", y="Sharpe Ratio", color="palevioletred")
  display(sharpe_ratio_barchart)

  return sharpe_ratio_df


