import yfinance as yf

o = {1, 2, 4}
print(len(o))

PORTFOLIO = ["CGC", "TD.TO", "WCN", "BMO.TO", "BNS.TO", "NFI.TO", "VCN.TO", 
            "VOO", "SPY", "YEKLALALSJNDJBDJHV", "PM", "TSLA"]

def check(s):
    
    OK = False
    try:
        i = yf.Ticker("XYZ")
        x = i.history(period="max")["Close"][-1]
        OK = True

    except:
        print("Ticker is not listed")

    return OK

print(check("SPY"))