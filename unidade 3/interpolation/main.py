import interpolation.methods.Lagrange as Lagrange
import interpolation.methods.Newton as Newton
import math
import time
import matplotlib.pyplot as plt

x = [1, 2, -3, 4, 5]
fx = [-3, 5, 7, 8, 10]
valor = 1
start_time = time.time()
print("Valores interpolados:\nLagrange: ", Lagrange.polinomio(x, fx, valor))
lagrange_time = time.time() - start_time

start_time = time.time()
print("Newton: ", Newton.polinomio(x, fx, valor))
newton_time = time.time() - start_time

plt.plot(x, fx, 'bo-')
plt.grid(True)
plt.xlabel("xi")
plt.ylabel("f(xi)")
plt.show()



   