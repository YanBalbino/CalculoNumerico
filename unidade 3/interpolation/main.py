import methods.Lagrange as Lagrange
import methods.Newton as Newton
import time
import matplotlib.pyplot as plt


def main():
    # tabela de valores

    x = [1, 2, -3, 4, 5] 
    fx = [-3, 5, 7, 8, 10]
    valor = 1 # valor a ser interpolado

    start_time = time.time()
    print("Valores interpolados:\nLagrange: ", Lagrange.polynomial(x, fx, valor))
    lagrange_time = time.time() - start_time

    start_time = time.time()
    print("Newton: ", Newton.polynomial(x, fx, valor))
    newton_time = time.time() - start_time

    # tempo normalmente buga

    print("Tempo de execução de Newton: ", newton_time)
    print("Tempo de execução de Lagrange: ", lagrange_time)

    # gráfico da função desconhecida

    plt.plot(x, fx, 'bo-')
    plt.grid(True)
    plt.xlabel("xi")
    plt.ylabel("f(xi)")
    plt.show()


if __name__ == "__main__":
    main()



   