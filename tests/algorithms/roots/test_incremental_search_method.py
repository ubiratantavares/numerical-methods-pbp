import pytest
import math
from src.algorithms.roots.incremental_search_method import IncrementalSearchMethod

class TestIncrementalSearchMethod:
    def setup_method(self):
        self.method = IncrementalSearchMethod()

    def test_simple_sign_change(self):
        # f(x) = x^2 - 4. Roots at -2 and 2.
        # Interval [-3, 3], step=1.0
        # Points: -3, -2, -1, 0, 1, 2, 3
        
        def func(x):
            return x**2 - 4

        result = self.method.solve(func, -3, 3, 1.0)
        
        # Exact roots should be found at -2 and 2
        assert -2.0 in result['exact_roots']
        assert 2.0 in result['exact_roots']
        
        # Intervals:
        # (-2, -1): f(-2)=0, f(-1)=-3. Product 0. No sign change detected by strict < 0 check.
        # (-1, 0): f(-1)=-3, f(0)=-4. No change.
        # (0, 1): f(0)=-4, f(1)=-3. No change.
        # (1, 2): f(1)=-3, f(2)=0. No change.
        
        # Let's try a step that doesn't hit the root exactly.
        # Step 0.9
        # -3 -> 5
        # -2.1 -> 0.41
        # -1.2 -> -2.56 (Sign change -2.1 to -1.2)
        
        result_offset = self.method.solve(func, -3, 3, 0.9)
        # We expect a sign change around -2 and 2
        
        has_neg_root = any(i[0] <= -2 <= i[1] for i in result_offset['intervals'])
        has_pos_root = any(i[0] <= 2 <= i[1] for i in result_offset['intervals'])
        
        assert has_neg_root
        assert has_pos_root

    def test_multiple_roots(self):
        # f(x) = sin(x) in [0, 7]
        # Roots at 0, pi(3.14), 2pi(6.28)
        
        def func(x):
            return math.sin(x)
            
        result = self.method.solve(func, 0, 7, 0.5)
        
        # Root at 0 is exact
        assert 0.0 in result['exact_roots']
        
        # Root at pi (3.14) should be bracketed
        # 3.0 -> sin(3) > 0
        # 3.5 -> sin(3.5) < 0
        assert any(i == (3.0, 3.5) for i in result['intervals'])
        
        # Root at 2pi (6.28) should be bracketed
        # 6.0 -> sin(6) < 0
        # 6.5 -> sin(6.5) > 0
        assert any(i == (6.0, 6.5) for i in result['intervals'])

    def test_no_roots(self):
        # f(x) = x^2 + 1
        def func(x):
            return x**2 + 1
            
        result = self.method.solve(func, -5, 5, 0.5)
        
        assert len(result['intervals']) == 0
        assert len(result['exact_roots']) == 0

    def test_invalid_params(self):
        def func(x): return x
        
        with pytest.raises(ValueError):
            self.method.solve(func, 0, 1, -0.1)
            
        with pytest.raises(ValueError):
            self.method.solve(func, 2, 1, 0.1)
