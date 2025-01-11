import numpy as np

def portfolio_return(weights, returns):
    """
    Calculate the expected return of a portfolio.
    """
    return np.dot(weights, returns)

def portfolio_variance(weights, covariance_matrix):
    """
    Calculate the variance of a portfolio.
    """
    return np.dot(weights.T, np.dot(covariance_matrix, weights))

# Example Usage:
# After installing the package, you can use it like this:

# from modelmyfinance import present_value, sharpe_ratio
# pv = present_value(1000, 0.05, 5)
# print("Present Value:", pv)

# sr = sharpe_ratio([0.01, 0.02, 0.015], 0.005)
# print("Sharpe Ratio:", sr)