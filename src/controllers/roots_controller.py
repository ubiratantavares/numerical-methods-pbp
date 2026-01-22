from typing import Tuple, Optional, Dict, Any
import sympy as sp
from src.algorithms.roots.graphical_method import GraphicalMethod
from src.views.graphical_view import GraphicalView
from src.algorithms.roots.analytical_method import AnalyticalMethod
from src.views.analytical_view import AnalyticalView
from src.algorithms.roots.table_method import TableMethod

class RootsController:
    def __init__(self):
        self.graphical_method = GraphicalMethod()
        self.graphical_view = GraphicalView()
        self.analytical_method = AnalyticalMethod()
        self.analytical_view = AnalyticalView()
        self.table_method = TableMethod()

    def plot_function(self, symbol: sp.Symbol, expression: sp.Expr, interval: Tuple[float, float], title: str = 'Graphical Method: Root Localization', label: Optional[str] = None):
        """
        Generates and displays the plot for the given function and interval.
        """
        print(f"Calculating plot for interval {interval}...")
        
        # Convert SymPy expression to callable for the numerical method
        f_callable = sp.lambdify(symbol, expression, "numpy")
        
        # Generate LaTeX label if not provided
        if label is None:
            label = f"$f({sp.latex(symbol)}) = {sp.latex(expression)}$"
            
        figure = self.graphical_method.solve(f_callable, interval, title=title, label=label)
        self.graphical_view.display(figure)

    def analyze_function(self, symbol: sp.Symbol, expression: sp.Expr, interval: Tuple[float, float]) -> Dict[str, Any]:
        """
        Performs analytical analysis (Bolzano + Derivatives) and displays results.
        Returns True if a root exists in the interval, False otherwise.
        """
        print(f"Analyzing function analytically in interval {interval}...")
        result = self.analytical_method.analyze(expression, symbol, interval)
        return result

    def analyze_verification(self, result: Dict[str, Any]) -> bool:
        """
        Performs analytical analysis (Bolzano + Derivatives) and displays results.
        Returns True if a root exists in the interval, False otherwise.
        """
        return result.get('exists', False)

    def analyze_display(self, result: Dict[str, Any]):
        """
        Performs analytical analysis (Bolzano + Derivatives) and displays results.
        Returns True if a root exists in the interval, False otherwise.
        """
        self.analytical_view.display(result)

    def find_bracketing_intervals(self, symbol: sp.Symbol, expression: sp.Expr, start: float, end: float, steps: int) -> Dict[str, Any]:
        """
        Uses the Table Method to find intervals that bracket roots.
        """
        print(f"Scanning interval [{start}, {end}] with {steps} steps...")
        f_callable = sp.lambdify(symbol, expression, "numpy")
        return self.table_method.solve(f_callable, start, end, steps)