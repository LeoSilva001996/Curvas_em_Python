import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1.0, 1.1, 0.1)
n = 6 # grau do monomio n-1
m = len(x)
phik = np.zeros((m, n))
tipos = ["k-", "b-", "g-", "r-", "y-", "m-"]
legenda = []
for i in range(n):
    legenda.append('$\phi_{'+str(i) +"}$")
    plt.style.use("seaborn-poster")
    fig = plt.figure(figsize = (10, 8))
for k in range(n):
    phik[:,k] = x ** k
    plt.plot(x, phik[:,k], tipos[k], label= legenda[k])
plt.title("Monômios Básico: $ \phi_{k}(x_j)$")
plt.xlabel("$x$")
plt.ylabel("$x^{k}$")
plt.legend()
plt.show()
