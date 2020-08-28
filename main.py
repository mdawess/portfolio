from stonk import Portfolio
import tkinter as tk

BASE = 10000

PORTFOLIO = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "PM", "TSLA"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1]

test = Portfolio()
test.portfolioOwner = "Michael Dawes"
test.add_ticker("MSFT", 7)
test.add_ticker("TSLA", 5)

print(test.percent_gain(BASE))

test.portfolioOwner = "Michael Dawes"
