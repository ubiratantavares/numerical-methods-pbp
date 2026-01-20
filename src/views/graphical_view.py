import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class GraphicalView:
    def display(self, figure: Figure, block: bool = True):
        """
        Displays the given matplotlib figure.
        
        Args:
            figure: The figure to display.
            block: Whether to block execution until the window is closed.
        """
        # We need to ensure the figure is the active one for plt.show() to work naturally 
        # with the state-machine interface if we were using it, but since we have the figure object:
        
        # If there are no managers, we might need to create a dummy one or just use show() 
        # if the figure was created with pyplot.subplots (which it was in the model).
        
        plt.show(block=block)
