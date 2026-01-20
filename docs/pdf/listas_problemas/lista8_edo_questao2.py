# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:48:10 2019

Lista 08 - Equações diferenciais ordinárias

Questao 2

@author: Ubiratan
"""
def inicializar():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    h = float(input("Digite o valor de h: "))
    t0 = float(input("Digite o valor de t0: "))
    y0 = float(input("Digite o valor de y0: "))
    t1 = t0 + h
    y1 = (y0 * (1 - h/2) + h) / (1 + h/2)  #crank_nicolson
    return [a, b, h, t0, y0, t1, y1]
    
def quantidade_pontos(a, b, h):
    return int((b - a)/h)

def regra_do_ponto_medio(n, h, t, y):
    for i in range(2, n+1):
        t[i] = t[i-1] + h
        y[i] = -2 * h * y[i-1] + y[i-2] + 2 * h           
    return t, y

def executar_regra_do_ponto_medio(n, h, t, y):
    print("Método da regra do ponto médio")
    t, y = regra_do_ponto_medio(n, h, t, y)
    for i in range(0, n+1):
        print("%d\t%9.3f\t%9.9f" %(i, t[i], y[i]))
    print()
    return None    

def regra_de_simpson(n, h, t, y):
    for i in range(2, n+1):
        t[i] = t[i-1] + h
        y[i] = (-4/3 * h * y[i-1] + (1 - h/3) * y[i-2] + 2 * h) / (1 + h/3)          
    return t, y

def executar_regra_do_simpson(n, h, t, y):
    print("Método da regra 1/3 de Simpson")
    t, y = regra_de_simpson(n, h, t, y)
    for i in range(0, n+1):
        print("%d\t%9.3f\t%9.9f" %(i, t[i], y[i]))
    print()
    return None    

def regra_de_adams_moulton(n, h, t, y):
    for i in range(2, n+1):
        t[i] = t[i-1] + h
        y[i] = ((1 - 8 * h / 12) * y[i-1] + h/12 * y[i-2] + h) / (1 + 5 * h /12)          
    return t, y

def executar_regra_de_adams_moulton(n, h, t, y):
    print("Método da regra de adams-moulton")
    t, y = regra_de_adams_moulton(n, h, t, y)
    for i in range(0, n+1):
        print("%d\t%9.3f\t%9.9f" %(i, t[i], y[i]))
    print()
    return None

def regra_de_adams_bashford(n, h, t, y):
    for i in range(2, n+1):
        t[i] = t[i-1] + h
        y[i] = y[i-1] * (1 - 3 * h / 2) + y[i-2] * h/2 + h
    return t, y

def executar_regra_de_adams_bashford(n, h, t, y):
    print("Método da regra de adams-bashford")
    t, y = regra_de_adams_bashford(n, h, t, y)
    for i in range(0, n+1):
        print("%d\t%9.3f\t%9.9f" %(i, t[i], y[i]))
    print()
    return None
    
def principal():
    dados = inicializar()
    h = dados[2]
    n = quantidade_pontos(dados[0], dados[1], dados[2])
    t = [0.0]*(n+1)
    y = [0.0]*(n+1)
    t[0] = dados[3] #t0
    y[0] = dados[4] #y0
    t[1] = dados[5] #t1
    y[1] = dados[6] #y1

    executar_regra_do_ponto_medio(n, h, t, y)
    executar_regra_do_simpson(n, h, t, y)
    executar_regra_de_adams_moulton(n, h, t, y)
    executar_regra_de_adams_bashford(n, h, t, y)
    
# principal
principal()   
    
    

