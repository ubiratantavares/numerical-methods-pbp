from typing import Callable, Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from src.interfaces.numerical_method import NumericalMethod

class GraphicalMethod(NumericalMethod):
    def solve(self, f: Callable[[float], float], interval: Tuple[float, float], num_points: int = 1000, title: str = 'Graphical Method: Root Localization', label: str = 'f(x)') -> Figure:
        """
        Generates a plot of the function f over the given interval.

        Args:
            f: The function to plot.
            interval: A tuple (start, end) defining the x-axis range.
            num_points: Number of points to generate for the plot.
            title: Title of the plot.
            label: Label for the function in the legend.

        Returns:
            A matplotlib Figure object containing the plot.
        """
        x_start, x_end = interval
        x = np.linspace(x_start, x_end, num_points)
        y = f(x)

        fig, ax = plt.subplots()
        ax.plot(x, y, label=label)
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--') # x-axis
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        ax.set_title(title)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()

        return fig
