import pytest
import sympy as sp
from src.algorithms.roots.analytical_method import AnalyticalMethod

def test_analytical_method_unique_root():
    """
    Test case: f(x) = x^2 - 4 in [0, 3]
    Root at x=2.
    f(0) = -4, f(3) = 5 -> Bolzano OK.
    f'(x) = 2x. In [0, 3], 2x >= 0. Monotonic. -> Unique OK.
    """
    method = AnalyticalMethod()
    x = sp.symbols('x')
    expr = x**2 - 4
    interval = (0, 3)

    result = method.analyze(expr, x, interval)

    assert result['exists'] is True
    assert result['unique'] is True
    assert result['details']['f_a'] == -4.0
    assert result['details']['f_b'] == 5.0

def test_analytical_method_no_root_bolzano_fails():
    """
    Test case: f(x) = x^2 + 1 in [-2, 2]
    No real roots.
    f(-2) = 5, f(2) = 5 -> Bolzano fails (product > 0).
    """
    method = AnalyticalMethod()
    x = sp.symbols('x')
    expr = x**2 + 1
    interval = (-2, 2)

    result = method.analyze(expr, x, interval)

    assert result['exists'] is False
    assert result['unique'] is None

def test_analytical_method_multiple_roots():
    """
    Test case: f(x) = sin(x) in [0, 4]
    Roots at 0 (endpoint), pi (~3.14).
    f(0) = 0, f(4) = sin(4) ~ -0.75.
    Wait, Bolzano requires f(a)*f(b) < 0. If f(a)=0, strictly it's not < 0.
    Let's use interval [1, 7] (~ 2pi range).
    Roots at pi (~3.14), 2pi (~6.28).
    f(1) > 0, f(7) > 0. Bolzano might fail if we pick bad points.
    
    Let's pick interval [2, 7].
    f(2) > 0, f(7) > 0. Bolzano fails.
    
    Let's pick interval [2, 5].
    Root at pi (~3.14).
    f(2) > 0, f(5) < 0. Bolzano OK.
    Derivative f'(x) = cos(x).
    In [2, 5], cos(x) changes sign (at pi/2 ~ 1.57 (outside), 3pi/2 ~ 4.71 (inside)).
    So unique should be False.
    """
    method = AnalyticalMethod()
    x = sp.symbols('x')
    expr = sp.sin(x)
    interval = (2, 5)

    result = method.analyze(expr, x, interval)

    assert result['exists'] is True
    assert result['unique'] is False # Derivative cos(x) is zero at 3pi/2 (~4.71), which is in [2, 5]

def test_analytical_method_invalid_interval():
    """
    Test case: f(x) = 1/x in [-1, 1]
    Discontinuous at 0.
    f(-1) = -1, f(1) = 1. Bolzano product < 0.
    But function is not continuous.
    Our current implementation doesn't check continuity explicitly (as per plan), 
    but let's see how it behaves.
    It should report exists=True based on endpoints, but unique might be tricky.
    f'(x) = -1/x^2. Always negative.
    So it might report unique=True, which is technically correct for the continuous parts, 
    but the theorem premise is violated.
    
    For now, let's just test that it runs without crashing.
    """
    method = AnalyticalMethod()
    x = sp.symbols('x')
    expr = 1/x
    interval = (-1, 1)

    # We expect it to run, results might be mathematically "garbage in, garbage out" 
    # regarding the theorem's guarantees, but the code should handle it.
    result = method.analyze(expr, x, interval)
    
    # In this specific case, f(-1)=-1, f(1)=1. Product < 0. Exists -> True.
    assert result['exists'] is True
