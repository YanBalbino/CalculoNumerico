# fazer gráfico depois
from math import fabs


def method(f, a, b, precisao):
    x = (a + b) / 2
    it = 1

    if f(x) == 0:
            return [x, it]

    while abs(b - a) > precisao or fabs(f(x)) > precisao:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        it += 1
        x = (a + b) / 2
    
    return [x, it]