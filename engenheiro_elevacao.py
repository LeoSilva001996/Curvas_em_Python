import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import pandas as pd
 
def n_newton(x,y):
  """
  n e DD
  """
  N = len(y)
  DD = np.zeros([N, N])
  # A primeira coluna é y
  DD[:,0] = y
  for j in range(1,N):
    for i in range(N-j):
      DD[i,j] = (DD[i+1,j-1]-DD[i,j-1])/(x[i+j]-x[i])
  a = DD[0,:]# coeficientes do polinômio de newton
  n=a[N-1]
  for k in reversed(range(N-1)):
    n = poly.polyadd(a[k] , poly.polymul(n,[-x[k],1]))
  return n,DD
x=np.arange(1.0,8.0)
y=np.array([1.,3.,2.,4.,2.,5.,4.])
n,DD =n_newton(x,y)
print('coeficientes de n na forma de newton é',DD[0,:])
x_new = np.arange(1.0, 7.1, 0.1)
n_6=poly.Polynomial(n)
Tabela=pd.DataFrame(DD)
print(Tabela)
print('o valor da elevação para x=3,5 é igual a n_6(3.5)=',n_6(3.5))
plt.plot(x_new,n_6(x_new),x,y,'ro')
plt.show()