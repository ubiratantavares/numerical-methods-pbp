import pytest
from src.domain.errors.errors import absolute_error, relative_error, NumericalError, ConvergenceError

def test_absolute_error():
    assert absolute_error(10.0, 9.5) == 0.5
    assert absolute_error(10.0, 10.5) == 0.5
    assert absolute_error(0.0, 0.0) == 0.0
    assert absolute_error(-5.0, -4.0) == 1.0

def test_relative_error():
    assert relative_error(10.0, 9.0) == 0.1
    assert relative_error(10.0, 11.0) == 0.1
    assert relative_error(-10.0, -9.0) == 0.1

def test_relative_error_zero_division():
    with pytest.raises(ZeroDivisionError):
        relative_error(0.0, 1.0)

def test_custom_exceptions():
    with pytest.raises(NumericalError):
        raise NumericalError("Generic numerical error")
    
    with pytest.raises(ConvergenceError):
        raise ConvergenceError("Convergence failed")
    
    # Verify inheritance
    with pytest.raises(NumericalError):
        raise ConvergenceError("Inheritance check")
