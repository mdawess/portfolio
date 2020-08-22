import yfinance as yf
import forex-python

class stk:

    def __init__(self, stocks):
        
        self.stocks = stocks

    def convert_cad(self) -> dict:
        """Returns a new dictionary with all prices in CAD."""



    def current_prices(self) -> dict:
        """Returns the current prices attached to the individual ticker in a dictionary."""

        ticker_to_price = {}

        for stock in self.stocks:
            initialize = yf.Ticker(stock)
            price = initialize.history(period="max")["Close"][-1]
            ticker_to_price[stock] = price

        return ticker_to_price

test = stk(["MSFT", "AAPL", "CGC"])

print(test.current_prices())
