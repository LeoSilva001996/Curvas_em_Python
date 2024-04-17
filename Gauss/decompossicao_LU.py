def Dec_Lu(A):
  n = A.shape[0]
  U = np.copy(A)
  L = np.identity(n-1)
  for j in range(n-1):
    for i in range(j + 1, n):
      m = U[i, j] / U[j, j]
      U[i, j:] -= m * U[j, j:]
      L[i, j] = m
  return L, U