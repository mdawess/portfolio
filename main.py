from stonk import Portfolio
from analysis import Analyze
import tkinter as tk
import dearpygui as gui

# ref https://pypi.org/project/dearpygui/

BASE = 10000

PORTFOLIO = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "YEKLALALSJNDJBDJHV", "PM", "TSLA"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1, 2]

myPortfolio = Portfolio()
myPortfolio.Owner = "Michael Dawes"

# for i in range(len(PORTFOLIO) - 1):
#     myPortfolio.add_ticker(PORTFOLIO[i], current_shares[i])
# myPortfolio.add_ticker("SPY")
# myPortfolio.add_ticker("MSFT", 3)
# myPortfolio.add_ticker("AAPL", 2)

# myPortfolio.add_ticker("TSLA", 2)
# myPortfolio.add_ticker("XYZ", 2)

test = Analyze(myPortfolio.check_portfolio(), myPortfolio.portfolio_value())
test.display_charts()


