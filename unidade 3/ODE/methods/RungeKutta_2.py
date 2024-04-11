def method(x0, y0, f, valor, h):
    h = h
    x = x0
    y = y0
    
    while x < valor:
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        y += h * k2
        x += h
    return y