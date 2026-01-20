from dataclasses import dataclass

class NumericalError(Exception):
    """Base class for all numerical errors."""
    pass

class ConvergenceError(NumericalError):
    """Raised when a method fails to converge within the maximum number of iterations."""
    pass

def absolute_error(true_val: float, approx_val: float) -> float:
    """Calculates the absolute error: |true_val - approx_val|."""
    return abs(true_val - approx_val)

def relative_error(true_val: float, approx_val: float) -> float:
    """
    Calculates the relative error: |true_val - approx_val| / |true_val|.
    Raises ZeroDivisionError if true_val is 0.
    """
    if true_val == 0:
        raise ZeroDivisionError("Cannot calculate relative error when true value is 0.")
    return abs(true_val - approx_val) / abs(true_val)
