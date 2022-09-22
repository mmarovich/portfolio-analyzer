
# Function to calculate and plot the Mean Variance Frontier

import random
import numpy as np
import pandas as pd
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')



def mean_variance_frontier(portfolio, tickers):
  random_tickers = random.sample(tickers, k=2)  
  print(f"The two randomly selected tickers are: {random_tickers}")
  random_ticker_list = []
  portfolio_returns_list = []
  portfolio_risk_list = []
  annualized_returns_list = []
  annualized_std_list = []
  weights = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
  number_trading_days = 252
  returns_df = pd.DataFrame()

  
  for random_ticker in random_tickers:
      random_ticker_list.append(random_ticker)
      random_df = pd.DataFrame(portfolio.loc[:, (random_ticker, "daily_returns")])
      
      annualized_returns = (portfolio.loc[:, (random_ticker, "daily_returns")].mean()) * number_trading_days
      annualized_returns_list.append(annualized_returns)
      
      annualized_std = (portfolio.loc[:, (random_ticker, "daily_returns")].std()) * np.sqrt(number_trading_days)
      annualized_std_list.append(annualized_std)
            
      returns_df = pd.concat([returns_df, random_df], axis=1)
      

  correlation_matrix = returns_df.corr()
  display(correlation_matrix)

  first_ticker_returns = returns_df.loc[:, (random_ticker_list[0], "daily_returns")]
  second_ticker_returns = returns_df.loc[:, (random_ticker_list[1], "daily_returns")]

  correlation = round(first_ticker_returns.corr(second_ticker_returns), 4)
  
  print("                                                                                                   ")
  
  print(f"The correlation coefficient of {random_ticker_list[0]} & {random_ticker_list[1]} is: {correlation}")
  
  for weight in weights:
    
    portfolio_returns = ((weight * annualized_returns_list[0])**2) + (((1-weight) * annualized_returns_list[1])**2)
    portfolio_returns_list.append(portfolio_returns)
    # Used formula to calculate portfolio return
    
    portfolio_risk = np.sqrt(((weight * annualized_std_list[0])**2) + (((1-weight) * annualized_std_list[1])**2) + (2 * weight * annualized_std_list[0] * (1-weight) * annualized_std_list[1] * correlation))
    portfolio_risk_list.append(portfolio_risk)
    # Used formula to calculate portfolio risk
  

  
  mvf_df = pd.DataFrame([portfolio_returns_list, portfolio_risk_list], index=["Portfolio Returns", "Portfolio Risk"])
  
  cols_list = []
  for each_execution in range(1, 12):
    cols_list.append("Execution "+str(each_execution))
  
  mvf_df.columns = cols_list
  mvf_df = mvf_df.T
  # Needed to call .T method to transpose data properly

  
  mvf_df.plot(kind="scatter", x="Portfolio Risk", y="Portfolio Returns")

  return mvf_df