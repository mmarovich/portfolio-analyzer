#Import libraries and dependencies
from pathlib import Path
from modules.alpaca_calls import *
from modules.MCForecastTools import MCSimulation

#import random function from rancom_csv_stock module
from modules.random_csv_stock import stock_tickers_random

#retrieve random function
random_cvs_stock = stock_tickers_random()
print(random_cvs_stock)

#Print ranndom function data
rand_stock_data = retrieve_alpaca_dataframes(random_cvs_stock)
print(rand_stock_data)

#Display MCSolutions.py
?MCSimulation

#10 year Monte Carlo simulation to forecast 10 years cumulative returns
MC_tenyear_rand = MCSimulation(
    portfolio_data = rand_stock_data,
    weights = [.20,.20,.20,.20,.20],
    num_simulation = 500,
    num_trading_days = 252*10
)

# Printing the simulation input data
MC_tenyear_rand.portfolio_data.head()

# Run a Monte Carlo simulation to forecast 12 years cumulative returns
MC_tenyear_rand.calc_cumulative_return()

#creat MC simulation line plot for random data 10 year
MC_sim_line_plot = MC_tenyear_rand.plot_simulation()



# Plot probability distribution and confidence intervals
MC_sim_dist_plot = MC_tenyear_rand.plot_distribution()


# Generate summary statiscs from the Monte Carlo simulation
# Set the sumamry statistics equal to a variable for future use
MC_summary_statistics_rand = MC_tenyear_rand.summarize_cumulative_return().astype("float")

#print summary statistics Series
print(MC_summary_statistics_rand)

# using the lower and uper '95%' confidence intervals from the summary statistics,
# calculate the range of the probable cumulative return for a $12,000 investment
ci_95_lower_cumulative_return = MC_summary_statistics_rand[8] * 12000
ci_95_upper_cumulative_return = MC_summary_statistics_rand[9] * 12000

# Print results
print(f"there is a 95% chance that an initial investment of $12,000 in the random portfolio"
      f" over the next 10 years will end with in the range of"
      f" ${ci_95_lower_cumulative_return: .2f} and {ci_95_upper_cumulative_return: .2f}.")
