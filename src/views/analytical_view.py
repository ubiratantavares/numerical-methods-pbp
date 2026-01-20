from typing import Dict, Any

class AnalyticalView:
    """
    View responsible for displaying the results of the Analytical Method analysis.
    """

    def display(self, result: Dict[str, Any]):
        """
        Displays the analysis results in a formatted manner.

        Args:
            result: A dictionary containing the analysis results from AnalyticalMethod.
        """
        print("\n--- Analytical Method Results ---")
        
        exists = result.get('exists')
        unique = result.get('unique')
        details = result.get('details', {})

        print(f"Root Existence (Bolzano): {'CONFIRMED' if exists else 'NOT GUARANTEED'}")
        
        if unique is True:
            unique_str = "GUARANTEED (Monotonic)"
        elif unique is False:
            unique_str = "NOT GUARANTEED (Derivative changes sign)"
        else:
            unique_str = "INCONCLUSIVE"
            
        print(f"Root Uniqueness: {unique_str}")
        
        print("\nDetailed Analysis:")
        if 'f_a' in details and 'f_b' in details:
            print(f"  f(a) = {details['f_a']}")
            print(f"  f(b) = {details['f_b']}")
            print(f"  f(a)*f(b) = {details['bolzano_product']}")
        
        if 'derivative' in details:
            print(f"  Derivative: {details['derivative']}")
            
        if 'critical_points_in_interval' in details:
            print(f"  Critical Points in Interval: {details['critical_points_in_interval']}")
            
        if 'error' in details:
            print(f"  Error: {details['error']}")
            
        print("---------------------------------")
