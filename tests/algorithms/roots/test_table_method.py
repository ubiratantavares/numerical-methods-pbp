import pytest
import math
from src.algorithms.roots.table_method import TableMethod

class TestTableMethod:
    def setup_method(self):
        self.method = TableMethod()

    def test_simple_polynomial_sign_change(self):
        # f(x) = x^2 - 4. Roots at -2 and 2.
        # Interval [-3, 3], steps=6 -> step=1
        # Points: -3, -2, -1, 0, 1, 2, 3
        # Values: 5, 0, -3, -4, -3, 0, 5
        # Sign changes: (-3, -2) [no, touches 0], (-2, -1) [0 to -], (-1, 0) [- to -], ...
        # Our implementation separates exact roots.
        
        def func(x):
            return x**2 - 4

        result = self.method.solve(func, -3, 3, 6)
        
        # Exact roots should be found at -2 and 2
        assert -2.0 in result['exact_roots']
        assert 2.0 in result['exact_roots']
        
        # Intervals with sign change strictly < 0.
        # Between -3 (5) and -2 (0) -> product 0. Not strictly < 0.
        # Between -2 (0) and -1 (-3) -> product 0.
        # Wait, if we hit exact roots, we might not report intervals if the root is exactly on the grid.
        # Let's test an interval where root is NOT on grid.
        
    def test_root_within_interval(self):
        # f(x) = x^2 - 2. Root at sqrt(2) approx 1.414
        # Interval [0, 2], steps=2 -> points 0, 1, 2
        # f(0)=-2, f(1)=-1, f(2)=2
        # Sign change between 1 and 2.
        
        def func(x):
            return x**2 - 2
            
        result = self.method.solve(func, 0, 2, 2)
        
        assert len(result['intervals']) == 1
        assert result['intervals'][0] == (1.0, 2.0)
        assert len(result['exact_roots']) == 0

    def test_multiple_roots(self):
        # f(x) = sin(x) in [0, 2pi] approx [0, 6.28]
        # Roots at 0, pi (3.14), 2pi (6.28)
        # Let's use steps that don't hit pi exactly.
        
        def func(x):
            return math.sin(x)
            
        # 0 to 7, steps=7 -> 0, 1, 2, 3, 4, 5, 6, 7
        # sin(0)=0, sin(1)>0, sin(2)>0, sin(3)>0, sin(4)<0...
        # Sign change between 3 and 4 (since pi is 3.14)
        
        result = self.method.solve(func, 0, 7, 7)
        
        # Root at 0 is exact
        assert 0.0 in result['exact_roots']
        
        # Root at pi is between 3 and 4
        assert (3.0, 4.0) in result['intervals']
        
        # Root at 2pi (6.28) is between 6 and 7
        assert (6.0, 7.0) in result['intervals']

    def test_no_roots(self):
        # f(x) = x^2 + 1
        def func(x):
            return x**2 + 1
            
        result = self.method.solve(func, -5, 5, 10)
        
        assert len(result['intervals']) == 0
        assert len(result['exact_roots']) == 0

    def test_invalid_steps(self):
        def func(x): return x
        with pytest.raises(ValueError):
            self.method.solve(func, 0, 1, 0)
