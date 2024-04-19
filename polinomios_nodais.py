import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
x=np.arange(-1.0,1.01,0.01)
x_no=[-1.,-0.5,0,0.5,1]
n=len(x_no) #grau do monomio n-1
#=======================================================
#configuração dos gráficos
#=======================================================
tipos=["k-","b-","g-","r-","y-","m-"]
legenda=[]
for i in range(n+1):
    legenda.append('$\pi_{'+str(i)+'}$')
plt.style.use("seaborn-poster")
fig = plt.figure(figsize = (10,8))
#=======================================================
#função nodal
#=======================================================
def nodal(x,k):
  coef=1
  for i in range(k):
     coef=(poly.polymul(coef,[-x[i],1]))
  n=poly.Polynomial(coef)
  return n
#gráficos do nodais
for k in range(n+1):
   pii =nodal(x_no,k)
   plt.plot(x,pii(x),tipos[k], label= legenda[k])
 
#==========================================================
#
y=np.zeros(n)
plt.plot(x_no,y,'ko')
#==========================================================
plt.title("Polinômios Nodais: $\pi_i(x) = \prod_{j=0}^{i-1}(x-x_j)$")
plt.xlabel("$x$")
plt.ylabel("$\pi_i(x)$")
plt.legend()
plt.show()