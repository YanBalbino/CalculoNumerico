from math import fabs


def method(f, a, b, x0, x1, e1, e2):
    if (x0 < a) or (x0 > b): # se o chute inicial estiver fora do intervalo
        return [None, None]
    
    if (f(a) * f(b) > 0): # se não houver raiz no intervalo
        return [None, None]

    if (fabs(f(x0)) < e1) or (fabs(x1 - x0) < e2): # se o chute inicial for a raiz
        return [x1, 0]
    
    k = 1

    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

    while (fabs(f(x2)) > e1) and (fabs(x2 - x1) > e2):
        x0 = x1
        x1 = x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        k += 1

    return [x2, k]
    