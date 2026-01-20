import numpy as np

def pend(y, t, b, c): 
    teta, omega = y # y é o vetor [teta, omega]
    dydt = [omega, -b*omega - c*np.sin(teta)] # dydt é o vetor contendo as EDOs
    return dydt

# Constantes do sistema
b = 0.25
c = 5.0

# Condições iniciais
# é assumido que o pêndulo é quase vertical com teta(0)=pi-0,1 e está inicialmente em repouso, de forma que omega(0)=0 
y0 = [np.pi - 0.1, 0.0] 
t = np.linspace(0, 10, 101) # Será gerada uma solução com 101 amostras uniformemente espaçadas no intervalo 0 <= t <= 10

from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(b, c)) # Chamada de odeint para gerar a solução. Para fornecer b e c para pend é usado a argumento args
print(sol) # A solução é uma matriz(101,2). A primeira coluna é teta(t), e a segunda é omega(t)

from pandas import DataFrame # Impressão dos resultado no Excel
tempo = t
teta = sol[:,0]
omega = sol[:,1]
df = DataFrame({"a": tempo, 'b': teta, 'c': omega})
df.to_excel('tetaomega.xlsx', sheet_name='Sheet1', index=False)

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='teta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
