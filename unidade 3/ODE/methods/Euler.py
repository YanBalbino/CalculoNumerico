def method(x0, y0, f, valor, h):
    h = h
    x = x0
    y = y0
    
    while x < valor:
        y += h * f(x, y)
        x += h
    return y