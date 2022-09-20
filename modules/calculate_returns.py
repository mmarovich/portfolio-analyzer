def returns_calc(portfolio, tickers):
    for ticker in tickers:
        portfolio.loc[:, (ticker, "daily_returns")] = portfolio.loc[:, (ticker,"close")].pct_change()
        portfolio.loc[:, (ticker, "cumulative_returns")] = (1+portfolio.loc[:, (ticker,"daily_returns")]).cumprod()
    
    return portfolio
