import numpy as np

a = np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
b = np.array([1., 0, 0])
def GaussJordan(A, b):
    R = np.copy(A)
    d = np.copy(b)
    n = d.size
    for k in range(n):
        d[k] /= R[k, k]
        R[k, :] /= R[k, k]
        for i in range(n):
            if i != k:
                m = R[i, k]
                R[i, k + 1:] -= m * R[k, k + 1:]
                d[i] -= m * d[k]
                R[i, k] = 0
    return d

print('x=', GaussJordan(a, b))