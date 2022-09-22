# Portfolio Analyzer

This portfolio analyzer uses the Alpaca API, python, and various packages to create analysis for 10 selected stocks, including annualized returns, beta, sharpe ratios, and Monte Carlo simulations.

---

## Technologies

* Python and Jupyter Lab
* [Alpaca API](https://alpaca.markets/)
* [Seaborn](https://seaborn.pydata.org/)
* [QuantStats](https://openbase.com/python/QuantStats/documentation)


---

## Installation Guide

In your terminal:
```console
git clone git@github.com:mmarovich/portfolio-analyzer.git
pip install pandas pathlib hvplot quantstats seaborn numpy random alpaca_trade_api os dotenv datetime csv
conda activate dev
Jupyter lab
```

You will need to create your .env file and enter in your Alpaca API key and secret:

```
ALPACA_API_KEY = <Your alpaca api key>
ALPACA_SECRET_KEY = <Your alpaca secret>
```

---

## Quantitative Analysis

### Calculate Daily Returns and Cumulative Returns
We calculated the daily returns and cumulative returns. Daily returns give insight into the day-to-day percentage change of stock price. Additionally, daily returns allow us to compare the performance of different stocks. Cumulative returns give us the gain or loss of an investment over a period of time.
### Returns analysis
We plot the daily returns and cumulative returns to see the price movement for each stock. We also look at the annualized returns for each stock to determine which stock has the highest annualized returns.
### Volatility analysis
We then look at the volatility or risk for each stock. The metric that we use to measure the volatility or risk is annualized standard deviation. We plot each stock’s volatility in ascending order, from lower to highest volatility.
### Sharpe ratio
We use a new library called Quantstats library to calculate the Sharpe Ratio for each stock. The sharpe ratio gives the expected return per unit of risk.
### Variance
The Quantitative section evaluated the two portfolios assets for the risk involved with each asset individually and as a group. After determining predicted returns, the analysis turns to measuring the risk of each asset by measuring their daily return variance. Our goal using the Pandas variance to identify the assets likelihood of achieving the profitability desired.  The variance provides an idea of the volatility and relative performance of the asset within the portfolio. Here, we acquired the daily returns and cumulative returns and appended the returns as additional columns to our initial dataframe. Then, we obtained the variance using the Pandas var() and ranked the assets from least volatile to most volatile within their respective portfolios.
### Covariance
Next in our evaluation, we sought to obtain the covariance.  The covariance gives us the movement relationship of the assets within the respective portfolio. We used the covariance to determine the whether these assets move in same direction or in opposite directions of one another. In doing so, we obtained the covariance, again, using Pandas covariance function to evaluate the daily returns of each asset against the S&P 500 historical daily returns.  Again we ranked the assets from moving correlated to least correlated within their respective portfolios. This helps anyone viewing the portfolio to understand the strength of the relationship between assets within these portfolios.
### Beta
Lastly, we obtained the beta for each asset. This provided us with the sensitivity of each assets movement in relationship to the overall market. To obtain the beta we used the covariance that we acquired in the previous calculation and divided by the daily returns for the S&P 500.  By obtaining the beta we have a better way of evaluating the risk and return among assets within each portfolio for best in the group. We also obtain the risk of the assets return relative to sentiment of the overall market. Again, we ranked our assets within their respective portfolios.

## Monte Carlo Simulation

We create a Monte Carlo Simulation to calculate and plot possible projected values for each portfolio.  

## Mean-Variance Optimization

### Mean-Variance Frontier
We finally plot the Mean-Variance Frontier for two randomly selected stocks. The mean-variance frontier plots the portoflio returns and portoflio risk, where different weights are asssigned to each security. This way we can construct multiple portfolios, each allocating different proportions to the securities. The weight combinations that we allocate to the two assets are - (100%, 0%), (90%, 10%), (80%, 20%), (70%, 30%), (60%, 40%), (50%, 50%), (40%, 60%),  (30%, 70%), (20%, 80%), (10%, 90%), and (0%, 100%). For each combination, we calculate and plot the portfolio return and portfolio risk. The resulting plot can be used to determine the optimal portfolio that a Risk-Averse investor would invest in, i.e., the one that gives the maximum return for the lowest possible risk. 

---

## Contributors

Aanchal Khanna
Maxwell Marovich
Nick Schulz
Zachary Butler

---

## License

MIT
