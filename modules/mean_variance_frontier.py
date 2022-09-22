
# Function to calculate and plot the Mean Variance Frontier

import random
import numpy as np
import pandas as pd
import seaborn as sns

def mean_variance_frontier(portfolio, tickers):
  random_tickers = random.sample(tickers, k=2)
  print(f"The two randomly selected tickers are: {random_tickers}")
  ef_portfolio_returns_list = []
  ef_portfolio_risk_list = []
  average_returns_list = []
  standard_deviation_returns_list = []
  weights = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
  number_trading_days = 252
  daily_returns_df = pd.DataFrame()

  
  for random_ticker in random_tickers:
      random_daily_returns_df = pd.DataFrame(portfolio.loc[:, (random_ticker, "daily_returns")])
      average_returns = portfolio.loc[:, (random_ticker, "daily_returns")].mean() * number_trading_days
      annualized_standard_deviation = (portfolio.loc[:, (random_ticker, "daily_returns")].std()) * np.sqrt(number_trading_days)
      average_returns_list.append(average_returns)
      standard_deviation_returns_list.append(annualized_standard_deviation)
      daily_returns_df = pd.concat([daily_returns_df, random_daily_returns_df], axis=1)
      

  correlation_matrix = daily_returns_df.corr()
  display(correlation_matrix)
  
  
  
  for weight in weights:
    
    portfolio_average = (weight*average_returns_list[0])**2 + ((1-weight)*average_returns_list[1])**2
    ef_portfolio_returns_list.append(portfolio_average)
    
    
    portfolio_risk = np.sqrt((weight*standard_deviation_returns_list[0])**2 + ((1-weight)*standard_deviation_returns_list[1])** + (2*weight*standard_deviation_returns_list[0]*(1-weight)*standard_deviation_returns_list[1]))
    ef_portfolio_risk_list.append(portfolio_risk)
  

  
  ef_portfolio_returns_df = pd.DataFrame([ef_portfolio_returns_list,ef_portfolio_risk_list], index=["Portfolio Returns", "Portfolio Risk"])
  
  cols_list = []
  for each_run in range(1, 12):
    cols_list.append("Execution "+str(each_run))
  
  ef_portfolio_returns_df.columns = cols_list
  ef_portfolio_returns_df = ef_portfolio_returns_df.T
  ef_portfolio_returns_df.plot.scatter(x="Portfolio Risk", y="Portfolio Returns")

  return ef_portfolio_returns_df
