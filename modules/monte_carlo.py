from MCForecastTools import MCSimulation

?MCSimultion

def simulate_monte(dataframe, tickers):

    #10 year Monte Carlo simulation to forecast 10 years cumulative returns
    MC_tenyear_rand = MCSimulation(
        portfolio_data = dataframe,
        weights = [.20,.20,.20,.20,.20],
        num_simulation = 500,
        num_trading_days = 252*10
    )

    #creat MC simulation line plot for random data 10 year
    MC_sim_line_plot = MC_tenyear_rand.plot_simulation()

    return MC_sim_line_plot