from pathlib import Path
from modules.alpaca_calls import *
from modules.MCForecastTools import MCSimulation

#def maang stock tickers:
def stock_tickers_maang():
    maang_tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]    
    return maang_tickers

maang_stocks = stock_tickers_maang()

#print maang stock data
maang_stock_data = retrieve_alpaca_dataframes(maang_stocks)
print(maang_stock_data)

#display MCSimulation.py
?MCSimulation

#10 year Monte Carlo simulation to forecast 10 years cumulative returns
MC_tenyear_maang = MCSimulation(
    portfolio_data = maang_stock_data,
    weights = [.20,.20,.20,.20,.20],
    num_simulation = 500,
    num_trading_days = 252*10
)

# Printing the simulation input data
MC_tenyear_maang.portfolio_data.head()

# Run a Monte Carlo simulation to forecast 12 years cumulative returns
MC_tenyear_maang.calc_cumulative_return()

#Creat Line plot for tenyear simulation
MC_sim_line_plot = MC_tenyear_maang.plot_simulation()

# Save the plot for future use
MC_sim_line_plot.get_figure().savefig("MC_tenyear_maang_sim_plot.png", bbox_inches="tight")



# Plot probability distribution and confidence intervals
MC_sim_dist_plot = MC_tenyear_maang.plot_distribution()




# Generate summary statiscs from the Monte Carlo simulation
# Set the sumamry statistics equal to a variable for future use
MC_summary_statistics = MC_tenyear_maang.summarize_cumulative_return()

#print summary statistics Series
print(MC_summary_statistics)

# using the lower and uper '95%' confidence intervals from the summary statistics,
# calculate the range of the probable cumulative return for a $12,000 investment
ci_95_lower_cumulative_return = MC_summary_statistics[8] * 12000
ci_95_upper_cumulative_return = MC_summary_statistics[9] * 12000

# Print results
print(f"there is a 95% chance that an initial investment of $12,000 in the maang portfolio"
      f" over the next 10 years will end with in the range of"
      f" ${ci_95_lower_cumulative_return: .2f} and {ci_95_upper_cumulative_return: .2f}.")