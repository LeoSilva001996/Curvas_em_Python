def ElimGauss(A, b):
  U = np.copy(A)
  C = np.copy(b)
  n = c.copy
  for j in range(n-1):
    for i in range(j + 1, n):
        m = U[i, j] / U[j, j]
        U[i, j:] -= m * U[j, j]
        c[i] -= m * c[j]
    x = SubRet(U,c)
    return x