import yfinance as yf

class stonk:

    def __init__(self, ticker):
        
        self.ticker = yf.ticker(ticker)