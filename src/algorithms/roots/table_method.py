from typing import Callable, List, Tuple, Any, Dict
import numpy as np
from src.interfaces.numerical_method import NumericalMethod

class TableMethod(NumericalMethod):
    """
    Implements the Table Method (Varredura / Incremental Search) for root localization.
    """

    def solve(self, function: Callable[[float], float], start: float, end: float, steps: int) -> Dict[str, Any]:
        """
        Scans the interval [start, end] to find sub-intervals containing roots.

        Args:
            function: The function f(x) to evaluate.
            start: The starting point of the interval.
            end: The ending point of the interval.
            steps: The number of steps (sub-intervals) to divide the interval into.

        Returns:
            A dictionary containing:
            - 'intervals': List[Tuple[float, float]] (List of intervals where sign change occurred)
            - 'exact_roots': List[float] (List of points where f(x) == 0 exactly)
            - 'step_size': float (The size of each step h)
            - 'evaluations': int (Number of function evaluations)
        """
        if steps <= 0:
            raise ValueError("Number of steps must be positive.")

        h = (end - start) / steps
        intervals = []
        exact_roots = []
        
        x_current = start
        try:
            f_current = function(x_current)
        except Exception as e:
             return {'error': f"Error evaluating function at start: {e}"}

        evaluations = 1

        for i in range(steps):
            x_next = start + (i + 1) * h # Use multiplication to avoid accumulating float error
            
            try:
                f_next = function(x_next)
                evaluations += 1
            except Exception as e:
                # If we can't evaluate, we skip this interval but continue
                x_current = x_next
                f_current = float('nan') # Placeholder
                continue

            # Check for exact root at start point (only on first iteration or if skipped)
            if i == 0 and f_current == 0:
                exact_roots.append(x_current)

            # Check for exact root at next point
            if f_next == 0:
                exact_roots.append(x_next)
            
            # Check for sign change (Bolzano)
            # We check f_current * f_next < 0
            # We handle cases where one is zero separately above, so strictly < 0 implies sign change
            if f_current * f_next < 0:
                intervals.append((x_current, x_next))

            x_current = x_next
            f_current = f_next

        return {
            'intervals': intervals,
            'exact_roots': exact_roots,
            'step_size': h,
            'evaluations': evaluations
        }
