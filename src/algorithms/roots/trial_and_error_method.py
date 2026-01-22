from typing import Callable, Dict, Any
import random
from src.interfaces.numerical_method import NumericalMethod

class TrialAndErrorMethod(NumericalMethod):
    """
    Implements the Trial and Error Method (Força Bruta) for root finding.
    This method randomly samples the interval to find a root approximation.
    """

    def solve(self, function: Callable[[float], float], start: float, end: float, tolerance: float, max_attempts: int) -> Dict[str, Any]:
        """
        Attempts to find a root by randomly sampling the interval [start, end].

        Args:
            function: The function f(x) to evaluate.
            start: The starting point of the interval.
            end: The ending point of the interval.
            tolerance: The acceptance tolerance for |f(x)|.
            max_attempts: The maximum number of random samples.

        Returns:
            A dictionary containing:
            - 'root': float (The best root approximation found)
            - 'error': float (The absolute value of f(root))
            - 'iterations': int (Number of attempts made)
            - 'converged': bool (True if error < tolerance)
            - 'message': str (Status message)
        """
        if max_attempts <= 0:
            raise ValueError("max_attempts must be positive.")
        if tolerance < 0:
            raise ValueError("tolerance must be non-negative.")

        best_x = None
        min_error = float('inf')
        iterations = 0
        converged = False

        for i in range(max_attempts):
            iterations += 1
            # Random sample in [start, end]
            x = random.uniform(start, end)
            
            try:
                f_x = function(x)
                error = abs(f_x)
            except Exception as e:
                # If evaluation fails, skip this point
                continue

            if error < min_error:
                min_error = error
                best_x = x

            if min_error < tolerance:
                converged = True
                break
        
        message = "Converged to tolerance." if converged else "Max attempts reached without converging to tolerance."

        return {
            'root': best_x,
            'error': min_error,
            'iterations': iterations,
            'converged': converged,
            'message': message
        }
