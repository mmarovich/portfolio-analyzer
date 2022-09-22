import seaborn as sns
import pandas as pd

def beta(portfolio, tickers, sp500_df):
    beta_list = []
    ticker_list = []
    
    for ticker in tickers:
        covariance_asset_market = portfolio.loc[:, (ticker, "daily_returns")].cov(sp500_df.loc[:, "daily_returns"])
        variance_market = sp500_df.loc[:, "daily_returns"].var()
        beta = covariance_asset_market/variance_market
        beta_list.append(beta)
        ticker_list.append(ticker)
    
    beta_df = pd.DataFrame([ticker_list, beta_list]).T
    # Needed to call .T method to transpose data properly
    
    cols = ["Stocks", "Beta"]
    beta_df.columns = cols
    beta_df.sort_values(by="Beta", inplace=True)
    beta_barchart = sns.barplot(data = beta_df, x="Stocks", y="Beta", palette="mako")
    display(beta_barchart)
    return beta_df
    
    