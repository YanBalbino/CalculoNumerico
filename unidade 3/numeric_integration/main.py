from methods import Trapezoidal
import math


def f(x):
    return math.exp(x**2)

def main():
    # intervalo de integração

    a = 1.2
    b = 1.6

    # quantidade de trapézios/divisões do intervalo
    qt_div = 5

    print("Integral de f(x) por trapézio repetido: ",
        Trapezoidal.method(qt_div, a, b, f))
    

if __name__ == "__main__":
        main()
