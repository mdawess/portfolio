from stonk import Portfolio
import tkinter as tk

BASE = 1

PORTFOLIO = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "PM", "TSLA"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1]

test = Portfolio()
test.add_ticker("MSFT")
test.add_ticker("TSLA")


test.check_portfolio()

# test.remove_ticker("MSFT", 3)
test.remove_ticker("AAPL", 3)
test.check_portfolio()

# test.remove_ticker("MSFT", 9)
test.check_portfolio()



test.remove_ticker("MSFT", 222222)
test.check_portfolio()