from stonk import Portfolio

BASE = 1

portfolio = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "PM"]

current_shares = [10, 20, 35, 5, 12, 1, 11, 6, 1, 1]

test = Portfolio(portfolio)
print(test.current_prices())