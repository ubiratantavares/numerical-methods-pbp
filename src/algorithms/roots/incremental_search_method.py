from typing import Callable, List, Tuple, Any, Dict
import numpy as np
from src.interfaces.numerical_method import NumericalMethod

class IncrementalSearchMethod(NumericalMethod):
    """
    Implements the Incremental Search Method (Busca Incremental) for root localization.
    This method scans the interval with a fixed step size.
    """

    def solve(self, function: Callable[[float], float], start: float, end: float, step_size: float) -> Dict[str, Any]:
        """
        Scans the interval [start, end] with a fixed step_size to find sub-intervals containing roots.

        Args:
            function: The function f(x) to evaluate.
            start: The starting point of the interval.
            end: The ending point of the interval.
            step_size: The fixed size of each step (delta x).

        Returns:
            A dictionary containing:
            - 'intervals': List[Tuple[float, float]] (List of intervals where sign change occurred)
            - 'exact_roots': List[float] (List of points where f(x) == 0 exactly)
            - 'step_size': float (The step size used)
            - 'evaluations': int (Number of function evaluations)
        """
        if step_size <= 0:
            raise ValueError("Step size must be positive.")
        
        if start >= end:
             raise ValueError("Start must be less than end.")

        intervals = []
        exact_roots = []
        
        x_current = start
        try:
            f_current = function(x_current)
        except Exception as e:
             return {'error': f"Error evaluating function at start: {e}"}

        evaluations = 1
        
        # We iterate while x_current < end. 
        # To avoid infinite loops with floating point issues, we might want a safety break or use arange logic,
        # but a while loop is more true to the "incremental" definition.
        
        while x_current < end:
            x_next = x_current + step_size
            
            # Clamp x_next to end if it overshoots slightly due to float math, 
            # or if we want to strictly stop at end. 
            # Usually incremental search goes up to end.
            if x_next > end:
                x_next = end
                
            # If we are effectively at the same point (step too small vs precision), break to avoid infinite loop
            if x_next <= x_current:
                break

            try:
                f_next = function(x_next)
                evaluations += 1
            except Exception as e:
                # Skip interval if evaluation fails
                x_current = x_next
                f_current = float('nan')
                continue

            # Check for exact root at start point (only on first iteration or if skipped)
            if x_current == start and f_current == 0:
                exact_roots.append(x_current)

            # Check for exact root at next point
            if f_next == 0:
                exact_roots.append(x_next)
            
            # Check for sign change (Bolzano)
            if f_current * f_next < 0:
                intervals.append((x_current, x_next))

            x_current = x_next
            f_current = f_next
            
            # If we reached the end, break
            if x_current >= end:
                break

        return {
            'intervals': intervals,
            'exact_roots': exact_roots,
            'step_size': step_size,
            'evaluations': evaluations
        }
