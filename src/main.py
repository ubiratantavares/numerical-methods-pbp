import sys
import os
import sympy as sp

# Add the project root to sys.path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.domain.functions import *
from src.utils.plotter import FunctionPlotter
from src.algorithms.roots.analytical_method import AnalyticalMethod
from src.controllers.roots_controller import RootsController

def main():
    x = sp.symbols('x')

    y = function_01(x)
    
    controller = RootsController()
    
    interval = (1, 2)

    result = controller.analyze_function(x, y, interval)

    controller.analyze_display(result)

    if (controller.analyze_verification(result)):

        controller.plot_function(x, y, interval)

if __name__ == "__main__":
    main()
