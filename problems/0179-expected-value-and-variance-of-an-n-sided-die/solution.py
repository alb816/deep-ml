import numpy as np


def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    exp_val = np.sum(range(1, n + 1)) / n
    variance = np.sum((np.array(range(1, n+1)) - exp_val)**2) / n

    return exp_val, variance
