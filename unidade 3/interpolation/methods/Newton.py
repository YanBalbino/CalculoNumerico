
def polynomial(x, fx, valor):
    n = len(x)
    coeficientes = [fx[0]]

    for i in range(1, n):
        coef = diferenca_dividida(x[:i+1], fx[:i+1]) # aplicação da diferença dividida
        coeficientes.append(coef)

    resultado = coeficientes[0]

    for i in range(1, n):
        termo = coeficientes[i]
        for j in range(i):
            termo *= (valor - x[j])

        resultado += termo

    return resultado

# função recursiva que calcula a diferença dividida

def diferenca_dividida(x, fx):
    n = len(x)
    
    if n == 1:
        return fx[0]
    else:
        return (diferenca_dividida(x[1:], fx[1:]) - 
        diferenca_dividida(x[:-1], fx[:-1])) / (x[-1] - x[0])