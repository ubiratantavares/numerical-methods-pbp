import pytest
import random
from src.algorithms.roots.trial_and_error_method import TrialAndErrorMethod

class TestTrialAndErrorMethod:
    def setup_method(self):
        self.method = TrialAndErrorMethod()
        # Seed random for reproducibility in tests
        random.seed(42)

    def test_find_root_success(self):
        # f(x) = x^2 - 4. Root at 2.
        # Interval [1.5, 2.5]. Tolerance 0.1.
        # With enough attempts, it should find something close to 2.
        
        def func(x):
            return x**2 - 4

        result = self.method.solve(func, 1.5, 2.5, tolerance=0.1, max_attempts=1000)
        
        assert result['converged'] is True
        assert abs(result['root'] - 2.0) < 0.1 # Approximate check
        assert result['error'] < 0.1

    def test_fail_to_converge(self):
        # f(x) = x^2 + 10. No roots.
        # Interval [-5, 5].
        
        def func(x):
            return x**2 + 10
            
        result = self.method.solve(func, -5, 5, tolerance=0.1, max_attempts=100)
        
        assert result['converged'] is False
        assert result['iterations'] == 100
        assert result['root'] is not None # Should return best guess (min error)

    def test_invalid_params(self):
        def func(x): return x
        
        with pytest.raises(ValueError):
            self.method.solve(func, 0, 1, tolerance=-0.1, max_attempts=10)
            
        with pytest.raises(ValueError):
            self.method.solve(func, 0, 1, tolerance=0.1, max_attempts=0)

    def test_best_approximation(self):
        # Even if not converged, it should return the x that minimized |f(x)|
        # f(x) = x - 100. Interval [0, 10]. Min error at x=10 (f(x)=-90).
        
        def func(x):
            return x - 100
            
        result = self.method.solve(func, 0, 10, tolerance=0.1, max_attempts=50)
        
        assert result['converged'] is False
        # Best x should be close to 10 (the upper bound)
        assert result['root'] > 9.0 
        assert result['error'] > 80.0 # Error is roughly 90
