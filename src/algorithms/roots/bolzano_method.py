from typing import Callable, Dict, Any
from src.interfaces.numerical_method import NumericalMethod

class RootIsolationMethod(NumericalMethod):
    """
    Implements the Root Isolation Method based on Bolzano's Theorem.
    Verifies if an interval contains a root by checking for sign changes.
    """

    def solve(self, function: Callable[[float], float], start: float, end: float) -> Dict[str, Any]:
        """
        Verifies if the interval [start, end] contains at least one root using Bolzano's Theorem.

        Args:
            function: The function f(x) to evaluate.
            start: The starting point of the interval.
            end: The ending point of the interval.

        Returns:
            A dictionary containing:
            - 'exists': bool (True if f(start) * f(end) < 0)
            - 'f_start': float (Value of f(start))
            - 'f_end': float (Value of f(end))
            - 'message': str (Status message)
        """
        try:
            f_start = function(start)
            f_end = function(end)
        except Exception as e:
            return {
                'exists': False,
                'f_start': None,
                'f_end': None,
                'message': f"Error evaluating function: {e}"
            }

        # Check for exact roots at boundaries
        if f_start == 0:
            return {
                'exists': True,
                'f_start': f_start,
                'f_end': f_end,
                'message': "Root found exactly at start of interval."
            }
        
        if f_end == 0:
            return {
                'exists': True,
                'f_start': f_start,
                'f_end': f_end,
                'message': "Root found exactly at end of interval."
            }

        # Bolzano's Theorem check
        if f_start * f_end < 0:
            return {
                'exists': True,
                'f_start': f_start,
                'f_end': f_end,
                'message': "Sign change detected. Root exists in interval (Bolzano)."
            }
        else:
            return {
                'exists': False,
                'f_start': f_start,
                'f_end': f_end,
                'message': "No sign change detected. Inconclusive (might have 0 or even number of roots)."
            }
