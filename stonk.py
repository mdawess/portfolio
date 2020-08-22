import yfinance as yf
from forex_python.converter import CurrencyRates

class Portfolio:

    def __init__(self, stocks):
        
        self.stocks = stocks

    def convert_cad(self, ttp) -> dict:
        """Returns a new dictionary with all prices in CAD."""
        c = CurrencyRates()
        CAD = c.get_rates("USD")["CAD"]

        for stock in ttp:
            if stock[-2:] != "TO":
                ttp[stock] = ttp[stock] * CAD

        return ttp
        
    def current_prices(self) -> dict:
        """Returns the current prices attached to the individual ticker in a dictionary."""

        ticker_to_price = {}

        for stock in self.stocks:
            initialize = yf.Ticker(stock)
            price = initialize.history(period="max")["Close"][-1]
            ticker_to_price[stock] = price

        ticker_to_price = self.convert_cad(ticker_to_price)

        return ticker_to_price

    def portfolio_value(self) -> float:
        """Returns the total value of all current holdings"""

    


