from numeric_integration.methods import Trapezoidal
import math

def f(x):
    return x

a = 1
b = 4

print("Integral de f(x) por trapézio repetido: ",
       Trapezoidal.method(5000, a, b, f))

