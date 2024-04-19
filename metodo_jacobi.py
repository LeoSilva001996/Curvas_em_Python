import numpy as np

A = np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
b = np.array([1., 0, 0])
def sol_Jacobi(A, b, x0, kmax=100):
    #M= diagonal de A
    d = np.diag(A)
    for k in range(kmax):
        r = b -A@x0
        print('r=', r)
        p = r/d #p =r[i]/A[i, i]
        if np.linalg.norm(p) <1e-2 + 1e-2 * np.linalg.norm(x0):
            break
        x0 += p
        print('k=', k)
        print('x_k=', x0)
    return x0
x0 = np.zeros(3)
kmax = 3
sol_Jacobi(A, b, x0, kmax)