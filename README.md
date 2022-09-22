Portfolio Analyzer

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
### Variance
The Quantitative section evaluated the two portfolios assets for the risk involved with each asset individually and as a group. After determining predicted returns, the analysis turns to measuring the risk of each asset by measuring their daily return variance. Our goal using the Pandas variance to identify the assets likelihood of achieving the profitability desired.  The variance provides an idea of the volatility and relative performance of the asset within the portfolio. Here, we acquired the daily returns and cumulative returns and appended the returns as additional columns to our initial dataframe. Then, we obtained the variance using the Pandas var() and ranked the assets from least volatile to most volatile within their respective portfolios.
### Covariance
Next in our evaluation, we sought to obtain the covariance.  The covariance gives us the movement relationship of the assets within the respective portfolio. We used the covariance to determine the whether these assets move in same direction or in opposite directions of one another. In doing so, we obtained the covariance, again, using Pandas covariance function to evaluate the daily returns of each asset against the S&P 500 historical daily returns.  Again we ranked the assets from moving correlated to least correlated within their respective portfolios. This helps anyone viewing the portfolio to understand the strength of the relationship between assets within these portfolios.
### Beta
Lastly, we obtained the beta for each asset. This provided us with the sensitivity of each assets movement in relationship to the overall market. To obtain the beta we used the covariance that we acquired in the previous calculation and divided by the daily returns for the S&P 500.  By obtaining the beta we have a better way of evaluating the risk and return among assets within each portfolio for best in the group. We also obtain the risk of the assets return relative to sentiment of the overall market. Again, we ranked our assets within their respective portfolios.

---

## Contributors

Aanchal Khanna
Maxwell Marovich
Nick Schulz
Zachary Butler

---

## License

MIT
