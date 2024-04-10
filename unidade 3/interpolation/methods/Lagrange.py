
def polinomio(x, fx, valor): 
    qt_pontos = len(x) # número de pontos
    pn_x = 0.0 # resultado do polinômio em x
    
    for i in range(qt_pontos): 
        L = 1.0 # valor mínimo do L
        for j in range(qt_pontos):
            if j != i: 
                L *= (valor - x[j]) / (x[i] - x[j]) # produtório dos termos de Ln(x)
        pn_x += fx[i] * L  # somatório de fxi * Li(x)

    return pn_x

