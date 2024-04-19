import numpy as np

A = np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
b = np.array([1., 0, 0])

def SubSuc(L, b):
    n = b.size
    c = np.zeros(n)
    for i in range(n):
        c[i] = (b[i] - L[i, :i] @ c[:i]) / L[i, i]
    return c

def sol_Gaussseideil(A, b, x0, kmax=100):
    # M = tridiagonal de A
    M = np.tril(A)
    for k in range(kmax):
        print('k=', k)
        r = b - A @ x0
        print('r=', r)
        p = SubSuc(M, r)  # solução por substituição sucesssivas
        print('p=', p)
        if np.linalg.norm(p) < 1e-9 + 1e-9 * np.linalg.norm(x0):
            break
        x0 += p
        print('k=', k)
        print('x_k=', x0)
    return x0

x0 = np.zeros(3)
kmax = 3
sol_Gaussseideil(A, b, x0, kmax)