import yfinance as yf
from forex_python.converter import CurrencyRates

class Portfolio:
    
    def __init__(self):
        
        self.stocks = {}

    def add_ticker(self, ticker, shares=1) -> None:
        """Adds a ticker or tickers to the list of stocks. Can either be a single ticker
        or a list of tickers.
        """ 
        OK = False
        try:
            i = yf.Ticker(ticker)
            x = i.history(period="max")["Close"][-1]
            OK = True
        except:
            OK = False

        if type(ticker) == str and OK == True:
            if ticker not in self.stocks:
                self.stocks[ticker] = []
                self.stocks[ticker].append(shares)
            elif ticker in self.stocks and OK == True:
                self.stocks[ticker][0] = self.stocks[ticker][0] + shares
            # pull current prices        
            self.current_prices()
        else:
            print("Please only enter a single ticker as a string")

        self.current_prices()
        # self.clean()
        
    def remove_ticker(self, ticker, shares=1) -> None:
        """Removes a ticker or tickers from the list from the list. Can be either a
        single ticker or a list.
        """
        if type(ticker) == str:
            if ticker in self.stocks:
                if self.stocks[ticker][0] > shares:
                    self.stocks[ticker][0] = self.stocks[ticker][0] - shares
                else:
                    self.stocks.pop(ticker)
            else:
                print("Unable to remove, " + ticker + " not found.")
        
        # pull current prices        
        self.current_prices()

    def clean(self) -> None:
        """Cleans the dictionary from tickers with no data found."""
        for stock in self.stocks:
            if len(self.stocks[stock]) != 2:
                self.stocks.pop(stock)

    def convert_cad(self, stock) -> dict:
        """Returns a new dictionary with all prices in CAD."""
        c = CurrencyRates()
        CAD = c.get_rates("USD")["CAD"]

        return (stock * CAD).round(2)
        
    def current_prices(self) -> None:
        """Returns the current prices attached to the individual ticker in a dictionary."""
        
        for stock in self.stocks:
            try:
                initialize = yf.Ticker(stock)
                price = initialize.history(period="max")["Close"][-1]
                if len(self.stocks[stock]) == 1:
                    if stock[-2:] != "TO":
                        self.stocks[stock].append(self.convert_cad(price))
                    else:
                        self.stocks[stock].append(price)
                elif len(self.stocks[stock]) == 0:
                    None
                else:
                    self.stocks[stock][1] == price

            except:
                print(stock + " not found, please enter another ticker.")

    def check_portfolio(self) -> list:
        """Returns the current holdings and their most recent price."""
        # add a filter to check if any invalid tickers are in a list
        print(self.stocks)
        return self.stocks

    def portfolio_value(self) -> float:
        """Returns the total value of all current holdings"""
        total_value = 0
        for stock in self.stocks:
            total_value += self.stocks[stock][0] * self.stocks[stock][1]

        return total_value

    def percent_gain(self, initial_investment) -> float:
        """Returns the net percent gain when compared to base."""

        current_value = self.portfolio_value()

        gain = ((current_value / initial_investment) - 1) * 100
        return str(gain.round(2)) + "%"

    


