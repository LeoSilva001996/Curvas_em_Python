import numpy as np
import pandas as pd
import numpy.polynomial.polynomial as ply

def lagrange_ln(x, y):
    n = len(x)  # grau do polinomio n-1
    l = np.zeros(n)
    L = np.zeros((n, n))
    for m in range(n):
        P = [1]
        for k in range(n):
            if k != m:
                P = poly.polymul(P, [-x[k], 1]) / (x[m] -x[k])
        L[m,:] = P
        l += y[m] * P
    return l, L


x = [-1, 0, 3]
y = [15, 8, -1]
l, L= lagrange_ln(x, y)

Tabela = pd.DataFrame(L)
print('1_2 =', 1)
print('L=')