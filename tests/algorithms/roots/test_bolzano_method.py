import pytest
from src.algorithms.roots.bolzano_method import RootIsolationMethod

class TestRootIsolationMethod:
    def setup_method(self):
        self.method = RootIsolationMethod()

    def test_root_exists(self):
        # f(x) = x^2 - 4. Roots at -2, 2.
        # Interval [0, 3]. f(0)=-4, f(3)=5. Sign change.
        
        def func(x):
            return x**2 - 4

        result = self.method.solve(func, 0, 3)
        
        assert result['exists'] is True
        assert "Bolzano" in result['message']

    def test_root_does_not_exist_or_even(self):
        # f(x) = x^2 + 1. No real roots.
        # Interval [-1, 1]. f(-1)=2, f(1)=2. No sign change.
        
        def func(x):
            return x**2 + 1
            
        result = self.method.solve(func, -1, 1)
        
        assert result['exists'] is False
        assert "No sign change" in result['message']

    def test_exact_root_at_start(self):
        def func(x): return x
        
        result = self.method.solve(func, 0, 1)
        assert result['exists'] is True
        assert "at start" in result['message']

    def test_exact_root_at_end(self):
        def func(x): return x - 1
        
        result = self.method.solve(func, 0, 1)
        assert result['exists'] is True
        assert "at end" in result['message']

    def test_error_evaluation(self):
        def func(x): raise ValueError("oops")
        
        result = self.method.solve(func, 0, 1)
        assert result['exists'] is False
        assert "Error" in result['message']
