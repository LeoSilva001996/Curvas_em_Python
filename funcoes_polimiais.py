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
#Ajuste de polinômios

def ajuste_poli(x,y,n):
    m = x.size
    A = np.ones((m,n+1))
    for k in reversed(range(n)):
        A[:,k] = x**(n-k)
    p = ElimGauss(A.T@A, A.T@y)
    return p

for i in range(1,5):
    p=ajuste_poli(x,y,2*i -1)
    plt.subplot(2,2,i)
    plt.plot(x, y, "o")
    x_novo=np.arange(0.0,8.1,0.1)
    plt.plot(x_novo, np.polyval(p, x_novo))
    plt.title(f"Ordem da Polinômio {2*i-1}")
    plt.tight_layout()
    plt.show()