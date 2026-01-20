import pytest
import sympy as sp
from src.algorithms.roots.analytical_method import AnalyticalMethod

class TestAnalyticalMethod:
    def setup_method(self):
        self.method = AnalyticalMethod()
        self.x = sp.Symbol('x')

    def test_linear_equation(self):
        # 2x - 4 = 0 -> x = 2
        expr = 2 * self.x - 4
        result = self.method.solve(expr, self.x)
        
        assert result['is_polynomial'] is True
        assert result['degree'] == 1
        assert len(result['roots']) == 1
        assert result['roots'][0] == 2
        assert "Euclides" in result['message']

    def test_quadratic_equation(self):
        # x^2 - 5x + 6 = 0 -> x = 2, x = 3
        expr = self.x**2 - 5 * self.x + 6
        result = self.method.solve(expr, self.x)
        
        assert result['is_polynomial'] is True
        assert result['degree'] == 2
        assert len(result['roots']) == 2
        assert 2 in result['roots']
        assert 3 in result['roots']
        assert "Bhaskara" in result['message']

    def test_cubic_equation(self):
        # x^3 - 6x^2 + 11x - 6 = 0 -> x = 1, x = 2, x = 3
        expr = self.x**3 - 6 * self.x**2 + 11 * self.x - 6
        result = self.method.solve(expr, self.x)
        
        assert result['is_polynomial'] is True
        assert result['degree'] == 3
        assert len(result['roots']) == 3
        assert 1 in result['roots']
        assert 2 in result['roots']
        assert 3 in result['roots']
        assert "Cardano" in result['message']

    def test_quartic_equation(self):
        # x^4 - 1 = 0 -> x = 1, -1, i, -i
        expr = self.x**4 - 1
        result = self.method.solve(expr, self.x)
        
        assert result['is_polynomial'] is True
        assert result['degree'] == 4
        assert len(result['roots']) == 4
        assert 1 in result['roots']
        assert -1 in result['roots']
        assert sp.I in result['roots']
        assert -sp.I in result['roots']
        assert "Ferrari" in result['message']

    def test_quintic_equation(self):
        # x^5 - x - 1 = 0 (Not solvable by radicals in general, but this one might have roots SymPy can find or represent implicitly)
        # Let's use a simple one: x^5 - 1 = 0
        expr = self.x**5 - 1
        result = self.method.solve(expr, self.x)
        
        assert result['is_polynomial'] is True
        assert result['degree'] == 5
        assert len(result['roots']) == 5 # SymPy finds roots of unity
        assert "Abel-Ruffini" in result['message']

    def test_non_polynomial(self):
        # e^x - 1 = 0 -> x = 0
        expr = sp.exp(self.x) - 1
        result = self.method.solve(expr, self.x)
        
        assert result['is_polynomial'] is False
        assert result['degree'] is None
        assert 0 in result['roots']
        assert "Non-polynomial" in result['message']

    def test_unsolvable_symbolically(self):
        # x + cos(x) = 0 (Transcendental, usually no closed form)
        # SymPy might return an empty list or a ConditionSet or similar.
        # For this test, we just want to ensure it doesn't crash and returns a result structure.
        expr = self.x + sp.cos(self.x)
        result = self.method.solve(expr, self.x)
        
        assert 'roots' in result
        assert 'message' in result
