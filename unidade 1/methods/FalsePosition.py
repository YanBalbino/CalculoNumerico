# fazer gráfico depois
from math import fabs


def method(f, a, b, precisao, max_iter):

    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    it = 1

    if f(x) == 0:
            return [x, it]
    
    while fabs(b - a) > precisao or fabs(f(x)) > precisao:
        if (it == max_iter): # se não controlar ele loopa
            return [x, it]
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        it += 1
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

    return [x, it]