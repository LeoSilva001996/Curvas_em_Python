import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

# Define os parâmetros
# EDO
f = lambda t, s: np.exp(-t)
#Tamanho do espaçamento
h = 0.1
#tamanho discretizado
l = 1 # Define the upper bound of the range for t
t = np.arange(0, l + h, h)

# Condição inicial
s0=-l
# Metodo Expicito de Euler
s = np.zeros(len(t))
s[0] = s0

for i in range(0,len(t) -l):
  s[i + l] = s[i] + h*f(t[i], s[i])

# gráfico
plt.figure(figsize = (12, 8))
plt.plot(t, s, "r--", label="Aproximação")
plt.plot(t, -np.exp(-t), "g", label="Exato")
plt.title("Solução exata e Aproximção de EDO")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.lagend(loc="lower ringht")
plt.show()