import numpy as np


def _poly_der(c):
    """Коэффициенты производной: d_j = (j+1) * c[j+1]."""
    c = np.asarray(c, float)
    return c[1:] * np.arange(1, len(c))      # константа -> пустой массив

def _mul(a, b):
    """Произведение многочленов (пустой массив = нулевой многочлен)."""
    if a.size == 0 or b.size == 0:
        return np.zeros(max(a.size + b.size - 1, 1))   # было: max(..., 0)
    return np.convolve(a, b)
 
def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    f, g = np.array(f_coeffs, float), np.array(g_coeffs, float)
    res = _mul(_poly_der(f), g) + _mul(f, _poly_der(g))
    return np.round(res, 4).tolist() 

           