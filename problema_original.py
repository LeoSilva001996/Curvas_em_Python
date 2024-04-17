import numpy as np

a = np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
b = np.array([1., 0, 0])

def SubSuc(L, b):
    n =b.size
    c =np.zeros(n)
    for i in range(n):
        c[i] = (b[i] - L[i,:i] @c [:i]) / L[i, i]
    return c

def SubRet(U, c):
    n = c.size
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (c[i] -U[i, i + 1:] @ x[i + 1:] / U[i, i])
    return x

def Dec_Lu(A):
    n = A.shape[0]
    U = np.copy(A)
    L = np.identity(n)
    for j in range(n-1):
        for i in range(j + 1,n):
            m = U[i, j] / U[j, j]
            U[i, j:] -= m* U[j, j:]
            L[i, j] = m
    return L, U

def solucao_Lu(A, b):
    L, U = Dec_Lu(A)
    c = SubSuc(L, b)
    x = SubRet(U, c)
    return x

print('x=',solucao_Lu(a, b))