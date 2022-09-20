def beta(portfolio, tickers, sp500_df):
    for ticker in tickers:
        covariance_asset_market = portfolio.loc[:, (ticker, "daily_returns")].cov(sp500_df.loc[:, "daily_returns"])
        variance_market = sp500_df.loc[:, "daily_returns"].var()
        beta = covariance_asset_market/variance_market
        print(f"The BETA of {ticker} versus the market (S&P500) is: {beta}")