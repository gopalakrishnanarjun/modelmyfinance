import numpy as np

def sharpe_ratio(returns, risk_free_rate):
    """
    Calculate the Sharpe Ratio.
    """
    excess_return = np.mean(returns) - risk_free_rate
    std_dev = np.std(returns)
    return excess_return / std_dev

def beta(asset_returns, market_returns):
    """
    Calculate the Beta of a security.
    """
    covariance = np.cov(asset_returns, market_returns)[0][1]
    market_variance = np.var(market_returns)
    return covariance / market_variance
