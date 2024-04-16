import methods.Bisection as Bisection
import methods.FalsePosition as FalsePosition
import methods.FixedPoint as FixedPoint
import methods.Newton as Newton
import methods.Secant as Secant
import math

def f(x):
    return math.cos(x) - x

# função de convergência correta para a função f(x) (M.P.F)
# calculada previamente
def g(x):
    return math.cos(x)

def m1():
    a = 0
    b = 90
    precisao = 0.0001

    result = Bisection.method(f, a, b, precisao)

    print("(Bissecção)")
    print("Raiz aproximada:", result[0], "em", result[1], "iterações\n")

def m2():
    a = 1
    b = 3
    precisao = 0.01

    result = FalsePosition.method(f, a, b, precisao, 30)

    print("(Falsa Posição)")
    print("Raiz aproximada:", result[0], "em", result[1], "iterações\n")

def m3():
    a = 0
    b = 90
    x0 = 45
    e1 = 0.00001
    e2 = 0.00001

    result = FixedPoint.method(f, g, a, b, x0, e1, e2)

    print("(Ponto Fixo)")
    print("Raiz aproximada:", result[0], "em", result[1], "iterações\n")

def m4():
    a = 0
    b = 90
    x0 = 45
    e1 = 0.00001
    e2 = 0.00001

    result = Newton.method(f, a, b, x0, e1, e2)
    print("(Newton)")
    print("Raiz aproximada:", result[0], "em", result[1], "iterações\n")

def m5():
    a = 0
    b = 90
    x0 = 45
    x1 = 50
    e1 = 0.00001
    e2 = 0.00001

    result = Secant.method(f, a, b, x0, x1, e1, e2)
    print("(Secante)")
    print("Raiz aproximada:", result[0], "em", result[1], "iterações\n")

def main():
    m1()
    m2()
    m3()
    m4()
    m5()

if __name__ == "__main__":
    main()