# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:48:10 2019

Lista 08 - Equações diferenciais ordinárias

Questao 3

@author: Ubiratan
"""
def inicializar():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    h = float(input("Digite o valor de h: "))
    t0 = float(input("Digite o valor de t0: "))
    x0 = float(input("Digite o valor de x0: "))
    y0 = float(input("Digite o valor de y0: "))
    return [a, b, h, t0, x0, y0]
    
def quantidade_pontos(a, b, h):
    return int((b - a) / h)

def euler_explicito(n, h, t, x, y):
    for i in range(1, n + 1):
        t[i] = t[i-1] + h
        x[i] = x[i-1] - h * y[i-1]
        y[i] = (1 + h) * y[i-1] - h * (10 - x[i-1])
    return t, x, y

def executar_euler_explicito(n, h, t, x, y):
    print("Método de Euler Explicito")
    t, x, y = euler_explicito(n, h, t, x, y)
    for i in range(0, n+1):
        print("%d\t%9.3f\t%9.9f\t%9.9f" %(i, t[i], x[i], y[i]))
    print()
    return None    

def euler_implicito(n, h, t, x, y):
    for i in range(1, n+1):
        t[i] = t[i-1] + h
        y[i] = (y[i-1] + h * (1 - x[i-1])) / (1 + h**2 - h)
        x[i] = x[i-1] + h * y[i]
    return t, x, y

def executar_euler_implicito(n, h, t, x, y):
    print("Método de Euler Implicito")
    t, x, y = euler_implicito(n, h, t, x, y)
    for i in range(0, n+1):
        print("%d\t%9.3f\t%9.9f\t%9.9f" %(i, t[i], x[i], y[i]))
    print()
    return None    

def crank_nicolson(n, h, t, x, y):
    return t, x, y

def executar_crank_nicolson(n, h, t, x, y):
    return None    
    
def principal():
    dados = inicializar()
    h = dados[2]
    n = quantidade_pontos(dados[0], dados[1], dados[2])
    t = [0.0]*(n+1)
    x = [0.0]*(n+1)
    y = [0.0]*(n+1)
    t[0] = dados[3] #t0
    x[0] = dados[4] #x0
    y[0] = dados[5] #y0
    
    executar_euler_explicito(n, h, t, x, y)
    executar_euler_implicito(n, h, t, x, y)
    
# principal
principal()   
    
    

