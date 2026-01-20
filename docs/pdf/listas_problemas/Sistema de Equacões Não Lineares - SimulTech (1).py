import numpy as np
from scipy.optimize import fsolve

def nlsistema(variaveis): # sistema que queremos resolver 
    (x,y) = variaveis     # variáveis do sistema
    eq1 = x * y - 2 * y - 2**x # equação 1
    eq2 = np.log(x)-y-np.cos(x)# equação 2
    return [eq1,eq2]

s0 = np.array([1,1])      # estimativa inicial
s = fsolve(nlsistema,s0)  # chamada de fsolve
print(s)
