def covariance(portfolio, tickers, sp500_df):
    
    for ticker in tickers:
        covariance = portfolio.loc[:, (ticker, "close")].cov(sp500_df.loc[:, "close"])
        print(f"The covariance of {ticker} versus the market (S&P500) is: {covariance}")
