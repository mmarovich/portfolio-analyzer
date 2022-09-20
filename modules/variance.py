def variance(portfolio, tickers):
  for ticker in tickers:
    daily_returns = portfolio.loc[:, (ticker,'daily_returns')]
    each_variance = daily_returns.var()
    print(f"The variance for {ticker} is:", each_variance)
    
