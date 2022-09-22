import pandas as pd
import seaborn as sns
number_trading_days = 252



def returns_analysis(portfolio, tickers):
  for ticker in tickers:
    daily_returns = pd.DataFrame(portfolio.loc[:, (ticker, "daily_returns")])
    daily_returns_lineplot = daily_returns[ticker].hvplot.line(color="midnightblue", title=ticker+" "+"Daily Returns", ylabel="Daily Returns", xlabel="Time")
    cumulative_returns = pd.DataFrame(portfolio.loc[:, (ticker, "cumulative_returns")])
    cumulative_returns_lineplot = cumulative_returns[ticker].hvplot.line(color="maroon", title=ticker+" "+"Cumulative Returns", ylabel="Cumulative Returns", xlabel="Time")
    display(daily_returns_lineplot)
    display(cumulative_returns_lineplot)




def annualized_returns_analysis(portfolio, tickers):
  each_ticker = []
  ticker_annualized_returns = []
  
  for ticker in tickers:
    each_ticker.append(ticker)
    daily_returns = portfolio.loc[:, (ticker, "daily_returns")]
    average_daily_returns = daily_returns.mean()
    annualized_daily_returns = average_daily_returns * number_trading_days
    ticker_annualized_returns.append(annualized_daily_returns)
  
  annualized_returns_df = pd.DataFrame([each_ticker, ticker_annualized_returns]).T
  # Needed to call .T method to transpose data properly
  
  cols = ["Stocks", "Annualized Returns"]
  annualized_returns_df.columns = cols
  annualized_returns_df.sort_values(by="Annualized Returns", inplace=True)
  annualized_returns_barplot = sns.barplot(data=annualized_returns_df, x="Stocks", y="Annualized Returns", palette="dark:#5A9")
  display(annualized_returns_df)
    
  