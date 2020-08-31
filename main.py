from stonk import Portfolio
from analysis import Analyze
from tkinter import *


# ref https://pypi.org/project/dearpygui/

BASE = 10000

PORTFOLIO = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "YEKLALALSJNDJBDJHV", "PM", "TSLA"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1, 2]

myPortfolio = Portfolio()
myPortfolio.Owner = "Michael"
myPortfolio.add_ticker("AAPL")

test = Analyze(myPortfolio.check_portfolio(), myPortfolio.portfolio_value())
# test.display_charts()

window = Tk()

window.title(myPortfolio.Owner + "'s Portfolio")
window.geometry("800x800")

btn1 = Button(window, text="Click to add a stock to the portfolio", bg="blue", fg="red", 
              COMMAND="myPortfolio.add_ticker(str(input('Please enter a ticker you would like to add to the portfolio')))")
btn1.place(x=80, y=100)

window.mainloop()