from abc import ABC, abstractmethod

class NumericalMethod(ABC):
    """Abstract base class for all numerical methods."""
    
    @abstractmethod
    def solve(self, *args, **kwargs):
        """
        Execute the numerical method.
        
        Parameters and return types should be defined by concrete implementations.
        """
        pass
