
#ver aulas depois
def method(qt_div, a, b, f):
    h = (b - a) / qt_div
    x = a
    y = 0
    for i in range(qt_div):
        k1 = h * f(x)
        k2 = h * f(x + h / 2)
        k3 = h * f(x + h / 2)
        k4 = h * f(x + h)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y