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

    # 1. Define the function
    y = function_01(x)
    
    controller = RootsController()
    
    # 2. Define a broad search interval for the Table Method (Varredura)
    search_start = -10
    search_end = 10
    steps = search_end - search_start
    
    print(f"\n--- 1. Table Method (Varredura) ---")
    # Use Table Method to find candidate intervals
    table_result = controller.find_bracketing_intervals(x, y, search_start, search_end, steps)
    
    intervals = table_result.get('intervals', [])
    exact_roots = table_result.get('exact_roots', [])
    
    print(f"Exact roots found during scan: {exact_roots}")
    print(f"Candidate intervals found: {intervals}")

    # 3. Analyze each candidate interval
    if intervals:
        print(f"\n--- 2. Analytical Method (Verification) ---")
        for interval in intervals:
            print(f"\nChecking interval: {interval}")
            
            # Use Analytical Method to verify existence and uniqueness
            analysis_result = controller.analyze_function(x, y, interval)
            controller.analyze_display(analysis_result)
            
            # 4. Visualize if confirmed
            if controller.analyze_verification(analysis_result):
                print(f"\n--- 3. Graphical Method (Visualization) ---")
                controller.plot_function(x, y, interval, title=f"Root in {interval}")
    else:
        print("\nNo intervals with sign changes found in the search range.")

if __name__ == "__main__":
    main()
