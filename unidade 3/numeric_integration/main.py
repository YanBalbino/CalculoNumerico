from methods import Trapezoidal
import math

def f(x):
    return math.exp(x**2)

a = 1.2
b = 1.6

print("Integral de f(x) por trapézio repetido: ",
       Trapezoidal.method(5, a, b, f))

