from typing import Tuple, Optional
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class FunctionPlotter:
    """
    Utility class to plot a given function using SymPy for automatic label generation.
    """
    def __init__(self, x: sp.Symbol, y: sp.Expr, interval: Tuple[float, float], title: str = "Function Plot"):
        """
        Args:
            x: The SymPy symbol variable.
            y: The SymPy expression to be plotted.
            interval: A tuple (start, end) defining the x-axis range.
            title: Title of the plot.
        """
        self.symbol = x
        self.expression = y
        self.interval = interval
        self.title = title
        self.f = sp.lambdify(x, y, "numpy")
        self.latex_label = f"$f({sp.latex(x)}) = {sp.latex(y)}$"

    def plot(self, num_points: int = 1000, label: Optional[str] = None):
        """
        Plots the function.

        Args:
            num_points: Number of points to generate for the plot.
            label: Label for the function in the legend. If None, uses the automatic LaTeX label.
        """
        x_start, x_end = self.interval
        x = np.linspace(x_start, x_end, num_points)
        y = self.f(x)

        if label is None:
            label = self.latex_label

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=label, color='blue')
        plt.axhline(0, color='black', linewidth=1, linestyle='-') # x-axis
        plt.axvline(0, color='black', linewidth=1, linestyle='-') # y-axis
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.title(self.title)
        plt.xlabel(f'${sp.latex(self.symbol)}$')
        plt.ylabel(f'$f({sp.latex(self.symbol)})$')
        plt.legend()
        plt.show()
