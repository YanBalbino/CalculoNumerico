from math import fabs


def method(f, g, a, b, x0, e1, e2):

    if (x0 < a) or (x0 > b): # se o chute inicial estiver fora do intervalo
        return [None, None]

    if fabs(f(x0)) < e1: # se o chute inicial for a raiz
        return [x0, 1]
    
    k = 1
    x = g(x0)

    while (fabs(f(x)) > e1) and (fabs(x - x0) > e2): # enquanto não atingir a precisão
        x0 = x
        x = g(x)
        k += 1
    
    return [x, k]