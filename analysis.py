import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class Analyze:

    def __init__(self, current_portfolio, total_portfolio_value):
        """Initialize with a dictionary containing tickers, 
        number of shares and the current prices of each.
        """
        self.portfolio = current_portfolio
        self.total_value = total_portfolio_value
        self.portfolio_breakdown = {}
    
    def breakdown(self) -> dict:
        """Crate a dictionary with the ticker as key and the %
        contribution to the portfolio as the value.
        """
        # portfolioBreakdown = {}
        for ticker in self.portfolio:
            self.portfolio_breakdown[ticker] = ((self.portfolio[ticker][0] * self.portfolio[ticker][1]) / self.total_value).round(2)

        return self.portfolio_breakdown

    def historical_charts(self) -> pd.DataFrame:
        """Returns to historical values of the portfolio."""
        print("Unfortunately, this doesn't work yet :(")

    def display_charts(self):
        """ """
        # Creating the pie chart for the breakdown of holdings
        self.breakdown()
        stocks = []
        percentages = []
        for stock in self.portfolio_breakdown:
            stocks.append(stock)
            percentages.append(self.portfolio_breakdown[stock])

        figure = plt.figure(figsize=(10, 7))
        plt.pie(percentages, labels=stocks)

        plt.show()


