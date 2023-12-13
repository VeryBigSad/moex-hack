from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd

class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20

    @staticmethod
    def SMA(values, n):
        return pd.Series(values).rolling(n).mean()

    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(self.SMA, self.data.Close, self.n1)
        self.sma2 = self.I(self.SMA, self.data.Close, self.n2)

    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()
        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()
