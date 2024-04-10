def method(qt_div, a, b, f):

    if qt_div == 1:
        return (b - a) * (f(a) + f(b)) / 2

    h = (b - a) / qt_div # (b - a) / deltaX ou espacamento entre os pontos
    sum = 0
    for i in range(qt_div):
        sum += f(a + i * h) # f(a) + f(a + h) + f(a + 2h) + ... + f(b - h) + f(b)
    return h * sum
    