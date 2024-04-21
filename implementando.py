import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
#solução do sistema linear pelo método de Eliminação de Gauss
def SubRet(U,c):
  n=c.size
  x=np.zeros(n)
  for i in reversed(range(n)):
    x[i] = (c[i] -U[i,i+1:]@x[i+1:])/U[i,i]
  return x

def ElimGauss(A, b):
  U = np.copy(A)
  c = np.copy(b)
  n = c.size
  for j in range(n-1):
    for i in range(j+1,n):
      m = U[i,j]/U[j,j]
      U[i,j:] -= m*U[j,j:]
      c[i] -= m*c[j]
  x = SubRet(U,c)
  return x
#dados do problema
x=np.arange(1.0,8.0)
y=np.array([1.,3.,2.,4.,2.,5.,4.])
#solução do ajuste linear

def Ajuste_Linear(x,y):
# definir a matriz A
  m = x.size
  A = np.ones((m,2))
  for k in reversed(range(m)):
    A[k,0] = x[k]
  x=ElimGauss(A.T@A,A.T@y)
  return x
#solução
# obter os coeficientes da função y =b +ax
p=Ajuste_Linear(x,y) 
plt.plot(x, y, "o")
# obtendo os valores da reta ajustada
x_novo=np.arange(0.0,9.1,0.1)
plt.style.use("seaborn-poster")
plt.plot(x_novo, np.polyval(p, x_novo))
plt.title(f"Ajuste Linear")
plt.tight_layout()
plt.show()