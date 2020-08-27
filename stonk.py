import yfinance as yf
from forex_python.converter import CurrencyRates

class Portfolio:
    
    def __init__(self):
        
        self.stocks = []

    def add_ticker(self, ticker) -> None:
        """Adds a ticker or tickers to the list of stocks. Can either be a single ticker
        or a list of tickers.
        """ 
        # Add ability to add X number of shares as well
        if type(ticker) == str:
            if ticker not in self.stocks:
                self.stocks.append(ticker)
            else:
                print(ticker + " has already been added to the portfolio")
        if type(ticker) == list:
            for t in ticker:
                if t not in self.stocks:
                    self.stocks.append(t)
                else:
                    print(t + " has already been added to the portfolio")

    def remove_ticker(self, ticker) -> None:
        """Removes a ticker or tickers from the list from the list. Can be either a
        single ticker or a list.
        """
        # Add ability to remove X number of shares as well
        if type(ticker) == str:
            if ticker in self.stocks:
                self.stocks.remove(ticker)
            else:
                print(ticker + " is not in the portfolio")
        if type(ticker) == list:
            for t in ticker:
                if t in self.stocks:
                    self.stocks.remove(t)
                else:
                    print(t + " is not in the portfolio")

    def check_portfolio(self) -> list:
        """Returns the current holdings and their most recent price."""
        
        print(self.stocks)

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

    


