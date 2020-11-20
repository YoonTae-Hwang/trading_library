import pandas as pd
import numpy as np
import math

class Performacne(object):
    def __init__(self, day):
        self.day = day

    def average(self, returns):
        """
        Annualized Aritmetic Average Return

        """
        return returns.mean() * self.day

    def geo_average(self, returns):
        """
        Annualized Geometrice Average Return
        """
        return (1 + returns).prod() ** (self.day / len(returns)) - 1

    def stdev(self, returns):
        """
        Annualized Standard Deviation
        """
        return returns.std() * np.sqrt(self.day)

    def down_stdev(self, returns, target = 0.0):
        """
        Downside Standard Deviation
        """
        returns = returns.copy()
        returns.loc[returns > target] = 0
        sum = (returns ** 2).sum()
        return np.sqrt(self.day * sum / len(returns))

    def up_stdev(self, returns, target = 0.0):
        """
        Downside Standard Deviation
        """
        returns = returns.copy()
        returns.loc[returns < target] = 0
        sum = (returns ** 2).sum()
        return np.sqrt(self.day * sum / len(returns))

    def cov(self, returns, benchmark):
        """
        Covariance
        """
        return returns.cov(benchmark) * self.day

    def corr(self, returns, benchmark):
        """
        Correlation
        """
        return returns.corr(benchmark)

    def skewness(self, returns):
        return returns.skew()

    def kurtosis(self, returns):
        return returns.kurtosis()

    def coskewness(self, returns, benchmark):
        T = len(returns)
        sum = ((returns - returns.mean() * (benchmark - benchmark.mean()) ** 2) / (returns.std() * (benchmark ** 2 ))).sum()
        return T / ( (T-1) * (T-2) ) * sum




