from math import fabs


def method(f, a, b, x0, e1, e2):
    if (x0 < a) or (x0 > b): # se o chute inicial estiver fora do intervalo
        return [None, None]
    
    if (f(a) * f(b) > 0): # se não houver raiz no intervalo
        return [None, None]

    if fabs(f(x0)) < e1: # se o chute inicial for a raiz
        return [x0, 1]
    
    k = 1
    xk1 = x0 - f(x0) / df_dx(f, x0)

    while (fabs(f(xk1)) > e1) and (fabs(xk1 - x0) > e2):
        x0 = xk1
        xk1 = x0 - f(x0) / df_dx(f, x0)
        k += 1

    return [xk1, k]


# derivada por diferença finita 'progressiva'

def df_dx(f, x):
    h = 0.000001 # 10^-6
    return (f(x + h) - f(x)) / h 
