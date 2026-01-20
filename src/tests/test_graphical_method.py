import pytest
import numpy as np
from matplotlib.figure import Figure
from src.algorithms.roots.graphical_method import GraphicalMethod

def test_graphical_method_returns_figure():
    method = GraphicalMethod()
    f = lambda x: x**2 - 4
    interval = (-3, 3)
    
    fig = method.solve(f, interval)
    
    assert isinstance(fig, Figure)
    assert len(fig.axes) > 0
    ax = fig.axes[0]
    assert ax.get_title() == 'Graphical Method: Root Localization'
    
    # Check if data is plotted
    lines = ax.get_lines()
    # Expecting at least the function plot. 
    # Note: axhline might not be in get_lines() depending on implementation, but plot() definitely is.
    assert len(lines) >= 1 
    
    # Verify x data range
    x_data = lines[0].get_xdata()
    assert np.isclose(x_data.min(), -3)
    assert np.isclose(x_data.max(), 3)

def test_graphical_method_custom_title_and_label():
    method = GraphicalMethod()
    f = lambda x: x**2 - 4
    interval = (-3, 3)
    custom_title = "Custom Title"
    custom_label = "Custom Label"
    
    fig = method.solve(f, interval, title=custom_title, label=custom_label)
    
    ax = fig.axes[0]
    assert ax.get_title() == custom_title
    
    lines = ax.get_lines()
    # The first line should be the function plot
    assert lines[0].get_label() == custom_label
