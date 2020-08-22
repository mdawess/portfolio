from stonk import stk

BASE = 1

portfolio = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "PM"]

test = stk(portfolio)
print(test.current_prices())