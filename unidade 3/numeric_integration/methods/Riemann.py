
def method(qt_divisoes, a, b, f):
    h = (b - a) / qt_divisoes
    x = a
    integral = 0
    for i in range(qt_divisoes):
        integral += h * f(x)
        x += h
    return integral