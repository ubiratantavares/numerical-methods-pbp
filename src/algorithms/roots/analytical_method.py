from typing import Tuple, Dict, Any, Optional
import sympy as sp
import numpy as np
from src.interfaces.numerical_method import NumericalMethod

class AnalyticalMethod(NumericalMethod):
    """
    Implements the Analytical Method for root localization using Bolzano's Theorem
    and derivative analysis for uniqueness.
    """

    def analyze(self, expression: sp.Expr, symbol: sp.Symbol, interval: Tuple[float, float]) -> Dict[str, Any]:
        """
        Analyzes the function within the given interval for root existence and uniqueness.

        Args:
            expression: The SymPy expression representing the function f(x).
            symbol: The SymPy symbol variable (e.g., x).
            interval: A tuple (a, b) defining the interval.

        Returns:
            A dictionary containing:
            - 'exists': bool (True if Bolzano's theorem is satisfied)
            - 'unique': Optional[bool] (True if derivative maintains sign, False if not, None if inconclusive)
            - 'details': dict (intermediate values like f(a), f(b), critical points)
        """
        a, b = interval
        
        # 1. Evaluate f(a) and f(b)
        # We use float() to ensure we get a numerical value for comparison
        try:
            f_a = float(expression.subs(symbol, a))
            f_b = float(expression.subs(symbol, b))
        except Exception as e:
             return {
                'exists': False,
                'unique': None,
                'details': {'error': f"Could not evaluate function at endpoints: {e}"}
            }

        # 2. Check Bolzano (Existence)
        # f(a) * f(b) < 0 implies at least one root
        exists = (f_a * f_b) < 0

        details = {
            'f_a': f_a,
            'f_b': f_b,
            'bolzano_product': f_a * f_b
        }

        if not exists:
            # If Bolzano fails, we can't guarantee existence (though roots might still exist if even number)
            # But for the purpose of this method as a "guarantee", we return False.
            return {
                'exists': False,
                'unique': None, # Not applicable if we don't even guarantee existence
                'details': details
            }

        # 3. Check Uniqueness (Derivative Analysis)
        # Calculate derivative
        derivative = sp.diff(expression, symbol)
        details['derivative'] = str(derivative)

        # To check if derivative maintains sign in [a, b], we can find critical points of the derivative
        # (i.e., where f''(x) = 0) or simply find where f'(x) = 0.
        # If f'(x) = 0 has no real solutions in [a, b], then f'(x) maintains sign (assuming continuity).
        
        try:
            # Find critical points where f'(x) = 0
            # We use solveset for a more robust solution set
            critical_points_set = sp.solveset(derivative, symbol, domain=sp.S.Reals)
            
            # Intersection with the open interval (a, b)
            # Monotonicity requires derivative to not change sign in the interior
            interval_set = sp.Interval.open(a, b)
            points_in_interval = critical_points_set.intersect(interval_set)
            
            details['critical_points_in_interval'] = str(points_in_interval)

            if points_in_interval.is_empty:
                # No critical points in the interval, derivative maintains sign
                unique = True
            else:
                # Derivative is zero at some point, monotonicity might change
                # Strictly speaking, if f'(x) touches 0 but doesn't cross (inflection), it's still monotonic.
                # But for a simple robust check, we flag it as potentially non-unique.
                unique = False
                
        except Exception as e:
            # Fallback or error in symbolic solving
            unique = None
            details['derivative_analysis_error'] = str(e)

        return {
            'exists': True,
            'unique': unique,
            'details': details
        }

    def solve(self, expression: sp.Expr, symbol: sp.Symbol) -> Dict[str, Any]:
        """
        Attempts to find the exact roots of the equation f(x) = 0 using analytical methods.

        Args:
            expression: The SymPy expression representing the function f(x).
            symbol: The SymPy symbol variable (e.g., x).

        Returns:
            A dictionary containing:
            - 'roots': List[sp.Expr] (List of exact roots found)
            - 'is_polynomial': bool (True if the expression is a polynomial)
            - 'degree': Optional[int] (Degree of the polynomial, if applicable)
            - 'message': str (Information about the solution process)
        """
        is_polynomial = expression.is_polynomial(symbol)
        degree = sp.degree(expression, symbol) if is_polynomial else None
        
        roots = []
        message = ""

        try:
            # Attempt to solve the equation f(x) = 0
            # SymPy's solve function returns a list of solutions
            solutions = sp.solve(expression, symbol)
            
            # Filter solutions to ensure they are valid (sometimes solve returns empty or complex if not specified)
            # We will return all found solutions, including complex ones, as they are "exact".
            roots = solutions
            
            if is_polynomial:
                if degree == 1:
                    message = "Linear equation solved exactly (Euclides)."
                elif degree == 2:
                    message = "Quadratic equation solved exactly (Bhaskara/Sridhara)."
                elif degree == 3:
                    message = "Cubic equation solved exactly (Cardano/Tartaglia)."
                elif degree == 4:
                    message = "Quartic equation solved exactly (Ferrari)."
                elif degree >= 5:
                    message = "Polynomial of degree >= 5. Exact solutions might not exist (Abel-Ruffini). SymPy returned what it could find."
            else:
                message = "Non-polynomial equation. Exact solutions attempted."

        except Exception as e:
            message = f"Error attempting to solve analytically: {str(e)}"

        return {
            'roots': roots,
            'is_polynomial': is_polynomial,
            'degree': degree,
            'message': message
        }
