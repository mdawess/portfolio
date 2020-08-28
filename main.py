from stonk import Portfolio
import tkinter as tk

BASE = 1

PORTFOLIO = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "PM", "TSLA"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1]

test = Portfolio()
test.add_ticker("MSFT", 7)
test.add_ticker("TSLA", 5)

#test.check_portfolio()

print(test.portfolio_value())

test.remove_ticker("TSLA", 3)

print(test.portfolio_value())
