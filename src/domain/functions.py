import sympy as sp

def function_01(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = e^-x - x
    """
    return sp.exp(-x) - x

def function_02(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = -0.5x^2 + 2.5x + 4.5
    Referência: Chapra & Canale (2008)
    """
    return -0.5 * x**2 + 2.5 * x + 4.5

def function_03(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = 5x^3 - 5x^2 + 6x - 2
    Referência: Chapra & Canale (2008)
    """
    return 5 * x**3 - 5 * x**2 + 6 * x - 2

def function_04(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = -12 - 21x + 18x^2 - 2.75x^3
    Referência: Chapra & Canale (2008)
    """
    return -12 - 21 * x + 18 * x**2 - 2.75 * x**3

def function_05(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = sin(x) - x^3
    Referência: Chapra & Canale (2008)
    """
    return sp.sin(x) - x**3

def function_06(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = ln(x^4) - 0.7
    Note: Domain x != 0
    Referência: Chapra & Canale (2008)
    """
    return sp.log(x**4) - 0.7

def function_07(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = (0.8 - 0.3x) / x
    Note: Domain x != 0
    Referência: Chapra & Canale (2008)
    """
    return (0.8 - 0.3 * x) / x

def function_08(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = sin(10x) + cos(3x)
    Referência: Chapra & Canale (2008)
    """
    return sp.sin(10 * x) + sp.cos(3 * x)

def function_09(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = e^x - 3|x|
    Referência: Freitas (2000)
    """
    return sp.exp(x) - 3 * sp.Abs(x)

def function_10(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = sin(x) - x/2
    Referência: Freitas (2000)
    """
    return sp.sin(x) - x / 2

def function_11(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = 2^x - cos(x) - 1
    Referência: Freitas (2000)
    """
    return 2**x - sp.cos(x) - 1

def function_12(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = e^x + x^2 - 2
    Referência: Freitas (2000)
    """
    return sp.exp(x) + x**2 - 2

def function_13(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = 5sin(x^2) - exp(x/10)
    Referência: Octave (2018)
    """
    return 5 * sp.sin(x**2) - sp.exp(x / 10)

def function_14(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = e^(-x^2) - x
    Referência: Octave (2018)
    """
    return sp.exp(-(x**2)) - x

def function_15(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = e^x * sin(x) - 1
    Referência: UFSC (2018)
    """
    return sp.exp(x) * sp.sin(x) - 1

def function_16(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = x * ln(x) - 3.2
    Note: Domain x > 0
    Referência: Humes (1984)
    """
    return x * sp.log(x) - 3.2

def function_17(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = x - cos(x)
    Referência: Aula-Zeros (Material Didático)
    """
    return x - sp.cos(x)

def function_18(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = x * tan(x) - 1
    Referência: Aula-Zeros (Material Didático)
    """
    return x * sp.tan(x) - 1

def function_19(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = 0.2x^2 + sin(x)
    Referência: Python/Colab (Fábio & Cinthia)
    """
    return 0.2 * x**2 + sp.sin(x)

def function_20(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = x^2 - 4x
    Referência: Python/Colab (Fábio & Cinthia)
    """
    return x**2 - 4 * x

def function_21(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = x^2 - cos(x)
    Referência: Python/Colab (Fábio & Cinthia)
    """
    return x**2 - sp.cos(x)

def function_22(x: sp.Symbol) -> sp.Expr:
    """
    f(x) = x^3 + sin(x)
    Referência: Python/Colab (Fábio & Cinthia)
    """
    return x**3 + sp.sin(x)
