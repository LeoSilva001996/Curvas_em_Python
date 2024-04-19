import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
 
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
 
def monomio(x,y):
   # definir a matriz A
   A = np.vander(x, increasing=True)
   cj = ElimGauss(A,y)
   return cj
 
x=np.arange(1.0,8.0)
y=np.array([1.,3.,2.,4.,2.,5.,4.])
coef=monomio(x,y)
print("coeficientes de p é",coef)
x_new = np.arange(1.0, 7.1, 0.1)
p=poly.Polynomial(coef)
print('o valor da elevação para x=3,5 é igual a p(3.5)=',p(3.5))
plt.plot(x_new,p(x_new),x,y,'ro')
plt.show()