import numpy as np
import math 
f = lambda x: x**2
a = 2; b = 3; N = 5 
x = np.linspace(a,b,N+1)
y = f(x)
y_maior = y[1:]
y_menor = y[:-1]
dx = (b-a)/N
soma_trapezio = (dx/2) * np.sum(y_maior + y_menor)
print("Integral:",soma_trapezio)