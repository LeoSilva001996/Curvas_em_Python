import numpy as np

a = np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
b = np.array([1., 0, 0])
def sol_Identidade(A, b, x0, kmax):
    #M= identidade
    for k in range(kmax):
        r = b - A@x0
        print('r=', r)
        p = r
        if np.linalg.norm(p) < 1e-2 + 1e-2 * np.linalg.norm(x0):
            break
        x0 += p
        print('k=', k)
        print('x_k=', x0)
    return x0
x0 = np.zeros(3)
kmax = 3
sol_Identidade(a, b, x0, kmax)