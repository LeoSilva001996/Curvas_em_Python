import numpy as np
import math
f = lambda x: x**2
a = 2; b = 3; N = 5
x = np.linspace(a,b,N+1)
y = f(x)
dx = (b-a)/N
x_medio = np.linspace(dx/2,b - dx/2,N)
soma_retangulo = np.sum(f(x_medio) * dx)
print("Integral:",soma_retangulo)

