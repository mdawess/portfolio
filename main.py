from stonk import Portfolio
import tkinter as tk

BASE = 1

portfolio = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "PM", "TSLA"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1]

test = Portfolio()
test.add_ticker("MSFT")
test.add_ticker("AAPL")
test.add_ticker("TSLA")
test.check_portfolio()


test.add_ticker(portfolio)
test.check_portfolio()

test.remove_ticker(["MSFT", "CGC", "AMZN"])
test.check_portfolio()