import numpy as np

def present_value(future_value, rate, periods):
    """
    Calculate the present value of a future sum of money.
    """
    return future_value / ((1 + rate) ** periods)

def future_value(present_value, rate, periods):
    """
    Calculate the future value of a present sum of money.
    """
    return present_value * ((1 + rate) ** periods)