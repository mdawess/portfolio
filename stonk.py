import yfinance as yf
from forex_python.converter import CurrencyRates

class Portfolio:
    
    def __init__(self):
        
        self.stocks = {}

    def add_ticker(self, ticker, shares=1) -> None:
        """Adds a ticker or tickers to the list of stocks. Can either be a single ticker
        or a list of tickers.
        """ 
        # Add ability to add X number of tickers at a time as well
        # Add error checking to see if the ticker symbol is valid
        if type(ticker) == str:
            if ticker not in self.stocks:
                self.stocks[ticker] = []
                self.stocks[ticker].append(shares)
            else:
                self.stocks[ticker][0] = self.stocks[ticker][0] + shares

    def remove_ticker(self, ticker, shares=1) -> None:
        """Removes a ticker or tickers from the list from the list. Can be either a
        single ticker or a list.
        """
        # Add ability to add X number of tickers at a time as well
        if type(ticker) == str:
            if ticker in self.stocks:
                if self.stocks[ticker][0] > shares:
                    self.stocks[ticker][0] = self.stocks[ticker][0] - shares
                else:
                    self.stocks.pop(ticker)
            else:
                print("Unable to remove, " + ticker + " not found.")

    def convert_cad(self, ttp) -> dict:
        """Returns a new dictionary with all prices in CAD."""
        c = CurrencyRates()
        CAD = c.get_rates("USD")["CAD"]

        for stock in ttp:
            if stock[-2:] != "TO":
                ttp[stock][1] = (ttp[stock][1] * CAD).round(2)

        return ttp
        
    def current_prices(self) -> None:
        """Returns the current prices attached to the individual ticker in a dictionary."""
        """
        ticker_to_price = {}

        for stock in self.stocks:
            initialize = yf.Ticker(stock)
            price = initialize.history(period="max")["Close"][-1]
            ticker_to_price[stock] = price

        ticker_to_price = self.convert_cad(ticker_to_price)

        return ticker_to_price
        """
        for stock in self.stocks:
            initialize = yf.Ticker(stock)
            price = initialize.history(period="max")["Close"][-1]
            if len(self.stocks[stock]) == 1:
                self.stocks[stock].append(price)
            elif len(self.stocks[stock]) == 0:
                None
            else:
                self.stocks[stock][1] == price

        self.stocks = self.convert_cad(self.stocks)

    def check_portfolio(self) -> list:
        """Returns the current holdings and their most recent price."""
        
        self.current_prices()
        print(self.stocks)

    def portfolio_value(self) -> float:
        """Returns the total value of all current holdings"""
        
    


